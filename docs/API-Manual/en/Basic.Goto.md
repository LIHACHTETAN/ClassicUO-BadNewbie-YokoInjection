# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

GoTo transfers execution to a named label in the current procedure or function. A label marks a location; it does not create a callable procedure. Prefer If, loops and Return for ordinary structured control flow.

## Exact syntax

```text
GoTo label
label:
```

## Parameters

- `label` — An identifier declared as label: on its own line in the same procedure. Write GoTo label without quotes, parentheses or a trailing colon. Forward and backward targets work; matching ignores case. The same name may be reused in another procedure. Symbol names may contain dots, but a dot does not make a label a module member. Numbers, computed expressions and labels in another procedure are not supported targets.

## Returns

GoTo and label: return no value. They do not report success as 1/0 or TRUE/FALSE. The examples explicitly Return Integer -1, 6 and 123 from Main; those values come from their own calculations.

## Behavior

- Preparation records label addresses and resolves branch instructions once the whole procedure has been read. Execution uses the resolved address without searching the source again. Variable values are preserved across the branch; earlier actions are not rolled back.
- An unknown target produces SC009 and the client blocks execution. Duplicate names within one procedure, including names differing only in case, produce SC021 before initialization. Included files retain their original diagnostic file and line. Stray characters after a target can produce a warning; use the exact clean syntax.
- A branch leaving active Try blocks runs their Finally blocks from the innermost outward before reaching the target. A branch within the same active Try keeps that scope active. An error raised during Finally can prevent reaching the target.
- Enter loops and Try/Catch/Finally through their normal opening statements. Jumping into the middle does not recreate skipped initialization or active runtime scopes; it is not a supported way to resume them. Use Continue or Exit for ordinary loop control.
- A backward branch has no automatic attempt limit, timeout or delay. Change the exit condition deliberately. A label also allows normal execution to fall through: branch or Return to skip a section that must not run. GoTo does not install an error handler; see On Error for that.

## Examples

### 1. Choose a forward branch

```vb
# amount=0 selects NoItems, which assigns result=-1. Execution then falls through Finished and Main returns -1. With amount=4 the ordinary path assigns 40, and GoTo Finished skips NoItems. Both labels belong to Main; neither is a function call.
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**Parameter and execution notes:**

amount=0 selects NoItems, which assigns result=-1. Execution then falls through Finished and Main returns -1. With amount=4 the ordinary path assigns 40, and GoTo Finished skips NoItems. Both labels belong to Main; neither is a function call.

### 2. Repeat a bounded calculation

```vb
# attempt starts at 0 and increases before the condition. Again and again refer to the same label. The three passes add 1, 2 and 3; attempt<3 then becomes false and Return gives 6. total is initialized before the label so it is not reset on each pass.
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**Parameter and execution notes:**

attempt starts at 0 and increases before the condition. Again and again refer to the same label. The three passes add 1, 2 and 3; attempt<3 then becomes false and Return gives 6. total is initialized before the label so it is not reset on each pass.

### 3. Leave nested Try blocks

```vb
# trace becomes 1, then GoTo Finished skips trace=99. The inner Finally appends digit 2 and the outer Finally appends 3. Only then does execution reach Finished and Return 123. Each cleanup block runs once for this branch.
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**Parameter and execution notes:**

trace becomes 1, then GoTo Finished skips trace=99. The inner Finally appends digit 2 and the outer Finally appends 3. Only then does execution reach Finished and Return 123. Each cleanup block runs once for this branch.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
