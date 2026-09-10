# UO.IsFrozen

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the paralysis flag currently known to the client for a mobile.

## Exact syntax

```text
UO.IsFrozen() -> Integer
UO.IsFrozen(value:Any) -> Integer
```

## Parameters

- `value` — Optional mobile serial/ID: integer, hexadecimal string, self, lasttarget, another standard object alias or an AddObject name. This is not graphic/type. Omit it to select self. An unresolved alias becomes 0; no target cursor is opened.

## Returns

Integer Boolean: 1 = TRUE when a loaded mobile has IsParalyzed; 0 = FALSE when the flag is absent, the mobile is unknown or destroyed, or the object is an item. It is not the remaining duration and 0 does not guarantee that movement is possible.

## Behavior

- Use Paralyzed to check the paralysis flag. The Is/Get variants, GetParalisa, Frozen and GetLocked read the same flag.
- This is a local query. It neither applies nor cures paralysis, waits for it to end, nor requests a server refresh.
- For this predicate, value = TRUE, value = 1 and IF value are equivalent. Write TRUE/FALSE without quotes. The result represents a flag, not a quantity or an ID.

## Examples

### Check self using TRUE

```vb
# Check self using TRUE
#
# Reads the paralysis flag currently known to the client for a mobile.
#
# Integer Boolean: 1 = TRUE when a loaded mobile has IsParalyzed; 0 = FALSE when the flag is
# absent, the mobile is unknown or destroyed, or the object is an item. It is not the remaining
# duration and 0 does not guarantee that movement is possible.

SUB Main()
    # Empty parentheses select self. state stores one flag snapshot; TRUE is the numeric constant 1.
    # FALSE does not rule out a wall, depleted stamina or another cause of blocked movement.

    VAR state = UO.IsFrozen()
    IF state = TRUE THEN
        UO.Print('Paralysis flag is set')
    ELSE
        UO.Print('Paralysis flag is absent or unavailable')
    END IF
END SUB
```

**Parameter and execution notes:**

- Empty parentheses select self. state stores one flag snapshot; TRUE is the numeric constant 1.
- FALSE does not rule out a wall, depleted stamina or another cause of blocked movement.

### Check a selected mobile

```vb
# Check a selected mobile
#
# Reads the paralysis flag currently known to the client for a mobile.
#
# Integer Boolean: 1 = TRUE when a loaded mobile has IsParalyzed; 0 = FALSE when the flag is
# absent, the mobile is unknown or destroyed, or the object is an item. It is not the remaining
# duration and 0 does not guarantee that movement is possible.

SUB Main()
    # target stores the last target serial as a hex string. IsNpc checks for a loaded mobile,
    # including players.
    # The argument selects that saved target. It does not open a cursor or change lasttarget.

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR state = UO.IsFrozen(target)
        UO.Print('Selected mobile paralysis 1/0: ' + STR(state))
    ELSE
        UO.Print('No loaded mobile selected')
    END IF
END SUB
```

**Parameter and execution notes:**

- target stores the last target serial as a hex string. IsNpc checks for a loaded mobile, including players.
- The argument selects that saved target. It does not open a cursor or change lasttarget.

### Wait for recovery with a limit

```vb
# Wait for recovery with a limit
#
# Reads the paralysis flag currently known to the client for a mobile.
#
# Integer Boolean: 1 = TRUE when a loaded mobile has IsParalyzed; 0 = FALSE when the flag is
# absent, the mobile is unknown or destroyed, or the object is an item. It is not the remaining
# duration and 0 does not guarantee that movement is possible.

SUB Main()
    # At most ten waits of 100 ms. Each zero-argument call reads self again.
    # After the loop, self is checked separately. This observes roughly one second plus execution
    # time; it does not guarantee recovery.

    VAR attempts = 0
    WHILE UO.IsFrozen() = TRUE AND attempts < 10
        WAIT(100)
        attempts = attempts + 1
    WEND
    IF UO.IsNpc('self') THEN
        IF UO.IsFrozen() = FALSE THEN
            UO.Print('Paralysis flag is clear')
        ELSE
            UO.Print('Still paralyzed')
        END IF
    ELSE
        UO.Print('Self is unavailable')
    END IF
END SUB
```

**Parameter and execution notes:**

- At most ten waits of 100 ms. Each zero-argument call reads self again.
- After the loop, self is checked separately. This observes roughly one second plus execution time; it does not guarantee recovery.
