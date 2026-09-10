# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

On Error 指定目前程序或函式中後續執行期錯誤的處理方式。它是語言陳述式，不是 API 呼叫。結構化處理與清理可使用 Try/Catch/Finally。

## 完整語法

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## 參數

- `label` — 同一程序內已存在的標籤，以 label: 獨立成行。可在 On Error 前或後，不區分大小寫。不是函式名、引號文字或原始碼行號。未知標籤產生 SC009，客戶端會阻止該腳本執行。
- `Resume Next / On Error` — On Error Resume Next 自動繼續至失敗指令之後，不跳到標籤。成功指令不受影響。只作用於目前程序呼叫，不影響所有腳本。
- `0` — On Error GoTo 0 關閉模式。零是特殊控制值，不是標籤或布林結果。不支援其他數字標籤或 GoTo -1。
- `Resume / Resume Next` — 處理區內 Resume 重試失敗指令，Resume Next 繼續至其後。須有已記錄的執行錯誤，使用後清除該地址。不接受標籤或逾時參數。

## 傳回值

On Error 與 Resume 不回傳值。捕捉錯誤不會轉成 TRUE/FALSE，也不會自動修正賦值。範例明確回傳 Integer 5、18、10；先前副作用不會自動回復。

## 行為

- 準備階段讀完整個程序後解析標籤，所以前後方向都可使用。執行時保存模式；發生例外先考慮結構化 Try，再考慮 On Error。
- 引擎記錄失敗指令地址。標籤模式跳至處理區，自動 Resume Next 跳過指令。Resume 會重新求值運算式與呼叫，請先修正原因並考慮重複的副作用。
- GoTo 0 不清除待處理錯誤地址，因此處理區可以先關閉自身、修正資料、再 Resume。請在處理區可能失敗的工作前關閉模式，避免重新進入同一處理區。
- 不捕捉語法錯誤或取消執行。命令若只回傳 0、FALSE 或失敗狀態但不拋例外，不會啟動 On Error；必須檢查該命令結果。
- 正常流程以 Return 或 GoTo 避開處理標籤。被呼叫程序有獨立模式；未處理錯誤可傳回呼叫端，此時 Resume 重做整個呼叫指令，而非內部一行。沒有自動重試次數或延遲。
- 錯誤在清理後離開 Try 並交給外部 On Error GoTo 時，Resume 會從標頭重試整個 Try。Resume Next 與 On Error Resume Next 都接續 End Try 後的第一個陳述式。已完成的動作可能重複，不會跳回已結束區塊的本體中間。

## 範例

### 1. 略過一次失敗賦值

```vb
# values[0] 配置一個儲存格，索引 5 無效。result=1。On Error Resume Next 在賦值前略過失敗讀取，因此仍為 1。GoTo 0 關閉模式；result+=4 得 5。Main 回傳 5，不表示讀取成功。
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**參數與執行說明:**

values[0] 配置一個儲存格，索引 5 無效。result=1。On Error Resume Next 在賦值前略過失敗讀取，因此仍為 1。GoTo 0 關閉模式；result+=4 得 5。Main 回傳 5，不表示讀取成功。

### 2. 修正後重試

```vb
# ReadCell 在儲存格 0 放入 8，但 index=2。錯誤跳至 FixIndex。GoTo 0 關閉處理，handled=1、index=0。Resume 重做 result=values[index]，現在寫入 8。Return 避免正常流程落入處理區。Main 收到 18。
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**參數與執行說明:**

ReadCell 在儲存格 0 放入 8，但 index=2。錯誤跳至 FixIndex。GoTo 0 關閉處理，handled=1、index=0。Resume 重做 result=values[index]，現在寫入 8。Return 避免正常流程落入處理區。Main 收到 18。

### 3. 處理區位於註冊之前

```vb
# 正常進入時 GoTo Work 略過 Failed。On Error GoTo Failed 啟用前方標籤。索引 2 在改變 result 前失敗。處理區關閉自身、增加 handled，再用 Resume Next 到 Return。結果 10；標籤不是獨立程序。
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**參數與執行說明:**

正常進入時 GoTo Work 略過 Failed。On Error GoTo Failed 啟用前方標籤。索引 2 在改變 result 前失敗。處理區關閉自身、增加 handled，再用 Resume Next 到 Return。結果 10；標籤不是獨立程序。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
