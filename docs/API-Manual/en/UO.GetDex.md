# UO.GetDex

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the player’s current Dexterity (DEX).

## Exact syntax

```text
UO.GetDex() -> Integer
UO.GetDex(ObjID:Any) -> Integer
```

## Parameters

- `ObjID` — ObjID, only in the displayed one-argument form: character serial as an integer, decimal/0x hexadecimal string, "self", "lasttarget" or a name registered by AddObject. This selects an object, not its graphic/type. Omission selects the current player.

## Returns

Integer — current attribute points, 0..65535 as stored by the client; not a percentage, ID, skill value, stat lock or Boolean. 0 also means missing/destroyed player or unavailable subject. Compare against a numeric requirement, not = TRUE. This is not the attribute cap or guaranteed unmodified base value.

## Behavior

- The supported forms are () for self and (ObjID) for an explicit subject. No other optional arguments are supported.
- Reads Player.Dexterity when Player exists and is not destroyed; otherwise 0. A present dead character is not a destroyed object. The client does not derive this attribute from HP, mana or stamina.
- GetStr/GetInt/GetDex accept ObjID, but this client stores these attributes only on PlayerMobile: any serial other than the current player returns 0, even for another loaded mobile. This is a limitation relative to the generic Stealth mobile-stat description; no remote value is invented.
- Invoke reads on the game thread and honours script cancellation while waiting. No status request, target, network packet, attribute change or built-in delay is issued.
- Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.
- Equivalent attribute names with and without UO., ignoring letter case: `Dex Dexterity GetDex GetDexterity`.
- Bare Int(value) floors a BASIC number, and bare Str(value) formats a value as text. Those one-argument operations differ from UO.Int()/UO.Str(), which read attributes. GetInt(ObjID) is not number rounding.
- ExecuteStealthCompatibility.Arg resolves a registered object name before numeric conversion. An unknown nonnumeric string causes a conversion error, not an interactive target. Decimal values are cast to Integer; Array/Unit convert to 0. Use a valid serial, not these coercions, to identify the player.

### Internal functions: from call to result

These are the native reading stages. AttributeAtLeast below is a complete user-defined BASIC helper, not a hidden built-in API or a stat-changing operation.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases registers missing zero-argument functions and intrinsic names. Existing compatibility branches select their own getter; both paths return Integer. An intrinsic without parentheses is reread unless a script variable shadows it.

Equivalent attribute names with and without UO., ignoring letter case: `Dex Dexterity GetDex GetDexterity`.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `RegisterCharacterGetterAliases`.

#### 2. ExecuteStealthCompatibility

ObjID, only in the displayed one-argument form: character serial as an integer, decimal/0x hexadecimal string, "self", "lasttarget" or a name registered by AddObject. This selects an object, not its graphic/type. Omission selects the current player.

ExecuteStealthCompatibility.Arg resolves a registered object name before numeric conversion. An unknown nonnumeric string causes a conversion error, not an interactive target. Decimal values are cast to Integer; Array/Unit convert to 0. Use a valid serial, not these coercions, to identify the player.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 3. GetDexterity

GetStr/GetInt/GetDex accept ObjID, but this client stores these attributes only on PlayerMobile: any serial other than the current player returns 0, even for another loaded mobile. This is a limitation relative to the generic Stealth mobile-stat description; no remote value is invented.

Reads Player.Dexterity when Player exists and is not destroyed; otherwise 0. A present dead character is not a destroyed object. The client does not derive this attribute from HP, mana or stamina.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `GetDexterity`.

#### 4. Invoke

Reads Player.Dexterity when Player exists and is not destroyed; otherwise 0. A present dead character is not a destroyed object. The client does not derive this attribute from HP, mana or stamina. Invoke reads on the game thread and honours script cancellation while waiting. No status request, target, network packet, attribute change or built-in delay is issued.

Integer — current attribute points, 0..65535 as stored by the client; not a percentage, ID, skill value, stat lock or Boolean. 0 also means missing/destroyed player or unavailable subject. Compare against a numeric requirement, not = TRUE. This is not the attribute cap or guaranteed unmodified base value. Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 5. CharacterStatus

CharacterStatus assigns the received STR/DEX/INT field to Player.Dexterity when an applicable own-character status packet is handled. These queries only read that cache; they do not wait for a new packet.

Invoke reads on the game thread and honours script cancellation while waiting. No status request, target, network packet, attribute change or built-in delay is issued.

Project source: `src/ClassicUO.Client/Network/PacketHandlers.cs`; function `CharacterStatus`.

#### 6. Clear

