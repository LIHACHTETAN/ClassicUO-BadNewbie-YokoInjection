# Runtime API Manual — Part 04

Commands: **CheckLag** through **ClientPrint**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.CheckLag`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет пинг-запрос серверу UO и ждёт ответа в течение указанного таймаута. Возвращает True , если сервер ответил в пределах timeoutMS миллисекунд, False , если таймаут истёк (лаг или проблема соединения). Часто используется для проверки того, что сервер обработал предыдущие действия, перед отправкой новых. В Python таймаут по умолчанию — 10000 мс.

### Current Yoko signatures / Return

- `UO.CheckLag(timeoutMS)`
  - **Return type:** `Integer`
  - **Return contract:** 0x73 server-echo status; nonzero means matching echo before timeout, 0 means timeout/offline/no ACK.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CheckLag"]` → `BRIDGE CONTRACT -> IApiBridge.CheckLag`

**Pascal compatibility signature:** `function CheckLag(timeoutMS: Integer): Boolean;`

### Parameters

- `timeoutMS` — Timeout/delay in milliseconds. 0 has command-specific meaning; see Notes / limitations.

### Behavior

Sends a tokenized 0x73 ping packet and waits for the matching server echo up to timeoutMS. It does not substitute IsOnline() for a network round trip.

### Notes / limitations

Requires a connected server that echoes 0x73. Timeout/offline/no matching ACK returns the documented failure value.

### Examples

```basic
VAR result = UO.CheckLag(1000)
```

---

## `UO.CheckLOS`

### Current Yoko signatures / Return

- `UO.CheckLOS(Xfrom:Integer, Yfrom:Integer, Zfrom:Integer, Xto:Integer, Yto:Integer, Zto:Integer, WorldNum:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** `1` when the Yoko/ClassicUO LOS path is clear; `0` when it is blocked, the requested map is not the loaded map, or a required world step cannot be validated.

### Parameters

- `Xfrom`, `Yfrom`, `Zfrom` — starting world coordinates.
- `Xto`, `Yto`, `Zto` — destination world coordinates.
- `WorldNum` — map/facet index. The current implementation requires this to match the currently loaded ClassicUO map.

### Behavior

The command traces from the start point to the destination and validates world movement cells. When `UO.LOSOptions()` is non-zero, every traced cell is additionally checked against the loaded ClassicUO land/static/multi/item tile data. The selected LOS algorithm family and flags affect `NoShoot`, windows and diagonal-corner behavior.

At the destination the vertical difference must be within the current portable LOS tolerance; otherwise the result is `0`.

### Notes / limitations

This is a **Yoko / ClassicUO adaptation** designed for current runtime behavior. It does not claim bit-identical results with every historical external Stealth LOS engine. Arbitrary offline facets are not loaded solely for this call; pass the current `UO.WorldNum()` unless the corresponding map is actually active.

For the meaning of algorithm values and flags, see `UO.LOSOptions`.

### Examples

```basic
VAR x1 = UO.GetX('self')
VAR y1 = UO.GetY('self')
VAR z1 = UO.GetZ('self')

UO.LOSOptions(3)
VAR visible = UO.CheckLOS(x1, y1, z1, x1 + 10, y1, z1, UO.WorldNum())
UO.Print(visible)
```

```basic
# Require diagonal corner clearance too
UO.LOSOptions(3 + 256)
VAR visible = UO.CheckLOS(1000, 1000, 0, 1010, 1010, 0, UO.WorldNum())
```
---

## `UO.CircleTrans`

### Direct runtime overloads

- `UO.CircleTrans() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.CircleTrans(arg1:Integer) -> Unit`
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
VAR result = UO.CircleTrans()
```

```basic
UO.CircleTrans(0)
```

---

## `UO.ClearBadLocationList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает список непроходимых точек, используемый pathfinder’ом. Список может заполняться: Вручную через SetBadLocation . Автоматически системой движения Stealth — если перемещение в точку не удалось 3 раза подряд, точка помечается как непроходимая. Точки, находящиеся в списке более 15 минут , удаляются автоматически.

### Current Yoko signatures / Return

- `UO.ClearBadLocationList()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearBadLocationList"]` → `STATE -> InjectionApiState.BadLocations`

