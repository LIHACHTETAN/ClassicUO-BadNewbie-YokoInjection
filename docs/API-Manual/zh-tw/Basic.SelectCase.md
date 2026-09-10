# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Select Case 將儲存的值依序與候選條件比較，只選擇一個分支。適合物品分類、腳本模式及數值區間。它是 Basic 敘述，不加 UO.；運算式中的遊戲 API 呼叫仍須加 UO.。

## 完整語法

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

## 參數

- `expression` — 必要運算式，可為變數、常值或函式呼叫。每次進入區塊只求值一次，即使區塊為空或只有 Case Else 也會求值。
- `value / from / to` — Case 可接受一個值或逗號分隔的候選運算式。from To to 包含兩端；反向區間不匹配。下界比較成立後才計算上界。函式引數內的逗號不會分割候選條件。
- `Is comparison value` — 使用 =、<>、<、<=、>、>=。Is 可省略：Case Is >= 5 等同 Case >= 5。這是引擎一般值比較，不是物件型別判斷。
- `Case Else` — 可選的預設分支，僅在先前 Case 都不匹配時執行。最多一個且必須最後。省略時，無匹配就繼續執行 End Select 之後的程式。
- `Exit Select` — 離開最近的外層 Select Case，到其 End Select 之後。不會結束外面的迴圈或程序。在 Select Case 外使用會產生載入錯誤。

## 傳回值

Select Case、Case、End Select、Exit Select 都不回傳值，不能與 TRUE 或 1 比較。範例中的函式透過 Return 明確回傳 String 或 Integer。TRUE 的數值為 1，FALSE 為 0，因此 Case True 只匹配 1，不是所有非零數字。

## 行為

- 準備階段建立 SelectInstruction、依序的 CaseInstruction 及已解析的跳躍。選擇值私下儲存在目前函式呼叫中，不會新增可見區域變數。遞迴及巢狀區塊各自保存值；每次重新進入都更新儲存值。
- CaseMatches 由左至右檢查，在第一個匹配處停止。所選分支執行一次，然後跳過其餘分支。Case 運算式修改變數也不會重新讀取選擇值；已產生的副作用不會復原。
- 數字及字串使用一般引擎比較規則，字串區分大小寫。未實作 Option Compare Text 或 VB.NET 自動型別轉換。比較數字與文字時請明確轉換。
- 必須有 End Select。第一個 Case 前不可放執行程式碼，For/Next 不可跨越不同分支。結構錯誤會阻止載入。應由 Select Case 進入，不要用 GoTo 跳進中間。
- 錯誤交給目前處理常式。選擇運算式失敗時，On Error Resume Next 跳過整個區塊；Case 失敗時移至下一個 Case。Resume 重試失敗指令。Exit Select 會執行離開的作用中 Finally。指令之間保留暫停與停止檢查，不新增等待或逾時。

## 範例

### 1. 依數量分類

```vb
# DescribeAmount 以 ByVal 接收 amount。Case 0 回傳 empty；1 To 4 包含 1 和 4；Is >= 5 回傳 large；負數進入 Case Else。Main 傳入 -1、0、4、5，組合得到 negative:empty:small:large。這些文字是腳本定義的結果。
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

**參數與執行說明:**

DescribeAmount 以 ByVal 接收 amount。Case 0 回傳 empty；1 To 4 包含 1 和 4；Is >= 5 回傳 large；負數進入 Case Else。Main 傳入 -1、0、4、5，組合得到 negative:empty:small:large。這些文字是腳本定義的結果。

### 2. 觀察實際呼叫

```vb
# ReadMode 透過 ByRef 增加 reads，僅回傳一次 2。Candidate 增加 checks 並回傳 value。候選 1 不匹配，2 匹配，因此跳過 3。selected 為 7，Main 回傳 1*100+2*10+7=127，不需存取遊戲。
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

**參數與執行說明:**

ReadMode 透過 ByRef 增加 reads，僅回傳一次 2。Candidate 增加 checks 並回傳 value。候選 1 不匹配，2 匹配，因此跳過 3。selected 為 7，Main 回傳 1*100+2*10+7=127，不需存取遊戲。

### 3. 離開巢狀選擇

```vb
# route 為 harvest，匹配第一個候選，trace 變成 1。內層 Case 2 執行 Exit Select，跳過 trace=99，但 Finally 加上數字 2。外層分支再加上 3，得到 123。外層 Case Else 被跳過。將 route 改成其他字串會回傳 -1。
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

**參數與執行說明:**

route 為 harvest，匹配第一個候選，trace 變成 1。內層 Case 2 執行 Exit Select，跳過 trace=99，但 Finally 加上數字 2。外層分支再加上 3，得到 123。外層 Case Else 被跳過。將 route 改成其他字串會回傳 -1。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
