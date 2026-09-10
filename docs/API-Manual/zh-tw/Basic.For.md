# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

For 在包含可到達端點的數字範圍內重複區塊，適合陣列索引或已知次數的操作；For Each 則走訪元素值。

## 完整語法

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## 參數

- `counter / VAR` — 可寫入的純量計數變數。VAR 在程序內宣告；省略 VAR 時使用既有變數。Option Explicit On 下須先宣告或使用 For Var。型別請先以 DIM counter AS Integer 宣告；數字 For 標頭不支援 AS。
- `start` — 起始數字運算式，只求值一次，並在求值 limit 與 increment 之前賦給計數器。
- `limit` — 包含在範圍內的終點，只在進入時求值一次。正步長檢查 counter <= limit；負步長檢查 counter >= limit。
- `increment` — 可選數字步長，預設 1；可為負數或小數。零會產生可捕捉錯誤。計數器型別與步長必須能使數值前進。
- `statements / Next / exit` — 本體與 Next 各自獨立成行。Next 後可省略名稱，但若提供就必須符合計數器。Continue For 前往下一步；Exit For 離開最近的 For/For Each；Break 離開最近的任意種類迴圈。

## 傳回值

For、Next、Exit For 沒有回傳值。計數器是數字，不會自動成為物品 ID。正常完成後，本引擎保留最後實際執行的計數值，而非超出範圍的值。略過本體時保留 start，提早離開時保留當前值。範例從 Main 回傳 Integer 12、28、395。

## 行為

- 進入順序：賦值 start、保存 limit 與步長、拒絕零步長、檢查第一個值。方向背離終點時略過本體；start=limit 執行一次。
- Next 檢查 counter+step，只有下一輪仍在範圍內才賦值。因此 1 To 5 Step 3 走訪 1、4。修改原先提供終點或步長的變數，不會改變已保存的值；修改計數器本身會影響下一步。
- 執行前檢查結構與 Next 名稱，結構錯誤為 SC020。巢狀迴圈應使用不同計數器。離開 Try 時會執行 Finally。暫停與停止仍有效；迴圈沒有自動延遲或逾時。

## 範例

### 1. 陣列儲存格加總

```vb
# values[2] 建立索引 0、1、2，值為 2、4、6。Sum 以 ByVal 收到陣列，從 index=0 開始，保存 length-1=2。預設步長 1 走訪三個儲存格；total=12 回傳給 Main。
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**參數與執行說明:**

values[2] 建立索引 0、1、2，值為 2、4、6。Sum 以 ByVal 收到陣列，從 index=0 開始，保存 length-1=2。預設步長 1 走訪三個儲存格；total=12 回傳給 Main。

### 2. 由後往前刪除

```vb
# items 內容為 -1、3、-2、5。起點 Count()-1=3、終點 0、步長 -1。刪除負值只會位移已走訪的索引，因此不會略過尚待處理的元素。剩下 3、5；Count()*10+3+5 回傳 28。
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**參數與執行說明:**

items 內容為 -1、3、-2、5。起點 Count()-1=3、終點 0、步長 -1。刪除負值只會位移已走訪的索引，因此不會略過尚待處理的元素。剩下 3、5；Count()*10+3+5 回傳 28。

### 3. 保存界限與最後計數值

```vb
# ReadLimit 透過 ByRef 增加 calls 並回傳 value。起點 1、終點 5、步長 2 各求值一次：calls=3。本體內 upper=99、stride=1 不影響此迴圈。走訪 1、3、5，total=9、index 保留 5；Main 回傳 395。
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**參數與執行說明:**

ReadLimit 透過 ByRef 增加 calls 並回傳 value。起點 1、終點 5、步長 2 各求值一次：calls=3。本體內 upper=99、stride=1 不影響此迴圈。走訪 1、3、5，total=9、index 保留 5；Main 回傳 395。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
