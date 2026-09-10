# UO.GetSkillCurrentValue

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the effective skill value including modifiers.

## Exact syntax

```text
UO.GetSkillCurrentValue(SkillName:Any) -> Decimal
```

## Parameters

- `SkillName` — Required skill: a name from client data, such as "Mining" or "Animal Lore", or a decimal index from 0 through Skills.Length−1, as a number or string. Names ignore case, trim outer whitespace and replace _ with a space. This is neither an item ID nor a one-based index. Numeric strings always select an index.

## Returns

Decimal (Double) — skill points in tenths, for example 95.1 rather than 951. Field ValueFixed is divided by 10 directly as Double. Zero means a zero skill or missing player/skill. This is not Boolean. Legacy SkillVal/BaseVal use a different scale; do not mix the families.

## Behavior

- Invoke reads existing data on the game thread and sends no network packets. It neither uses nor trains a skill. Two queries are separate snapshots.
- Required skill: a name from client data, such as "Mining" or "Animal Lore", or a decimal index from 0 through Skills.Length−1, as a number or string. Names ignore case, trim outer whitespace and replace _ with a space. This is neither an item ID nor a one-based index. Numeric strings always select an index.
- ExecuteStealthCompatibility selects the command branch. Text reads the skill selector; Arg reads numeric selectors and modes. Unconvertible arguments may raise a conversion error.

### Internal functions: from call to result

These are actual internal C# stages. ReadValue is a fully defined helper in the example, not an undocumented built-in command.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility selects the command branch. Text reads the skill selector; Arg reads numeric selectors and modes. Unconvertible arguments may raise a conversion error.

Decimal (Double) — skill points in tenths, for example 95.1 rather than 951. Field ValueFixed is divided by 10 directly as Double. Zero means a zero skill or missing player/skill. This is not Boolean. Legacy SkillVal/BaseVal use a different scale; do not mix the families.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke reads on the game thread; a worker waits for the manager to process the request. Script cancellation interrupts that wait. No extra delay or network query is added.

Invoke reads existing data on the game thread and sends no network packets. It neither uses nor trains a skill. Two queries are separate snapshots.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe first validates a decimal index and its bounds; otherwise it normalizes the name and matches Skill.Name exactly, ignoring case. An unknown name yields null; no target opens.

An unknown skill or absent player returns −1.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `FindSkillUnsafe`.

#### 4. GetSkillValue

GetSkillValue selects BaseFixed, ValueFixed or CapFixed and divides the integer tenths by 10d. There is no intermediate Single rounding.

Decimal (Double) — skill points in tenths, for example 95.1 rather than 951. Field ValueFixed is divided by 10 directly as Double. Zero means a zero skill or missing player/skill. This is not Boolean. Legacy SkillVal/BaseVal use a different scale; do not mix the families.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `GetSkillValue`.

Invoke reads existing data on the game thread and sends no network packets. It neither uses nor trains a skill. Two queries are separate snapshots.


## Examples

### Read and display

```vb
# Read and display
#
# Reads the effective skill value including modifiers.
#
# Decimal (Double) — skill points in tenths, for example 95.1 rather than 951. Field ValueFixed
# is divided by 10 directly as Double. Zero means a zero skill or missing player/skill. This is
# not Boolean. Legacy SkillVal/BaseVal use a different scale; do not mix the families.

SUB Main()
    # The example explicitly sets selector and, for writes, mode. The first line selects a skill by
    # name or a stat by number. Print only displays the result.

    VAR selector = 'Mining'
    VAR value = UO.GetSkillCurrentValue(selector)
    UO.Print(CStr(value))
END SUB
```

**Parameter and execution notes:**

- The example explicitly sets selector and, for writes, mode. The first line selects a skill by name or a stat by number. Print only displays the result.

### Use in a condition or comparison

```vb
# Use in a condition or comparison
#
# Reads the effective skill value including modifiers.
#
# Decimal (Double) — skill points in tenths, for example 95.1 rather than 951. Field ValueFixed
# is divided by 10 directly as Double. Zero means a zero skill or missing player/skill. This is
# not Boolean. Legacy SkillVal/BaseVal use a different scale; do not mix the families.

SUB Main()
    # The threshold 95.1 and modes 0/1/2 are example settings. Check −1 before changing a mode.
    # Reading after a write reads only the local copy, without waiting for server acknowledgement.

    IF UO.GetSkillLockState('Mining') >= 0 THEN
        VAR value = UO.GetSkillCurrentValue('Mining')
        IF value >= 95.1 THEN
            UO.Print('Value >= 95.1: ' + CStr(value))
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
# Reads the effective skill value including modifiers.
#
# Decimal (Double) — skill points in tenths, for example 95.1 rather than 951. Field ValueFixed
# is divided by 10 directly as Double. Zero means a zero skill or missing player/skill. This is
# not Boolean. Legacy SkillVal/BaseVal use a different scale; do not mix the families.

SUB Main()
    # The complete helper follows Main. selector chooses a skill/stat; mode sets the write mode.
    # ReadValue/ReadMode return the original number; ApplyMode checks arguments, performs the action
    # and returns no value. WAIT(1000) separates two reading snapshots.

    VAR before = ReadValue('Animal_Lore')
    WAIT(1000)
    VAR after = ReadValue('Animal Lore')
    UO.Print(CStr(after - before))
END SUB

SUB ReadValue(selector)
    RETURN UO.GetSkillCurrentValue(selector)
END SUB
```

**Parameter and execution notes:**

- The complete helper follows Main. selector chooses a skill/stat; mode sets the write mode. ReadValue/ReadMode return the original number; ApplyMode checks arguments, performs the action and returns no value. WAIT(1000) separates two reading snapshots.
