# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

For repeats a block over an inclusive numeric range. Use it for array indices or a known number of operations; For Each instead enumerates element values.

## Exact syntax

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## Parameters

- `counter / VAR` — Scalar counter variable. VAR declares a procedure-local counter; otherwise use an existing writable variable. Under Option Explicit On declare it first or use For Var. For a typed counter declare DIM counter AS Integer before the loop; AS in the numeric For header is not supported.
- `start` — Numeric starting expression, evaluated once and assigned before limit and increment are evaluated.
- `limit` — Inclusive numeric endpoint, evaluated once on entry. Positive steps compare counter <= limit; negative steps compare counter >= limit.
- `increment` — Optional numeric step, default 1. Negative and fractional steps are allowed; zero raises a catchable error. Use a compatible counter type and values that make progress.
- `statements / Next / exit` — Body and closing Next on separate lines. The optional Next name must match the counter. Continue For reaches the next step; Exit For leaves the nearest For/For Each; Break leaves the nearest loop of any kind.

## Returns

For, Next and Exit For return no value. The counter is a number, not an automatic item ID. On normal completion this engine retains the last executed counter value, rather than an out-of-range value. A skipped loop retains start; an early exit retains the current value. Main in the examples returns Integer 12, 28 and 395.

## Behavior

- Entry: assign start, capture limit and step, reject zero step, then test the first value. A range facing away from its endpoint skips the body. Start=limit runs once.
- Next checks counter+step against the captured endpoint and assigns it only if another iteration fits. Thus 1 To 5 Step 3 visits 1 and 4. Changing the variables used for limit/step does not change captured values; changing the counter itself affects the next step.
- Loop structure and Next names are checked before execution; invalid structure reports SC020. Nested loops need distinct counters. Exiting a Try runs Finally; ordinary pause/stop checks remain active. A loop adds no automatic delay or timeout.

## Examples

### 1. Sum array cells

```vb
# values[2] allocates indices 0, 1, 2 with values 2, 4, 6. Sum receives the array ByVal, starts index at 0 and captures length-1=2. Default step 1 visits all three cells; total=12 is returned to Main.
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**Parameter and execution notes:**

values[2] allocates indices 0, 1, 2 with values 2, 4, 6. Sum receives the array ByVal, starts index at 0 and captures length-1=2. Default step 1 visits all three cells; total=12 is returned to Main.

### 2. Delete from the end

```vb
# items contains -1, 3, -2, 5. Start is Count()-1=3, limit is 0, step is -1. Removing a negative cell shifts only indices already visited, so no pending cell is skipped. Remaining values are 3, 5; Count()*10+3+5 returns 28.
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**Parameter and execution notes:**

items contains -1, 3, -2, 5. Start is Count()-1=3, limit is 0, step is -1. Removing a negative cell shifts only indices already visited, so no pending cell is skipped. Remaining values are 3, 5; Count()*10+3+5 returns 28.

### 3. Capture limits and inspect the counter

```vb
# ReadLimit increments calls ByRef and returns its value argument. Entry evaluates start=1, limit=5 and step=2 exactly once: calls=3. Later assignments upper=99 and stride=1 do not change this loop. It visits 1, 3, 5; total=9, index remains 5. Main returns 300+90+5=395.
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**Parameter and execution notes:**

ReadLimit increments calls ByRef and returns its value argument. Entry evaluates start=1, limit=5 and step=2 exactly once: calls=3. Later assignments upper=99 and stride=1 do not change this loop. It visits 1, 3, 5; total=9, index remains 5. Main returns 300+90+5=395.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
