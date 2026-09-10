# Abs

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

傳回絕對值。

## 完整語法

```text
Abs(value:Any) -> Any
```

## 參數

- `value` — 必填：Integer/Decimal 或小數點格式、可帶指數的十進位文字，例如 "-1.25e2"。不受介面語言影響。無效/十六進位文字、Unit、Array、Object 變成 0；十六進位數字常值已是 Integer。可能有 NaN/Infinity。 Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到 Decimal。NaN 保持；正負無限都得到 +Infinity。

## 傳回值

Integer/Decimal — abs(value). Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到 Decimal。NaN 保持；正負無限都得到 +Infinity。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

## 行為

- 在腳本執行緒本機計算，不連線請求、不移動、不選目標、不等待或修改全域變數。
- Decimal 是二進位 Double，不是 .NET decimal。有限近似值應以容差比較。NaN/Infinity 不適合當座標或物品數量。
- Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到 Decimal。NaN 保持；正負無限都得到 +Infinity。

### 內部函式：從呼叫到結果

這是實際的註冊與轉換步驟。完整輔助函式展示腳本公式，不取代平台的數學實作。

#### 1. Register

Register 將單參數 BASIC 名稱綁定至原生計算，轉換後呼叫 System.Math。不執行隱藏腳本或伺服器程序。

Integer/Decimal — abs(value). Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到 Decimal。NaN 保持；正負無限都得到 +Infinity。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 函式 `Register`.

#### 2. BasicDouble

BasicDouble 保留 Integer/Decimal，以固定文化的 NumberStyles.Float 解析文字，其他值回傳 0。Abs 先直接處理一般 Integer，之後才用 Double。

必填：Integer/Decimal 或小數點格式、可帶指數的十進位文字，例如 "-1.25e2"。不受介面語言影響。無效/十六進位文字、Unit、Array、Object 變成 0；十六進位數字常值已是 Integer。可能有 NaN/Infinity。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 函式 `BasicDouble`.

#### 3. BasicAbs

Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到 Decimal。NaN 保持；正負無限都得到 +Infinity。

Integer/Decimal — abs(value). Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到 Decimal。NaN 保持；正負無限都得到 +Infinity。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 函式 `BasicAbs`.

在腳本執行緒本機計算，不連線請求、不移動、不選目標、不等待或修改全域變數。


## 範例

### 直接計算

```vb
# 直接計算
#
# 傳回絕對值。
#
# Integer/Decimal — abs(value). Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到
# Decimal。NaN 保持；正負無限都得到 +Infinity。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

SUB Main()
    # value = -12；預期 12（~ 表示近似）。value 保存結果，CStr 只為 Print 格式化。

    VAR value = Abs(-12)
    UO.Print(CStr(value))
END SUB
```

**參數與執行說明:**

- value = -12；預期 12（~ 表示近似）。value 保存結果，CStr 只為 Print 格式化。

### 用變數傳入不同值

```vb
# 用變數傳入不同值
#
# 傳回絕對值。
#
# Integer/Decimal — abs(value). Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到
# Decimal。NaN 保持；正負無限都得到 +Infinity。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

SUB Main()
    # value = '-2.5'；預期 2.5（~ 表示近似）。value 保存結果，CStr 只為 Print 格式化。

    VAR inputValue = '-2.5'
    VAR value = Abs(inputValue)
    UO.Print(CStr(value))
END SUB
```

**參數與執行說明:**

- value = '-2.5'；預期 2.5（~ 表示近似）。value 保存結果，CStr 只為 Print 格式化。

### 完整可重用輔助函式

```vb
# 完整可重用輔助函式
#
# 傳回絕對值。
#
# Integer/Decimal — abs(value). Integer 保留型別，唯 -2147483648 得到 Decimal 2147483648。Decimal/文字得到
# Decimal。NaN 保持；正負無限都得到 +Infinity。 數值，不是 ID 或成功旗標。此處 1/0 不代表成功/失敗。

# manual-check: scalar-math Abs
SUB Main()
    # value/target 是數字，tolerance 是 >=0 的容差。IsWithin 回傳 Boolean 1/0；負容差得 0。

    VAR value = IsWithin(12,10,2)
    UO.Print(CStr(value))
END SUB

SUB IsWithin(value,target,tolerance)
    IF tolerance < 0 THEN
        RETURN 0
    END IF
    RETURN Abs(CDbl(value)-CDbl(target)) <= tolerance
END SUB
```

**參數與執行說明:**

- value/target 是數字，tolerance 是 >=0 的容差。IsWithin 回傳 Boolean 1/0；負容差得 0。
