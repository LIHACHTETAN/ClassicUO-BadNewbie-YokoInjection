# Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

Int(value) 將 Basic 數值向負無限方向取整。

## 完整語法

```text
Int(value:Any) -> Integer
```

## 參數

- `value` — 必須提供一個 Integer/Decimal 或數字字串。小數點不受介面語言影響。無法辨識的文字、Array、Object、Unit 會轉成 0；請先用 IsNumeric 檢查輸入。

## 傳回值

Integer：floor(value)，例如 2.9 -> 2、-2.9 -> -3。取整結果必須在有號 Int32 範圍內；不要傳入非有限值或超出範圍的值。

## 行為

- 兩者都在本機計算，不查詢遊戲。省略參數會出錯。角色屬性應用 UO.Int()/UO.Str()，不是 Int()/Str()。Int 經過 BasicDouble 與 Math.Floor；Str 依種類選擇 InternalSubrutines.Str 並以固定文化格式輸出。

## 範例

### Int — 1

```vb
# Int — 1
#
# Int(value) 將 Basic 數值向負無限方向取整。
#
# Integer：floor(value)，例如 2.9 -> 2、-2.9 -> -3。取整結果必須在有號 Int32 範圍內；不要傳入非有限值或超出範圍的值。

SUB Main()
    # value=2.9。向下取整得到 Integer 2，由 Main 傳回。

    RETURN Int(2.9)
END SUB
```

**參數與執行說明:**

- value=2.9。向下取整得到 Integer 2，由 Main 傳回。

### Int — 2

```vb
# Int — 2
#
# Int(value) 將 Basic 數值向負無限方向取整。
#
# Integer：floor(value)，例如 2.9 -> 2、-2.9 -> -3。取整結果必須在有號 Int32 範圍內；不要傳入非有限值或超出範圍的值。

SUB Main()
    # value=-2.9。向下取整是 -3；朝零截斷才會是 -2。Main 傳回 Integer -3。

    VAR value = -2.9
    RETURN Int(value)
END SUB
```

**參數與執行說明:**

- value=-2.9。向下取整是 -3；朝零截斷才會是 -2。Main 傳回 Integer -3。

### Int — 3

```vb
# Int — 3
#
# Int(value) 將 Basic 數值向負無限方向取整。
#
# Integer：floor(value)，例如 2.9 -> 2、-2.9 -> -3。取整結果必須在有號 Int32 範圍內；不要傳入非有限值或超出範圍的值。

SUB Main()
    # WholeUnits 的 total=27、size=5。size<=0 時傳回 0，否則 Int(total/size) 將 5.4 向下取整。Main 傳回 5
    # 個完整單位。範例完整定義函式及兩個參數。

    RETURN WholeUnits(27,5)
END SUB

SUB WholeUnits(total,size)
    IF size <= 0 THEN
        RETURN 0
    END IF
    RETURN Int(total/size)
END SUB
```

**參數與執行說明:**

- WholeUnits 的 total=27、size=5。size<=0 時傳回 0，否則 Int(total/size) 將 5.4 向下取整。Main 傳回 5 個完整單位。範例完整定義函式及兩個參數。
