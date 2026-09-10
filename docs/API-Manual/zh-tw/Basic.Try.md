# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Try 處理內容及被呼叫函式的執行錯誤。Catch 接收錯誤，Finally 完成收尾，Throw 建立或重新拋出錯誤。API 傳回 0 或 false 是一般結果，必須明確檢查，不會自動進入 Catch。

## 完整語法

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

## 參數

- `Try / statements` — Try 必須包含一個 Catch、一個 Finally 或兩者，並以 End Try 結束。可巢狀使用；內容成功完成時會略過 Catch。此子集尚未實作多個 Catch、When 篩選條件及 Exit Try。
- `Catch / name / As type` — Catch 的變數可省略。指定 name 時會收到 String 錯誤訊息。As String 表示這種資料形式；As Exception 是相容寫法，不是 .NET 物件或型別篩選器。其他型別會遭拒絕。新名稱成為程序區域變數並遮蔽同名全域變數；既有區域變數則依照其型別及 Const 規則指定。如果未進入 Catch 的路徑也需要該變數，請在 Try 前宣告 String。
- `Finally / End Try` — 已有 Catch 時可省略 Finally，Finally 內容也可為空。正常完成、錯誤、Return、Exit Sub/Function，以及向外的迴圈／GoTo 跳轉都會執行相關 Finally。End Try 必須存在。腳本取消會刻意略過 Catch 與腳本 Finally，避免緊急停止被延後。
- `Throw stringExpression` — Throw stringExpression 只計算一次訊息並建立新腳本錯誤。訊息必須為 String，其他值請明確使用 CStr 轉換。這是 Basic 語法，不是 VB.NET 的 Throw New Exception(...)。沒有處理常式時，目前腳本執行會失敗，其他腳本不會因此全部停止。
- `Throw` — 不帶訊息的 Throw 只能出現在 Catch 內，包括其中的巢狀區塊。它重新拋出目前錯誤，保留原始訊息、檔案與行號。從 Catch 呼叫的輔助函式必須有自己的 Catch，才能使用這個形式。

## 傳回值

Try/Catch/Finally 和 Throw 不會傳回 ID、數字或 Boolean。Catch 透過 name 提供訊息；Throw 轉移控制流程而非傳回值。範例明確從 Main 傳回兩個 String 與 Integer 13。區塊內的 API 保留原本的傳回契約。

## 行為

- 準備階段驗證區塊並禁止 GoTo/On Error GoTo 直接進入 Try、Catch 或 Finally。產生器記錄處理與收尾位置。每次呼叫有獨立的有效處理常式，錯誤先到最近的適用 Catch。Catch 內再次出錯時，先經過自己的 Finally 再向外傳遞。沒有結構化處理常式時，可能套用一般 On Error 規則。
- 執行 Finally 時暫存待處理的傳回值、錯誤或向外跳轉；巢狀收尾由內向外進行。Finally 的新錯誤會取代原先錯誤。Basic 也允許 Finally 內的 Return 或向外跳轉，它們會取代原先待續的流程，這與 VB.NET 不同。重新拋出會保留第一次失敗的位置，包括被呼叫函式內的錯誤。
- 暫停與停止檢查仍然有效。Try 不會建立執行緒、重試或等待。準備好的位置會重複使用；一般條件應直接檢查，不要以例外代替。緊急停止會略過腳本收尾；主機管理的資源仍依照引擎自己的生命週期釋放。

## 範例

### 1. 驗證參數並保存訊息

```vb
# CheckedAmount 以 ByVal 接收 Integer amount=-2。負值觸發 Throw "amount must be non-negative"。Catch 將 String 存入 problem 並複製到 message；As Exception 不會建立物件。Finally 將 finished 設為 1。Main 傳回 "amount must be non-negative:1"。非負值則正常傳回，不執行 Catch。
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

**參數與執行說明:**

CheckedAmount 以 ByVal 接收 Integer amount=-2。負值觸發 Throw "amount must be non-negative"。Catch 將 String 存入 problem 並複製到 message；As Exception 不會建立物件。Finally 將 finished 設為 1。Main 傳回 "amount must be non-negative:1"。非負值則正常傳回，不執行 Catch。

### 2. 重新拋給外層

```vb
# 內層 Throw 建立 "missing item"。內層 Catch 設定 trace=1，空的 Throw 保留同一個錯誤。內層 Finally 加上數字 2，外層 Catch 將 outerProblem 複製到 message 並加上 3，外層 Finally 再加上 4。Main 傳回 "1234:missing item"。trace 記錄執行順序，不是錯誤代碼。
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

**參數與執行說明:**

內層 Throw 建立 "missing item"。內層 Catch 設定 trace=1，空的 Throw 保留同一個錯誤。內層 Finally 加上數字 2，外層 Catch 將 outerProblem 複製到 message 並加上 3，外層 Finally 再加上 4。Main 傳回 "1234:missing item"。trace 記錄執行順序，不是錯誤代碼。

### 3. 完成每次已開始的迭代

```vb
# number 依序為 1、2、3。只有 1 加入 total：Continue For 跳過 2，Exit For 在 3 結束迴圈。三次已進入的 Try 都執行 Finally，因此 finished=3。Main 傳回 1*10+3=13。Finally 不需要有錯誤才執行；迴圈跳轉會等到該次收尾完成。
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

**參數與執行說明:**

number 依序為 1、2、3。只有 1 加入 total：Continue For 跳過 2，Exit For 在 3 結束迴圈。三次已進入的 Try 都執行 Finally，因此 finished=3。Main 傳回 1*10+3=13。Finally 不需要有錯誤才執行；迴圈跳轉會等到該次收尾完成。

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
