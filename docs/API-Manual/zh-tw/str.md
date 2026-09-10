# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

Str(value) 將 Basic 純量格式化為文字。

## 完整語法

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## 參數

- `value` — 必須提供一個 Integer、Decimal 或 String；依實際種類選擇多載。Array、Object 與 Unit 沒有相符的 Str 多載。

## 傳回值

String：與語言無關的數字文字，或保持原樣的輸入字串。正數前不加空格。沒有小數位數參數。

## 行為

- 兩者都在本機計算，不查詢遊戲。省略參數會出錯。角色屬性應用 UO.Int()/UO.Str()，不是 Int()/Str()。Int 經過 BasicDouble 與 Math.Floor；Str 依種類選擇 InternalSubrutines.Str 並以固定文化格式輸出。

## 範例

### Str — 1

```vb
# Str — 1
#
# Str(value) 將 Basic 純量格式化為文字。
#
# String：與語言無關的數字文字，或保持原樣的輸入字串。正數前不加空格。沒有小數位數參數。

SUB Main()
    # value=42 為 Integer。Str 產生無前導空格的 "42"，Main 傳回此 String。

    RETURN Str(42)
END SUB
```

**參數與執行說明:**

- value=42 為 Integer。Str 產生無前導空格的 "42"，Main 傳回此 String。

### Str — 2

```vb
# Str — 2
#
# Str(value) 將 Basic 純量格式化為文字。
#
# String：與語言無關的數字文字，或保持原樣的輸入字串。正數前不加空格。沒有小數位數參數。

SUB Main()
    # amount=-12.5 為 Decimal。Str 在任何介面語言下都把帶小數點的 "-12.5" 存入 text。Main 傳回 text，amount 仍為數字。

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**參數與執行說明:**

- amount=-12.5 為 Decimal。Str 在任何介面語言下都把帶小數點的 "-12.5" 存入 text。Main 傳回 text，amount 仍為數字。

### Str — 3

```vb
# Str — 3
#
# Str(value) 將 Basic 純量格式化為文字。
#
# String：與語言無關的數字文字，或保持原樣的輸入字串。正數前不加空格。沒有小數位數參數。

SUB Main()
    # ItemLabel 接受 name="ore"、count=3。Str(name) 保留名稱，Str(count) 產生 "3"。函式以 " x" 連接文字，Main 傳回 "ore
    # x3"。

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**參數與執行說明:**

- ItemLabel 接受 name="ore"、count=3。Str(name) 保留名稱，Str(count) 產生 "3"。函式以 " x" 連接文字，Main 傳回 "ore x3"。
