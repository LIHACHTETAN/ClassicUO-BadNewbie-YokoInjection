# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

使用 +=、-=、*=、/= 更新既有變數或陣列元素。引擎讀取目前值、運算並寫回，不會重複計算目標。

## 完整語法

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## 參數

- `target` — target：既有純量名稱或 items[index]、grid[x][y] 等元素。元素必須初始化，從零開始的索引須有效。這不會宣告變數。
- `operator` — += 與 &= 將數字相加或連接兩個 String；-= 減、*= 乘、/= 除。預處理器把 &= 改成 +=，所以 5 &= 3 會存入 8。String 與數字需明確使用 CStr。每個運算子須連寫成單一符號。
- `value` — value：目標與索引之後僅計算一次的運算式。種類須符合操作；數字加入 String 前請用 CStr 轉換。

## 傳回值

無值（Unit）。這是陳述式，不是運算式或成功旗標。下一行讀取 target 即可取得儲存結果。純量寫回套用 AS：Integer 5 經 /=2 儲存 Integer 2，未限定型別的數值變數則收到 Decimal 2.5。

## 行為

- 每個陣列參考在計算索引前固定。索引由左至右計算一次，邊界在右運算元前檢查。即使索引或右側的 ByRef 函式替換陣列變數或父層元素，選取的儲存格仍是目標。
- 沿用 +、-、*、/ 規則：整數以有號32位元溢位，/ 產生 Decimal，浮點除以零可能為 Infinity/NaN。String 與數字混合相加會失敗。陣列元素不套用純量 AS 轉換。
- 未宣告目標、未初始化元素、無效索引、不相容操作、CONST 寫入或轉換失敗會產生可攔截錯誤。最終寫入不發生，但運算元函式已產生的副作用不會復原。CONST 和 AS 在純量寫回時才檢查，右側可能已執行。
- Option Explicit 在執行前檢查名稱。中斷點和變數觀察使用原始行號；忙碌迴圈仍檢查暫停和停止。讀取、計算、寫回不是並行程序間的不可分割同步操作。

## 範例

### 1. 四種運算

```vb
# amount 起始為10。+=2 得12，-=3 得9，*=4 得36，/=2 得 Decimal 18。Main 傳回儲存值，指定陳述式本身不傳回值。
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**參數與執行說明:**

amount 起始為10。+=2 得12，-=3 得9，*=4 得36，/=2 得 Decimal 18。Main 傳回儲存值，指定陳述式本身不傳回值。

### 2. 索引只算一次

```vb
# NextIndex 增加 ByRef 參數 calls 並傳回0。items[0] 起始為5，+=2 改成7。函式只呼叫一次，所以 calls=1。Main 傳回 items[0]*10+calls=71。輔助函式完整提供。
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**參數與執行說明:**

NextIndex 增加 ByRef 參數 calls 並傳回0。items[0] 起始為5，+=2 改成7。函式只呼叫一次，所以 calls=1。Main 傳回 items[0]*10+calls=71。輔助函式完整提供。

### 3. 處理受保護常數

```vb
# limit 是 CONST 5。limit+=1 在寫回時出錯；CATCH 將錯誤存入 problem，設定 caught=TRUE。limit 仍為5。Main 以明確 CStr 傳回 "5:1"。旗標代表錯誤處理，不是指定的回傳值。 以變數組合文字：report=CStr(limit)，接著 report &= ":" 與 report &= CStr(caught)。每次 &= 更新 report；Return report 得到 "5:1"。
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**參數與執行說明:**

limit 是 CONST 5。limit+=1 在寫回時出錯；CATCH 將錯誤存入 problem，設定 caught=TRUE。limit 仍為5。Main 以明確 CStr 傳回 "5:1"。旗標代表錯誤處理，不是指定的回傳值。 以變數組合文字：report=CStr(limit)，接著 report &= ":" 與 report &= CStr(caught)。每次 &= 更新 report；Return report 得到 "5:1"。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
