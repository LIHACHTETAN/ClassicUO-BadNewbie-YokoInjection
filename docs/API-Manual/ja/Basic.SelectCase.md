# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Select Case は保存した値を候補と順番に比較し、一つの分岐を選びます。アイテム分類、スクリプトのモード、数値範囲に使えます。UO. を付けない Basic 文です。式の中のゲーム API 呼び出しには UO. が必要です。

## 正確な構文

```text
Select Case expression
    Case value1, value2
        statements
        Exit Select
    Case from To to
        statements
    Case Is >= value
        statements
    Case Else
        statements
End Select
```

## パラメーター

- `expression` — 必須の式。変数、リテラル、関数呼び出しを指定できます。空のブロックや Case Else だけでも、ブロックに入るたびに一度だけ評価します。
- `value / from / to` — Case には値、またはコンマ区切りの候補式を指定します。from To to は両端を含み、逆向き範囲は一致しません。下限比較が成立した場合だけ上限を評価します。関数引数内のコンマは候補の区切りではありません。
- `Is comparison value` — =、<>、<、<=、>、>= を使用します。Is は省略可能で、Case Is >= 5 と Case >= 5 は同じです。通常の値比較であり、オブジェクト型の検査ではありません。
- `Case Else` — 先行する Case に一致しない場合の任意の分岐。一つだけ、最後に置きます。省略すると、不一致時は End Select の後に進みます。
- `Exit Select` — 最も近い外側の Select Case を抜け、その End Select の後へ進みます。外側のループや手続きは終了しません。Select Case の外では読み込みエラーになります。

## 戻り値

Select Case、Case、End Select、Exit Select は値を返さず、TRUE や 1 と比較できません。例の関数は Return で明示的に String または Integer を返します。TRUE は数値 1、FALSE は 0 です。Case True は 1 に一致し、すべての非ゼロ値に一致するわけではありません。

## 動作

- 準備時に SelectInstruction、順序付きの CaseInstruction、解決済みジャンプを作ります。選択値は現在の関数呼び出し内に保存され、人工的なローカル変数を表示しません。再帰と入れ子は独立した値を持ち、再び入ると保存値を更新します。
- CaseMatches は左から右へ調べ、最初の一致で止まります。選んだ本体を一度実行し、残りの分岐を飛ばします。Case 内で変数が変わっても選択値を読み直しません。既に起きた副作用は取り消しません。
- 数値と文字列には通常のエンジン比較規則を適用し、文字列は大文字小文字を区別します。Option Compare Text と VB.NET の自動型変換は未実装です。数値と文字列を比較する場合は明示的に変換してください。
- End Select は必須です。最初の Case より前の実行文や、別の分岐にまたがる For/Next は許可しません。不正な構造は読み込みを止めます。GoTo で途中へ飛ばず、Select Case から入ってください。
- エラーは現在のハンドラーへ渡します。選択式の失敗時は On Error Resume Next がブロック全体を飛ばし、Case の失敗時は次の Case へ進みます。Resume は失敗した命令を再試行します。Exit Select は抜ける有効な Finally を実行します。命令間の停止・一時停止確認は維持され、待機やタイムアウトは追加しません。

## 使用例

### 1. 数量を分類する

```vb
# DescribeAmount は amount を ByVal で受け取ります。Case 0 は empty、1 To 4 は両端を含み small、Is >= 5 は large を返します。負数は Case Else に入ります。Main は -1、0、4、5 で呼び、negative:empty:small:large を作ります。これらの文字列はスクリプトが決める結果です。
Option Explicit On
Function DescribeAmount(ByVal amount)
    Select Case amount
        Case 0
            Return "empty"
        Case 1 To 4
            Return "small"
        Case Is >= 5
            Return "large"
        Case Else
            Return "negative"
    End Select
End Function

Sub Main()
    Return DescribeAmount(-1) & ":" & DescribeAmount(0) & ":" & DescribeAmount(4) & ":" & DescribeAmount(5)
End Sub
```

**パラメーターと実行の説明:**

DescribeAmount は amount を ByVal で受け取ります。Case 0 は empty、1 To 4 は両端を含み small、Is >= 5 は large を返します。負数は Case Else に入ります。Main は -1、0、4、5 で呼び、negative:empty:small:large を作ります。これらの文字列はスクリプトが決める結果です。

### 2. 呼び出しを観察する

```vb
# ReadMode は ByRef の reads を増やし、一度だけ 2 を返します。Candidate は checks を増やし value を返します。候補 1 は不一致、2 は一致し、3 は省略します。selected は 7、Main の戻り値は 1*100+2*10+7=127 です。ゲームへアクセスしません。
Option Explicit On
Function ReadMode(ByRef reads)
    reads += 1
    Return 2
End Function

Function Candidate(ByRef checks, ByVal value)
    checks += 1
    Return value
End Function

Sub Main()
    Dim reads = 0
    Dim checks = 0
    Dim selected = 0
    Select Case ReadMode(reads)
        Case Candidate(checks, 1)
            selected = -1
        Case Candidate(checks, 2), Candidate(checks, 3)
            selected = 7
        Case Else
            selected = -9
    End Select
    Return reads * 100 + checks * 10 + selected
End Sub
```

**パラメーターと実行の説明:**

ReadMode は ByRef の reads を増やし、一度だけ 2 を返します。Candidate は checks を増やし value を返します。候補 1 は不一致、2 は一致し、3 は省略します。selected は 7、Main の戻り値は 1*100+2*10+7=127 です。ゲームへアクセスしません。

### 3. 入れ子から抜ける

```vb
# route は harvest なので最初の候補に一致し trace=1 になります。内側の Case 2 で Exit Select を実行し、trace=99 は省略しますが Finally が 2 を付けます。外側の分岐が 3 を付けて 123 を返します。外側の Case Else は実行しません。route を別の文字列にすると -1 を返します。
Option Explicit On
Sub Main()
    Dim route = "harvest"
    Dim trace = 0
    Select Case route
        Case "harvest", "loot"
            trace = 1
            Select Case 2
                Case 2
                    Try
                        Exit Select
                        trace = 99
                    Finally
                        trace = trace * 10 + 2
                    End Try
            End Select
            trace = trace * 10 + 3
        Case Else
            trace = -1
    End Select
    Return trace
End Sub
```

**パラメーターと実行の説明:**

route は harvest なので最初の候補に一致し trace=1 になります。内側の Case 2 で Exit Select を実行し、trace=99 は省略しますが Finally が 2 を付けます。外側の分岐が 3 を付けて 123 を返します。外側の Case Else は実行しません。route を別の文字列にすると -1 を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
