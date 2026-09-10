# Dictionary

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Dictionary() creates a key/value collection. Use methods on the returned object. Numeric and textual keys are distinct; "ore" and "Ore" are different keys.

## Exact syntax

```text
Dictionary() -> Object:Dictionary
Dictionary(source:Dictionary) -> Object:Dictionary
values.Add(key:String/Number, value:Any) -> Unit
values.Item(key:String/Number) -> Any
values[key] = value
values.Set(key:String/Number, value:Any) -> Unit
values.Get(key:String/Number, fallback:Any) -> Any
values.Count() -> Integer
values.ContainsKey(key:String/Number) -> Integer:1/0
values.Remove(key:String/Number) -> Integer:1/0
values.Clear() -> Unit
values.Keys() -> Array
values.Values() -> Array
entry.Key() -> String/Number
entry.Value() -> Any
```

## Parameters

- `source` — source: omitted means empty; List accepts an array or List, Dictionary accepts a Dictionary. Copying creates independent containers with shared nested object/array references.
- `index / key` — index / key: List positions are numeric whole numbers, starting at 0; Insert also accepts Count(). Dictionary accepts text or finite numbers. Numeric 1 and 1.0 denote one key; text "1" is different.
- `value` — value: an initialized Basic value, including nested arrays/collections. Unit cannot be stored. Equality compares numeric values, case-sensitive text, or array/object identity.
- `fallback` — fallback: Get returns this value for an absent key without inserting it. Arguments, including fallback expressions, evaluate before the method call.

## Returns

The factory returns an Object:Dictionary. Item/index/Get return a value; Count returns key count. ContainsKey/Remove return 1=TRUE or 0=FALSE. Add/Set/Clear return Unit. Keys/Values return new Arrays. For Each yields entries: Key() returns the key; Value() returns its stored value.

## Behavior

- Add rejects an existing key without overwriting it. Set/index assignment creates or replaces a key. Item/index requires an existing key; Get provides a fallback. Remove returns 0 when absent; Clear empties the dictionary.
- NaN, infinity, arrays, objects and Unit are invalid keys. Key order is unspecified. Each iterator entry preserves its own key/value pair; retaining an entry does not make it follow later entries.
- Keys/Values return shallow snapshots. Iterate Keys() to remove or replace dictionary entries; For Each over the dictionary itself yields entry objects.
- Changing a collection during its direct For Each enumeration, including Set, raises a catchable error on the next step. Try/Finally still unwinds. Failed mutations leave values unchanged.
- Aliases and ByVal arguments share the collection. Copy constructors and snapshots duplicate the outer container only. Indexed ByRef and compound assignment evaluate the receiver/key once; replacing the variable cannot redirect the captured write.
- These collections hold local script data; their methods do not move game items or access the network. A stack stored as one element still occupies one list position.

## Examples

### 1. Key types and fallback

```vb
# "ore" changes from 5 to 8. Numeric key 1 stores 2; text key "1" stores 3. Get("wood",7) returns fallback 7 without adding a key. Main returns 8*100+2*10+3+7, Integer 830.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**Parameter and execution notes:**

"ore" changes from 5 to 8. Numeric key 1 stores 2; text key "1" stores 3. Get("wood",7) returns fallback 7 without adding a key. Main returns 8*100+2*10+3+7, Integer 830.

### 2. Entries, snapshots and deletion

```vb
# The two entry values sum to 5. Keys() snapshots permit removal while iterating. copied retains ore=2 and snapshot retains two values. Clear leaves Count()=0. Main returns 5*100+2*10+2+0, Integer 522.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 2)
    values.Add("wood", 3)
    Var copied = Dictionary(values)
    Var snapshot = values.Values()
    Var total = 0
    For Each entry In values
        If values.ContainsKey(entry.Key()) Then
            total += entry.Value()
        End If
    Next
    For Each key In values.Keys()
        values.Remove(key)
    Next
    values.Clear()
    Return total*100 + copied["ore"]*10 + GetArrayLength(snapshot) + values.Count()
End Sub
```

**Parameter and execution notes:**

The two entry values sum to 5. Keys() snapshots permit removal while iterating. copied retains ore=2 and snapshot retains two values. Clear leaves Count()=0. Main returns 5*100+2*10+2+0, Integer 522.

### 3. Duplicate-key recovery

```vb
# The first Add stores ore=4. The second Add with value 7 raises an error; Catch sets caught=1. The original ore=4 is retained. Main returns 4*10+1, Integer 41.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 4)
    Var caught = 0
    Try
        values.Add("ore", 7)
    Catch problem
        caught = 1
    End Try
    Return values["ore"]*10 + caught
End Sub
```

**Parameter and execution notes:**

The first Add stores ore=4. The second Add with value 7 raises an error; Catch sets caught=1. The original ore=4 is retained. Main returns 4*10+1, Integer 41.

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/DictionaryObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-8.0
-->
