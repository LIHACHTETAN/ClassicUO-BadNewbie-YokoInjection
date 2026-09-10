# +, -, *, /, MOD

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Arithmetic expressions calculate a value from their operands. + adds, - subtracts or negates, * multiplies, / divides, and MOD returns the integer remainder. Assign or return the expression to retain its result.

## Exact syntax

```text
left + right
left - right
-right
left * right
left / right
left MOD right
(expression)
```

## Parameters

- `left` — Left numeric operand: literal, declared variable, parenthesized expression or function result. Unary minus has no left operand.
- `right` — Right numeric operand. For / this is the divisor; for MOD it is converted to Integer and must remain nonzero after conversion. For example, a MOD divisor 0.5 truncates to 0 and causes an error.
- `operator / precedence` — Unary - binds first, then * / MOD at equal precedence from left to right, then binary + - from left to right. Parentheses override the order. Unary +, exponentiation ^ and integer-division backslash are not supported by this grammar.

## Returns

Integer for integer +, -, * and unary minus. If a participating numeric operand is Decimal, these operations give Decimal. / always gives Decimal, even for two integers: 5/2=2.5. MOD gives Integer. This is a calculated number, not a success flag or an item count unless the script gives it that meaning.

## Behavior

- MOD converts both operands to signed 32-bit integers using the engine’s integer conversion, truncating in-range fractions toward zero. The remainder keeps the dividend’s sign: -17 MOD 5=-2. -2147483648 MOD -1 is exactly 0. Keyword casing, including mOd, does not affect the result.
- MOD by zero raises an error that TRY/CATCH can handle. / uses floating-point division: a nonzero numerator divided by zero produces signed Infinity and 0/0 produces NaN. Check the divisor before division when an ordinary finite result is required.
- Integer +, -, * and negation use 32-bit wraparound on overflow; they do not promote automatically to a larger Integer. Convert an operand to Decimal before a large calculation when approximation is acceptable. Floating arithmetic has binary rounding error.
- Ordinary numeric operators do not silently parse text. String+String joins text, while String+Integer fails. Use a deliberate conversion such as CDbl when accepting numeric text. Infix MOD uses stricter text-to-integer conversion than the separate BasicMod function.
- The evaluator visits operands in expression order, dispatches the operator token and produces an InjectionValue. Parentheses cause their nested expression to finish first. No movement, waiting or network request happens unless an operand itself calls an API that does such work.

## Examples

### 1. Precedence and parentheses

```vb
# plain=2+3*4 evaluates multiplication first and becomes 14. grouped=(2+3)*4 becomes 20. Main returns plain*100+grouped=1420 so both calculations can be inspected.
Option Explicit On
SUB Main()
    VAR plain = 2 + 3 * 4
    VAR grouped = (2 + 3) * 4
    RETURN plain * 100 + grouped
END SUB
```

**Parameter and execution notes:**

plain=2+3*4 evaluates multiplication first and becomes 14. grouped=(2+3)*4 becomes 20. Main returns plain*100+grouped=1420 so both calculations can be inspected.

### 2. Whole batches and remaining items

```vb
# DescribeBatches receives total=27 and size=5. The size guard rejects zero/negative batch sizes. Fix(total/size) converts 5.4 to 5 whole batches; total mOd size returns 2 remaining items. CStr converts both for the returned text "5:2". The helper is fully defined.
Option Explicit On
FUNCTION DescribeBatches(total, size)
    IF size <= 0 THEN
        RETURN "invalid"
    END IF
    VAR whole = Fix(total / size)
    VAR remaining = total mOd size
    RETURN CStr(whole) + ":" + CStr(remaining)
END FUNCTION
SUB Main()
    RETURN DescribeBatches(27, 5)
END SUB
```

**Parameter and execution notes:**

DescribeBatches receives total=27 and size=5. The size guard rejects zero/negative batch sizes. Fix(total/size) converts 5.4 to 5 whole batches; total mOd size returns 2 remaining items. CStr converts both for the returned text "5:2". The helper is fully defined.

### 3. Handle an invalid divisor

```vb
# 10 MOD 0 has a zero divisor. It raises an error before assigning a result to unusedResult. CATCH stores the error in problem and sets caught=TRUE. Main returns 1; this is the example’s error-handling flag, not a value returned by the failed MOD.
Option Explicit On
SUB Main()
    VAR caught = FALSE
    TRY
        VAR unusedResult = 10 MOD 0
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Parameter and execution notes:**

10 MOD 0 has a zero divisor. It raises an error before assigning a result to unusedResult. CATCH stores the error in problem and sets caught=TRUE. Main returns 1; this is the example’s error-handling flag, not a value returned by the failed MOD.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: signedOperand / additiveOperand / comparativeOperand
Runtime/Interpreter.cs: VisitSignedOperand / VisitAdditiveOperand / VisitComparativeOperand
Runtime/InjectionValue.cs: arithmetic operators
Runtime/NumberConversions.cs: ToInt
-->
