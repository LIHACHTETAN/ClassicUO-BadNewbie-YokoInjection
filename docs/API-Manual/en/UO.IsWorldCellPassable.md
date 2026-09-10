# UO.IsWorldCellPassable

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Checks one transition to a neighbouring world cell and returns passability together with height.

## Exact syntax

```text
UO.IsWorldCellPassable(CurrX:Any, CurrY:Any, CurrZ:Any, DestX:Any, DestY:Any, DestZ:Any, WorldNum:Any) -> Array
```

## Parameters

- `CurrX` — Required world X coordinate of the source cell. Integer 0..65535 within the loaded map; not a gump coordinate.
- `CurrY` — Required world Y coordinate of the source cell. Integer 0..65535 within the loaded map; not a gump coordinate.
- `CurrZ` — Required source height −128..127. World elevation, not a floor number. Invalid heights are rejected, not clamped.
- `DestX` — Required world X coordinate of the destination cell. Integer 0..65535 within the loaded map; not a gump coordinate.
- `DestY` — Required world Y coordinate of the destination cell. Integer 0..65535 within the loaded map; not a gump coordinate.
- `DestZ` — Required input fallback Z, usually CurrZ. Not a var argument: the variable is unchanged and does not specify a required floor. Read calculated height from result[1]. This bridge always supplies its own height; the argument preserves the Pascal-shaped signature.
- `WorldNum` — Required facet number: UO.WorldNum(). Only the current map with known dimensions is checked; another facet is not loaded.

## Returns

Array of two Integer values: [0] — passability, 1 = TRUE, 0 = FALSE; [1] — calculated Z. Only the first element is logical. Do not compare the array itself with TRUE. Zero/negative height is valid; when [0]=0, height does not prove reachability. Rejected arguments return [0, CurrZ].

## Behavior

- No movement, door opening, targeting or network packets. Reads existing local geometry; the server may later deny a step. Separate queries may see different state.
- Accepts a neighbour with X/Y differences no greater than 1. A farther destination, map boundary violation, missing player/map or IsDestroyed is rejected before collision work. Use GetPathArray or NewMoveXY for an entire route.
- Identical valid X/Y return [1, CurrZ] without collision checking: no step is needed. This does not test whether the character can leave that cell. Player state and current Pathfinder rules affect an adjacent step; missing loaded geometry may cause rejection.

### Internal functions: from call to result

These are actual internal C# stages. IsCellOpen is a fully defined helper in the example, not an undocumented built-in command.

#### 1. ExecuteStealthCompatibility

Selects the compatibility branch and reads seven Integer arguments. DestZ is used only if an alternative bridge returns no height. Returns an array without rewriting an argument.

Array of two Integer values: [0] — passability, 1 = TRUE, 0 = FALSE; [1] — calculated Z. Only the first element is logical. Do not compare the array itself with TRUE. Zero/negative height is valid; when [0]=0, height does not prove reachability. Rejected arguments return [0, CurrZ].

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 2. CheckWorldStep

Invoke validates player, map, dimensions, X/Y, Z and adjacency before coordinate subtraction. Chooses the direction. Success also requires exact destination X/Y after CanWalkForQuery.

Array of two Integer values: [0] — passability, 1 = TRUE, 0 = FALSE; [1] — calculated Z. Only the first element is logical. Do not compare the array itself with TRUE. Zero/negative height is valid; when [0]=0, height does not prove reachability. Rejected arguments return [0, CurrZ].

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `CheckWorldStep`.

#### 3. CanWalkForQuery

Temporarily removes another active route’s forbidden-cell predicate, restoring it in finally. Calls CanWalk without starting a route.

No movement, door opening, targeting or network packets. Reads existing local geometry; the server may later deny a step. Separate queries may see different state.

Project source: `src/ClassicUO.Client/Game/Pathfinder.cs`; function `CanWalkForQuery`.

#### 4. CanWalk

Checks the main step and diagonal side cells. Returns bool and updates ref coordinates only for an accepted step; a fallback side is not necessarily the requested destination.

CanWalk checks the main step and side cells for diagonals. CalculateNewZ selects a surface and clearance using player state. CalculateMinMaxZ derives the source height range via CreateItemList, which collects loaded Land/Static/Multi/Item/Mobile collision data and rules. A diagonal fallback side does not count as reaching the requested cell.

Project source: `src/ClassicUO.Client/Game/Pathfinder.cs`; function `CanWalk`.

#### 5. CalculateNewZ

Receives destination X/Y, source Z by ref and direction. Selects a surface with sufficient clearance using player state. bool indicates local passability; z holds the selected height.

CanWalk checks the main step and side cells for diagonals. CalculateNewZ selects a surface and clearance using player state. CalculateMinMaxZ derives the source height range via CreateItemList, which collects loaded Land/Static/Multi/Item/Mobile collision data and rules. A diagonal fallback side does not count as reaching the requested cell.

Project source: `src/ClassicUO.Client/Game/Pathfinder.cs`; function `CalculateNewZ`.

