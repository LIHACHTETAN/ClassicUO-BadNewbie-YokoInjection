# Option Explicit

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

要求在執行腳本前宣告變數。這是本引擎 Basic 語言的檔案指示詞，不是 UO 指令，也不是函式呼叫。

## 完整語法

```text
Option Explicit
Option Explicit On
Option Explicit Off
```

## 參數

- `On / Off` — On 啟用嚴格宣告檢查；Off 關閉。Explicit 後省略選項時代表 On。整個檔案沒有此指示詞時，保留原有的非嚴格模式。不要加括號或引號。

## 傳回值

沒有值。指示詞不是運算式，不會傳回 TRUE/FALSE、數字或 ID。範例中的 RETURN 屬於 Main 或 Enough，而非 Option Explicit。

## 行為

- 指示詞只能出現一次，且須放在變數、常數與程序之前。前面可有空白行或註解。重複或放置過晚會產生 SC013，包含稍後嘗試切換至 Off 的情況。
- On 模式下，讀取或指定未宣告變數會產生含原始碼位置的 SC006。陣列名稱、FOR 計數器及方法呼叫的接收物件也會檢查。VAR/DIM/CONST、參數與具名 CATCH 變數均會宣告名稱。FOR VAR 會宣告計數器。
- 區域變數須先宣告再使用。某程序的區域變數不會在另一程序宣告同名變數。全域宣告可供程序使用。此功能檢查名稱，不保證所有分支都已初始化數值。
- 剖析器讀取完整檔案；分析器解析宣告；嚴格檢查錯誤會在第一個指令前阻止執行。重新載入時獨立套用新檔案的模式，不沿用先前腳本的設定。Off 模式仍可能顯示警告，讀取尚不存在的值也可能在執行時失敗。
- 指示詞本身不執行遊戲動作，也不傳送封包。它不代表完全相容 VB.NET，亦不檢查遊戲目標是否存在。

## 範例

### 1. 先宣告再指定

```vb
# On 啟用檢查。DIM 將 count 宣告為 Integer；可成功指定 5。Main 傳回 5。若把 count 改為未宣告的 coutn，SC006 會阻止啟動。
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    RETURN count
END SUB
```

**參數與執行說明:**

On 啟用檢查。DIM 將 count 宣告為 Integer；可成功指定 5。Main 傳回 5。若把 count 改為未宣告的 coutn，SC006 會阻止啟動。

### 2. 參數與全域常數

```vb
# 省略模式代表 On。minimum 是值為 3 的全域常數。amount 在 Enough 是已宣告參數，在 Main 則是另一個區域變數。Enough 比較 5 >= 3，傳回 TRUE，數值為 1。
Option Explicit
CONST minimum = 3
FUNCTION Enough(amount)
    RETURN amount >= minimum
END FUNCTION
SUB Main()
    VAR amount = 5
    RETURN Enough(amount)
END SUB
```

**參數與執行說明:**

省略模式代表 On。minimum 是值為 3 的全域常數。amount 在 Enough 是已宣告參數，在 Main 則是另一個區域變數。Enough 比較 5 >= 3，傳回 TRUE，數值為 1。

### 3. 執行舊腳本

```vb
# Off 允許不用 DIM，以指定建立 legacyCounter。Main 傳回 7。此相容性範例仍可能出現宣告警告；若要嚴格檢查，請宣告變數並使用 On。
Option Explicit Off
SUB Main()
    legacyCounter = 7
    RETURN legacyCounter
END SUB
```

**參數與執行說明:**

Off 允許不用 DIM，以指定建立 legacyCounter。Main 傳回 7。此相容性範例仍可能出現宣告警告；若要嚴格檢查，請宣告變數並使用 On。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: optionExplicit
Analysis/SanityAnalyzer.cs
Analysis/InvalidSymbolVisitor.cs
Runtime/InjectionRuntime.cs
-->
