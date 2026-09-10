# UO.FindItem

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取上次搜尋第一個物件的 serial。

## 完整語法

```text
UO.FindItem() -> Any
```

## 參數

沒有參數。

## 傳回值

Integer — 第一個物件的 serial/ID；沒有結果時為 0。不是 graphic/type。與 FindType 不同，這裡傳回數字，而非十六進位字串。

## 行為

- 一般的 FindType（1–5 個引數）、FindTypeEx 及 Count/CountEx/CountGround 會取代此腳本的搜尋結果。沒有符合項目時會清空快照。再次搜尋前應儲存仍需使用的值。
- 這些呼叫不搜尋、不開容器、不搬物品，也不傳封包，只讀取用戶端已載入的資料。FindCount(id) 不需要先搜尋，也不會改變搜尋結果。
- FindItem/FindCount()/FindFullQuantity 是搜尋快照。FindQuantity 和 FindCount(id) 讀取目前數量；搜尋後物件可能改變或消失。

## 範例

### 讀取金幣搜尋結果

```vb
# 讀取金幣搜尋結果
#
# 讀取上次搜尋第一個物件的 serial。
#
# Integer — 第一個物件的 serial/ID；沒有結果時為 0。不是 graphic/type。與 FindType 不同，這裡傳回數字，而非十六進位字串。

SUB Main()
    # type=0x0EED 表示金幣；color=-1 接受任何顏色；此形式的 FindType 以 backpack 選擇背包的直接內容。value 儲存結果，STR 將它顯示為文字。

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindItem()
    UO.Print(STR(value))
END SUB
```

**參數與執行說明:**

- type=0x0EED 表示金幣；color=-1 接受任何顏色；此形式的 FindType 以 backpack 選擇背包的直接內容。value 儲存結果，STR 將它顯示為文字。

### 比較物件、一疊與總量

```vb
# 比較物件、一疊與總量
#
# 讀取上次搜尋第一個物件的 serial。
#
# Integer — 第一個物件的 serial/ID；沒有結果時為 0。不是 graphic/type。與 FindType 不同，這裡傳回數字，而非十六進位字串。

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
# 讀取上次搜尋第一個物件的 serial。
#
# Integer — 第一個物件的 serial/ID；沒有結果時為 0。不是 graphic/type。與 FindType 不同，這裡傳回數字，而非十六進位字串。

SUB Main()
    # 第一個 type 是金幣；0x0F7A 是另一種藥材。第二次 FindType 會取代快照。saved 保留舊值，最後一次讀取則使用新結果。

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindItem()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindItem()))
END SUB
```

**參數與執行說明:**

- 第一個 type 是金幣；0x0F7A 是另一種藥材。第二次 FindType 會取代快照。saved 保留舊值，最後一次讀取則使用新結果。
