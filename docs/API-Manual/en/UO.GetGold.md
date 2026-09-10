# UO.GetGold

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: en -->

Reads the gold amount reported in the current player’s status.

## Exact syntax

```text
UO.GetGold() -> Any
```

## Parameters

No parameters.

## Returns

Integer/Decimal — a nonnegative amount from 0 to 4294967295. Values through 2147483647 are Integer; larger values are Decimal (Double), which represents every 32-bit unsigned integer exactly. 0 also means no current live Player or no reported amount. This is not Boolean, an item ID, stack count or an inventory/bank scan.

## Behavior

- No arguments. Reads the cached Player.Gold received in CharacterStatus (0x11). The shard decides which gold its status counter includes; the command does not inspect nested bags or request a bank balance. A destroyed/missing Player gives 0, while a present ghost may retain a status amount.
- ReadGoldValue reads bridge.Gold once. The existing C# bridge keeps its Int32 signature and carries the UInt32 bits. unchecked conversion restores the unsigned amount; small amounts are wrapped as Integer, large amounts as Decimal. No negative balance is produced by high-bit overflow. This conversion is local and sends no packets.
- Keep the numeric result when comparing large amounts. Do not force it through CInt/CLng: these are 32-bit Integer conversions. Write a large BASIC numeric literal with a decimal point, e.g. 3000000000.0. A saved value can become stale before a purchase; CanAfford is only a local check, not server approval.
- Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.

### Internal functions: from call to result

Native stages of reading the status counter and widening its unsigned range. CanAfford is the complete user-defined BASIC helper shown below, not a hidden purchasing command.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases adds missing Gold/GetGold functions and intrinsics. The UO.Gold compatibility branch and its intrinsic use the same ReadGoldValue result. Unshadowed intrinsic names are evaluated on each read.

Integer/Decimal — a nonnegative amount from 0 to 4294967295. Values through 2147483647 are Integer; larger values are Decimal (Double), which represents every 32-bit unsigned integer exactly. 0 also means no current live Player or no reported amount. This is not Boolean, an item ID, stack count or an inventory/bank scan.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `RegisterCharacterGetterAliases`.

#### 2. ReadGoldValue

ReadGoldValue reads bridge.Gold once. The existing C# bridge keeps its Int32 signature and carries the UInt32 bits. unchecked conversion restores the unsigned amount; small amounts are wrapped as Integer, large amounts as Decimal. No negative balance is produced by high-bit overflow. This conversion is local and sends no packets.

Keep the numeric result when comparing large amounts. Do not force it through CInt/CLng: these are 32-bit Integer conversions. Write a large BASIC numeric literal with a decimal point, e.g. 3000000000.0. A saved value can become stale before a purchase; CanAfford is only a local check, not server approval.

Project source: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; function `ReadGoldValue`.

#### 3. Invoke

No arguments. Reads the cached Player.Gold received in CharacterStatus (0x11). The shard decides which gold its status counter includes; the command does not inspect nested bags or request a bank balance. A destroyed/missing Player gives 0, while a present ghost may retain a status amount.

Invoke reads on the game thread and honours script cancellation while waiting. No status request, target, network packet, attribute change or built-in delay is issued.

Project source: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; function `Invoke`.

#### 4. CharacterStatus

No arguments. Reads the cached Player.Gold received in CharacterStatus (0x11). The shard decides which gold its status counter includes; the command does not inspect nested bags or request a bank balance. A destroyed/missing Player gives 0, while a present ghost may retain a status amount.

Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.

Project source: `src/ClassicUO.Client/Network/PacketHandlers.cs`; function `CharacterStatus`.

#### 5. Clear

World.Clear removes Player. Later reads return 0 until a current player and its status are available; never keep a saved stat as proof that a reconnected character meets a requirement.

Integer/Decimal — a nonnegative amount from 0 to 4294967295. Values through 2147483647 are Integer; larger values are Decimal (Double), which represents every 32-bit unsigned integer exactly. 0 also means no current live Player or no reported amount. This is not Boolean, an item ID, stack count or an inventory/bank scan.

Project source: `src/ClassicUO.Client/Game/World.cs`; function `Clear`.

Each call is a new local read. Stored variables are snapshots; separate reads can see different server updates. A nonzero result is not a connectivity check. A zero can be a real value or unavailable data.


## Examples

### Display the reported amount

```vb
# Display the reported amount
#
# Reads the gold amount reported in the current player’s status.
#
# Integer/Decimal — a nonnegative amount from 0 to 4294967295. Values through 2147483647 are
# Integer; larger values are Decimal (Double), which represents every 32-bit unsigned integer
# exactly. 0 also means no current live Player or no reported amount. This is not Boolean, an
# item ID, stack count or an inventory/bank scan.

SUB Main()
    # amount stores one query; CStr formats it for the journal. No gold is searched, moved or spent.

    VAR amount = UO.GetGold()
    UO.Print('Status gold: ' + CStr(amount))
END SUB
```

**Parameter and execution notes:**

- amount stores one query; CStr formats it for the journal. No gold is searched, moved or spent.

### Complete CanAfford helper with a large price

```vb
# Complete CanAfford helper with a large price
#
# Reads the gold amount reported in the current player’s status.
#
# Integer/Decimal — a nonnegative amount from 0 to 4294967295. Values through 2147483647 are
# Integer; larger values are Decimal (Double), which represents every 32-bit unsigned integer
# exactly. 0 also means no current live Player or no reported amount. This is not Boolean, an
# item ID, stack count or an inventory/bank scan.

SUB Main()
    # price=3000000000.0 is an example price, not a limit. CanAfford(price) rejects a negative price
    # or missing Player, reads the amount once and returns Integer Boolean 1=TRUE or 0=FALSE for
    # amount >= price. The amount itself is not Boolean. The helper is fully defined below.

    VAR price = 3000000000.0
    IF CanAfford(price) = TRUE THEN
        UO.Print('Local balance is sufficient')
    ELSE
        UO.Print('Local check failed')
    END IF
END SUB

SUB CanAfford(price)
    IF price < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR amount = UO.GetGold()
    RETURN amount >= price
END SUB
```

**Parameter and execution notes:**

- price=3000000000.0 is an example price, not a limit. CanAfford(price) rejects a negative price or missing Player, reads the amount once and returns Integer Boolean 1=TRUE or 0=FALSE for amount >= price. The amount itself is not Boolean. The helper is fully defined below.

### Observe a balance change

```vb
# Observe a balance change
#
# Reads the gold amount reported in the current player’s status.
#
# Integer/Decimal — a nonnegative amount from 0 to 4294967295. Values through 2147483647 are
# Integer; larger values are Decimal (Double), which represents every 32-bit unsigned integer
# exactly. 0 also means no current live Player or no reported amount. This is not Boolean, an
# item ID, stack count or an inventory/bank scan.

SUB Main()
    # before/after are separated by WAIT(500) milliseconds. difference=after-before can be negative
    # when the reported balance falls; that differs from the corrected unsigned overflow.
    # Intermediate updates or character changes may be missed.

    VAR before = UO.GetGold()
    WAIT(500)
    VAR after = UO.GetGold()
    VAR difference = after - before
    UO.Print('Balance change: ' + CStr(difference))
END SUB
```

**Parameter and execution notes:**

- before/after are separated by WAIT(500) milliseconds. difference=after-before can be negative when the reported balance falls; that differs from the corrected unsigned overflow. Intermediate updates or character changes may be missed.
