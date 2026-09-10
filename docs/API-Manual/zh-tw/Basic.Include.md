# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Include 在解析及執行前載入其他原始碼檔案，讓主腳本使用其中的函式與變數；不會自動啟動程序或執行緒。

## 完整語法

```text
Include "fileName"
```

## 參數

- `fileName` — fileName：以單引號或雙引號括住的非空檔名。接受相對與絕對路徑；必須是字面路徑，不能用變數或運算式。副檔名不限，內容必須是本引擎支援的原始碼。

## 傳回值

沒有回傳值：這是原始碼準備指示詞。不可將 Include(...) 指派給變數，也不會得到 ID、TRUE/FALSE 或 1/0。載入的函式以 RETURN 回傳自己的值。

## 行為

- Include 必須單獨一行，位於 SUB/FUNCTION 之外。先找呼叫檔案旁邊，再找其 Include 子資料夾。巢狀路徑相對於目前的函式庫。使用相對路徑前先儲存主檔。
- 每個完整路徑只載入一次。A → B → A 循環產生 SC016。路徑、存取或語法錯誤會在全域初始化前阻止執行。診斷與偵錯器保留原始檔名及行號。
- 字串常值與 SUB/FUNCTION 必須在開始它們的同一檔案內結束。重複宣告全域變數或常數會在執行前產生 SC017。
- 下次啟動會讀取已修改的函式庫；已準備或執行中的腳本保留原始碼快照。不會複製設定檔或啟動其他腳本。
- 每個檔案可在自己的宣告前設定 Option Explicit；未設定時繼承主檔。宣告共用名稱空間，不會自動建立模組。
- 以 UTF-8 讀取並辨識 BOM。限制：含主檔共 128 個檔案、32 層巢狀、16,777,216 個原始碼字元。註解或字串中的 Include 不會載入檔案。
- 每個範例放在獨立資料夾。依顯示的名稱與子資料夾儲存 Main.bas 及所有檔案。現成檔案位於 API Manual/Examples/Basic.Include/1、/2、/3。執行 Main.bas，不要把全部內容合併成一個檔案。

## 範例

### 1. 共用函式

```vb
# Main.bas 載入 Common.bas 並呼叫 Add(4, 7)。left、right 以值傳遞；Add 回傳總和，Main 回傳 Integer 11。Common.bas 不會自行啟動。
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**參數與執行說明:**

Main.bas 載入 Common.bas 並呼叫 Add(4, 7)。left、right 以值傳遞；Add 回傳總和，Main 回傳 Integer 11。Common.bas 不會自行啟動。

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. 巢狀函式庫

```vb
# Main.bas 載入 lib/Route.bas，後者從自己的 lib 資料夾載入 Math.bas。Distance(-3, 5) 將 dx=-3、dy=5 傳給 Manhattan；Abs 去除正負號，總和為 Integer 8。此計算不會移動角色。
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**參數與執行說明:**

Main.bas 載入 lib/Route.bas，後者從自己的 lib 資料夾載入 Math.bas。Distance(-3, 5) 將 dx=-3、dy=5 傳給 Manhattan；Abs 去除正負號，總和為 Integer 8。此計算不會移動角色。

**lib/Route.bas**

```vbnet
Option Explicit On
Include "Math.bas"
FUNCTION Distance(ByVal dx, ByVal dy)
    RETURN Manhattan(dx, dy)
END FUNCTION
```

**lib/Math.bas**

```vbnet
Option Explicit On
FUNCTION Manhattan(ByVal dx, ByVal dy)
    RETURN Abs(dx) + Abs(dy)
END FUNCTION
```

### 3. 重複載入

```vb
# Common.bas 與 ./Common.bas 是同一檔案，CONST 與函式只宣告一次。SharedValue=7；GetShared() 回傳 7，Main 乘以 2 並回傳 Integer 14。兩個檔案都使用 Option Explicit On。
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**參數與執行說明:**

Common.bas 與 ./Common.bas 是同一檔案，CONST 與函式只宣告一次。SharedValue=7；GetShared() 回傳 7，Main 乘以 2 並回傳 Integer 14。兩個檔案都使用 Option Explicit On。

**Common.bas**

```vbnet
Option Explicit On
CONST SharedValue = 7
FUNCTION GetShared()
    RETURN SharedValue
END FUNCTION
```

<!-- implementation references (not callable script procedures):
Parsing/ScriptSourceGraph.cs: Load / Builder.AddInclude / ResolveLine
Runtime/InjectionRuntime.cs: Prepare / Load
Runtime/Interpreter.cs: Location / EvaluateInitializer / CallObserved
Analysis/SanityAnalyzer.cs: Analyze
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: PrepareScriptForExecution
InjectionScript.Lsp/Workspace.cs: UpdateDiagnostic
-->
