# CONST

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

CONST declares a name whose binding rejects ordinary reassignment. It can hold a literal or an expression result. This engine evaluates the initializer at runtime when the declaration is executed.

## Exact syntax

```text
CONST name [AS type] = expression [, name ...]
```

## Parameters

- `name` — Constant identifier without quotes. Use a distinct name in its scope. A declaration outside procedures is global; a declaration inside a procedure is local to that invocation.
- `type` — Optional supported AS type, using the same conversions as VAR. For example, AS Integer converts the initializer to this engine’s signed 32-bit integer. Square brackets denote optional syntax and are not typed around AS.
- `expression` — Required initializer. A number, quoted string, TRUE/FALSE, arithmetic expression or supported function result is allowed. The result is evaluated once for this execution of the declaration, not once forever for the file.

## Returns

No value. CONST is a declaration, not a function or Boolean query. Reading its name gives the stored initializer result. RETURN in the examples belongs to Main or ApplyLimit.

## Behavior

- Ordinary assignment, LET and SET cannot replace this binding: execution raises a constant-assignment error. TRY/CATCH can handle that runtime error. Option Explicit requires a declaration but does not turn every invalid assignment into a pre-execution error.
- A global constant is initialized for a new top-level run and inherited by called procedures with its constant flag and AS type. Local constants initialize when their declaration runs. A function initializer can therefore perform work again on a later run.
- This is binding protection, not deep freezing of Array/Object contents. A separate local declaration can shadow a global name; another declaration creates a new binding. Avoid reusing constant names to keep the script clear.
- Execution evaluates the initializer, applies AS conversion and records the constant flag in the scope. Later ordinary assignment checks that flag before changing storage. Scalar literal examples perform no game action.

## Examples

### 1. Fixed delay used in a calculation

```vb
# delay is a local Integer constant equal to 350. Multiplication by 2 produces a separate variable doubled=700. Main returns 700; the example does not perform a wait.
Option Explicit On
SUB Main()
    CONST delay AS Integer = 350
    VAR doubled = delay * 2
    RETURN doubled
END SUB
```

**Parameter and execution notes:**

delay is a local Integer constant equal to 350. Multiplication by 2 produces a separate variable doubled=700. Main returns 700; the example does not perform a wait.

### 2. Pass a global limit to a helper

```vb
# limit is a global Integer constant equal to 50. ApplyLimit receives amount=72 and maximum=50, then returns the smaller amount, 50. The helper is fully defined and only reads its parameters.
Option Explicit On
CONST limit AS Integer = 50
FUNCTION ApplyLimit(amount, maximum)
    IF amount > maximum THEN
        RETURN maximum
    END IF
    RETURN amount
END FUNCTION
SUB Main()
    RETURN ApplyLimit(72, limit)
END SUB
```

**Parameter and execution notes:**

limit is a global Integer constant equal to 50. ApplyLimit receives amount=72 and maximum=50, then returns the smaller amount, 50. The helper is fully defined and only reads its parameters.

### 3. Handle forbidden reassignment

```vb
# limit starts at 3. Assigning 4 raises an error and does not change the constant. CATCH binds the error to problem and sets caught=TRUE. Main returns logical 1; TRUE and 1 are equivalent here.
Option Explicit On
SUB Main()
    CONST limit = 3
    VAR caught = FALSE
    TRY
        limit = 4
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Parameter and execution notes:**

limit starts at 3. Assigning 4 raises an error and does not change the constant. CATCH binds the error to problem and sets caught=TRUE. Main returns logical 1; TRUE and 1 are equivalent here.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: constDeclaration / globalConst
Runtime/DefinitionCollector.cs: VisitGlobalConst
Runtime/Interpreter.cs: VisitConstDef
Runtime/SemanticScope.cs: DefineVar / SetVar
-->
