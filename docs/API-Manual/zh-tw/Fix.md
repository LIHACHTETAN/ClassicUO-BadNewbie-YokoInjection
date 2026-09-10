# Fix

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

朝零捨去小數部分。

## 完整語法

```text
Fix(value:Any) -> Integer
```

## 參數

- `value` — 必填：Integer/Decimal 或小數點格式、可帶指數的十進位文字，例如 "-1.25e2"。不受介面語言影響。無效/十六進位文字、Unit、Array、Object 變成 0；十六進位數字常值已是 Integer。可能有 NaN/Infinity。 僅限有限輸入，截斷結果須在 -2147483648..2147483647。-2.9 得 -2，不同於 floor=-3。越界/NaN/Infinity 不是有效輸入。

## 傳回值

Integer — truncate(value). 僅限有限輸入，截斷結果須在 -2147483648..2147483647。-2.9 得 -2，不同於 floor=-3。越界/NaN/Infinity 不是有效輸入。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

## 行為

- 在腳本執行緒本機計算，不連線請求、不移動、不選目標、不等待或修改全域變數。
- Decimal 是二進位 Double，不是 .NET decimal。有限近似值應以容差比較。NaN/Infinity 不適合當座標或物品數量。
- 僅限有限輸入，截斷結果須在 -2147483648..2147483647。-2.9 得 -2，不同於 floor=-3。越界/NaN/Infinity 不是有效輸入。

### 內部函式：從呼叫到結果

這是實際的註冊與轉換步驟。完整輔助函式展示腳本公式，不取代平台的數學實作。

#### 1. Register

Register 將單參數 BASIC 名稱綁定至原生計算，轉換後呼叫 System.Math。不執行隱藏腳本或伺服器程序。

Integer — truncate(value). 僅限有限輸入，截斷結果須在 -2147483648..2147483647。-2.9 得 -2，不同於 floor=-3。越界/NaN/Infinity 不是有效輸入。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 函式 `Register`.

#### 2. BasicDouble

BasicDouble 保留 Integer/Decimal，以固定文化的 NumberStyles.Float 解析文字，其他值回傳 0。Abs 先直接處理一般 Integer，之後才用 Double。

必填：Integer/Decimal 或小數點格式、可帶指數的十進位文字，例如 "-1.25e2"。不受介面語言影響。無效/十六進位文字、Unit、Array、Object 變成 0；十六進位數字常值已是 Integer。可能有 NaN/Infinity。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 函式 `BasicDouble`.

在腳本執行緒本機計算，不連線請求、不移動、不選目標、不等待或修改全域變數。


## 範例

### 直接計算

```vb
# 直接計算
#
# 朝零捨去小數部分。
#
# Integer — truncate(value). 僅限有限輸入，截斷結果須在 -2147483648..2147483647。-2.9 得 -2，不同於
# floor=-3。越界/NaN/Infinity 不是有效輸入。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

SUB Main()
    # value = 2.9；預期 2（~ 表示近似）。value 保存結果，CStr 只為 Print 格式化。

    VAR value = Fix(2.9)
    UO.Print(CStr(value))
END SUB
```

**參數與執行說明:**

- value = 2.9；預期 2（~ 表示近似）。value 保存結果，CStr 只為 Print 格式化。

### 用變數傳入不同值

```vb
# 用變數傳入不同值
#
# 朝零捨去小數部分。
#
# Integer — truncate(value). 僅限有限輸入，截斷結果須在 -2147483648..2147483647。-2.9 得 -2，不同於
# floor=-3。越界/NaN/Infinity 不是有效輸入。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

SUB Main()
    # value = -2.9；預期 -2（~ 表示近似）。value 保存結果，CStr 只為 Print 格式化。

    VAR inputValue = -2.9
    VAR value = Fix(inputValue)
    UO.Print(CStr(value))
END SUB
```

**參數與執行說明:**

- value = -2.9；預期 -2（~ 表示近似）。value 保存結果，CStr 只為 Print 格式化。

### 完整可重用輔助函式

```vb
# 完整可重用輔助函式
#
# 朝零捨去小數部分。
#
# Integer — truncate(value). 僅限有限輸入，截斷結果須在 -2147483648..2147483647。-2.9 得 -2，不同於
# floor=-3。越界/NaN/Infinity 不是有效輸入。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

# manual-check: scalar-math Fix
SUB Main()
    # total>=0、size>0：完整批數；27/5 得 5。無效輸入的備用值 0 也可能代表無完整批次。商須在 Integer 範圍。

    VAR value = WholeBatches(27,5)
    UO.Print(CStr(value))
END SUB

SUB WholeBatches(total,size)
    IF total < 0 OR size <= 0 THEN
        RETURN 0
    END IF
    RETURN Fix(CDbl(total)/CDbl(size))
END SUB
```

**參數與執行說明:**

- total>=0、size>0：完整批數；27/5 得 5。無效輸入的備用值 0 也可能代表無完整批次。商須在 Integer 範圍。
