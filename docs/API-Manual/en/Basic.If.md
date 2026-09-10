# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

IF selects at most one branch. It checks IF, then successive ELSEIF conditions until the first true result; otherwise it runs ELSE when present. Execution normally continues after END IF.

## Exact syntax

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## Parameters

- `condition` — condition: expression checked once on entry. Numeric zero is false; nonzero numbers are true. Prefer explicit comparisons or Boolean API results.
- `elseifCondition` — elseifCondition: optional additional condition, checked only if every earlier condition was false. Write ELSEIF as one word.
- `statements / ELSE` — statements / ELSE: statements on following lines. ELSE is optional, has no condition and may appear only once, last. THEN and END IF are required; use a multiline block.

## Returns

No value (Unit). IF is a control statement, not a function. A condition or a RETURN inside a selected branch may produce a value. A Boolean 1/0 may be compared with TRUE/FALSE; IF count accepts any nonzero count, whereas IF count=TRUE matches exactly 1.

## Behavior

- The compiler creates conditional and exit jumps. A false branch jumps to the next condition or ELSE; a selected branch skips the remaining alternatives. Nested IF blocks keep their own ELSE. RETURN leaves the procedure while honoring enclosing FINALLY.
- For legacy compatibility, IF tests equality with numeric zero rather than converting every kind with CBool. Text "0", empty text, arrays, objects and Unit are not numeric zero, so they select the true branch. Convert text explicitly or compare the intended property. AndAlso/OrElse instead require numeric operands.
- Declarations in a skipped branch do not create runtime variables. Declare and initialize shared results before IF. Option Explicit checks spelling, not whether every execution path assigns a value. Multiple ELSE clauses are rejected with SC015 before execution, also without Option Explicit.

## Examples

### 1. Classify four cases

```vb
# Classify(value) checks <0, =0 and <10 in order, then uses ELSE. Inputs -2, 0, 7, 20 return negative, zero, small, large. Main joins them as "negative:zero:small:large". Each helper call executes one RETURN only.
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**Parameter and execution notes:**

Classify(value) checks <0, =0 and <10 in order, then uses ELSE. Inputs -2, 0, 7, 20 return negative, zero, small, large. Main joins them as "negative:zero:small:large". Each helper call executes one RETURN only.

### 2. Nested decisions

```vb
# Action(enabled, amount) first checks enabled. If true, amount>0 chooses work, otherwise idle. The outer ELSE returns disabled. Main calls (TRUE,5), (TRUE,0), (FALSE,5) and returns "work:idle:disabled". Each END IF closes its matching block.
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**Parameter and execution notes:**

Action(enabled, amount) first checks enabled. If true, amount>0 chooses work, otherwise idle. The outer ELSE returns disabled. Main calls (TRUE,5), (TRUE,0), (FALSE,5) and returns "work:idle:disabled". Each END IF closes its matching block.

### 3. Observe condition evaluation

```vb
# Check(calls,value) increments calls ByRef and returns value. The first condition is false, the second true; the third condition and ELSE are skipped. result becomes 7, calls is 2. Main returns calls*10+result=27. All helpers and initial values are shown.
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**Parameter and execution notes:**

Check(calls,value) increments calls ByRef and returns value. The first condition is false, the second true; the third condition and ELSE are skipped. result becomes 7, calls is 2. Main returns calls*10+result=27. All helpers and initial values are shown.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
