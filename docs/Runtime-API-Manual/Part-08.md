# Runtime API Manual — Part 08

Commands: **Exec** through **FindQuantity**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.Exec`

### Direct runtime overloads

- `UO.Exec(name:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Starts the named loaded Yoko procedure/subroutine through the runtime Exec route.

### Parameters

- `name` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Exec('value')
```

---

## `UO.Exists`

### Direct runtime overloads

- `UO.Exists(arg1:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.Exists(arg1:String) -> Integer`
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
VAR result = UO.Exists(0)
```

```basic
VAR result = UO.Exists(0)
```

---

## `UO.ExtChangeProfile`

### Current Yoko signatures / Return

- `UO.ExtChangeProfile(ProfileName) -> Integer`
- `UO.ExtChangeProfile(ProfileName, ShardName) -> Integer`
- `UO.ExtChangeProfile(ProfileName, ShardName, CharName) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** `0` = accepted; `-2` = connected/connecting; `-3` = multiple Yoko scripts are running; `-4` = profile/shard selection cannot be resolved.

### Parameters

- `ProfileName` — canonical Yoko character profile name, normally `0x<serial>`.
- `ShardName` — optional human-readable server/shard name. Empty uses the current/last selected server.
- `CharName` — optional character name. Empty uses the character identity stored with that profile when available.

### Behavior

Extended profile selection for a disconnected client. The command validates that the target profile exists beneath the selected server-name folder, saves/unloads the current profile, stores the selected shard in ClassicUO settings and supplies the target character to the real login character-selection flow.

### Notes / limitations

- The server folder uses the actual display server name, not `V2`, not `IP:port`, and not the internal shard identity key.
- If `CharName` is empty, the `.character-name` metadata saved with the canonical profile is used.
- The command does not bypass server authentication and cannot select a character the shard does not return.
- Use `UO.Connect()` after a successful return when an immediate reconnect is desired.

### Examples

```basic
VAR rc = UO.ExtChangeProfile('0x12345678', 'Age of Power', 'LIHACH')
IF rc = 0 THEN
    UO.Connect()
END IF
```
---

## `UO.ExtendedInfo`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает расширенную информацию о персонаже в виде записи TExtendedInfo . Данные доступны только для серверов эры SE+ (Samurai Empire и выше), отправляющих расширенную статистику. В Python метод называется GetExtInfo .

### Current Yoko signatures / Return

- `UO.ExtendedInfo()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ExtendedInfo"]` → `BRIDGE CONTRACT -> IApiBridge.ClientPath` → `BRIDGE CONTRACT -> IApiBridge.CurrentProfilePath` → `BRIDGE CONTRACT -> IApiBridge.GameServerAddress` → `BRIDGE CONTRACT -> IApiBridge.GameServerPort`

**Pascal compatibility signature:** `function ExtendedInfo: TExtendedInfo;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ExtendedInfo()
```

---

## `UO.FillInfoWindow`

### Current Yoko signatures / Return

- `UO.FillInfoWindow(text) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Appends the supplied text to the Yoko/ClassicUO **Info Window** and opens/brings that information surface into use.

### Parameters

- `text` — text line to append.

### Behavior

Writes to the Info Window through the client text-information route. It does not merely emit a normal in-game/system chat message.

### Notes / limitations

`FillInfoWindow` is explicit output and is **not suppressed** by `SetSilentMode(True)`. Silent mode controls automatic diagnostic output from commands such as Gump line/description queries.

### Examples

```basic
UO.FillInfoWindow('Runebook inspection started')
```

---

## `UO.FillNewWindow`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Добавляет строку в информационное окно Stealth. Содержимое информационного окна можно очистить через ClearInfoWindow . Примечание: Настройка SetSilentMode не влияет на этот метод — строки всегда добавляются независимо от тихого режима.

### Current Yoko signatures / Return

- `UO.FillNewWindow(S)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FillNewWindow"]` → `BRIDGE CONTRACT -> IApiBridge.TextClear` → `BRIDGE CONTRACT -> IApiBridge.TextOpen` → `BRIDGE CONTRACT -> IApiBridge.TextPrint`

**Pascal compatibility signature:** `procedure FillNewWindow(S: String);`

### Parameters

- `S` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.FillNewWindow(0)
```

---

## `UO.FilterSpeech`

### Manifest-registered overloads

- `UO.FilterSpeech() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.FilterSpeech(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.FilterSpeech()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.FilterSpeech(enabled)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `enabled` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FilterSpeech()
```

```basic
UO.FilterSpeech(0)
```

---

## `UO.FilterWeather`

### Manifest-registered overloads

- `UO.FilterWeather() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.FilterWeather(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.FilterWeather()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.FilterWeather(enabled)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `enabled` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FilterWeather()
```

```basic
UO.FilterWeather(0)
```

---

## `UO.FindAnyType`

### Direct runtime overloads

- `UO.FindAnyType(arg1, arg2) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindAnyType(0, 0)
```

---

## `UO.FindAtCoord`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет все объекты в указанных мировых координатах ( X , Y ) и возвращает ID последнего найденного объекта. Возвращает 0 , если ничего не найдено или персонаж не подключён. После успешного поиска обновляются FindCount , FindItem и GetFindedList .

### Current Yoko signatures / Return

- `UO.FindAtCoord(X, Y)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindAtCoord"]` → `BRIDGE CONTRACT -> IApiBridge.FindAtCoord`

**Pascal compatibility signature:** `function FindAtCoord(X: Word; Y: Word): Cardinal;`

### Parameters

- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindAtCoord(UO.GetX(self), UO.GetY(self))
```

---

## `UO.FindByNotoriety`

### Direct runtime overloads

- `UO.FindByNotoriety(arg1, arg2) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindByNotoriety(0, 0)
```

---

## `UO.FindCount`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает количество найденных предметов после последнего вызова FindType , FindTypeEx или FindTypesArrayEx . Возвращает 0 , если ничего не найдено или персонаж не подключён. Стеки, содержащие несколько предметов, считаются как 1 предмет. Для получения общего количества с учётом стеков используйте FindFullQuantity .

### Current Yoko signatures / Return

- `UO.FindCount()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.FindCount"]`

**Pascal compatibility signature:** `function FindCount: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindCount()
```

---

## `UO.FindDistance`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Задаёт горизонтальный радиус поиска (в тайлах) для поиска на земле методами FindType , FindTypeEx , FindTypesArrayEx и связанными. Значение по умолчанию: 2 . Максимальное значение: 90 — значения выше 90 обрезаются. Влияет только на поиск с контейнером Ground ( $FFFFFFFF ). Не влияет на поиск в контейнерах или рюкзаке. В Python используйте GetFindDistance() / SetFindDistance(value) .

### Current Yoko signatures / Return

- `UO.FindDistance()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindDistance"]` → `BRIDGE CONTRACT -> IApiBridge.GetFindDistance` → `BRIDGE CONTRACT -> IApiBridge.SetFindDistance`
- `UO.FindDistance(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindDistance"]` → `BRIDGE CONTRACT -> IApiBridge.GetFindDistance` → `BRIDGE CONTRACT -> IApiBridge.SetFindDistance`

**Pascal compatibility signature:** `var FindDistance: Cardinal;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindDistance()
```

```basic
UO.FindDistance('value')
```

---

## `UO.FindFullQuantity`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает общее количество найденных предметов после последнего поиска, включая содержимое стеков. Возвращает 0 , если ничего не найдено или персонаж не подключён. В отличие от FindCount , который считает стеки как отдельные предметы, этот метод суммирует все предметы внутри стеков.

### Current Yoko signatures / Return

- `UO.FindFullQuantity()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindFullQuantity"]` → `BRIDGE CONTRACT -> IApiBridge.FindFullQuantity`

**Pascal compatibility signature:** `function FindFullQuantity: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindFullQuantity()
```

---

## `UO.FindItem`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает ID последнего объекта, найденного через FindType , FindTypeEx или FindTypesArrayEx . Возвращает 0 , если ничего не найдено или персонаж не подключён. Совпадает со значением, возвращаемым самими методами поиска.

### Current Yoko signatures / Return

- `UO.FindItem()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindItem"]` → `BRIDGE CONTRACT -> IApiBridge.FindItem`

**Pascal compatibility signature:** `function FindItem: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindItem()
```

---

## `UO.FindList`

### Direct runtime overloads

- `UO.FindList(arg1:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.
- `UO.FindList(arg1:Any, arg2:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.
- `UO.FindList(arg1:Any, arg2:Any, arg3:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.
- `UO.FindList(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.
- `UO.FindList(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Resolves the named list created in runtime state, then executes the same Search Core used by FindType/FindNotoriety. The list name is not treated as a numeric type string.

### Notes / limitations

The named list must exist in runtime state. Missing/empty lists produce the documented no-match result instead of inventing a type from the list name.

### Examples

```basic
VAR result = UO.FindList(0)
```

```basic
VAR result = UO.FindList(0, 0, 0, 0, 0)
```

---

## `UO.FindMan`

### Direct runtime overloads

- `UO.FindMan(notoriety) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety, distance) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety, distance, nearest) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety, distance, nearest, maxZ) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety, distance, nearest, maxZ, body) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety, distance, nearest, maxZ, body, color) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety, distance, nearest, maxZ, body, color, includeSelf) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.

