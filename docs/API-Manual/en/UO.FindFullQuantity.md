# UO.FindFullQuantity

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the total units captured by the latest search.

## Exact syntax

```text
UO.FindFullQuantity() -> Any
```

## Parameters

No parameters.

## Returns

Integer — sum of max(1, Amount) for the found items, plus 1 for each found mobile. No results: 0. Two stacks of 50 give 100, while FindCount() gives 2. This total is a snapshot taken during the search.

## Behavior

- The regular FindType forms with 1–5 arguments, FindTypeEx and Count/CountEx/CountGround replace this script’s search results. A search with no matches clears the snapshot. Save any value needed after another search.
- These calls do not start a search, open containers, move items or send packets. They use data already loaded by the client. FindCount(id) needs no prior search and does not change its results.
- FindItem/FindCount()/FindFullQuantity are search snapshots. FindQuantity and FindCount(id) read the current object amount; an item may change or disappear after the search.

## Examples

### Read a gold search

```vb
# Read a gold search
#
# Reads the total units captured by the latest search.
#
# Integer — sum of max(1, Amount) for the found items, plus 1 for each found mobile. No results:
# 0. Two stacks of 50 give 100, while FindCount() gives 2. This total is a snapshot taken during
# the search.

SUB Main()
    # type=0x0EED is gold; color=-1 allows any hue; backpack selects direct contents in this
    # FindType form. value stores the chosen command’s result, and STR displays it.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindFullQuantity()
    UO.Print(STR(value))
END SUB
```

**Parameter and execution notes:**

- type=0x0EED is gold; color=-1 allows any hue; backpack selects direct contents in this FindType form. value stores the chosen command’s result, and STR displays it.

### Compare objects, one stack and all units

```vb
# Compare objects, one stack and all units
#
# Reads the total units captured by the latest search.
#
# Integer — sum of max(1, Amount) for the found items, plus 1 for each found mobile. No results:
# 0. Two stacks of 50 give 100, while FindCount() gives 2. This total is a snapshot taken during
# the search.

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
# Reads the total units captured by the latest search.
#
# Integer — sum of max(1, Amount) for the found items, plus 1 for each found mobile. No results:
# 0. Two stacks of 50 give 100, while FindCount() gives 2. This total is a snapshot taken during
# the search.

SUB Main()
    # The first type is gold; 0x0F7A selects a different reagent type. The second FindType replaces
    # the snapshot. saved retains the earlier value; the final reading uses the new result.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindFullQuantity()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindFullQuantity()))
END SUB
```

**Parameter and execution notes:**

- The first type is gold; 0x0F7A selects a different reagent type. The second FindType replaces the snapshot. saved retains the earlier value; the final reading uses the new result.
