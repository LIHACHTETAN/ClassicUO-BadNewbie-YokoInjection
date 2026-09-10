# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

GoTo 將執行移至目前程序或函式中的具名標籤。標籤只是程式位置，不是可呼叫的程序。一般流程請優先使用 If、迴圈與 Return。

## 完整語法

```text
GoTo label
label:
```

## 參數

- `label` — 在同一程序內，以獨立一行 label: 宣告的識別名稱。跳轉寫成 GoTo label，不加引號、括號或目標後的冒號。可向前或向後跳轉，不區分大小寫。不同程序可重用名稱。名稱可含點號，但不代表模組成員。數字、計算式與其他程序的標籤不是支援的目標。

## 傳回值

GoTo 與 label: 不傳回值，也不以 1/0 或 TRUE/FALSE 表示成功。範例中的 Main 明確 Return 自行計算的 Integer -1、6 與 123。

## 行為

- 準備階段記錄標籤位址，讀完整個程序後解析跳轉。執行時使用已解析位址，不會重新搜尋原始碼。變數值會保留，先前的操作不會回復。
- 未知目標產生 SC009，客戶端會阻止執行。同一程序內重複名稱，即使大小寫不同，也會在初始化前產生 SC021。Include 診斷保留原始檔案與行號。目標後多餘字元可能產生警告，請使用正確語法。
- 離開作用中的 Try 時，會由內而外執行各 Finally，之後才到目標。在同一作用中 Try 內跳轉會保留該區塊。Finally 發生錯誤可能使目標無法到達。
- 請從正常開頭進入迴圈及 Try/Catch/Finally。跳入中間不會重建被略過的初始化或執行狀態，不能用來恢復區塊。一般迴圈控制請用 Continue 或 Exit。
- 向後跳轉沒有自動次數限制、逾時或等待。必須主動改變結束條件。正常流程也會通過標籤，請用跳轉或 Return 略過不應執行的區段。GoTo 不會安裝錯誤處理器，請參閱 On Error。

## 範例

### 1. 向前分支

```vb
# amount=0 選擇 NoItems 並設 result=-1，接著經過 Finished 傳回 -1。amount=4 時，正常路徑設為 40，GoTo Finished 略過 NoItems。兩個標籤都屬於 Main，不是函式呼叫。
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**參數與執行說明:**

amount=0 選擇 NoItems 並設 result=-1，接著經過 Finished 傳回 -1。amount=4 時，正常路徑設為 40，GoTo Finished 略過 NoItems。兩個標籤都屬於 Main，不是函式呼叫。

### 2. 限制重複次數

```vb
# attempt 從 0 開始，在判斷前遞增。Again 與 again 是同一標籤。三次分別加上 1、2、3；之後 attempt<3 為假，Return 得到 6。total 在標籤前初始化，不會因跳轉而歸零。
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**參數與執行說明:**

attempt 從 0 開始，在判斷前遞增。Again 與 again 是同一標籤。三次分別加上 1、2、3；之後 attempt<3 為假，Return 得到 6。total 在標籤前初始化，不會因跳轉而歸零。

### 3. 離開巢狀 Try

```vb
# trace 成為 1，GoTo Finished 略過 trace=99。內層 Finally 接上數字 2，外層接上 3，然後才到 Finished 並傳回 123。這次跳轉讓每個 Finally 各執行一次。
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**參數與執行說明:**

trace 成為 1，GoTo Finished 略過 trace=99。內層 Finally 接上數字 2，外層接上 3，然後才到 Finished 並傳回 123。這次跳轉讓每個 Finally 各執行一次。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
