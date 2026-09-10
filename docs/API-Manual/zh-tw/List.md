# List

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

List() 建立有順序、可調整長度的集合。請用變數保存物件；items.Add 是物件方法，並不存在全域 List.Add 命令。

## 完整語法

```text
List() -> Object
List(source:Any) -> Object
```

## 參數

- `source` — source：省略時建立空集合。List 接受陣列或 List；Dictionary 接受 Dictionary。複製外層容器，內層物件與陣列參考仍共用。

## 傳回值

建構函式回傳 Object:List。Item／索引讀取儲存值；Count 回傳元素數，IndexOf 回傳從 0 開始的位置或 -1。Contains/Remove 回傳 1=TRUE 或 0=FALSE。Add/Insert/Set/RemoveAt/Clear 回傳 Unit；ToArray 回傳新的 Array。

## 行為

- index / key：List 位置為從 0 開始的整數數值；Insert 也接受 Count()。Dictionary 的鍵可為文字或有限數字。數字 1 與 1.0 是相同鍵，文字 "1" 則不同。
- value：已初始化的 Basic 值，可包含陣列或集合。不能儲存 Unit。相等判斷比較數值、區分大小寫的文字，或陣列／物件的參考識別。
- fallback：鍵不存在時 Get 回傳此備用值，不插入鍵。所有引數，包括 fallback 運算式，都在方法呼叫前計算。
- Add 加到尾端；Insert 插入指定位置之前；Set／索引指定取代現有元素，Item／索引讀取元素。Remove 刪除第一個相等值，RemoveAt 刪除指定位置，Clear 刪除所有元素。
- Contains 檢查是否存在，IndexOf 尋找第一個符合項目。負數、小數、文字或超出範圍的索引產生可捕捉錯誤，且不修改列表。
- For Each 保留列表順序。ToArray 建立淺層快照；修改原列表時應走訪該快照。
- 直接 For Each 期間修改集合（包括 Set），會在下一步產生可捕捉錯誤。Try/Finally 仍正常離開。被拒絕的修改不影響舊資料。
- 別名及 ByVal 引數共用集合。複製與快照只複製外層容器。索引式 ByRef 與複合指定只計算容器／鍵一次；重新指定變數不會改變已捕捉的回寫位置。
- 集合保存腳本本地資料。方法不移動遊戲物品，也不使用網路。以一個元素儲存的物品堆疊只占一個位置。

## 範例

### 建立列表並加總

```vb
# 建立列表並加總
#
# List() 建立有順序、可調整長度的集合。請用變數保存物件；items.Add 是物件方法，並不存在全域 List.Add 命令。
#
# 建構函式回傳 Object:List。Item／索引讀取儲存值；Count 回傳元素數，IndexOf 回傳從 0 開始的位置或 -1。Contains/Remove 回傳 1=TRUE
# 或 0=FALSE。Add/Insert/Set/RemoveAt/Clear 回傳 Unit；ToArray 回傳新的 Array。

Option Explicit On
Sub Main()
    # Add 產生 [3,7]；Insert(1,5) 產生 [3,5,7]；Set(0,2) 產生 [2,5,7]。For Each 將三個值相加。Main 回傳 Integer 14。

    Var items = List()
    items.Add(3)
    items.Add(7)
    items.Insert(1, 5)
    items.Set(0, 2)
    Var total = 0
    For Each item In items
        total += item
    Next
    Return total
End Sub
```

**參數與執行說明:**

- Add 產生 [3,7]；Insert(1,5) 產生 [3,5,7]；Set(0,2) 產生 [2,5,7]。For Each 將三個值相加。Main 回傳 Integer 14。

### 獨立副本與快照

```vb
# 獨立副本與快照
#
# List() 建立有順序、可調整長度的集合。請用變數保存物件；items.Add 是物件方法，並不存在全域 List.Add 命令。
#
# 建構函式回傳 Object:List。Item／索引讀取儲存值；Count 回傳元素數，IndexOf 回傳從 0 開始的位置或 -1。Contains/Remove 回傳 1=TRUE
# 或 0=FALSE。Add/Insert/Set/RemoveAt/Clear 回傳 Unit；ToArray 回傳新的 Array。

Option Explicit On
Sub Main()
    # seed=[4,6]。copied 與 snapshot 保留這些值。原列表變為 [9,6]；Remove(6) 回傳 TRUE=1，RemoveAt(0) 清空列表，Clear
    # 維持空白。Main 回傳 4*100+6*10+1+0，即 Integer 461。

    Dim seed[1]
    seed[0] = 4
    seed[1] = 6
    Var items = List(seed)
    Var copied = List(items)
    Var snapshot = items.ToArray()
    items[0] = 9
    Var removed = items.Remove(6)
    items.RemoveAt(0)
    items.Clear()
    Return snapshot[0]*100 + copied[1]*10 + removed + items.Count()
End Sub
```

**參數與執行說明:**

- seed=[4,6]。copied 與 snapshot 保留這些值。原列表變為 [9,6]；Remove(6) 回傳 TRUE=1，RemoveAt(0) 清空列表，Clear 維持空白。Main 回傳 4*100+6*10+1+0，即 Integer 461。

### 搜尋與 ByRef 修改

```vb
# 搜尋與 ByRef 修改
#
# List() 建立有順序、可調整長度的集合。請用變數保存物件；items.Add 是物件方法，並不存在全域 List.Add 命令。
#
# 建構函式回傳 Object:List。Item／索引讀取儲存值；Count 回傳元素數，IndexOf 回傳從 0 開始的位置或 -1。Contains/Remove 回傳 1=TRUE
# 或 0=FALSE。Add/Insert/Set/RemoveAt/Clear 回傳 Unit；ToArray 回傳新的 Array。

Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    # NextIndex 只執行一次：calls=1、索引為 0。Bump 將 5 改為 6。Contains(6)=TRUE、IndexOf(6)=0，Item(0) 回傳 6。Main 回傳
    # Integer 601。

    Var items = List()
    items.Add(5)
    Var calls = 0
    Bump(items[NextIndex(calls)])
    If items.Contains(6) AndAlso items.IndexOf(6) = 0 Then
        Return items.Item(0)*100 + calls
    End If
    Return -1
End Sub
```

**參數與執行說明:**

- NextIndex 只執行一次：calls=1、索引為 0。Bump 將 5 改為 6。Contains(6)=TRUE、IndexOf(6)=0，Item(0) 回傳 6。Main 回傳 Integer 601。