#### 6. CalculateMinMaxZ

Receives the new cell, current Z, direction and player mode. Uses CreateItemList to obtain source geometry and computes ref minZ/maxZ for rise and clearance checks.

CanWalk checks the main step and side cells for diagonals. CalculateNewZ selects a surface and clearance using player state. CalculateMinMaxZ derives the source height range via CreateItemList, which collects loaded Land/Static/Multi/Item/Mobile collision data and rules. A diagonal fallback side does not count as reaching the requested cell.

Project source: `src/ClassicUO.Client/Game/Pathfinder.cs`; function `CalculateMinMaxZ`.

#### 7. CreateItemList

Receives a list, X/Y and player mode. Collects loaded cell objects and collision rules; bool indicates available geometry. Map.GetTile uses load=false, so it does not read new blocks.

CanWalk checks the main step and side cells for diagonals. CalculateNewZ selects a surface and clearance using player state. CalculateMinMaxZ derives the source height range via CreateItemList, which collects loaded Land/Static/Multi/Item/Mobile collision data and rules. A diagonal fallback side does not count as reaching the requested cell.

Project source: `src/ClassicUO.Client/Game/Pathfinder.cs`; function `CreateItemList`.

No movement, door opening, targeting or network packets. Reads existing local geometry; the server may later deny a step. Separate queries may see different state.


## Examples

### Check the cell to the east

```vb
# Check the cell to the east
#
# Checks one transition to a neighbouring world cell and returns passability together with
# height.
#
# Array of two Integer values: [0] — passability, 1 = TRUE, 0 = FALSE; [1] — calculated Z. Only
# the first element is logical. Do not compare the array itself with TRUE. Zero/negative height
# is valid; when [0]=0, height does not prove reachability. Rejected arguments return [0,
# CurrZ].

SUB Main()
    # x/y/z are the source; x+1/y is its neighbour; the sixth argument z is fallback Z; the last
    # selects the current facet. Check result[0] before using result[1].

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR result = UO.IsWorldCellPassable(x,y,z,x+1,y,z,UO.WorldNum())
    IF result[0] = TRUE THEN
        UO.Print('Passable, Z=' + CStr(result[1]))
    ELSE
        UO.Print('Blocked')
    END IF
END SUB
```

**Parameter and execution notes:**

- x/y/z are the source; x+1/y is its neighbour; the sixth argument z is fallback Z; the last selects the current facet. Check result[0] before using result[1].

### Read Z without changing the input argument

```vb
# Read Z without changing the input argument
#
# Checks one transition to a neighbouring world cell and returns passability together with
# height.
#
# Array of two Integer values: [0] — passability, 1 = TRUE, 0 = FALSE; [1] — calculated Z. Only
# the first element is logical. Do not compare the array itself with TRUE. Zero/negative height
# is valid; when [0]=0, height does not prove reachability. Rejected arguments return [0,
# CurrZ].

SUB Main()
    # proposedZ remains 0 after the call. targetZ comes from result[1], not from the argument. The
    # example does not infer height on failure.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR proposedZ = 0
    VAR result = UO.IsWorldCellPassable(x,y,z,x,y+1,proposedZ,UO.WorldNum())
    IF result[0] = 1 THEN
        VAR targetZ = result[1]
        UO.Print('Input=' + CStr(proposedZ) + '; result=' + CStr(targetZ))
    END IF
END SUB
```

**Parameter and execution notes:**

- proposedZ remains 0 after the call. targetZ comes from result[1], not from the argument. The example does not infer height on failure.

### Complete IsCellOpen helper

```vb
# Complete IsCellOpen helper
#
# Checks one transition to a neighbouring world cell and returns passability together with
# height.
#
# Array of two Integer values: [0] — passability, 1 = TRUE, 0 = FALSE; [1] — calculated Z. Only
# the first element is logical. Do not compare the array itself with TRUE. Zero/negative height
# is valid; when [0]=0, height does not prove reachability. Rejected arguments return [0,
# CurrZ].

SUB Main()
    # The complete helper below Main accepts source X/Y/Z, destination X/Y and map. It supplies the
    # required sixth argument and returns only Integer 1/0, not an array. IsCellOpen can therefore
    # be compared with TRUE. This code does not move the player.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR openCell = IsCellOpen(x,y,UO.GetZ(),x+1,y+1,UO.WorldNum())
    IF openCell = TRUE THEN
        UO.Print('Diagonal cell is locally passable')
    END IF
END SUB

SUB IsCellOpen(x,y,z,toX,toY,map)
    VAR cellResult = UO.IsWorldCellPassable(x,y,z,toX,toY,z,map)
    IF GetArrayLength(cellResult) <> 2 THEN
        RETURN 0
    END IF
    RETURN cellResult[0]
END SUB
```

**Parameter and execution notes:**

- The complete helper below Main accepts source X/Y/Z, destination X/Y and map. It supplies the required sixth argument and returns only Integer 1/0, not an array. IsCellOpen can therefore be compared with TRUE. This code does not move the player.
