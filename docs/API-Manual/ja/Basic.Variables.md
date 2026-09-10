# VAR / DIM

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

VAR とスカラーの DIM は名前付きの値を宣言します。代入は式を評価して結果を保存します。プロシージャ内の宣言はその呼び出しにローカルで、外の宣言はスクリプト全体で使用できます。

## 正確な構文

```text
VAR name [AS type] [= expression] [, name ...]
DIM name [AS type] [= expression] [, name ...]
name = expression
LET name = expression
SET name = expression
```

## パラメーター

- `name` — 引用符なしの識別名。英字、数字、アンダースコアを使い、英字またはアンダースコアで始めます。同じ綴りを使い、言語の予約語を避けてください。
- `type` — 省略可能な AS 型指定。Integer/Long/Short/Byte はエンジンの符号付き 32 ビット整数変換、Double/Single/Decimal は倍精度数値、String は文字列、Boolean/Bool は論理値、Variant/Object は値の種類を維持します。VB.NET の byte/short/long ごとの範囲は適用しません。
- `expression` — VAR/DIM の初期式は省略可能ですが、代入の右辺は必須です。その行の実行時に評価します。AS String で初期式がない場合は空文字列、型付きの数値と Boolean はゼロです。初期式なしの型指定なし VAR および VAR AS Variant/Object は Unit（値なし）ですが、スカラーの DIM は 0 を設定します。型指定なしの変数は後で異なる種類の値を保持できます。

## 戻り値

値はありません。VAR、DIM、代入文は結果を返しません。名前を読むと保存した値を取得します。例の RETURN は Main から値を返すもので、DIM の戻り値ではありません。

## 動作

- 構文の角括弧は省略可能な部分を表します。AS や初期式を囲む角括弧は入力しません。配列の DIM は別の宣言形式です。
- このエンジンでは LET と SET は通常の代入の互換形式です。Option Explicit On では名前を宣言しません。AS 型は後の代入にも適用し、無効な変換や未対応型は実行エラーになります。
- ローカル名はプロシージャ呼び出しに属します。IF 内の宣言は独立したブロックスコープを作りません。実行されない分岐は実行時の値を作りません。分岐後に使う場合はその前に宣言します。
- Injection の互換規則として、呼び出されたプロシージャは呼び出し元の現在のグローバルスカラー値と AS 型を継承します。呼び出し先でスカラーを再代入しても呼び出し元は更新しません。更新には値を返すか BYREF 引数を使用します。Array/Object 値のディープコピーではありません。新しい最上位呼び出しではグローバル値を再初期化します。ローカル宣言は自身のフレームの名前を隠しますが、グローバル宣言を置き換えません。
- エンジンは初期式を評価し、現在のスコープに保存場所を定義して型変換します。後の代入も右辺を先に評価します。例はローカル計算であり、変数はプロファイルや JSON ファイルに自動保存されません。

## 使用例

### 1. 整数の更新

```vb
# count は 0 で始まり、5 を代入し、LET で 2 を足します。Main は Integer の 7 を返します。最初の DIM は宣言で、以後の代入は値の更新です。
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    LET count = count + 2
    RETURN count
END SUB
```

**パラメーターと実行の説明:**

count は 0 で始まり、5 を代入し、LET で 2 を足します。Main は Integer の 7 を返します。最初の DIM は宣言で、以後の代入は値の更新です。

### 2. 文字列と論理フラグ

```vb
# label は空の String で始まります。SET で "ore" を保存します。enabled は Boolean の TRUE なので IF 分岐は String の "ore" を返します。引用符なしの TRUE は論理値 1 です。
Option Explicit On
SUB Main()
    DIM label AS String
    VAR enabled AS Boolean = TRUE
    SET label = "ore"
    IF enabled = TRUE THEN
        RETURN label
    END IF
    RETURN "disabled"
END SUB
```

**パラメーターと実行の説明:**

label は空の String で始まります。SET で "ore" を保存します。enabled は Boolean の TRUE なので IF 分岐は String の "ore" を返します。引用符なしの TRUE は論理値 1 です。

### 3. グローバル入力とローカル計算

```vb
# baseAmount はグローバルで値は 4 です。extra は Calculate のローカル変数で 3 です。Calculate が返した 7 を Main 自身のローカル result に保存し、7 を返します。extra は Main のローカル変数ではありません。
Option Explicit On
VAR baseAmount AS Integer = 4
FUNCTION Calculate()
    VAR extra = 3
    RETURN baseAmount + extra
END FUNCTION
SUB Main()
    VAR result = Calculate()
    RETURN result
END SUB
```

**パラメーターと実行の説明:**

baseAmount はグローバルで値は 4 です。extra は Calculate のローカル変数で 3 です。Calculate が返した 7 を Main 自身のローカル result に保存し、7 を返します。extra は Main のローカル変数ではありません。

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim
Runtime/Interpreter.cs: VisitVarDef / VisitAssignment
Runtime/SemanticScope.cs: DefineVar / SetVar / Coerce
-->
