# Exp

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Raises e to a power.

## Exact syntax

```text
Exp(power:Any) -> Decimal
```

## Parameters

- `power` — Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible. Exp(0)=1. Large positive exponents overflow to Infinity; very negative exponents underflow to 0. NaN stays NaN.

## Returns

Decimal — e^power. Exp(0)=1. Large positive exponents overflow to Infinity; very negative exponents underflow to 0. NaN stays NaN. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

## Behavior

- Runs locally on the script thread with no server request, movement, target, wait or global-variable change.
- Decimal is binary Double, not the .NET decimal type. Results may be approximate; compare finite floating results with a tolerance. Do not use infinite or NaN results as coordinates or item amounts.
- Exp(0)=1. Large positive exponents overflow to Infinity; very negative exponents underflow to 0. NaN stays NaN.

### Internal functions: from call to result

These are the real registration/conversion stages. Complete helper functions below show useful script-level formulas; they do not replace the platform mathematics implementation.

#### 1. Register

Register binds the one-argument BASIC name to its native calculation. The binding calls System.Math after conversion; no hidden script or server procedure is run.

Decimal — e^power. Exp(0)=1. Large positive exponents overflow to Infinity; very negative exponents underflow to 0. NaN stays NaN. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

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
# Raises e to a power.
#
# Decimal — e^power. Exp(0)=1. Large positive exponents overflow to Infinity; very negative
# exponents underflow to 0. NaN stays NaN. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

SUB Main()
    # power = 0; expected result 1 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR value = Exp(0)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- power = 0; expected result 1 (~ means approximate). value stores the result and CStr only formats it for Print.

### A different input through a variable

```vb
# A different input through a variable
#
# Raises e to a power.
#
# Decimal — e^power. Exp(0)=1. Large positive exponents overflow to Infinity; very negative
# exponents underflow to 0. NaN stays NaN. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

SUB Main()
    # power = 1; expected result ~2.718281828459045 (~ means approximate). value stores the result
    # and CStr only formats it for Print.

    VAR inputValue = 1
    VAR value = Exp(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- power = 1; expected result ~2.718281828459045 (~ means approximate). value stores the result and CStr only formats it for Print.

### Complete reusable helper

```vb
# Complete reusable helper
#
# Raises e to a power.
#
# Decimal — e^power. Exp(0)=1. Large positive exponents overflow to Infinity; very negative
# exponents underflow to 0. NaN stays NaN. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

# manual-check: scalar-math Exp
SUB Main()
    # value is the initial value, rate is continuous growth per time unit, period uses that unit.
    # Growth(100,0.05,2) is approximately 110.517; numeric example only.

    VAR value = Growth(100,0.05,2)
    UO.Print(CStr(value))
END SUB

SUB Growth(value,rate,period)
    RETURN value*Exp(rate*period)
END SUB
```

**Parameter and execution notes:**

- value is the initial value, rate is continuous growth per time unit, period uses that unit. Growth(100,0.05,2) is approximately 110.517; numeric example only.
