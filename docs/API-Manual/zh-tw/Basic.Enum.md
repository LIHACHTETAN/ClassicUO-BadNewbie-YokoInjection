# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

Enum 將有名稱的 Integer 常數組成腳本狀態或模式。請在檔案或 Module 層級宣告，不可放在 Sub/Function 內。這是 VB.NET 列舉的支援子集，不會建立 .NET Enum 物件。

## 完整語法

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## 參數

- `Public / Private` — 預設為 Public，在 Module 內也一樣。Private 只能用於 Module 內，其他模組與檔案層級無法存取該型別及成員。
- `name` — 使用不含點號的單純名稱，例如 Mode，不區分大小寫。UO 與內建型別名称保留；完整名稱不得與 Enum、Module 或全域變數重複。
- `As Integer` — 可省略；底層型別僅支援有號 32 位元 Integer：-2147483648..2147483647。其他型別會被拒絕。變數、參數及 Function 結果中的 As Mode 使用一般 Integer 儲存與轉換，不限制為已列出的成員值。未初始化時為 0。
- `member` — 每行一個單純成員名稱，至少一個。禁止重複名稱、True 及 False。省略運算式時，第一個為 0，後續為前一個值加 1。不同名稱可以共用相同數值。
- `constantExpression` — 可選常數運算式：十進位或 0x 整數、括號、單項負號、+ - * / Mod、前面的成員及已宣告的數字 Const。最終結果必須為範圍內整數，中間除法可產生分數。引用的 Const 也必須求得 Integer，未指定型別或 As Integer/Long/Short/Byte。不可呼叫函式、讀取變數、字串、比較或陣列。禁止向後引用、循環依賴及超過 128 層的依賴。
- `name.member` — 以 Mode.Ready 讀取；從模組外使用 Tools.Mode.Ready，在 Tools 內可省略 Tools。With Mode 允許 .Ready。成員不可變，賦值、+= 或 ByRef 回寫都不能修改常數。Enum 型別不可當函式呼叫。

## 傳回值

宣告本身不回傳值，也不需要呼叫括號。讀取成員回傳 Integer，例如 Mode.Working = 3，是狀態值而非自動成功旗標。state = Mode.Finished 的 Boolean 比較才回傳 1/True 或 0/False，兩種寫法均可使用。狀態 0 可能表示 Idle，不表示失敗。

## 行為

- 準備腳本時，EnumCatalog 不執行腳本/API，僅計算前面的數值常數、自動編號，並檢查名稱、存取及範圍。SC026 即使沒有 Option Explicit 也會阻止啟動。語法錯誤同樣阻止執行；編輯未完成宣告時會顯示診斷。
- DefinitionCollector 在全域初始化與 Optional 預設值之前建立不可變成員，因此這些位置可以引用檔案後方的 Enum。Enum 內的常數運算式仍只能使用前面的常數。預先準備的腳本保留固定目錄；載入其他腳本會替換它。
- ScriptBindings 一次解析模組相對名稱與 Private。執行時讀取一般常數，不在迴圈重算，也不使用反射。As Mode 正規化為 Integer，偵錯器可能顯示 Integer。Include 可提供宣告。沒有 Flags 屬性、System.Enum 方法、隱含成員匯入或自動成員列表。

## 範例

### 1. 為狀態命名

```vb
# Idle=0、Queued=1 自動產生；Working=10 重設編號，因此 Finished=11。state As TaskState 得到 10。Main 以 CStr 轉換數字並回傳 String "0:1:10:11"。可替換為自己的狀態名稱，宣告不會啟動程序。
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**參數與執行說明:**

Idle=0、Queued=1 自動產生；Working=10 重設編號，因此 Finished=11。state As TaskState 得到 10。Main 以 CStr 轉換數字並回傳 String "0:1:10:11"。可替換為自己的狀態名稱，宣告不會啟動程序。

### 2. 隱藏模組狀態

```vb
# Controller.Mode 僅供 Controller 內部使用。NextMode 接收 distance ByVal As Integer，不修改呼叫端的參數。distance<=1 選 Arrived=5，否則 Walking=4；state 起始為 0。Main 傳入 3 與 1，得到 4 與 5，回傳 Integer 45。此例不移動角色，distance 只是輸入資料。外部可以呼叫 Controller.NextMode，不能讀 Controller.Mode.Arrived。
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**參數與執行說明:**

Controller.Mode 僅供 Controller 內部使用。NextMode 接收 distance ByVal As Integer，不修改呼叫端的參數。distance<=1 選 Arrived=5，否則 Walking=4；state 起始為 0。Main 傳入 3 與 1，得到 4 與 5，回傳 Integer 45。此例不移動角色，distance 只是輸入資料。外部可以呼叫 Controller.NextMode，不能讀 Controller.Mode.Arrived。

### 3. 切換狀態並回傳 Boolean

```vb
# 前面的 Integer Const FirstState=2 產生 Idle=2、Working=3、Finished=4。Advance 以 ByRef 接收 state 並修改 Main 的變數；With Mode 縮短名稱，Select Case 選擇轉換。呼叫兩次得到 2→3→4。IsFinal 以 ByVal 接收副本並比較 Finished，因此 Main 回傳 1/True；只轉換一次時為 0/False。再呼叫 Advance 會產生 "No next state"。Mode 常數始終不變。
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**參數與執行說明:**

前面的 Integer Const FirstState=2 產生 Idle=2、Working=3、Finished=4。Advance 以 ByRef 接收 state 並修改 Main 的變數；With Mode 縮短名稱，Select Case 選擇轉換。呼叫兩次得到 2→3→4。IsFinal 以 ByVal 接收副本並比較 Finished，因此 Main 回傳 1/True；只轉換一次時為 0/False。再呼叫 Advance 會產生 "No next state"。Mode 常數始終不變。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
