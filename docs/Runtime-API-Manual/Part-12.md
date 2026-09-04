# Runtime API Manual — Part 12

Commands: **GetInfo** through **GetMobile**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.GetInfo`

### Direct runtime overloads

- `UO.GetInfo(arg1:String) -> String`
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
VAR result = UO.GetInfo(0)
```

---

## `UO.GetInt`

### Current Yoko signatures / Return

- `UO.GetInt() -> Integer`
- `UO.GetInt(ObjID) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Returns the current player's Intelligence when called without arguments or when `ObjID=self`. For another mobile serial, the current ClassicUO world model does not expose that attribute and Yoko returns `0`.

### Parameters

- `ObjID` — optional mobile serial. In the current ClassicUO bridge, INT is available only for the active player (`self`).

### Behavior

Reads Intelligence from `PlayerMobile`. `UO.GetInt()` is equivalent to reading the active player's value. `UO.GetInt(self)` reads the same value.

### Notes / limitations

- **SELF ONLY for a meaningful non-zero value in the current runtime.** ClassicUO's generic loaded `Mobile` object does not contain server-authoritative Intelligence; only `PlayerMobile` exposes it.
- Passing another mobile does not trigger a server stat request and returns `0` rather than fabricating data.
- `0` for another serial means “attribute unavailable through the current world model”, not necessarily that the mobile's real INT is zero.
- This deliberately differs from historical Stealth descriptions that may imply arbitrary-mobile stat availability.

### Examples

```basic
VAR value = UO.GetInt()
UO.Print('INT: ' + CStr(value))
```

```basic
VAR value = UO.GetInt(self)
```

## `UO.GetIntelligence`

### Direct runtime overloads

- `UO.GetIntelligence() -> Integer`
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
VAR result = UO.GetIntelligence()
```

---

## `UO.GetLandscapeTile`

### Direct runtime overloads

- `UO.GetLandscapeTile(arg1:Any, arg2:Any, arg3:Any) -> Array`
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
VAR result = UO.GetLandscapeTile(0, 0, 0)
```

---

## `UO.GetLandTileAt`

### Direct runtime overloads

- `UO.GetLandTileAt(arg1:Any, arg2:Any) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
- `UO.GetLandTileAt(arg1:Any, arg2:Any, arg3:Any) -> Array`
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
VAR result = UO.GetLandTileAt(0, 0)
```

```basic
VAR result = UO.GetLandTileAt(0, 0, 0)
```

---

## `UO.GetLandTileData`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает детальную информацию о ландшафтном тайле, включая флаги и имя, в виде записи TLandTileData . Значение Tile можно получить из GetMapCell .

### Current Yoko signatures / Return

- `UO.GetLandTileData(Tile)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetLandTileData"]`

**Pascal compatibility signature:** `function GetLandTileData(Tile: Word): TLandTileData;`

### Parameters

- `Tile` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetLandTileData(0)
```

---

## `UO.GetLandTilesArray`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет ландшафтные тайлы типа TileType в прямоугольной области ( Xmin , Ymin ) – ( Xmax , Ymax ) в мире WorldNum . В Python TileTypes — список (поддерживает поиск нескольких типов одновременно).

### Current Yoko signatures / Return

- `UO.GetLandTilesArray(Xmin, Ymin, Xmax, Ymax, WorldNum, TileType)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetLandTilesArray"]`

**Pascal compatibility signature:** `function GetLandTilesArray(Xmin: Word; Ymin: Word; Xmax: Word; Ymax: Word; WorldNum: Byte; TileType: Word): TFoundTilesArray;`

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
VAR result = UO.GetLandTilesArray(0, 0, 0, 0, 0, 0x0190)
```

---

## `UO.GetLandTilesArrayEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Как GetLandTilesArray , но ищет несколько типов ландшафтных тайлов сразу в прямоугольной области ( Xmin , Ymin ) – ( Xmax , Ymax ) в мире WorldNum . TileTypes — массив график тайлов для поиска: все ландшафтные тайлы, чья графика есть в списке, собираются в один общий результат.

