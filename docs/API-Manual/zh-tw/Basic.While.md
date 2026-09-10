# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

While 在每次迭代前檢查條件，為真時重複本體。本引擎用 Wend 結束區塊，不支援 VB.NET 的 End While 寫法。

## 完整語法

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## 參數

- `condition` — 每次檢查都重新求值的運算式，包括第一次與最後一次。使用比較或數字布林值：0/False 結束，1/True 與其他非零數字繼續。文字不會被解析為 Boolean。
- `statements` — 執行工作並使條件前進的陳述式。第一次條件為假時，整個本體都被略過。
- `Wend / exit` — Wend 返回條件。Continue While 再次檢查；Exit While 離開最近的 While，即使要跨越內部其他種類的迴圈。Break 離開最近的任意種類迴圈。

## 傳回值

While、Wend、Exit While、Break 不回傳值。本體內的 RETURN 結束整個程序或函式。範例回傳 Integer 6、1、406；搜尋結果 1 是陣列索引，不是布林成功旗標。

## 行為

- 流程是檢查、執行本體、跳回檢查。它不保存數字界限，也不自動增加計數器。
- 必須明確寫出前進方式。反覆查詢遊戲狀態時加入適當 Wait 與期限；While 本身不睡眠，也沒有逾時。執行階段暫停和停止仍可使用。
- Continue 與離開會執行所離開 Try 區塊的 Finally。標頭、各陳述式及 Wend 請在程序或函式內分行書寫。

## 範例

### 1. 數字位數加總

```vb
# DigitSum 以 ByVal 收到 number=123。MOD 10 讀最後一位，Fix(number/10) 移除它：123→12→1→0。total=3+2+1=6。最後一次假條件退出；Main 收到 6。輸入 0 時本體不執行，結果為 0。
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**參數與執行說明:**

DigitSum 以 ByVal 收到 number=123。MOD 10 讀最後一位，Fix(number/10) 移除它：123→12→1→0。total=3+2+1=6。最後一次假條件退出；Main 收到 6。輸入 0 時本體不執行，結果為 0。

### 2. 尋找第一個符合項目

```vb
# FirstAbove 收到 values=[4,7,9]、threshold=6。長度檢查保護 values[index]。index=1 時 7>6 設定 found=1，Exit While 停止搜尋。沒有符合項目時保持 -1；Main 回傳從零起算的索引 1。
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**參數與執行說明:**

FirstAbove 收到 values=[4,7,9]、threshold=6。長度檢查保護 values[index]。index=1 時 7>6 設定 found=1，Exit While 停止搜尋。沒有符合項目時保持 -1；Main 回傳從零起算的索引 1。

### 3. 計算條件求值次數

```vb
# CanContinue 以 ByRef 收到 checks，以 ByVal 收到 index 與 limit=3；增加 checks，再以 1/0 回傳 index<limit。在 index=0、1、2、3 檢查，共四次呼叫、三輪本體。total=6；Main 回傳 406。
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**參數與執行說明:**

CanContinue 以 ByRef 收到 checks，以 ByVal 收到 index 與 limit=3；增加 checks，再以 1/0 回傳 index<limit。在 index=0、1、2、3 檢查，共四次呼叫、三輪本體。total=6；Main 回傳 406。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
