# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Module groups functions, procedures, VAR/DIM and CONST under one name. Outside use Tools.Sum or Counter.count; members of the current module may use short names.

## Exact syntax

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## Parameters

- `moduleName` — moduleName: a simple case-insensitive identifier such as Tools. UO is reserved. Duplicate module names and nested Module declarations are rejected.
- `members` — members: SUB/FUNCTION, scalar VAR/DIM, CONST, Include and a valid Option Explicit directive. A field can hold an array or object value. Direct module-level DIM[...] is unsupported; create an array with a function and store it in VAR.
- `member / arguments` — member / arguments: the member name and its function arguments. Tools.Sum(2, 3) passes left=2 and right=3. A field access such as Counter.count has no parentheses.

## Returns

Module itself has no value and is not called as Module(...). Tools.Sum(...) returns the value of that function's RETURN; a field yields its stored value. Comparison results are Integer 1/0 and correspond to TRUE/FALSE in conditions and comparisons. An arbitrary number, ID or count is not automatically a Boolean result.

## Behavior

- Declare Module at file level and close it with End Module. Include may load a whole module or its members; errors retain the included file and line. Option Explicit belongs to the physical source file.
- Preparation collects qualified names, binds short references to the current module and validates visibility before execution. An explicitly declared local parameter, VAR, CONST or DIM shadows an equally named field. Otherwise resolution tries the current module field before a legacy global variable.
- Fields initialize in declaration order at the start of each separate run. Nested calls in that run share field mutations. Another run starts fresh; concurrent script runs do not share module state. This does not persist settings to disk.
- Module functions/procedures default to Public; fields/constants default to Private. Private requires Module. See Public / Private.
- The IDE lists qualified procedure names. Public procedures with no required arguments can be launched from the list; private helpers remain internal. Completion, navigation and variable inspection use the current module.

## Examples

### 1. Same names in different modules

```vb
# Tools.Sum adds left=2 and right=3, returning 5. Other.Sum multiplies them, returning 6. Qualified names distinguish the functions; Main returns Integer 11.
Option Explicit On
Module Tools
    Public Function Sum(ByVal left, ByVal right)
        Return left + right
    End Function
End Module
Module Other
    Public Function Sum(ByVal left, ByVal right)
        Return left * right
    End Function
End Module
Sub Main()
    Return Tools.Sum(2, 3) + Other.Sum(2, 3)
End Sub
```

**Parameter and execution notes:**

Tools.Sum adds left=2 and right=3, returning 5. Other.Sum multiplies them, returning 6. Qualified names distinguish the functions; Main returns Integer 11.

### 2. Shared field during one run

```vb
# count starts at 0. Each Increment changes that same field by 1; two calls leave before=2. Counter.count=5 is visible to Read. Main returns 2*10+5, Integer 25. A new run starts from 0 again.
Option Explicit On
Module Counter
    Public Var count As Integer = 0
    Public Sub Increment()
        count += 1
    End Sub
    Public Function Read()
        Return count
    End Function
End Module
Sub Main()
    Counter.Increment()
    Counter.Increment()
    Var before = Counter.Read()
    Counter.count = 5
    Return before * 10 + Counter.Read()
End Sub
```

**Parameter and execution notes:**

count starts at 0. Each Increment changes that same field by 1; two calls leave before=2. Counter.count=5 is visible to Read. Main returns 2*10+5, Integer 25. A new run starts from 0 again.

### 3. Boolean function result

```vb
# maximum=4 is accessible inside Limits. Allowed(3) returns Integer 1; Allowed(7) returns Integer 0. accepted=TRUE and rejected=FALSE test those results. Main returns Integer 10 on success.
Option Explicit On
Module Limits
    Private Const maximum = 4
    Public Function Allowed(ByVal amount)
        Return amount <= maximum
    End Function
End Module
Sub Main()
    Var accepted = Limits.Allowed(3)
    Var rejected = Limits.Allowed(7)
    If accepted = TRUE AndAlso rejected = FALSE Then
        Return 10
    End If
    Return 0
End Sub
```

**Parameter and execution notes:**

maximum=4 is accessible inside Limits. Allowed(3) returns Integer 1; Allowed(7) returns Integer 0. accepted=TRUE and rejected=FALSE test those results. Main returns Integer 10 on success.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