World.Clear removes Player. Later reads return 0 until a current player and its status are available; never keep a saved stat as proof that a reconnected character meets a requirement.

Integer — current attribute points, 0..65535 as stored by the client; not a percentage, ID, skill value, stat lock or Boolean. 0 also means missing/destroyed player or unavailable subject. Compare against a numeric requirement, not = TRUE. This is not the attribute cap or guaranteed unmodified base value.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Clear`.

World.Clear removes Player. Later reads return 0 until a current player and its status are available; never keep a saved stat as proof that a reconnected character meets a requirement.


## Examples

### Read and display points

```vb
# Read and display points
#
# Reads the player’s current Dexterity (DEX).
#
# Integer — current attribute points, 0..65535 as stored by the client; not a percentage, ID,
# skill value, stat lock or Boolean. 0 also means missing/destroyed player or unavailable
# subject. Compare against a numeric requirement, not = TRUE. This is not the attribute cap or
# guaranteed unmodified base value.

SUB Main()
    # value holds the numeric result; CStr only formats it for the journal. No arguments are passed
    # and no character action is performed.

    VAR value = UO.GetDex()
    UO.Print('Dexterity: ' + CStr(value))
END SUB
```

**Parameter and execution notes:**

- value holds the numeric result; CStr only formats it for the journal. No arguments are passed and no character action is performed.

### Compare two observations

```vb
# Compare two observations
#
# Reads the player’s current Dexterity (DEX).
#
# Integer — current attribute points, 0..65535 as stored by the client; not a percentage, ID,
# skill value, stat lock or Boolean. 0 also means missing/destroyed player or unavailable
# subject. Compare against a numeric requirement, not = TRUE. This is not the attribute cap or
# guaranteed unmodified base value.

SUB Main()
    # before and after are 1000 ms apart; WAIT belongs to this example. change=after-before can be
    # positive, zero or negative. It cannot distinguish every intermediate update or a disconnect by
    # itself.

    VAR before = UO.GetDex()
    WAIT(1000)
    VAR after = UO.GetDex()
    VAR change = after - before
    UO.Print('Change: ' + CStr(change))
END SUB
```

**Parameter and execution notes:**

- before and after are 1000 ms apart; WAIT belongs to this example. change=after-before can be positive, zero or negative. It cannot distinguish every intermediate update or a disconnect by itself.

### Complete requirement-check helper

```vb
# Complete requirement-check helper
#
# Reads the player’s current Dexterity (DEX).
#
# Integer — current attribute points, 0..65535 as stored by the client; not a percentage, ID,
# skill value, stat lock or Boolean. 0 also means missing/destroyed player or unavailable
# subject. Compare against a numeric requirement, not = TRUE. This is not the attribute cap or
# guaranteed unmodified base value.

SUB Main()
    # minimum=80 is an example requirement, not a client cap. AttributeAtLeast(minimum) first
    # rejects a missing player, reads the attribute once, then returns Integer Boolean 1=TRUE or
    # 0=FALSE for >= minimum. The attribute itself is not Boolean; the comparison is.

    IF AttributeAtLeast(80) = TRUE THEN
        UO.Print('Requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB AttributeAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetDex()
    RETURN value >= minimum
END SUB
```

**Parameter and execution notes:**

- minimum=80 is an example requirement, not a client cap. AttributeAtLeast(minimum) first rejects a missing player, reads the attribute once, then returns Integer Boolean 1=TRUE or 0=FALSE for >= minimum. The attribute itself is not Boolean; the comparison is.

### Select the player by serial and object name

```vb
# Select the player by serial and object name
#
# Reads the player’s current Dexterity (DEX).
#
# Integer — current attribute points, 0..65535 as stored by the client; not a percentage, ID,
# skill value, stat lock or Boolean. 0 also means missing/destroyed player or unavailable
# subject. Compare against a numeric requirement, not = TRUE. This is not the attribute cap or
# guaranteed unmodified base value.

SUB Main()
    # id is UO.Self(), not type. AddObject stores that ID under statSubject without a target because
    # its second argument is supplied. Both calls read the same subject; separate reads still need
    # not be atomic.

    VAR id = UO.Self()
    IF id <> 0 THEN
        UO.AddObject('statSubject', id)
        VAR direct = UO.GetDex(id)
        VAR byName = UO.GetDex('statSubject')
        UO.Print('Direct: ' + CStr(direct) + '; alias: ' + CStr(byName))
    END IF
END SUB
```

**Parameter and execution notes:**

- id is UO.Self(), not type. AddObject stores that ID under statSubject without a target because its second argument is supplied. Both calls read the same subject; separate reads still need not be atomic.
