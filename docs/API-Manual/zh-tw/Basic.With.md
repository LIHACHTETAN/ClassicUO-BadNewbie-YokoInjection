# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

With 將多個操作套用到同一個已保存的物件。成員名稱前的句點指向該物件。Basic 也支援 With UO 與 With moduleName，明確指定命名空間；這兩種形式是引擎擴充。

## 完整語法

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## 參數

- `objectExpression / UO / moduleName` — 必要的接收對象：List()、Dictionary() 等原生物件、保存物件的變數，或傳回物件的函式。進入區塊時只計算一次運算式，即使區塊內容為空也一樣。此引擎不接受數字、字串、陣列或 Unit 作為物件接收對象。同名的區域物件變數優先於模組。
- `.Method(arguments) / .field` — 物件方法必須使用括號，例如 .Add(value)、.Item(index)、.Count()。參數與結果不變，詳見 Basic.List／Basic.Dictionary。此處不支援任意物件欄位或屬性。模組可使用可存取的 .field 與 .Procedure(arguments)，仍遵守 Private 規則。在 With UO 中，.Command(...) 就是 UO.Command(...)；區塊外的遊戲指令仍需要 UO 前綴。
- `statements / End With` — 內容可以為空，也可以包含呼叫、指定、條件與正確巢狀的迴圈或區塊。必須以 End With 結束。區塊外不能使用以句點開頭的成員名稱。其他物件仍可使用完整名稱存取。

## 傳回值

With 是控制區塊，沒有自己的傳回值，不會傳回 ID、Boolean 或成功旗標。每個方法保留原有的傳回契約。範例中的 Return 明確從 Main 傳回 Integer；127、28、72 是範例計算結果。

## 行為

- 準備階段會驗證區塊並繫結相對名稱。進入時，直譯器計算運算式，將物件參考保存在目前呼叫中。重新指定原始變數不會改變這個參考。重新從標頭進入會再次計算；遞迴呼叫各自保存獨立參考。
- 內層 With 的標頭在外層環境中計算。進入內層內容後，句點改為指向內層物件；End With 會還原外層環境。Return、迴圈跳轉與向外的 GoTo 會在相關 Finally 執行後移除離開的範圍。禁止直接跳入 With 內容。
- 接收對象不適用或找不到方法時會產生錯誤，而非 false。可由 Catch／On Error 處理。若接收對象計算失敗，On Error Resume Next 會略過整個區塊。With 不會自行重複、等待或建立執行緒；暫停與停止檢查仍有效。名稱繫結隨準備好的腳本快取，不會在每次呼叫方法時重新計算接收對象。

## 範例

### 1. 只計算一次

```vb
# Choose 以 ByVal 接收 values，以 ByRef 接收 calls，將 calls 增加到 1 並傳回原始清單。雖然中途把新清單指定給 values，兩次 .Add 仍將 2、7 加入保存的原始清單。Item 使用從零開始的索引 0、1。Main 傳回 1*100+2*10+7=127。
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**參數與執行說明:**

Choose 以 ByVal 接收 values，以 ByRef 接收 calls，將 calls 增加到 1 並傳回原始清單。雖然中途把新清單指定給 values，兩次 .Add 仍將 2、7 加入保存的原始清單。Item 使用從零開始的索引 0、1。Main 傳回 1*100+2*10+7=127。

### 2. 巢狀物件與收尾

```vb
# groups 用文字鍵 "child" 保存清單 child。.Item("child") 從外層字典取得該物件。內層的 .Add(2) 與 Finally 中的 .Add(7) 修改清單。End With 之後，.Set("result",8) 再次操作字典。Count() 傳回 2，Item("result") 傳回 8，因此 Main 傳回 28。
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**參數與執行說明:**

groups 用文字鍵 "child" 保存清單 child。.Item("child") 從外層字典取得該物件。內層的 .Add(2) 與 Finally 中的 .Add(7) 修改清單。End With 之後，.Set("result",8) 再次操作字典。Count() 傳回 2，Item("result") 傳回 8，因此 Main 傳回 28。

### 3. 模組欄位與 UO

```vb
# With Tools 指定 .total、.AddAmount、.CountItems 所屬的模組。total 先為 4，AddAmount 以 ByVal 接收 amount=3，得到 7。CountItems 接收含兩個元素的陣列，透過 With UO 呼叫 UO.GetArrayLength(values)，得到 2。Main 計算 7*10+2=72。模組存取規則仍然有效。
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**參數與執行說明:**

With Tools 指定 .total、.AddAmount、.CountItems 所屬的模組。total 先為 4，AddAmount 以 ByVal 接收 amount=3，得到 7。CountItems 接收含兩個元素的陣列，透過 With UO 呼叫 UO.GetArrayLength(values)，得到 2。Main 計算 7*10+2=72。模組存取規則仍然有效。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
