# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Try は本体と呼び出した関数の実行エラーを扱います。Catch がエラーを受け取り、Finally が後処理を行い、Throw がエラーを発生または再送出します。API の 0 や false は通常の戻り値です。明示的に判定する必要があり、自動的に Catch には入りません。

## 正確な構文

```text
Try
    statements
Catch
    handlerStatements
Finally
    cleanupStatements
End Try
Catch name
Catch name As Exception
Catch name As String
Throw stringExpression
Throw
```

## パラメーター

- `Try / statements` — Try には一つの Catch、一つの Finally、または両方と End Try が必要です。入れ子にできます。本体が正常に終わると Catch を飛ばします。このサブセットでは複数の Catch、When フィルター、Exit Try は未実装です。
- `Catch / name / As type` — Catch の変数は省略できます。name を指定すると String のエラーメッセージを受け取ります。As String はその表現を示し、As Exception は互換表記です。.NET オブジェクトや型フィルターではありません。他の型は拒否されます。新しい名前は手続きのローカルとなり同名のグローバルを隠します。既存のローカルには型・Const の規則に従って代入します。Catch を通らない経路でも使うなら Try の前で String を宣言してください。
- `Finally / End Try` — Catch があれば Finally は省略でき、本体は空でも構いません。正常終了、エラー、Return、Exit Sub/Function、外向きのループ移動や GoTo では必要な Finally が実行されます。End Try は必須です。スクリプトのキャンセルは意図的に Catch とスクリプトの Finally を飛ばし、緊急停止の遅延を防ぎます。
- `Throw stringExpression` — Throw stringExpression はメッセージを一度だけ評価して新しいスクリプトエラーを発生させます。String が必要で、他の値は CStr で明示的に変換します。これは Basic の形式であり VB.NET の Throw New Exception(...) ではありません。ハンドラーがなければ現在の実行が失敗し、他のスクリプトすべてが止まるわけではありません。
- `Throw` — 引数なしの Throw は Catch とその入れ子のブロック内でのみ使えます。元のメッセージ、ファイル、行を保持したまま現在のエラーを再送出します。Catch から呼び出した補助関数には、この形式を使うための独自の Catch が必要です。

## 戻り値

Try/Catch/Finally と Throw は ID、数値、Boolean を返しません。Catch は name にメッセージを渡し、Throw は値を返さず制御を移します。例では Main から二つの String と Integer 13 を明示的に返します。中で呼ぶ API の戻り値の規則は変わりません。

## 動作

- 準備時にブロックを検証し、GoTo/On Error GoTo による Try、Catch、Finally への飛び込みを禁止します。生成器はハンドラーと後処理の位置を記録します。各呼び出しは固有の有効ハンドラーを持ち、エラーは最も近い適切な Catch に届きます。Catch 内のエラーはその Finally を通って外側へ進みます。構造化ハンドラーがなければ通常の On Error が適用される場合があります。
- Finally の間、保留中の戻り値、エラー、外向き移動を保存します。入れ子の後処理は内側から外側へ進みます。Finally の新しいエラーは保留中のエラーを置き換えます。Basic は Finally 内の Return や外向き移動も許可し、保留中の継続を置き換えます。これは VB.NET と異なります。再送出は補助関数を含む最初の失敗位置を保持します。
- 一時停止・停止のチェックは続きます。Try はスレッド、再試行、待機を作りません。準備済みの位置を再利用します。通常の条件は例外で代用せず直接判定してください。緊急停止はスクリプトの後処理を飛ばします。ホスト所有のリソースはエンジンの別の寿命管理に従います。

## 使用例

### 1. 引数を検証しメッセージを保存する

```vb
# CheckedAmount は Integer の amount=-2 を ByVal で受け取ります。負値なので Throw "amount must be non-negative" が発生します。Catch は String を problem に受け取り message にコピーします。As Exception はオブジェクトを作りません。Finally は finished=1 にします。Main は "amount must be non-negative:1" を返します。非負値なら通常どおり戻り Catch は実行されません。
Option Explicit On
Function CheckedAmount(ByVal amount As Integer) As Integer
    If amount < 0 Then
        Throw "amount must be non-negative"
    End If
    Return amount
End Function

Sub Main()
    Dim message=""
    Dim finished=0
    Try
        CheckedAmount(-2)
    Catch problem As Exception
        message=problem
    Finally
        finished=1
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**パラメーターと実行の説明:**

CheckedAmount は Integer の amount=-2 を ByVal で受け取ります。負値なので Throw "amount must be non-negative" が発生します。Catch は String を problem に受け取り message にコピーします。As Exception はオブジェクトを作りません。Finally は finished=1 にします。Main は "amount must be non-negative:1" を返します。非負値なら通常どおり戻り Catch は実行されません。

### 2. 外側へ再送出する

```vb
# 内側の Throw は "missing item" を発生させます。内側の Catch は trace=1 にし、引数なしの Throw が同じエラーを保持します。内側の Finally は 2 を付け、外側の Catch は outerProblem を message にコピーして 3 を付け、外側の Finally は 4 を付けます。Main は "1234:missing item" を返します。trace は実行順序でありエラーコードではありません。
Option Explicit On
Sub Main()
    Dim trace=0
    Dim message=""
    Try
        Try
            Throw "missing item"
        Catch problem
            trace=1
            Throw
        Finally
            trace=trace*10+2
        End Try
    Catch outerProblem
        message=outerProblem
        trace=trace*10+3
    Finally
        trace=trace*10+4
    End Try
    Return CStr(trace) & ":" & message
End Sub
```

**パラメーターと実行の説明:**

内側の Throw は "missing item" を発生させます。内側の Catch は trace=1 にし、引数なしの Throw が同じエラーを保持します。内側の Finally は 2 を付け、外側の Catch は outerProblem を message にコピーして 3 を付け、外側の Finally は 4 を付けます。Main は "1234:missing item" を返します。trace は実行順序でありエラーコードではありません。

### 3. 開始した各反復を片付ける

```vb
# number は 1、2、3 になります。total に加えるのは 1 だけです。Continue For は 2 を飛ばし、Exit For は 3 で終了します。開始した三つの Try はすべて Finally を実行し finished=3 になります。Main は 1*10+3=13 を返します。Finally にエラーは必須ではなく、ループの移動は反復の後処理を待ちます。
Option Explicit On
Sub Main()
    Dim total=0
    Dim finished=0
    For Var number=1 To 3
        Try
            If number=2 Then
                Continue For
            End If
            If number=3 Then
                Exit For
            End If
            total+=number
        Finally
            finished+=1
        End Try
    Next
    Return total*10+finished
End Sub
```

**パラメーターと実行の説明:**

number は 1、2、3 になります。total に加えるのは 1 だけです。Continue For は 2 を飛ばし、Exit For は 3 で終了します。開始した三つの Try はすべて Finally を実行し finished=3 になります。Main は 1*10+3=13 を返します。Finally にエラーは必須ではなく、ループの移動は反復の後処理を待ちます。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: tryStatement / catchClause / finallyClause / throwStatement
Analysis/TryStructureValidator.cs: VisitTryStatement / VisitSubrutine / VisitCatchClause / VisitThrowStatement
Runtime/Instructions/Generator.cs: Generate(TryStatementContext)
Runtime/Instructions/TryInstruction.cs: TryInstruction / CatchInstruction / FinallyInstruction / EndTryInstruction
Runtime/Interpreter.cs: CallSubrutine / TryHandleStructuredError / Transfer / DeferReturn / Failure
Runtime/SemanticScope.cs: IsLocal / DefineVar / SetVar
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/try-catch-finally-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/throw-statement
-->
