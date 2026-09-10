# Abs

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Returns the absolute value.

## Exact syntax

```text
Abs(value:Any) -> Any
```

## Parameters

- `value` — Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible. Integer input stays Integer except -2147483648, whose magnitude is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces positive infinity.

## Returns

Integer/Decimal — abs(value). Integer input stays Integer except -2147483648, whose magnitude is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces positive infinity. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

## Behavior

- Runs locally on the script thread with no server request, movement, target, wait or global-variable change.
- Decimal is binary Double, not the .NET decimal type. Results may be approximate; compare finite floating results with a tolerance. Do not use infinite or NaN results as coordinates or item amounts.
- Integer input stays Integer except -2147483648, whose magnitude is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces positive infinity.

### Internal functions: from call to result

These are the real registration/conversion stages. Complete helper functions below show useful script-level formulas; they do not replace the platform mathematics implementation.

#### 1. Register

Register binds the one-argument BASIC name to its native calculation. The binding calls System.Math after conversion; no hidden script or server procedure is run.

Integer/Decimal — abs(value). Integer input stays Integer except -2147483648, whose magnitude is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces positive infinity. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; function `Register`.

#### 2. BasicDouble

BasicDouble preserves numeric Integer/Decimal, parses text with invariant NumberStyles.Float and returns 0 for unsupported values. Abs handles ordinary Integer input directly before its Double fallback.

Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; function `BasicDouble`.

#### 3. BasicAbs

Integer input stays Integer except -2147483648, whose magnitude is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces positive infinity.

Integer/Decimal — abs(value). Integer input stays Integer except -2147483648, whose magnitude is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces positive infinity. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; function `BasicAbs`.

Runs locally on the script thread with no server request, movement, target, wait or global-variable change.


## Examples

### Direct calculation

```vb
# Direct calculation
#
# Returns the absolute value.
#
# Integer/Decimal — abs(value). Integer input stays Integer except -2147483648, whose magnitude
# is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces
# positive infinity. A numeric result, not an ID or a success flag; do not interpret 1/0 as
# success/failure here.

SUB Main()
    # value = -12; expected result 12 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR value = Abs(-12)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- value = -12; expected result 12 (~ means approximate). value stores the result and CStr only formats it for Print.

### A different input through a variable

```vb
# A different input through a variable
#
# Returns the absolute value.
#
# Integer/Decimal — abs(value). Integer input stays Integer except -2147483648, whose magnitude
# is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces
# positive infinity. A numeric result, not an ID or a success flag; do not interpret 1/0 as
# success/failure here.

SUB Main()
    # value = '-2.5'; expected result 2.5 (~ means approximate). value stores the result and CStr
    # only formats it for Print.

    VAR inputValue = '-2.5'
    VAR value = Abs(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- value = '-2.5'; expected result 2.5 (~ means approximate). value stores the result and CStr only formats it for Print.

### Complete reusable helper

```vb
# Complete reusable helper
#
# Returns the absolute value.
#
# Integer/Decimal — abs(value). Integer input stays Integer except -2147483648, whose magnitude
# is Decimal 2147483648. Decimal/text produce Decimal. NaN remains NaN; either infinity produces
# positive infinity. A numeric result, not an ID or a success flag; do not interpret 1/0 as
# success/failure here.

# manual-check: scalar-math Abs
SUB Main()
    # value/target are numbers, tolerance is a nonnegative allowed deviation. IsWithin returns 1/0;
    # a negative tolerance returns 0. Only this helper result is Boolean.

    VAR value = IsWithin(12,10,2)
    UO.Print(CStr(value))
END SUB

SUB IsWithin(value,target,tolerance)
    IF tolerance < 0 THEN
        RETURN 0
    END IF
    RETURN Abs(CDbl(value)-CDbl(target)) <= tolerance
END SUB
```

**Parameter and execution notes:**

- value/target are numbers, tolerance is a nonnegative allowed deviation. IsWithin returns 1/0; a negative tolerance returns 0. Only this helper result is Boolean.
