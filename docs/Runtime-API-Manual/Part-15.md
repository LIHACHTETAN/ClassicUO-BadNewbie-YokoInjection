# Runtime API Manual — Part 15

Commands: **GetStaticTileAt** through **GetUserStatics**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `524c4a06be8a621b5b5e24dabc4795c2c7da682f9c23e0b516f2de0a437ee254`

---

## `UO.GetStaticTileAt`

### Direct runtime overloads

- `UO.GetStaticTileAt(arg1:Any, arg2:Any, arg3:Any) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
- `UO.GetStaticTileAt(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetStaticTileAt(0, 0, 0)
```

```basic
VAR result = UO.GetStaticTileAt(0, 0, 0, 0)
```

---

## `UO.GetStaticTileData`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает детальную информацию о статическом тайле, включая флаги, вес, высоту и имя, в виде записи TStaticTileData .

### Current Yoko signatures / Return

- `UO.GetStaticTileData(Tile)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetStaticTileData"]`

**Pascal compatibility signature:** `function GetStaticTileData(Tile: Word): TStaticTileData;`

### Parameters

- `Tile` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetStaticTileData(0)
```

---

## `UO.GetStaticTiles`

### Direct runtime overloads

- `UO.GetStaticTiles(arg1:Any, arg2:Any, arg3:Any) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetStaticTiles(0, 0, 0)
```

---

## `UO.GetStaticTilesArray`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет статические тайлы типа TileType в прямоугольной области ( Xmin , Ymin ) – ( Xmax , Ymax ) в мире WorldNum . В Python TileTypes — список (поддерживает поиск нескольких типов одновременно).

### Current Yoko signatures / Return

- `UO.GetStaticTilesArray(Xmin, Ymin, Xmax, Ymax, WorldNum, TileType)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetStaticTilesArray"]`

**Pascal compatibility signature:** `function GetStaticTilesArray(Xmin: Word; Ymin: Word; Xmax: Word; Ymax: Word; WorldNum: Byte; TileType: Word): TFoundTilesArray;`

### Parameters

- `Xmin` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Ymin` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Xmax` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Ymax` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.
- `TileType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetStaticTilesArray(0, 0, 0, 0, 0, 0x0190)
```

---

## `UO.GetStaticTilesArrayEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Как GetStaticTilesArray , но ищет несколько типов статических тайлов сразу в прямоугольной области ( Xmin , Ymin ) – ( Xmax , Ymax ) в мире WorldNum . TileTypes — массив график тайлов для поиска: все статические тайлы, чья графика есть в списке, собираются в один общий результат.

### Current Yoko signatures / Return

- `UO.GetStaticTilesArrayEx(Xmin, Ymin, Xmax, Ymax, WorldNum, TileTypes)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetStaticTilesArrayEx"]`

**Pascal compatibility signature:** `function GetStaticTilesArrayEx(Xmin: Word; Ymin: Word; Xmax: Word; Ymax: Word; WorldNum: Byte; TileTypes: array of Word): TFoundTilesArray;`

### Parameters

- `Xmin` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Ymin` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Xmax` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Ymax` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.
- `TileTypes` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetStaticTilesArrayEx(0, 0, 0, 0, 0, 0x0190)
```

---

## `UO.GetStatLockState`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает состояние блокировки указанной характеристики. statNum : 0 = STR, 1 = DEX, 2 = INT (см. константы Stats ). Значения: 0 = растёт, 1 = падает, 2 = заблокирована.

### Current Yoko signatures / Return

- `UO.GetStatLockState(statNum)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetStatLockState"]` → `BRIDGE CONTRACT -> IApiBridge.GetStatLockState`

**Pascal compatibility signature:** `function GetStatLockState(statNum: Byte): ShortInt;`

### Parameters

- `statNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetStatLockState(0)
```

---

## `UO.GetStatus`

### Direct runtime overloads

- `UO.GetStatus(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.GetStatus(arg1:Integer) -> Unit`
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
UO.GetStatus(0)
```

```basic
UO.GetStatus(0)
```

---

## `UO.GetStr`

### Current Yoko signatures / Return

- `UO.GetStr() -> Integer`
- `UO.GetStr(ObjID) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Returns the current player's Strength when called without arguments or when `ObjID=self`. For another mobile serial, the current ClassicUO world model does not expose that attribute and Yoko returns `0`.

### Parameters

- `ObjID` — optional mobile serial. In the current ClassicUO bridge, STR is available only for the active player (`self`).

### Behavior

Reads Strength from `PlayerMobile`. `UO.GetStr()` is equivalent to reading the active player's value. `UO.GetStr(self)` reads the same value.

### Notes / limitations

- **SELF ONLY for a meaningful non-zero value in the current runtime.** ClassicUO's generic loaded `Mobile` object does not contain server-authoritative Strength; only `PlayerMobile` exposes it.
- Passing another mobile does not trigger a server stat request and returns `0` rather than fabricating data.
- `0` for another serial means “attribute unavailable through the current world model”, not necessarily that the mobile's real STR is zero.
- This deliberately differs from historical Stealth descriptions that may imply arbitrary-mobile stat availability.

### Examples

```basic
VAR value = UO.GetStr()
UO.Print('STR: ' + CStr(value))
```

```basic
VAR value = UO.GetStr(self)
```

## `UO.GetStrength`

### Direct runtime overloads

- `UO.GetStrength() -> Integer`
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
VAR result = UO.GetStrength()
```

---

## `UO.GetSurfaceZ`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает среднюю высоту поверхности (Z) ландшафтных тайлов в указанной точке карты. Это значение используется при расчёте пути и позволяет определить уровень проходимой поверхности в заданной точке. X — координата X на карте. Y — координата Y на карте. WorldNum — номер карты (фасета): 0 = Felucca, 1 = Trammel и т.д. Возвращает 0 , если персонаж не подключён или данные карты недоступны.

### Current Yoko signatures / Return

- `UO.GetSurfaceZ(X, Y, WorldNum)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetSurfaceZ"]` → `BRIDGE CONTRACT -> IApiBridge.GetSurfaceZ`

**Pascal compatibility signature:** `function GetSurfaceZ(X: Word; Y: Word; WorldNum: Byte): ShortInt;`

### Parameters

- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetSurfaceZ(UO.GetX(self), UO.GetY(self), 0)
```

---

## `UO.GetTileFlags`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает «сырые» флаги указанного тайла в виде беззнакового целого. Group — категория тайла: 1 — ландшафтный, 2 — статический. Любое другое значение возвращает 0 . Tile — графический ID (тип) тайла. Возвращаемое значение — битовая маска. Для декодирования в набор имён флагов используйте ConvertIntegerToFlags . Возвращает 0 , если персонаж не подключён, данные карты недоступны или Group не равен 1 или 2 .

### Current Yoko signatures / Return

- `UO.GetTileFlags(Group, Tile)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.GetTileFlags"]`

**Pascal compatibility signature:** `function GetTileFlags(Group: Byte; Tile: Word): Cardinal;`

### Parameters

- `Group` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Tile` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTileFlags(0, 0)
```

---

## `UO.GetTileHeight`

### Direct runtime overloads

- `UO.GetTileHeight(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTileHeight(0, 0)
```

---

## `UO.GetTileLayer`

### Direct runtime overloads

- `UO.GetTileLayer(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTileLayer(0, 0)
```

---

## `UO.GetTileName`

### Direct runtime overloads

- `UO.GetTileName(arg1:Any, arg2:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTileName(0, 0)
```

---

## `UO.GetTileXYM`

### Direct runtime overloads

- `UO.GetTileXYM(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any, arg6:Any) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg6` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTileXYM(0, 0, 0, 0, 0, 0)
```

---

## `UO.GetTitle`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает титул (суффикс) объекта или мобила с указанным ObjID . Для NPC и игроков титул — это профессия или тег гильдии, отображаемые после имени (например, «the blacksmith», «the mage»). ObjID — ID объекта или мобила. Возвращает пустую строку, если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetTitle(ObjID)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetTitle"]` → `BRIDGE CONTRACT -> IApiBridge.GetTitle` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetTitle(ObjID: Cardinal): String;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTitle(self)
```

---

## `UO.GetTooltip`

### Current Yoko signatures / Return

- `UO.GetTooltip(ObjID) -> String`
  - **Return type:** `String`
  - **Return contract:** Returns concatenated tooltip/OPL text. Returns `""` when no tooltip arrives within the bounded wait or the object is invalid/unavailable.

### Parameters

- `ObjID` — object/mobile serial.

### Behavior

Reads the current Object Property List. If the OPL is not cached yet, Yoko requests it from the shard and waits up to approximately **200 ms**, polling without blocking the ClassicUO UI thread. If data arrives, the object name and property text are combined into one string.

### Notes / limitations

A timeout is not an exception; the result is an empty string. Server latency can require retrying later. Use `GetTooltipRec` when individual cliloc IDs are required.

### Examples

```basic
VAR tip = UO.GetTooltip(lasttarget)
IF tip <> '' THEN
    UO.Print(tip)
END IF
```

---

## `UO.GetTooltipRec`

### Current Yoko signatures / Return

- `UO.GetTooltipRec(ObjID) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Returns the available cliloc IDs for the object's structured OPL data. An empty array means no structured data was available within the bounded wait.

### Parameters

- `ObjID` — object/mobile serial. `0` returns an empty result immediately.

### Behavior

If structured OPL data is not cached, requests it and waits up to approximately **120 ms** without blocking the UI thread.

### Notes / limitations

This is a Yoko array adaptation of the historical structured tooltip record.

### Examples

```basic
VAR clilocs = UO.GetTooltipRec(lasttarget)
```

---

## `UO.GetTradeContainer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает ID контейнера в указанном окне безопасного обмена. TradeNum — индекс активного окна обмена (начиная с 1, как возвращает TradeCount ). Num — какой контейнер получить: 1 — ваш собственный, 2 — контейнер оппонента. Возвращает 0 , если Num не равен 1 или 2 , окно обмена не существует или персонаж не подключён. Полученный ID контейнера можно передать в GetContent или методы поиска для просмотра предметов внутри.

### Current Yoko signatures / Return

- `UO.GetTradeContainer(TradeNum, Num)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetTradeContainer"]` → `BRIDGE CONTRACT -> IApiBridge.GetTradeContainer`

**Pascal compatibility signature:** `function GetTradeContainer(TradeNum: Byte; Num: Byte): Cardinal;`

### Parameters

- `TradeNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Num` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTradeContainer(0, 0)
```

---

## `UO.GetTradeOpponent`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) оппонента в указанном окне безопасного обмена. TradeNum — индекс активного окна обмена (начиная с 1, как возвращает TradeCount ). Возвращает 0 , если окно обмена не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetTradeOpponent(TradeNum)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetTradeOpponent"]` → `BRIDGE CONTRACT -> IApiBridge.GetTradeOpponent`

**Pascal compatibility signature:** `function GetTradeOpponent(TradeNum: Byte): Cardinal;`

### Parameters

- `TradeNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTradeOpponent(0)
```

---

## `UO.GetTradeOpponentName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя оппонента в указанном окне безопасного обмена. TradeNum — индекс активного окна обмена (начиная с 1, как возвращает TradeCount ). Возвращает пустую строку, если окно обмена не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetTradeOpponentName(TradeNum)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetTradeOpponentName"]` → `BRIDGE CONTRACT -> IApiBridge.GetTradeOpponentName`

**Pascal compatibility signature:** `function GetTradeOpponentName(TradeNum: Byte): String;`

### Parameters

- `TradeNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetTradeOpponentName(0)
```

---

## `UO.GetType`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает графический тип (art ID) объекта с указанным ObjID . ObjID — ID объекта или мобила. Если 0 , немедленно возвращает 0 . Возвращает 0 , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetType(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetType"]` → `BRIDGE CONTRACT -> IApiBridge.GetGraphics`

**Pascal compatibility signature:** `function GetType(ObjID: Cardinal): Word;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetType(self)
```

---

## `UO.GetUserCodepage`

### Direct runtime overloads

- `UO.GetUserCodepage() -> Integer`
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
VAR result = UO.GetUserCodepage()
```

---

## `UO.GetUserStatic`

### Direct runtime overloads

- `UO.GetUserStatic(arg1:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetUserStatic(0)
```

---

## `UO.GetUserStatics`

### Direct runtime overloads

- `UO.GetUserStatics() -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetUserStatics()
```

---
