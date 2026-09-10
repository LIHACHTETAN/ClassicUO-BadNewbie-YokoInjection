# UO.SetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Requests a change to the stat advancement mode.

## Exact syntax

```text
UO.SetStatLockState(statNum:Any, statState:Any) -> Unit
```

## Parameters

- `statNum` — Required stat number: 0 — STR, 1 — DEX, 2 — INT. This is not its current value or a name string.
- `statState` — Required mode: 0 — increase, 1 — decrease, 2 — locked. These are three codes, not Boolean; true/false cannot describe every mode.

## Returns

Unit — no return value. Do not treat the result as success/failure or compare it with true. Reading afterwards shows the local model, not server acknowledgement.

## Behavior

- A valid request sends one packet through GameActions and immediately changes the local mode. Server rules still apply; skill or stat gain is not guaranteed. Unknown skills, invalid indices/modes and an absent player are ignored without a packet.
- Required stat number: 0 — STR, 1 — DEX, 2 — INT. This is not its current value or a name string.
- ExecuteStealthCompatibility selects the command branch. Text reads the skill selector; Arg reads numeric selectors and modes. Unconvertible arguments may raise a conversion error.

### Internal functions: from call to result

These are actual internal C# stages. ApplyMode is a fully defined helper in the example, not an undocumented built-in command.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility selects the command branch. Text reads the skill selector; Arg reads numeric selectors and modes. Unconvertible arguments may raise a conversion error.

Unit — no return value. Do not treat the result as success/failure or compare it with true. Reading afterwards shows the local model, not server acknowledgement.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.

A valid request sends one packet through GameActions and immediately changes the local mode. Server rules still apply; skill or stat gain is not guaranteed. Unknown skills, invalid indices/modes and an absent player are ignored without a packet.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 3. SetStatLockState

GetStatLockState/SetStatLockState select StrLock, DexLock or IntLock by 0/1/2. An unknown number reads −1; a write checks both bounds before sending.

Unit — no return value. Do not treat the result as success/failure or compare it with true. Reading afterwards shows the local model, not server acknowledgement.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `SetStatLockState`.

#### 4. ChangeStatLock

A valid request sends one packet through GameActions and immediately changes the local mode. Server rules still apply; skill or stat gain is not guaranteed. Unknown skills, invalid indices/modes and an absent player are ignored without a packet.

Unit — no return value. Do not treat the result as success/failure or compare it with true. Reading afterwards shows the local model, not server acknowledgement.

Project source: `src/ClassicUO.Client/Game/GameActions.cs`; function `ChangeStatLock`.

A valid request sends one packet through GameActions and immediately changes the local mode. Server rules still apply; skill or stat gain is not guaranteed. Unknown skills, invalid indices/modes and an absent player are ignored without a packet.


## Examples

### Read and display

```vb
# Read and display
#
# Requests a change to the stat advancement mode.
#
# Unit — no return value. Do not treat the result as success/failure or compare it with true.
# Reading afterwards shows the local model, not server acknowledgement.

SUB Main()
    # The example explicitly sets selector and, for writes, mode. The first line selects a skill by
    # name or a stat by number. Print only displays the result.

    VAR selector = 0
    VAR mode = 2
    UO.SetStatLockState(selector, mode)
    UO.Print(CStr(UO.GetStatLockState(selector)))
END SUB
```

**Parameter and execution notes:**

- The example explicitly sets selector and, for writes, mode. The first line selects a skill by name or a stat by number. Print only displays the result.

### Use in a condition or comparison

```vb
# Use in a condition or comparison
#
# Requests a change to the stat advancement mode.
#
# Unit — no return value. Do not treat the result as success/failure or compare it with true.
# Reading afterwards shows the local model, not server acknowledgement.

SUB Main()
    # The threshold 95.1 and modes 0/1/2 are example settings. Check −1 before changing a mode.
    # Reading after a write reads only the local copy, without waiting for server acknowledgement.

    VAR selector = 0
    VAR before = UO.GetStatLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetStatLockState(selector, 0)
        UO.Print(CStr(UO.GetStatLockState(selector)))
    END IF
END SUB
```

**Parameter and execution notes:**

- The threshold 95.1 and modes 0/1/2 are example settings. Check −1 before changing a mode. Reading after a write reads only the local copy, without waiting for server acknowledgement.

### Complete helper function

```vb
# Complete helper function
#
# Requests a change to the stat advancement mode.
#
# Unit — no return value. Do not treat the result as success/failure or compare it with true.
# Reading afterwards shows the local model, not server acknowledgement.

SUB Main()
    # The complete helper follows Main. selector chooses a skill/stat; mode sets the write mode.
    # ReadValue/ReadMode return the original number; ApplyMode checks arguments, performs the action
    # and returns no value. WAIT(1000) separates two reading snapshots.

    ApplyMode(0, 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetStatLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetStatLockState(selector, mode)
END SUB
```

**Parameter and execution notes:**

- The complete helper follows Main. selector chooses a skill/stat; mode sets the write mode. ReadValue/ReadMode return the original number; ApplyMode checks arguments, performs the action and returns no value. WAIT(1000) separates two reading snapshots.
