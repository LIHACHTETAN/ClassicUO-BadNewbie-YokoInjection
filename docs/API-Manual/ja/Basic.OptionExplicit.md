# Option Explicit

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

スクリプト実行前に変数の宣言を要求します。このエンジンの Basic 言語におけるファイル指令であり、UO コマンドや関数呼び出しではありません。

## 正確な構文

```text
Option Explicit
Option Explicit On
Option Explicit Off
```

## パラメーター

- `On / Off` — On は厳密な宣言チェックを有効化し、Off は無効化します。Explicit の後を省略すると On です。指令自体がない場合は従来の非厳密モードを維持します。括弧や引用符は不要です。

## 戻り値

値はありません。指令は式ではなく、TRUE/FALSE、数値、ID を返しません。例の RETURN は Main または Enough のもので、Option Explicit の戻り値ではありません。

## 動作

- 変数、定数、プロシージャより前に一度だけ記述します。前に空行やコメントを置けます。重複または遅い位置の指令は SC013 となり、後から Off に切り替える場合も同様です。
- On では未宣言変数の読み取りや代入がソース位置付きの SC006 になります。配列名、FOR カウンター、メソッド呼び出し先のオブジェクトも検査します。VAR/DIM/CONST、引数、名前付き CATCH 変数で名前を宣言します。FOR VAR はカウンターを宣言します。
- ローカル変数は使用前に宣言します。あるプロシージャのローカル変数は別のプロシージャの名前を宣言しません。グローバル宣言はプロシージャで利用できます。名前の検査であり、全分岐での初期化を証明するものではありません。
- パーサーはファイル全体を読み、解析で宣言を解決し、厳密チェックのエラーがあると最初のコマンドより前に実行を拒否します。再読み込みでは前のスクリプトとは独立して新しいファイルの設定を適用します。Off でも警告は残る場合があり、未作成の値を読むと実行時に失敗することがあります。
- 指令自体はゲーム操作やパケット送信を行いません。VB.NET との完全互換性やゲームのターゲットの存在を保証しません。

## 使用例

### 1. 代入前の宣言

```vb
# On で検査を有効にします。DIM が count を Integer として宣言し、5 を代入できます。Main は 5 を返します。count を未宣言の coutn に変えると SC006 で起動を拒否します。
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    RETURN count
END SUB
```

**パラメーターと実行の説明:**

On で検査を有効にします。DIM が count を Integer として宣言し、5 を代入できます。Main は 5 を返します。count を未宣言の coutn に変えると SC006 で起動を拒否します。

### 2. 引数とグローバル定数

```vb
# モード省略は On です。minimum は値が 3 のグローバル定数です。amount は Enough の宣言済み引数であり、Main の同名変数とは別です。Enough は 5 >= 3 を比較し、TRUE、数値では 1 を返します。
Option Explicit
CONST minimum = 3
FUNCTION Enough(amount)
    RETURN amount >= minimum
END FUNCTION
SUB Main()
    VAR amount = 5
    RETURN Enough(amount)
END SUB
```

**パラメーターと実行の説明:**

モード省略は On です。minimum は値が 3 のグローバル定数です。amount は Enough の宣言済み引数であり、Main の同名変数とは別です。Enough は 5 >= 3 を比較し、TRUE、数値では 1 を返します。

### 3. 古いスクリプトの実行

```vb
# Off では DIM なしの代入で legacyCounter を作成できます。Main は 7 を返します。この互換性の例では警告が残る場合があります。厳密に検査するには変数を宣言して On にします。
Option Explicit Off
SUB Main()
    legacyCounter = 7
    RETURN legacyCounter
END SUB
```

**パラメーターと実行の説明:**

Off では DIM なしの代入で legacyCounter を作成できます。Main は 7 を返します。この互換性の例では警告が残る場合があります。厳密に検査するには変数を宣言して On にします。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: optionExplicit
Analysis/SanityAnalyzer.cs
Analysis/InvalidSymbolVisitor.cs
Runtime/InjectionRuntime.cs
-->
