# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Wait Until 會重複檢查條件，直到成功或超過時限。這是 Basic 擴充語法，不是 VB.NET 陳述式。它在目前腳本內執行，不會建立執行緒或啟動另一個程序。

## 完整語法

```text
Wait Until condition Timeout milliseconds
```

## 參數

- `condition` — condition 會立即求值，之後在短暫等待之間再次求值。請使用 Boolean 或比較式：數值 0 代表 false，其他值遵循 If 規則。字串 "false" 不是 Boolean false。可呼叫 UO 或自訂函式；錯誤會向外傳遞，副作用則在每次檢查時重複發生。
- `Timeout milliseconds` — Timeout 為必要標記。milliseconds 在第一次條件檢查前只求值一次，必須為 Integer 0..2147483647。負數、小數或 String 會在條件執行前引發錯誤。0 只允許立即檢查。其他位置仍可將 timeout 當作一般變數名稱。

## 傳回值

陳述式本身沒有回傳值。成功後執行下一行；逾時會產生含檔案與行號的執行錯誤，可由 Try/Catch 或 On Error 處理，否則目前執行失敗。它不會自動回傳 false。範例 2 明確建立回傳 True/1 或 False/0 的包裝函式。

## 行為

- 引擎保存時限並啟動單調遞增的 Stopwatch。第一次立即檢查可在時限為 0 時成功。若為 false，迴圈會檢查取消與暫停、計算剩餘時間，最多等待 10 毫秒後再次檢查，避免持續忙碌迴圈；作業系統排程可能延長間隔。
- 暫停會停止輪詢，但實際經過時間仍計入時限。恢復後若已到期，會在再次檢查前引發逾時。停止會中斷等待，並如其他緊急取消一樣略過腳本的 Catch/Finally。它無法強制中斷 condition 內阻塞的呼叫，請讓條件函式保持簡短。已開始的檢查完成後才會處理其結果或錯誤。
- 條件錯誤不會被替換成逾時。一般錯誤與逾時會執行適用的 Finally。變數屬於目前呼叫，每次重新進入都啟動新時限。沒有 End Wait 或額外輪詢間隔參數。Wait(milliseconds) 仍是獨立的延遲函式。

## 範例

### 1. 在時限內輪詢函式

```vb
# checks 初值為 0；Ready 以 ByRef 接收並在每次檢查加 1。required=3 以 ByVal 傳入；budget=5000 允許最多五秒。前兩次 false，第三次 true，Main 回傳 Integer 3。這是確定性的輪詢示範，並非模擬伺服器；可改為真正需要的狀態檢查。
Option Explicit On
Function Ready(ByRef checks As Integer, ByVal required As Integer) As Boolean
    checks += 1
    Return checks >= required
End Function

Sub Main()
    Dim checks As Integer = 0
    Const budget = 5000
    Wait Until Ready(checks, 3) Timeout budget
    Return checks
End Sub
```

**參數與執行說明:**

checks 初值為 0；Ready 以 ByRef 接收並在每次檢查加 1。required=3 以 ByVal 傳入；budget=5000 允許最多五秒。前兩次 false，第三次 true，Main 回傳 Integer 3。這是確定性的輪詢示範，並非模擬伺服器；可改為真正需要的狀態檢查。

### 2. 自行包裝 Boolean 回傳

```vb
# TryWait 接收 ready=False 與 budget=0。立即檢查失敗並引發逾時，Catch problem 執行 Return False；Main 回傳 0，可與 False 比較。ready=True 時會回傳 1/True。此函式捕捉所有執行錯誤，若需區分請檢查 problem。ready 是 Boolean 值，不是回呼函式。
Option Explicit On
Function TryWait(ByVal ready As Boolean, ByVal budget As Integer) As Boolean
    Try
        Wait Until ready Timeout budget
        Return True
    Catch problem
        Return False
    End Try
End Function

Sub Main()
    Dim success = TryWait(False, 0)
    Return success
End Sub
```

**參數與執行說明:**

TryWait 接收 ready=False 與 budget=0。立即檢查失敗並引發逾時，Catch problem 執行 Return False；Main 回傳 0，可與 False 比較。ready=True 時會回傳 1/True。此函式捕捉所有執行錯誤，若需區分請檢查 problem。ready 是 Boolean 值，不是回呼函式。

### 3. 保留條件錯誤並完成收尾

```vb
# CheckStatus 收到 state=-1 時立即拋出 "disconnected"。3000 毫秒時限不會替換錯誤。Catch 將 problem 複製到 message，Finally 設定 finished=True/1。Main 回傳 "disconnected:1"。state=1 會立即成功，state=0 會持續 false 直到逾時。本例不需連線遊戲。
Option Explicit On
Function CheckStatus(ByVal state As Integer) As Boolean
    If state < 0 Then
        Throw "disconnected"
    End If
    Return state = 1
End Function

Sub Main()
    Dim message = ""
    Dim finished = False
    Try
        Wait Until CheckStatus(-1) Timeout 3000
    Catch problem
        message = problem
    Finally
        finished = True
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**參數與執行說明:**

CheckStatus 收到 state=-1 時立即拋出 "disconnected"。3000 毫秒時限不會替換錯誤。Catch 將 problem 複製到 message，Finally 設定 finished=True/1。Main 回傳 "disconnected:1"。state=1 會立即成功，state=0 會持續 false 直到逾時。本例不需連線遊戲。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
