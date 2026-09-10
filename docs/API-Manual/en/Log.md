# Log

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Computes the natural logarithm.

## Exact syntax

```text
Log(number:Any) -> Decimal
```

## Parameters

- `number` — Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible. Base e, not base 10. Log(1)=0, Log(0)=-Infinity, negative input gives NaN, positive infinity gives Infinity.

## Returns

Decimal — ln(number). Base e, not base 10. Log(1)=0, Log(0)=-Infinity, negative input gives NaN, positive infinity gives Infinity. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

## Behavior

- Runs locally on the script thread with no server request, movement, target, wait or global-variable change.
- Decimal is binary Double, not the .NET decimal type. Results may be approximate; compare finite floating results with a tolerance. Do not use infinite or NaN results as coordinates or item amounts.
- Base e, not base 10. Log(1)=0, Log(0)=-Infinity, negative input gives NaN, positive infinity gives Infinity.

### Internal functions: from call to result

These are the real registration/conversion stages. Complete helper functions below show useful script-level formulas; they do not replace the platform mathematics implementation.

#### 1. Register

Register binds the one-argument BASIC name to its native calculation. The binding calls System.Math after conversion; no hidden script or server procedure is run.

Decimal — ln(number). Base e, not base 10. Log(1)=0, Log(0)=-Infinity, negative input gives NaN, positive infinity gives Infinity. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

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
# Computes the natural logarithm.
#
# Decimal — ln(number). Base e, not base 10. Log(1)=0, Log(0)=-Infinity, negative input gives
# NaN, positive infinity gives Infinity. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

SUB Main()
    # number = 1; expected result 0 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR value = Log(1)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- number = 1; expected result 0 (~ means approximate). value stores the result and CStr only formats it for Print.

### A different input through a variable

```vb
# A different input through a variable
#
# Computes the natural logarithm.
#
# Decimal — ln(number). Base e, not base 10. Log(1)=0, Log(0)=-Infinity, negative input gives
# NaN, positive infinity gives Infinity. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

SUB Main()
    # number = 2.718281828459045; expected result ~1 (~ means approximate). value stores the result
    # and CStr only formats it for Print.

    VAR inputValue = 2.718281828459045
    VAR value = Log(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- number = 2.718281828459045; expected result ~1 (~ means approximate). value stores the result and CStr only formats it for Print.

### Complete reusable helper

```vb
# Complete reusable helper
#
# Computes the natural logarithm.
#
# Decimal — ln(number). Base e, not base 10. Log(1)=0, Log(0)=-Infinity, negative input gives
# NaN, positive infinity gives Infinity. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

# manual-check: scalar-math Log
SUB Main()
    # value>0 and baseValue>0, baseValue<>1. LogBase returns Log(value)/Log(baseValue);
    # LogBase(100,10)≈2. Invalid arguments return helper fallback 0, also a possible valid
    # logarithm.

    VAR value = LogBase(100,10)
    UO.Print(CStr(value))
END SUB

SUB LogBase(value,baseValue)
    IF value <= 0 OR baseValue <= 0 OR baseValue = 1 THEN
        RETURN 0
    END IF
    RETURN Log(value)/Log(baseValue)
END SUB
```

**Parameter and execution notes:**

- value>0 and baseValue>0, baseValue<>1. LogBase returns Log(value)/Log(baseValue); LogBase(100,10)≈2. Invalid arguments return helper fallback 0, also a possible valid logarithm.
