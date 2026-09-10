# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

遊戲命令使用 UO.；Basic 語法、內建及自訂函式使用各自宣告的名稱。

## 完整語法

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## 參數

- `UO.command` — UO.command(arguments)：遊戲 API 必須有此前綴。UO.GetType(id) 讀取圖形／身體編號，不是 Basic 或 CLR 型別。
- `BasicFunction` — BasicFunction(arguments)：例如 Int(value)、Str(value)、CInt(value)，不要加 UO.。
- `arguments` — self、backpack、ground、Rhand 仍是物件、篩選或裝備層參數；參數名稱不是省略前綴的命令呼叫。

## 傳回值

命名規則本身沒有回傳值。Int 回傳 Integer，Str 回傳 String；三個 Api*Exists 回傳 Integer 1/0，可當 TRUE/FALSE 使用。

## 行為

- 名稱不分大小寫。InjectionApi 註冊不帶前綴的 Basic；InjectionApiUO 註冊帶 UO. 的遊戲呼叫。舊短名呼叫會產生 SC005 並建議已註冊的 UO. 名稱，不會自動執行替代呼叫。角色屬性值也需要 UO.。ApiNameExists、ApiSignatureExists、ApiParameterExists 去除前後空白後檢查確切的註冊名稱，不會補上前綴；它們檢查中繼資料而非伺服器狀態。未實作 VB.NET 反射運算子 GetType(TypeName)。

## 範例

### 1. 1

```vb
# graphic 讀取角色身體編號，無資料則為 0；whole=2。registered 檢查單一參數的 UO.GetType。Main 不論圖形為何都回傳 "2:1"，不移動或搬運物品。
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**參數與執行說明:**

graphic 讀取角色身體編號，無資料則為 0；whole=2。registered 檢查單一參數的 UO.GetType。Main 不論圖形為何都回傳 "2:1"，不移動或搬運物品。

### 2. 2

```vb
# 完整自訂 Function GetType 接收 CInt(6) 得到的 value=6，回傳 7。UO.GetType 仍讀取遊戲圖形，兩者不會攔截彼此的呼叫。
Option Explicit On
Function GetType(value)
    Return value + 1
End Function
Sub Main()
    Var localResult = GetType(CInt(6))
    Var graphic = UO.GetType('self')
    Return localResult
End Sub
```

**參數與執行說明:**

完整自訂 Function GetType 接收 CInt(6) 得到的 value=6，回傳 7。UO.GetType 仍讀取遊戲圖形，兩者不會攔截彼此的呼叫。

### 3. 3

```vb
# oldCall=0、gameCall=1、basicCall=1 分別檢查 GetType、UO.GetType(id)、Int(value)。argumentName=1 表示 backpack 仍是參數選擇器。Main 回傳 "0:1:1:1"；這些檢查不搜尋自訂程序。
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**參數與執行說明:**

oldCall=0、gameCall=1、basicCall=1 分別檢查 GetType、UO.GetType(id)、Int(value)。argumentName=1 表示 backpack 仍是參數選擇器。Main 回傳 "0:1:1:1"；這些檢查不搜尋自訂程序。

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
