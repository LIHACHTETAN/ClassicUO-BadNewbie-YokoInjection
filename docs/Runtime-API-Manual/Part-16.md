# Runtime API Manual — Part 16

Commands: **GetWalkMountTimer** through **Gold**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.GetWalkMountTimer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущую задержку ходьбы (в миллисекундах), используемую, когда персонаж верхом и идёт шагом. Этот таймер управляет интервалом между шагами при ходьбе верхом. Значение можно изменить с помощью SetWalkMountTimer .

### Current Yoko signatures / Return

- `UO.GetWalkMountTimer()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetWalkMountTimer"]` → `STATE -> InjectionApiState.WalkMountTimer`

**Pascal compatibility signature:** `function GetWalkMountTimer: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetWalkMountTimer()
```

---

## `UO.GetWalkUnmountTimer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущую задержку ходьбы (в миллисекундах), используемую, когда персонаж идёт пешком. Этот таймер управляет интервалом между шагами при ходьбе без маунта. Значение можно изменить с помощью SetWalkUnmountTimer .

### Current Yoko signatures / Return

- `UO.GetWalkUnmountTimer()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetWalkUnmountTimer"]` → `STATE -> InjectionApiState.WalkUnmountTimer`

**Pascal compatibility signature:** `function GetWalkUnmountTimer: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetWalkUnmountTimer()
```

---

## `UO.GetWeaponAbilities`

### Direct runtime overloads

- `UO.GetWeaponAbilities() -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetWeaponAbilities()
```

---

## `UO.GetWeight`

### Direct runtime overloads

