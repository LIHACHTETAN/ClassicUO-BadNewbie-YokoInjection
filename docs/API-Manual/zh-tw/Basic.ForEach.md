# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

For Each 不使用數字索引，依序走訪陣列或可列舉原生集合的元素。這是程序或函式內的迴圈陳述式，不是可呼叫的 API 函式。

## 完整語法

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## 參數

- `item` — item：迭代變數。重用已有的區域變數、參數或可存取欄位；不存在時建立程序區域變數，Option Explicit On 也適用。不可寫入常數。
- `type` — type：可選的 AS type，例如 Integer。宣告區域迭代變數，並在每次賦值時轉換元素。省略 AS 時，已有變數保留原宣告型別。
- `collection` — collection：進入時只求值一次。接受陣列或支援列舉的原生物件，不接受純量。巢狀陣列先傳出各列，再用內層迴圈取得儲存格。
- `statements / NEXT item` — statements / NEXT item：迴圈本體及結尾。NEXT 後的名稱可省略，但若提供就必須與迭代變數相同。NEXT 必須單獨一行。

## 傳回值

For Each 和 Next 沒有回傳值。item 取得元素值，不會自動取得索引、長度、物品 ID 或堆疊數量；意義由集合內容決定。本體中的 RETURN 結束整個函式。範例分別回傳 Integer 12、105、10。

## 行為

- 準備階段在執行初始化式之前配對 FOR EACH 與 NEXT，錯誤配對產生 SC020。collection 求值一次後，引擎保留參考和獨立游標；修改 item 不會移動游標。
- 陣列按索引遞增讀取。空陣列略過本體，保留已有且未指定 AS 之變數的舊值。未初始化元素與 AS 轉換失敗會產生可捕捉的錯誤。
- 賦值給 item 不會替換陣列元素。巢狀陣列及物件為參考：修改 row 的儲存格會改變該列。重新賦值 collection 不會切換目前集合；同一陣列後續元素的修改會在讀取時反映。
- Continue For 前進到最近 For 或 For Each 的下一次迭代；Exit For 離開該迴圈。錯誤、RETURN 和取消會釋放原生列舉器。有些集合禁止迭代期間修改；不會自動建立快照。
- 迭代變數在迴圈後仍可於所屬程序內存取，並保留最後賦值。不同執行有獨立游標。IDE 支援名稱補全、迴圈範本及宣告導覽，暫停與停止檢查仍有效。

## 範例

### 1. 不使用索引加總

```vb
# values[2] 有三個元素 2、4、6。SumItems 接收陣列，item 依序取得各數字。total 從 0 累加至 12，RETURN 將 Integer 12 傳給 Main。NEXT item 關閉同一迴圈。
Option Explicit On
Function SumItems(values)
    Var total = 0
    For Each item In values
        total += item
    Next item
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return SumItems(values)
End Sub
```

**參數與執行說明:**

values[2] 有三個元素 2、4、6。SumItems 接收陣列，item 依序取得各數字。total 從 0 累加至 12，RETURN 將 Integer 12 傳給 Main。NEXT item 關閉同一迴圈。

### 2. 求值一次並轉換

```vb
# SelectItems 以 ByRef 接收 calls，將其加至 1，回傳 ["2", "3"]。AS Integer 轉成 2、3，total=5。item=100 不改變來源或順序。Main 回傳 calls*100+total，即 Integer 105。
Option Explicit On
Function SelectItems(ByRef calls)
    calls += 1
    Dim values[1]
    values[0] = "2"
    values[1] = "3"
    Return values
End Function
Sub Main()
    Var calls = 0
    Var total = 0
    For Each item As Integer In SelectItems(calls)
        total += item
        item = 100
    Next
    Return calls * 100 + total
End Sub
```

**參數與執行說明:**

SelectItems 以 ByRef 接收 calls，將其加至 1，回傳 ["2", "3"]。AS Integer 轉成 2、3，total=5。item=100 不改變來源或順序。Main 回傳 calls*100+total，即 Integer 105。

### 3. 巢狀陣列

```vb
# rows[1][1] 有兩列，每列兩個儲存格。row 取得列參考，cell 依序取得 1、2、3、4。每個 NEXT 關閉自己的迴圈。SumGrid 與 Main 回傳 Integer 10，不會自動推算 ID 或數量。
Option Explicit On
Function SumGrid(rows)
    Var total = 0
    For Each row In rows
        For Each cell In row
            total += cell
        Next cell
    Next row
    Return total
End Function
Sub Main()
    Dim rows[1][1]
    rows[0][0] = 1
    rows[0][1] = 2
    rows[1][0] = 3
    rows[1][1] = 4
    Return SumGrid(rows)
End Sub
```

**參數與執行說明:**

rows[1][1] 有兩列，每列兩個儲存格。row 取得列參考，cell 依序取得 1、2、3、4。每個 NEXT 關閉自己的迴圈。SumGrid 與 Main 回傳 Integer 10，不會自動推算 ID 或數量。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
