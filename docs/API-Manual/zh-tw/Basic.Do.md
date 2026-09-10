# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Do 可在本體前或後檢查條件。While 在真時繼續；Until 在真時結束。Repeat … Until 是支援的舊式寫法，於本體後檢查。

## 完整語法

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## 參數

- `condition / While / Until` — 數字布林運算式 0/False 或 1/True。While 為真時繼續，Until 為真時離開。每次檢查重新求值；文字不解析為 Boolean。
- `position / Repeat` — Do 後的條件可略過第一輪。Loop 後或 Repeat 的 Until 條件，至少在執行一輪後才檢查。只能選一個條件位置。無條件 Do … Loop 需要明確離開。
- `statements / exit` — 迴圈本體。Continue Do 前往下一個條件檢查；Exit Do 離開最近的 Do 或 Repeat。Break 離開最近的任意種類迴圈；RETURN 結束整個程序或函式。

## 傳回值

Do、Loop、Repeat、Until、Exit Do 不回傳值。範例由 Main 明確回傳 Integer 1、33、83：這是計數值的組合，不是命令的布林結果。

## 行為

- 準備階段配對區塊並檢查跳轉。同一個 Do 的開頭與結尾同時指定條件會產生 SC020。引擎在所選位置求值，依 While/Until 規則重複。
- 後置條件迴圈中的 Continue Do 仍會檢查後置條件；前置條件迴圈則返回標頭。跳轉離開 Try 前，對應 Finally 恰好執行一次。
- Repeat 先執行：進入前要防範空陣列。沒有隱含逾時。等待遊戲事件時使用 Wait 與期限；暫停、停止檢查仍有效。

## 範例

### 1. 之前與之後

```vb
# ready=True 已滿足 Until。Do Until ready 執行零輪：before=0。第二個迴圈增加 after 之後才檢查，因此 after=1。Main 回傳 before*10+after=1。
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**參數與執行說明:**

ready=True 已滿足 Until。Do Until ready 執行零輪：before=0。第二個迴圈增加 after 之後才檢查，因此 after=1。Main 回傳 before*10+after=1。

### 2. 有限嘗試與清理

```vb
# attempts 從 0 開始，每輪增加。前兩次 Continue Do 執行 Finally，再檢查 attempts<4。第三次 Exit Do 同樣執行 Finally。attempts=3、cleanup=3，結果 33。這是本機模擬，不是真正的網路重試。
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**參數與執行說明:**

attempts 從 0 開始，每輪增加。前兩次 Continue Do 執行 Finally，再檢查 attempts<4。第三次 Exit Do 同樣執行 Finally。attempts=3、cleanup=3，結果 33。這是本機模擬，不是真正的網路重試。

### 3. 舊式結束標記迴圈

```vb
# values=[3,5,0] 已知不為空。Repeat 讀儲存格、增加 index、累計 total。Until 在值為零或到達長度時結束；找到零時 OrElse 略過第二個檢查。total=8、index=3，回傳 83。
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**參數與執行說明:**

values=[3,5,0] 已知不為空。Repeat 讀儲存格、增加 index、累計 total。Until 在值為零或到達長度時結束；找到零時 OrElse 略過第二個檢查。total=8、index=3，回傳 83。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
