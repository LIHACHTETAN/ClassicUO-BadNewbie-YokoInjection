# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads structured object properties, including each cliloc ID and its substitution parameters.

## Exact syntax

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## Parameters

- `ObjID` — Required object serial, not a graphic/type or a cliloc ID. Accepts an integer, decimal/hex string, self, backpack, lasttarget, finditem or an AddObject name. 0 selects no object.

## Returns

Array<Array>: each row is [clilocID:Integer, parameters:Array<String>]. rows[i][0] is the message ID; rows[i][1] is its parameter array. GetArrayLength(rows) counts properties. An empty array means no received records or ObjID=0. These are not item serials.

## Behavior

- Cached data returns immediately. Missing OPL triggers a request and a wait of up to 120 ms, interrupted by procedure cancellation. A known empty OPL returns immediately.
- This BASIC array represents the external TClilocRec structure: Count is GetArrayLength(rows), and Items are the rows. Leading transport tabs are skipped; empty interior arguments retain their positions. #number stays a string for localization. Missing parameters produce an empty array. Editing the snapshot does not edit the client cache.
- https://stealth.od.ua/api/GetTooltipRec/

## Examples

### List property IDs

```vb
# List property IDs
#
# Reads structured object properties, including each cliloc ID and its substitution parameters.
#
# Array<Array>: each row is [clilocID:Integer, parameters:Array<String>]. rows[i][0] is the
# message ID; rows[i][1] is its parameter array. GetArrayLength(rows) counts properties. An
# empty array means no received records or ObjID=0. These are not item serials.

SUB Main()
    # ObjID=lasttarget selects the object. i starts at 0; row[0] is a cliloc ID. An empty array
    # skips the loop.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**Parameter and execution notes:**

- ObjID=lasttarget selects the object. i starts at 0; row[0] is a cliloc ID. An empty array skips the loop.

### Localize every property

```vb
# Localize every property
#
# Reads structured object properties, including each cliloc ID and its substitution parameters.
#
# Array<Array>: each row is [clilocID:Integer, parameters:Array<String>]. rows[i][0] is the
# message ID; rows[i][1] is its parameter array. GetArrayLength(rows) counts properties. An
# empty array means no received records or ObjID=0. These are not item serials.

SUB Main()
    # GetClilocByID receives row[0] as ClilocID and row[1] as Params, preserving parameter order. Do
    # not pass the complete row as Params.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR text = UO.GetClilocByID(row[0], row[1])
        UO.Print(text)
        i = i + 1
    WEND
END SUB
```

**Parameter and execution notes:**

- GetClilocByID receives row[0] as ClilocID and row[1] as Params, preserving parameter order. Do not pass the complete row as Params.

### Read a numeric property

```vb
# Read a numeric property
#
# Reads structured object properties, including each cliloc ID and its substitution parameters.
#
# Array<Array>: each row is [clilocID:Integer, parameters:Array<String>]. rows[i][0] is the
# message ID; rows[i][1] is its parameter array. GetArrayLength(rows) counts properties. An
# empty array means no received records or ObjID=0. These are not item serials.

SUB Main()
    # wanted=1060401 is an example property ID; replace it. args[0] is a String. Check array length
    # and IsNumeric before Val; a parameter may contain text or #cliloc.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR wanted = 1060401
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR args = row[1]
        IF row[0] = wanted AND GetArrayLength(args) > 0 THEN
            IF IsNumeric(args[0]) THEN
                UO.Print('Value: ' + STR(Val(args[0])))
            END IF
        END IF
        i = i + 1
    WEND
END SUB
```

**Parameter and execution notes:**

- wanted=1060401 is an example property ID; replace it. args[0] is a String. Check array length and IsNumeric before Val; a parameter may contain text or #cliloc.
