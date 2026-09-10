# UO.GetDead

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Checks whether a mobile is dead.

## Exact syntax

```text
UO.GetDead() -> Integer
UO.GetDead(value:Any) -> Integer
```

## Parameters

- `value` — Optional object in the displayed overloads: numeric/hex-string serial, self, lasttarget or a registered AddObject name. This is not a type. Omission reads self. Unknown text causes a conversion error in some overloads; validate the name first.

## Returns

Integer Boolean: 1 = TRUE, 0 = FALSE. Compare with numbers or unquoted logical constants. 1 means the mobile has IsDead; 0 means no such state or no mobile. HP=0 alone does not mean death.

This is a logical result: 1 = TRUE, 0 = FALSE. After VAR result = command(...), use IF result = TRUE THEN or IF result = 1 THEN; for a negative result, IF result = FALSE THEN or IF result = 0 THEN. Do not quote TRUE/FALSE. Call once and save the result: another call can repeat the action or read changed state.

## Behavior

- Reads the local model: no target, status request, flag change or outgoing packet. A destroyed object is absent even before its dictionary entry is removed.
- Each result is a separate read. The world may change between Exists and the next call; several queries do not form an atomic snapshot.

### Internal functions: from call to result

These are actual internal C# stages. ReadState is a fully defined helper in the example, not an undocumented built-in command.

#### 1. RegisterCharacterGetterAliases

At runtime creation, RegisterCharacterGetterAliases registers names and overloads. Omission selects bridge.Self; an argument selects its serial. Existing registrations are retained.

1 means the mobile has IsDead; 0 means no such state or no mobile. HP=0 alone does not mean death.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject resolves numbers, hex strings and saved names. An AddObject name is resolved again on each call; this neither searches graphic/type nor opens an interactive selector.

Optional object in the displayed overloads: numeric/hex-string serial, self, lasttarget or a registered AddObject name. This is not a type. Omission reads self. Unknown text causes a conversion error in some overloads; validate the name first.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `TryGetObject`.

#### 3. Invoke

Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.

Each result is a separate read. The world may change between Exists and the next call; several queries do not form an atomic snapshot.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 4. Get

World.Get resolves the serial and returns null for IsDestroyed, then the Mobile flag is read. Alive checks Exists and absence of IsDead; items are allowed. The self Dead query reads Player.IsDead.

1 means the mobile has IsDead; 0 means no such state or no mobile. HP=0 alone does not mean death.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Get`.

Reads the local model: no target, status request, flag change or outgoing packet. A destroyed object is absent even before its dictionary entry is removed.


## Examples

### Check the player state

```vb
# Check the player state
#
# Checks whether a mobile is dead.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Compare with numbers or unquoted logical constants. 1
# means the mobile has IsDead; 0 means no such state or no mobile. HP=0 alone does not mean
# death.
#
# This is a logical result: 1 = TRUE, 0 = FALSE. After VAR result = command(...), use IF result
# = TRUE THEN or IF result = 1 THEN; for a negative result, IF result = FALSE THEN or IF result
# = 0 THEN. Do not quote TRUE/FALSE. Call once and save the result: another call can repeat the
# action or read changed state.

SUB Main()
    # Empty parentheses read self. active stores one result; TRUE and FALSE select the two branches.
    # Print only displays an example message.

    VAR active = UO.GetDead()
    IF active = TRUE THEN
        UO.Print('State is active')
    ELSE
        UO.Print('State is inactive or unavailable')
    END IF
END SUB
```

**Parameter and execution notes:**

- Empty parentheses read self. active stores one result; TRUE and FALSE select the two branches. Print only displays an example message.

### Selected object and the complete ReadState helper

```vb
# Selected object and the complete ReadState helper
#
# Checks whether a mobile is dead.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Compare with numbers or unquoted logical constants. 1
# means the mobile has IsDead; 0 means no such state or no mobile. HP=0 alone does not mean
# death.
#
# This is a logical result: 1 = TRUE, 0 = FALSE. After VAR result = command(...), use IF result
# = TRUE THEN or IF result = 1 THEN; for a negative result, IF result = FALSE THEN or IF result
# = 0 THEN. Do not quote TRUE/FALSE. Call once and save the result: another call can repeat the
# action or read changed state.

SUB Main()
    # lasttarget is the previously selected object. Exists checks its presence. obj is ReadState’s
    # only parameter; the helper returns the command result unchanged. Its full definition is
    # included in the copied code.

    IF UO.Exists('lasttarget') THEN
        VAR observed = ReadState('lasttarget')
        UO.Print('State 1/0: ' + CStr(observed))
    END IF
END SUB

SUB ReadState(obj)
    RETURN UO.GetDead(obj)
END SUB
```

**Parameter and execution notes:**

- lasttarget is the previously selected object. Exists checks its presence. obj is ReadState’s only parameter; the helper returns the command result unchanged. Its full definition is included in the copied code.

### Detect a change over half a second

```vb
# Detect a change over half a second
#
# Checks whether a mobile is dead.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Compare with numbers or unquoted logical constants. 1
# means the mobile has IsDead; 0 means no such state or no mobile. HP=0 alone does not mean
# death.
#
# This is a logical result: 1 = TRUE, 0 = FALSE. After VAR result = command(...), use IF result
# = TRUE THEN or IF result = 1 THEN; for a negative result, IF result = FALSE THEN or IF result
# = 0 THEN. Do not quote TRUE/FALSE. Call once and save the result: another call can repeat the
# action or read changed state.

SUB Main()
    # Both calls without arguments read self; WAIT(500) means 500 milliseconds. Two snapshots are
    # compared, so intermediate changes may be missed. The example has no endless wait.

    VAR before = UO.GetDead()
    WAIT(500)
    VAR after = UO.GetDead()
    IF before <> after THEN
        UO.Print('State changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Parameter and execution notes:**

- Both calls without arguments read self; WAIT(500) means 500 milliseconds. Two snapshots are compared, so intermediate changes may be missed. The example has no endless wait.
