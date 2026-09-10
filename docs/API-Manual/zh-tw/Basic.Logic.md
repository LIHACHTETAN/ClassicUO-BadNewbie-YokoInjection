# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

NOT 反轉條件。AND 要求兩個條件都成立，OR 至少一個，XOR 恰好一個。&& 是 AND 的別名，|| 是 OR 的別名。關鍵字不區分大小寫。

## 完整語法

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## 參數

- `left` — 二元運算的左條件。AND/OR 需要 Integer 或 Decimal：零是假，任何非零數字是真。
- `right` — 右條件，AND/OR 同樣要求數值。兩個運算元都會計算；AND 左側為假或 OR 左側為真，均不會跳過此運算式。
- `NOT / grouping` — 使用 NOT 時請將整個要反轉的條件括起。混合 AND、OR、XOR 時，以括號明確分組。

## 傳回值

Integer 1（TRUE）或 Integer 0（FALSE）。這是邏輯運算而非位元運算：2 AND 4 傳回 1，不是位元遮罩。傳回旗標可用 =TRUE 或 =1、=FALSE 或 =0 檢查。

## 行為

- 本引擎的 AND、OR、XOR 優先順序相同且由左至右：TRUE OR FALSE AND FALSE 得到 0，TRUE OR (FALSE AND FALSE) 得到 1。改寫 VB 程式時請注意此相容規則。
- NOT(condition) 計算條件並反轉真假。在比較開頭，NOT 1=2 等同 NOT(1=2)。若要將反轉值本身作為比較運算元，請寫 (NOT value)。
- AND/OR 拒絕 String、Array、Object、Unit。既有 NOT 和 XOR 則檢查是否等於數值零：文字 "0"、空字串、陣列、物件和 Unit 都算非零。請為這些值明確建立數值判斷；CBool 有自己的轉換規則。
- 每個右側運算式均執行，包含函式呼叫、等待和錯誤。括號只改變分組，不會省略計算。若後續運算式必須在前一條件成功後才執行，請使用巢狀 IF。

## 範例

### 1. 合併命名旗標

```vb
# ready=TRUE，blocked=FALSE。NOT(blocked) 得到 1，因此 canRun 為 1。ready XOR blocked 為真，因為恰好一個旗標為真。Main 傳回 canRun*10+exclusive=11。
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**參數與執行說明:**

ready=TRUE，blocked=FALSE。NOT(blocked) 得到 1，因此 canRun 為 1。ready XOR blocked 為真，因為恰好一個旗標為真。Main 傳回 canRun*10+exclusive=11。

### 2. 觀察兩次呼叫

```vb
# Mark 增加以 ByRef 傳入的 counter 並傳回 TRUE。Main 從 counter=0 開始。FALSE AND Mark(counter) 仍然呼叫 Mark；TRUE OR Mark(counter) 再次呼叫。條件結果為 0、1，而 Main 傳回 counter=2。Mark 完整列出。
Option Explicit On
FUNCTION Mark(ByRef counter)
    counter = counter + 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR counter = 0
    VAR first = FALSE AND Mark(counter)
    VAR second = TRUE OR Mark(counter)
    RETURN counter
END SUB
```

**參數與執行說明:**

Mark 增加以 ByRef 傳入的 counter 並傳回 TRUE。Main 從 counter=0 開始。FALSE AND Mark(counter) 仍然呼叫 Mark；TRUE OR Mark(counter) 再次呼叫。條件結果為 0、1，而 Main 傳回 counter=2。Mark 完整列出。

### 3. 明確分組

```vb
# legacy 先算 TRUE OR FALSE，再 AND FALSE，得到 0。grouped 先算括號中的 FALSE AND FALSE，再與 TRUE 做 OR，得到 1。Main 傳回 legacy*10+grouped=1。
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**參數與執行說明:**

legacy 先算 TRUE OR FALSE，再 AND FALSE，得到 0。grouped 先算括號中的 FALSE AND FALSE，再與 TRUE 做 OR，得到 1。Main 傳回 legacy*10+grouped=1。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
