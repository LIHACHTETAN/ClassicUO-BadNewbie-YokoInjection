# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

With は、保存した同じオブジェクトに対する操作をまとめます。名前の先頭のドットは、そのオブジェクトのメンバーを指定します。With UO と With moduleName は、名前空間を明示的に選択する Basic 独自の拡張です。

## 正確な構文

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## パラメーター

- `objectExpression / UO / moduleName` — 対象は必須です。List()、Dictionary() などのネイティブオブジェクト、それを持つ変数、またはオブジェクトを返す関数を指定します。式は入口で一度だけ評価され、空の本体でも評価されます。このエンジンでは数値、文字列、配列、Unit は対象にできません。同名のローカルオブジェクト変数はモジュールより優先されます。
- `.Method(arguments) / .field` — オブジェクトのメソッドには括弧が必要です。.Add(value)、.Item(index)、.Count() の引数と戻り値は通常どおりです。Basic.List／Basic.Dictionary を参照してください。任意のオブジェクトフィールドやプロパティはここでは未対応です。モジュールではアクセス可能な .field と .Procedure(arguments) を使えますが、Private の制限は残ります。With UO 内の .Command(...) は UO.Command(...) を意味します。外ではゲームコマンドに UO が必要です。
- `statements / End With` — 本体は空でも、呼び出し、代入、条件、正しく入れ子になったループやブロックを含んでも構いません。End With は必須です。本体の外で先頭ドットを使うことはできません。他のオブジェクトには完全な名前でアクセスできます。

## 戻り値

With 自体は値を返さない制御ブロックです。ID、Boolean、成功フラグは返しません。各メソッドには固有の戻り値があります。例の Return は Main から明示的に Integer を返します。127、28、72 は例の計算結果です。

## 動作

- 準備時にブロックを検証し、相対名を結び付けます。入口で式を評価し、現在の呼び出しにオブジェクト参照を保存します。元の変数に別の値を代入しても、この参照は変わりません。入口に戻ると再評価され、再帰呼び出しは別々の参照を持ちます。
- 内側の With の先頭式は外側の文脈で評価されます。内側の本体ではドットが内側のオブジェクトを指し、End With で外側に戻ります。Return、ループの移動、外向きの GoTo は、必要な Finally の実行後に離れたスコープを破棄します。With の本体への飛び込みは禁止です。
- 不適切な対象や不明なメソッドは false ではなくエラーです。Catch／On Error で処理できます。対象の評価が失敗した場合、On Error Resume Next はブロック全体を飛ばします。With は反復、待機、スレッド作成をしません。一時停止・停止のチェックは継続します。名前の結び付けは準備済みスクリプトに保存され、メソッドごとに対象式を評価し直しません。

## 使用例

### 1. 一度だけ評価する

```vb
# Choose は values を ByVal、calls を ByRef で受け取り、calls を 1 に増やして元のリストを返します。途中で values に新しいリストを代入しても、両方の .Add は保存したリストに 2 と 7 を追加します。Item の添字は 0 と 1 です。Main は 1*100+2*10+7=127 を返します。
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**パラメーターと実行の説明:**

Choose は values を ByVal、calls を ByRef で受け取り、calls を 1 に増やして元のリストを返します。途中で values に新しいリストを代入しても、両方の .Add は保存したリストに 2 と 7 を追加します。Item の添字は 0 と 1 です。Main は 1*100+2*10+7=127 を返します。

### 2. 入れ子と後処理

```vb
# groups は文字列キー "child" にリスト child を保存します。.Item("child") は外側の辞書からそのオブジェクトを取得します。内側の .Add(2) と Finally の .Add(7) がリストを変更します。End With の後の .Set("result",8) は辞書を操作します。Count() は 2、Item("result") は 8 を返すため、Main の結果は 28 です。
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**パラメーターと実行の説明:**

groups は文字列キー "child" にリスト child を保存します。.Item("child") は外側の辞書からそのオブジェクトを取得します。内側の .Add(2) と Finally の .Add(7) がリストを変更します。End With の後の .Set("result",8) は辞書を操作します。Count() は 2、Item("result") は 8 を返すため、Main の結果は 28 です。

### 3. モジュールと UO

```vb
# With Tools は .total、.AddAmount、.CountItems を Tools に限定します。total は 4 から始まり、AddAmount が amount=3 を ByVal で受け取って 7 になります。CountItems は二要素の配列を受け取り、With UO から UO.GetArrayLength(values) を呼び出して 2 を得ます。Main は 7*10+2=72 を返します。モジュールのアクセス制限も有効です。
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**パラメーターと実行の説明:**

With Tools は .total、.AddAmount、.CountItems を Tools に限定します。total は 4 から始まり、AddAmount が amount=3 を ByVal で受け取って 7 になります。CountItems は二要素の配列を受け取り、With UO から UO.GetArrayLength(values) を呼び出して 2 を得ます。Main は 7*10+2=72 を返します。モジュールのアクセス制限も有効です。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
