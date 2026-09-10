# Optional

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

パラメーターは SUB/FUNCTION にデータを渡します。ByRef は変更値を呼び出し元へ書き戻し、ByVal は呼び出し元の変数を保ちます。Optional は省略引数を補い、ParamArray は残りの引数を集めます。呼び出す命令ではなく宣言の修飾子です。

## 正確な構文

```text
Function Scale(ByVal value, Optional ByVal factor = 2)
Scale(3)
Scale(3, 4)
```

## パラメーター

- `name / As type` — name / As type：名前と省略可能な入力時の型変換です。引数は位置順で渡し、修飾子は宣言に書きます。
- `ByRef` — ByRef：書き込み可能な変数または既存の添字要素です。このエンジンは ByVal を省略した場合も書き戻し、VB.NET の既定とは異なります。リテラル、定数、計算式は一時値です。
- `ByVal` — ByVal：値のローカルコピーです。パラメーターの再代入は呼び出し元の変数を置換しません。配列とオブジェクトは参照を共有し、深いコピーではありません。
- `Optional / defaultValue` — Optional / defaultValue：末尾の引数を省略した場合に = 後の式を評価します。既定値を明示してください。ない場合は未初期化の Unit になります。
- `ParamArray` — ParamArray values()：最後のパラメーターが残りの値をゼロ個以上受け取ります。配列一つなら直接再使用し、スカラーなら新しい配列を作ります。GetArrayLength が長さを返します。

## 戻り値

修飾子は値を返しません。RETURN が結果を別に設定します。ByRef は引数の変更であり戻り値ではありません。RETURN のない SUB は Unit を返します。例の数値は計算結果で、TRUE/FALSE のフラグではありません。

## 動作

- 引数は左から右へ一度ずつ評価します。添字付き ByRef はコンテナーと添字／キーを保持し、別の引数がコンテナー変数を再代入しても書き戻し先は変わりません。
- 入口でローカルパラメーターを作ります。終了時は内部 FINALLY の後、パラメーター順に ByRef を書き戻します。本文からエラーで抜ける場合も同様です。同じ変数を二度渡しても二つのローカル値は即時連動せず、最後の書き戻しが残ります。
- ByVal は呼び出し元の変数の置換を防ぎますが、共有する配列やオブジェクト内部は変更できます。ReDim は新しいローカル参照を作ります。独立したデータには明示的なコピーが必要です。
- Optional は末尾から省略し、コンマ間の空引数は使えません。既定値は省略ごとに評価するエンジンの式でよく、VB.NET の定数である必要はありません。
- ParamArray はまとめたスカラーを元の変数へ書き戻しません。配列を明示して渡した場合、要素変更は呼び出し元にも見えます。別の ParamArray に渡しても入れ子は増えません。
- 意図を示すため ByRef と ByVal を明示してください。ユーザー手続きのスクリプト呼び出しの規則であり、組み込み命令の引数は各ページに説明があります。

## 使用例

### 1. 省略した係数と明示した係数

```vb
# Scale(3) は factor=2 で 6 を返し、Scale(3,4) は 4 で 12 を返します。Main は 6*100+12、Integer 612 を返します。
Option Explicit On
Function Scale(ByVal value, Optional ByVal factor = 2)
    Return value * factor
End Function
Sub Main()
    Return Scale(3) * 100 + Scale(3, 4)
End Sub
```

**パラメーターと実行の説明:**

Scale(3) は factor=2 で 6 を返し、Scale(3,4) は 4 で 12 を返します。Main は 6*100+12、Integer 612 を返します。

### 2. 既定式の評価時点

```vb
# Pick(5) は DefaultAmount を呼ばず 5 を返します。Pick() は一回呼び、calls=1、値は 7。Main は 5*100+7*10+1、Integer 571 を返します。
Option Explicit On
Module Counter
    Public Var calls = 0
End Module
Function DefaultAmount()
    Counter.calls += 1
    Return 7
End Function
Function Pick(Optional ByVal value = DefaultAmount())
    Return value
End Function
Sub Main()
    Var first = Pick(5)
    Var second = Pick()
    Return first * 100 + second * 10 + Counter.calls
End Sub
```

**パラメーターと実行の説明:**

Pick(5) は DefaultAmount を呼ばず 5 を返します。Pick() は一回呼び、calls=1、値は 7。Main は 5*100+7*10+1、Integer 571 を返します。

### 3. Optional、ByRef、As Integer

```vb
# value は 1 から始まります。Increase(value) は amount=2 を足して 3、Increase(value,4) は 4 を足して 7 を保存します。両パラメーターは Integer。Main は Integer 7 を返します。
Option Explicit On
Sub Increase(ByRef value As Integer, Optional ByVal amount As Integer = 2)
    value += amount
End Sub
Sub Main()
    Var value As Integer = 1
    Increase(value)
    Increase(value, 4)
    Return value
End Sub
```

**パラメーターと実行の説明:**

value は 1 から始まります。Increase(value) は amount=2 を足して 3、Increase(value,4) は 4 を足して 7 を保存します。両パラメーターは Integer。Main は Integer 7 を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: parameterName / parameterModifier / defaultValue
Runtime/SubrutineDefinition.cs: WritableParameters / RequiredArgumentCount / HasParamArray
Runtime/Interpreter.cs: VisitCall / CreateArgumentWriter / CallSubrutine / EvaluateInitializer
Runtime/IndexedValueSlot.cs: Read / Write
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/byref
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/byval
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/optional
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/paramarray
-->
