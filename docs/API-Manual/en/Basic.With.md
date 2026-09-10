# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

With groups operations on one captured object. A leading dot selects a member of that object. Basic also allows With UO and With moduleName as explicit namespace shorthand; these two forms are engine extensions.

## Exact syntax

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## Parameters

- `objectExpression / UO / moduleName` — Required receiver: a native object such as List(), Dictionary(), a variable containing one, or a function returning one. The expression is evaluated once on entry, even for an empty body. Numbers, text, arrays and Unit are not object receivers in this engine. A local object variable takes precedence over an equally named module.
- `.Method(arguments) / .field` — For objects use methods, including parentheses: .Add(value), .Item(index), .Count(). Their arguments and results are unchanged; see Basic.List/Basic.Dictionary. Arbitrary object fields/properties are not supported here. A module permits accessible .field and .Procedure(arguments); Private restrictions still apply. With UO makes .Command(...) mean UO.Command(...). It does not enable bare game commands elsewhere.
- `statements / End With` — The body may be empty or contain calls, assignments, conditions and correctly nested loops/blocks. End With is required. Outside the body a leading-dot member is invalid. Other objects can still be accessed with their full names.

## Returns

With is a control block, not a value-returning function: it does not return an ID, Boolean or success flag. Each member call keeps its own return contract. The Return statements in these examples explicitly return Integer values from Main; 127, 28 and 72 are demonstration calculations.

## Behavior

- Preparation validates the block and binds relative members. On entry, the interpreter evaluates and captures the object reference in the current call frame. Reassigning the original variable does not change this reference. Re-entering the header evaluates the expression again; recursive calls have separate captures.
- The header of a nested With is evaluated in the outer context; inside its body the dot refers to the inner object. End With restores the outer context. Return, loop transfers and outward GoTo discard scopes they leave after applicable Finally blocks execute. Jumping into a With body is rejected.
- An invalid receiver or unknown method raises an error, not false. Catch/On Error may handle it. On Error Resume Next skips the whole block if its receiver fails. With does not loop, wait or start a thread; pause/stop checkpoints remain active. Binding is cached with the prepared script, and the receiver is not re-evaluated for each member call.

## Examples

### 1. Capture once

```vb
# Choose receives values ByVal and calls ByRef, increments calls to 1 and returns the original list. Both .Add calls append whole values 2 and 7 to that captured list, although values is reassigned to a new list in between. Item uses zero-based indices 0 and 1. Main returns 1*100+2*10+7=127.
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**Parameter and execution notes:**

Choose receives values ByVal and calls ByRef, increments calls to 1 and returns the original list. Both .Add calls append whole values 2 and 7 to that captured list, although values is reassigned to a new list in between. Item uses zero-based indices 0 and 1. Main returns 1*100+2*10+7=127.

### 2. Nested objects and cleanup

```vb
# groups maps the text key "child" to the list child. .Item("child") reads that object through the outer dictionary. The inner .Add(2) and Finally .Add(7) modify the list. After End With, .Set("result",8) addresses the dictionary again. Count() returns two entries; Item("result") returns 8, so Main returns 28.
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**Parameter and execution notes:**

groups maps the text key "child" to the list child. .Item("child") reads that object through the outer dictionary. The inner .Add(2) and Finally .Add(7) modify the list. After End With, .Set("result",8) addresses the dictionary again. Count() returns two entries; Item("result") returns 8, so Main returns 28.

### 3. Module fields and the UO namespace

```vb
# With Tools qualifies .total, .AddAmount and .CountItems. total starts at 4 and AddAmount receives amount=3 ByVal, giving 7. CountItems receives the two-element array and uses With UO to call UO.GetArrayLength(values), returning 2. Main computes 7*10+2=72. Module access rules remain in force.
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**Parameter and execution notes:**

With Tools qualifies .total, .AddAmount and .CountItems. total starts at 4 and AddAmount receives amount=3 ByVal, giving 7. CountItems receives the two-element array and uses With UO to call UO.GetArrayLength(values), returning 2. Main computes 7*10+2=72. Module access rules remain in force.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
