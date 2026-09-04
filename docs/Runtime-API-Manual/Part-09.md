# Runtime API Manual — Part 09

Commands: **FindType** through **GetArrayLength**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.FindType`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет объекты с типом ObjType в указанном Container . Ищет любой цвет, только верхний уровень (без подконтейнеров). Для поиска с фильтром по цвету и/или с подконтейнерами используйте FindTypeEx . Возвращает ID последнего найденного объекта или 0 .

### Current Yoko runtime signatures / Return

- `UO.FindType(type) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string of the first match; empty string means no match.
- `UO.FindType(type, color) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string of the first match; empty string means no match.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.FindType"]`
- `UO.FindType(type, color, container) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string of the first match; empty string means no match.
- `UO.FindType(type, color, container, distance) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string of the first match; empty string means no match.
- `UO.FindType(type, color, container, distance, notoriety) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string of the first match; empty string means no match.
- `UO.FindType(type, color, container, distance, notoriety, nearest) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string of the first match; empty string means no match.

### Historical compatibility reference

- Pascal: `function FindType(ObjType: Word; Container: Cardinal): Cardinal;`
- Historical Yoko/Stealth syntax: `UO.FindType(ObjType, Container)`

### Parameters

- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `distance` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.
- `notoriety` — Actual ClassicUO Mobile.Notoriety value or supported mask/string form; it is not inferred from hue/name/body.
- `nearest` — Boolean ordering flag. TRUE selects/orders nearest matches first; FALSE preserves the runtime search order.

### Behavior

Runs the shared Search Core against the requested type/color/container and optional distance/notoriety/nearest filters. Ignore, FindDistance and FindVertical are respected when the overload does not replace them explicitly.

### Notes / limitations

Overloads are positional. Explicit distance/notoriety/nearest parameters must be supplied in order. Ignore remains active unless an API explicitly exposes includeIgnored.

### Examples

```basic
VAR result = UO.FindType(0x0190)
```

```basic
VAR result = UO.FindType(0x0190, -1, backpack, 18, 5, TRUE)
```

---

## `UO.FindTypeEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет объекты с указанным типом ObjType и цветом Color в заданном контейнере Container . ObjType — graphic (тип) искомого объекта. $FFFF (65535) — любой тип. Color — цвет объекта. $FFFF (65535) — любой цвет. Container — где искать: Backpack (рюкзак), Ground / $FFFFFFFF (земля в радиусе FindDistance / FindVertical ), или ID конкретного контейнера. InSub — True для рекурсивного поиска по вложенным контейнерам. Возвращает ID последнего найденного объекта, или 0 если ничего не найдено или персонаж не подключён. Радиус поиска задаётся FindDistance (по горизонтали, макс. 90) и FindVertical (по вертикали, макс. 120). После успешного поиска обновляются: FindItem , FindCount , FindFullQuantity , FindQuantity , GetFindedList . Объекты, добавленные в список игнорирования через Ignore , исключаются из результатов.

### Current Yoko signatures / Return

- `UO.FindTypeEx(ObjType, Color, Container, InSub)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindTypeEx"]` → `BRIDGE CONTRACT -> IApiBridge.FindType`

**Pascal compatibility signature:** `function FindTypeEx(ObjType: Word; Color: Word; Container: Cardinal; InSub: Boolean): Cardinal;`

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `Container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `InSub` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindTypeEx(0x0190, -1, backpack, 0)
```

---

## `UO.FindTypesArrayEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет объекты, соответствующие любой комбинации из массивов типов ObjTypes , цветов Colors и контейнеров Containers . Внутри метод перебирает каждую комбинацию тип/цвет/контейнер и выполняет простой поиск для каждой. Все результаты агрегируются.

### Current Yoko signatures / Return

- `UO.FindTypesArrayEx(ObjTypes, Colors, Containers, InSub)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindTypesArrayEx"]` → `BRIDGE CONTRACT -> IApiBridge.FindTypes`

**Pascal compatibility signature:** `function FindTypesArrayEx(ObjTypes: array of Word; Colors: array of Word; Containers: array of Cardinal; InSub: Boolean): Cardinal;`

### Parameters

- `ObjTypes` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Colors` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `Containers` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `InSub` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindTypesArrayEx(0x0190, -1, backpack, 0)
```

---

## `UO.FindVertical`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Задаёт вертикальный радиус поиска (ось Z, в тайлах) для поиска на земле методами FindType , FindTypeEx , FindTypesArrayEx и связанными. Значение по умолчанию: 2 . Максимальное значение: 120 — значения выше 120 обрезаются. Влияет только на поиск с контейнером Ground ( $FFFFFFFF ). В Python используйте GetFindVertical() / SetFindVertical(value) .

### Current Yoko signatures / Return

- `UO.FindVertical()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindVertical"]` → `BRIDGE CONTRACT -> IApiBridge.GetFindVertical` → `BRIDGE CONTRACT -> IApiBridge.SetFindVertical`
- `UO.FindVertical(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindVertical"]` → `BRIDGE CONTRACT -> IApiBridge.GetFindVertical` → `BRIDGE CONTRACT -> IApiBridge.SetFindVertical`

