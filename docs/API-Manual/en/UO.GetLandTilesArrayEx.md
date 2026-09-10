# UO.GetLandTilesArrayEx

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Finds land tiles by graphic/type in a rectangle.

## Exact syntax

```text
UO.GetLandTilesArrayEx(Xmin:Any, Ymin:Any, Xmax:Any, Ymax:Any, WorldNum:Any, TileTypes:Any) -> Any
```

## Parameters

- `Xmin` — World coordinates of two inclusive corners, 0..65535. Reversed corners are normalized. At most 1,000,000 cells; invalid bounds raise a script error before any map read.
- `Ymin` — World coordinates of two inclusive corners, 0..65535. Reversed corners are normalized. At most 1,000,000 cells; invalid bounds raise a script error before any map read.
- `Xmax` — World coordinates of two inclusive corners, 0..65535. Reversed corners are normalized. At most 1,000,000 cells; invalid bounds raise a script error before any map read.
- `Ymax` — World coordinates of two inclusive corners, 0..65535. Reversed corners are normalized. At most 1,000,000 cells; invalid bounds raise a script error before any map read.
- `WorldNum` — Facet number, 0..255; use UO.WorldNum(). A different facet returns an empty Array. A facet change between slices discards the partial result.
- `TileTypes` — Array of numeric graphics/types. Repeated types do not duplicate records. A scalar is also accepted as one type. An empty Array matches all types; an array containing one 0 matches only 0.

## Returns

Array of [graphic, X, Y, Z] records, all Integer. graphic is the land type; Z is its base height. No matches: empty Array. Count records with GetArrayLength(result). Indexes start at 0. The result is not a Boolean, serial, or Pascal record; there is no seventh output parameter.

## Behavior

- Reads local data without changing FindItem/FindCount, moving, targeting or sending a server command.
- Ascending X, then ascending Y within each X. Records at one cell retain bridge order, not distance or height order.
- Processes up to 32 cells per slice with a soft budget near 1 ms. Checks cancellation between slices. Complex cells or cold reads can exceed the budget. Split large areas; world data can change during a scan.

### Internal functions: from call to result

Actual C# stages, not extra UO commands. The executable examples below include their helper procedure.

#### 1. ExecuteStealthCompatibility

Accepts six arguments; the regular form passes one type, Ex converts an Array or scalar to types.

Calls FindPortableTiles with land/static mode and returns the record Array directly.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 2. FindPortableTiles

Validates coordinates, facet and area using 64-bit arithmetic; normalizes corners and builds a type HashSet.

Keeps an X/Y cursor; schedules ScanSlice through ExecutePathQuerySlice. Wait(0) checks cancellation between slices; a facet change returns an empty Array.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `FindPortableTiles`.

#### 3. ScanSlice

Visits at most 32 cells on the game thread, preserving the cursor after each cell.

GetLandscapeTile supplies graphic/Z/flags; GetStaticTiles supplies graphic/Z/hue triples. Matching records are appended; control returns between slices.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ScanSlice`.

#### 4. GetChunk2

Accepts two chunk coordinates and a load flag; validates each axis before flattening the index.

Returns a Chunk or null, never a neighboring column for out-of-map Y. Reuses loaded chunks and reads new ones when needed.

Project source: `src/ClassicUO.Client/Game/Map/Map.cs`; function `GetChunk2`.

Reads local data without changing FindItem/FindCount, moving, targeting or sending a server command.


## Examples

### Search near the character

```vb
# Search near the character
#
# Finds land tiles by graphic/type in a rectangle.
#
# Array of [graphic, X, Y, Z] records, all Integer. graphic is the land type; Z is its base
# height. No matches: empty Array. Count records with GetArrayLength(result). Indexes start at
# 0. The result is not a Boolean, serial, or Pascal record; there is no seventh output
# parameter.

SUB Main()
    # x/y are self coordinates; map is the current facet. The inclusive area is 3×3. Ex uses two
    # sample types; the regular form uses one. Replace graphics with your resources, not object IDs.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArrayEx(x, y, x + 2, y + 2, map, types)
    UO.Print("Records: " + CStr(GetArrayLength(rows)))
END SUB
```

**Parameter and execution notes:**

- x/y are self coordinates; map is the current facet. The inclusive area is 3×3. Ex uses two sample types; the regular form uses one. Replace graphics with your resources, not object IDs.

### Reversed corners and all result fields

```vb
# Reversed corners and all result fields
#
# Finds land tiles by graphic/type in a rectangle.
#
# Array of [graphic, X, Y, Z] records, all Integer. graphic is the land type; Z is its base
# height. No matches: empty Array. Count records with GetArrayLength(result). Indexes start at
# 0. The result is not a Boolean, serial, or Pascal record; there is no seventh output
# parameter.

SUB Main()
    # The 2×2 area uses descending corners; bounds are normalized. row is one record. PrintTile is
    # fully defined and only prints numbers. For land, its hue argument is a placeholder 0; land
    # records contain no hue field.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArrayEx(x + 1, y + 1, x, y, map, types)
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        PrintTile(row[0], row[1], row[2], row[3], 0)
        i = i + 1
    WEND
END SUB

SUB PrintTile(graphic, x, y, z, hue)
    UO.Print("Type=" + CStr(graphic) + " X=" + CStr(x) + " Y=" + CStr(y))
    UO.Print("Z=" + CStr(z) + " hue=" + CStr(hue))
END SUB
```

**Parameter and execution notes:**

- The 2×2 area uses descending corners; bounds are normalized. row is one record. PrintTile is fully defined and only prints numbers. For land, its hue argument is a placeholder 0; land records contain no hue field.

### Poll with a bounded retry count

```vb
# Poll with a bounded retry count
#
# Finds land tiles by graphic/type in a rectangle.
#
# Array of [graphic, X, Y, Z] records, all Integer. graphic is the land type; Z is its base
# height. No matches: empty Array. Count records with GetArrayLength(result). Indexes start at
# 0. The result is not a Boolean, serial, or Pascal record; there is no seventh output
# parameter.

SUB Main()
    # At most three scans of one cell, with WAIT(250) between attempts. Every call produces a new
    # result. Zero length means no current matches, not permanent absence on the server.

    DIM types[1]
    types[0] = 0x0003
    types[1] = 0x0004
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR attempt = 0
    WHILE attempt < 3
        VAR rows = UO.GetLandTilesArrayEx(x, y, x, y, map, types)
        UO.Print("Records: " + CStr(GetArrayLength(rows)))
        attempt = attempt + 1
        WAIT(250)
    WEND
END SUB
```

**Parameter and execution notes:**

- At most three scans of one cell, with WAIT(250) between attempts. Every call produces a new result. Zero length means no current matches, not permanent absence on the server.
