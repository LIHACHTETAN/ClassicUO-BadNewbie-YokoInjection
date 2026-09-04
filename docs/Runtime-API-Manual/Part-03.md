# Runtime API Manual — Part 03

Commands: **Bow** through **CharTitle**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `524c4a06be8a621b5b5e24dabc4795c2c7da682f9c23e0b516f2de0a437ee254`

---

## `UO.Bow`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Выполняет жест «поклон» — персонаж кланяется.

### Current Yoko signatures / Return

- `UO.Bow()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Bow"]` → `BRIDGE CONTRACT -> IApiBridge.Bow`

**Pascal compatibility signature:** `procedure Bow;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Bow()
```

---

## `UO.BoxHack`

### Manifest-registered overloads

- `UO.BoxHack() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.BoxHack()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.BoxHack()
```

```basic
UO.BoxHack()
```

---

## `UO.Buy`

### Manifest-registered overloads

- `UO.Buy(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Buy(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Buy(arg1:Any, arg2:Any, arg3:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Buy(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Buy(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Buy(type)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Buy(type, color)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Buy(type, color, quantity)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Buy(type, color, quantity, maxPrice)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Buy(type, color, quantity, maxPrice, name)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `quantity` — Quantity/count. 0 may mean all/default only where explicitly supported.
- `maxPrice` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `name` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Buy(0)
```

```basic
UO.Buy(0x0190, -1, 1, 0, 'value')
```

---

## `UO.CalcDir`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Вычисляет направление для шага из точки ( Xfrom , Yfrom ) в точку ( Xto , Yto ). Возвращает значение направления (0–7, см. таблицу выше). Если обе точки совпадают (Xfrom = Xto и Yfrom = Yto), возвращает 100 .

### Current Yoko signatures / Return

- `UO.CalcDir(Xfrom, Yfrom, Xto, Yto)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CalcDir"]`

**Pascal compatibility signature:** `function CalcDir(Xfrom: Word; Yfrom: Word; Xto: Word; Yto: Word): Byte;`

### Parameters

- `Xfrom` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Yfrom` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Xto` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Yto` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CalcDir(0, 0, 0, 0)
```

---

## `UO.CallSub`

### Direct runtime overloads

- `UO.CallSub(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CallSub(0)
```

---

## `UO.CancelAllMenuHooks`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Удаляет все ловушки на меню, установленные через AutoMenu и WaitMenu . Вызывайте перед установкой новых хуков, чтобы убедиться, что не осталось устаревших ловушек. Алиас: CancelMenu (устаревший синоним). В Python метод называется CancelMenu .

### Current Yoko signatures / Return

- `UO.CancelAllMenuHooks()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CancelAllMenuHooks"]` → `BRIDGE CONTRACT -> IApiBridge.ClearMenuHooks`

**Pascal compatibility signature:** `procedure CancelAllMenuHooks;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CancelAllMenuHooks()
```

---

## `UO.CancelGump`

### Manifest-registered overloads

- `UO.CancelGump() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.CancelGump(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.CancelGump()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.CancelGump(gumpId)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `gumpId` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CancelGump()
```

```basic
UO.CancelGump(self)
```

---

## `UO.CancelMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устаревший синоним для CancelAllMenuHooks . Удаляет все ловушки на меню, установленные через AutoMenu и WaitMenu .

### Current Yoko signatures / Return

- `UO.CancelMenu()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `LEGACY DISPATCH -> InjectionApiUO.ExecuteLegacyCommand["CancelMenu"]`

**Pascal compatibility signature:** `procedure CancelMenu;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CancelMenu()
```

---

## `UO.CancelMove`

### Manifest-registered overloads

- `UO.CancelMove() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.CancelMove()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CancelMove()
```

```basic
UO.CancelMove()
```

---

## `UO.CancelTarget`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отменяет текущий курсор таргета, если он активен. Используйте TargetPresent для проверки наличия активного курсора таргета перед вызовом этого метода.

### Current Yoko signatures / Return

- `UO.CancelTarget()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.CancelTarget"]`

**Pascal compatibility signature:** `procedure CancelTarget;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CancelTarget()
```

---

## `UO.CancelTrade`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отменяет окно обмена с индексом TradeNum из списка активных обменов. Возвращает True , если обмен успешно отменён, False , если индекс обмена недействителен или такой обмен не существует.

### Current Yoko signatures / Return

- `UO.CancelTrade(TradeNum)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CancelTrade"]` → `BRIDGE CONTRACT -> IApiBridge.CancelTrade`

**Pascal compatibility signature:** `function CancelTrade(TradeNum: Byte): Boolean;`

### Parameters

- `TradeNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CancelTrade(0)
```

---

## `UO.CancelWaitTarget`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отменяет текущую ловушку на таргет (установленную через WaitTargetObject , WaitTargetXYZ , WaitTargetTile и т. д.). После отмены следующий курсор таргета от сервера не будет автоматически обработан и останется в ожидании до ручной обработки или установки новой ловушки.

### Current Yoko signatures / Return

- `UO.CancelWaitTarget()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CancelWaitTarget"]`

**Pascal compatibility signature:** `procedure CancelWaitTarget;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CancelWaitTarget()
```

---

## `UO.CanChangeName`

### Direct runtime overloads

- `UO.CanChangeName(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CanChangeName(0)
```

---

