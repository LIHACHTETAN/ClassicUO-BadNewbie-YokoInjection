# String + / &

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

以 + 或 Basic 相容寫法 & 串接文字。將數量、座標等數字加入訊息前，請先用 CStr 明確轉換。

## 完整語法

```text
leftText + rightText
leftText & rightText
"label" & CStr(number)
```

## 參數

- `leftText` — 左側文字：常值、String 變數或已轉成文字的函式結果。
- `rightText` — 右側文字。CStr(number) 轉換數字，CStr(Unit) 得到空字串。空格、冒號等分隔符號需自行提供。

## 傳回值

兩個運算元都是 String 時傳回 String，不是成功旗標。本引擎將 & 正規化為 + 並沿用其規則：兩個數字會相加，2 & 3 得到 Integer 5。混合 String 與數字會出錯，與 VB 隱含文字轉換不同。

## 行為

- 兩側依順序計算並串接，連續串接由左至右。數值運算請加括號，先轉換結果再串接。
- 不會自動插入分隔符號、空格、引號或換行。字串常值內的 & 保持原樣。邏輯權杖 && 仍為 AND，不會串接文字。
- CStr 以不受客戶端語言影響的格式輸出數字，小數使用句點。轉換與串接本身不列印或傳送訊息；有需要時再將結果 String 傳入 API。
- 字串不可變更，串接會建立新值而不修改來源變數。持續擴增大字串會複製內容；請只建立需要的輸出，避免每次迴圈都重建整份報告。

## 範例

### 1. 數量加上標籤

```vb
# amount=50 是 Integer，CStr(amount) 產生 "50"。"Items: " 包含冒號與尾端空格。Main 傳回 "Items: 50"，不會自動列印。
Option Explicit On
SUB Main()
    VAR amount = 50
    RETURN "Items: " & CStr(amount)
END SUB
```

**參數與執行說明:**

amount=50 是 Integer，CStr(amount) 產生 "50"。"Items: " 包含冒號與尾端空格。Main 傳回 "Items: 50"，不會自動列印。

### 2. 完整可重用格式函式

```vb
# Label 接收 name="ore"、amount=3，串接名稱、明確提供的冒號與 CStr(amount)。完整函式將 "ore:3" 傳回 Main，也可用於其他名稱和數量。
Option Explicit On
FUNCTION Label(name, amount)
    RETURN name + ":" + CStr(amount)
END FUNCTION
SUB Main()
    RETURN Label("ore", 3)
END SUB
```

**參數與執行說明:**

Label 接收 name="ore"、amount=3，串接名稱、明確提供的冒號與 CStr(amount)。完整函式將 "ore:3" 傳回 Main，也可用於其他名稱和數量。

### 3. 先計算再串接

```vb
# CStr(2+3) 先算出 5，再轉成 "5"。第二個常值保留分號、空格和 A&B。Main 傳回 "Total: 5; literal: A&B"。
Option Explicit On
SUB Main()
    RETURN "Total: " & CStr(2 + 3) & "; literal: A&B"
END SUB
```

**參數與執行說明:**

CStr(2+3) 先算出 5，再轉成 "5"。第二個常值保留分號、空格和 A&B。Main 傳回 "Total: 5; literal: A&B"。

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: ProtectLiteralText / ReplaceConcatenationOutsideLiterals
Runtime/InjectionValue.cs: operator + / explicit operator string
Runtime/InjectionApi.cs: CStr
-->
