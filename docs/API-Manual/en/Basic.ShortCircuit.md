# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

AndAlso and OrElse combine conditions while skipping an unnecessary right operand. AndAlso skips it when the left is false; OrElse skips it when the left is true. Use them to guard array access or avoid unnecessary calls.

## Exact syntax

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## Parameters

- `left` — left: expression evaluated first and once. Integer or Decimal zero is false; any nonzero numeric value is true.
- `right` — right: expression evaluated once only when required. Skipped array reads, function calls and side effects do not happen. An evaluated operand must be numeric; use CBool explicitly for text.

## Returns

Integer 1 (TRUE) or 0 (FALSE), never the original operand. You can compare result=1 or result=TRUE, and result=0 or result=FALSE. This engine uses 1 for true, not VB.NET’s numeric -1. A plain count remains a count; the Boolean conversion applies to this operation.

## Behavior

- Comparisons are evaluated inside each operand. AndAlso binds more tightly than OrElse; equal operators associate left to right. Parentheses override grouping. A skipped expression is still parsed and checked by Option Explicit.
- For compatibility, contiguous legacy AND/OR/XOR operations keep their old eager, left-to-right grouping inside an operand, before AndAlso/OrElse. Thus TRUE OR FALSE AndAlso FALSE is FALSE; TRUE OrElse FALSE AND FALSE is TRUE. Parenthesize when mixing old and new operators. AND, OR, && and || remain eager.
- Execution evaluates the left value, checks numeric truth, then either returns a Boolean or visits the required right expression. Required operand errors propagate to CATCH; FINALLY and pause/stop checkpoints continue to work. Skipping a call also skips any action it would perform.

## Examples

### 1. Guard the first array element

```vb
# FirstEquals receives items and expected. GetArrayLength(items)>0 is checked first, so an empty array never reads items[0]. Main passes [42] and an empty array, producing 1 and 0, and returns 10. The complete helper returns a Boolean without modifying the array.
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**Parameter and execution notes:**

FirstEquals receives items and expected. GetArrayLength(items)>0 is checked first, so an empty array never reads items[0]. Main passes [42] and an empty array, producing 1 and 0, and returns 10. The complete helper returns a Boolean without modifying the array.

### 2. Run a fallback once

```vb
# Probe increments calls through ByRef and returns TRUE. TRUE OrElse Probe(calls) skips Probe; FALSE OrElse Probe(calls) invokes it once. Both conditions return 1, while Main returns the final call count 1.
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**Parameter and execution notes:**

Probe increments calls through ByRef and returns TRUE. TRUE OrElse Probe(calls) skips Probe; FALSE OrElse Probe(calls) invokes it once. Both conditions return 1, while Main returns the final call count 1.

### 3. Guard division and show precedence

```vb
# AverageExceeds(total, count, limit) divides total by count only when count>0. Inputs (25,0,10) yield 0 and (25,2,10) yield 1 because 12.5>10. TRUE OrElse FALSE AndAlso FALSE yields 1: the right AndAlso group is skipped. Main returns "0:1:1".
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**Parameter and execution notes:**

AverageExceeds(total, count, limit) divides total by count only when count>0. Inputs (25,0,10) yield 0 and (25,2,10) yield 1 because 12.5>10. TRUE OrElse FALSE AndAlso FALSE yields 1: the right AndAlso group is skipped. Main returns "0:1:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
