# SUB Main()

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Basic ファイルには手続き/関数定義と任意のグローバル宣言を記述します。実行する処理は手続き内に置きます。以下は Main() を入口とする完全なファイルで、手続き外へ貼る断片ではありません。

## 正確な構文

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

## パラメーター

- `Main / entry` — 実行対象に選ぶ手続き。Main は慣用名で、自動実行の命令ではありません。SUB Main() は引数なしの手続きを宣言します。補助関数は呼ばれたときだけ動作します。
- `statement` — SUB…END SUB または FUNCTION…END FUNCTION 内では1行に1つの実行文を記述します。グローバル VAR/CONST と Option Explicit は外に置き、Option Explicit は宣言より前に記述します。
- `comment` — # と ; は文字列の引用符外でコメントを開始し、コードの後にも置けます。REM、//、アポストロフィは任意のインデント後で行全体のコメントを開始します。文字列内ではそのままの文字として保持できます。

## 戻り値

ファイルの読み込みや SUB 宣言自体は値を返しません。RETURN expression は値を返して現在の呼び出しを即座に終了します。末尾への到達や式なし RETURN は Unit（値なし）になります。

## 動作

- ローカライズされたコメントや文字列を保つため UTF-8 で保存してください。改行は CRLF と LF に対応します。インデントや空行は読みやすさのためで、END SUB や END FUNCTION の代わりにはなりません。
- キーワード、手続き名、変数名は大文字小文字を区別しません。itemCount、ITEMCOUNT、ItemCount は同じ束縛です。文字列の表記は保持され、UO.SetGlobal("Key", …) の文字列キーは識別子ではなくデータです。
- 単純名は ASCII 英字か下線で始め、その後に英字、数字、下線を使います。予約語や API 名を独自宣言に使わないでください。UO.Print は修飾呼び出し名です。名前の後のコロンはラベルを定義し、複数文の汎用区切りではありません。
- エンジンは対応する Basic 構文を正規化し、ファイル全体を解析して宣言を収集し、名前を確認します。そのため補助関数を Main の下に置けます。読み込みですべての定義が動くわけではなく、選択した手続きの開始時に実行を初期化して呼び出しを追います。
- 例は値の計算だけを行います。テンプレートを確認した後、必要な UO 呼び出しを本体に入れます。これは本エンジンの規則であり、他の Basic の全機能の対応を意味しません。

## 使用例

### 1. コメントと文字列

```vb
# Main は note に "ore #1; keep" を設定します。文字列内の # と ; は保持されます。他の #、REM、//、アポストロフィのコメントは何もしません。RETURN は元の文字列を返します。
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

**パラメーターと実行の説明:**

Main は note に "ore #1; keep" を設定します。文字列内の # と ; は保持されます。他の #、REM、//、アポストロフィのコメントは何もしません。RETURN は元の文字列を返します。

### 2. 完全な補助関数

```vb
# Main は amount=7 で DoubleCount を呼びます。Main の下で定義した関数は Integer 引数を2倍し14を返し、Main がその結果を返します。不足した Include ファイルや未宣言関数は不要です。
Option Explicit On
SUB Main()
    RETURN DoubleCount(7)
END SUB
FUNCTION DoubleCount(ByVal amount AS Integer)
    VAR result = amount * 2
    RETURN result
END FUNCTION
```

**パラメーターと実行の説明:**

Main は amount=7 で DoubleCount を呼びます。Main の下で定義した関数は Integer 引数を2倍し14を返し、Main がその結果を返します。不足した Include ファイルや未宣言関数は不要です。

### 3. 識別子の大小文字

```vb
# itemCount=3 を宣言し、ITEMCOUNT と itemcount で同じ変数に2を加えます。混在したキーワードの大小文字も受け付けます。Main は5を返し、表記差で余分な変数は作られません。
Option Explicit On
sUb Main()
    Var itemCount = 3
    ITEMCOUNT = itemcount + 2
    ReTuRn ItemCount
EnD sUb
```

**パラメーターと実行の説明:**

itemCount=3 を宣言し、ITEMCOUNT と itemcount で同じ変数に2を加えます。混在したキーワードの大小文字も受け付けます。Main は5を返し、表記差で余分な変数は作られません。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: file / subrutine / LineComment / SYMBOL
Runtime/BasicSyntaxPreprocessor.cs: Process
Runtime/InjectionRuntime.cs: Prepare / Load / CallSubrutineValues
Runtime/SemanticScope.cs: Scope
https://learn.microsoft.com/en-us/dotnet/visual-basic/reference/language-specification/introduction (comparison of identifier casing only)
-->
