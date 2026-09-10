# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

IF は最大一つの分岐を選びます。IF、続く ELSEIF を順に調べ、最初の真を選びます。すべて偽なら、存在する場合は ELSE を実行し、通常は END IF の後に進みます。

## 正確な構文

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## パラメーター

- `condition` — condition：入るときに一回調べる式。数値のゼロは偽、ゼロ以外は真です。明確な比較や API の真偽結果を推奨します。
- `elseifCondition` — elseifCondition：前の条件がすべて偽の場合にだけ調べる任意の追加条件。ELSEIF は一語で記述します。
- `statements / ELSE` — statements / ELSE：続く行の命令。ELSE は任意で条件を持たず、最後に一つだけ置けます。THEN と END IF は必須で、複数行ブロックを使います。

## 戻り値

値を返しません（Unit）。IF は制御命令であり関数ではありません。条件や選ばれた RETURN は値を生成できます。真偽値 1/0 は TRUE/FALSE と比較できます。IF count はゼロ以外の件数を受け入れますが、IF count=TRUE は 1 のみです。

## 動作

- コンパイラは条件分岐と終了へのジャンプを作ります。偽なら次の条件か ELSE に進み、選んだ分岐は残りを飛ばします。入れ子の IF は独自の ELSE を持ちます。RETURN も周囲の FINALLY を実行してから手続きを離れます。
- 互換性のため、IF はすべてを CBool 変換せず数値ゼロと比較します。文字列 "0"、空文字列、配列、オブジェクト、Unit は真側を選びます。文字列は明示的に変換するか対象のプロパティを比較してください。AndAlso/OrElse は数値を要求します。
- 省略した分岐の宣言は実行時の変数を作りません。共有する結果は IF の前で宣言・初期化します。Option Explicit は名前を検査し、全経路の代入は保証しません。複数 ELSE は Option Explicit がなくても SC015 として実行前に拒否します。

## 使用例

### 1. 四つの分類

```vb
# Classify(value) は <0、=0、<10、最後に ELSE を調べます。-2、0、7、20 は negative、zero、small、large です。Main は "negative:zero:small:large" を返し、各呼び出しで一つの RETURN だけを実行します。
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**パラメーターと実行の説明:**

Classify(value) は <0、=0、<10、最後に ELSE を調べます。-2、0、7、20 は negative、zero、small、large です。Main は "negative:zero:small:large" を返し、各呼び出しで一つの RETURN だけを実行します。

### 2. 入れ子の判断

```vb
# Action(enabled, amount) は enabled、次に amount>0 を調べて work か idle を選びます。外側の ELSE は disabled です。(TRUE,5)、(TRUE,0)、(FALSE,5) から "work:idle:disabled" を返します。END IF は対応するブロックを閉じます。
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**パラメーターと実行の説明:**

Action(enabled, amount) は enabled、次に amount>0 を調べて work か idle を選びます。外側の ELSE は disabled です。(TRUE,5)、(TRUE,0)、(FALSE,5) から "work:idle:disabled" を返します。END IF は対応するブロックを閉じます。

### 3. 条件評価の順序

```vb
# Check(calls,value) は ByRef の calls を増やして value を返します。最初は偽、二番目は真で、三番目と ELSE は省略されます。result=7、calls=2 となり、Main は calls*10+result=27 を返します。補助関数はすべて記載しています。
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**パラメーターと実行の説明:**

Check(calls,value) は ByRef の calls を増やして value を返します。最初は偽、二番目は真で、三番目と ELSE は省略されます。result=7、calls=2 となり、Main は calls*10+result=27 を返します。補助関数はすべて記載しています。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
