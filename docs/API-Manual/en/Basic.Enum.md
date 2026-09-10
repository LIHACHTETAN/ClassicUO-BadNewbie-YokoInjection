# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Enum groups named Integer constants for script states and modes. Declare it at file or Module level, never inside Sub/Function. This engine implements a useful subset of VB.NET enumerations; it does not create a .NET Enum object.

## Exact syntax

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## Parameters

- `Public / Private` — Public is the default, including inside a Module. Private is allowed only inside a Module and hides the type and its members from other modules and the file scope.
- `name` — Use one simple name, such as Mode, without dots; names are case-insensitive. UO and built-in type names are reserved. An Enum, Module or global variable cannot reuse the same full name.
- `As Integer` — Optional; the only supported underlying type is signed 32-bit Integer, from -2147483648 to 2147483647. Other underlying types are rejected. As Mode in a variable, parameter or Function result uses ordinary Integer storage/conversion; it does not restrict values to the listed members. An uninitialized typed variable is 0.
- `member` — One simple member name per line, at least one member. Duplicate names, True and False are rejected. Without an expression, the first value is 0 and each next value is the previous value plus 1. Different names may intentionally share a value.
- `constantExpression` — Optional integer constant expression: decimal/0x hexadecimal integers, parentheses, unary minus, + - * / Mod, earlier members and already declared numeric Const values. The final result must be an in-range integer; division may have intermediate fractions. Referenced Const expressions must also yield an in-range integer and be untyped or As Integer/Long/Short/Byte. No function calls, variables, strings, comparisons or array reads. Forward member references, cyclic Const dependencies and dependencies deeper than 128 levels are rejected.
- `name.member` — Read a member as Mode.Ready; outside its Module use Tools.Mode.Ready. Inside Tools, Mode.Ready suffices. With Mode allows .Ready. Members are immutable: assignment, += or write-back through ByRef cannot change a constant. Enum types are not callable functions.

## Returns

The declaration itself returns no value and needs no parentheses. Reading a member returns Integer, for example Mode.Working = 3. This is a state value, not automatically a success flag. Compare named states explicitly. A Boolean comparison such as state = Mode.Finished returns 1/True or 0/False; both forms are usable for that comparison. A state value of 0 can mean Idle, not failure.

## Behavior

- During preparation, EnumCatalog scans declarations, resolves earlier numeric constants without executing any script/API, assigns automatic values and checks names, access and bounds. SC026 errors prevent startup even without Option Explicit. Parse errors also prevent execution; editing an incomplete declaration produces diagnostics.
- DefinitionCollector installs immutable numeric members before runtime global initializers and Optional defaults, so they can reference an Enum declared later in the file. Constant initializers inside the Enum still use only earlier constants. Prepared scripts retain this fixed catalog; loading a different script replaces it.
- ScriptBindings resolves module-relative names and Private access once. Execution reads ordinary constant values; loops do not re-evaluate Enum expressions or use reflection. As Mode is normalized to Integer, while the debugger may display Integer. Include can supply an Enum declaration. This feature has no Flags attribute, System.Enum methods, implicit member imports or automatic enumeration of members.

## Examples

### 1. Name script states

```vb
# TaskState has Idle=0 and Queued=1 automatically. Working=10 resets the sequence; Finished becomes 11. state As TaskState receives 10. Main returns String "0:1:10:11"; CStr converts each numeric value for display. Replace these names with the states in your script; declaring them does not start any procedure.
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**Parameter and execution notes:**

TaskState has Idle=0 and Queued=1 automatically. Working=10 resets the sequence; Finished becomes 11. state As TaskState receives 10. Main returns String "0:1:10:11"; CStr converts each numeric value for display. Replace these names with the states in your script; declaring them does not start any procedure.

### 2. Keep a module state private

```vb
# Controller.Mode belongs only to Controller. NextMode takes distance ByVal As Integer; it cannot modify the caller’s argument. distance<=1 selects Arrived=5, otherwise Walking=4. state starts at Integer 0. Main passes 3 and 1, receives 4 and 5, then returns Integer 45. No movement occurs here: distance is an example input. Outside code may call Controller.NextMode but cannot read Controller.Mode.Arrived.
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**Parameter and execution notes:**

Controller.Mode belongs only to Controller. NextMode takes distance ByVal As Integer; it cannot modify the caller’s argument. distance<=1 selects Arrived=5, otherwise Walking=4. state starts at Integer 0. Main passes 3 and 1, receives 4 and 5, then returns Integer 45. No movement occurs here: distance is an example input. Outside code may call Controller.NextMode but cannot read Controller.Mode.Arrived.

### 3. Advance through named states and return Boolean

```vb
# FirstState=2 is an earlier Integer Const. Mode.Idle=2, Working=3 and Finished=4. Advance receives state ByRef, so assignments update Main’s variable; With Mode abbreviates member names, and Select Case chooses the transition. Two calls move 2→3→4. IsFinal receives a copy ByVal and compares with Finished, returning 1/True. Main therefore returns Integer 1; calling IsFinal after one transition would return 0/False. A further Advance would throw "No next state"; Mode constants themselves never change.
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**Parameter and execution notes:**

FirstState=2 is an earlier Integer Const. Mode.Idle=2, Working=3 and Finished=4. Advance receives state ByRef, so assignments update Main’s variable; With Mode abbreviates member names, and Select Case chooses the transition. Two calls move 2→3→4. IsFinal receives a copy ByVal and compares with Finished, returning 1/True. Main therefore returns Integer 1; calling IsFinal after one transition would return 0/False. A further Advance would throw "No next state"; Mode constants themselves never change.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
