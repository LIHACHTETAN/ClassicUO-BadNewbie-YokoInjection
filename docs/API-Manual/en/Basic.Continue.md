# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Continue skips the remaining body of the nearest enclosing loop of the requested kind. Use Continue For for both numeric For and For Each, Continue Do for Do/Loop or Repeat/Until, and Continue While for While/Wend.

## Exact syntax

```text
Continue For
Continue Do
Continue While
```

## Parameters

- `kind` — kind: required For, Do or While after Continue. There are no parentheses or return arguments. The requested loop must enclose this statement in the same procedure. A nested loop of another kind does not intercept the transfer.

## Returns

Continue returns no value and cannot be used in an expression. It neither reports TRUE/FALSE nor restarts the procedure. The enclosing function may later RETURN a result; these examples return Integer 10, 3 and 34.

## Behavior

- For: numeric loops execute NEXT, apply STEP and check the next value against the bound; collection loops fetch the next element. An exhausted loop exits. Continue does not repeat the original counter initialization or reevaluate the collection expression.
- Do: a condition on Do is checked again at the start; a condition on Loop is checked at the end. Repeat/Until uses its UNTIL condition. An unconditional Do/Loop continues until an explicit exit or stop. While: its WHILE condition is checked again. Continue Do never selects While/Wend.
- Preparation resolves the nearest requested loop to an instruction address. Continue outside such a loop is SC020 before global initializers, even without Option Explicit. NEXT names and missing terminators are checked too. Legacy FOR/NEXT crossing an IF boundary remains supported.
- Leaving TRY/CATCH through Continue executes crossed FINALLY blocks from inner to outer, once each. A loop contained entirely inside a TRY does not execute that TRY’s FINALLY on every iteration. A RETURN or error in FINALLY replaces the pending transfer.
- Continue is not a delay. Update the condition or use an appropriate wait when polling, otherwise a loop may run indefinitely. Pause/stop checkpoints still run. Exited native enumerators are released, and independent runs keep separate cursors. Exit For/Do/While leaves the selected loop instead of advancing it.

## Examples

### 1. Skip unwanted elements

```vb
# values contains -2, 4, 0, 6. item<=0 causes Continue For for -2 and 0, so total+=item is skipped only for those elements. The same form works in For Each. SumPositive and Main return Integer 10 from 4+6.
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

**Parameter and execution notes:**

values contains -2, 4, 0, 6. item<=0 causes Continue For for -2 and 0, so total+=item is skipped only for those elements. The same form works in For Each. SumPositive and Main return Integer 10 from 4+6.

### 2. Select the outer loop by kind

```vb
# AdvanceTo receives limit=3. count starts at 0. Inside While True, count increases and Continue Do targets the enclosing Do, not that While. The Do condition is checked after each transfer; count=3 ends the loop and returns Integer 3.
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

**Parameter and execution notes:**

AdvanceTo receives limit=3. count starts at 0. Inside While True, count increases and Continue Do targets the enclosing Do, not that While. The Do condition is checked after each transfer; count=3 ends the loop and returns Integer 3.

### 3. Cleanup for a skipped iteration

```vb
# Process receives limit=3 and skip=2. i visits 1, 2, 3. The middle iteration skips total+=i, but Finally increases cleanup on all three iterations. total=4, cleanup=3; RETURN cleanup*10+total produces Integer 34.
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

**Parameter and execution notes:**

Process receives limit=3 and skip=2. i visits 1, 2, 3. The middle iteration skips total+=i, but Finally increases cleanup on all three iterations. total=4, cleanup=3; RETURN cleanup*10+total produces Integer 34.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
