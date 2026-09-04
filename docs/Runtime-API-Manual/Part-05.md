# Runtime API Manual — Part 05

Commands: **ClientPrintEx** through **ContainerOff**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.ClientPrintEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Расширенная версия ClientPrint . Отправляет текстовое сообщение подключённому клиенту с настраиваемым форматированием. Сообщение отправляется только клиенту — оно не передаётся на сервер и не видно другим игрокам.

### Current Yoko signatures / Return

- `UO.ClientPrintEx(SenderID, Color, Font, Text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClientPrintEx"]` → `BRIDGE CONTRACT -> IApiBridge.CharPrintEx`

**Pascal compatibility signature:** `procedure ClientPrintEx(SenderID: Cardinal; Color: Word; Font: Word; Text: String);`

### Parameters

- `SenderID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `Font` — Font identifier/name. Exact support depends on the client UI route documented for the command.
- `Text` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClientPrintEx(self, -1, 0, 'value')
```

---

## `UO.ClientRequestObjectTarget`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет запрос на выбор объекта подключённому клиенту. Клиент покажет курсор таргета, позволяющий пользователю выбрать объект (не тайл/точку на земле). После выбора объекта результат можно получить через ClientTargetResponse . Используйте ClientTargetResponsePresent для проверки ответа или WaitForClientTargetResponse для ожидания с таймаутом. Для выбора тайлов или точек на земле используйте ClientRequestTileTarget .

### Current Yoko signatures / Return

- `UO.ClientRequestObjectTarget()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClientRequestObjectTarget"]` → `BRIDGE CONTRACT -> IApiBridge.RequestClientTarget`

**Pascal compatibility signature:** `procedure ClientRequestObjectTarget;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClientRequestObjectTarget()
```

---

## `UO.ClientRequestTileTarget`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет запрос на выбор тайла подключённому клиенту. Клиент покажет курсор таргета, позволяющий пользователю выбрать тайл или точку на земле (не объект). После выбора тайла результат можно получить через ClientTargetResponse . Используйте ClientTargetResponsePresent для проверки ответа или WaitForClientTargetResponse для ожидания с таймаутом. Для выбора объектов используйте ClientRequestObjectTarget .

### Current Yoko signatures / Return

- `UO.ClientRequestTileTarget()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClientRequestTileTarget"]` → `BRIDGE CONTRACT -> IApiBridge.RequestClientTarget`

**Pascal compatibility signature:** `procedure ClientRequestTileTarget;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClientRequestTileTarget()
```

---

## `UO.ClientTargetResponse`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает информацию о цели, выбранной пользователем в клиенте, после запроса таргета через ClientRequestObjectTarget или ClientRequestTileTarget . Перед вызовом проверьте ClientTargetResponsePresent , чтобы убедиться, что пользователь ответил.

### Current Yoko signatures / Return

- `UO.ClientTargetResponse()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClientTargetResponse"]` → `BRIDGE CONTRACT -> IApiBridge.ClientTargetResponse`

**Pascal compatibility signature:** `function ClientTargetResponse: TTargetInfo;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ClientTargetResponse()
```

---

## `UO.ClientTargetResponsePresent`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если пользователь уже выбрал цель в клиенте (после запроса через ClientRequestObjectTarget или ClientRequestTileTarget ), False , если ответа ещё нет. Используйте для опроса готовности ответа, или WaitForClientTargetResponse для ожидания с таймаутом.

### Current Yoko signatures / Return

- `UO.ClientTargetResponsePresent()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClientTargetResponsePresent"]` → `BRIDGE CONTRACT -> IApiBridge.ClientTargetResponsePresent`

**Pascal compatibility signature:** `function ClientTargetResponsePresent: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ClientTargetResponsePresent()
```

---

## `UO.CloseClientGump`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Закрывает гамп с указанным ID на подключённом клиенте. Команда закрытия отправляется непосредственно клиенту. Гамп идентифицируется по его gump ID (не по индексу в списке гампов Stealth).

### Current Yoko signatures / Return

- `UO.CloseClientGump(ID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CloseClientGump"]` → `BRIDGE CONTRACT -> IApiBridge.CloseClientGump`

**Pascal compatibility signature:** `procedure CloseClientGump(ID: Cardinal);`

### Parameters

- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CloseClientGump(self)
```

---

## `UO.CloseClientUIWindow`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Закрывает окно клиентского интерфейса указанного типа для объекта с данным ID .

### Current Yoko signatures / Return

- `UO.CloseClientUIWindow(UIWindowType, ID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CloseClientUIWindow"]` → `BRIDGE CONTRACT -> IApiBridge.CloseClientWindow`

**Pascal compatibility signature:** `procedure CloseClientUIWindow(UIWindowType: TUIWindowType; ID: Cardinal);`

### Parameters

- `UIWindowType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CloseClientUIWindow(0x0190, self)
```

---

## `UO.CloseHandle`

### Direct runtime overloads

- `UO.CloseHandle() -> Unit`
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
UO.CloseHandle()
```

---

## `UO.CloseMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Закрывает все открытые в данный момент меню в Stealth для текущего персонажа. Для каждого открытого меню на сервер отправляется ответ MenuCancel . В отличие от CancelAllMenuHooks (который удаляет ловушки ), этот метод закрывает фактически открытые окна меню. Поведение клиентов: В клиенте Orion меню реально закроется визуально. В других подключённых клиентах (ClassicUO, TazUO, legacy 2D/3D) меню на стороне клиента не закрывается — вместо этого клиент получает сообщение "Menu reply sent from stealth" .

### Current Yoko signatures / Return

- `UO.CloseMenu()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CloseMenu"]` → `BRIDGE CONTRACT -> IApiBridge.CloseMenu`

**Pascal compatibility signature:** `procedure CloseMenu;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CloseMenu()
```

---

## `UO.CloseSimpleGump`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Закрывает гамп по указанному индексу в списке гампов Stealth. Закрыть можно только гампы без свойства NoClose . Используйте IsGumpCanBeClosed для предварительной проверки. Индекс гампа можно получить через GetGumpsCount (нумерация с 0).

### Current Yoko signatures / Return

- `UO.CloseSimpleGump(GumpIndex)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CloseSimpleGump"]` → `BRIDGE CONTRACT -> IApiBridge.CloseSimpleGump`

**Pascal compatibility signature:** `procedure CloseSimpleGump(GumpIndex: Word);`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.CloseSimpleGump(0)
```

---

## `UO.CloseUO`

### Manifest-registered overloads

- `UO.CloseUO() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.CloseUO()`
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
VAR result = UO.CloseUO()
```

```basic
UO.CloseUO()
```

---

## `UO.ColdResist`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение сопротивления холоду персонажа. Работает только с эрой сервера Samurai Empire и выше, и сервер должен отправлять расширенную статистику. Иначе всегда возвращает 0 .

### Current Yoko signatures / Return

- `UO.ColdResist()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ColdResist"]` → `BRIDGE CONTRACT -> IApiBridge.ColdResistance`

**Pascal compatibility signature:** `function ColdResist: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ColdResist()
```

---

## `UO.ColorPrint`

### Direct runtime overloads

- `UO.ColorPrint(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ColorPrint(0, 0)
```

---

## `UO.ConColor`

### Direct runtime overloads

- `UO.ConColor(arg1:Any) -> Unit`
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
UO.ConColor(0)
```

---

## `UO.ConfirmTrade`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Подтверждает обмен, устанавливая флажок подтверждения для обмена с индексом TradeNum в списке активных обменов.

### Current Yoko signatures / Return

- `UO.ConfirmTrade(TradeNum)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ConfirmTrade"]` → `BRIDGE CONTRACT -> IApiBridge.ConfirmTrade`

**Pascal compatibility signature:** `procedure ConfirmTrade(TradeNum: Byte);`

### Parameters

- `TradeNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ConfirmTrade(0)
```

---

## `UO.Connect`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Подключает текущего персонажа к серверу UO, используя настройки из активного профиля. Если персонаж уже подключён, метод ничего не делает. После вызова Connect рекомендуется подождать несколько секунд для завершения подключения, прежде чем выполнять другие действия.

### Current Yoko signatures / Return

- `UO.Connect()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Connect"]` → `BRIDGE CONTRACT -> IApiBridge.ConnectClient`

**Pascal compatibility signature:** `procedure Connect;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Connect()
```

---

## `UO.Connected`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает статус подключения: True , если персонаж подключён к серверу UO, False , если нет.

### Current Yoko signatures / Return

- `UO.Connected()`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Connected"]` → `BRIDGE CONTRACT -> IApiBridge.IsOnline`

**Pascal compatibility signature:** `function Connected: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Connected()
```

---

## `UO.ConnectedTime`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает дату и время последнего успешного подключения к серверу. Если успешного подключения ещё не было, возвращает 30.12.1899 (эквивалент 0 в формате TDateTime Delphi).

### Current Yoko signatures / Return

- `UO.ConnectedTime()`
  - **Return type:** `Decimal`
  - **Return contract:** Decimal numeric runtime value.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ConnectedTime"]` → `STATE -> InjectionApiState.ConnectedTime`

**Pascal compatibility signature:** `function ConnectedTime: TDateTime;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ConnectedTime()
```

---

## `UO.ConsoleEntryReply`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет ответ на запрос консольного ввода от сервера UO. Консольный ввод используется для текстового ввода в клиенте, например для переименования рун. Метод обрабатывает оба варианта запроса: ANSI и Unicode. ConsoleEntryUnicodeReply — синоним этого метода. Если запрос консольного ввода уже получен от сервера, метод немедленно отправляет ответ. Если ещё не получен — устанавливается хук, и ответ отправляется автоматически при получении запроса. Если не уверены, какой тип запроса приходит от сервера, проверьте журнал — там будет сообщение о типе.

### Current Yoko signatures / Return

- `UO.ConsoleEntryReply(Text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ConsoleEntryReply"]` → `BRIDGE CONTRACT -> IApiBridge.ReplyServerPrompt`

**Pascal compatibility signature:** `procedure ConsoleEntryReply(Text: String);`

### Parameters

- `Text` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ConsoleEntryReply('value')
```

---

## `UO.ConsoleEntryUnicodeReply`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Синоним для ConsoleEntryReply . Оба метода одинаково обрабатывают ANSI и Unicode запросы консольного ввода. См. ConsoleEntryReply для полной документации.

### Current Yoko signatures / Return

- `UO.ConsoleEntryUnicodeReply(Text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ConsoleEntryUnicodeReply"]` → `BRIDGE CONTRACT -> IApiBridge.ReplyServerPrompt`

**Pascal compatibility signature:** `procedure ConsoleEntryUnicodeReply(Text: String);`

### Parameters

- `Text` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ConsoleEntryUnicodeReply('value')
```

---

## `UO.ConsolePrint`

### Direct runtime overloads

- `UO.ConsolePrint(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ConsolePrint(0)
```

---

## `UO.ContainerOf`

### Direct runtime overloads

- `UO.ContainerOf(arg1:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ContainerOf(0)
```

---

## `UO.ContainerOff`

### Direct runtime overloads

- `UO.ContainerOff() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ContainerOff()
```

---
