# UO.GetResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads one resistance of the current player using a numeric or textual selector.

## Exact syntax

```text
UO.GetResist(resistance:Any) -> Integer
```

## Parameters

- `resistance` — resistance is required. Numbers: 0=physical, 1=fire, 2=cold, 3=poison, 4=energy. Strings: physical/phys/armor, fire, cold, poison, energy. String case and surrounding whitespace are ignored. There is no serial, type, hue, target or second argument.

## Returns

Integer — the signed status value, -32768..32767 in the client model. Negative values are preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player; GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or a resistance cap. A value of 1 means one point, not confirmation of success.

## Behavior

- GetResistance branches on value kind first: the strings "1" and "0" are unknown names and return 0; they are not numeric selectors. Non-string Decimal values truncate toward zero (1.9 -> fire, -0.9 -> physical). TRUE=1 selects fire, FALSE=0 selects physical; Array/Unit also convert to 0. Use an explicit integer or supported name. AddObject names are not resolved.
- GetResistance selects exactly one bridge getter. Unsupported numbers/names return Integer 0 without a read. It neither collects all five values atomically nor changes the player’s resistances.
- PhysicalResistance is the server’s armor/status field: classic shards can use an armor rating, while resistance-based rules use physical resistance. The API does not translate between rulesets or calculate a damage-reduction percentage. Armor and physical aliases read the same field.
- The elemental fields arrive in extended CharacterStatus (0x11), type >= 4. The query itself imposes no server-era check. A compact/older status without these fields leaves their previous cache unchanged; a new Player starts at 0. Poison resistance is not the Poisoned flag; no resistance here is the Resisting Spells skill.
- CharacterStatus validates the fixed body before changing name, health or own status fields, then converts each resistance word to signed Int16. A truncated fixed body leaves the prior state intact. Optional type-6 trailer fields retain their existing fallback; these resistance commands do not read that trailer’s maximum-resistance fields.
- Invoke reads on the game thread and honours script cancellation while waiting. No status request, target, network packet, attribute change or built-in delay is issued.
- Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.

### Internal functions: from call to result

Actual native stages of a local resistance read. ResistanceAtLeast below is a fully defined user BASIC helper, not a hidden built-in function or a command that equips protective items.

#### 1. RegisterCharacterGetterAliases

Registers GetResist(resistance) and UO.GetResist(resistance) as one-argument functions bound to GetResistance. There is no zero-argument intrinsic for this selector.

resistance is required. Numbers: 0=physical, 1=fire, 2=cold, 3=poison, 4=energy. Strings: physical/phys/armor, fire, cold, poison, energy. String case and surrounding whitespace are ignored. There is no serial, type, hue, target or second argument.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `RegisterCharacterGetterAliases`.

#### 2. GetResistance

GetResistance branches on value kind first: the strings "1" and "0" are unknown names and return 0; they are not numeric selectors. Non-string Decimal values truncate toward zero (1.9 -> fire, -0.9 -> physical). TRUE=1 selects fire, FALSE=0 selects physical; Array/Unit also convert to 0. Use an explicit integer or supported name. AddObject names are not resolved.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`. GetResistance selects exactly one bridge getter. Unsupported numbers/names return Integer 0 without a read. It neither collects all five values atomically nor changes the player’s resistances.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `GetResistance`.

#### 3. ToInt

ToInt receives only a non-string selector here. Integer is unchanged; Decimal truncates toward zero; Array/Unit become 0. Its result is a selector index, not a resistance. String name handling stays in GetResistance.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/NumberConversions.cs`; function `ToInt`.

#### 4. Invoke

Invoke reads the selected Player field from the mapping above, preserving its sign. Missing/destroyed Player gives 0. The operation does not request status or wait for new data.

Invoke reads on the game thread and honours script cancellation while waiting. No status request, target, network packet, attribute change or built-in delay is issued.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 5. CharacterStatus

CharacterStatus validates the fixed body before changing name, health or own status fields, then converts each resistance word to signed Int16. A truncated fixed body leaves the prior state intact. Optional type-6 trailer fields retain their existing fallback; these resistance commands do not read that trailer’s maximum-resistance fields.

