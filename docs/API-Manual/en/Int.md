# Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Int(value) rounds a Basic number down toward negative infinity.

## Exact syntax

```text
Int(value:Any) -> Integer
```

## Parameters

- `value` — One required Integer/Decimal number or numeric string. Numeric text uses a dot independently of UI language. Unrecognized text, Array, Object and Unit are converted to 0; validate input with IsNumeric first.

## Returns

Integer: floor(value), e.g. 2.9 -> 2 and -2.9 -> -3. Keep the rounded value within signed Int32 limits; do not use non-finite or out-of-range inputs.

## Behavior

- Both functions run locally without game queries. A missing argument is an error. Int() and Str() are not character getters: use UO.Int() and UO.Str() for those attributes. Int dispatches through BasicDouble and Math.Floor; Str dispatches to the matching InternalSubrutines.Str overload with invariant formatting.

## Examples

### Int — 1

```vb
# Int — 1
#
# Int(value) rounds a Basic number down toward negative infinity.
#
# Integer: floor(value), e.g. 2.9 -> 2 and -2.9 -> -3. Keep the rounded value within signed
# Int32 limits; do not use non-finite or out-of-range inputs.

SUB Main()
    # value=2.9. Int discards the positive fractional part by rounding down; Main returns Integer 2.

    RETURN Int(2.9)
END SUB
```

**Parameter and execution notes:**

- value=2.9. Int discards the positive fractional part by rounding down; Main returns Integer 2.

### Int — 2

```vb
# Int — 2
#
# Int(value) rounds a Basic number down toward negative infinity.
#
# Integer: floor(value), e.g. 2.9 -> 2 and -2.9 -> -3. Keep the rounded value within signed
# Int32 limits; do not use non-finite or out-of-range inputs.

SUB Main()
    # value=-2.9. Rounding down moves to -3, whereas truncation toward zero would give -2. Main
    # returns Integer -3.

    VAR value = -2.9
    RETURN Int(value)
END SUB
```

**Parameter and execution notes:**

- value=-2.9. Rounding down moves to -3, whereas truncation toward zero would give -2. Main returns Integer -3.

### Int — 3

```vb
# Int — 3
#
# Int(value) rounds a Basic number down toward negative infinity.
#
# Integer: floor(value), e.g. 2.9 -> 2 and -2.9 -> -3. Keep the rounded value within signed
# Int32 limits; do not use non-finite or out-of-range inputs.

SUB Main()
    # WholeUnits receives total=27 and size=5. Nonpositive size returns 0; otherwise Int(total/size)
    # rounds 5.4 down. Main returns 5 complete units. The helper and its two parameters are defined
    # in full.

    RETURN WholeUnits(27,5)
END SUB

SUB WholeUnits(total,size)
    IF size <= 0 THEN
        RETURN 0
    END IF
    RETURN Int(total/size)
END SUB
```

**Parameter and execution notes:**

- WholeUnits receives total=27 and size=5. Nonpositive size returns 0; otherwise Int(total/size) rounds 5.4 down. Main returns 5 complete units. The helper and its two parameters are defined in full.
