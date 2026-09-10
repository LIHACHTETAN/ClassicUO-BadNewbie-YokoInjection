# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

DIM 建立動態陣列；REDIM 替換其儲存空間。PRESERVE 複製重疊索引的值。維度指定包含在內的上界，而非元素數量。讀取前必須初始化元素。

## 完整語法

```text
DIM name[upper]
DIM name(upper) AS type
DIM grid[xUpper][yUpper]
DIM grid(xUpper, yUpper)
REDIM name[upper]
REDIM PRESERVE name[upper]
name[index] = value
GetArrayLength(name)
```

## 參數

- `name` — name：陣列變數。DIM 宣告它；REDIM 替換現有變數的值。以 items[i]、grid[x][y] 讀寫元素。
- `upper` — upper：轉為 Integer 的運算式，由左至右各計算一次。DIM items[2] 建立索引 0..2 的三格；-1 建立空維度。更小的上界或長度溢位會出錯；實際大小仍受記憶體限制。
- `PRESERVE` — PRESERVE：REDIM 的選用關鍵字，遞迴複製重疊索引。縮小時，超出新邊界的值會丟失。不加此字時，新格子尚未初始化。
- `AS type` — AS type：DIM 陣列宣告接受的註記，不會限制、初始化或轉換元素型別。同一陣列可存放不同種類的值。

## 傳回值

DIM 與 REDIM 不回傳值（Unit）。items[i] 回傳儲存值及其實際種類：Integer、Decimal、String、Array 或 Object。讀取未初始化的格子會出錯，不是回傳 0 或 FALSE。GetArrayLength(array) 回傳 Integer 外層長度；非陣列回傳 0。

## 行為

- DIM grid(1, 2) 等同 grid[1][2]，即兩列、每列三格。邊界內的函式呼叫會保留。存取仍寫 grid[1][2]；運算式中的圓括號表示函式呼叫。
- 一般指派與 ByVal 傳參複製的是參考，不是元素。別名會看到共用格子的修改。REDIM 綁定新陣列，舊別名仍指向舊陣列。PRESERVE 複製巢狀陣列中重疊座標，並非任意物件的完整深層複製。
- 只支援從零開始的索引。DIM items[2]=5 及 REDIM 的行內初始化式會以 SC014 拒絕；請逐格另行指派。錯誤索引、缺少元素或未初始化的讀取會產生可捕捉錯誤。
- 這是本專案的 Basic 方言；動態元素種類及多維 PRESERVE 與 VB.NET 型別化陣列不同。儲存的布林值使用 1/0；一般數字或陣列長度並非成功旗標。
- RETURN array 回傳陣列參照，建立函式結束後資料仍有效。將結果指定給其他變數不會複製元素，因此共用函式可為 Module 欄位建立陣列。不同的腳本啟動在重新執行 DIM 時會建立各自的新陣列。

## 範例

### 1. 加總已初始化元素

```vb
# Abs(-2) 得到上界 2：Main 建立三格，寫入 2、4、6。Sum 以 ByVal 接收共用參考，遍歷 0..GetArrayLength(items)-1，回傳 12。完整輔助函式不修改元素，也可處理空陣列。
Option Explicit On
FUNCTION Sum(ByVal items)
    VAR total = 0
    VAR i = 0
    FOR i = 0 TO GetArrayLength(items) - 1
        total += items[i]
    NEXT
    RETURN total
END FUNCTION
SUB Main()
    DIM items(Abs(-2))
    items[0] = 2
    items[1] = 4
    items[2] = 6
    RETURN Sum(items)
END SUB
```

**參數與執行說明:**

Abs(-2) 得到上界 2：Main 建立三格，寫入 2、4、6。Sum 以 ByVal 接收共用參考，遍歷 0..GetArrayLength(items)-1，回傳 12。完整輔助函式不修改元素，也可處理空陣列。

### 2. 擴充並保留內容

```vb
# values 原有 7、8。REDIM PRESERVE values(2) 建立三格，複製索引 0、1。新格子 2 必須初始化為 9。Main 回傳 7*100+8*10+9=789。
Option Explicit On
SUB Main()
    DIM values[1]
    values[0] = 7
    values[1] = 8
    REDIM PRESERVE values(2)
    values[2] = 9
    RETURN values[0] * 100 + values[1] * 10 + values[2]
END SUB
```

**參數與執行說明:**

values 原有 7、8。REDIM PRESERVE values(2) 建立三格，複製索引 0、1。新格子 2 必須初始化為 9。Main 回傳 7*100+8*10+9=789。

### 3. 觀察別名與新儲存空間

```vb
# grid 有兩列，每列兩格。alias 共用陣列，因此 alias[0][1]=9 也修改 grid。PRESERVE 將 grid 擴為三列並保留 9，alias 仍有兩列。"9:3:2" 表示保留值、新外層長度、舊別名長度。
Option Explicit On
SUB Main()
    DIM grid[1][1]
    grid[0][1] = 4
    VAR alias = grid
    alias[0][1] = 9
    REDIM PRESERVE grid[2][1]
    RETURN CStr(grid[0][1]) + ":" + CStr(GetArrayLength(grid)) + ":" + CStr(GetArrayLength(alias))
END SUB
```

**參數與執行說明:**

grid 有兩列，每列兩格。alias 共用陣列，因此 alias[0][1]=9 也修改 grid。PRESERVE 將 grid 擴為三列並保留 9，alias 仍有兩列。"9:3:2" 表示保留值、新外層長度、舊別名長度。

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
