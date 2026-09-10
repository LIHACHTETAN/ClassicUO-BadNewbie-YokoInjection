# Cos

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Computes cosine.

## Exact syntax

```text
Cos(radians:Any) -> Decimal
```

## Parameters

- `radians` — Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible. Input is radians, not degrees or a game direction. Finite result lies in [-1,1]; NaN or infinite input yields NaN.

## Returns

Decimal — cos(radians). Input is radians, not degrees or a game direction. Finite result lies in [-1,1]; NaN or infinite input yields NaN. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

## Behavior

- Runs locally on the script thread with no server request, movement, target, wait or global-variable change.
- Decimal is binary Double, not the .NET decimal type. Results may be approximate; compare finite floating results with a tolerance. Do not use infinite or NaN results as coordinates or item amounts.
- Input is radians, not degrees or a game direction. Finite result lies in [-1,1]; NaN or infinite input yields NaN.

### Internal functions: from call to result

These are the real registration/conversion stages. Complete helper functions below show useful script-level formulas; they do not replace the platform mathematics implementation.

#### 1. Register

Register binds the one-argument BASIC name to its native calculation. The binding calls System.Math after conversion; no hidden script or server procedure is run.

Decimal — cos(radians). Input is radians, not degrees or a game direction. Finite result lies in [-1,1]; NaN or infinite input yields NaN. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

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
# Computes cosine.
#
# Decimal — cos(radians). Input is radians, not degrees or a game direction. Finite result lies
# in [-1,1]; NaN or infinite input yields NaN. A numeric result, not an ID or a success flag; do
# not interpret 1/0 as success/failure here.

SUB Main()
    # radians = 0; expected result 1 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR value = Cos(0)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- radians = 0; expected result 1 (~ means approximate). value stores the result and CStr only formats it for Print.

### A different input through a variable

```vb
# A different input through a variable
#
# Computes cosine.
#
# Decimal — cos(radians). Input is radians, not degrees or a game direction. Finite result lies
# in [-1,1]; NaN or infinite input yields NaN. A numeric result, not an ID or a success flag; do
# not interpret 1/0 as success/failure here.

SUB Main()
    # radians = 3.141592653589793; expected result ~-1 (~ means approximate). value stores the
    # result and CStr only formats it for Print.

    VAR inputValue = 3.141592653589793
    VAR value = Cos(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- radians = 3.141592653589793; expected result ~-1 (~ means approximate). value stores the result and CStr only formats it for Print.

### Complete reusable helper

```vb
# Complete reusable helper
#
# Computes cosine.
#
# Decimal — cos(radians). Input is radians, not degrees or a game direction. Finite result lies
# in [-1,1]; NaN or infinite input yields NaN. A numeric result, not an ID or a success flag; do
# not interpret 1/0 as success/failure here.

# manual-check: scalar-math Cos
SUB Main()
    # degrees is an angle in degrees; multiplying by pi/180 gives radians before Cos.
    # CosineDegrees(60) is approximately 0.5.

    VAR value = CosineDegrees(60)
    UO.Print(CStr(value))
END SUB

SUB CosineDegrees(degrees)
    RETURN Cos(degrees*3.141592653589793/180)
END SUB
```

**Parameter and execution notes:**

- degrees is an angle in degrees; multiplying by pi/180 gives radians before Cos. CosineDegrees(60) is approximately 0.5.
