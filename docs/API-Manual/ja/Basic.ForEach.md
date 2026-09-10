# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

For Each は数値インデックスを使わず、配列または列挙可能なネイティブコレクションの要素を順に読みます。手続きや関数内のループ文であり、API 関数の呼び出しではありません。

## 正確な構文

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## パラメーター

- `item` — item：反復変数。既存のローカル変数、引数、アクセス可能なフィールドを再利用します。なければ Option Explicit On でも手続きのローカル変数を作ります。定数には代入できません。
- `type` — type：省略可能な AS type。例えば Integer です。ローカル反復変数を宣言し、各要素を代入時に変換します。AS を省略すると既存変数の型を保持します。
- `collection` — collection：開始時に一度だけ評価する式。配列または列挙対応のネイティブオブジェクトを受け付け、スカラーは拒否します。入れ子の配列は行を返すため、セルには内側のループを使います。
- `statements / NEXT item` — statements / NEXT item：本体と終端。NEXT の後の名前は省略可能ですが、指定するなら反復変数と一致させます。NEXT は独立した行に書きます。

## 戻り値

For Each と Next に戻り値はありません。item は要素値を受け取り、自動的にインデックス、ID、スタック個数になるわけではありません。本体内の RETURN は関数全体を終了します。例は Integer 12、105、10 を返します。

## 動作

- 準備時に初期化式より先に FOR EACH と NEXT を対応付け、誤った対応は SC020 になります。collection を一度評価して参照と独立したカーソルを保持します。item の代入でカーソルは動きません。
- 配列はインデックス昇順です。空配列は本体を飛ばし、AS のない既存変数の値を保持します。未初期化要素と AS 変換失敗は捕捉可能なエラーです。
- item への代入は配列要素を置き換えません。入れ子の配列やオブジェクトは参照であり、row のセルを変えるとその行が変わります。collection の再代入は現在の列挙を変えません。同じ配列の後続要素の変更は読み取り時に反映されます。
- Continue For は最も近い For または For Each の次の反復へ進み、Exit For はそれを終了します。エラー、RETURN、キャンセル時はネイティブ列挙子を解放します。列挙中の変更を禁止するコレクションもあり、自動コピーはありません。
- 反復変数はループ後も手続き内で利用でき、最後の代入値を保持します。各実行は独立したカーソルを持ちます。IDE の補完、テンプレート、宣言移動と通常の一時停止・停止が利用できます。

## 使用例

### 1. インデックスなしの合計

```vb
# values[2] は 2、4、6 の三要素です。SumItems が配列を受け、item が各値を受け取ります。total は 0 から 12 になり、RETURN が Integer 12 を Main に返します。NEXT item はこの反復を閉じます。
Option Explicit On
Function SumItems(values)
    Var total = 0
    For Each item In values
        total += item
    Next item
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return SumItems(values)
End Sub
```

**パラメーターと実行の説明:**

values[2] は 2、4、6 の三要素です。SumItems が配列を受け、item が各値を受け取ります。total は 0 から 12 になり、RETURN が Integer 12 を Main に返します。NEXT item はこの反復を閉じます。

### 2. 一度の評価と型変換

```vb
# SelectItems は calls を ByRef で受け取り 1 に増やし、["2", "3"] を返します。AS Integer で 2、3 へ変換し total=5 になります。item=100 は元の配列や順序を変えません。Main は calls*100+total、Integer 105 を返します。
Option Explicit On
Function SelectItems(ByRef calls)
    calls += 1
    Dim values[1]
    values[0] = "2"
    values[1] = "3"
    Return values
End Function
Sub Main()
    Var calls = 0
    Var total = 0
    For Each item As Integer In SelectItems(calls)
        total += item
        item = 100
    Next
    Return calls * 100 + total
End Sub
```

**パラメーターと実行の説明:**

SelectItems は calls を ByRef で受け取り 1 に増やし、["2", "3"] を返します。AS Integer で 2、3 へ変換し total=5 になります。item=100 は元の配列や順序を変えません。Main は calls*100+total、Integer 105 を返します。

### 3. 入れ子の配列

```vb
# rows[1][1] は二行二セルです。row は行への参照、cell は順に 1、2、3、4 を受けます。各 NEXT は対応するループを閉じます。SumGrid と Main は Integer 10 を返し、ID や個数を自動計算しません。
Option Explicit On
Function SumGrid(rows)
    Var total = 0
    For Each row In rows
        For Each cell In row
            total += cell
        Next cell
    Next row
    Return total
End Function
Sub Main()
    Dim rows[1][1]
    rows[0][0] = 1
    rows[0][1] = 2
    rows[1][0] = 3
    rows[1][1] = 4
    Return SumGrid(rows)
End Sub
```

**パラメーターと実行の説明:**

rows[1][1] は二行二セルです。row は行への参照、cell は順に 1、2、3、4 を受けます。各 NEXT は対応するループを閉じます。SumGrid と Main は Integer 10 を返し、ID や個数を自動計算しません。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