**Pascal compatibility signature:** `var FindVertical: Cardinal;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FindVertical()
```

```basic
UO.FindVertical('value')
```

---

## `UO.FireResist`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение сопротивления огню персонажа. Работает только с эрой сервера Samurai Empire и выше. Иначе всегда возвращает 0 .

### Current Yoko signatures / Return

- `UO.FireResist()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FireResist"]` → `BRIDGE CONTRACT -> IApiBridge.FireResistance`

**Pascal compatibility signature:** `function FireResist: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FireResist()
```

---

## `UO.FixTalk`

### Manifest-registered overloads

- `UO.FixTalk() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.FixTalk()`
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
VAR result = UO.FixTalk()
```

```basic
UO.FixTalk()
```

---

## `UO.FixWalk`

### Manifest-registered overloads

- `UO.FixWalk() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.FixWalk()`
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
VAR result = UO.FixWalk()
```

```basic
UO.FixWalk()
```

---

## `UO.Flying`

### Direct runtime overloads

- `UO.Flying() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.Flying(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.Flying(serial:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Flying()
```

```basic
VAR result = UO.Flying(0)
```

```basic
VAR result = UO.Flying(self)
```

---

## `UO.Followers`

### Direct runtime overloads

- `UO.Followers() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Followers()
```

---

## `UO.FollowersMax`

### Direct runtime overloads

- `UO.FollowersMax() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FollowersMax()
```

---

## `UO.FontColor`

### Manifest-registered overloads

- `UO.FontColor(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.FontColor(color)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FontColor(0)
```

```basic
UO.FontColor(-1)
```

---

## `UO.Forget`

### Manifest-registered overloads

- `UO.Forget(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Forget(name)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `name` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Forget(0)
```

```basic
UO.Forget('value')
```

---

## `UO.FoundedParamId`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает ID параметра из последнего успешного поиска в журнале через InJournal или InJournalBetweenTimes . Значение указывает на тип/источник найденной записи журнала.

### Current Yoko signatures / Return

- `UO.FoundedParamId()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FoundedParamId"]` → `BRIDGE CONTRACT -> IApiBridge.JournalTextType`

**Pascal compatibility signature:** `function FoundedParamID: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.FoundedParamId()
```

---

## `UO.Frozen`

### Direct runtime overloads

- `UO.Frozen() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.Frozen(serial:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- `serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Frozen()
```

```basic
VAR result = UO.Frozen(self)
```

---

## `UO.FunRunning`

### Direct runtime overloads

- `UO.FunRunning(arg1:String) -> Integer`
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
VAR result = UO.FunRunning(0)
```

---

## `UO.GameServerIPString`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает IP-адрес игрового сервера (не логин-сервера).

### Current Yoko signatures / Return

- `UO.GameServerIPString()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GameServerIPString"]` → `BRIDGE CONTRACT -> IApiBridge.GameServerAddress`

**Pascal compatibility signature:** `function GameServerIPString: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GameServerIPString()
```

---

## `UO.Gate`

### Manifest-registered overloads

- `UO.Gate() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Gate(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Gate()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Gate(target)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `target` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Gate()
```

```basic
UO.Gate(self)
```

---

## `UO.GetAbilityID`

### Direct runtime overloads

- `UO.GetAbilityID(arg1:String) -> Integer`
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
VAR result = UO.GetAbilityID(0)
```

---

## `UO.GetAbilityName`

### Direct runtime overloads

- `UO.GetAbilityName(arg1:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetAbilityName(0)
```

---

## `UO.GetActiveAbility`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя текущей активной боевой способности персонажа в виде строки. Если способность не активна, возвращает '0' .

### Current Yoko signatures / Return

- `UO.GetActiveAbility()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetActiveAbility"]` → `BRIDGE CONTRACT -> IApiBridge.GetActiveAbility`

**Pascal compatibility signature:** `function GetActiveAbility: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetActiveAbility()
```

---

## `UO.GetAlive`

### Direct runtime overloads

- `UO.GetAlive() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetAlive(serial:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- `serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetAlive()
```

```basic
VAR result = UO.GetAlive(self)
```

---

## `UO.GetAltName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает «альтернативное имя» объекта с ObjID . В зависимости от сервера может содержать титул, название гильдии, профессию или другую информацию. Может быть пустым. Иногда нужно предварительно вызвать ClickOnObject для заполнения полей имени и альтернативного имени.

### Current Yoko signatures / Return

- `UO.GetAltName(ObjID)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetAltName"]` → `BRIDGE CONTRACT -> IApiBridge.GetAltName`

**Pascal compatibility signature:** `function GetAltName(ObjID: Cardinal): String;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetAltName(self)
```

---

## `UO.GetArmor`

### Direct runtime overloads

- `UO.GetArmor() -> Integer`
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
VAR result = UO.GetArmor()
```

---

## `UO.GetArrayLength`

### Direct runtime overloads

- `UO.GetArrayLength(value:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer array length; returns 0 when the supplied value is not an Array.

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetArrayLength('value')
```

---
