# UO.LastTarget

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the serial of the last saved object target.

## Exact syntax

```text
UO.LastTarget() -> Integer
```

## Parameters

No parameters.

## Returns

Integer — serial/ID, not a type or Boolean. 0 means no object target; land/static targets also have serial 0 although coordinates may be retained. All 32 bits are preserved. Test a nonzero ID with <> 0, not > 0 or = TRUE.

## Behavior

- No parameters. Does not open a cursor, select a new target, attack or send packets. LastTarget differs from LastAttack and LastStatus. An ordinary self selection does not replace the last target; explicit ClientMarkChar may change it.
- SetEntity saves known Entity.X/Y; an item in a container may have content coordinates. SetLand/SetStatic save the selected world X/Y. Later object movement/removal does not change retained coordinates. Use GetX/GetY(serial) for its current position.
- Clear and World.Clear reset the record, including cleanup that preserves scripts. An explicitly assigned unknown serial does not inherit previous X/Y: they become 0. This does not guarantee a target exists on the server.
- Reading serial and X/Y in separate calls is not atomic. For object targets LastTile retains protocol X/Y=65535, not the object’s saved position. For land/statics LastTile(1)/(2) read selected X/Y. Bare lasttarget is a live intrinsic unless a variable shadows it.
- World.Clear calls ClearWorldState: it resets the active cursor/callback, clears the saved target and repeat-last packet. A normal Reset retains history. Native TargetLast only sends a recorded target for an active server cursor; without history or for a local callback it leaves the cursor unchanged and sends nothing. An active client callback receives null once as cancellation, so ClientTargetResponsePresent becomes 1 with an empty response. An already completed selection is not notified again.

### Internal functions: from call to result

These are actual internal C# stages. ReadTargetValue is a fully defined helper in the example, not an undocumented built-in command.

#### 1. SetEntity

SetEntity saves the serial and separately copies X/Y from World.Get(serial). Missing/destroyed Entity yields coordinates 0. Protocol target fields keep their existing sentinels.

SetEntity saves known Entity.X/Y; an item in a container may have content coordinates. SetLand/SetStatic save the selected world X/Y. Later object movement/removal does not change retained coordinates. Use GetX/GetY(serial) for its current position.

Project source: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; function `SetEntity`.

#### 2. SetLand

SetLand and SetStatic save X/Y/Z with serial 0. SavedX/SavedY are separate from protocol fields to preserve target transmission.

Integer — serial/ID, not a type or Boolean. 0 means no object target; land/static targets also have serial 0 although coordinates may be retained. All 32 bits are preserved. Test a nonzero ID with <> 0, not > 0 or = TRUE.

Project source: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; function `SetLand`.

#### 3. SetStatic

SetLand and SetStatic save X/Y/Z with serial 0. SavedX/SavedY are separate from protocol fields to preserve target transmission.

Integer — serial/ID, not a type or Boolean. 0 means no object target; land/static targets also have serial 0 although coordinates may be retained. All 32 bits are preserved. Test a nonzero ID with <> 0, not > 0 or = TRUE.

Project source: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; function `SetStatic`.

#### 4. ExecuteStealthCompatibility

The command reads the bridge; LastTargetX/LastTargetY use ITargetSnapshotBridge. Older external bridges without it keep GetX/GetY lookups. Invoke reads on the game thread with cancellation support.

Integer — serial/ID, not a type or Boolean. 0 means no object target; land/static targets also have serial 0 although coordinates may be retained. All 32 bits are preserved. Test a nonzero ID with <> 0, not > 0 or = TRUE.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 5. Invoke

The command reads the bridge; LastTargetX/LastTargetY use ITargetSnapshotBridge. Older external bridges without it keep GetX/GetY lookups. Invoke reads on the game thread with cancellation support.

No parameters. Does not open a cursor, select a new target, attack or send packets. LastTarget differs from LastAttack and LastStatus. An ordinary self selection does not replace the last target; explicit ClientMarkChar may change it.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 6. Clear

Clear resets serial and retained coordinates. World.Clear calls it when cleaning the world.

Clear and World.Clear reset the record, including cleanup that preserves scripts. An explicitly assigned unknown serial does not inherit previous X/Y: they become 0. This does not guarantee a target exists on the server.

Project source: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; function `Clear`.

#### 7. ClearWorldState

World.Clear calls ClearWorldState: it resets the active cursor/callback, clears the saved target and repeat-last packet. A normal Reset retains history. Native TargetLast only sends a recorded target for an active server cursor; without history or for a local callback it leaves the cursor unchanged and sends nothing. An active client callback receives null once as cancellation, so ClientTargetResponsePresent becomes 1 with an empty response. An already completed selection is not notified again.

