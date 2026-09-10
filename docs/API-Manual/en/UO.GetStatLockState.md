# UO.GetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the local stat advancement mode.

## Exact syntax

```text
UO.GetStatLockState(statNum:Any) -> Integer
```

## Parameters

- `statNum` — Required stat number: 0 — STR, 1 — DEX, 2 — INT. This is not its current value or a name string.

## Returns

Integer: 0 — increase, 1 — decrease, 2 — locked. A mode code, not true/false. Numbers outside 0..2 return −1. Without a player, a valid number defaults to 0; this does not confirm server state.

## Behavior

- Invoke reads existing data on the game thread and sends no network packets. It neither uses nor trains a skill. Two queries are separate snapshots.
- Required stat number: 0 — STR, 1 — DEX, 2 — INT. This is not its current value or a name string.
- ExecuteStealthCompatibility selects the command branch. Text reads the skill selector; Arg reads numeric selectors and modes. Unconvertible arguments may raise a conversion error.

### Internal functions: from call to result

These are actual internal C# stages. ReadMode is a fully defined helper in the example, not an undocumented built-in command.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility selects the command branch. Text reads the skill selector; Arg reads numeric selectors and modes. Unconvertible arguments may raise a conversion error.

Integer: 0 — increase, 1 — decrease, 2 — locked. A mode code, not true/false. Numbers outside 0..2 return −1. Without a player, a valid number defaults to 0; this does not confirm server state.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.

Invoke reads existing data on the game thread and sends no network packets. It neither uses nor trains a skill. Two queries are separate snapshots.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 3. GetStatLockState

GetStatLockState/SetStatLockState select StrLock, DexLock or IntLock by 0/1/2. An unknown number reads −1; a write checks both bounds before sending.

Integer: 0 — increase, 1 — decrease, 2 — locked. A mode code, not true/false. Numbers outside 0..2 return −1. Without a player, a valid number defaults to 0; this does not confirm server state.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `GetStatLockState`.

Invoke reads existing data on the game thread and sends no network packets. It neither uses nor trains a skill. Two queries are separate snapshots.


## Examples

### Read and display

```vb
# Read and display
#
# Reads the local stat advancement mode.
#
# Integer: 0 — increase, 1 — decrease, 2 — locked. A mode code, not true/false. Numbers outside
# 0..2 return −1. Without a player, a valid number defaults to 0; this does not confirm server
# state.

SUB Main()
    # The example explicitly sets selector and, for writes, mode. The first line selects a skill by
    # name or a stat by number. Print only displays the result.

    VAR selector = 0
    VAR mode = UO.GetStatLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**Parameter and execution notes:**

- The example explicitly sets selector and, for writes, mode. The first line selects a skill by name or a stat by number. Print only displays the result.

### Use in a condition or comparison

```vb
# Use in a condition or comparison
#
# Reads the local stat advancement mode.
#
# Integer: 0 — increase, 1 — decrease, 2 — locked. A mode code, not true/false. Numbers outside
# 0..2 return −1. Without a player, a valid number defaults to 0; this does not confirm server
# state.

SUB Main()
    # The threshold 95.1 and modes 0/1/2 are example settings. Check −1 before changing a mode.
    # Reading after a write reads only the local copy, without waiting for server acknowledgement.

    VAR mode = UO.GetStatLockState(0)
    IF mode = 2 THEN
        UO.Print("Locked")
    ELSE
        IF mode = -1 THEN
            UO.Print("Unknown selector")
        ELSE
            UO.Print("Mode: " + CStr(mode))
        END IF
    END IF
END SUB
```

**Parameter and execution notes:**

- The threshold 95.1 and modes 0/1/2 are example settings. Check −1 before changing a mode. Reading after a write reads only the local copy, without waiting for server acknowledgement.

### Complete helper function

```vb
# Complete helper function
#
# Reads the local stat advancement mode.
#
# Integer: 0 — increase, 1 — decrease, 2 — locked. A mode code, not true/false. Numbers outside
# 0..2 return −1. Without a player, a valid number defaults to 0; this does not confirm server
# state.

SUB Main()
    # The complete helper follows Main. selector chooses a skill/stat; mode sets the write mode.
    # ReadValue/ReadMode return the original number; ApplyMode checks arguments, performs the action
    # and returns no value. WAIT(1000) separates two reading snapshots.

    VAR before = ReadMode(0)
    WAIT(1000)
    VAR after = ReadMode(0)
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetStatLockState(selector)
END SUB
```

**Parameter and execution notes:**

- The complete helper follows Main. selector chooses a skill/stat; mode sets the write mode. ReadValue/ReadMode return the original number; ApplyMode checks arguments, performs the action and returns no value. WAIT(1000) separates two reading snapshots.
