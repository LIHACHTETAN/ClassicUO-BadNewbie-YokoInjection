# UO.SetSkillLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Requests a change to the skill advancement mode.

## Exact syntax

```text
UO.SetSkillLockState(SkillName:Any, skillState:Any) -> Unit
```

## Parameters

- `SkillName` — Required skill: a name from client data, such as "Mining" or "Animal Lore", or a decimal index from 0 through Skills.Length−1, as a number or string. Names ignore case, trim outer whitespace and replace _ with a space. This is neither an item ID nor a one-based index. Numeric strings always select an index.
- `skillState` — Required mode: 0 — increase, 1 — decrease, 2 — locked. These are three codes, not Boolean; true/false cannot describe every mode.

## Returns

Unit — no return value. Do not treat the result as success/failure or compare it with true. Reading afterwards shows the local model, not server acknowledgement.

## Behavior

- A valid request sends one packet through GameActions and immediately changes the local mode. Server rules still apply; skill or stat gain is not guaranteed. Unknown skills, invalid indices/modes and an absent player are ignored without a packet.
- Required skill: a name from client data, such as "Mining" or "Animal Lore", or a decimal index from 0 through Skills.Length−1, as a number or string. Names ignore case, trim outer whitespace and replace _ with a space. This is neither an item ID nor a one-based index. Numeric strings always select an index.
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

#### 3. FindSkillUnsafe

FindSkillUnsafe first validates a decimal index and its bounds; otherwise it normalizes the name and matches Skill.Name exactly, ignoring case. An unknown name yields null; no target opens.

An unknown skill or absent player returns −1.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `FindSkillUnsafe`.

#### 4. SetSkillLockState

A valid request sends one packet through GameActions and immediately changes the local mode. Server rules still apply; skill or stat gain is not guaranteed. Unknown skills, invalid indices/modes and an absent player are ignored without a packet.

Unit — no return value. Do not treat the result as success/failure or compare it with true. Reading afterwards shows the local model, not server acknowledgement.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `SetSkillLockState`.

#### 5. ChangeSkillLockStatus

A valid request sends one packet through GameActions and immediately changes the local mode. Server rules still apply; skill or stat gain is not guaranteed. Unknown skills, invalid indices/modes and an absent player are ignored without a packet.

Unit — no return value. Do not treat the result as success/failure or compare it with true. Reading afterwards shows the local model, not server acknowledgement.

Project source: `src/ClassicUO.Client/Game/GameActions.cs`; function `ChangeSkillLockStatus`.

A valid request sends one packet through GameActions and immediately changes the local mode. Server rules still apply; skill or stat gain is not guaranteed. Unknown skills, invalid indices/modes and an absent player are ignored without a packet.


## Examples

### Read and display

```vb
# Read and display
#
# Requests a change to the skill advancement mode.
#
# Unit — no return value. Do not treat the result as success/failure or compare it with true.
# Reading afterwards shows the local model, not server acknowledgement.

SUB Main()
    # The example explicitly sets selector and, for writes, mode. The first line selects a skill by
    # name or a stat by number. Print only displays the result.

    VAR selector = 'Mining'
    VAR mode = 2
    UO.SetSkillLockState(selector, mode)
    UO.Print(CStr(UO.GetSkillLockState(selector)))
END SUB
```

**Parameter and execution notes:**

- The example explicitly sets selector and, for writes, mode. The first line selects a skill by name or a stat by number. Print only displays the result.

### Use in a condition or comparison

```vb
# Use in a condition or comparison
#
# Requests a change to the skill advancement mode.
#
# Unit — no return value. Do not treat the result as success/failure or compare it with true.
# Reading afterwards shows the local model, not server acknowledgement.

SUB Main()
    # The threshold 95.1 and modes 0/1/2 are example settings. Check −1 before changing a mode.
    # Reading after a write reads only the local copy, without waiting for server acknowledgement.

    VAR selector = 'Mining'
    VAR before = UO.GetSkillLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetSkillLockState(selector, 0)
        UO.Print(CStr(UO.GetSkillLockState(selector)))
    END IF
END SUB
```

**Parameter and execution notes:**

- The threshold 95.1 and modes 0/1/2 are example settings. Check −1 before changing a mode. Reading after a write reads only the local copy, without waiting for server acknowledgement.

### Complete helper function

```vb
# Complete helper function
#
# Requests a change to the skill advancement mode.
#
# Unit — no return value. Do not treat the result as success/failure or compare it with true.
# Reading afterwards shows the local model, not server acknowledgement.

SUB Main()
    # The complete helper follows Main. selector chooses a skill/stat; mode sets the write mode.
    # ReadValue/ReadMode return the original number; ApplyMode checks arguments, performs the action
    # and returns no value. WAIT(1000) separates two reading snapshots.

    ApplyMode('Mining', 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetSkillLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetSkillLockState(selector, mode)
END SUB
```

**Parameter and execution notes:**

- The complete helper follows Main. selector chooses a skill/stat; mode sets the write mode. ReadValue/ReadMode return the original number; ApplyMode checks arguments, performs the action and returns no value. WAIT(1000) separates two reading snapshots.