**Pascal compatibility signature:** `procedure ClearBadLocationList;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearBadLocationList()
```

---

## `UO.ClearBadObjectList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает список непроходимых объектов, используемый pathfinder’ом. Список заполняется вручную через SetBadObject . В отличие от списка непроходимых точек, записи не удаляются автоматически по таймауту.

### Current Yoko signatures / Return

- `UO.ClearBadObjectList()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearBadObjectList"]` → `STATE -> InjectionApiState.BadObjects`

**Pascal compatibility signature:** `procedure ClearBadObjectList;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearBadObjectList()
```

---

## `UO.ClearChatUserIgnore`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает список игнорируемых имён пользователей для входящих сообщений чата (список, заполненный через AddChatUserIgnore ). После вызова этого метода сообщения от всех ранее игнорируемых пользователей снова будут появляться в журнале.

### Current Yoko signatures / Return

- `UO.ClearChatUserIgnore()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearChatUserIgnore"]` → `BRIDGE CONTRACT -> IApiBridge.ClearChatUserIgnore`

**Pascal compatibility signature:** `procedure ClearChatUserIgnore;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearChatUserIgnore()
```

---

## `UO.ClearContextMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает сохранённые данные контекстного меню. Контекстное меню заполняется, когда сервер присылает ответ на запрос (после RequestContextMenu ). Сохранённые данные можно прочитать через GetContextMenu . Вызывайте этот метод перед запросом нового контекстного меню, чтобы получить актуальные данные, или используйте событие evContextMenu для более надёжного отслеживания.

### Current Yoko signatures / Return

- `UO.ClearContextMenu()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearContextMenu"]` → `BRIDGE CONTRACT -> IApiBridge.ClearContextMenu`

**Pascal compatibility signature:** `procedure ClearContextMenu;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearContextMenu()
```

---

## `UO.ClearFigures`

### Current Yoko signatures / Return

- `UO.ClearFigures() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. All Yoko-created World Map figures are removed from both visual map state and runtime figure state.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.ClearMapFigures` -> `WorldMapGump`.

### Parameters

- None.

### Behavior

Clears every client-side map figure created through the Yoko `AddFigure` API. Normal World Map marker files/user markers are not affected.

### Notes / limitations

This operates only on Yoko figure overlays; it does not delete persisted `userMarkers` map files.

### Examples

```basic
UO.ClearFigures()
```

# Search / World

## `UO.ClearFindList`

### Manifest-registered overloads

- `UO.ClearFindList() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.ClearFindList(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.ClearFindList()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.ClearFindList(list)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `list` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ClearFindList()
```

```basic
UO.ClearFindList(0)
```

---

## `UO.ClearGumpsIgnore`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает список игнорируемых гампов, удаляя все записи, добавленные через AddGumpIgnoreByID и AddGumpIgnoreBySerial . После вызова этого метода все ранее игнорируемые гампы снова будут отображаться.

### Current Yoko signatures / Return

- `UO.ClearGumpsIgnore()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearGumpsIgnore"]` → `STATE -> InjectionApiState.IgnoredGumpIds` → `STATE -> InjectionApiState.IgnoredGumpSerials`

**Pascal compatibility signature:** `procedure ClearGumpsIgnore;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearGumpsIgnore()
```

---

## `UO.ClearIgnoreList`

### Manifest-registered overloads

- `UO.ClearIgnoreList() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.ClearIgnoreList(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.ClearIgnoreList()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.ClearIgnoreList(list)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `list` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ClearIgnoreList()
```

```basic
UO.ClearIgnoreList(0)
```

---

## `UO.ClearInfoWindow`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает содержимое информационного окна Stealth. Информационное окно заполняется различными методами, такими как GetGumpTextLines , FillNewWindow , GetShopList и другими.

### Current Yoko signatures / Return

- `UO.ClearInfoWindow()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearInfoWindow"]` → `BRIDGE CONTRACT -> IApiBridge.TextClear`

**Pascal compatibility signature:** `procedure ClearInfoWindow;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearInfoWindow()
```

---

## `UO.ClearJournal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает UO-журнал (основной журнал, не системный). После вызова метода InJournal и InJournalBetweenTimes не найдут предыдущих сообщений. Для очистки системного журнала используйте ClearSystemJournal .

