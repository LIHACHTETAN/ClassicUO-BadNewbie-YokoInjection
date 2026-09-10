# UO.GetMaxStam

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads maximum stamina from the local model.

## Exact syntax

```text
UO.GetMaxStam() -> Integer
UO.GetMaxStam(ObjID:Any) -> Any
```

## Parameters

- `ObjID` — Optional object in the displayed overloads: numeric/hex-string serial, self, lasttarget or a registered AddObject name. This is not a type. Omission reads self. Unknown text causes a conversion error in some overloads; validate the name first.

## Returns

Integer — field StaminaMax, not a percentage or Boolean. Zero can be a real value or missing data. Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may be a relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead for that state.

## Behavior

- Does not open status or ask the server for an update. Unlike Stealth’s automatic request for missing HP, this client only reads existing data. It changes no stats and sends no packets.
- Each result is a separate read. The world may change between Exists and the next call; several queries do not form an atomic snapshot.
- For an object, World.Get rejects absent or IsDestroyed entries, producing 0. HP/HitsMax read Entity fields, including items with those fields; Mana/Stamina require Mobile. Omission reads self. A name with no arguments does not necessarily have an ID overload: check its signatures.
- Zero-argument reads also reject a missing or destroyed Player and return 0. This includes direct Mana/Stamina and their maximum-value getters, not only the overloads routed through World.Get. A present dead character can still have stored values.

### Internal functions: from call to result

These are actual internal C# stages. ReadValue is a fully defined helper in the example, not an undocumented built-in command.

#### 1. RegisterCharacterGetterAliases

At runtime creation, RegisterCharacterGetterAliases registers names and overloads. Omission selects bridge.Self; an argument selects its serial. Existing registrations are retained.

Integer — field StaminaMax, not a percentage or Boolean. Zero can be a real value or missing data. Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may be a relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead for that state.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject resolves numbers, hex strings and saved names. An AddObject name is resolved again on each call; this neither searches graphic/type nor opens an interactive selector.

Optional object in the displayed overloads: numeric/hex-string serial, self, lasttarget or a registered AddObject name. This is not a type. Omission reads self. Unknown text causes a conversion error in some overloads; validate the name first.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `TryGetObject`.

#### 3. Invoke

Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.

Each result is a separate read. The world may change between Exists and the next call; several queries do not form an atomic snapshot.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 4. Get

For an object, World.Get rejects absent or IsDestroyed entries, producing 0. HP/HitsMax read Entity fields, including items with those fields; Mana/Stamina require Mobile. Omission reads self. A name with no arguments does not necessarily have an ID overload: check its signatures.

Integer — field StaminaMax, not a percentage or Boolean. Zero can be a real value or missing data. Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may be a relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead for that state.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Get`.

Does not open status or ask the server for an update. Unlike Stealth’s automatic request for missing HP, this client only reads existing data. It changes no stats and sends no packets.


## Examples

### Display the player value

```vb
# Display the player value
#
# Reads maximum stamina from the local model.
#
# Integer — field StaminaMax, not a percentage or Boolean. Zero can be a real value or missing
# data. Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may
# be a relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead
# for that state.

SUB Main()
    # The call without arguments reads self. value stores one number; STR converts it only for the
    # message.

    VAR value = UO.GetMaxStam()
    UO.Print('GetMaxStam: ' + STR(value))
END SUB
```

**Parameter and execution notes:**

- The call without arguments reads self. value stores one number; STR converts it only for the message.

### Use the value in a condition or calculation

```vb
# Use the value in a condition or calculation
#
# Reads maximum stamina from the local model.
#
# Integer — field StaminaMax, not a percentage or Boolean. Zero can be a real value or missing
# data. Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may
# be a relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead
# for that state.

SUB Main()
    # The example applies a threshold or calculation for this field. Numbers in conditions are
    # example settings, not server limits. A maximum is checked for positivity before division.

    VAR value = UO.GetMaxStam()
    IF value > 0 THEN
        UO.Print('Stamina percent: ' + STR(UO.Stamina() * 100 / value))
    END IF
END SUB
```

**Parameter and execution notes:**

- The example applies a threshold or calculation for this field. Numbers in conditions are example settings, not server limits. A maximum is checked for positivity before division.

### Complete ReadValue helper

```vb
# Complete ReadValue helper
#
# Reads maximum stamina from the local model.
#
# Integer — field StaminaMax, not a percentage or Boolean. Zero can be a real value or missing
# data. Never divide by a zero maximum. Other mobiles’ values may be unavailable. HP/HitsMax may
# be a relative server scale instead of exact points. HP=0 does not prove death; use Dead/IsDead
# for that state.

SUB Main()
    # lasttarget is the previously selected object; Exists checks presence. obj is ReadValue’s only
    # parameter. The fully defined helper returns the command’s number unchanged.

    IF UO.Exists('lasttarget') THEN
        VAR value = ReadValue('lasttarget')
        UO.Print('Selected value: ' + CStr(value))
    END IF
END SUB

SUB ReadValue(obj)
    RETURN UO.GetMaxStam(obj)
END SUB
```

**Parameter and execution notes:**

- lasttarget is the previously selected object; Exists checks presence. obj is ReadValue’s only parameter. The fully defined helper returns the command’s number unchanged.
