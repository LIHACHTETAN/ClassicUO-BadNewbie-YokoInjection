# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Public 讓外部程式碼存取模組成員；Private 只允許同一模組的函式、程序和初始化式存取。修飾詞放在宣告前，不是呼叫前。

## 完整語法

```text
Public declaration
Private declaration
```

## 參數

- `visibility` — visibility：Public 或 Private。省略時，模組的 SUB/FUNCTION 為公開，VAR/DIM/CONST 為私有。
- `declaration` — declaration：SUB/FUNCTION、純量 VAR/DIM 或 CONST。Public 也可用於 Module 和檔案層级宣告。Private 不可位於檔案層級或程序本體內。宣告成員時名稱不能含點。

## 傳回值

Public 和 Private 不回傳值，也不改變欄位型別或函式結果。Normalize(12) 透過 RETURN 回傳 Integer 10；NextCount() 回傳新的數量，而不是 TRUE/FALSE。

## 行為

- 模組內可用自己的短名稱或完整名稱。外部只能透過 ModuleName.Member 存取 Public。Public 不會建立未限定的全域短名稱。
- 即使 Option Explicit Off，也會在執行前檢查存取。存取其他模組的 Private 產生 SC019；無效的模組／修飾詞宣告產生 SC018 或語法錯誤。這些錯誤之後不執行初始化式。
- 公開函式可以呼叫私有輔助函式；判斷依據是呼叫方函式宣告在哪個模組，而不是誰啟動它。私有程序不能從 IDE、快捷鍵或外部程序 API 單獨啟動。
- Public Const 仍不可修改，Public Var 仍可修改。明確的區域變數只在自己的程序中遮蔽同名欄位。Private 不會加密來源檔案，也不會向擁有者隱藏程式碼。
- 除錯器依選取的呼叫框架解析短名稱及 Private 權限。模組內可讀取欄位；切換至外部呼叫方後，ModuleName.privateField 運算式會被拒絕。

## 範例

### 1. 公開入口和私有輔助函式

```vb
# value=12 傳入 Limits.Normalize，再傳給 Clamp。maximum=10 限制數值，兩個函式都回傳 Integer 10。Main 只呼叫公開的 Normalize；外部直接呼叫 Limits.Clamp(12) 不被允許。
Option Explicit On
Module Limits
    Private Const maximum = 10
    Private Function Clamp(ByVal value)
        If value > maximum Then
            Return maximum
        End If
        Return value
    End Function
    Public Function Normalize(ByVal value)
        Return Clamp(value)
    End Function
End Module
Sub Main()
    Return Limits.Normalize(12)
End Sub
```

**參數與執行說明:**

value=12 傳入 Limits.Normalize，再傳給 Clamp。maximum=10 限制數值，兩個函式都回傳 Integer 10。Main 只呼叫公開的 Normalize；外部直接呼叫 Limits.Clamp(12) 不被允許。

### 2. 私有欄位和區域變數

```vb
# 沒有修飾詞的 VAR value=7 在 Store 中是私有的。Read 回傳欄位值 7；LocalValue 建立自己的 value=9，不改變欄位。Main 回傳 7*10+9，即 Integer 79。
Option Explicit On
Module Store
    Var value = 7
    Public Function Read()
        Return value
    End Function
    Public Function LocalValue()
        Var value = 9
        Return value
    End Function
End Module
Sub Main()
    Return Store.Read() * 10 + Store.LocalValue()
End Sub
```

**參數與執行說明:**

沒有修飾詞的 VAR value=7 在 Store 中是私有的。Read 回傳欄位值 7；LocalValue 建立自己的 value=9，不改變欄位。Main 回傳 7*10+9，即 Integer 79。

### 3. 公開常數、私有計數器

```vb
# Public Const increment=2 可用 Counter.increment 讀取。Private count 從 1 開始。NextCount 加上 increment，儲存並回傳 3。Main 回傳 3*10+2，即 Integer 32。禁止外部存取 Counter.count，也不能修改 increment。
Option Explicit On
Module Counter
    Public Const increment = 2
    Private Var count = 1
    Public Function NextCount()
        count += increment
        Return count
    End Function
End Module
Sub Main()
    Var result = Counter.NextCount()
    Return result * 10 + Counter.increment
End Sub
```

**參數與執行說明:**

Public Const increment=2 可用 Counter.increment 讀取。Private count 從 1 開始。NextCount 加上 increment，儲存並回傳 3。Main 回傳 3*10+2，即 Integer 32。禁止外部存取 Counter.count，也不能修改 increment。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
