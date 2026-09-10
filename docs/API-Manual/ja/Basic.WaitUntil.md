# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Wait Until は条件が成立するか時間切れになるまで繰り返し確認します。VB.NET の文ではなく Basic の拡張です。現在のスクリプトで動作し、新しいスレッドや別の手続きを開始しません。

## 正確な構文

```text
Wait Until condition Timeout milliseconds
```

## パラメーター

- `condition` — condition は直ちに評価され、その後短い待機の間に再評価されます。Boolean または比較式を使ってください。数値 0 は false、他の値は If と同じ規則です。文字列 "false" は Boolean false ではありません。UO や自作関数を呼べますが、エラーは伝播し、副作用は評価のたびに繰り返されます。
- `Timeout milliseconds` — Timeout は必須です。milliseconds は最初の条件評価前に一度だけ評価され、Integer 0..2147483647 が必要です。負数、小数、String は条件実行前にエラーになります。0 は即時評価だけを許可します。他の場所では timeout を通常の変数名に使えます。

## 戻り値

文自体に戻り値はありません。成功すると次の行へ進み、時間切れではファイルと行を持つ実行エラーが発生します。Try/Catch または On Error で処理でき、なければ現在の実行が失敗します。自動的に false を返しません。例 2 では True/1 または False/0 を返す関数を明示的に作ります。

## 動作

- 処理系は時間を保存し、単調な Stopwatch を開始します。最初の即時評価は制限 0 でも成功できます。false の場合、ループは取り消しと一時停止を確認し、残り時間を計算して最大 10 ミリ秒待ってから再評価します。連続したビジーループを避けますが、OS のスケジュールで間隔は長くなり得ます。
- 一時停止中は条件を評価しませんが、実際の経過時間は制限に含まれます。再開時に期限が過ぎていれば、次の評価より前に時間切れになります。停止は待機を中断し、他の緊急取り消しと同じくスクリプトの Catch/Finally を通りません。condition 内でブロックする呼び出しを強制中断できないため、条件関数は短くしてください。開始済み評価は終了後に結果またはエラーが処理されます。
- 条件のエラーは時間切れに置き換わりません。通常エラーと時間切れでは該当する Finally を実行します。変数は現在の呼び出しに属し、再び入ると新しい制限時間が始まります。End Wait や追加の評価間隔引数はありません。Wait(milliseconds) は独立した遅延関数として残ります。

## 使用例

### 1. 制限時間付きで関数を確認する

```vb
# checks は 0 で開始し、Ready は ByRef で受け取り毎回 1 加算します。required=3 は ByVal、budget=5000 は最大 5 秒です。最初の 2 回は false、3 回目は true となり、Main は Integer 3 を返します。サーバーの模擬接続ではなく決定的な確認例です。必要な実際の状態確認に置き換えてください。
Option Explicit On
Function Ready(ByRef checks As Integer, ByVal required As Integer) As Boolean
    checks += 1
    Return checks >= required
End Function

Sub Main()
    Dim checks As Integer = 0
    Const budget = 5000
    Wait Until Ready(checks, 3) Timeout budget
    Return checks
End Sub
```

**パラメーターと実行の説明:**

checks は 0 で開始し、Ready は ByRef で受け取り毎回 1 加算します。required=3 は ByVal、budget=5000 は最大 5 秒です。最初の 2 回は false、3 回目は true となり、Main は Integer 3 を返します。サーバーの模擬接続ではなく決定的な確認例です。必要な実際の状態確認に置き換えてください。

### 2. Boolean を返す関数で包む

```vb
# TryWait に ready=False と budget=0 を渡します。即時評価が失敗し時間切れとなり、Catch problem が Return False を実行します。Main の戻り値 0 は False と比較できます。ready=True なら 1/True です。すべての実行エラーを捕捉するため、区別する場合は problem を確認してください。ready は Boolean 値でありコールバックではありません。
Option Explicit On
Function TryWait(ByVal ready As Boolean, ByVal budget As Integer) As Boolean
    Try
        Wait Until ready Timeout budget
        Return True
    Catch problem
        Return False
    End Try
End Function

Sub Main()
    Dim success = TryWait(False, 0)
    Return success
End Sub
```

**パラメーターと実行の説明:**

TryWait に ready=False と budget=0 を渡します。即時評価が失敗し時間切れとなり、Catch problem が Return False を実行します。Main の戻り値 0 は False と比較できます。ready=True なら 1/True です。すべての実行エラーを捕捉するため、区別する場合は problem を確認してください。ready は Boolean 値でありコールバックではありません。

### 3. 条件エラーを保って終了処理する

```vb
# CheckStatus は state=-1 を受け取ると直ちに "disconnected" を送出します。3000 ミリ秒の制限はこのエラーを置き換えません。Catch は problem を message にコピーし、Finally は finished=True/1 にします。Main は "disconnected:1" を返します。state=1 は即時成功、state=0 は時間切れまで false です。ゲーム接続は不要です。
Option Explicit On
Function CheckStatus(ByVal state As Integer) As Boolean
    If state < 0 Then
        Throw "disconnected"
    End If
    Return state = 1
End Function

Sub Main()
    Dim message = ""
    Dim finished = False
    Try
        Wait Until CheckStatus(-1) Timeout 3000
    Catch problem
        message = problem
    Finally
        finished = True
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**パラメーターと実行の説明:**

CheckStatus は state=-1 を受け取ると直ちに "disconnected" を送出します。3000 ミリ秒の制限はこのエラーを置き換えません。Catch は problem を message にコピーし、Finally は finished=True/1 にします。Main は "disconnected:1" を返します。state=1 は即時成功、state=0 は時間切れまで false です。ゲーム接続は不要です。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
