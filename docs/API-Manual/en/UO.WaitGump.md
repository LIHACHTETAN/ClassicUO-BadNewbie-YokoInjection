# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Registers an ordered sequence of one-time button replies. Execution continues immediately; an absent window does not block the script for 30 seconds.

## Exact syntax

```text
UO.WaitGump(Value:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any, trigger16:Any) -> Unit
UO.WaitGump(triggerId:Integer) -> Unit
UO.WaitGump(triggerId:String) -> Unit
```

## Parameters

- `triggerId` — Integer ButtonID or numeric String. One string may contain a | or comma-separated sequence. Forms with 2..16 arguments accept a sequence, including arrays and nested sequences. All IDs are parsed before registration. An empty sequence, over 256 pending buttons in the client, or nesting beyond 32 levels raises an error without partial registration.
- `Value` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger1` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger2` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger3` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger4` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger5` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger6` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger7` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger8` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger9` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger10` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger11` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger12` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger13` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger14` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger15` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.
- `trigger16` — Sequence element: Integer ButtonID, numeric String, a |/comma-separated string, or an Array of these elements. Processed left to right under the triggerId bounds and rules. Value names the single Any parameter, which also accepts an array.

## Returns

Unit — no return value: neither success, the new value nor server acknowledgement.

## Behavior

- Requires an actual Activate button with the requested ButtonID; page switches and unrelated windows are skipped. Later IDs cannot bypass the first pending ID. At most one reply is made to each window per layout delivery. A rebuilt layout may reuse the same window object.
- Another WaitGump in the same script appends to its pending sequence. Search is not restricted by GumpID: use NumGumpButton or SendGumpSelect for precise selection. ButtonID=0 requires an actual Activate button with ID 0; it is not universal close.
- Normal procedure completion preserves pending actions. Owner cancellation or Terminate with its name removes its actions; TerminateAll clears every action, including those left by completed procedures. Changing worlds clears the queue. Actions are not saved in profiles.

## Examples

### One reply

```vb
# One reply
#
# Registers an ordered sequence of one-time button replies. Execution continues immediately; an
# absent window does not block the script for 30 seconds.
#
# Unit — no return value: neither success, the new value nor server acknowledgement.

SUB Main()
    # 100 is the reply ButtonID. WaitGump registers it before UseObject; continued script execution
    # does not mean that the server has acknowledged the reply.

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Parameter and execution notes:**

- 100 is the reply ButtonID. WaitGump registers it before UseObject; continued script execution does not mean that the server has acknowledged the reply.

### Multiple stages

```vb
# Multiple stages
#
# Registers an ordered sequence of one-time button replies. Execution continues immediately; an
# absent window does not block the script for 30 seconds.
#
# Unit — no return value: neither success, the new value nor server acknowledgement.

SUB Main()
    # 7, 22 and 1 are ButtonIDs of successive forms, checked in that order. The argument count does
    # not specify a delay; the call registers the complete sequence.

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**Parameter and execution notes:**

- 7, 22 and 1 are ButtonIDs of successive forms, checked in that order. The argument count does not specify a delay; the call registers the complete sequence.

### Cancel pending actions

```vb
# Cancel pending actions
#
# Registers an ordered sequence of one-time button replies. Execution continues immediately; an
# absent window does not block the script for 30 seconds.
#
# Unit — no return value: neither success, the new value nor server acknowledgement.

SUB Main()
    # The string 7|22|1 defines the same sequence. TerminateAll then clears every pending gump
    # action and stops every procedure; its effect is global.

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**Parameter and execution notes:**

- The string 7|22|1 defines the same sequence. TerminateAll then clears every pending gump action and stops every procedure; its effect is global.
