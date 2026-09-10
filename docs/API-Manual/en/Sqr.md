# Sqr

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Computes a square root.

## Exact syntax

```text
Sqr(number:Any) -> Decimal
```

## Parameters

- `number` — Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible. For input >=0 returns its nonnegative square root. Negative input gives NaN, positive infinity gives Infinity, NaN stays NaN.

## Returns

Decimal — sqrt(number). For input >=0 returns its nonnegative square root. Negative input gives NaN, positive infinity gives Infinity, NaN stays NaN. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

## Behavior

- Runs locally on the script thread with no server request, movement, target, wait or global-variable change.
- Decimal is binary Double, not the .NET decimal type. Results may be approximate; compare finite floating results with a tolerance. Do not use infinite or NaN results as coordinates or item amounts.
- For input >=0 returns its nonnegative square root. Negative input gives NaN, positive infinity gives Infinity, NaN stays NaN.

### Internal functions: from call to result

These are the real registration/conversion stages. Complete helper functions below show useful script-level formulas; they do not replace the platform mathematics implementation.

#### 1. Register

Register binds the one-argument BASIC name to its native calculation. The binding calls System.Math after conversion; no hidden script or server procedure is run.

Decimal — sqrt(number). For input >=0 returns its nonnegative square root. Negative input gives NaN, positive infinity gives Infinity, NaN stays NaN. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

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
# Computes a square root.
#
# Decimal — sqrt(number). For input >=0 returns its nonnegative square root. Negative input
# gives NaN, positive infinity gives Infinity, NaN stays NaN. A numeric result, not an ID or a
# success flag; do not interpret 1/0 as success/failure here.

SUB Main()
    # number = 25; expected result 5 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR value = Sqr(25)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- number = 25; expected result 5 (~ means approximate). value stores the result and CStr only formats it for Print.

### A different input through a variable

```vb
# A different input through a variable
#
# Computes a square root.
#
# Decimal — sqrt(number). For input >=0 returns its nonnegative square root. Negative input
# gives NaN, positive infinity gives Infinity, NaN stays NaN. A numeric result, not an ID or a
# success flag; do not interpret 1/0 as success/failure here.

SUB Main()
    # number = 2; expected result ~1.4142135623730951 (~ means approximate). value stores the result
    # and CStr only formats it for Print.

    VAR inputValue = 2
    VAR value = Sqr(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- number = 2; expected result ~1.4142135623730951 (~ means approximate). value stores the result and CStr only formats it for Print.

### Complete reusable helper

```vb
# Complete reusable helper
#
# Computes a square root.
#
# Decimal — sqrt(number). For input >=0 returns its nonnegative square root. Negative input
# gives NaN, positive infinity gives Infinity, NaN stays NaN. A numeric result, not an ID or a
# success flag; do not interpret 1/0 as success/failure here.

# manual-check: scalar-math Sqr
SUB Main()
    # dx/dy are coordinate differences. CDbl prevents integer multiplication overflow before
    # sqrt(dx²+dy²); SegmentLength(3,4)=5. This Euclidean length is not a path length or collision
    # check.

    VAR value = SegmentLength(3,4)
    UO.Print(CStr(value))
END SUB

SUB SegmentLength(dx,dy)
    VAR x = CDbl(dx)
    VAR y = CDbl(dy)
    RETURN Sqr(x*x+y*y)
END SUB
```

**Parameter and execution notes:**

- dx/dy are coordinate differences. CDbl prevents integer multiplication overflow before sqrt(dx²+dy²); SegmentLength(3,4)=5. This Euclidean length is not a path length or collision check.
