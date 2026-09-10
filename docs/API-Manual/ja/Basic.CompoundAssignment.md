# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

既存の変数や配列要素を +=、-=、*=、/= で更新します。現在値を読み、計算して書き戻し、対象を二度評価しません。

## 正確な構文

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## パラメーター

- `target` — target：既存のスカラー名、items[index]、grid[x][y] など。要素は初期化済みで、ゼロ始まりの添字が有効である必要があります。変数の宣言はしません。
- `operator` — += と &= は数値を加算するか二つの String を結合します。-= は減算、*= は乗算、/= は除算です。プリプロセッサーが &= を += に変えるため、5 &= 3 は 8 を保存します。String と数値には明示的な CStr が必要です。各演算子は一つのトークンとして書きます。
- `value` — value：対象と添字の後に一度だけ評価する式。種類が演算に適合する必要があります。String に数値を追加する前に CStr で変換します。

## 戻り値

値なし（Unit）。文であり、式や成功フラグではありません。次の行で target を読み保存結果を取得します。スカラー書き戻しには AS が適用され、Integer 5 に /=2 を行うと Integer 2、型未指定の数値変数は Decimal 2.5 です。

## 動作

- 各配列参照は添字を評価する前に保持されます。添字は左から一度ずつ評価し、右オペランドより先に範囲を確認します。添字や右辺の ByRef 関数が配列変数や親要素を置き換えても、選択済み要素が書き込み先です。
- +、-、*、/ と同じ規則です。整数は符号付き32ビットでオーバーフローし、/ は Decimal、浮動小数点のゼロ除算は Infinity/NaN になり得ます。String と数値の加算は失敗します。配列要素にスカラー AS 変換はありません。
- 未宣言対象、未初期化要素、範囲外添字、不適合演算、CONST 書き込み、型変換失敗は捕捉可能なエラーです。最後の書き込みはされませんが、オペランド関数の実行済み副作用は戻りません。CONST と AS は右辺実行後のスカラー書き戻し時に確認します。
- Option Explicit は実行前に名前を確認します。デバッガーは元の行番号を使い、ループは一時停止と停止の確認を続けます。読み取り、計算、書き込みは並列手続き間の不可分な同期処理ではありません。

## 使用例

### 1. 4種類の演算

```vb
# amount は10から開始し、+=2 で12、-=3 で9、*=4 で36、/=2 で Decimal 18 です。Main が保存値を返し、代入文自体は値を返しません。
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**パラメーターと実行の説明:**

amount は10から開始し、+=2 で12、-=3 で9、*=4 で36、/=2 で Decimal 18 です。Main が保存値を返し、代入文自体は値を返しません。

### 2. 添字は一度だけ

```vb
# NextIndex は ByRef 引数 calls を増やし0を返します。items[0] は5から +=2 で7になります。呼び出しは一度なので calls=1。Main は items[0]*10+calls=71 を返します。補助関数も全文掲載しています。
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**パラメーターと実行の説明:**

NextIndex は ByRef 引数 calls を増やし0を返します。items[0] は5から +=2 で7になります。呼び出しは一度なので calls=1。Main は items[0]*10+calls=71 を返します。補助関数も全文掲載しています。

### 3. 定数保護の処理

```vb
# limit は CONST 5。limit+=1 は書き込み時に失敗し、CATCH が problem に保存して caught=TRUE にします。limit は5のままです。Main は明示的な CStr で "5:1" を返します。フラグはエラー処理の結果で、代入の戻り値ではありません。 文字列は変数で作ります。report=CStr(limit) の後、report &= ":" と report &= CStr(caught) を実行します。各 &= が report を更新し、Return report が "5:1" を返します。
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**パラメーターと実行の説明:**

limit は CONST 5。limit+=1 は書き込み時に失敗し、CATCH が problem に保存して caught=TRUE にします。limit は5のままです。Main は明示的な CStr で "5:1" を返します。フラグはエラー処理の結果で、代入の戻り値ではありません。 文字列は変数で作ります。report=CStr(limit) の後、report &= ":" と report &= CStr(caught) を実行します。各 &= が report を更新し、Return report が "5:1" を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
