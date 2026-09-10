# UO.Mana

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads current mana from the local model.

## Exact syntax

```text
UO.Mana() -> Any
```

## Parameters

No parameters.

## Returns

Integer — field Mana, not a percentage or Boolean. Zero can be a real value or missing data. Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may be a relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead for that state.

## Behavior

- Does not open status or ask the server for an update. Unlike Stealth’s automatic request for missing HP, this client only reads existing data. It changes no stats and sends no packets.
- Each result is a separate read. The world may change between Exists and the next call; several queries do not form an atomic snapshot.
- For an object, World.Get rejects absent or IsDestroyed entries, producing 0. HP/HitsMax read Entity fields, including items with those fields; Mana/Stamina require Mobile. Omission reads self. A name with no arguments does not necessarily have an ID overload: check its signatures.
- Zero-argument reads also reject a missing or destroyed Player and return 0. This includes direct Mana/Stamina and their maximum-value getters, not only the overloads routed through World.Get. A present dead character can still have stored values.

### Internal functions: from call to result

These are actual internal C# stages. ReadValue is a fully defined helper in the example, not an undocumented built-in command.

#### 1. RegisterCharacterGetterAliases

At runtime creation, RegisterCharacterGetterAliases registers names and overloads. Omission selects bridge.Self; an argument selects its serial. Existing registrations are retained.

Integer — field Mana, not a percentage or Boolean. Zero can be a real value or missing data. Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may be a relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead for that state.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `RegisterCharacterGetterAliases`.

#### 2. Invoke

Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.

Each result is a separate read. The world may change between Exists and the next call; several queries do not form an atomic snapshot.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

Does not open status or ask the server for an update. Unlike Stealth’s automatic request for missing HP, this client only reads existing data. It changes no stats and sends no packets.


## Examples

### Display the player value

```vb
# Display the player value
#
# Reads current mana from the local model.
#
# Integer — field Mana, not a percentage or Boolean. Zero can be a real value or missing data.
# Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may be a
# relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead for
# that state.

SUB Main()
    # The call without arguments reads self. value stores one number; STR converts it only for the
    # message.

    VAR value = UO.Mana()
    UO.Print('Mana: ' + STR(value))
END SUB
```

**Parameter and execution notes:**

- The call without arguments reads self. value stores one number; STR converts it only for the message.

### Use the value in a condition or calculation

```vb
# Use the value in a condition or calculation
#
# Reads current mana from the local model.
#
# Integer — field Mana, not a percentage or Boolean. Zero can be a real value or missing data.
# Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may be a
# relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead for
# that state.

SUB Main()
    # The example applies a threshold or calculation for this field. Numbers in conditions are
    # example settings, not server limits. A maximum is checked for positivity before division.

    VAR value = UO.Mana()
    IF value >= 10 THEN
        UO.Print('At least ten mana points are known')
    END IF
END SUB
```

**Parameter and execution notes:**

- The example applies a threshold or calculation for this field. Numbers in conditions are example settings, not server limits. A maximum is checked for positivity before division.

### Complete ReadValue helper

```vb
# Complete ReadValue helper
#
# Reads current mana from the local model.
#
# Integer — field Mana, not a percentage or Boolean. Zero can be a real value or missing data.
# Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may be a
# relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead for
# that state.

SUB Main()
    # This name has no ID overload. ReadValue without parameters reads self; WAIT(1000) separates
    # two calls. Comparing two snapshots can miss intermediate changes.

    VAR before = ReadValue()
    WAIT(1000)
    VAR after = ReadValue()
    UO.Print('Before: ' + CStr(before) + '; after: ' + CStr(after))
END SUB

SUB ReadValue()
    RETURN UO.Mana()
END SUB
```

**Parameter and execution notes:**

- This name has no ID overload. ReadValue without parameters reads self; WAIT(1000) separates two calls. Comparing two snapshots can miss intermediate changes.
