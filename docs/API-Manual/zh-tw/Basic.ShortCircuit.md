# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

AndAlso 與 OrElse 結合條件並略過不必要的右運算元。AndAlso 在左側為假時略過右側；OrElse 在左側為真時略過。可用來保護陣列存取或避免多餘呼叫。

## 完整語法

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## 參數

- `left` — left：首先計算一次的運算式。Integer 或 Decimal 的零是假；任何非零數值都是真。
- `right` — right：只有需要時才計算一次。略過的陣列讀取、函式呼叫及其副作用均不發生。實際計算的運算元必須是數值；文字請明確使用 CBool 轉換。

## 傳回值

Integer 1（TRUE）或 0（FALSE），不是原始運算元。可比較 result=1 或 result=TRUE，以及 result=0 或 result=FALSE。本引擎的真是 1，並非 VB.NET 數值轉換的 -1。一般計數仍是計數；此運算才產生布林結果。

## 行為

- 比較運算位於各運算元內。AndAlso 優先於 OrElse，相同運算子由左至右結合。括號可改變分組。略過的運算式仍會解析並由 Option Explicit 檢查。
- 為維持相容性，連續 AND/OR/XOR 在運算元內先按舊規則由左至右完整計算，然後才處理 AndAlso/OrElse。因此 TRUE OR FALSE AndAlso FALSE 為 FALSE；TRUE OrElse FALSE AND FALSE 為 TRUE。混用時請加括號。AND、OR、&&、|| 仍計算兩側。
- 引擎先計算左值、檢查數值真假，再直接回傳布林值或計算必要的右側。必要運算元的錯誤會傳至 CATCH；FINALLY、暫停與停止檢查仍有效。略過呼叫也代表不執行它的任何動作。

## 範例

### 1. 保護第一個元素

```vb
# FirstEquals 接收 items 與 expected，先檢查 GetArrayLength(items)>0，空陣列便不讀取 items[0]。Main 傳入 [42] 與空陣列，得到 1 和 0，回傳 10。完整輔助函式不修改陣列。
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**參數與執行說明:**

FirstEquals 接收 items 與 expected，先檢查 GetArrayLength(items)>0，空陣列便不讀取 items[0]。Main 傳入 [42] 與空陣列，得到 1 和 0，回傳 10。完整輔助函式不修改陣列。

### 2. 備用呼叫只執行一次

```vb
# Probe 透過 ByRef 增加 calls 並回傳 TRUE。TRUE OrElse Probe(calls) 略過呼叫；FALSE OrElse Probe(calls) 呼叫一次。兩個條件都得到 1，Main 回傳實際呼叫數 1。
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**參數與執行說明:**

Probe 透過 ByRef 增加 calls 並回傳 TRUE。TRUE OrElse Probe(calls) 略過呼叫；FALSE OrElse Probe(calls) 呼叫一次。兩個條件都得到 1，Main 回傳實際呼叫數 1。

### 3. 保護除法與展示優先序

```vb
# AverageExceeds(total, count, limit) 只在 count>0 時相除。(25,0,10) 得到 0；(25,2,10) 因 12.5>10 得到 1。TRUE OrElse FALSE AndAlso FALSE 略過右側 AndAlso 群組，得到 1。Main 回傳 "0:1:1"。
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**參數與執行說明:**

AverageExceeds(total, count, limit) 只在 count>0 時相除。(25,0,10) 得到 0；(25,2,10) 因 12.5>10 得到 1。TRUE OrElse FALSE AndAlso FALSE 略過右側 AndAlso 群組，得到 1。Main 回傳 "0:1:1"。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
