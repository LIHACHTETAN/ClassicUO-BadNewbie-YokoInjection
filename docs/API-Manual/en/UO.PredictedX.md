# UO.PredictedX

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the predicted X coordinate after the player’s currently queued movement steps.

## Exact syntax

```text
UO.PredictedX() -> Integer
```

## Parameters

No parameters.

## Returns

Integer X in map tiles. 0 is a valid coordinate or missing-player result.

## Behavior

- Exactly the zero-argument UO function shown in Syntax. No target, serial, type, destination, distance or timeout parameter. The number is not Boolean, an ID or a tile record; 1 does not mean arrival.
- GetEndPosition reads X/Y/Z/direction from the last already queued Mobile.Step. If the queue is empty, it reads the current player position/direction. This is an O(1) peek: it does not remove a step, walk, send a packet, calculate a route or wait for arrival.
- X and Y are world/map coordinates, not container-gump pixels. Z is height, not a floor number. The return is one component, not an array or the final pathfinding destination.
- This is a local prediction, not confirmed arrival. New steps, completion, denied movement, queue clearing or teleportation may change it. Separate component calls are not an atomic snapshot; matching X alone does not prove Y/Z or server acceptance.
- Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.
- External IApiBridge implementations without IPredictedMovementBridge retain their current-coordinate/current-direction fallback. Classic UO implements the queue-aware interface.

### Internal functions: from call to result

Actual native read stages. PredictionEquals is a complete user-defined BASIC helper, not an internal command or a movement procedure.

#### 1. ExecuteStealthCompatibility

The registered native function dispatches to ReadPredictedCoordinate, which selects the matching IPredictedMovementBridge property. It does not call NewMoveXY or start a pathfinder.

Exactly the zero-argument UO function shown in Syntax. No target, serial, type, destination, distance or timeout parameter. The number is not Boolean, an ID or a tile record; 1 does not mean arrival.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 2. ReadPredictedCoordinate

The registered native function dispatches to ReadPredictedCoordinate, which selects the matching IPredictedMovementBridge property. It does not call NewMoveXY or start a pathfinder.

External IApiBridge implementations without IPredictedMovementBridge retain their current-coordinate/current-direction fallback. Classic UO implements the queue-aware interface.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ReadPredictedCoordinate`.

#### 3. Invoke

Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.

Integer X in map tiles. 0 is a valid coordinate or missing-player result.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 4. ReadPredictedPosition

ReadPredictedPosition returns 0 for a missing/destroyed Player; otherwise it calls GetEndPosition and selects one component.

GetEndPosition reads X/Y/Z/direction from the last already queued Mobile.Step. If the queue is empty, it reads the current player position/direction. This is an O(1) peek: it does not remove a step, walk, send a packet, calculate a route or wait for arrival.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `ReadPredictedPosition`.

#### 5. GetEndPosition

GetEndPosition reads X/Y/Z/direction from the last already queued Mobile.Step. If the queue is empty, it reads the current player position/direction. This is an O(1) peek: it does not remove a step, walk, send a packet, calculate a route or wait for arrival.

X and Y are world/map coordinates, not container-gump pixels. Z is height, not a floor number. The return is one component, not an array or the final pathfinding destination.

Project source: `src/ClassicUO.Client/Game/GameObjects/Mobile.cs`; function `GetEndPosition`.

#### 6. InjectionValue

Integer X in map tiles. 0 is a valid coordinate or missing-player result.

This is a local prediction, not confirmed arrival. New steps, completion, denied movement, queue clearing or teleportation may change it. Separate component calls are not an atomic snapshot; matching X alone does not prove Y/Z or server acceptance.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs`; function `InjectionValue`.

PredictionEquals(expected) accepts one numeric coordinate/height/direction, rejects a missing player and compares one predicted component. Returns Integer Boolean 1=TRUE or 0=FALSE. It never waits for or guarantees arrival.


## Examples

### Read one component

```vb
# Read one component
#
# Reads the predicted X coordinate after the player’s currently queued movement steps.
#
# Integer X in map tiles. 0 is a valid coordinate or missing-player result.

SUB Main()
    # predicted stores one call without arguments; CStr formats its number for the journal.

    VAR predicted = UO.PredictedX()
    UO.Print('Predicted: ' + CStr(predicted))
END SUB
```

**Parameter and execution notes:**

- predicted stores one call without arguments; CStr formats its number for the journal.

### Observe a changing prediction

```vb
# Observe a changing prediction
#
# Reads the predicted X coordinate after the player’s currently queued movement steps.
#
# Integer X in map tiles. 0 is a valid coordinate or missing-player result.

SUB Main()
    # WAIT(100) pauses this example for 100 ms. before and after may be equal despite intermediate
    # movement; no movement is started by these reads.

    VAR before = UO.PredictedX()
    WAIT(100)
    VAR after = UO.PredictedX()
    IF before <> after THEN
        UO.Print('Prediction changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Parameter and execution notes:**

- WAIT(100) pauses this example for 100 ms. before and after may be equal despite intermediate movement; no movement is started by these reads.

### Complete comparison helper

```vb
# Complete comparison helper
#
# Reads the predicted X coordinate after the player’s currently queued movement steps.
#
# Integer X in map tiles. 0 is a valid coordinate or missing-player result.

SUB Main()
    # expected is the example’s coordinate/height/direction value, not an argument of the native
    # command. PredictionEquals checks UO.Self(), reads once, then returns 1=TRUE on equality and
    # 0=FALSE otherwise. All helper code is shown below Main. Matching one component is not arrival.

    IF PredictionEquals(1445) = TRUE THEN
        UO.Print('Queued endpoint matches this component')
    ELSE
        UO.Print('Different component or no player')
    END IF
END SUB

SUB PredictionEquals(expected)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR predicted = UO.PredictedX()
    RETURN predicted = expected
END SUB
```

**Parameter and execution notes:**

- expected is the example’s coordinate/height/direction value, not an argument of the native command. PredictionEquals checks UO.Self(), reads once, then returns 1=TRUE on equality and 0=FALSE otherwise. All helper code is shown below Main. Matching one component is not arrival.
