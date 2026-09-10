# UO.Backpack

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Returns the currently equipped backpack container ID.

## Exact syntax

```text
UO.Backpack() -> Integer
```

## Parameters

No parameters.

## Returns

Integer — serial/ID, not graphic/type, layer, item count or Boolean. 0 means no current object. All 32 serial bits are preserved; test <> 0 rather than = TRUE or > 0. A stored result does not update automatically. Reads the non-destroyed item on the current Player’s Backpack layer. Missing/destroyed Player, missing backpack or destroyed bag gives 0. This identifies the container, not its contents or a newly created bag.

## Behavior

- No arguments. Reads local client state through Invoke on the game thread; script cancellation can interrupt waiting for that thread. Sends no packet, opens no container or target, and does not move an item.
- The intrinsic without parentheses (self/backpack) is a fresh read unless a script variable shadows it. Quoted aliases are resolved by the receiving command. In transfer destinations, "self" means backpack, whereas UO.Self() returns the player serial. Use UO.Backpack() explicitly when a container ID is required.
- World.Clear removes the player; subsequent reads give 0. Logging in or replacing the equipped bag can change the ID. Separate reads are not an atomic snapshot. A nonzero ID alone is not proof of connectivity, server permission or loaded contents.

### Internal functions: from call to result

The internal stages below read the actual client object. IsOwnSerial is the complete script helper shown in the example, not another built-in API.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility selects the zero-argument branch and wraps the bridge integer in InjectionValue. There is no Pascal out parameter or additional optional argument.

Integer — serial/ID, not graphic/type, layer, item count or Boolean. 0 means no current object. All 32 serial bits are preserved; test <> 0 rather than = TRUE or > 0. A stored result does not update automatically.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 2. Invoke

Reads the non-destroyed item on the current Player’s Backpack layer. Missing/destroyed Player, missing backpack or destroyed bag gives 0. This identifies the container, not its contents or a newly created bag. Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.

Integer — serial/ID, not graphic/type, layer, item count or Boolean. 0 means no current object. All 32 serial bits are preserved; test <> 0 rather than = TRUE or > 0. A stored result does not update automatically. No arguments. Reads local client state through Invoke on the game thread; script cancellation can interrupt waiting for that thread. Sends no packet, opens no container or target, and does not move an item.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 3. FindItemByLayer

Reads the non-destroyed item on the current Player’s Backpack layer. Missing/destroyed Player, missing backpack or destroyed bag gives 0. This identifies the container, not its contents or a newly created bag.

Integer — serial/ID, not graphic/type, layer, item count or Boolean. 0 means no current object. All 32 serial bits are preserved; test <> 0 rather than = TRUE or > 0. A stored result does not update automatically.

Project source: `src/ClassicUO.Client/Game/GameObjects/Entity.cs`; function `FindItemByLayer`.

#### 4. Clear

World.Clear removes the player; subsequent reads give 0. Logging in or replacing the equipped bag can change the ID. Separate reads are not an atomic snapshot. A nonzero ID alone is not proof of connectivity, server permission or loaded contents.

World.Clear removes the player; subsequent reads give 0. Logging in or replacing the equipped bag can change the ID. Separate reads are not an atomic snapshot. A nonzero ID alone is not proof of connectivity, server permission or loaded contents.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Clear`.

World.Clear removes the player; subsequent reads give 0. Logging in or replacing the equipped bag can change the ID. Separate reads are not an atomic snapshot. A nonzero ID alone is not proof of connectivity, server permission or loaded contents.


## Examples

### Read and format the ID

```vb
# Read and format the ID
#
# Returns the currently equipped backpack container ID.
#
# Integer — serial/ID, not graphic/type, layer, item count or Boolean. 0 means no current
# object. All 32 serial bits are preserved; test <> 0 rather than = TRUE or > 0. A stored result
# does not update automatically. Reads the non-destroyed item on the current Player’s Backpack
# layer. Missing/destroyed Player, missing backpack or destroyed bag gives 0. This identifies
# the container, not its contents or a newly created bag.

SUB Main()
    # id stores one call; HEX formats that serial for the journal. This example does not select or
    # use the object.

    VAR id = UO.Backpack()
    UO.Print('ID: ' + HEX(id))
END SUB
```

**Parameter and execution notes:**

- id stores one call; HEX formats that serial for the journal. This example does not select or use the object.

### Detect an ID change between two reads

```vb
# Detect an ID change between two reads
#
# Returns the currently equipped backpack container ID.
#
# Integer — serial/ID, not graphic/type, layer, item count or Boolean. 0 means no current
# object. All 32 serial bits are preserved; test <> 0 rather than = TRUE or > 0. A stored result
# does not update automatically. Reads the non-destroyed item on the current Player’s Backpack
# layer. Missing/destroyed Player, missing backpack or destroyed bag gives 0. This identifies
# the container, not its contents or a newly created bag.

SUB Main()
    # before/after are values 250 ms apart. WAIT is only in this example. Equality means the
    # endpoint IDs match; changes in between can be missed.

    VAR before = UO.Backpack()
    WAIT(250)
    VAR after = UO.Backpack()
    IF before <> after THEN
        UO.Print('ID changed: ' + HEX(after))
    END IF
END SUB
```

**Parameter and execution notes:**

- before/after are values 250 ms apart. WAIT is only in this example. Equality means the endpoint IDs match; changes in between can be missed.

### Complete IsOwnSerial helper

```vb
# Complete IsOwnSerial helper
#
# Returns the currently equipped backpack container ID.
#
# Integer — serial/ID, not graphic/type, layer, item count or Boolean. 0 means no current
# object. All 32 serial bits are preserved; test <> 0 rather than = TRUE or > 0. A stored result
# does not update automatically. Reads the non-destroyed item on the current Player’s Backpack
# layer. Missing/destroyed Player, missing backpack or destroyed bag gives 0. This identifies
# the container, not its contents or a newly created bag.

SUB Main()
    # candidate is the saved LastTarget ID. IsOwnSerial(candidate) takes one serial and returns a
    # Boolean Integer: 1=TRUE for the current nonzero own ID, otherwise 0=FALSE. The helper is fully
    # defined; it never changes target.

    VAR candidate = UO.LastTarget()
    IF IsOwnSerial(candidate) = TRUE THEN
        UO.Print('Own object selected')
    ELSE
        UO.Print('Different object or no own object')
    END IF
END SUB

SUB IsOwnSerial(candidate)
    VAR current = UO.Backpack()
    RETURN current <> 0 AND current = candidate
END SUB
```

**Parameter and execution notes:**

- candidate is the saved LastTarget ID. IsOwnSerial(candidate) takes one serial and returns a Boolean Integer: 1=TRUE for the current nonzero own ID, otherwise 0=FALSE. The helper is fully defined; it never changes target.