### Current Yoko signatures / Return

- `UO.ClearJournal()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearJournal"]`

**Pascal compatibility signature:** `procedure ClearJournal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearJournal()
```

---

## `UO.ClearJournalIgnore`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает список игнорируемых сообщений журнала, заполненный через AddJournalIgnore . После вызова метода все входящие сообщения снова будут отображаться в журнале, независимо от ранее установленных фильтров.

### Current Yoko signatures / Return

- `UO.ClearJournalIgnore()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearJournalIgnore"]` → `BRIDGE CONTRACT -> IApiBridge.ClearJournalIgnore`

**Pascal compatibility signature:** `procedure ClearJournalIgnore;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearJournalIgnore()
```

---

## `UO.ClearShopList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает сохранённое содержимое списка товаров вендора. Список товаров заполняется автоматически, когда игрок открывает меню покупки у вендора (командой “buy” или через контекстное меню). Содержимое списка можно прочитать через GetShopList . Метод очищает только текстовое представление списка товаров. Он не влияет на хуки покупки/продажи, установленные через AutoBuy или AutoSell .

### Current Yoko signatures / Return

- `UO.ClearShopList()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearShopList"]` → `BRIDGE CONTRACT -> IApiBridge.ClearAutoShopRules`

**Pascal compatibility signature:** `procedure ClearShopList;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearShopList()
```

---

## `UO.ClearSystemJournal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает системный журнал (вкладка «System» в главном окне Stealth). Для очистки основного UO-журнала используйте ClearJournal .

### Current Yoko signatures / Return

- `UO.ClearSystemJournal()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearSystemJournal"]` → `BRIDGE CONTRACT -> IApiBridge.DeleteSystemJournal`

**Pascal compatibility signature:** `procedure ClearSystemJournal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearSystemJournal()
```

---

## `UO.ClearUserStatics`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Удаляет все пользовательские статик-объекты, ранее добавленные через AddUserStatic . Поскольку пользовательские статики хранятся в данных шарда (а не для каждого персонажа отдельно), их очистка затрагивает всех персонажей, использующих те же файлы шарда.

### Current Yoko signatures / Return

- `UO.ClearUserStatics()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClearUserStatics"]` → `STATE -> InjectionApiState.UserStatics` → `BRIDGE CONTRACT -> IApiBridge.ClearUserStatics`

**Pascal compatibility signature:** `procedure ClearUserStatics;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClearUserStatics()
```

---

## `UO.Click`

### Direct runtime overloads

- `UO.Click(arg1:Any) -> Unit`
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
UO.Click(0)
```

---

## `UO.ClickOnObject`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет одиночный клик по объекту с указанным ObjID . Сервер обычно отвечает именем и/или описанием объекта в журнале. Метод отправляет запрос клика на сервер. Для чтения тултипов объектов используйте GetTooltip или GetToolTipRec .

### Current Yoko signatures / Return

- `UO.ClickOnObject(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClickOnObject"]`

**Pascal compatibility signature:** `procedure ClickOnObject(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClickOnObject(self)
```

---

## `UO.ClientHide`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Скрывает указанный объект на подключённом клиенте. Объект становится невидимым локально — сервер не уведомляется, другие игроки по-прежнему видят объект. Возвращает True , если объект успешно скрыт, False в противном случае.

### Current Yoko signatures / Return

- `UO.ClientHide(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClientHide"]` → `BRIDGE CONTRACT -> IApiBridge.ClientHide`

**Pascal compatibility signature:** `function ClientHide(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ClientHide(self)
```

---

## `UO.ClientMarkChar`

### Direct runtime overloads

- `UO.ClientMarkChar(arg1:Any, arg2:Any) -> Unit`
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
UO.ClientMarkChar(0, 0)
```

---

## `UO.ClientPrint`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет текстовое сообщение подключённому клиенту. Текст появляется в области журнала/чата клиента. Сообщение отправляется только клиенту — оно не передаётся на сервер и не видно другим игрокам.

### Current Yoko signatures / Return

- `UO.ClientPrint(Text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClientPrint"]`

**Pascal compatibility signature:** `procedure ClientPrint(Text: String);`

### Parameters

- `Text` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ClientPrint('value')
```

---