## `UO.Cast`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Произносит заклинание. В Pascal заклинание задаётся именем (строка). Пробелы в именах заменяются подчёркиваниями. Имена "Spell Reflection" и "Magic Reflection" считаются эквивалентными. Если имя заклинания не распознано, метод записывает ошибку в журнал и возвращает False . Возвращает True , если запрос на каст отправлен серверу. В Python метод называется Cast и принимает индекс заклинания (целое число) или значение enum Spell .

### Current Yoko signatures / Return

- `UO.Cast(SpellID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Cast"]` → `BRIDGE CONTRACT -> IApiBridge.Cast`

**Pascal compatibility signature:** `function CastSpell(SpellName: String): Boolean;`

### Additional current runtime overloads

- `UO.Cast(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `SpellID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Cast(self)
```

```basic
VAR result = UO.Cast(0, 0)
```

---

## `UO.CastAbility`

### Direct runtime overloads

- `UO.CastAbility(arg1:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.CastAbility(arg1:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CastAbility(0)
```

```basic
VAR result = UO.CastAbility(0)
```

---

## `UO.CastToObject`

### Current Yoko signatures / Return

- `UO.CastToObject(SpellName, ObjID) -> Boolean`
- `UO.CastToObject(SpellIndex, ObjID) -> Boolean`
  - **Return type:** `Boolean` (`1/0` in integer-compatible BASIC contexts)
  - **Return contract:** `True` only when the runtime accepts the cast request. Invalid/rejected spell requests return `False`; the command no longer reports unconditional success.

### Parameters

- `SpellName` — registered spell name understood by the active Yoko/ClassicUO cast route.
- `SpellIndex` — numeric spell identifier accepted by the bridge.
- `ObjID` — target object/mobile serial.

### Behavior

Queues/sets the object target and submits the spell through the ClassicUO cast bridge. The target wait is cancelled when the cast request itself is rejected so a failed `CastToObject` does not leave a stale target trap behind.

### Notes / limitations

A `True` result means the client accepted/sent the cast request; it does not guarantee that the server completed the spell. Mana, reagents, skill checks, range, line-of-sight, server rules, interruption and target validity can still make the spell fail afterward. Confirm server completion through journal/state when the script depends on it.

### Examples

```basic
IF UO.CastToObject('Greater Heal', self) THEN
    UO.Print('Cast request accepted')
ELSE
    UO.Print('Cast request rejected')
END IF
```

---

## `UO.ChangeJournalLength`

### Manifest-registered overloads

- `UO.ChangeJournalLength(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.ChangeJournalLength(newLength)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `newLength` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ChangeJournalLength(0)
```

```basic
UO.ChangeJournalLength(0)
```

---

## `UO.ChangeProfile`

### Current Yoko signatures / Return

- `UO.ChangeProfile(Name) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** `0` = accepted; `-2` = client is connected/connecting; `-3` = more than one Yoko script is running; `-4` = requested Yoko profile does not exist or cannot be resolved.

### Parameters

- `Name` — exact Yoko profile name. In this ClassicUO integration a character profile is the canonical serial folder name, for example `0x12345678`.

### Behavior

Switches the **disconnected** Yoko/ClassicUO profile selection to another existing character profile on the current server. Character metadata saved with the profile is used to configure the next login/reconnect. The current profile is saved and unloaded before the new selection is accepted.

Profiles are stored under the connected server display name:

`Data/Profiles/<server name>/<0xSerial>/`

### Notes / limitations

- The client must be disconnected; an in-game or connecting client returns `-2`.
- Only one Yoko script may be active; otherwise `-3` is returned.
- `Name` is case-sensitive at the API level and must resolve to an existing canonical character profile; missing profiles return `-4`.
- The command selects the profile/reconnect target; it does not itself force an immediate network connection. Use `UO.Connect()` when appropriate.

### Examples

```basic
VAR rc = UO.ChangeProfile('0x12345678')
IF rc = 0 THEN
    UO.Connect()
END IF
```
---

## `UO.CharacterTitle`

### Direct runtime overloads

- `UO.CharacterTitle() -> String`
  - **Return type:** `String`
  - **Return contract:** String player name/title value; empty string is possible when the value is unavailable.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CharacterTitle()
```

---

## `UO.CharName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя текущего персонажа. Возвращает пустую строку, если персонаж не подключён к серверу UO.

### Current Yoko signatures / Return

- `UO.CharName()`
  - **Return type:** `String`
  - **Return contract:** String player name/title value; empty string is possible when the value is unavailable.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CharName"]` → `BRIDGE CONTRACT -> IApiBridge.GetName` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function CharName: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CharName()
```

---

## `UO.CharPrint`

### Direct runtime overloads

- `UO.CharPrint(arg1:Integer, arg2:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.CharPrint(arg1:String, arg2:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.CharPrint(arg1:Integer, arg2:Integer, arg3:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.CharPrint(arg1:Any, arg2:Any, arg3:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CharPrint(0, 0)
```

```basic
UO.CharPrint(0, 0, 0)
```

---

## `UO.CharTitle`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает титул текущего персонажа (например, "Alex, Grandmaster Alchemist" ). Возвращает пустую строку, если персонаж не подключён к серверу UO. В Python метод называется GetCharTitle .

### Current Yoko signatures / Return

- `UO.CharTitle()`
  - **Return type:** `String`
  - **Return contract:** String player name/title value; empty string is possible when the value is unavailable.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CharTitle"]` → `BRIDGE CONTRACT -> IApiBridge.CharacterTitle`

**Pascal compatibility signature:** `function CharTitle: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CharTitle()
```

---
