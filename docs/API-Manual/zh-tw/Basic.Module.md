# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Module 將函式、程序、VAR/DIM 與 CONST 放在同一名稱下。外部使用 Tools.Sum 或 Counter.count；目前模組內可以使用成員的短名稱。

## 完整語法

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## 參數

- `moduleName` — moduleName：不區分大小寫的簡單識別字，例如 Tools。UO 為保留名稱。禁止重複模組名稱及巢狀 Module。
- `members` — members：SUB/FUNCTION、純量 VAR/DIM、CONST、Include 及有效的 Option Explicit 指示詞。欄位可以存放陣列或物件。模組內不支援直接宣告 DIM[...]；可由函式建立陣列再存入 VAR。
- `member / arguments` — member / arguments：成員名稱及函式引數。Tools.Sum(2, 3) 傳入 left=2、right=3；欄位 Counter.count 不加括號。

## 傳回值

Module 本身沒有回傳值，不能當作 Module(...) 呼叫。Tools.Sum(...) 回傳該函式的 RETURN 值；欄位傳回儲存的值。比較運算回傳 Integer 1/0，在條件與比較中對應 TRUE/FALSE。一般數字、ID 或數量不能一概視為布林結果。

## 行為

- 在檔案層級宣告 Module，以 End Module 結束。Include 可載入完整模組或其成員；錯誤保留來源檔案與行號。Option Explicit 屬於實體來源檔案。
- 準備階段收集完整名稱，將短名稱綁定至目前模組，並於執行前檢查存取權。明確宣告的區域參數、VAR、CONST 或 DIM 會遮蔽同名欄位；否則先查模組欄位，再查傳統全域變數。
- 每次獨立啟動時，欄位依宣告順序初始化。同一次啟動的巢狀呼叫共用欄位變更。新啟動會重新初始化；並行腳本不共用模組狀態。這不會將設定寫入磁碟。
- 模組函式／程序預設為 Public，欄位／常數預設為 Private。Private 必須位於 Module 內。詳見 Public / Private。
- IDE 顯示完整程序名稱。沒有必要引數的公開程序可從清單啟動；私有輔助程序仍供內部使用。補全、導覽與變數檢視會使用目前模組的範圍。

## 範例

### 1. 不同模組中的同名函式

```vb
# Tools.Sum 將 left=2 與 right=3 相加回傳 5；Other.Sum 將它們相乘回傳 6。完整名稱區分兩個函式，Main 回傳 Integer 11。
Option Explicit On
Module Tools
    Public Function Sum(ByVal left, ByVal right)
        Return left + right
    End Function
End Module
Module Other
    Public Function Sum(ByVal left, ByVal right)
        Return left * right
    End Function
End Module
Sub Main()
    Return Tools.Sum(2, 3) + Other.Sum(2, 3)
End Sub
```

**參數與執行說明:**

Tools.Sum 將 left=2 與 right=3 相加回傳 5；Other.Sum 將它們相乘回傳 6。完整名稱區分兩個函式，Main 回傳 Integer 11。

### 2. 單次執行共用欄位

```vb
# count 從 0 開始。每次 Increment 將相同欄位加 1，兩次後 before=2。Read 可讀到 Counter.count=5。Main 回傳 2*10+5，即 Integer 25。下一次啟動重新從 0 開始。
Option Explicit On
Module Counter
    Public Var count As Integer = 0
    Public Sub Increment()
        count += 1
    End Sub
    Public Function Read()
        Return count
    End Function
End Module
Sub Main()
    Counter.Increment()
    Counter.Increment()
    Var before = Counter.Read()
    Counter.count = 5
    Return before * 10 + Counter.Read()
End Sub
```

**參數與執行說明:**

count 從 0 開始。每次 Increment 將相同欄位加 1，兩次後 before=2。Read 可讀到 Counter.count=5。Main 回傳 2*10+5，即 Integer 25。下一次啟動重新從 0 開始。

### 3. 布林函式結果

```vb
# maximum=4 只能在 Limits 內存取。Allowed(3) 回傳 Integer 1，Allowed(7) 回傳 Integer 0。accepted=TRUE 與 rejected=FALSE 檢查這些結果；成功時 Main 回傳 Integer 10。
Option Explicit On
Module Limits
    Private Const maximum = 4
    Public Function Allowed(ByVal amount)
        Return amount <= maximum
    End Function
End Module
Sub Main()
    Var accepted = Limits.Allowed(3)
    Var rejected = Limits.Allowed(7)
    If accepted = TRUE AndAlso rejected = FALSE Then
        Return 10
    End If
    Return 0
End Sub
```

**參數與執行說明:**

maximum=4 只能在 Limits 內存取。Allowed(3) 回傳 Integer 1，Allowed(7) 回傳 Integer 0。accepted=TRUE 與 rejected=FALSE 檢查這些結果；成功時 Main 回傳 Integer 10。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