- `UO.GetWeight() -> Integer`
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
VAR result = UO.GetWeight()
```

---

## `UO.GetWord`

### Direct runtime overloads

- `UO.GetWord(text:String, wordIndex:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String word selected by zero-based wordIndex; empty string when the index is outside the split result.
- `UO.GetWord(text:String, wordIndex:Integer, delimiter:String) -> String`
  - **Return type:** `String`
  - **Return contract:** String word selected by zero-based wordIndex; empty string when the index is outside the split result.

### Parameters

- `text` — String/text value interpreted according to the command.
- `wordIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `delimiter` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetWord('value', 0)
```

```basic
VAR result = UO.GetWord('value', 0, 0)
```

---

## `UO.GetWordCount`

### Direct runtime overloads

- `UO.GetWordCount(text:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer number of words after splitting by whitespace/default delimiter or the supplied delimiter.
- `UO.GetWordCount(text:String, delimiter:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer number of words after splitting by whitespace/default delimiter or the supplied delimiter.

### Parameters

- `text` — String/text value interpreted according to the command.
- `delimiter` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetWordCount('value')
```

```basic
VAR result = UO.GetWordCount('value', 0)
```

---

## `UO.GetWorldCell`

### Direct runtime overloads

- `UO.GetWorldCell(arg1:Any, arg2:Any) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
- `UO.GetWorldCell(arg1:Any, arg2:Any, arg3:Any) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetWorldCell(0, 0)
```

```basic
VAR result = UO.GetWorldCell(0, 0, 0)
```

---

## `UO.GetWorldItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает массив всех предметов мира, известных клиенту на данный момент. Каждый элемент — запись TWorldItemData , содержащая серийный номер, графику, цвет, координаты, номер мира, количество в стопке и флаги. Предоставляет снимок предметов, видимых в игровом мире (не внутри контейнеров). Для мобилов используйте GetMobiles .

### Current Yoko runtime signatures / Return

- `UO.GetWorldItems() -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of matching world/container item serials; an empty array is valid.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetWorldItems"]` → `BRIDGE CONTRACT -> IApiBridge.GetWorldItems`
- `UO.GetWorldItems(type) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of matching world/container item serials; an empty array is valid.
- `UO.GetWorldItems(type, color) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of matching world/container item serials; an empty array is valid.
- `UO.GetWorldItems(type, color, distance) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of matching world/container item serials; an empty array is valid.
- `UO.GetWorldItems(type, color, distance, container) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of matching world/container item serials; an empty array is valid.
- `UO.GetWorldItems(type, color, distance, container, nearest) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of matching world/container item serials; an empty array is valid.
- `UO.GetWorldItems(type, color, distance, container, nearest, maxZ) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of matching world/container item serials; an empty array is valid.

### Historical compatibility reference

- Pascal: `function GetWorldItems: TArray ;`
- Historical Yoko/Stealth syntax: `UO.GetWorldItems()`

### Parameters

- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `distance` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.
- `container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `nearest` — Boolean ordering flag. TRUE selects/orders nearest matches first; FALSE preserves the runtime search order.
- `maxZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.

### Behavior

Enumerates world/container Item objects and applies type/hue/distance/container/Z plus optional nearest ordering.

### Notes / limitations

Only loaded/current world and container items are available. Nearest ordering is based on the player position when enabled.

### Examples

```basic
VAR result = UO.GetWorldItems()
```

```basic
VAR result = UO.GetWorldItems(0x0190, -1, 18, backpack, TRUE, 12)
```

---

## `UO.GetWorldNum`

### Direct runtime overloads

- `UO.GetWorldNum() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetWorldNum()
```

---

## `UO.GetWorldTilesArray`

### Direct runtime overloads

- `UO.GetWorldTilesArray(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.

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
VAR result = UO.GetWorldTilesArray(0, 0, 0, 0, 0)
```

---

## `UO.GetX`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает координату X объекта или мобила с указанным ObjID . ObjID — ID объекта или мобила. Возвращает 0 , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetX(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetX"]` → `BRIDGE CONTRACT -> IApiBridge.GetX` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetX(ObjID: Cardinal): Word;`

### Additional current runtime overloads

- `UO.GetX() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetX(self)
```

```basic
VAR result = UO.GetX()
```

---

## `UO.GetY`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает координату Y объекта или мобила с указанным ObjID . ObjID — ID объекта или мобила. Возвращает 0 , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetY(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetY"]` → `BRIDGE CONTRACT -> IApiBridge.GetY` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetY(ObjID: Cardinal): Word;`

### Additional current runtime overloads

- `UO.GetY() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetY(self)
```

```basic
VAR result = UO.GetY()
```

---

## `UO.GetYellowBar`

### Direct runtime overloads

- `UO.GetYellowBar(arg1:Any) -> Integer`
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
VAR result = UO.GetYellowBar(0)
```

---

## `UO.GetZ`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает координату Z (высоту) объекта или мобила с указанным ObjID . ObjID — ID объекта или мобила. Возвращает 0 , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetZ(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetZ"]` → `BRIDGE CONTRACT -> IApiBridge.GetZ` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetZ(ObjID: Cardinal): ShortInt;`

### Additional current runtime overloads

- `UO.GetZ() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetZ(self)
```

```basic
VAR result = UO.GetZ()
```

---

## `UO.GListClear`

### Direct runtime overloads

- `UO.GListClear() -> Unit`
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
UO.GListClear()
```

---

## `UO.GListGet`

### Direct runtime overloads

- `UO.GListGet(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant: the exact stored global-list InjectionValue; Integer 0 when the name does not exist.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GListGet(0)
```

---

## `UO.GListPosName`

### Direct runtime overloads

- `UO.GListPosName(arg1:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GListPosName(0)
```

---

## `UO.GListPosValue`

### Direct runtime overloads

- `UO.GListPosValue(arg1:Integer) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant: the exact stored global-list InjectionValue at the requested position; Integer 0 for an invalid index.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GListPosValue(0)
```

---

## `UO.GListSet`

### Direct runtime overloads

- `UO.GListSet(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.GListSet(0, 0)
```

---

## `UO.GListSize`

### Direct runtime overloads

- `UO.GListSize() -> Integer`
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
VAR result = UO.GListSize()
```

---

## `UO.GlobalChatActiveChannel`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает название канала глобального чата, в котором сейчас находится персонаж. Возвращает пустую строку, если персонаж не находится ни в одном чат-канале.

### Current Yoko signatures / Return

- `UO.GlobalChatActiveChannel()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GlobalChatActiveChannel"]` → `BRIDGE CONTRACT -> IApiBridge.GlobalChatActiveChannel`

**Pascal compatibility signature:** `function GlobalChatActiveChannel: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GlobalChatActiveChannel()
```

---

## `UO.GlobalChatChannelsList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает список доступных каналов глобального чата.

### Current Yoko signatures / Return

- `UO.GlobalChatChannelsList()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GlobalChatChannelsList"]` → `BRIDGE CONTRACT -> IApiBridge.GlobalChatChannels`

**Pascal compatibility signature:** `function GlobalChatChannelsList: TArray ;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GlobalChatChannelsList()
```

---

## `UO.GlobalChatJoinChannel`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Присоединяется к указанному каналу глобального чата. ChName — название канала для подключения. Отправляет серверу пакет присоединения к чату. Текущий активный канал можно проверить через GlobalChatActiveChannel .

### Current Yoko signatures / Return

- `UO.GlobalChatJoinChannel(ChName)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GlobalChatJoinChannel"]` → `BRIDGE CONTRACT -> IApiBridge.GlobalChatJoin`

**Pascal compatibility signature:** `procedure GlobalChatJoinChannel(ChName: String);`

### Parameters

- `ChName` — String/text value interpreted according to the command.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.GlobalChatJoinChannel('value')
```

---

## `UO.GlobalChatLeaveChannel`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Покидает текущий канал глобального чата. Метод автоматически определяет имя активного канала и отправляет пакет выхода из него. Параметры не требуются.

### Current Yoko signatures / Return

- `UO.GlobalChatLeaveChannel()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GlobalChatLeaveChannel"]` → `BRIDGE CONTRACT -> IApiBridge.GlobalChatLeave`

**Pascal compatibility signature:** `procedure GlobalChatLeaveChannel;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.GlobalChatLeaveChannel()
```

---

## `UO.GlobalChatSendMsg`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет сообщение в текущий канал глобального чата. MsgText — текст отправляемого сообщения. Персонаж должен находиться в чат-канале (см. GlobalChatJoinChannel ), чтобы сообщение было доставлено.

### Current Yoko signatures / Return

- `UO.GlobalChatSendMsg(MsgText)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GlobalChatSendMsg"]` → `BRIDGE CONTRACT -> IApiBridge.GlobalChatSend`

**Pascal compatibility signature:** `procedure GlobalChatSendMsg(MsgText: String);`

### Parameters

- `MsgText` — String/text value interpreted according to the command.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.GlobalChatSendMsg(1000)
```

---

## `UO.Gold`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущее количество золота персонажа (как отображается в окне статуса). Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Gold()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Gold"]` → `BRIDGE CONTRACT -> IApiBridge.Gold`

**Pascal compatibility signature:** `function Gold: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Gold()
```

---
