# Dictionary

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

Dictionary() 建立鍵 → 值集合。請在回傳的物件上呼叫方法。數字鍵與文字鍵不同，"ore" 和 "Ore" 也不同。

## 完整語法

```text
Dictionary() -> Object
Dictionary(source:Any) -> Object
```

## 參數

- `source` — source：省略時建立空集合。List 接受陣列或 List；Dictionary 接受 Dictionary。複製外層容器，內層物件與陣列參考仍共用。

## 傳回值

建構函式回傳 Object:Dictionary。Item／索引／Get 回傳值；Count 回傳鍵數。ContainsKey/Remove 回傳 1=TRUE 或 0=FALSE。Add/Set/Clear 回傳 Unit；Keys/Values 回傳新的 Array。For Each 產生項目物件，Key() 回傳鍵，Value() 回傳值。

## 行為

- index / key：List 位置為從 0 開始的整數數值；Insert 也接受 Count()。Dictionary 的鍵可為文字或有限數字。數字 1 與 1.0 是相同鍵，文字 "1" 則不同。
- value：已初始化的 Basic 值，可包含陣列或集合。不能儲存 Unit。相等判斷比較數值、區分大小寫的文字，或陣列／物件的參考識別。
- fallback：鍵不存在時 Get 回傳此備用值，不插入鍵。所有引數，包括 fallback 運算式，都在方法呼叫前計算。
- Add 拒絕既有鍵且不覆寫。Set／索引指定新增或取代；Item／索引讀取要求鍵存在，Get 可使用備用值。Remove 在鍵不存在時回傳 0，Clear 清空字典。
- NaN、無限值、陣列、物件及 Unit 不能當鍵。鍵的順序未定義。每個走訪項目保留自己的鍵值對，不會隨下一次迭代改變。
- Keys/Values 建立淺層快照。要在走訪時刪除／取代，請走訪 Keys()；直接走訪字典則取得項目物件。
- 直接 For Each 期間修改集合（包括 Set），會在下一步產生可捕捉錯誤。Try/Finally 仍正常離開。被拒絕的修改不影響舊資料。
- 別名及 ByVal 引數共用集合。複製與快照只複製外層容器。索引式 ByRef 與複合指定只計算容器／鍵一次；重新指定變數不會改變已捕捉的回寫位置。
- 集合保存腳本本地資料。方法不移動遊戲物品，也不使用網路。以一個元素儲存的物品堆疊只占一個位置。

## 範例

### 鍵型別與備用值

```vb
# 鍵型別與備用值
#
# Dictionary() 建立鍵 → 值集合。請在回傳的物件上呼叫方法。數字鍵與文字鍵不同，"ore" 和 "Ore" 也不同。
#
# 建構函式回傳 Object:Dictionary。Item／索引／Get 回傳值；Count 回傳鍵數。ContainsKey/Remove 回傳 1=TRUE 或
# 0=FALSE。Add/Set/Clear 回傳 Unit；Keys/Values 回傳新的 Array。For Each 產生項目物件，Key() 回傳鍵，Value() 回傳值。

Option Explicit On
Sub Main()
    # "ore" 從 5 改為 8。數字鍵 1 存 2，文字鍵 "1" 存 3。Get("wood",7) 回傳 7，不插入鍵。Main 回傳 8*100+2*10+3+7，即 Integer
    # 830。

    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**參數與執行說明:**

- "ore" 從 5 改為 8。數字鍵 1 存 2，文字鍵 "1" 存 3。Get("wood",7) 回傳 7，不插入鍵。Main 回傳 8*100+2*10+3+7，即 Integer 830。

### 項目、快照與刪除

```vb
# 項目、快照與刪除
#
# Dictionary() 建立鍵 → 值集合。請在回傳的物件上呼叫方法。數字鍵與文字鍵不同，"ore" 和 "Ore" 也不同。
#
# 建構函式回傳 Object:Dictionary。Item／索引／Get 回傳值；Count 回傳鍵數。ContainsKey/Remove 回傳 1=TRUE 或
# 0=FALSE。Add/Set/Clear 回傳 Unit；Keys/Values 回傳新的 Array。For Each 產生項目物件，Key() 回傳鍵，Value() 回傳值。

Option Explicit On
Sub Main()
    # 兩個值總和是 5。Keys() 快照允許走訪時刪除。copied 保留 ore=2，snapshot 保留兩個值。Clear 後 Count()=0。Main 回傳
    # 5*100+2*10+2+0，即 Integer 522。

    Var values = Dictionary()
    values.Add("ore", 2)
    values.Add("wood", 3)
    Var copied = Dictionary(values)
    Var snapshot = values.Values()
    Var total = 0
    For Each entry In values
        If values.ContainsKey(entry.Key()) Then
            total += entry.Value()
        End If
    Next
    For Each key In values.Keys()
        values.Remove(key)
    Next
    values.Clear()
    Return total*100 + copied["ore"]*10 + GetArrayLength(snapshot) + values.Count()
End Sub
```

**參數與執行說明:**

- 兩個值總和是 5。Keys() 快照允許走訪時刪除。copied 保留 ore=2，snapshot 保留兩個值。Clear 後 Count()=0。Main 回傳 5*100+2*10+2+0，即 Integer 522。

### 處理重複鍵

```vb
# 處理重複鍵
#
# Dictionary() 建立鍵 → 值集合。請在回傳的物件上呼叫方法。數字鍵與文字鍵不同，"ore" 和 "Ore" 也不同。
#
# 建構函式回傳 Object:Dictionary。Item／索引／Get 回傳值；Count 回傳鍵數。ContainsKey/Remove 回傳 1=TRUE 或
# 0=FALSE。Add/Set/Clear 回傳 Unit；Keys/Values 回傳新的 Array。For Each 產生項目物件，Key() 回傳鍵，Value() 回傳值。

Option Explicit On
Sub Main()
    # 第一次 Add 儲存 ore=4。第二次 Add 傳入 7 時發生錯誤，Catch 設定 caught=1。原來的 ore=4 保留。Main 回傳 4*10+1，即 Integer
    # 41。

    Var values = Dictionary()
    values.Add("ore", 4)
    Var caught = 0
    Try
        values.Add("ore", 7)
    Catch problem
        caught = 1
    End Try
    Return values["ore"]*10 + caught
End Sub
```

**參數與執行說明:**

- 第一次 Add 儲存 ore=4。第二次 Add 傳入 7 時發生錯誤，Catch 設定 caught=1。原來的 ore=4 保留。Main 回傳 4*10+1，即 Integer 41。
