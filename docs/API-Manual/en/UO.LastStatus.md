# UO.LastStatus

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Returns the serial of the last object whose status the client accepted.

## Exact syntax

```text
UO.LastStatus() -> Integer
```

## Parameters

No parameters.

## Returns

Integer — the 32 serial bits, not a type or Boolean. 0 means no accepted status yet or the world was cleared. The high bit is retained, so a negative integer can also represent a serial. Test <> 0, not > 0 or = TRUE.

## Behavior

- No parameters. Reading sends no packets, opens no window and waits for no response. UO.GetStatus(id), RequestStats and UpdateObject request data; sending a request does not change LastStatus.
- An accepted 0x11 packet saves serial and the locally known X/Y together in World, shared by scripts. Unknown/destroyed subjects and incomplete basic packets do not replace the record. Later packets for other objects may replace it.
- X/Y capture Entity at reception, not its live position. For a mobile these are world cells; an item inside a container may have container-content coordinates. The status packet itself contains no X/Y. Later movement/removal does not change the snapshot; World.Clear resets it. Use GetX/GetY for a present object’s current coordinates.
- Separate calls are not an atomic snapshot; a server update may occur between them. An equal serial does not prove a fresh response to your request. Bare laststatus is a live intrinsic unless shadowed by a script variable; UO.LastStatus() is the registered function.

### Internal functions: from call to result

These are actual internal C# stages. ReadSavedStatus is a fully defined helper in the example, not an undocumented built-in command.

#### 1. CharacterStatus

CharacterStatus validates the basic payload and Entity through World.Get, updates status fields and stores serial/X/Y. Position comes from Entity, not status bytes.

Integer — the 32 serial bits, not a type or Boolean. 0 means no accepted status yet or the world was cleared. The high bit is retained, so a negative integer can also represent a serial. Test <> 0, not > 0 or = TRUE.

Project source: `src/ClassicUO.Client/Network/PacketHandlers.cs`; function `CharacterStatus`.

#### 2. ExecuteStealthCompatibility

ExecuteStealthCompatibility returns the bridge serial as Integer. LastStatusX/LastStatusY use IStatusSnapshotBridge for retained coordinates; an older external bridge without it keeps the legacy GetX/GetY lookup.

Integer — the 32 serial bits, not a type or Boolean. 0 means no accepted status yet or the world was cleared. The high bit is retained, so a negative integer can also represent a serial. Test <> 0, not > 0 or = TRUE.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 3. Invoke

Invoke reads World on the game thread with script cancellation support. It neither waits for a network response nor modifies status.

No parameters. Reading sends no packets, opens no window and waits for no response. UO.GetStatus(id), RequestStats and UpdateObject request data; sending a request does not change LastStatus.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 4. Clear

Clear resets serial and both coordinates to 0, including cleanup that preserves running scripts.

X/Y capture Entity at reception, not its live position. For a mobile these are world cells; an item inside a container may have container-content coordinates. The status packet itself contains no X/Y. Later movement/removal does not change the snapshot; World.Clear resets it. Use GetX/GetY for a present object’s current coordinates.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Clear`.

Separate calls are not an atomic snapshot; a server update may occur between them. An equal serial does not prove a fresh response to your request. Bare laststatus is a live intrinsic unless shadowed by a script variable; UO.LastStatus() is the registered function.


## Examples

### Read the last value

```vb
# Read the last value
#
# Returns the serial of the last object whose status the client accepted.
#
# Integer — the 32 serial bits, not a type or Boolean. 0 means no accepted status yet or the
# world was cleared. The high bit is retained, so a negative integer can also represent a
# serial. Test <> 0, not > 0 or = TRUE.

SUB Main()
    # Read once. HEX displays a serial in hexadecimal; CStr displays a coordinate as a number. The
    # call does not select an object.

    VAR value = UO.LastStatus()
    UO.Print('Saved value: ' + HEX(value))
END SUB
```

**Parameter and execution notes:**

- Read once. HEX displays a serial in hexadecimal; CStr displays a coordinate as a number. The call does not select an object.

### Request status and read known data

```vb
# Request status and read known data
#
# Returns the serial of the last object whose status the client accepted.
#
# Integer — the 32 serial bits, not a type or Boolean. 0 means no accepted status yet or the
# world was cleared. The high bit is retained, so a negative integer can also represent a
# serial. Test <> 0, not > 0 or = TRUE.

SUB Main()
    # subject is self’s serial. 500 is an example wait in milliseconds, not a response guarantee.
    # The displayed record may be old or belong to another object.

    VAR subject = UO.Self()
    IF subject <> 0 THEN
        UO.GetStatus(subject)
        WAIT(500)
        VAR value = UO.LastStatus()
        UO.Print('Known value: ' + HEX(value))
    END IF
END SUB
```

**Parameter and execution notes:**

- subject is self’s serial. 500 is an example wait in milliseconds, not a response guarantee. The displayed record may be old or belong to another object.

### Complete ReadSavedStatus helper

```vb
# Complete ReadSavedStatus helper
#
# Returns the serial of the last object whose status the client accepted.
#
# Integer — the 32 serial bits, not a type or Boolean. 0 means no accepted status yet or the
# world was cleared. The high bit is retained, so a negative integer can also represent a
# serial. Test <> 0, not > 0 or = TRUE.

SUB Main()
    # expectedId is the serial saved by Main. The helper is defined in full below; -1 means that
    # record is no longer selected and is not this command’s own return code. The before/after
    # checks reduce mixed-object reads but cannot guarantee atomicity for updates of the same
    # serial.

    VAR expectedId = UO.LastStatus()
    IF expectedId <> 0 THEN
        VAR value = ReadSavedStatus(expectedId)
        UO.Print('Checked value: ' + CStr(value))
    END IF
END SUB

SUB ReadSavedStatus(expectedId)
    IF expectedId = 0 OR UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    VAR value = UO.LastStatus()
    IF UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Parameter and execution notes:**

- expectedId is the serial saved by Main. The helper is defined in full below; -1 means that record is no longer selected and is not this command’s own return code. The before/after checks reduce mixed-object reads but cannot guarantee atomicity for updates of the same serial.
