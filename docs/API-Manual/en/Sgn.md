# Sgn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Returns the sign of a number.

## Exact syntax

```text
Sgn(value:Any) -> Integer
```

## Parameters

- `value` — Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible. -1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical error; infinities return their sign.

## Returns

Integer — sign(value). -1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical error; infinities return their sign. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

## Behavior

- Runs locally on the script thread with no server request, movement, target, wait or global-variable change.
- Decimal is binary Double, not the .NET decimal type. Results may be approximate; compare finite floating results with a tolerance. Do not use infinite or NaN results as coordinates or item amounts.
- -1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical error; infinities return their sign.

### Internal functions: from call to result

These are the real registration/conversion stages. Complete helper functions below show useful script-level formulas; they do not replace the platform mathematics implementation.

#### 1. Register

Register binds the one-argument BASIC name to its native calculation. The binding calls System.Math after conversion; no hidden script or server procedure is run.

Integer — sign(value). -1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical error; infinities return their sign. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; function `Register`.

#### 2. BasicDouble

BasicDouble preserves numeric Integer/Decimal, parses text with invariant NumberStyles.Float and returns 0 for unsupported values. Abs handles ordinary Integer input directly before its Double fallback.

Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; function `BasicDouble`.

#### 3. BasicSgn

-1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical error; infinities return their sign.

Integer — sign(value). -1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical error; infinities return their sign. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; function `BasicSgn`.

Runs locally on the script thread with no server request, movement, target, wait or global-variable change.


## Examples

### Direct calculation

```vb
# Direct calculation
#
# Returns the sign of a number.
#
# Integer — sign(value). -1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical
# error; infinities return their sign. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

SUB Main()
    # value = -8; expected result -1 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR value = Sgn(-8)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- value = -8; expected result -1 (~ means approximate). value stores the result and CStr only formats it for Print.

### A different input through a variable

```vb
# A different input through a variable
#
# Returns the sign of a number.
#
# Integer — sign(value). -1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical
# error; infinities return their sign. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

SUB Main()
    # value = 10-10; expected result 0 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR inputValue = 10-10
    VAR value = Sgn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- value = 10-10; expected result 0 (~ means approximate). value stores the result and CStr only formats it for Print.

### Complete reusable helper

```vb
# Complete reusable helper
#
# Returns the sign of a number.
#
# Integer — sign(value). -1 for negative, 0 for zero, +1 for positive. NaN raises a mathematical
# error; infinities return their sign. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

# manual-check: scalar-math Sgn
SUB Main()
    # current/destination define a scalar displacement. StepToward returns -1/0/1, not an eight-way
    # direction; it does not move.

    VAR value = StepToward(12,10)
    UO.Print(CStr(value))
END SUB

SUB StepToward(current,destination)
    RETURN Sgn(CDbl(destination)-CDbl(current))
END SUB
```

**Parameter and execution notes:**

- current/destination define a scalar displacement. StepToward returns -1/0/1, not an eight-way direction; it does not move.
