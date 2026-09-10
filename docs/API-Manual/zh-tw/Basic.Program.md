# SUB Main()

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Basic 檔案包含程序/函式定義及可選的全域宣告。可執行動作應放在程序內。以下範例以 Main() 為進入點，都是完整檔案，不是可貼在程序外的片段。

## 完整語法

```text
Option Explicit On
SUB Main()
    statement
END SUB
# comment
; comment
REM comment
// comment
' comment
```

## 參數

- `Main / entry` — 選來執行的程序。Main 是慣用名稱，不是自動執行的指令。SUB Main() 宣告無引數程序。輔助函式只有被呼叫時才工作。
- `statement` — SUB…END SUB 或 FUNCTION…END FUNCTION 內，每行一個可執行陳述式。全域 VAR/CONST 與 Option Explicit 放在外面；Option Explicit 應在宣告之前。
- `comment` — # 和 ; 在引號外開始註解，也可放在程式碼後面。REM、// 和單引號可在縮排後開始整行註解。在字串內，這些字元可以原樣保留。

## 傳回值

載入檔案或宣告 SUB 本身不回傳值。RETURN expression 回傳該值並立即結束目前呼叫。到達程序結尾或使用沒有運算式的 RETURN 會產生 Unit（沒有值）。

## 行為

- 請以 UTF-8 儲存，保留本地化註解與字串。接受 CRLF 和 LF 換行。縮排與空行改善閱讀，但不能代替 END SUB 或 END FUNCTION。
- 關鍵字、程序名稱與變數名稱不區分大小寫：itemCount、ITEMCOUNT、ItemCount 指向同一綁定。文字內容保留大小寫；UO.SetGlobal("Key", …) 的字串鍵是資料，不是識別名稱。
- 簡單名稱以 ASCII 英文字母或底線開頭，後面可接字母、數字或底線。自己的宣告請避開保留字與 API 名稱。UO.Print 是限定名稱呼叫。名稱後的冒號用來定義標籤，不是多個陳述式的通用分隔符號。
- 引擎先正規化支援的 Basic 語法，再解析整個檔案、收集宣告並檢查名稱。因此輔助函式可寫在 Main 下方。載入不會執行所有定義；啟動選定程序後才初始化該次執行並沿著呼叫前進。
- 這些範例僅計算值。確認範本可用後，將需要的 UO 呼叫放入程序本體。上述規則描述本引擎，並不代表支援其他 Basic 的全部功能。

## 範例

### 1. 註解與原樣文字

```vb
# Main 宣告 note 為 "ore #1; keep"。字串內的 # 和 ; 保留。其他 #、REM、// 和單引號註解不執行動作。RETURN 回傳原來文字。
Option Explicit On
# Complete file
SUB Main()
    REM Full-line comment
    VAR note = "ore #1; keep" # Trailing comment
    // Another full-line comment
    ' Another full-line comment
    RETURN note
END SUB
```

**參數與執行說明:**

Main 宣告 note 為 "ore #1; keep"。字串內的 # 和 ; 保留。其他 #、REM、// 和單引號註解不執行動作。RETURN 回傳原來文字。

### 2. 完整定義的輔助函式

```vb
# Main 用 amount=7 呼叫 DoubleCount。函式定義在 Main 下方，將 Integer 參數乘以 2，回傳 14。Main 再傳回此結果。無須缺少的 Include 檔案或未宣告函式。
Option Explicit On
SUB Main()
    RETURN DoubleCount(7)
END SUB
FUNCTION DoubleCount(ByVal amount AS Integer)
    VAR result = amount * 2
    RETURN result
END FUNCTION
```

**參數與執行說明:**

Main 用 amount=7 呼叫 DoubleCount。函式定義在 Main 下方，將 Integer 參數乘以 2，回傳 14。Main 再傳回此結果。無須缺少的 Include 檔案或未宣告函式。

### 3. 名稱大小寫

```vb
# 先宣告 itemCount=3，再透過 ITEMCOUNT 和 itemcount 對同一變數加 2。混合大小寫關鍵字也有效。Main 回傳 5，不會因拼寫大小寫不同而建立額外變數。
Option Explicit On
sUb Main()
    Var itemCount = 3
    ITEMCOUNT = itemcount + 2
    ReTuRn ItemCount
EnD sUb
```

**參數與執行說明:**

先宣告 itemCount=3，再透過 ITEMCOUNT 和 itemcount 對同一變數加 2。混合大小寫關鍵字也有效。Main 回傳 5，不會因拼寫大小寫不同而建立額外變數。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: file / subrutine / LineComment / SYMBOL
Runtime/BasicSyntaxPreprocessor.cs: Process
Runtime/InjectionRuntime.cs: Prepare / Load / CallSubrutineValues
Runtime/SemanticScope.cs: Scope
https://learn.microsoft.com/en-us/dotnet/visual-basic/reference/language-specification/introduction (comparison of identifier casing only)
-->