PhysicalResistance is the server’s armor/status field: classic shards can use an armor rating, while resistance-based rules use physical resistance. The API does not translate between rulesets or calculate a damage-reduction percentage. Armor and physical aliases read the same field. The elemental fields arrive in extended CharacterStatus (0x11), type >= 4. The query itself imposes no server-era check. A compact/older status without these fields leaves their previous cache unchanged; a new Player starts at 0. Poison resistance is not the Poisoned flag; no resistance here is the Resisting Spells skill.

Project source: `src/ClassicUO.Client/Network/PacketHandlers.cs`; function `CharacterStatus`.

#### 6. Clear

World.Clear removes Player. Later reads return 0 until a current player and its status are available; never keep a saved stat as proof that a reconnected character meets a requirement.

Integer — the signed status value, -32768..32767 in the client model. Negative values are preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player; GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or a resistance cap. A value of 1 means one point, not confirmation of success.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Clear`.

Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.


## Examples

### Select by name with mixed case

```vb
# Select by name with mixed case
#
# Reads one resistance of the current player using a numeric or textual selector.
#
# Integer — the signed status value, -32768..32767 in the client model. Negative values are
# preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player;
# GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or
# a resistance cap. A value of 1 means one point, not confirmation of success.

SUB Main()
    # resistance=" FiRe " selects fire after trimming and ignoring case. value remains a signed
    # numeric resistance; no target cursor opens.

    VAR value = UO.GetResist(' FiRe ')
    UO.Print('Fire resistance: ' + CStr(value))
END SUB
```

**Parameter and execution notes:**

- resistance=" FiRe " selects fire after trimming and ignoring case. value remains a signed numeric resistance; no target cursor opens.

### Compare numeric and textual selectors

```vb
# Compare numeric and textual selectors
#
# Reads one resistance of the current player using a numeric or textual selector.
#
# Integer — the signed status value, -32768..32767 in the client model. Negative values are
# preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player;
# GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or
# a resistance cap. A value of 1 means one point, not confirmation of success.

SUB Main()
    # 2 selects cold; "poison" selects poison. These are selectors, not serials. The comparison
    # reads two snapshots and returns a Boolean; poison resistance does not say whether the player
    # is poisoned.

    VAR cold = UO.GetResist(2)
    VAR poison = UO.GetResist('poison')
    IF cold < poison THEN
        UO.Print('Cold resistance is lower')
    ELSE
        UO.Print('Cold resistance is equal or higher')
    END IF
END SUB
```

**Parameter and execution notes:**

- 2 selects cold; "poison" selects poison. These are selectors, not serials. The comparison reads two snapshots and returns a Boolean; poison resistance does not say whether the player is poisoned.

### Complete minimum-resistance helper

```vb
# Complete minimum-resistance helper
#
# Reads one resistance of the current player using a numeric or textual selector.
#
# Integer — the signed status value, -32768..32767 in the client model. Negative values are
# preserved. 0 can be a real resistance, an unavailable field or a missing/destroyed Player;
# GetResist also gives 0 for an unknown selector. This is not Boolean, an object ID, a skill or
# a resistance cap. A value of 1 means one point, not confirmation of success.

SUB Main()
    # minimum=50 is an example requirement, not a client cap. ResistanceAtLeast rejects a missing
    # Player, reads one value and returns Integer Boolean 1=TRUE or 0=FALSE for value >= minimum.
    # The returned resistance itself is not Boolean. The helper is fully defined below.
    # The helper’s selector is passed unchanged to GetResist; the example uses "fire". It checks
    # Player presence, but does not validate arbitrary selector input or prove a fresh server
    # update. Use a selector listed above.

    IF ResistanceAtLeast('fire', 50) = TRUE THEN
        UO.Print('Local fire resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(selector, minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetResist(selector)
    RETURN value >= minimum
END SUB
```

**Parameter and execution notes:**

- minimum=50 is an example requirement, not a client cap. ResistanceAtLeast rejects a missing Player, reads one value and returns Integer Boolean 1=TRUE or 0=FALSE for value >= minimum. The returned resistance itself is not Boolean. The helper is fully defined below.
- The helper’s selector is passed unchanged to GetResist; the example uses "fire". It checks Player presence, but does not validate arbitrary selector input or prove a fresh server update. Use a selector listed above.