### Legacy Yoko overloads

- `UO.FindMan()`
  - **Return type:** `Unit`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.

### Parameters

- `notoriety` — Actual ClassicUO Mobile.Notoriety value or supported mask/string form; it is not inferred from hue/name/body.
- `distance` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.
- `nearest` — Boolean ordering flag. TRUE selects/orders nearest matches first; FALSE preserves the runtime search order.
- `maxZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.
- `body` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `includeSelf` — Boolean. TRUE allows the player mobile to be included; FALSE excludes self.

### Behavior

Scans loaded mobiles only and applies notoriety, distance, nearest, Z/body/color/self and Ignore filters supported by the selected overload.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindMan(5)
```

```basic
UO.FindMan()
```

---

## `UO.FindMobile`

### Direct runtime overloads

- `UO.FindMobile() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.FindMobile(arg1, arg2, arg3, arg4) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.FindMobile(arg1, arg2, arg3, arg4, arg5) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindMobile()
```

```basic
VAR result = UO.FindMobile(0, 0, 0, 0)
```

```basic
VAR result = UO.FindMobile(0, 0, 0, 0, 0)
```

---

## `UO.FindNotoriety`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет mobile с указанными body/graphic ObjType и статусом Notoriety на земле. Это не гарантированный поиск только игроков: mobile может быть персонажем игрока либо NPC, а универсального отличия на всех шардах нет. ObjType = 0xFFFF означает любой тип. Notoriety: 1 Innocent/синий, 2 Ally/зелёный, 3 Attackable/серый, 4 Criminal/серый, 5 Enemy/оранжевый, 6 Murderer/красный, 7 Invulnerable/жёлтый. Радиус задают FindDistance и FindVertical. Возвращает ID последнего найденного mobile либо 0. После вызова обновляются FindItem, FindCount и GetFoundItems/GetFindedList.

