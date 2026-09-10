# UO.GumpAutoTextEntry

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Sets a control once in the first matching server gump; if the control is absent, keeps a pending action.

## Exact syntax

```text
UO.GumpAutoTextEntry(TextEntryID:Any, Value:Any) -> Unit
```

## Parameters

- `TextEntryID` — Integer — exact ID of the corresponding control type. Not an index, GumpID or window serial. 0 is an ordinary ID and never means the first control.
- `Value` — String — field text; an empty string clears it. The field retains its length and character restrictions.

## Returns

Unit — no return value: neither success, the new value nor server acknowledgement.

## Behavior

- Checks existing windows in current UI order, then incoming or rebuilt server layouts. Consumed once by the first matching type and ID. Use indexed NumGump* for a specific window.
- Pending fields are applied before automatic button replies. Repeating a type and ID in the same script replaces its unconsumed value. The client allows 1024 pending fields; exceeding this limit raises a script error.
- Normal procedure completion preserves pending actions. Owner cancellation or Terminate with its name removes its actions; TerminateAll clears every action, including those left by completed procedures. Changing worlds clears the queue. Actions are not saved in profiles.
- A restricted field can truncate or reject text; finding the control still consumes the action. This command sends no button reply and does not wait for the server. Inspect GetGumpInfo/NumGumpTextEntry to verify the text.

## Examples

### Fill an existing control

```vb
# Fill an existing control
#
# Sets a control once in the first matching server gump; if the control is absent, keeps a
# pending action.
#
# Unit — no return value: neither success, the new value nor server acknowledgement.

SUB Main()
    # The first argument, 33, is an example control ID: replace it with the actual ID from InfoGump.
    # The second argument is the assigned value. An absent control leaves a pending action.

    UO.GumpAutoTextEntry(33, '500')
END SUB
```

**Parameter and execution notes:**

- The first argument, 33, is an example control ID: replace it with the actual ID from InfoGump. The second argument is the assigned value. An absent control leaves a pending action.

### Fill before opening

```vb
# Fill before opening
#
# Sets a control once in the first matching server gump; if the control is absent, keeps a
# pending action.
#
# Unit — no return value: neither success, the new value nor server acknowledgement.

SUB Main()
    # 33 is the control ID, 100 an example confirmation ButtonID, and 0x40001234 the serial of the
    # object that opens the form. Replace all three. The field is filled before the reply even if
    # the window arrives later.

    UO.GumpAutoTextEntry(33, '500')
    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Parameter and execution notes:**

- 33 is the control ID, 100 an example confirmation ButtonID, and 0x40001234 the serial of the object that opens the form. Replace all three. The field is filled before the reply even if the window arrives later.

### Replace a pending value

```vb
# Replace a pending value
#
# Sets a control once in the first matching server gump; if the control is absent, keeps a
# pending action.
#
# Unit — no return value: neither success, the new value nor server acknowledgement.

SUB Main()
    # Both calls use ID 33. If the control has not arrived, the last value wins. If already open,
    # both changes happen immediately in call order.

    UO.GumpAutoTextEntry(33, '500')
    UO.GumpAutoTextEntry(33, '')
END SUB
```

**Parameter and execution notes:**

- Both calls use ID 33. If the control has not arrived, the last value wins. If already open, both changes happen immediately in call order.