World.Clear calls ClearWorldState: it resets the active cursor/callback, clears the saved target and repeat-last packet. A normal Reset retains history. Native TargetLast only sends a recorded target for an active server cursor; without history or for a local callback it leaves the cursor unchanged and sends nothing. An active client callback receives null once as cancellation, so ClientTargetResponsePresent becomes 1 with an empty response. An already completed selection is not notified again.

Project source: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; function `ClearWorldState`.

#### 8. TargetLast

World.Clear calls ClearWorldState: it resets the active cursor/callback, clears the saved target and repeat-last packet. A normal Reset retains history. Native TargetLast only sends a recorded target for an active server cursor; without history or for a local callback it leaves the cursor unchanged and sends nothing. An active client callback receives null once as cancellation, so ClientTargetResponsePresent becomes 1 with an empty response. An already completed selection is not notified again.

World.Clear calls ClearWorldState: it resets the active cursor/callback, clears the saved target and repeat-last packet. A normal Reset retains history. Native TargetLast only sends a recorded target for an active server cursor; without history or for a local callback it leaves the cursor unchanged and sends nothing. An active client callback receives null once as cancellation, so ClientTargetResponsePresent becomes 1 with an empty response. An already completed selection is not notified again.

Project source: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; function `TargetLast`.

Reading serial and X/Y in separate calls is not atomic. For object targets LastTile retains protocol X/Y=65535, not the object’s saved position. For land/statics LastTile(1)/(2) read selected X/Y. Bare lasttarget is a live intrinsic unless a variable shadows it.


## Examples

### Read a saved value

```vb
# Read a saved value
#
# Reads the serial of the last saved object target.
#
# Integer — serial/ID, not a type or Boolean. 0 means no object target; land/static targets also
# have serial 0 although coordinates may be retained. All 32 bits are preserved. Test a nonzero
# ID with <> 0, not > 0 or = TRUE.

SUB Main()
    # value holds the single return value; HEX displays an ID and CStr a coordinate. The call
    # selects nothing.

    VAR value = UO.LastTarget()
    UO.Print('Saved value: ' + HEX(value))
END SUB
```

**Parameter and execution notes:**

- value holds the single return value; HEX displays an ID and CStr a coordinate. The call selects nothing.

### Compare saved and live position

```vb
# Compare saved and live position
#
# Reads the serial of the last saved object target.
#
# Integer — serial/ID, not a type or Boolean. 0 means no object target; land/static targets also
# have serial 0 although coordinates may be retained. All 32 bits are preserved. Test a nonzero
# ID with <> 0, not > 0 or = TRUE.

SUB Main()
    # id is the retained serial. Exists checks the object before GetX/GetY. Saved and live
    # coordinates may differ. With serial=0 the example prints the selected point, but 0 alone does
    # not prove any point was selected.

    VAR id = UO.LastTarget()
    VAR x = UO.LastTargetX()
    VAR y = UO.LastTargetY()
    UO.Print('Saved XY: ' + CStr(x) + ',' + CStr(y))
    IF id <> 0 AND UO.Exists(id) THEN
        UO.Print('Live XY: ' + CStr(UO.GetX(id)) + ',' + CStr(UO.GetY(id)))
    END IF
END SUB
```

**Parameter and execution notes:**

- id is the retained serial. Exists checks the object before GetX/GetY. Saved and live coordinates may differ. With serial=0 the example prints the selected point, but 0 alone does not prove any point was selected.

### Complete ReadTargetValue helper

```vb
# Complete ReadTargetValue helper
#
# Reads the serial of the last saved object target.
#
# Integer — serial/ID, not a type or Boolean. 0 means no object target; land/static targets also
# have serial 0 although coordinates may be retained. All 32 bits are preserved. Test a nonzero
# ID with <> 0, not > 0 or = TRUE.

SUB Main()
    # minimum/maximum configure the helper’s acceptable result range, not API parameters. The helper
    # is fully defined; -1 is its own out-of-range signal. For IDs, the alternative check preserves
    # every nonzero serial, including the high bit.

    VAR value = ReadTargetValue()
    UO.Print('Checked value: ' + CStr(value))
END SUB

SUB ReadTargetValue()
    VAR value = UO.LastTarget()
    IF value = 0 THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Parameter and execution notes:**

- minimum/maximum configure the helper’s acceptable result range, not API parameters. The helper is fully defined; -1 is its own out-of-range signal. For IDs, the alternative check preserves every nonzero serial, including the high bit.