### Current Yoko runtime signatures / Return

- `UO.FindNotoriety(type, notoriety) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindNotoriety"]` → `BRIDGE CONTRACT -> IApiBridge.FindNotoriety`
- `UO.FindNotoriety(type, notoriety, distance) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
- `UO.FindNotoriety(type, notoriety, distance, nearest) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
- `UO.FindNotoriety(type, notoriety, distance, nearest, maxZ) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
- `UO.FindNotoriety(type, notoriety, distance, nearest, maxZ, color) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
- `UO.FindNotoriety(type, notoriety, distance, nearest, maxZ, color, container) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.

### Historical compatibility reference

- Pascal: `function FindNotoriety(ObjType: Word; Notoriety: Byte): Cardinal;`
- Historical Yoko/Stealth syntax: `UO.FindNotoriety(ObjType, Notoriety)`

### Parameters

- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `notoriety` — Actual ClassicUO Mobile.Notoriety value or supported mask/string form; it is not inferred from hue/name/body.
- `distance` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.
- `nearest` — Boolean ordering flag. TRUE selects/orders nearest matches first; FALSE preserves the runtime search order.
- `maxZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.

### Behavior

Scans loaded World.Mobiles using the real Mobile.Notoriety field, body/type, distance/Z and Ignore rules. The registered result uses first-match semantics unless nearest ordering is requested.

### Notes / limitations

Uses real notoriety values; do not treat hue, body or name as substitutes. 0 means no matching mobile.

### Examples

```basic
VAR result = UO.FindNotoriety(0x0190, 5)
```

```basic
VAR result = UO.FindNotoriety(0x0190, 5, 18, TRUE, 12, -1, backpack)
```

---

## `UO.FindQuantity`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает размер стека (количество) последнего найденного предмета. Возвращает 0 , если ничего не найдено или персонаж не подключён. Возвращает 1 , если найденный объект не является стеком.

### Current Yoko signatures / Return

- `UO.FindQuantity()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindQuantity"]` → `BRIDGE CONTRACT -> IApiBridge.FindQuantity`

**Pascal compatibility signature:** `function FindQuantity: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindQuantity()
```

---
