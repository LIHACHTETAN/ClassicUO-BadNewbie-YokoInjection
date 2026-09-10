# UO.GetWeight

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the current player’s status counter: current weight in stones.

## Exact syntax

```text
UO.GetWeight() -> Integer
```

## Parameters

No parameters.

## Returns

Integer — current weight in stones, 0..65535 in the client model. 0 can be a real value, unavailable data or a missing/destroyed Player. This is a quantity, not Boolean, ID or type: 1 means one unit, not success. It does not enumerate objects or return an array.

## Behavior

- This command takes no arguments. Use the exact signatures shown above.
- The game-thread read takes Player.Weight if the current Player exists and is not destroyed; otherwise 0. It does not search equipment, recompute bonuses, request status or wait for an update. A present ghost is not the same as a destroyed Player.
- Weight reads the total reported by the server in stones. Which body, equipment and nested-bag weights are included follows the shard’s rules. The getter does not traverse containers, sum item weights or refresh unopened bags. It is not an item’s Weight property or number of items.
- CharacterStatus validates its fixed body before updates. Weight is present in own extended status, follower slots from type 3, Luck from type 4, and server WeightMax from type 5. Compact/older packets without an optional counter preserve its previous cache. A new Player starts with zero counters; the command does not prove that a fresh status has arrived.
- RegisterCharacterGetterAliases adds missing zero-argument functions and intrinsic names for this field. Existing compatibility branches read the same bridge field. Names ignore letter case; an intrinsic without parentheses is reread unless a script variable shadows it.
- Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.

### Internal functions: from call to result

Native stages of reading a cached status counter. The complete CanCarry, LuckAtLeast or CanAddFollower helper in the example is user-defined BASIC, not a hidden native action. It does not change inventory or followers.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases adds missing zero-argument functions and intrinsic names for this field. Existing compatibility branches read the same bridge field. Names ignore letter case; an intrinsic without parentheses is reread unless a script variable shadows it.

`Weight GetWeight`.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `RegisterCharacterGetterAliases`.

#### 2. Invoke

The game-thread read takes Player.Weight if the current Player exists and is not destroyed; otherwise 0. It does not search equipment, recompute bonuses, request status or wait for an update. A present ghost is not the same as a destroyed Player.

Invoke reads on the game thread and honours script cancellation while waiting. No status request, target, network packet, attribute change or built-in delay is issued.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 3. CharacterStatus

CharacterStatus validates its fixed body before updates. Weight is present in own extended status, follower slots from type 3, Luck from type 4, and server WeightMax from type 5. Compact/older packets without an optional counter preserve its previous cache. A new Player starts with zero counters; the command does not prove that a fresh status has arrived.

Weight reads the total reported by the server in stones. Which body, equipment and nested-bag weights are included follows the shard’s rules. The getter does not traverse containers, sum item weights or refresh unopened bags. It is not an item’s Weight property or number of items.

Project source: `src/ClassicUO.Client/Network/PacketHandlers.cs`; function `CharacterStatus`.

#### 4. Clear

World.Clear removes Player. Later reads return 0 until a current player and its status are available; never keep a saved stat as proof that a reconnected character meets a requirement.

Integer — current weight in stones, 0..65535 in the client model. 0 can be a real value, unavailable data or a missing/destroyed Player. This is a quantity, not Boolean, ID or type: 1 means one unit, not success. It does not enumerate objects or return an array.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Clear`.

Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.


## Examples

### Display the cached counter

```vb
# Display the cached counter
#
# Reads the current player’s status counter: current weight in stones.
#
# Integer — current weight in stones, 0..65535 in the client model. 0 can be a real value,
# unavailable data or a missing/destroyed Player. This is a quantity, not Boolean, ID or type: 1
# means one unit, not success. It does not enumerate objects or return an array.

SUB Main()
    # value stores one no-argument read of the current player; CStr formats it for the journal
    # without changing its numeric meaning.

    VAR value = UO.GetWeight()
    UO.Print('Weight: ' + CStr(value))
END SUB
```

**Parameter and execution notes:**

- value stores one no-argument read of the current player; CStr formats it for the journal without changing its numeric meaning.

### Observe a change

```vb
# Observe a change
#
# Reads the current player’s status counter: current weight in stones.
#
# Integer — current weight in stones, 0..65535 in the client model. 0 can be a real value,
# unavailable data or a missing/destroyed Player. This is a quantity, not Boolean, ID or type: 1
# means one unit, not success. It does not enumerate objects or return an array.

SUB Main()
    # WAIT(500) separates before and after by 500 milliseconds. difference may be positive, zero or
    # negative; intermediate updates and character changes may be missed. The wait belongs to this
    # example.

    VAR before = UO.GetWeight()
    WAIT(500)
    VAR after = UO.GetWeight()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**Parameter and execution notes:**

- WAIT(500) separates before and after by 500 milliseconds. difference may be positive, zero or negative; intermediate updates and character changes may be missed. The wait belongs to this example.

### Complete decision helper

```vb
# Complete decision helper
#
# Reads the current player’s status counter: current weight in stones.
#
# Integer — current weight in stones, 0..65535 in the client model. 0 can be a real value,
# unavailable data or a missing/destroyed Player. This is a quantity, not Boolean, ID or type: 1
# means one unit, not success. It does not enumerate objects or return an array.

SUB Main()
    # CanCarry(extra) receives an additional weight in stones; 10 is an example, not a stack count.
    # It rejects negative extra, missing Player or maximum <= 0, reads current and maximum, then
    # returns Integer Boolean 1=TRUE or 0=FALSE for extra <= maximum - current. Subtraction avoids
    # overflow from current + extra. A character already above the limit fails even for extra=0.
    # This is a local estimate, not server permission; reads are not atomic and a zero current
    # weight can be unknown.

    IF CanCarry(10) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanCarry(extra)
    IF extra < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.GetWeight()
    VAR maximum = UO.MaxWeight()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extra <= maximum - current
END SUB
```

**Parameter and execution notes:**

- CanCarry(extra) receives an additional weight in stones; 10 is an example, not a stack count. It rejects negative extra, missing Player or maximum <= 0, reads current and maximum, then returns Integer Boolean 1=TRUE or 0=FALSE for extra <= maximum - current. Subtraction avoids overflow from current + extra. A character already above the limit fails even for extra=0. This is a local estimate, not server permission; reads are not atomic and a zero current weight can be unknown.
