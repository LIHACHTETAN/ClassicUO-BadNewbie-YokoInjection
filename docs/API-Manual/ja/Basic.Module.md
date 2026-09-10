# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Module は関数、手続き、VAR/DIM、CONST を一つの名前にまとめます。外部からは Tools.Sum や Counter.count、同じモジュール内では短いメンバー名を使えます。

## 正確な構文

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## パラメーター

- `moduleName` — moduleName：Tools などの単純な識別子。大文字と小文字は区別しません。UO は予約名です。重複名と入れ子の Module は禁止です。
- `members` — members：SUB/FUNCTION、スカラー VAR/DIM、CONST、Include、有効な Option Explicit。フィールドには配列やオブジェクトの値も格納できます。モジュール直下の DIM[...] は未対応です。関数で配列を作り VAR に保存してください。
- `member / arguments` — member / arguments：メンバー名と関数の引数。Tools.Sum(2, 3) は left=2、right=3 を渡します。Counter.count の読み出しに括弧は不要です。

## 戻り値

Module 自体は値を返さず、Module(...) として呼び出しません。Tools.Sum(...) は関数の RETURN 値、フィールドは保存された値を返します。比較結果は Integer 1/0 で、条件式や比較では TRUE/FALSE に対応します。任意の数値、ID、個数を一律に真偽値とは扱いません。

## 動作

- ファイル直下に Module を宣言し End Module で閉じます。Include でモジュール全体やメンバーを読み込めます。エラーは元ファイルと行番号を保持します。Option Explicit は物理ファイル単位です。
- 準備時に完全名を収集し、短い参照を現在のモジュールに結び付け、実行前にアクセスを検証します。明示的なローカル引数、VAR、CONST、DIM は同名フィールドを隠します。それ以外はモジュールのフィールド、従来のグローバル変数の順に検索します。
- 独立した実行の開始時に宣言順で初期化します。同じ実行の入れ子呼び出しはフィールド変更を共有します。新しい実行は初期状態に戻り、並列スクリプトとは共有しません。ディスクへの設定保存ではありません。
- 関数／手続きの既定は Public、フィールド／定数は Private です。Private は Module 内だけで使えます。Public / Private を参照してください。
- IDE は完全な手続き名を表示します。必須引数のない公開手続きは一覧から起動でき、非公開ヘルパーは内部用のままです。補完、定義への移動、変数表示は現在のモジュールを考慮します。

## 使用例

### 1. 別モジュールの同名関数

```vb
# Tools.Sum は left=2 と right=3 を足して 5 を返し、Other.Sum は掛けて 6 を返します。完全名で区別でき、Main は Integer 11 を返します。
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

**パラメーターと実行の説明:**

Tools.Sum は left=2 と right=3 を足して 5 を返し、Other.Sum は掛けて 6 を返します。完全名で区別でき、Main は Integer 11 を返します。

### 2. 一回の実行で共有するフィールド

```vb
# count は 0 から始まり、Increment ごとに同じフィールドへ 1 を足します。二回後は before=2、Counter.count=5 を Read も参照できます。Main は 2*10+5、Integer 25 を返します。次の起動では再び 0 です。
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

**パラメーターと実行の説明:**

count は 0 から始まり、Increment ごとに同じフィールドへ 1 を足します。二回後は before=2、Counter.count=5 を Read も参照できます。Main は 2*10+5、Integer 25 を返します。次の起動では再び 0 です。

### 3. 真偽値の戻り値

```vb
# maximum=4 は Limits 内で参照できます。Allowed(3) は Integer 1、Allowed(7) は Integer 0 です。accepted=TRUE と rejected=FALSE で確認し、成功時 Main は Integer 10 を返します。
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

**パラメーターと実行の説明:**

maximum=4 は Limits 内で参照できます。Allowed(3) は Integer 1、Allowed(7) は Integer 0 です。accepted=TRUE と rejected=FALSE で確認し、成功時 Main は Integer 10 を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
