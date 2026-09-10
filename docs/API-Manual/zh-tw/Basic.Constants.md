# CONST

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

CONST 宣告一個名稱，其綁定不允許一般重新指定。初始值可以是常值或運算式結果，由引擎在執行宣告時計算。

## 完整語法

```text
CONST name [AS type] = expression [, name ...]
```

## 參數

- `name` — 不加引號的常數名稱，請在範圍內使用不同名稱。程序外的宣告為全域，程序內的宣告則屬於該次呼叫。
- `type` — 可省略的支援 AS 型別，轉換規則與 VAR 相同。例如 AS Integer 轉成引擎的有號 32 位元整數。方括號表示可省略部分，不要在 AS 外輸入方括號。
- `expression` — 必要的初始運算式：數字、引號文字、TRUE/FALSE、算術或支援函式的結果。每次執行此宣告時計算一次，不是整個檔案永久只計算一次。

## 傳回值

沒有值。CONST 是宣告，不是函式或邏輯查詢。讀取名稱可取得已存的初始值。範例中的 RETURN 屬於 Main 或 ApplyLimit。

## 行為

- 一般指定、LET、SET 都不能取代此綁定，否則會產生修改常數的錯誤。TRY/CATCH 可處理此執行錯誤。Option Explicit 要求宣告，但不會在啟動前找出所有無效指定。
- 新的最上位執行會初始化全域常數；被呼叫程序會繼承其常數標記與 AS 型別。區域常數在宣告執行時初始化。因此，作為初始運算式的函式可能在下次啟動再次工作。
- 保護的是名稱綁定，不會凍結 Array/Object 的內部內容。另一個區域宣告可遮蔽全域名稱，重新宣告會建立新的綁定。請避免重複使用常數名稱。
- 引擎計算初始值、套用 AS 轉換，並在範圍內標記常數。之後的一般指定會先檢查標記，再決定是否可變更。純量常值範例不會執行遊戲動作。

## 範例

### 1. 使用固定延遲計算

```vb
# delay 是值為 350 的區域 Integer 常數。乘以 2 建立另一個變數 doubled=700。Main 傳回 700；本範例沒有實際等待。
Option Explicit On
SUB Main()
    CONST delay AS Integer = 350
    VAR doubled = delay * 2
    RETURN doubled
END SUB
```

**參數與執行說明:**

delay 是值為 350 的區域 Integer 常數。乘以 2 建立另一個變數 doubled=700。Main 傳回 700；本範例沒有實際等待。

### 2. 傳入全域上限

```vb
# limit 是值為 50 的全域 Integer 常數。ApplyLimit 收到 amount=72、maximum=50，傳回較小的數量 50。輔助函式已完整定義，且只讀取參數。
Option Explicit On
CONST limit AS Integer = 50
FUNCTION ApplyLimit(amount, maximum)
    IF amount > maximum THEN
        RETURN maximum
    END IF
    RETURN amount
END FUNCTION
SUB Main()
    RETURN ApplyLimit(72, limit)
END SUB
```

**參數與執行說明:**

limit 是值為 50 的全域 Integer 常數。ApplyLimit 收到 amount=72、maximum=50，傳回較小的數量 50。輔助函式已完整定義，且只讀取參數。

### 3. 處理禁止的重新指定

```vb
# limit 初值為 3。指定 4 會產生錯誤，不會改變常數。CATCH 將錯誤放入 problem，並設 caught=TRUE。Main 傳回邏輯值 1；此處 TRUE 等同於 1。
Option Explicit On
SUB Main()
    CONST limit = 3
    VAR caught = FALSE
    TRY
        limit = 4
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**參數與執行說明:**

limit 初值為 3。指定 4 會產生錯誤，不會改變常數。CATCH 將錯誤放入 problem，並設 caught=TRUE。Main 傳回邏輯值 1；此處 TRUE 等同於 1。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: constDeclaration / globalConst
Runtime/DefinitionCollector.cs: VisitGlobalConst
Runtime/Interpreter.cs: VisitConstDef
Runtime/SemanticScope.cs: DefineVar / SetVar
-->
