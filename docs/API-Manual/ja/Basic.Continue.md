# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Continue は指定した種類の最も近い外側ループの残りを飛ばします。Continue For は数値 For と For Each、Continue Do は Do/Loop と Repeat/Until、Continue While は While/Wend に使います。

## 正確な構文

```text
Continue For
Continue Do
Continue While
```

## パラメーター

- `kind` — kind：Continue の後に For、Do、While のいずれかを必ず指定し、括弧は付けません。同じ手続き内でそのループが文を囲む必要があります。異なる種類の内側ループは対象になりません。

## 戻り値

Continue に戻り値はなく、式には使えません。TRUE/FALSE を示したり手続きを再起動したりしません。関数は後で RETURN により値を返せます。例は Integer 10、3、34 を返します。

## 動作

- For は NEXT で STEP を適用し、次の値を境界と比較します。For Each は次の要素を取得し、尽きると終了します。カウンター初期化やコレクション式の評価は繰り返しません。
- Do の先頭条件は先頭で、Loop の末尾条件は末尾で再評価します。Repeat/Until は UNTIL を使います。無条件 Do/Loop は明示的終了または停止まで続きます。While は WHILE を再評価し、Continue Do は While/Wend を選びません。
- 準備時に対応する最寄りループの命令アドレスを解決します。存在しなければ Option Explicit がなくても初期化前に SC020 になります。NEXT 名と終端も検証します。IF をまたぐ旧 FOR/NEXT の互換性は維持します。
- TRY/CATCH からの移動では越える FINALLY を内側から外側へ一度ずつ実行します。ループ全体が TRY 内なら、その FINALLY は毎回実行しません。FINALLY の RETURN やエラーは保留中の移動を置き換えます。
- Continue 自体は待機しません。ポーリング時は条件を更新するか適切に待機し、無限ループを避けてください。一時停止・停止確認は有効です。離れたネイティブ列挙子は解放され、各実行は独立します。Exit For/Do/While は次へ進まずループを終了します。

## 使用例

### 1. 不要な要素を飛ばす

```vb
# values は -2、4、0、6 です。item<=0 で -2 と 0 に Continue For を実行し、total+=item を飛ばします。For Each でも同じ記述です。SumPositive と Main は 4+6、Integer 10 を返します。
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**パラメーターと実行の説明:**

values は -2、4、0、6 です。item<=0 で -2 と 0 に Continue For を実行し、total+=item を飛ばします。For Each でも同じ記述です。SumPositive と Main は 4+6、Integer 10 を返します。

### 2. 種類で外側を選ぶ

```vb
# AdvanceTo は limit=3 を受け、count は 0 から始まります。While True 内で count を増やし、Continue Do で外側 Do へ移動します。条件を再評価し、count=3 で終了して Integer 3 を返します。
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**パラメーターと実行の説明:**

AdvanceTo は limit=3 を受け、count は 0 から始まります。While True 内で count を増やし、Continue Do で外側 Do へ移動します。条件を再評価し、count=3 で終了して Integer 3 を返します。

### 3. 飛ばしても後処理を実行

```vb
# Process は limit=3、skip=2 を受けます。i は 1、2、3 です。二回目は total+=i を飛ばしますが Finally は三回とも cleanup を増やします。total=4、cleanup=3 なので RETURN cleanup*10+total は Integer 34 です。
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**パラメーターと実行の説明:**

Process は limit=3、skip=2 を受けます。i は 1、2、3 です。二回目は total+=i を飛ばしますが Finally は三回とも cleanup を増やします。total=4、cleanup=3 なので RETURN cleanup*10+total は Integer 34 です。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
