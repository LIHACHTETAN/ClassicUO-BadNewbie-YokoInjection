# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Public exposes a module member to external code. Private permits access only from functions, procedures and initializers in its own module. Place the modifier before the declaration, not the call.

## Exact syntax

```text
Public declaration
Private declaration
```

## Parameters

- `visibility` — visibility: Public or Private. Without a modifier, module SUB/FUNCTION are public and VAR/DIM/CONST are private.
- `declaration` — declaration: SUB/FUNCTION, scalar VAR/DIM or CONST. Public also applies to Module and file-level declarations. Private is invalid at file level or inside a procedure body. Declare member names without a dot.

## Returns

Public and Private return no value. They do not alter function results or field types. Normalize(12) in the example returns Integer 10 through RETURN; NextCount() returns the new count, not TRUE/FALSE.

## Behavior

- Inside a Module both short and qualified names of its own members are allowed. External code can access only Public through ModuleName.Member. Public does not import a field into the unqualified global namespace.
- Access is validated before execution, even with Option Explicit Off. Access to another module’s Private produces SC019; invalid module/modifier declarations produce SC018 or a syntax error. Initializers do not run after these errors.
- A public function may call a private helper: access depends on where the calling function is declared, not who launched it. A private helper cannot be launched separately from the IDE, a hotkey or the host procedure API.
- Public Const remains read-only; Public Var remains mutable. An explicit local of the same name shadows a field only in that procedure. Private does not encrypt source or hide code from its owner.
- Debugger short names and Private access use the selected frame. The field is accessible inside the module; selecting the outside caller rejects a direct ModuleName.privateField watch expression.

## Examples

### 1. Public wrapper and private helper

```vb
# value=12 passes into Limits.Normalize and then Clamp. maximum=10 caps the value; Clamp and Normalize return Integer 10. Main calls only public Normalize. An outside Limits.Clamp(12) call is forbidden.
Option Explicit On
Module Limits
    Private Const maximum = 10
    Private Function Clamp(ByVal value)
        If value > maximum Then
            Return maximum
        End If
        Return value
    End Function
    Public Function Normalize(ByVal value)
        Return Clamp(value)
    End Function
End Module
Sub Main()
    Return Limits.Normalize(12)
End Sub
```

**Parameter and execution notes:**

value=12 passes into Limits.Normalize and then Clamp. maximum=10 caps the value; Clamp and Normalize return Integer 10. Main calls only public Normalize. An outside Limits.Clamp(12) call is forbidden.

### 2. Private field and local variable

```vb
# Unmodified VAR value=7 is private in Store. Read returns field value 7. LocalValue declares its own value=9 without changing the field. Main returns 7*10+9, Integer 79.
Option Explicit On
Module Store
    Var value = 7
    Public Function Read()
        Return value
    End Function
    Public Function LocalValue()
        Var value = 9
        Return value
    End Function
End Module
Sub Main()
    Return Store.Read() * 10 + Store.LocalValue()
End Sub
```

**Parameter and execution notes:**

Unmodified VAR value=7 is private in Store. Read returns field value 7. LocalValue declares its own value=9 without changing the field. Main returns 7*10+9, Integer 79.

### 3. Expose a constant, retain a private counter

```vb
# Public Const increment=2 can be read as Counter.increment. Private count starts at 1. NextCount adds increment, stores 3 and returns 3. Main returns 3*10+2, Integer 32. Outside access to Counter.count and changes to increment are forbidden.
Option Explicit On
Module Counter
    Public Const increment = 2
    Private Var count = 1
    Public Function NextCount()
        count += increment
        Return count
    End Function
End Module
Sub Main()
    Var result = Counter.NextCount()
    Return result * 10 + Counter.increment
End Sub
```

**Parameter and execution notes:**

Public Const increment=2 can be read as Counter.increment. Private count starts at 1. NextCount adds increment, stores 3 and returns 3. Main returns 3*10+2, Integer 32. Outside access to Counter.count and changes to increment are forbidden.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
