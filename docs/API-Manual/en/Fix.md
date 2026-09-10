# Fix

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Discards the fractional part towards zero.

## Exact syntax

```text
Fix(value:Any) -> Integer
```

## Parameters

- `value` — Required numeric Integer/Decimal or decimal text with a dot and optional exponent, e.g. "-1.25e2". UI language does not affect parsing. Invalid text (including hexadecimal text), Unit, Array and Object become 0; numeric hexadecimal literals are already Integer values. NaN/Infinity are possible. Finite input only, with truncated result in -2147483648..2147483647. -2.9 becomes -2, unlike floor(-2.9)=-3. Out-of-range and NaN/Infinity are not valid conversion inputs.

## Returns

Integer — truncate(value). Finite input only, with truncated result in -2147483648..2147483647. -2.9 becomes -2, unlike floor(-2.9)=-3. Out-of-range and NaN/Infinity are not valid conversion inputs. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

## Behavior

- Runs locally on the script thread with no server request, movement, target, wait or global-variable change.
- Decimal is binary Double, not the .NET decimal type. Results may be approximate; compare finite floating results with a tolerance. Do not use infinite or NaN results as coordinates or item amounts.
- Finite input only, with truncated result in -2147483648..2147483647. -2.9 becomes -2, unlike floor(-2.9)=-3. Out-of-range and NaN/Infinity are not valid conversion inputs.

### Internal functions: from call to result

These are the real registration/conversion stages. Complete helper functions below show useful script-level formulas; they do not replace the platform mathematics implementation.

#### 1. Register

Register binds the one-argument BASIC name to its native calculation. The binding calls System.Math after conversion; no hidden script or server procedure is run.

Integer — truncate(value). Finite input only, with truncated result in -2147483648..2147483647. -2.9 becomes -2, unlike floor(-2.9)=-3. Out-of-range and NaN/Infinity are not valid conversion inputs. A numeric result, not an ID or a success flag; do not interpret 1/0 as success/failure here.

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
# Discards the fractional part towards zero.
#
# Integer — truncate(value). Finite input only, with truncated result in
# -2147483648..2147483647. -2.9 becomes -2, unlike floor(-2.9)=-3. Out-of-range and NaN/Infinity
# are not valid conversion inputs. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

SUB Main()
    # value = 2.9; expected result 2 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR value = Fix(2.9)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- value = 2.9; expected result 2 (~ means approximate). value stores the result and CStr only formats it for Print.

### A different input through a variable

```vb
# A different input through a variable
#
# Discards the fractional part towards zero.
#
# Integer — truncate(value). Finite input only, with truncated result in
# -2147483648..2147483647. -2.9 becomes -2, unlike floor(-2.9)=-3. Out-of-range and NaN/Infinity
# are not valid conversion inputs. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

SUB Main()
    # value = -2.9; expected result -2 (~ means approximate). value stores the result and CStr only
    # formats it for Print.

    VAR inputValue = -2.9
    VAR value = Fix(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- value = -2.9; expected result -2 (~ means approximate). value stores the result and CStr only formats it for Print.

### Complete reusable helper

```vb
# Complete reusable helper
#
# Discards the fractional part towards zero.
#
# Integer — truncate(value). Finite input only, with truncated result in
# -2147483648..2147483647. -2.9 becomes -2, unlike floor(-2.9)=-3. Out-of-range and NaN/Infinity
# are not valid conversion inputs. A numeric result, not an ID or a success flag; do not
# interpret 1/0 as success/failure here.

# manual-check: scalar-math Fix
SUB Main()
    # total>=0 and size>0 define complete batches; 27/5 gives 5. Invalid inputs return helper value
    # 0, also valid for no complete batch. Keep the quotient within Integer range.

    VAR value = WholeBatches(27,5)
    UO.Print(CStr(value))
END SUB

SUB WholeBatches(total,size)
    IF total < 0 OR size <= 0 THEN
        RETURN 0
    END IF
    RETURN Fix(CDbl(total)/CDbl(size))
END SUB
```

**Parameter and execution notes:**

- total>=0 and size>0 define complete batches; 27/5 gives 5. Invalid inputs return helper value 0, also valid for no complete batch. Keep the quotient within Integer range.
