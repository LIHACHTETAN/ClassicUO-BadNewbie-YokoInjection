# UO.FindCount

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Counts search objects, or reads the amount in one stack by its ID.

## Exact syntax

```text
UO.FindCount() -> Integer
UO.FindCount(id:Any) -> Integer
```

## Parameters

- `id` — Optional only for FindCount. Serial of one item: Integer, decimal/hexadecimal string, lasttarget, lastobject, backpack or a name assigned with AddObject. Pass an ID, not a graphic/type. Unknown names return 0; self resolves the character and therefore gives 0 here. With no argument, read the search object count instead.

## Returns

Integer — FindCount() returns the number of found objects: one stack counts as one item. FindCount(id) returns the current Amount of that item’s stack; unavailable/deleted IDs and mobiles return 0. A nonstackable item normally has Amount=1. Neither form returns an ID, type or Boolean.

## Behavior

- The regular FindType forms with 1–5 arguments, FindTypeEx and Count/CountEx/CountGround replace this script’s search results. A search with no matches clears the snapshot. Save any value needed after another search.
- These calls do not start a search, open containers, move items or send packets. They use data already loaded by the client. FindCount(id) needs no prior search and does not change its results.
- FindItem/FindCount()/FindFullQuantity are search snapshots. FindQuantity and FindCount(id) read the current object amount; an item may change or disappear after the search.

## Examples

### Read a gold search

```vb
# Read a gold search
#
# Counts search objects, or reads the amount in one stack by its ID.
#
# Integer — FindCount() returns the number of found objects: one stack counts as one item.
# FindCount(id) returns the current Amount of that item’s stack; unavailable/deleted IDs and
# mobiles return 0. A nonstackable item normally has Amount=1. Neither form returns an ID, type
# or Boolean.

SUB Main()
    # type=0x0EED is gold; color=-1 allows any hue; backpack selects direct contents in this
    # FindType form. value stores the chosen command’s result, and STR displays it.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindCount()
    UO.Print(STR(value))
END SUB
```

**Parameter and execution notes:**

- type=0x0EED is gold; color=-1 allows any hue; backpack selects direct contents in this FindType form. value stores the chosen command’s result, and STR displays it.

### Compare objects, one stack and all units

```vb
# Compare objects, one stack and all units
#
# Counts search objects, or reads the amount in one stack by its ID.
#
# Integer — FindCount() returns the number of found objects: one stack counts as one item.
# FindCount(id) returns the current Amount of that item’s stack; unavailable/deleted IDs and
# mobiles return 0. A nonstackable item normally has Amount=1. Neither form returns an ID, type
# or Boolean.

SUB Main()
    # The four readings follow the same search. With two stacks of 50: object count=2, first
    # stack=50, total=100. FindItem is the unique ID of the first stack, not its type.

    UO.FindType(0x0EED, -1, 'backpack')
    UO.Print(STR(UO.FindCount()))
    UO.Print(STR(UO.FindQuantity()))
    UO.Print(STR(UO.FindFullQuantity()))
    UO.Print('0x' + Hex(UO.FindItem()))
END SUB
```

**Parameter and execution notes:**

- The four readings follow the same search. With two stacks of 50: object count=2, first stack=50, total=100. FindItem is the unique ID of the first stack, not its type.

### Keep a result before another search

```vb
# Keep a result before another search
#
# Counts search objects, or reads the amount in one stack by its ID.
#
# Integer — FindCount() returns the number of found objects: one stack counts as one item.
# FindCount(id) returns the current Amount of that item’s stack; unavailable/deleted IDs and
# mobiles return 0. A nonstackable item normally has Amount=1. Neither form returns an ID, type
# or Boolean.

SUB Main()
    # The first type is gold; 0x0F7A selects a different reagent type. The second FindType replaces
    # the snapshot. saved retains the earlier value; the final reading uses the new result.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindCount()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindCount()))
END SUB
```

**Parameter and execution notes:**

- The first type is gold; 0x0F7A selects a different reagent type. The second FindType replaces the snapshot. saved retains the earlier value; the final reading uses the new result.

### Read an item directly by ID

```vb
# Read an item directly by ID
#
# Counts search objects, or reads the amount in one stack by its ID.
#
# Integer — FindCount() returns the number of found objects: one stack counts as one item.
# FindCount(id) returns the current Amount of that item’s stack; unavailable/deleted IDs and
# mobiles return 0. A nonstackable item normally has Amount=1. Neither form returns an ID, type
# or Boolean.

SUB Main()
    # lasttarget must refer to an item already selected in the game. No new target cursor appears.
    # FindCount(id) reads that item’s current stack, returning 0 when unavailable; it leaves the
    # search snapshot intact.

    VAR id = lasttarget
    VAR amount = UO.FindCount(id)
    UO.Print(STR(amount))
END SUB
```

**Parameter and execution notes:**

- lasttarget must refer to an item already selected in the game. No new target cursor appears. FindCount(id) reads that item’s current stack, returning 0 when unavailable; it leaves the search snapshot intact.
