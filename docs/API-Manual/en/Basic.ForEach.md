# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

For Each reads each element of an array or a native enumerable collection in order, without a numeric index. It is a loop statement inside a procedure or function; it is not a callable API function.

## Exact syntax

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## Parameters

- `item` — item: iteration variable. Reuse an existing local, parameter or accessible field; if it is absent, create a procedure local, also with Option Explicit On. Assignment to a constant is forbidden.
- `type` — type: optional AS type, for example Integer. This declares a local iterator and converts each element on assignment. Without AS an existing variable retains its declared type.
- `collection` — collection: expression evaluated once on entry. Supported values are an array or a native object exposing enumeration. Scalars are errors. Nested arrays yield rows first; use a nested loop for cells.
- `statements / NEXT item` — statements / NEXT item: body and loop terminator. The name after NEXT is optional; when present it must match the counter. NEXT is written on its own line.

## Returns

For Each and Next return no value. item receives the element value, not its index, array length, item ID or stack quantity automatically. The value depends on the collection. RETURN inside the body exits the entire function with that value; the examples return Integer 12, 105 and 10.

## Behavior

- Preparation pairs FOR EACH with NEXT and validates structure before any initializer runs. A mismatched NEXT produces SC020. After evaluating collection once, the interpreter keeps its reference and its own cursor; changing item cannot move that cursor.
- Arrays are read in ascending index order. A zero-length array skips the body and preserves an existing untyped iterator value. An uninitialized element raises a catchable runtime error. AS conversion errors are also catchable.
- Assigning item changes only the iterator variable. It does not replace the array element. Arrays and objects stored as elements are references: modifying a nested row modifies that row. Reassigning collection in the body does not switch the active collection; changes to later elements of the same array are observed when read.
- Continue For advances the nearest For or For Each; Exit For exits it. Exceptions, RETURN and cancellation release active native enumerators. Native collections may reject modifications during iteration; do not assume snapshot semantics.
- The iterator is visible in its procedure after the loop and retains the last assigned value. Separate executions have separate cursors. The IDE offers the iterator name, loop snippets and declaration navigation; normal pause/stop checkpoints remain active.

## Examples

### 1. Sum an array without an index

```vb
# values has upper bound 2 and three elements: 2, 4, 6. SumItems receives that array; item receives each number. total starts at 0, accumulates 12, and RETURN passes Integer 12 to Main. NEXT item closes the same iterator.
Option Explicit On
Function SumItems(values)
    Var total = 0
    For Each item In values
        total += item
    Next item
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return SumItems(values)
End Sub
```

**Parameter and execution notes:**

values has upper bound 2 and three elements: 2, 4, 6. SumItems receives that array; item receives each number. total starts at 0, accumulates 12, and RETURN passes Integer 12 to Main. NEXT item closes the same iterator.

### 2. Evaluate once and convert each value

```vb
# calls is passed ByRef into SelectItems and becomes 1. The function returns ["2", "3"]. AS Integer converts these strings to 2 and 3; total becomes 5. item=100 does not alter the source or iteration order. Main returns calls*100+total = Integer 105.
Option Explicit On
Function SelectItems(ByRef calls)
    calls += 1
    Dim values[1]
    values[0] = "2"
    values[1] = "3"
    Return values
End Function
Sub Main()
    Var calls = 0
    Var total = 0
    For Each item As Integer In SelectItems(calls)
        total += item
        item = 100
    Next
    Return calls * 100 + total
End Sub
```

**Parameter and execution notes:**

calls is passed ByRef into SelectItems and becomes 1. The function returns ["2", "3"]. AS Integer converts these strings to 2 and 3; total becomes 5. item=100 does not alter the source or iteration order. Main returns calls*100+total = Integer 105.

### 3. Nested arrays and independent cursors

```vb
# rows[1][1] contains two rows of two cells. row receives an array reference, then cell receives 1, 2, 3, 4. Each NEXT closes its own loop. SumGrid and Main return Integer 10. No item IDs or quantities are inferred.
Option Explicit On
Function SumGrid(rows)
    Var total = 0
    For Each row In rows
        For Each cell In row
            total += cell
        Next cell
    Next row
    Return total
End Function
Sub Main()
    Dim rows[1][1]
    rows[0][0] = 1
    rows[0][1] = 2
    rows[1][0] = 3
    rows[1][1] = 4
    Return SumGrid(rows)
End Sub
```

**Parameter and execution notes:**

rows[1][1] contains two rows of two cells. row receives an array reference, then cell receives 1, 2, 3, 4. Each NEXT closes its own loop. SumGrid and Main return Integer 10. No item IDs or quantities are inferred.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
