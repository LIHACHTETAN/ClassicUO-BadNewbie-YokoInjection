# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Do は本体の前または後で条件を検査します。While は真の間、Until は真になるまで繰り返します。Repeat … Until は後で検査する対応済みの旧形式です。

## 正確な構文

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## パラメーター

- `condition / While / Until` — 数値 Boolean 式 0/False または 1/True。While は真なら継続、Until は真なら終了します。検査ごとに再評価し、文字列は Boolean として解析しません。
- `position / Repeat` — Do 後の条件は最初の反復を飛ばせます。Loop 後や Repeat の Until は少なくとも一度実行した後に検査します。条件位置は一つだけ指定できます。無条件の Do … Loop には明示的な終了が必要です。
- `statements / exit` — 本体。Continue Do は次の条件検査へ、Exit Do は最も近い Do または Repeat の外へ進みます。Break は種類を問わず最も近いループを終了。RETURN は手続き・関数全体を終了します。

## 戻り値

Do、Loop、Repeat、Until、Exit Do に戻り値はありません。例では Main から Integer 1、33、83 を明示的に返します。カウンターを組み合わせた数値であり、コマンドの Boolean 結果ではありません。

## 動作

- 準備時にブロックを対応付け、遷移を検査します。同じ Do の先頭と末尾両方に条件があると SC020 です。選んだ位置で評価し、While/Until の規則で繰り返します。
- 後置条件の Continue Do はその後置条件を必ず検査します。前置条件ならヘッダーに戻ります。離れる Try の Finally は遷移前にちょうど一度実行されます。
- Repeat はまず実行するので、空配列は入る前に処理します。暗黙の時間制限はありません。ゲーム待機には Wait と期限を使います。一時停止・停止の検査は有効です。

## 使用例

### 1. 前と後の検査

```vb
# ready=True はすでに Until を満たします。最初の Do Until ready はゼロ回で before=0。二つ目は after を増やした後で検査するため after=1。Main は before*10+after=1 を返します。
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**パラメーターと実行の説明:**

ready=True はすでに Until を満たします。最初の Do Until ready はゼロ回で before=0。二つ目は after を増やした後で検査するため after=1。Main は before*10+after=1 を返します。

### 2. 回数制限と後始末

```vb
# attempts は 0 から各回増加します。最初の二回の Continue Do は Finally と attempts<4 の検査を実行します。三回目の Exit Do も Finally を実行します。attempts=3、cleanup=3 で 33。これはローカルの模擬試行で、実際のネットワーク再試行ではありません。
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**パラメーターと実行の説明:**

attempts は 0 から各回増加します。最初の二回の Continue Do は Finally と attempts<4 の検査を実行します。三回目の Exit Do も Finally を実行します。attempts=3、cleanup=3 で 33。これはローカルの模擬試行で、実際のネットワーク再試行ではありません。

### 3. 旧形式で終了値を読む

```vb
# values=[3,5,0] は空ではありません。Repeat はセルを読み、index を増やし total に加算します。Until はゼロまたは長さの境界で終了し、ゼロ発見時は OrElse が二つ目の検査を省略します。total=8、index=3 で 83 を返します。
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**パラメーターと実行の説明:**

values=[3,5,0] は空ではありません。Repeat はセルを読み、index を増やし total に加算します。Until はゼロまたは長さの境界で終了し、ゼロ発見時は OrElse が二つ目の検査を省略します。total=8、index=3 で 83 を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
