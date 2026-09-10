# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Do supports a condition before or after its body. While repeats while true; Until repeats until true. Repeat … Until is the supported legacy form with a condition after the body.

## Exact syntax

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

## Parameters

- `condition / While / Until` — Boolean expression: use numeric 0/False or 1/True. While continues when true; Until exits when true. Expressions are evaluated again at each check. Text is not parsed as Boolean.
- `position / Repeat` — A condition after Do can skip the first pass. A condition after Loop or Until in Repeat always follows at least one pass. Specify only one condition position. Do … Loop without a condition needs an explicit exit.
- `statements / exit` — Loop body. Continue Do reaches the next condition check; Exit Do leaves the nearest Do or Repeat. Break leaves the nearest loop of any kind. RETURN exits the entire procedure/function.

## Returns

Do, Loop, Repeat, Until and Exit Do return no value. The examples explicitly return Integer 1, 33 and 83 from Main; these encode counters, not Boolean command results.

## Behavior

- Preparation matches each block and validates loop transfers. Conditions at both ends of one Do report SC020. Runtime evaluates the selected condition at its selected position and jumps back only while the continuation rule is satisfied.
- Continue Do in a postcondition loop still checks that postcondition; in a precondition loop it returns to the header. Transfers out of Try execute Finally once before continuing or exiting.
- Repeat always executes first: guard empty arrays before entering it. Conditionless loops have no implicit timeout. For game polling use a deliberate Wait and a deadline; pause and stop checks remain active.

## Examples

### 1. Before versus after

```vb
# ready=True already satisfies Until. The first Do Until ready performs zero iterations: before=0. The second loop checks only after incrementing after, so after=1. Main returns before*10+after=1.
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

**Parameter and execution notes:**

ready=True already satisfies Until. The first Do Until ready performs zero iterations: before=0. The second loop checks only after incrementing after, so after=1. Main returns before*10+after=1.

### 2. Bounded attempts with cleanup

```vb
# attempts starts at 0; each pass increments it. The first two Continue Do transfers run Finally then test attempts<4. On attempt 3, Exit Do also runs Finally. cleanup=3 and attempts=3, so Main returns 33. These are local simulated attempts, not actual network retries.
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

**Parameter and execution notes:**

attempts starts at 0; each pass increments it. The first two Continue Do transfers run Finally then test attempts<4. On attempt 3, Exit Do also runs Finally. cleanup=3 and attempts=3, so Main returns 33. These are local simulated attempts, not actual network retries.

### 3. Legacy sentinel loop

```vb
# values contains 3, 5, 0 and is known to be nonempty. Repeat reads the current cell, advances index, and accumulates total. Until stops at value=0 or the array boundary; OrElse skips the second test if zero was found. total=8 and index=3 produce 83.
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

**Parameter and execution notes:**

values contains 3, 5, 0 and is known to be nonempty. Repeat reads the current cell, advances index, and accumulates total. Until stops at value=0 or the array boundary; OrElse skips the second test if zero was found. total=8 and index=3 produce 83.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
