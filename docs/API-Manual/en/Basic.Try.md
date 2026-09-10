# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Try handles execution errors from its body and called helpers. Catch handles the error, Finally completes the operation, and Throw raises or rethrows an error. An API result of 0 or false is an ordinary result: inspect it explicitly; it does not automatically enter Catch.

## Exact syntax

```text
Try
    statements
Catch
    handlerStatements
Finally
    cleanupStatements
End Try
Catch name
Catch name As Exception
Catch name As String
Throw stringExpression
Throw
```

## Parameters

- `Try / statements` — Try starts a protected block. It requires one Catch, one Finally, or both, followed by End Try. Nested blocks are allowed. A successful body skips Catch. Multiple Catch clauses, When filters and Exit Try are not implemented in this subset.
- `Catch / name / As type` — Catch may omit its variable. Otherwise name receives the error message as String. As String states this representation; As Exception is a compatibility spelling, not a .NET object or type filter. Other catch types are rejected. A new name becomes a procedure local and shadows an equally named global. An existing local is assigned normally, respecting its type/Const rules. Declare a String before Try if it must exist on paths where Catch does not run.
- `Finally / End Try` — Finally is optional if Catch exists; its body may be empty. Ordinary completion, errors, Return, Exit Sub/Function and outward loop/GoTo transfers execute the applicable Finally blocks. End Try is mandatory. Script cancellation deliberately bypasses Catch and script Finally so emergency stop cannot be delayed.
- `Throw stringExpression` — Throw stringExpression evaluates the message once and raises a new script error. The message must be String; use CStr explicitly for other values. This is a Basic form, not Throw New Exception(...) from VB.NET. Without a handler, it fails the current script run, not all other scripts.
- `Throw` — Bare Throw is valid only inside Catch, including its nested blocks. It rethrows the active error without replacing its original message, file or line. A helper called from Catch cannot use bare Throw outside its own Catch.

## Returns

Try/Catch/Finally and Throw do not return an ID, number or Boolean. Catch exposes message text through name; Throw transfers control instead of returning a value. The examples explicitly return two String results and Integer 13 from Main. API methods called inside retain their own return contracts.

## Behavior

- Preparation validates block nesting and disallows GoTo/On Error GoTo into Try, Catch or Finally. The generator records handler/finalization addresses. At runtime each call maintains its own active handlers; errors first reach the nearest eligible Catch. Errors in Catch continue through its Finally to an outer handler. With no structured handler, ordinary On Error rules may apply.
- A pending return, error or outward jump is saved while Finally executes; nested finalization runs from inside outward. A new error in Finally replaces the pending error. Basic also permits Return or outward transfers from Finally, which replace the pending continuation; this differs from VB.NET. Bare Throw retains the first failure location, including errors from called helpers.
- Pause/stop checkpoints remain active. Try does not start threads, retry work or insert delays. Prepared handler addresses are reused; exception handling is for failures, not a substitute for routine checks. Emergency termination skips script cleanup; host-owned resources still follow their separate runtime lifetimes.
- If an error leaves a Try block after cleanup and reaches an external On Error GoTo handler, Resume retries the whole Try from its header. Resume Next continues with the first statement after End Try. On Error Resume Next has the same continuation. Completed actions may repeat when retrying; it does not jump back into an unwound body.

## Examples

### 1. Validate input and keep the message

```vb
# CheckedAmount receives amount=-2 as an Integer ByVal, so the negative-value branch throws "amount must be non-negative". Catch stores that String in problem and copies it to message. As Exception does not create an object. Finally sets finished=1. Main returns "amount must be non-negative:1". A non-negative amount would return normally and skip Catch.
Option Explicit On
Function CheckedAmount(ByVal amount As Integer) As Integer
    If amount < 0 Then
        Throw "amount must be non-negative"
    End If
    Return amount
End Function

Sub Main()
    Dim message=""
    Dim finished=0
    Try
        CheckedAmount(-2)
    Catch problem As Exception
        message=problem
    Finally
        finished=1
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Parameter and execution notes:**

CheckedAmount receives amount=-2 as an Integer ByVal, so the negative-value branch throws "amount must be non-negative". Catch stores that String in problem and copies it to message. As Exception does not create an object. Finally sets finished=1. Main returns "amount must be non-negative:1". A non-negative amount would return normally and skip Catch.

### 2. Rethrow through nested handlers

```vb
# The inner Throw creates "missing item". Inner Catch sets trace=1; bare Throw keeps the same error. Inner Finally appends 2, outer Catch copies outerProblem to message and appends 3, outer Finally appends 4. Main returns "1234:missing item". trace records the execution order; it is not an error code.
Option Explicit On
Sub Main()
    Dim trace=0
    Dim message=""
    Try
        Try
            Throw "missing item"
        Catch problem
            trace=1
            Throw
        Finally
            trace=trace*10+2
        End Try
    Catch outerProblem
        message=outerProblem
        trace=trace*10+3
    Finally
        trace=trace*10+4
    End Try
    Return CStr(trace) & ":" & message
End Sub
```

**Parameter and execution notes:**

The inner Throw creates "missing item". Inner Catch sets trace=1; bare Throw keeps the same error. Inner Finally appends 2, outer Catch copies outerProblem to message and appends 3, outer Finally appends 4. Main returns "1234:missing item". trace records the execution order; it is not an error code.

### 3. Finish each entered iteration

```vb
# number visits 1, 2 and 3. Only 1 is added to total: Continue For skips 2, Exit For ends the loop at 3. All three entered Try blocks run Finally, increasing finished to 3. Main returns 1*10+3=13. No error is required for Finally to run; the loop transfer is deferred until that iteration is finalized.
Option Explicit On
Sub Main()
    Dim total=0
    Dim finished=0
    For Var number=1 To 3
        Try
            If number=2 Then
                Continue For
            End If
            If number=3 Then
                Exit For
            End If
            total+=number
        Finally
            finished+=1
        End Try
    Next
    Return total*10+finished
End Sub
```

**Parameter and execution notes:**

number visits 1, 2 and 3. Only 1 is added to total: Continue For skips 2, Exit For ends the loop at 3. All three entered Try blocks run Finally, increasing finished to 3. Main returns 1*10+3=13. No error is required for Finally to run; the loop transfer is deferred until that iteration is finalized.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: tryStatement / catchClause / finallyClause / throwStatement
Analysis/TryStructureValidator.cs: VisitTryStatement / VisitSubrutine / VisitCatchClause / VisitThrowStatement
Runtime/Instructions/Generator.cs: Generate(TryStatementContext)
Runtime/Instructions/TryInstruction.cs: TryInstruction / CatchInstruction / FinallyInstruction / EndTryInstruction
Runtime/Interpreter.cs: CallSubrutine / TryHandleStructuredError / Transfer / DeferReturn / Failure
Runtime/SemanticScope.cs: IsLocal / DefineVar / SetVar
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/try-catch-finally-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/throw-statement
-->
