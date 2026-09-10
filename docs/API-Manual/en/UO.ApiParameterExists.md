# UO.ApiParameterExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Tests whether an intrinsic value or object selector is registered.

## Exact syntax

```text
UO.ApiParameterExists(name:String) -> Integer
```

## Parameters

- `name` — Required String: exact registered name, not a call expression. Case and outer spaces are ignored; UO. is never added automatically. Empty or unknown names return 0. User procedures are not included.

## Returns

Integer 1 if the registration exists, otherwise 0. You may compare with TRUE/FALSE or 1/0. This does not confirm a game object, successful action or server permission.

## Behavior

- Names are case-insensitive. InjectionApi registers the bare Basic library; InjectionApiUO registers game calls with UO. The analyzer reports SC005 for a removed short call and suggests a registered UO. replacement. No fallback executes that old call. Character getter values also require UO. ApiNameExists, ApiSignatureExists and ApiParameterExists trim surrounding spaces and check the exact registered name without adding a prefix. They inspect metadata, not server state. The engine does not implement the VB.NET reflection operator GetType(TypeName).

## Examples

### UO.ApiParameterExists — 1

```vb
# UO.ApiParameterExists — 1
#
# Tests whether an intrinsic value or object selector is registered.
#
# Integer 1 if the registration exists, otherwise 0. You may compare with TRUE/FALSE or 1/0.
# This does not confirm a game object, successful action or server permission.

SUB Main()
    # The first example checks an explicitly qualified game API name and returns 1. The exact
    # queried name and argument count, when needed, are visible in the call.

    RETURN UO.ApiParameterExists('UO.GetHP')
END SUB
```

**Parameter and execution notes:**

- The first example checks an explicitly qualified game API name and returns 1. The exact queried name and argument count, when needed, are visible in the call.

### UO.ApiParameterExists — 2

```vb
# UO.ApiParameterExists — 2
#
# Tests whether an intrinsic value or object selector is registered.
#
# Integer 1 if the registration exists, otherwise 0. You may compare with TRUE/FALSE or 1/0.
# This does not confirm a game object, successful action or server permission.

SUB Main()
    # The second example checks Basic or a retained argument selector. Int(value) exists, Int() does
    # not; backpack is a selector. The script returns 1 or "1:0" as shown by its calls.

    VAR name = 'backpack'
    RETURN UO.ApiParameterExists(name)
END SUB
```

**Parameter and execution notes:**

- The second example checks Basic or a retained argument selector. Int(value) exists, Int() does not; backpack is a selector. The script returns 1 or "1:0" as shown by its calls.

### UO.ApiParameterExists — 3

```vb
# UO.ApiParameterExists — 3
#
# Tests whether an intrinsic value or object selector is registered.
#
# Integer 1 if the registration exists, otherwise 0. You may compare with TRUE/FALSE or 1/0.
# This does not confirm a game object, successful action or server permission.

SUB Main()
    # The third example defines the helper completely. It compares a removed short form or
    # unsupported arity with a supported form. Parameters name, first, second and count pass the
    # queried names/count unchanged. The result is 0 for the callable checks and "0:1" for the value
    # check.

    RETURN CompareNames('GetHP','UO.GetHP')
END SUB

FUNCTION CompareNames(first,second)
    RETURN CStr(UO.ApiParameterExists(first)) + ":" + CStr(UO.ApiParameterExists(second))
END FUNCTION
```

**Parameter and execution notes:**

- The third example defines the helper completely. It compares a removed short form or unsupported arity with a supported form. Parameters name, first, second and count pass the queried names/count unchanged. The result is 0 for the callable checks and "0:1" for the value check.
