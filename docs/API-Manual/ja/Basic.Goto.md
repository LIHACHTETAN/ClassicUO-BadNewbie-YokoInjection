# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

GoTo は現在のプロシージャまたは関数内の名前付きラベルへ実行を移します。ラベルはコード上の位置であり、呼び出せるプロシージャではありません。通常の制御には If、ループ、Return を使います。

## 正確な構文

```text
GoTo label
label:
```

## パラメーター

- `label` — 同じプロシージャ内で独立した行の label: として宣言する識別名です。移動先は引用符、括弧、末尾のコロンを付けず GoTo label と書きます。前方・後方へ移動でき、大文字と小文字を区別しません。別プロシージャでは同名を使えます。名前のドットは許可されますが、モジュールのメンバーを意味しません。数値、計算式、別プロシージャのラベルは移動先として非対応です。

## 戻り値

GoTo と label: は値を返さず、成功を 1/0 や TRUE/FALSE で報告しません。例の Main は自分で計算した Integer -1、6、123 を明示的に Return します。

## 動作

- 準備時にラベルのアドレスを記録し、プロシージャ全体を読んでから移動先を解決します。実行時は解決済みアドレスを使い、ソースを再検索しません。変数値は維持され、過去の操作は取り消されません。
- 未知の移動先は SC009 となり、クライアントが実行を止めます。同じプロシージャの重複名は大文字小文字が違っても初期化前に SC021 となります。Include の診断は元ファイルと行番号を保ちます。余計な文字は警告になるため正確な構文を使ってください。
- 有効な Try から出る際は、内側から外側へ Finally を実行してから移動先へ進みます。同じ有効な Try 内の移動ではその状態を保ちます。Finally 内のエラーで移動先へ到達できない場合があります。
- ループや Try/Catch/Finally は通常の開始文から入ってください。途中へ移動しても飛ばした初期化や実行状態は復元されず、再開方法として使えません。ループ制御には Continue または Exit を使います。
- 後方移動に自動回数制限、タイムアウト、待機はありません。終了条件を明示的に変化させてください。通常の実行もラベルを通過するため、不要な部分は移動または Return で避けます。エラーハンドラーの設定は On Error です。

## 使用例

### 1. 前方へ分岐

```vb
# amount=0 では NoItems が result=-1 を設定し、Finished から -1 を返します。amount=4 なら通常経路で 40 を設定し、GoTo Finished が NoItems を飛ばします。どちらも Main 内のラベルで、関数呼び出しではありません。
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**パラメーターと実行の説明:**

amount=0 では NoItems が result=-1 を設定し、Finished から -1 を返します。amount=4 なら通常経路で 40 を設定し、GoTo Finished が NoItems を飛ばします。どちらも Main 内のラベルで、関数呼び出しではありません。

### 2. 回数を制限した反復

```vb
# attempt は 0 から始まり、判定前に増えます。Again と again は同じラベルです。3 回で 1、2、3 を加え、attempt<3 が偽になって 6 を返します。total はラベルより前で初期化されるため、移動してもゼロに戻りません。
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**パラメーターと実行の説明:**

attempt は 0 から始まり、判定前に増えます。Again と again は同じラベルです。3 回で 1、2、3 を加え、attempt<3 が偽になって 6 を返します。total はラベルより前で初期化されるため、移動してもゼロに戻りません。

### 3. 入れ子の Try から出る

```vb
# trace は 1 になり、GoTo Finished が trace=99 を飛ばします。内側の Finally が桁 2、外側が桁 3 を追加してから Finished に到達し、123 を返します。この移動では各 Finally を一度ずつ実行します。
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**パラメーターと実行の説明:**

trace は 1 になり、GoTo Finished が trace=99 を飛ばします。内側の Finally が桁 2、外側が桁 3 を追加してから Finished に到達し、123 を返します。この移動では各 Finally を一度ずつ実行します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
