# Atn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Computes arctangent.

## Exact syntax

```text
Atn(number:Any) -> Decimal
```

## Parameters

- `number` — Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible. Input is a slope, output radians in [-pi/2,pi/2]; infinite slopes give the endpoints, NaN stays NaN. This is not two-coordinate atan2.

## Returns

Decimal — atan(number). Input is a slope, output radians in [-pi/2,pi/2]; infinite slopes give the endpoints, NaN stays NaN. This is not two-coordinate atan2. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

## Behavior

- Runs locally on the script thread with no server request, movement, target, wait or global-variable change.
- Decimal is binary Double, not the .NET decimal type. Results may be approximate; compare finite floating results with a tolerance. Do not use infinite or NaN results as coordinates or item amounts.
- Input is a slope, output radians in [-pi/2,pi/2]; infinite slopes give the endpoints, NaN stays NaN. This is not two-coordinate atan2.

### Internal functions: from call to result

These are the real registration/conversion stages. Complete helper functions below show useful script-level formulas; they do not replace the platform mathematics implementation.

#### 1. Register

Register binds the one-argument BASIC name to its native calculation. The binding calls System.Math after conversion; no hidden script or server procedure is run.

Decimal — atan(number). Input is a slope, output radians in [-pi/2,pi/2]; infinite slopes give the endpoints, NaN stays NaN. This is not two-coordinate atan2. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; function `Register`.

#### 2. BasicDouble

BasicDouble preserves numeric Integer/Decimal, parses text with invariant NumberStyles.Float and returns 0 for unsupported values. Abs handles ordinary Integer input directly before its Double fallback.

Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; function `BasicDouble`.

Runs locally on the script thread with no server request, movement, target, wait or global-variable change.


## Examples

### Direct calculation

```vb
# Direct calculation
#
# Computes arctangent.
#
# Decimal — atan(number). Input is a slope, output radians in [-pi/2,pi/2]; infinite slopes give
# the endpoints, NaN stays NaN. This is not two-coordinate atan2. A numeric result, not an ID or
# a success flag; do not interpret 1/0 as success/failure here.

SUB Main()
    # number = 0; expected result 0 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR value = Atn(0)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- number = 0; expected result 0 (~ means approximate). value stores the result and CStr only formats it for Print.

### A different input through a variable

```vb
# A different input through a variable
#
# Computes arctangent.
#
# Decimal — atan(number). Input is a slope, output radians in [-pi/2,pi/2]; infinite slopes give
# the endpoints, NaN stays NaN. This is not two-coordinate atan2. A numeric result, not an ID or
# a success flag; do not interpret 1/0 as success/failure here.

SUB Main()
    # number = 1; expected result ~0.7853981633974483 (~ means approximate). value stores the result
    # and CStr only formats it for Print.

    VAR inputValue = 1
    VAR value = Atn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- number = 1; expected result ~0.7853981633974483 (~ means approximate). value stores the result and CStr only formats it for Print.

### Complete reusable helper

```vb
# Complete reusable helper
#
# Computes arctangent.
#
# Decimal — atan(number). Input is a slope, output radians in [-pi/2,pi/2]; infinite slopes give
# the endpoints, NaN stays NaN. This is not two-coordinate atan2. A numeric result, not an ID or
# a success flag; do not interpret 1/0 as success/failure here.

# manual-check: scalar-math Atn
SUB Main()
    # rise/run is a slope. run=0 returns helper fallback 0, not a vertical angle. SlopeDegrees(1,1)
    # is approximately 45; it does not resolve all quadrants.

    VAR value = SlopeDegrees(1,1)
    UO.Print(CStr(value))
END SUB

SUB SlopeDegrees(rise,run)
    IF run = 0 THEN
        RETURN 0
    END IF
    RETURN Atn(CDbl(rise)/CDbl(run))*180/3.141592653589793
END SUB
```

**Parameter and execution notes:**

- rise/run is a slope. run=0 returns helper fallback 0, not a vertical angle. SlopeDegrees(1,1) is approximately 45; it does not resolve all quadrants.