### Current Yoko signatures / Return

- `UO.GetLandTilesArrayEx(Xmin, Ymin, Xmax, Ymax, WorldNum, TileTypes)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetLandTilesArrayEx"]`

**Pascal compatibility signature:** `function GetLandTilesArrayEx(Xmin: Word; Ymin: Word; Xmax: Word; Ymax: Word; WorldNum: Byte; TileTypes: array of Word): TFoundTilesArray;`

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
VAR result = UO.GetLandTilesArrayEx(0, 0, 0, 0, 0, 0x0190)
```

---

## `UO.GetLastMenuItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает все элементы последнего (новейшего) активного меню в виде списка строк. Не возвращает ничего, если нет активного меню или персонаж не подключён. Для других способов получения меню см. GetMenuItems и GetMenuItemsEx .

### Current Yoko signatures / Return

- `UO.GetLastMenuItems()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetLastMenuItems"]` → `BRIDGE CONTRACT -> IApiBridge.GetLastMenuItems`

**Pascal compatibility signature:** `function GetLastMenuItems: TArray ;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetLastMenuItems()
```

---

## `UO.GetLayer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает слой экипировки, на котором находится объект с ObjID . Перебирает все слои персонажа и сравнивает объект на каждом слое с ObjID . Возвращает 0 , если персонаж не подключён или объект не найден.

### Current Yoko signatures / Return

- `UO.GetLayer(ObjID)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.GetLayer"]`

**Pascal compatibility signature:** `function GetLayer(ObjID: Cardinal): Byte;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetLayer(self)
```

---

## `UO.GetLayerCount`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает количество статических слоёв в указанной позиции карты ( X , Y ) в мире WorldNum . Устаревший: Метод внутри вызывает ReadStaticsXY . Рекомендуется вызывать ReadStaticsXY напрямую и проверять поле StaticCount .

### Current Yoko signatures / Return

- `UO.GetLayerCount(X, Y, WorldNum)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetLayerCount"]` → `BRIDGE CONTRACT -> IApiBridge.GetStaticTiles`

**Pascal compatibility signature:** `function GetLayerCount(X: Word; Y: Word; WorldNum: Byte): Byte;`

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
VAR result = UO.GetLayerCount(UO.GetX(self), UO.GetY(self), 0)
```

---

## `UO.GetLife`

### Direct runtime overloads

- `UO.GetLife() -> Integer`
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
VAR result = UO.GetLife()
```

---

## `UO.GetLocked`

### Direct runtime overloads

- `UO.GetLocked(arg1:Any) -> Integer`
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
VAR result = UO.GetLocked(0)
```

---

## `UO.GetLuck`

### Direct runtime overloads

- `UO.GetLuck() -> Integer`
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
VAR result = UO.GetLuck()
```

---

## `UO.GetMana`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущую ману мобайла с ObjID .

### Current Yoko signatures / Return

- `UO.GetMana(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMana"]` → `BRIDGE CONTRACT -> IApiBridge.GetMana` → `BRIDGE CONTRACT -> IApiBridge.Mana`

**Pascal compatibility signature:** `function GetMana(ObjID: Cardinal): Integer;`

### Additional current runtime overloads

- `UO.GetMana() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetMana(self)
```

```basic
VAR result = UO.GetMana()
```

---

## `UO.GetMapCell`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает информацию о ячейке карты (ландшафта) по указанным координатам, включая графику тайла и уровень Z. В Python метод называется GetCell .

### Current Yoko signatures / Return

- `UO.GetMapCell(X, Y, WorldNum)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMapCell"]` → `BRIDGE CONTRACT -> IApiBridge.GetLandscapeTile`

