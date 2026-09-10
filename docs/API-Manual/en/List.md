# List

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

List() creates an ordered, resizable collection. Use its returned object through a variable; items.Add is an object method, not a global List.Add command.

## Exact syntax

```text
List() -> Object
List(source:Any) -> Object
```

## Parameters

- `source` — source: omitted means empty; List accepts an array or List, Dictionary accepts a Dictionary. Copying creates independent containers with shared nested object/array references.

## Returns

The factory returns an Object:List. Item/index reads return the stored value. Count is item count; IndexOf is a zero-based position or -1. Contains/Remove return 1=TRUE or 0=FALSE. Add/Insert/Set/RemoveAt/Clear return Unit. ToArray returns a new Array.

## Behavior

- index / key: List positions are numeric whole numbers, starting at 0; Insert also accepts Count(). Dictionary accepts text or finite numbers. Numeric 1 and 1.0 denote one key; text "1" is different.
- value: an initialized Basic value, including nested arrays/collections. Unit cannot be stored. Equality compares numeric values, case-sensitive text, or array/object identity.
- fallback: Get returns this value for an absent key without inserting it. Arguments, including fallback expressions, evaluate before the method call.
- Add appends; Insert inserts before the position; Set/index assignment replaces an existing element. Item/index reads it. Remove deletes the first equal value; RemoveAt deletes a position. Clear removes all elements.
- Contains tests membership; IndexOf finds the first match. Invalid indices (negative, fractional, text or outside the range) raise a catchable error and do not alter the list.
- For Each preserves list order. ToArray is a shallow snapshot: iterate it when adding, replacing or removing list elements.
- Changing a collection during its direct For Each enumeration, including Set, raises a catchable error on the next step. Try/Finally still unwinds. Failed mutations leave values unchanged.
- Aliases and ByVal arguments share the collection. Copy constructors and snapshots duplicate the outer container only. Indexed ByRef and compound assignment evaluate the receiver/key once; replacing the variable cannot redirect the captured write.
- These collections hold local script data; their methods do not move game items or access the network. A stack stored as one element still occupies one list position.

## Examples

### Build and sum a list

```vb
# Build and sum a list
#
# List() creates an ordered, resizable collection. Use its returned object through a variable;
# items.Add is an object method, not a global List.Add command.
#
# The factory returns an Object:List. Item/index reads return the stored value. Count is item
# count; IndexOf is a zero-based position or -1. Contains/Remove return 1=TRUE or 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear return Unit. ToArray returns a new Array.

Option Explicit On
Sub Main()
    # Add creates [3,7]; Insert(1,5) makes [3,5,7]; Set(0,2) makes [2,5,7]. For Each sums all three
    # values. Main returns Integer 14.

    Var items = List()
    items.Add(3)
    items.Add(7)
    items.Insert(1, 5)
    items.Set(0, 2)
    Var total = 0
    For Each item In items
        total += item
    Next
    Return total
End Sub
```

**Parameter and execution notes:**

- Add creates [3,7]; Insert(1,5) makes [3,5,7]; Set(0,2) makes [2,5,7]. For Each sums all three values. Main returns Integer 14.

### Independent copies and snapshots

```vb
# Independent copies and snapshots
#
# List() creates an ordered, resizable collection. Use its returned object through a variable;
# items.Add is an object method, not a global List.Add command.
#
# The factory returns an Object:List. Item/index reads return the stored value. Count is item
# count; IndexOf is a zero-based position or -1. Contains/Remove return 1=TRUE or 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear return Unit. ToArray returns a new Array.

Option Explicit On
Sub Main()
    # seed=[4,6]. copied and snapshot retain those values. The original list changes to [9,6];
    # Remove(6) returns TRUE=1, RemoveAt(0) empties it, and Clear remains empty. Main returns
    # 4*100+6*10+1+0, Integer 461.

    Dim seed[1]
    seed[0] = 4
    seed[1] = 6
    Var items = List(seed)
    Var copied = List(items)
    Var snapshot = items.ToArray()
    items[0] = 9
    Var removed = items.Remove(6)
    items.RemoveAt(0)
    items.Clear()
    Return snapshot[0]*100 + copied[1]*10 + removed + items.Count()
End Sub
```

**Parameter and execution notes:**

- seed=[4,6]. copied and snapshot retain those values. The original list changes to [9,6]; Remove(6) returns TRUE=1, RemoveAt(0) empties it, and Clear remains empty. Main returns 4*100+6*10+1+0, Integer 461.

### Search and modify through ByRef

```vb
# Search and modify through ByRef
#
# List() creates an ordered, resizable collection. Use its returned object through a variable;
# items.Add is an object method, not a global List.Add command.
#
# The factory returns an Object:List. Item/index reads return the stored value. Count is item
# count; IndexOf is a zero-based position or -1. Contains/Remove return 1=TRUE or 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear return Unit. ToArray returns a new Array.

Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    # NextIndex runs once, increments calls to 1 and returns 0. Bump changes the stored 5 to 6.
    # Contains(6)=TRUE; IndexOf(6)=0. Item(0) returns 6. Main returns Integer 601.

    Var items = List()
    items.Add(5)
    Var calls = 0
    Bump(items[NextIndex(calls)])
    If items.Contains(6) AndAlso items.IndexOf(6) = 0 Then
        Return items.Item(0)*100 + calls
    End If
    Return -1
End Sub
```

**Parameter and execution notes:**

- NextIndex runs once, increments calls to 1 and returns 0. Bump changes the stored 5 to 6. Contains(6)=TRUE; IndexOf(6)=0. Item(0) returns 6. Main returns Integer 601.
