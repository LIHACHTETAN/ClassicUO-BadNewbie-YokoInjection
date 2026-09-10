# Option Explicit

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Requires variable declarations before script execution. This is a file directive of the Basic language in this engine, not a UO command or a function call.

## Exact syntax

```text
Option Explicit
Option Explicit On
Option Explicit Off
```

## Parameters

- `On / Off` — On enables strict declarations; Off disables this check. With no word after Explicit, On is implied. With no directive in the file, legacy non-strict mode is retained. Do not add parentheses or quotes.

## Returns

No value. The directive is not an expression and does not return TRUE/FALSE, a number or an ID. The RETURN statements in the examples belong to Main or Enough, not to Option Explicit.

## Behavior

- Write the directive once, before variables, constants and procedures. Blank lines and comments may precede it. A repeated or late directive is an SC013 error, including a later attempt to switch Off.
- In On mode, a read or assignment of an undeclared variable produces SC006 with a source location. Array names, FOR counters and object receivers are checked too. Declare with VAR/DIM/CONST; parameters and a named CATCH variable also introduce names. FOR VAR declares its counter.
- Declare local variables before their use. A local in one procedure does not declare a name in another procedure. Global declarations are available to procedures. This is name checking, not proof that every branch initializes every value.
- The parser reads the complete file; the analyzer resolves declarations; execution rejects strict validation errors before the first command. A reload applies the new file option independently of the preceding script. In Off mode, undeclared names may still produce warnings, and reading a value before it exists can still fail at runtime.
- The directive alone performs no game action and sends no packets. It does not establish full VB.NET compatibility or validate whether a game target exists.

## Examples

### 1. Declare before assignment

```vb
# On enables checking. DIM declares count as Integer; assigning 5 succeeds. Main returns 5. Changing count to an undeclared coutn prevents execution with SC006.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    RETURN count
END SUB
```

**Parameter and execution notes:**

On enables checking. DIM declares count as Integer; assigning 5 succeeds. Main returns 5. Changing count to an undeclared coutn prevents execution with SC006.

### 2. Parameters and a global constant

```vb
# The bare directive means On. minimum is a global constant equal to 3. amount is a declared parameter inside Enough and a separate local inside Main. Enough compares 5 >= 3 and returns TRUE, numerically 1.
Option Explicit
CONST minimum = 3
FUNCTION Enough(amount)
    RETURN amount >= minimum
END FUNCTION
SUB Main()
    VAR amount = 5
    RETURN Enough(amount)
END SUB
```

**Parameter and execution notes:**

The bare directive means On. minimum is a global constant equal to 3. amount is a declared parameter inside Enough and a separate local inside Main. Enough compares 5 >= 3 and returns TRUE, numerically 1.

### 3. Run an older script

```vb
# Off permits the assignment to create legacyCounter without DIM. Main returns 7. This compatibility example may still show a declaration warning; declare the variable and use On for strict checking.
Option Explicit Off
SUB Main()
    legacyCounter = 7
    RETURN legacyCounter
END SUB
```

**Parameter and execution notes:**

Off permits the assignment to create legacyCounter without DIM. Main returns 7. This compatibility example may still show a declaration warning; declare the variable and use On for strict checking.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: optionExplicit
Analysis/SanityAnalyzer.cs
Analysis/InvalidSymbolVisitor.cs
Runtime/InjectionRuntime.cs
-->
