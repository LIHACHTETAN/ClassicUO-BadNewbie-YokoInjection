# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Wait Until repeatedly tests a condition until it succeeds or the time limit expires. This is a Basic extension, not a VB.NET statement. It runs in the current script and does not create a thread or start another procedure.

## Exact syntax

```text
Wait Until condition Timeout milliseconds
```

## Parameters

- `condition` — condition is an expression evaluated immediately, then again between short waits. Use a Boolean or comparison: numeric 0 means false, other values follow the same truth rules as If. A String such as "false" is not Boolean false. The expression may call UO methods or your helpers; their errors propagate normally. Any side effects repeat on every test.
- `Timeout milliseconds` — Timeout is mandatory. milliseconds is evaluated once, before the first condition test. It must be Integer 0..2147483647; negative numbers, fractional values and Strings raise an error before the condition runs. Zero permits only the immediate test. Timeout remains usable as an ordinary variable name outside this contextual marker.

## Returns

The statement returns no value. Success continues at the next statement. Expiry raises a source-located execution error, handled by Try/Catch or the configured On Error rule; otherwise the current run fails. It does not return false automatically. Example 2 explicitly builds a Boolean wrapper returning True/1 or False/0.

## Behavior

- The interpreter captures the duration and starts a monotonic Stopwatch. It tests condition once immediately; an immediately true result completes even with a zero limit. A false result enters the waiting loop. Each loop checks cancellation and the host pause gate, computes the remaining time and sleeps for at most 10 ms before another check. This avoids a busy loop; OS scheduling can make intervals longer.
- Pause stops condition polling, but elapsed wall time still counts toward the limit. After resuming, an expired deadline raises the timeout before another test. Stop interrupts the wait and bypasses script Catch/Finally, as with other emergency cancellation. This statement cannot forcibly interrupt a condition/native call that itself blocks; keep condition helpers short. An already started condition finishes before its result or error is observed.
- A condition error is not changed into a timeout. Normal timeout/error handling still runs applicable Finally blocks. Script variables remain in the current call, and repeated entry starts a new duration. This statement has no End Wait or extra polling parameter. Wait(milliseconds) remains a separate, ordinary delay function.

## Examples

### 1. Poll a helper with a bounded budget

```vb
# checks starts at 0; Ready receives it ByRef and increments it on every test. required=3 is passed ByVal. budget=5000 permits up to five seconds. Tests 1 and 2 return false, test 3 returns true; Main returns Integer 3. This deterministic helper demonstrates polling, not a simulated server connection. Replace its condition with the real status you need to inspect.
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

**Parameter and execution notes:**

checks starts at 0; Ready receives it ByRef and increments it on every test. required=3 is passed ByVal. budget=5000 permits up to five seconds. Tests 1 and 2 return false, test 3 returns true; Main returns Integer 3. This deterministic helper demonstrates polling, not a simulated server connection. Replace its condition with the real status you need to inspect.

### 2. Return a Boolean from your own wrapper

```vb
# TryWait receives ready=False and budget=0. The one immediate condition test fails and raises a timeout. Catch problem converts that execution error into Return False; Main returns 0, also comparable with False. With ready=True it would return 1/True. This wrapper catches all execution errors, not only timeout; inspect problem if you need different handling. ready is a captured Boolean value here, not a function callback.
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

**Parameter and execution notes:**

TryWait receives ready=False and budget=0. The one immediate condition test fails and raises a timeout. Catch problem converts that execution error into Return False; Main returns 0, also comparable with False. With ready=True it would return 1/True. This wrapper catches all execution errors, not only timeout; inspect problem if you need different handling. ready is a captured Boolean value here, not a function callback.

### 3. Preserve a condition failure and finalize

```vb
# CheckStatus receives state=-1 and throws "disconnected" on the first test. The 3000 ms limit does not replace that error. Catch copies problem into message; Finally sets finished=True/1. Main returns "disconnected:1". state=1 would satisfy the condition immediately, while state=0 would remain false until the deadline. The example demonstrates your own status validation without requiring a game connection.
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

**Parameter and execution notes:**

CheckStatus receives state=-1 and throws "disconnected" on the first test. The 3000 ms limit does not replace that error. Catch copies problem into message; Finally sets finished=True/1. Main returns "disconnected:1". state=1 would satisfy the condition immediately, while state=0 would remain false until the deadline. The example demonstrates your own status validation without requiring a game connection.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
