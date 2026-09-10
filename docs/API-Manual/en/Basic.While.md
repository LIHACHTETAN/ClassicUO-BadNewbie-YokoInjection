# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

While tests its condition before each iteration and repeats while it is true. This engine closes the block with Wend; the VB.NET spelling End While is not supported.

## Exact syntax

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## Parameters

- `condition` — Expression evaluated before every pass, including the first and final check. Use a comparison or numeric Boolean: 0/False stops, 1/True continues; other nonzero numbers also continue. Text is not parsed as a Boolean.
- `statements` — Statements that perform work and update the condition. If the first check is false, the body is skipped entirely.
- `Wend / exit` — Wend returns to the condition. Continue While checks it again; Exit While leaves the nearest While, even across an inner loop of another kind. Break leaves the nearest loop of any kind.

## Returns

While, Wend, Exit While and Break have no return value. RETURN in the body returns from the entire procedure/function. Examples return Integer 6, 1 and 406. The search result 1 is an array index, not a Boolean success flag.

## Behavior

- Execution checks the condition, runs the body and jumps back to the check. Unlike For, it does not capture a bound or update a counter automatically.
- Keep progress explicit. For repeated game-state polling include an appropriate Wait and a deadline; While itself neither sleeps nor times out. Runtime pause and stop remain available.
- Continue/exit transfers run enclosing Finally blocks that they leave. Use separate lines for header, statements and Wend, and place the loop inside a procedure or function.

## Examples

### 1. Sum digits

```vb
# DigitSum receives number=123 ByVal. MOD 10 reads the last digit and Fix(number/10) removes it: 123→12→1→0. total adds 3+2+1=6. The final false check exits and Main receives 6; input 0 would skip the body and return 0.
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**Parameter and execution notes:**

DigitSum receives number=123 ByVal. MOD 10 reads the last digit and Fix(number/10) removes it: 123→12→1→0. total adds 3+2+1=6. The final false check exits and Main receives 6; input 0 would skip the body and return 0.

### 2. Find the first match

```vb
# FirstAbove receives values=[4,7,9] and threshold=6. The bound check protects values[index]. At index 1, 7>6 stores found=1 and Exit While skips further cells. No match leaves found=-1; Main returns the zero-based index 1.
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**Parameter and execution notes:**

FirstAbove receives values=[4,7,9] and threshold=6. The bound check protects values[index]. At index 1, 7>6 stores found=1 and Exit While skips further cells. No match leaves found=-1; Main returns the zero-based index 1.

### 3. Count condition evaluations

```vb
# CanContinue receives checks ByRef, index and limit=3 ByVal. It increments checks then returns index<limit as 1/0. Checks occur at index 0, 1, 2 and 3: four calls for three iterations. total=1+2+3=6; Main returns 400+6=406.
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**Parameter and execution notes:**

CanContinue receives checks ByRef, index and limit=3 ByVal. It increments checks then returns index<limit as 1/0. Checks occur at index 0, 1, 2 and 3: four calls for three iterations. total=1+2+3=6; Main returns 400+6=406.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
