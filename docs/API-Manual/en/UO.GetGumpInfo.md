# UO.GetGumpInfo

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads one consistent snapshot of a server gump and its controls.

## Exact syntax

```text
UO.GetGumpInfo(GumpIndex:Any) -> Array
```

## Parameters

- `GumpIndex` — Required Integer: zero-based index, from 0 to GetGumpsCount()-1. It is not a serial or GumpID. Negative/out-of-range indices are invalid. Opening, closing or reordering windows can change the index.

## Returns

Array with exactly five fields: [0] Integer serial; [1] Integer GumpID; [2] Array<String> nonblank texts; [3] Array<String> ordinary button descriptions; [4] Array<String> all live controls, including nested controls. An invalid, closed or ignored gump returns []. High-bit IDs appear as negative Integers; use Hex to display their bits.

## Behavior

- The entire snapshot is copied in one game-thread request. Later edits or closing the window do not change saved arrays. Only active server gumps are included; local backpack, map and settings windows are excluded.
- This BASIC array is not the Pascal TGumpInfo record or the original layout packet. Descriptions contain control type, page, ID, X/Y and dimensions. Buttons add ButtonID, action, toPage and graphics; switches add checked and inactive/active graphics. Text may contain spaces and equals signs. Radio buttons are in [4], not [3].
- AddGumpIgnoreByID/BySerial suppress this getter in the current script; ClearGumpsIgnore resets that filter. GetGumpsCount is unchanged. Empty text/control arrays can belong to an existing gump. Use GetArrayLength, not Len, for arrays.

## Examples

### Read both IDs

```vb
# Read both IDs
#
# Reads one consistent snapshot of a server gump and its controls.
#
# Array with exactly five fields: [0] Integer serial; [1] Integer GumpID; [2] Array<String>
# nonblank texts; [3] Array<String> ordinary button descriptions; [4] Array<String> all live
# controls, including nested controls. An invalid, closed or ignored gump returns []. High-bit
# IDs appear as negative Integers; use Hex to display their bits.

SUB Main()
    # 0 selects the first server gump. Check GetArrayLength(info)=5 before indexing. info[0] is the
    # serial and info[1] is the GumpID from the same snapshot.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        UO.Print('Serial=' + Hex(info[0]))
        UO.Print('GumpID=' + Hex(info[1]))
    END IF
END SUB
```

**Parameter and execution notes:**

- 0 selects the first server gump. Check GetArrayLength(info)=5 before indexing. info[0] is the serial and info[1] is the GumpID from the same snapshot.

### List the actual ButtonIDs

```vb
# List the actual ButtonIDs
#
# Reads one consistent snapshot of a server gump and its controls.
#
# Array with exactly five fields: [0] Integer serial; [1] Integer GumpID; [2] Array<String>
# nonblank texts; [3] Array<String> ordinary button descriptions; [4] Array<String> all live
# controls, including nested controls. An invalid, closed or ignored gump returns []. High-bit
# IDs appear as negative Integers; use Hex to display their bits.

SUB Main()
    # info[3] contains button descriptions. i is a string-array index; the ButtonID field in each
    # description is the ID to use for a reply. Radio buttons belong to the full control list.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR buttons = info[3]
        VAR i = 0
        WHILE i < GetArrayLength(buttons)
            UO.Print(buttons[i])
            i = i + 1
        WEND
    END IF
END SUB
```

**Parameter and execution notes:**

- info[3] contains button descriptions. i is a string-array index; the ButtonID field in each description is the ID to use for a reply. Radio buttons belong to the full control list.

### Keep text before closing

```vb
# Keep text before closing
#
# Reads one consistent snapshot of a server gump and its controls.
#
# Array with exactly five fields: [0] Integer serial; [1] Integer GumpID; [2] Array<String>
# nonblank texts; [3] Array<String> ordinary button descriptions; [4] Array<String> all live
# controls, including nested controls. An invalid, closed or ignored gump returns []. High-bit
# IDs appear as negative Integers; use Hex to display their bits.

SUB Main()
    # info[2] is a text copy. CloseSimpleGump(0) closes locally only when NoClose is absent and
    # returns no value. Saved texts remain valid; test their array length before reading texts[0].

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR texts = info[2]
        UO.CloseSimpleGump(0)
        IF GetArrayLength(texts) > 0 THEN
            UO.Print(texts[0])
        END IF
    END IF
END SUB
```

**Parameter and execution notes:**

- info[2] is a text copy. CloseSimpleGump(0) closes locally only when NoClose is absent and returns no value. Saved texts remain valid; test their array length before reading texts[0].
