# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Update an existing variable or array element with +=, -=, *= or /=. The engine reads its current value, applies the operation and writes the result back without evaluating the target twice.

## Exact syntax

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## Parameters

- `target` — target: an existing scalar name or array element such as items[index] or grid[x][y]. Arrays need initialized elements and valid zero-based indices. This statement does not declare a variable.
- `operator` — += and &= add numbers or join two Strings; -= subtracts; *= multiplies; /= divides. The preprocessor changes &= to +=, so 5 &= 3 stores 8. String and number require explicit CStr. Write each operator as one token.
- `value` — value: an expression evaluated once after the target and indices. Its kind must work with the selected operation. Convert numbers with CStr before appending them to a String.

## Returns

No value (Unit). This is a statement, not an expression or success flag. Read target on a following line to obtain the stored result. Normal AS conversion applies on scalar writeback: Integer 5 divided with /=2 stores Integer 2, while an untyped numeric variable receives Decimal 2.5.

## Behavior

- Each array receiver is captured before evaluating its index. Indices run from left to right once, with bounds checked before the right operand. The selected slot stays the target even if an index or right-side ByRef function replaces the array variable or a parent array slot.
- The operator uses the same numeric/string rules as +, -, *, /: signed 32-bit integer overflow wraps, / produces Decimal and floating zero division may produce Infinity/NaN. Mixed String/number addition fails. Array elements have no scalar AS conversion.
- An undefined target, uninitialized element, bad index, incompatible operation, CONST write or failed type conversion raises a catchable error. The final write does not occur on failure, but side effects already performed by operand functions are not undone. CONST and AS checks occur at scalar writeback, after the right operand may have run.
- Option Explicit checks names before execution. Breakpoints and variable observation use the original line; busy loops still honor pause/stop checkpoints. This read/calculate/write sequence is not an atomic synchronization operation between concurrently running procedures.

## Examples

### 1. Use all four operators

```vb
# amount starts at 10. +=2 gives 12, -=3 gives 9, *=4 gives 36, /=2 gives Decimal 18. Main returns that stored value; the assignment statements themselves return no value.
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**Parameter and execution notes:**

amount starts at 10. +=2 gives 12, -=3 gives 9, *=4 gives 36, /=2 gives Decimal 18. Main returns that stored value; the assignment statements themselves return no value.

### 2. Evaluate an index once

```vb
# NextIndex increments its ByRef parameter calls and returns index 0. items[0] starts at 5. +=2 changes it to 7; NextIndex runs once, so calls=1. Main returns items[0]*10+calls=71. The helper is fully included.
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**Parameter and execution notes:**

NextIndex increments its ByRef parameter calls and returns index 0. items[0] starts at 5. +=2 changes it to 7; NextIndex runs once, so calls=1. Main returns items[0]*10+calls=71. The helper is fully included.

### 3. Handle a protected constant

```vb
# limit is CONST 5. The attempt limit+=1 raises an error at writeback; CATCH stores it in problem and sets caught=TRUE. limit remains 5. Main returns "5:1" via explicit CStr conversions. The flag describes error handling, not an assignment return value. The report is now built in a variable: report=CStr(limit), then report &= ":" and report &= CStr(caught). Each &= updates report; Return report yields "5:1".
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**Parameter and execution notes:**

limit is CONST 5. The attempt limit+=1 raises an error at writeback; CATCH stores it in problem and sets caught=TRUE. limit remains 5. Main returns "5:1" via explicit CStr conversions. The flag describes error handling, not an assignment return value. The report is now built in a variable: report=CStr(limit), then report &= ":" and report &= CStr(caught). Each &= updates report; Return report yields "5:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
