# UO.GetArmor

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the current player’s resistance field: physical armor/resistance.

## Exact syntax

```text
UO.GetArmor() -> Integer
```

## Parameters

No parameters.

## Returns

Integer — the signed status value, -32768..32767 in the client model. Negative values are preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player; GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or a resistance cap. A value of 1 means one point, not confirmation of success.

## Behavior

- This command takes no arguments. Use the exact signatures shown above.
- The game-thread read takes Player.PhysicalResistance if the current Player exists and is not destroyed; otherwise 0. It does not search equipment, recompute bonuses, request status or wait for an update. A present ghost is not the same as a destroyed Player.
- PhysicalResistance is the server’s armor/status field: classic shards can use an armor rating, while resistance-based rules use physical resistance. The API does not translate between rulesets or calculate a damage-reduction percentage. Armor and physical aliases read the same field.
- CharacterStatus validates the fixed body before changing name, health or own status fields, then converts each resistance word to signed Int16. A truncated fixed body leaves the prior state intact. Optional type-6 trailer fields retain their existing fallback; these resistance commands do not read that trailer’s maximum-resistance fields.
- Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.
- RegisterCharacterGetterAliases adds missing zero-argument functions and intrinsic names for this field. Existing compatibility branches read the same bridge field. Names ignore letter case; an intrinsic without parentheses is reread unless a script variable shadows it.

### Internal functions: from call to result

Actual native stages of a local resistance read. ResistanceAtLeast below is a fully defined user BASIC helper, not a hidden built-in function or a command that equips protective items.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases adds missing zero-argument functions and intrinsic names for this field. Existing compatibility branches read the same bridge field. Names ignore letter case; an intrinsic without parentheses is reread unless a script variable shadows it.

`Armor PhysicalResist ResistPhysical GetArmor GetPhysicalResist GetResistPhysical`.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `RegisterCharacterGetterAliases`.

#### 2. Invoke

The game-thread read takes Player.PhysicalResistance if the current Player exists and is not destroyed; otherwise 0. It does not search equipment, recompute bonuses, request status or wait for an update. A present ghost is not the same as a destroyed Player.

Invoke reads on the game thread and honours script cancellation while waiting. No status request, target, network packet, attribute change or built-in delay is issued.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 3. CharacterStatus

CharacterStatus validates the fixed body before changing name, health or own status fields, then converts each resistance word to signed Int16. A truncated fixed body leaves the prior state intact. Optional type-6 trailer fields retain their existing fallback; these resistance commands do not read that trailer’s maximum-resistance fields.

PhysicalResistance is the server’s armor/status field: classic shards can use an armor rating, while resistance-based rules use physical resistance. The API does not translate between rulesets or calculate a damage-reduction percentage. Armor and physical aliases read the same field.

Project source: `src/ClassicUO.Client/Network/PacketHandlers.cs`; function `CharacterStatus`.

#### 4. Clear

World.Clear removes Player. Later reads return 0 until a current player and its status are available; never keep a saved stat as proof that a reconnected character meets a requirement.

Integer — the signed status value, -32768..32767 in the client model. Negative values are preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player; GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or a resistance cap. A value of 1 means one point, not confirmation of success.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Clear`.

Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.


## Examples

### Display the cached value

```vb
# Display the cached value
#
# Reads the current player’s resistance field: physical armor/resistance.
#
# Integer — the signed status value, -32768..32767 in the client model. Negative values are
# preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player;
# GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or
# a resistance cap. A value of 1 means one point, not confirmation of success.

SUB Main()
    # value stores one query. CStr formats it for the journal. No parameter is supplied; this reads
    # the current player.

    VAR value = UO.GetArmor()
    UO.Print('PhysicalResistance: ' + CStr(value))
END SUB
```

**Parameter and execution notes:**

- value stores one query. CStr formats it for the journal. No parameter is supplied; this reads the current player.

### Compare two observations

```vb
# Compare two observations
#
# Reads the current player’s resistance field: physical armor/resistance.
#
# Integer — the signed status value, -32768..32767 in the client model. Negative values are
# preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player;
# GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or
# a resistance cap. A value of 1 means one point, not confirmation of success.

SUB Main()
    # before and after are separated by WAIT(500) milliseconds; difference can be negative.
    # Intermediate updates can be missed. The wait is part of the example, not an API delay.

    VAR before = UO.GetArmor()
    WAIT(500)
    VAR after = UO.GetArmor()
    VAR difference = after - before
    UO.Print('Resistance change: ' + CStr(difference))
END SUB
```

**Parameter and execution notes:**

- before and after are separated by WAIT(500) milliseconds; difference can be negative. Intermediate updates can be missed. The wait is part of the example, not an API delay.

### Complete minimum-resistance helper

```vb
# Complete minimum-resistance helper
#
# Reads the current player’s resistance field: physical armor/resistance.
#
# Integer — the signed status value, -32768..32767 in the client model. Negative values are
# preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player;
# GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or
# a resistance cap. A value of 1 means one point, not confirmation of success.

SUB Main()
    # minimum=50 is an example requirement, not a client cap. ResistanceAtLeast rejects a missing
    # Player, reads one value and returns Integer Boolean 1=TRUE or 0=FALSE for value >= minimum.
    # The returned resistance itself is not Boolean. The helper is fully defined below.

    IF ResistanceAtLeast(50) = TRUE THEN
        UO.Print('Local resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetArmor()
    RETURN value >= minimum
END SUB
```

**Parameter and execution notes:**

- minimum=50 is an example requirement, not a client cap. ResistanceAtLeast rejects a missing Player, reads one value and returns Integer Boolean 1=TRUE or 0=FALSE for value >= minimum. The returned resistance itself is not Boolean. The helper is fully defined below.
