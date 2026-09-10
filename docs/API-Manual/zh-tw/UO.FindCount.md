# UO.FindCount

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

計算搜尋物件數，或依 ID 讀取指定堆疊的數量。

## 完整語法

```text
UO.FindCount() -> Integer
UO.FindCount(id:Any) -> Integer
```

## 參數

- `id` — 僅 FindCount 可選用。物品的 serial：Integer、十進位／十六進位字串、lasttarget、lastobject、backpack 或 AddObject 名稱。應傳 ID，不是 graphic/type。未知名稱為 0；self 指向角色，因此此處也是 0。不傳引數時讀取搜尋物件數。

## 傳回值

Integer — FindCount() 傳回找到的物件數：一整疊只算一個 item。FindCount(id) 讀取該物品目前的 Amount；未知／已刪除 ID 或角色傳回 0。不可堆疊物品通常為 Amount=1。不是 ID、type 或 Boolean。

## 行為

- 一般的 FindType（1–5 個引數）、FindTypeEx 及 Count/CountEx/CountGround 會取代此腳本的搜尋結果。沒有符合項目時會清空快照。再次搜尋前應儲存仍需使用的值。
- 這些呼叫不搜尋、不開容器、不搬物品，也不傳封包，只讀取用戶端已載入的資料。FindCount(id) 不需要先搜尋，也不會改變搜尋結果。
- FindItem/FindCount()/FindFullQuantity 是搜尋快照。FindQuantity 和 FindCount(id) 讀取目前數量；搜尋後物件可能改變或消失。

## 範例

### 讀取金幣搜尋結果

```vb
# 讀取金幣搜尋結果
#
# 計算搜尋物件數，或依 ID 讀取指定堆疊的數量。
#
# Integer — FindCount() 傳回找到的物件數：一整疊只算一個 item。FindCount(id) 讀取該物品目前的 Amount；未知／已刪除 ID 或角色傳回
# 0。不可堆疊物品通常為 Amount=1。不是 ID、type 或 Boolean。

SUB Main()
    # type=0x0EED 表示金幣；color=-1 接受任何顏色；此形式的 FindType 以 backpack 選擇背包的直接內容。value 儲存結果，STR 將它顯示為文字。

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindCount()
    UO.Print(STR(value))
END SUB
```

**參數與執行說明:**

- type=0x0EED 表示金幣；color=-1 接受任何顏色；此形式的 FindType 以 backpack 選擇背包的直接內容。value 儲存結果，STR 將它顯示為文字。

### 比較物件、一疊與總量

```vb
# 比較物件、一疊與總量
#
# 計算搜尋物件數，或依 ID 讀取指定堆疊的數量。
#
# Integer — FindCount() 傳回找到的物件數：一整疊只算一個 item。FindCount(id) 讀取該物品目前的 Amount；未知／已刪除 ID 或角色傳回
# 0。不可堆疊物品通常為 Amount=1。不是 ID、type 或 Boolean。

SUB Main()
    # 四次讀取都接在同一次搜尋之後。兩疊各 50：物件數=2、第一疊=50、總量=100。FindItem 是第一疊的唯一 ID，不是 type。

    UO.FindType(0x0EED, -1, 'backpack')
    UO.Print(STR(UO.FindCount()))
    UO.Print(STR(UO.FindQuantity()))
    UO.Print(STR(UO.FindFullQuantity()))
    UO.Print('0x' + Hex(UO.FindItem()))
END SUB
```

**參數與執行說明:**

- 四次讀取都接在同一次搜尋之後。兩疊各 50：物件數=2、第一疊=50、總量=100。FindItem 是第一疊的唯一 ID，不是 type。

### 再次搜尋前保留數值

```vb
# 再次搜尋前保留數值
#
# 計算搜尋物件數，或依 ID 讀取指定堆疊的數量。
#
# Integer — FindCount() 傳回找到的物件數：一整疊只算一個 item。FindCount(id) 讀取該物品目前的 Amount；未知／已刪除 ID 或角色傳回
# 0。不可堆疊物品通常為 Amount=1。不是 ID、type 或 Boolean。

SUB Main()
    # 第一個 type 是金幣；0x0F7A 是另一種藥材。第二次 FindType 會取代快照。saved 保留舊值，最後一次讀取則使用新結果。

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindCount()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindCount()))
END SUB
```

**參數與執行說明:**

- 第一個 type 是金幣；0x0F7A 是另一種藥材。第二次 FindType 會取代快照。saved 保留舊值，最後一次讀取則使用新結果。

### 直接依 ID 讀取物品

```vb
# 直接依 ID 讀取物品
#
# 計算搜尋物件數，或依 ID 讀取指定堆疊的數量。
#
# Integer — FindCount() 傳回找到的物件數：一整疊只算一個 item。FindCount(id) 讀取該物品目前的 Amount；未知／已刪除 ID 或角色傳回
# 0。不可堆疊物品通常為 Amount=1。不是 ID、type 或 Boolean。

SUB Main()
    # lasttarget 必須指向已在遊戲內選取的物品，不會出現新的目標游標。FindCount(id) 讀取目前堆疊，物品不在時為 0，且不改變搜尋快照。

    VAR id = lasttarget
    VAR amount = UO.FindCount(id)
    UO.Print(STR(amount))
END SUB
```

**參數與執行說明:**

- lasttarget 必須指向已在遊戲內選取的物品，不會出現新的目標游標。FindCount(id) 讀取目前堆疊，物品不在時為 0，且不改變搜尋快照。
