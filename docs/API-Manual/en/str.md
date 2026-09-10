# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Str(value) formats a Basic scalar as text.

## Exact syntax

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## Parameters

- `value` — One required Integer, Decimal or String. The overload is selected from the actual value kind. Array, Object and Unit have no matching Str overload.

## Returns

String: invariant numeric text, or the original String unchanged. Positive numbers get no leading space. No rounding-precision argument is available.

## Behavior

- Both functions run locally without game queries. A missing argument is an error. Int() and Str() are not character getters: use UO.Int() and UO.Str() for those attributes. Int dispatches through BasicDouble and Math.Floor; Str dispatches to the matching InternalSubrutines.Str overload with invariant formatting.

## Examples

### Str — 1

```vb
# Str — 1
#
# Str(value) formats a Basic scalar as text.
#
# String: invariant numeric text, or the original String unchanged. Positive numbers get no
# leading space. No rounding-precision argument is available.

SUB Main()
    # value=42 is an Integer. Str returns "42" without a leading blank; Main returns that String.

    RETURN Str(42)
END SUB
```

**Parameter and execution notes:**

- value=42 is an Integer. Str returns "42" without a leading blank; Main returns that String.

### Str — 2

```vb
# Str — 2
#
# Str(value) formats a Basic scalar as text.
#
# String: invariant numeric text, or the original String unchanged. Positive numbers get no
# leading space. No rounding-precision argument is available.

SUB Main()
    # amount=-12.5 is Decimal. Str stores "-12.5" in text with a dot for every UI language. Main
    # returns text; the original amount stays numeric.

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**Parameter and execution notes:**

- amount=-12.5 is Decimal. Str stores "-12.5" in text with a dot for every UI language. Main returns text; the original amount stays numeric.

### Str — 3

```vb
# Str — 3
#
# Str(value) formats a Basic scalar as text.
#
# String: invariant numeric text, or the original String unchanged. Positive numbers get no
# leading space. No rounding-precision argument is available.

SUB Main()
    # ItemLabel takes name="ore" and count=3. Str(name) preserves the name; Str(count) produces "3".
    # The helper joins both Strings with " x" and Main returns "ore x3".

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**Parameter and execution notes:**

- ItemLabel takes name="ore" and count=3. Str(name) preserves the name; Str(count) produces "3". The helper joins both Strings with " x" and Main returns "ore x3".
