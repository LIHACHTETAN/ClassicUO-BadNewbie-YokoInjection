# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

NOT inverts a condition. AND requires both conditions, OR at least one, XOR exactly one. && is an alias of AND and || is an alias of OR. Keywords are case-insensitive.

## Exact syntax

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## Parameters

- `left` — Left condition for a binary operator. AND/OR require Integer or Decimal: zero is false and any nonzero number is true.
- `right` — Right condition, also numeric for AND/OR. Both operands are evaluated; a false left side of AND or a true left side of OR does not skip this expression.
- `NOT / grouping` — For NOT, parenthesize the complete condition to invert. For combinations of AND, OR and XOR, parentheses define the grouping explicitly.

## Returns

Integer 1 (TRUE) or Integer 0 (FALSE). These are logical operators, not bitwise operations: 2 AND 4 returns 1, not a bit mask. A returned flag may be checked with =TRUE or =1, =FALSE or =0.

## Behavior

- AND, OR and XOR share one precedence level and evaluate left to right in this engine: TRUE OR FALSE AND FALSE gives 0. TRUE OR (FALSE AND FALSE) gives 1. Keep this legacy rule in mind when adapting VB code.
- NOT(condition) evaluates the condition and reverses its truth. At the beginning of a comparison, NOT 1=2 means NOT(1=2). Parenthesize (NOT value) if the inverted value itself is one comparison operand.
- AND/OR reject String, Array, Object and Unit. Legacy NOT and XOR instead test equality with numeric zero: text "0", empty text, arrays, objects and Unit all count as nonzero. Use explicitly defined numeric predicates for such values; CBool has its own conversion rules.
- Every right-hand expression runs, including function calls, waits and their errors. Parentheses change grouping, not this eager evaluation. Use nested IF statements when a later expression must only execute after an earlier condition succeeds.

## Examples

### 1. Combine named flags

```vb
# ready=TRUE and blocked=FALSE. NOT(blocked) gives 1, so canRun becomes 1. ready XOR blocked is true because exactly one flag is true. Main returns canRun*10+exclusive=11.
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**Parameter and execution notes:**

ready=TRUE and blocked=FALSE. NOT(blocked) gives 1, so canRun becomes 1. ready XOR blocked is true because exactly one flag is true. Main returns canRun*10+exclusive=11.

### 2. Observe both eager calls

```vb
# Mark increments its ByRef parameter counter and returns TRUE. Main starts counter=0. FALSE AND Mark(counter) still calls Mark once; TRUE OR Mark(counter) calls it again. The results are 0 and 1, while Main returns counter=2. Mark is fully defined.
Option Explicit On
FUNCTION Mark(ByRef counter)
    counter = counter + 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR counter = 0
    VAR first = FALSE AND Mark(counter)
    VAR second = TRUE OR Mark(counter)
    RETURN counter
END SUB
```

**Parameter and execution notes:**

Mark increments its ByRef parameter counter and returns TRUE. Main starts counter=0. FALSE AND Mark(counter) still calls Mark once; TRUE OR Mark(counter) calls it again. The results are 0 and 1, while Main returns counter=2. Mark is fully defined.

### 3. Make grouping explicit

```vb
# legacy evaluates TRUE OR FALSE first, then AND FALSE, so it is 0. grouped evaluates the parenthesized FALSE AND FALSE first, then OR with TRUE, so it is 1. Main returns legacy*10+grouped=1.
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**Parameter and execution notes:**

legacy evaluates TRUE OR FALSE first, then AND FALSE, so it is 0. grouped evaluates the parenthesized FALSE AND FALSE first, then OR with TRUE, so it is 1. Main returns legacy*10+grouped=1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
