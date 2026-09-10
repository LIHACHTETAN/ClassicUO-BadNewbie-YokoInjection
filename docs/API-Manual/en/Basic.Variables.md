# VAR / DIM

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

VAR and scalar DIM declare a named value. Assignment evaluates the expression and stores its result. A declaration inside a procedure is local to that call; a declaration outside procedures is global to the script.

## Exact syntax

```text
VAR name [AS type] [= expression] [, name ...]
DIM name [AS type] [= expression] [, name ...]
name = expression
LET name = expression
SET name = expression
```

## Parameters

- `name` — Variable identifier, without quotes. Use letters, digits and underscores, beginning with a letter or underscore. Keep variable names consistently spelled; do not use language keywords.
- `type` — Optional AS annotation. Integer/Long/Short/Byte use this engine’s signed 32-bit integer conversion; Double/Single/Decimal use its double-precision number; String stores text; Boolean/Bool stores a logical value; Variant/Object retains the value kind. These aliases do not impose separate VB.NET byte/short/long ranges.
- `expression` — Optional initializer in VAR/DIM, required right-hand expression in assignment. It is evaluated when that statement executes. A scalar with AS String and no initializer starts as empty text; typed numeric and Boolean defaults are zero. Without an initializer, untyped VAR and VAR AS Variant/Object contain Unit (no value), while scalar DIM supplies 0. An untyped variable can later contain a different value kind.

## Returns

No value. VAR, DIM and assignment statements do not return a result. Reading the declared name gives its stored value. RETURN in each example returns that value from Main; it is not the return value of DIM.

## Behavior

- Square brackets in the syntax above indicate optional text; do not type them around AS or an initializer. Array DIM uses a different declaration form.
- LET and SET are compatibility forms of ordinary assignment in this engine. They do not declare a name under Option Explicit On. Declared AS types are also applied to later assignments; invalid conversion or an unsupported type raises a runtime error.
- Local names belong to a procedure call. Declaring a local inside IF does not create a separate block scope. A declaration in a branch that never executes does not create a runtime value. Use a declaration before branching when the value is needed afterwards.
- Injection compatibility: a called procedure inherits the caller’s current global scalar values and their AS types. Reassigning a scalar in the callee does not update the caller. Return the new value or pass a BYREF argument when that update is needed. This is not a deep clone of Array/Object values. A new top-level run initializes globals again; a local declaration shadows its frame’s name without replacing the global declaration.
- Execution evaluates the initializer, defines storage in the current scope and applies the declared conversion. A later assignment evaluates its right-hand side before updating storage. These examples calculate locally; their variables are not automatically saved to a profile or JSON file.

## Examples

### 1. Update an integer

```vb
# count starts at 0, becomes 5, then LET adds 2. Main returns the Integer 7. The first DIM declares the name; the later assignments update it.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    LET count = count + 2
    RETURN count
END SUB
```

**Parameter and execution notes:**

count starts at 0, becomes 5, then LET adds 2. Main returns the Integer 7. The first DIM declares the name; the later assignments update it.

### 2. Text and a logical flag

```vb
# label starts as empty String. SET stores "ore". enabled is Boolean TRUE; the IF branch returns the String "ore". TRUE is unquoted and represents logical 1.
Option Explicit On
SUB Main()
    DIM label AS String
    VAR enabled AS Boolean = TRUE
    SET label = "ore"
    IF enabled = TRUE THEN
        RETURN label
    END IF
    RETURN "disabled"
END SUB
```

**Parameter and execution notes:**

label starts as empty String. SET stores "ore". enabled is Boolean TRUE; the IF branch returns the String "ore". TRUE is unquoted and represents logical 1.

### 3. Global input and local calculation

```vb
# baseAmount is global and equals 4. extra is local to Calculate and equals 3. Calculate returns 7; Main stores it in its own local result and returns 7. extra is not a local variable of Main.
Option Explicit On
VAR baseAmount AS Integer = 4
FUNCTION Calculate()
    VAR extra = 3
    RETURN baseAmount + extra
END FUNCTION
SUB Main()
    VAR result = Calculate()
    RETURN result
END SUB
```

**Parameter and execution notes:**

baseAmount is global and equals 4. extra is local to Calculate and equals 3. Calculate returns 7; Main stores it in its own local result and returns 7. extra is not a local variable of Main.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim
Runtime/Interpreter.cs: VisitVarDef / VisitAssignment
Runtime/SemanticScope.cs: DefineVar / SetVar / Coerce
-->
