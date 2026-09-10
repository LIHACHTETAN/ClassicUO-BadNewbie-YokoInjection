# CONST

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

CONST は通常の再代入を拒否する名前の束縛を宣言します。初期値はリテラルや式の結果を使用でき、宣言の実行時に評価します。

## 正確な構文

```text
CONST name [AS type] = expression [, name ...]
```

## パラメーター

- `name` — 引用符なしの定数名。スコープ内で区別できる名前を使います。プロシージャ外ではグローバル、内部ではその呼び出しにローカルです。
- `type` — 省略可能な対応 AS 型。VAR と同じ変換を使用します。AS Integer は例えばエンジンの符号付き 32 ビット整数に変換します。角括弧は省略可能の意味であり、AS の周りには入力しません。
- `expression` — 必須の初期式。数値、引用符付き文字列、TRUE/FALSE、算術、対応する関数の結果を使えます。宣言を実行するたびに一度評価し、ファイル全体で永久に一度だけではありません。

## 戻り値

値はありません。CONST は宣言であり関数や論理問い合わせではありません。名前を読むと保存した初期値を取得します。例の RETURN は Main または ApplyLimit のものです。

## 動作

- 通常の代入、LET、SET はこの束縛を置き換えられず、定数変更のエラーになります。TRY/CATCH でこの実行エラーを処理できます。Option Explicit は宣言を要求しますが、すべての不正代入を起動前に検出するわけではありません。
- グローバル定数は新しい最上位実行で初期化し、呼び出し先に定数フラグと AS 型を継承します。ローカル定数は宣言の実行時に初期化します。そのため初期式の関数は次の起動時に再び動作する場合があります。
- 保護するのは束縛で、Array/Object の内容を凍結しません。別のローカル宣言はグローバル名を隠せます。別の宣言は新たな束縛を作ります。定数名の使い回しは避けてください。
- エンジンは初期式を評価し、AS 変換を適用してスコープ内に定数フラグを記録します。以後の通常代入では変更前にこのフラグを確認します。スカラーリテラルの例はゲーム操作を行いません。

## 使用例

### 1. 固定待機時間を計算に使う

```vb
# delay は値が 350 のローカル Integer 定数です。2 倍して別の変数 doubled=700 を作ります。Main は 700 を返し、この例自体は待機しません。
Option Explicit On
SUB Main()
    CONST delay AS Integer = 350
    VAR doubled = delay * 2
    RETURN doubled
END SUB
```

**パラメーターと実行の説明:**

delay は値が 350 のローカル Integer 定数です。2 倍して別の変数 doubled=700 を作ります。Main は 700 を返し、この例自体は待機しません。

### 2. グローバル上限を渡す

```vb
# limit は値が 50 のグローバル Integer 定数です。ApplyLimit は amount=72 と maximum=50 を受け取り、小さい数量の 50 を返します。補助関数は全文が定義され、引数を読むだけです。
Option Explicit On
CONST limit AS Integer = 50
FUNCTION ApplyLimit(amount, maximum)
    IF amount > maximum THEN
        RETURN maximum
    END IF
    RETURN amount
END FUNCTION
SUB Main()
    RETURN ApplyLimit(72, limit)
END SUB
```

**パラメーターと実行の説明:**

limit は値が 50 のグローバル Integer 定数です。ApplyLimit は amount=72 と maximum=50 を受け取り、小さい数量の 50 を返します。補助関数は全文が定義され、引数を読むだけです。

### 3. 禁止された再代入の処理

```vb
# limit の初期値は 3 です。4 の代入はエラーになり定数を変えません。CATCH はエラーを problem に保存し、caught=TRUE にします。Main は論理値 1 を返します。ここでは TRUE と 1 は同じです。
Option Explicit On
SUB Main()
    CONST limit = 3
    VAR caught = FALSE
    TRY
        limit = 4
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**パラメーターと実行の説明:**

limit の初期値は 3 です。4 の代入はエラーになり定数を変えません。CATCH はエラーを problem に保存し、caught=TRUE にします。Main は論理値 1 を返します。ここでは TRUE と 1 は同じです。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: constDeclaration / globalConst
Runtime/DefinitionCollector.cs: VisitGlobalConst
Runtime/Interpreter.cs: VisitConstDef
Runtime/SemanticScope.cs: DefineVar / SetVar
-->
