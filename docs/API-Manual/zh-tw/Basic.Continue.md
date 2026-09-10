# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Continue 略過最近、指定類型之外層迴圈的剩餘本體。Continue For 用於數字 For 與 For Each，Continue Do 用於 Do/Loop 或 Repeat/Until，Continue While 用於 While/Wend。

## 完整語法

```text
Continue For
Continue Do
Continue While
```

## 參數

- `kind` — kind：Continue 後必須是 For、Do 或 While，不加括號。指定迴圈必須在同一程序內包住此陳述式。不同類型的內層迴圈不會攔截跳轉。

## 傳回值

Continue 沒有回傳值，也不能用於運算式。它不表示 TRUE/FALSE，也不重新啟動程序。函式之後可透過 RETURN 回傳結果；範例回傳 Integer 10、3、34。

## 行為

- For 執行 NEXT、套用 STEP，並用界限檢查下一個值；For Each 取得下一個元素。耗盡後離開迴圈，不會重新初始化計數器或再次求值集合運算式。
- Do 的開始條件重新在開始檢查，Loop 上的結尾條件在結尾檢查。Repeat/Until 使用 UNTIL。無條件 Do/Loop 持續至明確離開或停止。While 重新檢查 WHILE；Continue Do 不會選擇 While/Wend。
- 準備階段找出最近指定類型迴圈的指令位址。不存在時，即使沒有 Option Explicit，也在初始化前產生 SC020。也檢查 NEXT 名稱及缺少的結尾；保留舊 FOR/NEXT 跨越 IF 的相容行為。
- 跳轉離開 TRY/CATCH 時，依內至外順序將跨越的 FINALLY 各執行一次。若整個迴圈都在 TRY 內，該 FINALLY 不會每次迭代執行。FINALLY 中的 RETURN 或錯誤會取代待處理跳轉。
- Continue 不會等待。輪詢時應更新條件或使用適當等待，否則可能無限迴圈。暫停與停止仍會檢查。離開的原生列舉器會釋放，各執行互相獨立。Exit For/Do/While 是離開迴圈，而非進到下一次迭代。

## 範例

### 1. 略過不需要的元素

```vb
# values 是 -2、4、0、6。item<=0 時為 -2 與 0 執行 Continue For，略過 total+=item。For Each 也使用此寫法。SumPositive 與 Main 回傳 4+6，即 Integer 10。
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**參數與執行說明:**

values 是 -2、4、0、6。item<=0 時為 -2 與 0 執行 Continue For，略過 total+=item。For Each 也使用此寫法。SumPositive 與 Main 回傳 4+6，即 Integer 10。

### 2. 按類型選擇外層迴圈

```vb
# AdvanceTo 接收 limit=3，count 從 0 開始。在 While True 內遞增 count，再以 Continue Do 跳至外層 Do。每次重新檢查條件；count=3 時離開並回傳 Integer 3。
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**參數與執行說明:**

AdvanceTo 接收 limit=3，count 從 0 開始。在 While True 內遞增 count，再以 Continue Do 跳至外層 Do。每次重新檢查條件；count=3 時離開並回傳 Integer 3。

### 3. 略過迭代仍執行清理

```vb
# Process 接收 limit=3、skip=2。i 依序為 1、2、3。第二次略過 total+=i，但 Finally 三次都遞增 cleanup。total=4、cleanup=3；RETURN cleanup*10+total 回傳 Integer 34。
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**參數與執行說明:**

Process 接收 limit=3、skip=2。i 依序為 1、2、3。第二次略過 total+=i，但 Finally 三次都遞增 cleanup。total=4、cleanup=3；RETURN cleanup*10+total 回傳 Integer 34。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
