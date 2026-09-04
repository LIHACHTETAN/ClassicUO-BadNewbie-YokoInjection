# Runtime API Manual — Part 21

Commands: **LineID** through **MaxStamina**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.LineID`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) говорящего из последней найденной записи журнала. Это свойство обновляется после вызовов InJournal , InJournalBetweenTimes , Journal или LastJournalMessage .

### Current Yoko signatures / Return

- `UO.LineID()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineID"]` → `BRIDGE CONTRACT -> IApiBridge.JournalSerialInt`

**Pascal compatibility signature:** `function LineID: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineID()
```

---

## `UO.LineIndex`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает индекс строки последней найденной записи журнала. Это свойство обновляется после вызовов InJournal , InJournalBetweenTimes , Journal или LastJournalMessage . Индекс строки можно передать в Journal для получения текста или в SetJournalLine для установки начальной точки поиска.

### Current Yoko signatures / Return

- `UO.LineIndex()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineIndex"]`

**Pascal compatibility signature:** `function LineIndex: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineIndex()
```

---

## `UO.LineMsgType`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает тип сообщения последней найденной записи журнала. Типичные значения: 0 = обычная речь, 1 = системное/широковещательное, 2 = эмоция, 6 = метка, 7 = фокус, 12 = шёпот, 13 = крик. Это свойство обновляется после вызовов InJournal , InJournalBetweenTimes , Journal или LastJournalMessage .

### Current Yoko signatures / Return

- `UO.LineMsgType()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineMsgType"]` → `BRIDGE CONTRACT -> IApiBridge.JournalMessageType`

**Pascal compatibility signature:** `function LineMsgType: Byte;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineMsgType()
```

---

## `UO.LineName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя говорящего из последней найденной записи журнала. Это свойство обновляется после вызовов InJournal , InJournalBetweenTimes , Journal или LastJournalMessage .

### Current Yoko signatures / Return

- `UO.LineName()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineName"]` → `BRIDGE CONTRACT -> IApiBridge.JournalName`

**Pascal compatibility signature:** `function LineName: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineName()
```

---

## `UO.LineTextColor`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает цвет текста (оттенок) последней найденной записи журнала. Это свойство обновляется после вызовов InJournal , InJournalBetweenTimes , Journal или LastJournalMessage .

### Current Yoko signatures / Return

- `UO.LineTextColor()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineTextColor"]` → `BRIDGE CONTRACT -> IApiBridge.JournalColor`

**Pascal compatibility signature:** `function LineTextColor: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineTextColor()
```

---

## `UO.LineTextFont`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает ID шрифта последней найденной записи журнала. Это свойство обновляется после вызовов InJournal , InJournalBetweenTimes , Journal или LastJournalMessage .

### Current Yoko signatures / Return

- `UO.LineTextFont()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineTextFont"]` → `BRIDGE CONTRACT -> IApiBridge.JournalFont`

**Pascal compatibility signature:** `function LineTextFont: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineTextFont()
```

---

## `UO.LineTime`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает временну́ю метку ( TDateTime ) последней найденной записи журнала. Это свойство обновляется после вызовов InJournal , InJournalBetweenTimes , Journal или LastJournalMessage .

### Current Yoko signatures / Return

- `UO.LineTime()`
  - **Return type:** `Decimal`
  - **Return contract:** Decimal numeric runtime value.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineTime"]` → `BRIDGE CONTRACT -> IApiBridge.JournalTimestamp`

**Pascal compatibility signature:** `function LineTime: TDateTime;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineTime()
```

---

## `UO.LineType`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает код типа последней найденной записи журнала. Это свойство обновляется после вызовов InJournal , InJournalBetweenTimes , Journal или LastJournalMessage .

### Current Yoko signatures / Return

- `UO.LineType()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineType"]` → `BRIDGE CONTRACT -> IApiBridge.JournalTextType`

**Pascal compatibility signature:** `function LineType: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineType()
```

---

## `UO.LoadHotkeys`

### Current Yoko signatures / Return

