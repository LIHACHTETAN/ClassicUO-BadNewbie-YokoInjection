# SUB Main()

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

A Basic file contains procedure/function definitions and optional global declarations. Put executable work inside a procedure. These examples use Main() as their entry point and are complete files, not fragments to paste outside a procedure.

## Exact syntax

```text
Option Explicit On
SUB Main()
    statement
END SUB
# comment
; comment
REM comment
// comment
' comment
```

## Parameters

- `Main / entry` — Entry procedure selected for execution. Main is a conventional name, not an automatic statement. SUB Main() declares a procedure with no arguments. A helper is run only when called.
- `statement` — One executable statement per line inside SUB…END SUB or FUNCTION…END FUNCTION. Global VAR/CONST declarations and Option Explicit belong outside those bodies. Put Option Explicit before declarations.
- `comment` — # and ; start comments outside quoted strings, including after code. REM, // and an apostrophe start full-line comments after optional indentation. A quoted string may contain comment characters literally.

## Returns

A file or SUB declaration returns no value merely by being loaded. RETURN expression returns that value from the invoked procedure; it also ends that invocation immediately. Finishing a body or using RETURN without an expression produces Unit (no value).

## Behavior

- Save source text as UTF-8 to preserve localized comments and strings. CRLF and LF line endings are accepted. Indentation and blank lines improve readability but do not replace END SUB or END FUNCTION.
- Keywords, procedure names and variable identifiers ignore letter case. itemCount, ITEMCOUNT and ItemCount resolve to the same binding. String contents keep their case; string keys such as UO.SetGlobal("Key", …) are data, not identifiers.
- Use ASCII letters or underscore to start a simple name, followed by letters, digits or underscore. Avoid reserved keywords and API names for your own declarations. Dotted API names such as UO.Print are qualified calls. A colon after a name defines a label, not a general separator for several statements.
- The engine normalizes supported Basic syntax, parses the whole file, collects declarations and checks names. A helper may therefore appear below Main. Loading does not execute all the declared helpers; starting the chosen procedure initializes its run and follows its calls.
- The examples calculate values only. After testing a template, place the required UO calls inside its body. These file and comment rules describe this engine; they do not imply support for every construct of another Basic implementation.

## Examples

### 1. Comments and literal text

```vb
# Main declares note containing "ore #1; keep". The # and ; inside the string are retained. The other #, REM, // and apostrophe comments do no work. RETURN gives the original text.
Option Explicit On
# Complete file
SUB Main()
    REM Full-line comment
    VAR note = "ore #1; keep" # Trailing comment
    // Another full-line comment
    ' Another full-line comment
    RETURN note
END SUB
```

**Parameter and execution notes:**

Main declares note containing "ore #1; keep". The # and ; inside the string are retained. The other #, REM, // and apostrophe comments do no work. RETURN gives the original text.

### 2. A fully defined helper

```vb
# Main calls DoubleCount with amount=7. The helper is defined below Main, multiplies its Integer parameter by 2 and returns 14. Main forwards that value. No missing Include file or undeclared helper is required.
Option Explicit On
SUB Main()
    RETURN DoubleCount(7)
END SUB
FUNCTION DoubleCount(ByVal amount AS Integer)
    VAR result = amount * 2
    RETURN result
END FUNCTION
```

**Parameter and execution notes:**

Main calls DoubleCount with amount=7. The helper is defined below Main, multiplies its Integer parameter by 2 and returns 14. Main forwards that value. No missing Include file or undeclared helper is required.

### 3. Identifier casing

```vb
# The script declares itemCount=3, then uses ITEMCOUNT and itemcount to add 2 to the same variable. Mixed-case keywords are accepted. Main returns 5; the different spelling does not create extra variables.
Option Explicit On
sUb Main()
    Var itemCount = 3
    ITEMCOUNT = itemcount + 2
    ReTuRn ItemCount
EnD sUb
```

**Parameter and execution notes:**

The script declares itemCount=3, then uses ITEMCOUNT and itemcount to add 2 to the same variable. Mixed-case keywords are accepted. Main returns 5; the different spelling does not create extra variables.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: file / subrutine / LineComment / SYMBOL
Runtime/BasicSyntaxPreprocessor.cs: Process
Runtime/InjectionRuntime.cs: Prepare / Load / CallSubrutineValues
Runtime/SemanticScope.cs: Scope
https://learn.microsoft.com/en-us/dotnet/visual-basic/reference/language-specification/introduction (comparison of identifier casing only)
-->