**Pascal compatibility signature:** `function GetMapCell(X: Word; Y: Word; WorldNum: Byte): TMapCell;`

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
VAR result = UO.GetMapCell(UO.GetX(self), UO.GetY(self), 0)
```

---

## `UO.GetMaxHP`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает максимальные HP мобайла с ObjID .

### Current Yoko signatures / Return

- `UO.GetMaxHP(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMaxHP"]` → `BRIDGE CONTRACT -> IApiBridge.GetMaxHP` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetMaxHP(ObjID: Cardinal): Integer;`

### Additional current runtime overloads

- `UO.GetMaxHP() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetMaxHP(self)
```

```basic
VAR result = UO.GetMaxHP()
```

---

## `UO.GetMaxLife`

### Direct runtime overloads

- `UO.GetMaxLife() -> Integer`
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
VAR result = UO.GetMaxLife()
```

---

## `UO.GetMaxMana`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает максимальную ману мобайла с ObjID .

### Current Yoko signatures / Return

- `UO.GetMaxMana(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMaxMana"]` → `BRIDGE CONTRACT -> IApiBridge.GetMaxMana` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetMaxMana(ObjID: Cardinal): Integer;`

### Additional current runtime overloads

- `UO.GetMaxMana() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetMaxMana(self)
```

```basic
VAR result = UO.GetMaxMana()
```

---

## `UO.GetMaxStam`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает максимальную выносливость (stamina) мобайла с ObjID .

### Current Yoko signatures / Return

- `UO.GetMaxStam(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMaxStam"]` → `BRIDGE CONTRACT -> IApiBridge.GetMaxStamina` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetMaxStam(ObjID: Cardinal): Integer;`

### Additional current runtime overloads

- `UO.GetMaxStam() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetMaxStam(self)
```

```basic
VAR result = UO.GetMaxStam()
```

---

## `UO.GetMaxStamina`

### Direct runtime overloads

- `UO.GetMaxStamina() -> Integer`
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
VAR result = UO.GetMaxStamina()
```

---

## `UO.GetMaxWeight`

### Direct runtime overloads

- `UO.GetMaxWeight() -> Integer`
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
VAR result = UO.GetMaxWeight()
```

---

## `UO.GetMenuItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает все элементы активного меню с заголовком Caption в виде списка строк.

### Current Yoko signatures / Return

- `UO.GetMenuItems(Caption)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMenuItems"]` → `BRIDGE CONTRACT -> IApiBridge.GetMenuItems`

**Pascal compatibility signature:** `function GetMenuItems(Caption: String): TArray ;`

### Parameters

- `Caption` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetMenuItems(0)
```

---

## `UO.GetMenuItemsEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает все элементы активного меню с заголовком Caption в виде массива записей TMenuResponse , предоставляя структурированный доступ к модели, цвету и тексту. Возвращает пустой массив, если подходящее меню не найдено или персонаж не подключён. Для строкового вывода используйте GetMenuItems .

### Current Yoko signatures / Return

- `UO.GetMenuItemsEx(Caption)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMenuItemsEx"]` → `BRIDGE CONTRACT -> IApiBridge.GetMenuItems`

**Pascal compatibility signature:** `function GetMenuItemsEx(Caption: String): TMenuResponses;`

### Parameters

- `Caption` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetMenuItemsEx(0)
```

---

## `UO.GetMobile`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает детальные данные о мобайле с ID в виде записи TMobileData .

### Current Yoko signatures / Return

- `UO.GetMobile(ID)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMobile"]` → `BRIDGE CONTRACT -> IApiBridge.GetDir` → `BRIDGE CONTRACT -> IApiBridge.GetHP` → `BRIDGE CONTRACT -> IApiBridge.GetMaxHP` → `BRIDGE CONTRACT -> IApiBridge.GetName` → `BRIDGE CONTRACT -> IApiBridge.GetNotoriety`

**Pascal compatibility signature:** `function GetMobile(ID: Cardinal): TMobileData;`

### Parameters

- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetMobile(self)
```

---
