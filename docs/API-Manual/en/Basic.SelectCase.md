# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Select Case chooses one branch by comparing a captured value with ordered alternatives. Use it for item categories, script modes or numeric ranges. It is a Basic statement, written without UO.; game calls inside expressions still require UO.

## Exact syntax

```text
Select Case expression
    Case value1, value2
        statements
        Exit Select
    Case from To to
        statements
    Case Is >= value
        statements
    Case Else
        statements
End Select
```

## Parameters

- `expression` — Required expression after Select Case. A variable, literal or function call is evaluated exactly once whenever execution enters the block, even if the block is empty or contains only Case Else.
- `value / from / to` — Case accepts a value or comma-separated alternatives; each alternative may be an expression. from To to includes both endpoints. A reversed range does not match. The upper endpoint is evaluated only if the lower comparison succeeds. Commas inside function arguments do not separate alternatives.
- `Is comparison value` — Compare using =, <>, <, <=, > or >=. Is is optional: Case Is >= 5 and Case >= 5 mean the same thing. These comparisons use the engine’s ordinary value rules, not object type tests.
- `Case Else` — Optional fallback, used only if no earlier Case matches. It must be the last branch and may occur at most once. Without it, a failed selection continues after End Select.
- `Exit Select` — Leaves the nearest enclosing Select Case and continues after its End Select. It does not exit a surrounding loop or procedure. Outside Select Case it is a load error.

## Returns

Select Case, Case, End Select and Exit Select return no value. They are not Boolean calls and cannot be compared with TRUE or 1. The example functions explicitly Return a String or Integer. In value comparisons TRUE is numeric 1 and FALSE is numeric 0; Case True therefore matches 1, not every nonzero number.

## Behavior

- Preparation builds SelectInstruction, ordered CaseInstruction guards and resolved jumps. Execution stores the selection privately in the current function invocation, without adding a visible local variable. Recursive calls and nested blocks have independent captures; each new entry replaces the previous capture.
- CaseMatches examines alternatives from left to right and stops at the first match. The chosen body runs once, then a jump skips all remaining branches. Changes made by a case expression do not reread the captured selection. Side effects of expressions already evaluated are not undone.
- Numeric values and case-sensitive strings use the same comparisons as ordinary expressions. This engine does not implement Option Compare Text or automatic VB.NET type coercion. Use explicit conversion when comparing a number with text.
- End Select is required. Do not place executable statements before the first Case or continue a For/Next loop across two branches. Malformed blocks are rejected during loading. Enter a selection through Select Case, not GoTo into its middle.
- Errors propagate to the current error handler. On Error Resume Next skips a failed selection entirely; a failed Case advances to the next Case. Explicit Resume retries that failed instruction. Exit Select runs any active Finally it leaves. Stop/pause checks remain between runtime instructions; selection adds no wait or timeout.

## Examples

### 1. Classify a quantity

```vb
# DescribeAmount receives amount ByVal. Case 0 returns empty; 1 To 4 includes 1 and 4; Is >= 5 returns large. Remaining negative values reach Case Else. Main calls the helper with -1, 0, 4 and 5 and joins their results into negative:empty:small:large. These words are script results, not built-in modes.
Option Explicit On
Function DescribeAmount(ByVal amount)
    Select Case amount
        Case 0
            Return "empty"
        Case 1 To 4
            Return "small"
        Case Is >= 5
            Return "large"
        Case Else
            Return "negative"
    End Select
End Function

Sub Main()
    Return DescribeAmount(-1) & ":" & DescribeAmount(0) & ":" & DescribeAmount(4) & ":" & DescribeAmount(5)
End Sub
```

**Parameter and execution notes:**

DescribeAmount receives amount ByVal. Case 0 returns empty; 1 To 4 includes 1 and 4; Is >= 5 returns large. Remaining negative values reach Case Else. Main calls the helper with -1, 0, 4 and 5 and joins their results into negative:empty:small:large. These words are script results, not built-in modes.

### 2. Observe exactly which functions run

```vb
# ReadMode increments reads through ByRef and returns 2 once. Candidate increments checks and returns its value argument. Candidate(checks,1) fails; Candidate(checks,2) matches, so Candidate(checks,3) is skipped. selected becomes 7. Main returns 1*100+2*10+7=127, exposing all three values without accessing the game.
Option Explicit On
Function ReadMode(ByRef reads)
    reads += 1
    Return 2
End Function

Function Candidate(ByRef checks, ByVal value)
    checks += 1
    Return value
End Function

Sub Main()
    Dim reads = 0
    Dim checks = 0
    Dim selected = 0
    Select Case ReadMode(reads)
        Case Candidate(checks, 1)
            selected = -1
        Case Candidate(checks, 2), Candidate(checks, 3)
            selected = 7
        Case Else
            selected = -9
    End Select
    Return reads * 100 + checks * 10 + selected
End Sub
```

**Parameter and execution notes:**

ReadMode increments reads through ByRef and returns 2 once. Candidate increments checks and returns its value argument. Candidate(checks,1) fails; Candidate(checks,2) matches, so Candidate(checks,3) is skipped. selected becomes 7. Main returns 1*100+2*10+7=127, exposing all three values without accessing the game.

### 3. Exit a nested selection and finish cleanup

```vb
# route is the String harvest, matching the first alternative. trace becomes 1. The inner Case 2 executes Exit Select; trace=99 is skipped, but Finally appends 2. Execution resumes in the outer branch and appends 3, so Main returns 123. The outer Case Else is skipped. Changing route to another string returns -1.
Option Explicit On
Sub Main()
    Dim route = "harvest"
    Dim trace = 0
    Select Case route
        Case "harvest", "loot"
            trace = 1
            Select Case 2
                Case 2
                    Try
                        Exit Select
                        trace = 99
                    Finally
                        trace = trace * 10 + 2
                    End Try
            End Select
            trace = trace * 10 + 3
        Case Else
            trace = -1
    End Select
    Return trace
End Sub
```

**Parameter and execution notes:**

route is the String harvest, matching the first alternative. trace becomes 1. The inner Case 2 executes Exit Select; trace=99 is skipped, but Finally appends 2. Execution resumes in the outer branch and appends 3, so Main returns 123. The outer Case Else is skipped. Changing route to another string returns -1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