- `UO.LoadHotkeys() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Reloads the active ClassicUO profile `macros.xml` through `World.Macros.Load()`.

### Parameters

- None in the current embedded Yoko overload.

### Behavior

Reloads the macro/hotkey definitions for the **current profile** from `macros.xml`. Because profile storage is server-scoped, the file is read from the active server-name profile folder for the current character.

### Notes / limitations

This command no longer calls `SaveConfig()` and does not overwrite the current profile as a substitute for loading hotkeys. If `macros.xml` is missing, ClassicUO's MacroManager creates its default macro file according to its normal load behavior.

### Examples

```basic
UO.LoadHotkeys()
```

---

## `UO.LOSOptions`

### Current Yoko signatures / Return

- `UO.LOSOptions() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Returns the currently configured LOS option bitmask.
- `UO.LOSOptions(value:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Stores `value` and returns the resulting bitmask.

### Parameters

- `value` — integer bitmask. The low byte selects the compatibility algorithm family; optional flags are OR-ed into the value:
  - `1` — Sphere compatibility mode.
  - `2` — SphereAdv compatibility mode.
  - `3` — RunUO compatibility mode.
  - `4` — POL compatibility mode.
  - `0x100` / `256` — check both adjacent cardinal cells during a diagonal LOS step.
  - `0x200` / `512` — in POL mode, respect the tile `NoShoot` flag.
  - `0x400` / `1024` — in POL mode, allow LOS through tiles flagged as windows.

### Behavior

`LOSOptions` is no longer a state-only setting. `UO.CheckLOS(...)` consumes the current value on every check. The Yoko implementation evaluates the currently loaded ClassicUO map, land, static, multi and world-item tile data. Walls and impassable tiles block LOS; RunUO mode also respects `NoShoot`; POL can opt into `NoShoot` and window-through behavior with the flags above.

The optional `0x100` flag adds corner validation: on a diagonal ray step both adjacent cardinal cells must remain clear.

### Notes / limitations

This is a **Yoko / ClassicUO adaptation** of the historical Stealth LOS options, not a byte-for-byte reimplementation of the external Stealth Sphere/RunUO/POL engines. Checks are limited to the **currently loaded ClassicUO map/facet**. If `value` contains an unknown algorithm number in the low byte, the ClassicUO implementation falls back to RunUO-style handling.

`LOSOptions(0)` disables the additional tile-option pass and leaves `CheckLOS` using the portable movement/world-step visibility path.

### Examples

```basic
# RunUO-style LOS
UO.LOSOptions(3)
VAR visible = UO.CheckLOS(UO.GetX('self'), UO.GetY('self'), UO.GetZ('self'), 1500, 1600, 0, UO.WorldNum())
UO.Print(visible)
```

```basic
# POL + NoShoot + allow windows
UO.LOSOptions(4 + 512 + 1024)
```

```basic
# Sphere-compatible selection + diagonal corner validation
UO.LOSOptions(1 + 256)
```
---

## `UO.LowJournal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает индекс строки самой старой записи журнала. Возвращает -1 , если журнал пуст. Это значение вместе с HighJournal определяет полный диапазон доступных записей журнала.

### Current Yoko signatures / Return

- `UO.LowJournal()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LowJournal"]` → `BRIDGE CONTRACT -> IApiBridge.JournalEntryCount`

**Pascal compatibility signature:** `function LowJournal: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LowJournal()
```

---

## `UO.Luck`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущее значение Удачи (Luck) персонажа (из расширенной информации о статусе). Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Luck()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Luck"]` → `BRIDGE CONTRACT -> IApiBridge.Luck`

**Pascal compatibility signature:** `function Luck: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Luck()
```

---

## `UO.MakeFakeItem`

### Current Yoko signatures / Return

- `UO.MakeFakeItem(type)` -> `Unit`
- `UO.MakeFakeItem(type, serial)` -> `Unit`
- `UO.MakeFakeItem(type, serial, count)` -> `Unit`
- `UO.MakeFakeItem(type, serial, count, color)` -> `Unit`
- `UO.MakeFakeItem(type, serial, count, color, x)` -> `Unit`
- `UO.MakeFakeItem(type, serial, count, color, x, y)` -> `Unit`

- **Return type:** `Unit`
- **Return contract:** No value. On success a drawable client-side item is created in the currently loaded ClassicUO world. On invalid graphic/serial or when no player is loaded, no item is created and the runtime reports an error message.

### Parameters

- `type` — item graphic ID. Must be in `1..0xFFFF`.
- `serial` — optional item serial. `0` asks Yoko to allocate a collision-free local item serial automatically. A non-zero value must be a valid item serial (`0x40000000..0x7FFFFFFF`).
- `count` — optional stack amount. Values <= 0 are normalized to `1`; values above `65535` are clamped.
- `color` — optional hue. Clamped to the ClassicUO 16-bit hue domain and normalized by the normal client hue rules.
- `x` — optional world X coordinate. If omitted, the player's current X is used.
- `y` — optional world Y coordinate. If omitted, the player's current Y is used.

