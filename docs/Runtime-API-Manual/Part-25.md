# Runtime API Manual — Part 25

Commands: **PredictedY** through **RenameMobile**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `524c4a06be8a621b5b5e24dabc4795c2c7da682f9c23e0b516f2de0a437ee254`

---

## `UO.PredictedY`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает предсказанную координату Y персонажа на основе текущей траектории движения.

### Current Yoko signatures / Return

- `UO.PredictedY()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PredictedY"]` → `BRIDGE CONTRACT -> IApiBridge.GetY` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function PredictedY: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PredictedY()
```

---

## `UO.PredictedZ`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает предсказанную координату Z (высоту) персонажа на основе текущей траектории движения.

### Current Yoko signatures / Return

- `UO.PredictedZ()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PredictedZ"]` → `BRIDGE CONTRACT -> IApiBridge.GetZ` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function PredictedZ: ShortInt;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PredictedZ()
```

---

## `UO.Press`

### Direct runtime overloads

- `UO.Press(arg1:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Press(arg1:Integer, arg2:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Press(arg1:Integer, arg2:Integer, arg3:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Press(0)
```

```basic
UO.Press(0, 0)
```

```basic
UO.Press(0, 0, 0)
```

---

## `UO.Print`

### Direct runtime overloads

- `UO.Print(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Print(arg1:Any, arg2:Any) -> Unit`
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
UO.Print(0)
```

```basic
UO.Print(0, 0)
```

---

## `UO.PrivateGetTile`

### Direct runtime overloads

- `UO.PrivateGetTile(arg1:Integer, arg2:Integer, arg3:Integer, arg4:Integer, arg5:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PrivateGetTile(0, 0, 0, 0, 0)
```

---

## `UO.ProfileName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя текущего активного профиля Stealth.

### Current Yoko signatures / Return

- `UO.ProfileName()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ProfileName"]` → `BRIDGE CONTRACT -> IApiBridge.ProfileName`

**Pascal compatibility signature:** `function ProfileName: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ProfileName()
```

---

## `UO.ProfileShardName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя шарда, связанного с текущим активным профилем.

### Current Yoko signatures / Return

- `UO.ProfileShardName()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ProfileShardName"]` → `BRIDGE CONTRACT -> IApiBridge.ShardName`

**Pascal compatibility signature:** `function ProfileShardName: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ProfileShardName()
```

---

## `UO.ProxyIP`

### Current Yoko signatures / Return

- `UO.ProxyIP() -> String`
  - **Return type:** `String`
  - **Return contract:** Returns the configured Yoko proxy address. In the current embedded runtime, proxy mode is not implemented, therefore the value is an empty string.

### Parameters

- None.

### Behavior

Reports proxy state only. It deliberately does **not** return the game-server IP as a fake proxy address.

### Notes / limitations

Use the normal server/address APIs for the actual game endpoint. `ProxyIP` remains empty until a real proxy layer is configured/implemented.

### Examples

```basic
VAR proxy = UO.ProxyIP()
```

---

## `UO.ProxyPort`

### Current Yoko signatures / Return

- `UO.ProxyPort() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Returns the configured proxy port. Current embedded Yoko proxy support is disabled/unimplemented, so the result is `0`.

### Parameters

- None.

### Behavior

Reports proxy state only and does not mirror the game-server port.

### Notes / limitations

`0` is the explicit compatibility value until a separate proxy transport is implemented.

### Examples

```basic
VAR port = UO.ProxyPort()
```

---

## `UO.QuestRequest`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос квеста для собственного персонажа. Обычно открывает журнал квестов или гамп квестов на серверах, которые это поддерживают.

### Current Yoko signatures / Return

- `UO.QuestRequest()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["QuestRequest"]` → `BRIDGE CONTRACT -> IApiBridge.QuestRequest`

**Pascal compatibility signature:** `procedure QuestRequest;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.QuestRequest()
```

---

## `UO.Race`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает расу персонажа в виде числового значения (из расширенной информации о статусе). Типичные значения: 1 = Человек, 2 = Эльф, 3 = Гаргулья. Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Race()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Race"]` → `BRIDGE CONTRACT -> IApiBridge.Race`

**Pascal compatibility signature:** `function Race: Byte;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Race()
```

---

## `UO.Random`

### Direct runtime overloads

- `UO.Random(arg1:Integer) -> Integer`
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
VAR result = UO.Random(0)
```

---

## `UO.RClick`

### Direct runtime overloads

- `UO.RClick(arg1:Integer, arg2:Integer) -> Unit`
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
UO.RClick(0, 0)
```

---

## `UO.RDblClick`

### Direct runtime overloads

- `UO.RDblClick(arg1:Integer, arg2:Integer) -> Unit`
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
UO.RDblClick(0, 0)
```

---

## `UO.ReadStaticsXY`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает все статические объекты в указанных мировых координатах в виде записи TStaticCell . X , Y — координаты тайла на карте. WorldNum — номер мира (фасета): 0 = Felucca, 1 = Trammel, 2 = Ilshenar, 3 = Malas, 4 = Tokuno, 5 = Ter Mur. Возвращаемый TStaticCell содержит массив Statics из записей TStaticItem и поле StaticCount . Каждая запись включает graphic тайла, абсолютные координаты X/Y, высоту Z и цвет статического объекта. Возвращает пустую запись (StaticCount = 0), если статика в данной позиции нет или персонаж не подключён. В Python метод возвращает список объектов StaticItemRealXY (словари с целочисленными значениями). В отличие от GetStaticTilesArray , которая ищет в прямоугольной области и возвращает TFoundTile (без цвета), ReadStaticsXY возвращает данные для одной позиции тайла с полной информацией, включая цвет.

### Current Yoko signatures / Return

- `UO.ReadStaticsXY(X, Y, WorldNum)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ReadStaticsXY"]` → `BRIDGE CONTRACT -> IApiBridge.GetStaticTiles`

**Pascal compatibility signature:** `function ReadStaticsXY(X: Word; Y: Word; WorldNum: Byte): TStaticCell;`

### Parameters

- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ReadStaticsXY(UO.GetX(self), UO.GetY(self), 0)
```

---

## `UO.Recall`

### Manifest-registered overloads

- `UO.Recall() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Recall(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Recall()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Recall(target)`
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
VAR result = UO.Recall()
```

```basic
UO.Recall(self)
```

---

## `UO.ReceiveObjectName`

### Direct runtime overloads

- `UO.ReceiveObjectName(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.ReceiveObjectName(arg1:Any, arg2:Any) -> Unit`
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
UO.ReceiveObjectName(0)
```

```basic
UO.ReceiveObjectName(0, 0)
```

---

## `UO.RemoveEarrings`

### Manifest-registered overloads

- `UO.RemoveEarrings() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.RemoveEarrings()`
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
VAR result = UO.RemoveEarrings()
```

```basic
UO.RemoveEarrings()
```

---

## `UO.RemoveFigure`

### Current Yoko signatures / Return

- `UO.RemoveFigure(FigureID) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** `1` if the figure existed and was removed from the visual World Map collection; `0` if the ID was not present.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.RemoveMapFigure` -> `WorldMapGump`.

### Parameters

- `FigureID` — ID previously returned by `UO.AddFigure`.

### Behavior

Removes the corresponding client-side overlay from `WorldMapGump` and from Yoko runtime figure state.

### Notes / limitations

Local client operation only; no server packet is sent.

### Examples

```basic
IF UO.RemoveFigure(figureId) = 0 THEN
    UO.Print('Figure already absent')
END IF
```

## `UO.RemoveFromParty`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет запрос на исключение указанного мобайла из группы (пати). ObjID — serial (ID) исключаемого члена группы. Только лидер группы может исключать других членов. Если персонаж не является лидером, сервер проигнорирует запрос. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.RemoveFromParty(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RemoveFromParty"]` → `BRIDGE CONTRACT -> IApiBridge.PartyRemove`

**Pascal compatibility signature:** `procedure RemoveFromParty(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.RemoveFromParty(self)
```

---

## `UO.RemoveHat`

### Manifest-registered overloads

- `UO.RemoveHat() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.RemoveHat()`
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
VAR result = UO.RemoveHat()
```

```basic
UO.RemoveHat()
```

---

## `UO.RemoveNeckless`

### Manifest-registered overloads

- `UO.RemoveNeckless() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.RemoveNeckless()`
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
VAR result = UO.RemoveNeckless()
```

```basic
UO.RemoveNeckless()
```

---

## `UO.RemoveRing`

### Manifest-registered overloads

- `UO.RemoveRing() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.RemoveRing()`
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
VAR result = UO.RemoveRing()
```

```basic
UO.RemoveRing()
```

---

## `UO.RemoveUserStatic`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Удаляет пользовательский статический объект по его идентификатору из локальных данных карты. ID — идентификатор пользовательского статика, возвращённый AddUserStatic (Python: CreateUserStatic ). Возвращает True , если статик найден и удалён, False — в противном случае. Пользовательские статики — это локальные дополнения к данным статических тайлов карты (добавляемые через AddUserStatic ). Они расширяют информацию UOData о статических ячейках и влияют на отрисовку карты и поиск пути локально. Возвращает False , если персонаж не подключён или данные UO не загружены.

### Current Yoko signatures / Return

- `UO.RemoveUserStatic(ID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RemoveUserStatic"]` → `STATE -> InjectionApiState.UserStatics` → `BRIDGE CONTRACT -> IApiBridge.RemoveUserStatic`

**Pascal compatibility signature:** `function RemoveUserStatic(ID: Integer): Boolean;`

### Parameters

- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.RemoveUserStatic(self)
```

---

## `UO.Rename`

### Manifest-registered overloads

- `UO.Rename(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Rename(mobile, newName)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `mobile` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `newName` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Rename(0, 0)
```

```basic
UO.Rename(self, 'value')
```

---

## `UO.RenameMobile`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос на переименование указанного мобайла. MobID — serial (ID) мобайла для переименования. NewName — новое имя. Переименование возможно только для мобайлов, для которых сервер разрешает переименование (обычно — собственные питомцы игрока). Сервер молча отклонит запрос, если мобайл не может быть переименован. Используйте MobileCanBeRenamed для предварительной проверки. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.RenameMobile(MobID, NewName)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RenameMobile"]` → `BRIDGE CONTRACT -> IApiBridge.RenameMobile`

**Pascal compatibility signature:** `procedure RenameMobile(MobID: Cardinal; NewName: String);`

### Parameters

- `MobID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `NewName` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.RenameMobile(self, 'value')
```

---
