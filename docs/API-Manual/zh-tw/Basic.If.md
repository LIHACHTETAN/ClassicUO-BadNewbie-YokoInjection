# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

IF 最多選擇一個分支。先檢查 IF，再依序檢查 ELSEIF，直到第一個真條件；都不符合時執行可選的 ELSE。正常情況下接著執行 END IF 之後的程式。

## 完整語法

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## 參數

- `condition` — condition：進入時檢查一次的運算式。數值零是假，非零數字是真。建議使用明確比較或 API 布林結果。
- `elseifCondition` — elseifCondition：可選的額外條件，僅在前面所有條件為假時檢查。ELSEIF 必須寫成一個字。
- `statements / ELSE` — statements / ELSE：後續各行的指令。ELSE 可省略、不帶條件，最多一次且位於最後。THEN、END IF 必須存在，請使用多行區塊。

## 傳回值

不回傳值（Unit）。IF 是控制指令，不是函式。條件或選中分支內的 RETURN 可以產生值。布林 1/0 可與 TRUE/FALSE 比較；IF count 接受任何非零數量，而 IF count=TRUE 只匹配 1。

## 行為

- 編譯器建立條件與結束跳躍。假分支跳至下一條件或 ELSE；選中的分支略過後續選項。巢狀 IF 各有自己的 ELSE。RETURN 離開程序時仍執行包住它的 FINALLY。
- 為相容舊程式，IF 與數值零比較，不會把所有種類都用 CBool 轉換。因此文字 "0"、空文字、陣列、物件、Unit 都走真分支。請明確轉換文字或比較指定屬性。AndAlso/OrElse 則要求數值運算元。
- 略過分支中的宣告不會在執行時建立變數。共用結果應在 IF 前宣告並初始化。Option Explicit 檢查名稱，不保證每條路徑都有指派。多個 ELSE 會在執行前以 SC015 拒絕，即使沒有 Option Explicit。

## 範例

### 1. 四種分類

```vb
# Classify(value) 依序檢查 <0、=0、<10，最後使用 ELSE。-2、0、7、20 得到 negative、zero、small、large。Main 回傳 "negative:zero:small:large"；每次呼叫只執行一個 RETURN。
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**參數與執行說明:**

Classify(value) 依序檢查 <0、=0、<10，最後使用 ELSE。-2、0、7、20 得到 negative、zero、small、large。Main 回傳 "negative:zero:small:large"；每次呼叫只執行一個 RETURN。

### 2. 巢狀決策

```vb
# Action(enabled, amount) 先看 enabled，再以 amount>0 選 work 或 idle。外層 ELSE 得到 disabled。(TRUE,5)、(TRUE,0)、(FALSE,5) 組成 "work:idle:disabled"。每個 END IF 關閉自己的區塊。
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**參數與執行說明:**

Action(enabled, amount) 先看 enabled，再以 amount>0 選 work 或 idle。外層 ELSE 得到 disabled。(TRUE,5)、(TRUE,0)、(FALSE,5) 組成 "work:idle:disabled"。每個 END IF 關閉自己的區塊。

### 3. 觀察條件順序

```vb
# Check(calls,value) 透過 ByRef 增加 calls 並回傳 value。第一條件是假、第二是真，第三條件與 ELSE 被略過。result=7、calls=2，Main 回傳 calls*10+result=27。所有輔助函式均完整提供。
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**參數與執行說明:**

Check(calls,value) 透過 ByRef 增加 calls 並回傳 value。第一條件是假、第二是真，第三條件與 ELSE 被略過。result=7、calls=2，Main 回傳 calls*10+result=27。所有輔助函式均完整提供。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
