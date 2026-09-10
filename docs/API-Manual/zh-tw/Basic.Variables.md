# VAR / DIM

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

VAR 與純量 DIM 宣告具名的值。指定會計算運算式並儲存結果。程序內的宣告只屬於該次呼叫；程序外的宣告則為腳本全域變數。

## 完整語法

```text
VAR name [AS type] [= expression] [, name ...]
DIM name [AS type] [= expression] [, name ...]
name = expression
LET name = expression
SET name = expression
```

## 參數

- `name` — 不加引號的識別名稱。使用英文字母、數字、底線，並以字母或底線開頭。保持拼法一致，不要使用語言關鍵字。
- `type` — 可省略的 AS 型別。Integer/Long/Short/Byte 使用本引擎的有號 32 位元整數轉換；Double/Single/Decimal 使用雙精度數值；String 為文字；Boolean/Bool 為邏輯值；Variant/Object 保留值的種類。這些別名不會套用 VB.NET 各自的 byte/short/long 範圍。
- `expression` — VAR/DIM 的初始運算式可省略；指定的右側運算式必填。執行該行時才計算。AS String 沒有初始值時為空字串；具型別的數字與 Boolean 預設為零。沒有初始值的無型別 VAR 與 VAR AS Variant/Object 會包含 Unit（沒有值），而純量 DIM 會提供 0。未指定型別的變數日後可存放其他種類的值。

## 傳回值

沒有值。VAR、DIM 與指定敘述不傳回結果。讀取名稱會取得已存的值。範例的 RETURN 從 Main 傳回此值，而不是 DIM 的傳回值。

## 行為

- 上述語法中的方括號表示可省略部分；不要在 AS 或初始值外實際輸入方括號。陣列 DIM 使用另一種宣告形式。
- 本引擎的 LET 與 SET 都是一般指定的相容寫法。Option Explicit On 時它們不宣告名稱。AS 型別也套用於後續指定；無效轉換或不支援的型別會造成執行錯誤。
- 區域名稱屬於程序呼叫。在 IF 內宣告不會建立獨立的區塊範圍。未執行的分支不會在執行時建立值。若分支之後需要使用，請先宣告變數。
- Injection 相容規則：被呼叫的程序繼承呼叫端目前的全域純量值及其 AS 型別。被呼叫程序重新指定純量時，不會更新呼叫端。若要更新，請傳回新值或使用 BYREF 引數。這並非對 Array/Object 值進行深層複製。重新啟動主要程序會再次初始化全域變數；區域宣告只遮蔽自身框架的名稱，不取代全域宣告。
- 引擎先計算初始值，在目前範圍定義儲存位置，再套用型別轉換。之後指定時先計算右側。範例僅在本機計算；變數不會自動儲存至設定檔或 JSON 檔案。

## 範例

### 1. 更新整數

```vb
# count 起始為 0，指定為 5，LET 再加 2。Main 傳回 Integer 7。第一個 DIM 宣告名稱，後續指定則更新數值。
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    LET count = count + 2
    RETURN count
END SUB
```

**參數與執行說明:**

count 起始為 0，指定為 5，LET 再加 2。Main 傳回 Integer 7。第一個 DIM 宣告名稱，後續指定則更新數值。

### 2. 文字與邏輯旗標

```vb
# label 起始為空的 String。SET 儲存 "ore"。enabled 是 Boolean TRUE；IF 分支傳回 String "ore"。TRUE 不加引號，代表邏輯值 1。
Option Explicit On
SUB Main()
    DIM label AS String
    VAR enabled AS Boolean = TRUE
    SET label = "ore"
    IF enabled = TRUE THEN
        RETURN label
    END IF
    RETURN "disabled"
END SUB
```

**參數與執行說明:**

label 起始為空的 String。SET 儲存 "ore"。enabled 是 Boolean TRUE；IF 分支傳回 String "ore"。TRUE 不加引號，代表邏輯值 1。

### 3. 全域輸入與區域計算

```vb
# baseAmount 是值為 4 的全域變數。extra 是 Calculate 的區域變數，值為 3。Calculate 傳回 7；Main 存入自己的區域 result 並傳回 7。extra 不是 Main 的區域變數。
Option Explicit On
VAR baseAmount AS Integer = 4
FUNCTION Calculate()
    VAR extra = 3
    RETURN baseAmount + extra
END FUNCTION
SUB Main()
    VAR result = Calculate()
    RETURN result
END SUB
```

**參數與執行說明:**

baseAmount 是值為 4 的全域變數。extra 是 Calculate 的區域變數，值為 3。Calculate 傳回 7；Main 存入自己的區域 result 並傳回 7。extra 不是 Main 的區域變數。

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim
Runtime/Interpreter.cs: VisitVarDef / VisitAssignment
Runtime/SemanticScope.cs: DefineVar / SetVar / Coerce
-->
