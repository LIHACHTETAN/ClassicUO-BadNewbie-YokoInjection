# UO.Random

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Selects one pseudorandom integer. Random(min,max) includes both bounds; the legacy Random(max) excludes its upper bound.

## Exact syntax

```text
UO.Random(max:Integer) -> Integer
UO.Random(min:Integer, max:Integer) -> Integer
```

## Parameters

- `min` — Lower bound, only in the two-argument form. Signed 32-bit integer from -2147483648 to 2147483647; must be <= max.
- `max` — Two arguments: inclusive upper bound, any signed 32-bit integer. One argument: exclusive upper bound, 0..2147483647. Random(0) returns 0.

## Returns

Integer — one selected number, not a Boolean or a serial. Two arguments: min <= result <= max. One positive argument: 0 <= result < max. Repeated values are allowed.

## Behavior

- No zero-argument form. Equal bounds return that value. Reversed bounds or a negative single argument raise a script error; bounds are not swapped.
- The full signed 32-bit range is supported without overflowing max+1. For scaled fractions, select integers and divide, for example Random(0,100)/100.0.
- The generator belongs to the script runtime; concurrent calls are synchronized. Random has no seed parameter and differs from BASIC Rnd. Save the result if it must be reused.
- The call is local and does not wait, move or send packets. Random coordinates still need map/path checks; an empty array has no index even though Random(0)=0.

## Examples

### Roll a die

```vb
# Roll a die
#
# Selects one pseudorandom integer. Random(min,max) includes both bounds; the legacy Random(max)
# excludes its upper bound.
#
# Integer — one selected number, not a Boolean or a serial. Two arguments: min <= result <= max.
# One positive argument: 0 <= result < max. Repeated values are allowed.

SUB Main()
    # min=1 and max=6 include all six values. roll stores one draw; STR converts it to text. A later
    # call may return the same value.

    VAR roll = UO.Random(1, 6)
    UO.Print(STR(roll))
END SUB
```

**Parameter and execution notes:**

- min=1 and max=6 include all six values. roll stores one draw; STR converts it to text. A later call may return the same value.

### Wait for a random interval

```vb
# Wait for a random interval
#
# Selects one pseudorandom integer. Random(min,max) includes both bounds; the legacy Random(max)
# excludes its upper bound.
#
# Integer — one selected number, not a Boolean or a serial. Two arguments: min <= result <= max.
# One positive argument: 0 <= result < max. Repeated values are allowed.

SUB Main()
    # min=350, max=700 are inclusive milliseconds. Random computes delay; UO.Wait(delay) performs
    # the wait. Keep any minimum delay required by the server.

    VAR delay = UO.Random(350, 700)
    UO.Print(STR(delay))
    UO.Wait(delay)
END SUB
```

**Parameter and execution notes:**

- min=350, max=700 are inclusive milliseconds. Random computes delay; UO.Wait(delay) performs the wait. Keep any minimum delay required by the server.

### Legacy indices and equal bounds

```vb
# Legacy indices and equal bounds
#
# Selects one pseudorandom integer. Random(min,max) includes both bounds; the legacy Random(max)
# excludes its upper bound.
#
# Integer — one selected number, not a Boolean or a serial. Two arguments: min <= result <= max.
# One positive argument: 0 <= result < max. Repeated values are allowed.

SUB Main()
    # Random(10) gives 0..9, never 10. Random(7,7) always gives 7. Random(-2,2) may give
    # -2,-1,0,1,2. Each expression is a separate draw.

    VAR index = UO.Random(10)
    VAR fixedValue = UO.Random(7, 7)
    VAR offset = UO.Random(-2, 2)
    UO.Print(STR(index) + ', ' + STR(fixedValue) + ', ' + STR(offset))
END SUB
```

**Parameter and execution notes:**

- Random(10) gives 0..9, never 10. Random(7,7) always gives 7. Random(-2,2) may give -2,-1,0,1,2. Each expression is a separate draw.
