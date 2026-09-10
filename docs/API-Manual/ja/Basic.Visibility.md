# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Public はモジュールのメンバーを外部に公開します。Private は同じモジュール内の関数、手続き、初期化式からだけアクセスできます。修飾子は呼び出しではなく宣言の前に書きます。

## 正確な構文

```text
Public declaration
Private declaration
```

## パラメーター

- `visibility` — visibility：Public または Private。省略時はモジュールの SUB/FUNCTION が公開、VAR/DIM/CONST が非公開です。
- `declaration` — declaration：SUB/FUNCTION、スカラー VAR/DIM、CONST。Public は Module とファイル直下の宣言にも使えます。Private はファイル直下や手続き本体内では無効です。宣言名にドットは付けません。

## 戻り値

Public と Private は値を返さず、フィールド型や関数の結果も変えません。Normalize(12) は RETURN で Integer 10 を返し、NextCount() は新しい個数を返します。TRUE/FALSE ではありません。

## 動作

- Module 内では自分の短い名前と完全名を使えます。外部からは ModuleName.Member で Public だけにアクセスできます。Public でも短いグローバル名にはなりません。
- Option Explicit Off でも実行前に検証します。他モジュールの Private へのアクセスは SC019、不正なモジュール／修飾子宣言は SC018 または構文エラーです。その後は初期化式も実行しません。
- 公開関数は非公開ヘルパーを呼べます。判定は呼び出し元関数の宣言モジュールによります。非公開ヘルパーを IDE、ホットキー、外部手続き API から単独起動することはできません。
- Public Const は変更不可、Public Var は変更可能のままです。明示的ローカル変数は自分の手続き内だけで同名フィールドを隠します。Private はソースを暗号化せず、所有者からコードを隠しません。
- デバッガーは選択したフレームで短い名前と Private を解決します。モジュール内では参照でき、外部の呼び出し元に切り替えると ModuleName.privateField は拒否されます。

## 使用例

### 1. 公開窓口と非公開ヘルパー

```vb
# value=12 を Limits.Normalize、次に Clamp へ渡します。maximum=10 で制限し、両関数は Integer 10 を返します。Main は Normalize のみを呼び、外部から Limits.Clamp(12) は呼べません。
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

**パラメーターと実行の説明:**

value=12 を Limits.Normalize、次に Clamp へ渡します。maximum=10 で制限し、両関数は Integer 10 を返します。Main は Normalize のみを呼び、外部から Limits.Clamp(12) は呼べません。

### 2. 非公開フィールドとローカル変数

```vb
# 修飾子のない VAR value=7 は Store 内で非公開です。Read はフィールドの 7、LocalValue は独自の value=9 を返し、フィールドは変わりません。Main は 7*10+9、Integer 79 を返します。
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

**パラメーターと実行の説明:**

修飾子のない VAR value=7 は Store 内で非公開です。Read はフィールドの 7、LocalValue は独自の value=9 を返し、フィールドは変わりません。Main は 7*10+9、Integer 79 を返します。

### 3. 定数は公開、カウンターは非公開

```vb
# Public Const increment=2 は Counter.increment で読めます。Private count は 1 から始まり、NextCount が increment を足して 3 を保存し返します。Main は 3*10+2、Integer 32 を返します。外部から Counter.count へのアクセスや increment の変更は禁止です。
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

**パラメーターと実行の説明:**

Public Const increment=2 は Counter.increment で読めます。Private count は 1 から始まり、NextCount が increment を足して 3 を保存し返します。Main は 3*10+2、Integer 32 を返します。外部から Counter.count へのアクセスや increment の変更は禁止です。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