### Behavior

Creates or updates a **local client-side ground `Item`** through the ClassicUO `World` item collection. The item is made drawable, receives the requested graphic/hue/count and world coordinates, and uses the current player's Z coordinate. When `serial=0`, Yoko allocates a free local item serial automatically.

This command does **not** send an item-create request to the Ultima Online server. It is a visual/local runtime object and can disappear when the world is reloaded or the server later sends state that replaces/removes the same serial.

### Notes / limitations

- Requires a loaded player/world.
- This is a client-side visual object; it is not a real server-owned item and cannot be used to create inventory or server resources.
- Supplying a serial already used by an item updates that local item; scripts should normally use `serial=0` unless they intentionally need a stable client-local serial.
- X/Y default to the player's position; Z always uses the player's current Z in this compatibility command.
- The command returns `Unit`; success is observable through world/search APIs rather than a returned serial.

### Examples

```basic
# Create 10 gold coins locally at the player position using an automatic serial
UO.MakeFakeItem(0x0EED, 0, 10, 0, UO.GetX(self), UO.GetY(self))
```

```basic
# Create a local item one tile east of the player
UO.MakeFakeItem(0x0F0E, 0, 1, 0, UO.GetX(self) + 1, UO.GetY(self))
```

# Character / Stats

## `UO.Mana`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайлов, use GetMana . Returns 0 if the character is not connected. Возвращает текущее количество маны персонажа. Для проверки маны других мобайлов используйте GetMana . Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Mana()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Mana"]` → `BRIDGE CONTRACT -> IApiBridge.Mana`

**Pascal compatibility signature:** `function Mana: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Mana()
```

---

## `UO.MassMove`

### Manifest-registered overloads

- `UO.MassMove(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.MassMove(arg1:Any, arg2:Any, arg3:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.MassMove(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any, arg6:Any, arg7:Any, arg8:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.MassMove(source, destination)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.MassMove(source, destination, delay)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.MassMove(type, color, source, destination, x, y, z, delay)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg6` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg7` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg8` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `source` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `destination` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `delay` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `x` — World/tile X coordinate.
- `y` — World/tile Y coordinate.
- `z` — World/tile Z coordinate.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MassMove(0, 0)
```

```basic
UO.MassMove(0x0190, -1, 0, 0, UO.GetX(self), UO.GetY(self), UO.GetZ(self), 0)
```

---

## `UO.MassPriceMove`

### Manifest-registered overloads

- `UO.MassPriceMove(arg1:Any, arg2:Any, arg3:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.MassPriceMove(type, destination, price)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `destination` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `price` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MassPriceMove(0, 0, 0)
```

```basic
UO.MassPriceMove(0x0190, 0, 0)
```

---

## `UO.MaxHP`

### Direct runtime overloads

- `UO.MaxHP() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MaxHP()
```

---

## `UO.MaxLife`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайлов, use GetMaxHP . Returns 0 if the character is not connected. Возвращает максимальное количество очков здоровья персонажа. Для проверки максимального HP других мобайлов используйте GetMaxHP . Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.MaxLife()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MaxLife"]` → `BRIDGE CONTRACT -> IApiBridge.GetMaxHP` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function MaxLife: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MaxLife()
```

---

## `UO.MaxMana`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайлов, use GetMaxMana . Returns 0 if the character is not connected. Возвращает максимальное количество маны персонажа. Для проверки максимальной маны других мобайлов используйте GetMaxMana . Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.MaxMana()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MaxMana"]` → `BRIDGE CONTRACT -> IApiBridge.MaxMana`

**Pascal compatibility signature:** `function MaxMana: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MaxMana()
```

---

## `UO.MaxStam`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайлов, use GetMaxStam . Returns 0 if the character is not connected. Возвращает максимальное количество стамины персонажа. Для проверки максимальной стамины других мобайлов используйте GetMaxStam . Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.MaxStam()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MaxStam"]` → `BRIDGE CONTRACT -> IApiBridge.MaxStamina`

**Pascal compatibility signature:** `function MaxStam: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MaxStam()
```

---

## `UO.MaxStamina`

### Direct runtime overloads

- `UO.MaxStamina() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MaxStamina()
```

---
