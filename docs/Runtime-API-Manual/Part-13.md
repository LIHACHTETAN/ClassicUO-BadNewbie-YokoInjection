# Runtime API Manual — Part 13

Commands: **GetMobiles** through **GetPrice**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.GetMobiles`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает данные всех известных мобайлов в виде массива записей TMobileData .

### Current Yoko runtime signatures / Return

- `UO.GetMobiles() -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of loaded mobile serials; an empty array is valid.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMobiles"]` → `BRIDGE CONTRACT -> IApiBridge.GetMobiles`
- `UO.GetMobiles(distance) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of loaded mobile serials; an empty array is valid.
- `UO.GetMobiles(distance, notoriety) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of loaded mobile serials; an empty array is valid.
- `UO.GetMobiles(distance, notoriety, body) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of loaded mobile serials; an empty array is valid.
- `UO.GetMobiles(distance, notoriety, body, maxZ) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of loaded mobile serials; an empty array is valid.
- `UO.GetMobiles(distance, notoriety, body, maxZ, nearest) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of loaded mobile serials; an empty array is valid.
- `UO.GetMobiles(distance, notoriety, body, maxZ, nearest, includeSelf) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of loaded mobile serials; an empty array is valid.

### Historical compatibility reference

- Pascal: `function GetMobiles: TArray ;`
- Historical Yoko/Stealth syntax: `UO.GetMobiles()`

### Parameters

- `distance` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.
- `notoriety` — Actual ClassicUO Mobile.Notoriety value or supported mask/string form; it is not inferred from hue/name/body.
- `body` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `maxZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.
- `nearest` — Boolean ordering flag. TRUE selects/orders nearest matches first; FALSE preserves the runtime search order.
- `includeSelf` — Boolean. TRUE allows the player mobile to be included; FALSE excludes self.

### Behavior

Enumerates loaded World.Mobiles only; ordinary Item objects are excluded. Optional filters and nearest ordering are applied by the shared Search Core.

### Notes / limitations

Only currently loaded mobiles can be returned. Objects outside the loaded ClassicUO world are unavailable to this call.

### Examples

```basic
VAR result = UO.GetMobiles()
```

```basic
VAR result = UO.GetMobiles(18, 5, 0x0190, 12, TRUE, TRUE)
```

---

## `UO.GetMultiAllParts`

### Current Yoko signatures / Return

- `UO.GetMultiAllParts(MultiID) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Returns an array of loaded components for the specified ClassicUO house/multi serial. Returns an empty array when that multi is not loaded.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.GetMultiAllParts` -> `World.HouseManager` / `House.Components`.

### Parameters

- `MultiID` — serial of the currently loaded house/multi.

### Behavior

Reads the actual loaded ClassicUO multi/house component collection. Each returned component is a Yoko array with this layout:

`[graphic, hue, x, y, z, multiOffsetX, multiOffsetY, multiOffsetZ, multiSerial]`

The first five values describe the rendered world component; the offset fields are the component's coordinates relative to its multi; the last value identifies the owning multi.

### Notes / limitations

- Works on **currently loaded** house/multi data in `World.HouseManager`.
- It does not parse an arbitrary offline facet or arbitrary multi definition that is not loaded in the current world.
- Destroyed components are excluded.
- Empty result means the multi is not loaded or has no live components.

### Examples

```basic
VAR parts = UO.GetMultiAllParts(multiSerial)
UO.Print('Multi parts: ' + CStr(GetArrayLength(parts)))
```

## `UO.GetMultiPartsAtPosition`

### Current Yoko signatures / Return

- `UO.GetMultiPartsAtPosition(X, Y) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Returns all loaded house/multi components occupying world tile X/Y. Returns an empty array when no loaded multi component occupies that tile.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.GetMultiPartsAtPosition` -> `World.HouseManager.Houses` / `House.GetMultiAt`.

### Parameters

- `X` — world X coordinate.
- `Y` — world Y coordinate.

### Behavior

Searches every currently loaded ClassicUO house/multi and returns components located at the requested world tile. Each component uses the same layout as `GetMultiAllParts`:

`[graphic, hue, x, y, z, multiOffsetX, multiOffsetY, multiOffsetZ, multiSerial]`

### Notes / limitations

- Searches only multis currently present in `World.HouseManager`.
- This is loaded-world data, not an offline arbitrary-map/facet parser.
- Destroyed components are excluded.

### Examples

```basic
VAR parts = UO.GetMultiPartsAtPosition(UO.GetX(self), UO.GetY(self))
UO.Print('Multi parts here: ' + CStr(GetArrayLength(parts)))
```

# Other Runtime API

## `UO.GetMultis`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает все мульти-объекты (дома, лодки) из кеша Stealth в виде массива записей TMultiItem . Возвращает пустой массив, если мульти-объектов нет, файлы UO Data не загружены, или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetMultis()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetMultis"]` → `BRIDGE CONTRACT -> IApiBridge.GetWorldItems` → `BRIDGE CONTRACT -> IApiBridge.IsHouse`

**Pascal compatibility signature:** `function GetMultis: TArray ;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetMultis()
```

---

## `UO.GetName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя объекта с ObjID . Возвращает "NoName" , если персонаж не подключён или имя не было отправлено сервером. В некоторых случаях нужно сначала вызвать ClickOnObject для запроса имени с сервера. Примечание: Для предметов (не мобайлов) на версиях клиента 4.x+ имена обычно не отправляются сервером. Используйте GetTooltip .

### Current Yoko signatures / Return

- `UO.GetName(ObjID)`
  - **Return type:** `String`
  - **Return contract:** String player name/title value; empty string is possible when the value is unavailable.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetName"]` → `BRIDGE CONTRACT -> IApiBridge.GetName` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetName(ObjID: Cardinal): String;`

### Additional current runtime overloads

- `UO.GetName() -> String`
  - **Return type:** `String`
  - **Return contract:** String player name/title value; empty string is possible when the value is unavailable.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetName(self)
```

```basic
VAR result = UO.GetName()
```

---

## `UO.GetNextStepZ`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Вычисляет ожидаемый уровень Z для следующего шага из ( CurrX , CurrY ) в направлении ( DestX , DestY ) в мире WorldNum , начиная с CurrZ . Возвращает 0 , если персонаж не подключён или файлы UO Data не загружены.

### Current Yoko signatures / Return

- `UO.GetNextStepZ(CurrX, CurrY, DestX, DestY, WorldNum, CurrZ)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetNextStepZ"]` → `BRIDGE CONTRACT -> IApiBridge.CheckWorldStep`

**Pascal compatibility signature:** `function GetNextStepZ(CurrX: Word; CurrY: Word; DestX: Word; DestY: Word; WorldNum: Byte; CurrZ: ShortInt): ShortInt;`

### Parameters

- `CurrX` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `CurrY` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `DestX` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `DestY` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.
- `CurrZ` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetNextStepZ(0, 0, 0, 0, 0, 0)
```

---

## `UO.GetNotoriety`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение нотариетета мобайла с ObjID (см. таблицу выше).

### Current Yoko signatures / Return

- `UO.GetNotoriety(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetNotoriety"]` → `BRIDGE CONTRACT -> IApiBridge.GetNotoriety`

**Pascal compatibility signature:** `function GetNotoriety(ObjID: Cardinal): Byte;`

### Additional current runtime overloads

- `UO.GetNotoriety() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetNotoriety(self)
```

```basic
VAR result = UO.GetNotoriety()
```

---

## `UO.GetParalisa`

### Direct runtime overloads

- `UO.GetParalisa() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetParalisa(serial:Integer) -> Integer`
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
VAR result = UO.GetParalisa()
```

```basic
VAR result = UO.GetParalisa(self)
```

---

## `UO.GetParalysed`

### Direct runtime overloads

- `UO.GetParalysed() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetParalysed(serial:Integer) -> Integer`
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
VAR result = UO.GetParalysed()
```

```basic
VAR result = UO.GetParalysed(self)
```

---

## `UO.GetParalyzed`

### Direct runtime overloads

- `UO.GetParalyzed() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetParalyzed(serial:Integer) -> Integer`
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
VAR result = UO.GetParalyzed()
```

```basic
VAR result = UO.GetParalyzed(self)
```

---

## `UO.GetParent`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает ID родительского контейнера объекта с ObjID . Возвращает 0 , если персонаж не подключён, предмет не найден, или объект не имеет родителя (например, лежит на земле).

### Current Yoko signatures / Return

- `UO.GetParent(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetParent"]` → `BRIDGE CONTRACT -> IApiBridge.ContainerOf`

**Pascal compatibility signature:** `function GetParent(ObjID: Cardinal): Cardinal;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetParent(self)
```

---

## `UO.GetPathArray`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Строит текущую переносимую последовательность шагов от X/Y/Z персонажа к Xdst/Ydst и возвращает массив точек [X, Y, Z]. Каждая прямая или диагональная клетка проверяется через ClassicUO CheckWorldStep. Если прямая последовательность заблокирована, функция возвращает пустой массив; полный обход препятствий A* ClassicUO здесь не выполняется. Optimized принимается, но текущим fallback Yoko игнорируется. Accuracy ограничивается диапазоном 0–20. GetArrayLength(result) возвращает количество рассчитанных точек, GetPathArray3D позволяет явно указать начальный и конечный Z, а newMoveXY использует Player.Pathfinder.WalkTo с обходом препятствий.

### Current Yoko signatures / Return

- `UO.GetPathArray(Xdst, Ydst, Optimized, Accuracy)`
  - **Return type:** `Array`
  - **Return contract:** Array of path points; empty array means no usable path.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetPathArray"]` → `BRIDGE CONTRACT -> IApiBridge.GetX` → `BRIDGE CONTRACT -> IApiBridge.GetY` → `BRIDGE CONTRACT -> IApiBridge.GetZ` → `BRIDGE CONTRACT -> IApiBridge.Self` → `BRIDGE CONTRACT -> IApiBridge.WorldNumber`

**Pascal compatibility signature:** `function GetPathArray(Xdst: Word; Ydst: Word; Optimized: Boolean; Accuracy: Integer): TPathArray;`

### Parameters

- `Xdst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Ydst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Optimized` — Boolean path/movement optimization flag; changes the runtime path strategy/heuristic where supported.
- `Accuracy` — Allowed XY destination tolerance in tiles.

### Behavior

Builds a path using the ClassicUO pathfinder and returns the resulting point array; optimization flags affect the registered path strategy.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetPathArray(0, 0, TRUE, 0)
```

---

## `UO.GetPathArray3D`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Строит текущую переносимую последовательность 3D-шагов от StartX/StartY/StartZ к FinishX/FinishY/FinishZ. Каждый элемент результата — точка [X, Y, Z]. Каждая следующая прямая или диагональная клетка проверяется через ClassicUO CheckWorldStep, включая рассчитанный Z. При блокировке прямой последовательности процедура прекращает расчёт и возвращает пустой массив; полный обход препятствий A* ClassicUO здесь не запускается. AccuracyXY ограничивается диапазоном 0–20. Текущий fallback Yoko принимает AccuracyZ и Run для совместимости исходников, но не использует их; API Inspector отмечает оба аргумента как игнорируемые. Количество рассчитанных 3D-точек возвращает GetArrayLength(result). Для маршрута ClassicUO с обходом препятствий используйте newMoveXY, который вызывает Player.Pathfinder.WalkTo.

### Current Yoko signatures / Return

- `UO.GetPathArray3D(StartX, StartY, StartZ, FinishX, FinishY, FinishZ, WorldNum, AccuracyXY, AccuracyZ, Run)`
  - **Return type:** `Array`
  - **Return contract:** Array of [X,Y,Z] path points; empty array means no usable path.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetPathArray3D"]`

**Pascal compatibility signature:** `function GetPathArray3D(StartX: Word; StartY: Word; StartZ: ShortInt; FinishX: Word; FinishY: Word; FinishZ: ShortInt; WorldNum: Byte; AccuracyXY: Integer; AccuracyZ: Integer; Run: Boolean): TPathArray;`

### Parameters

- `StartX` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `StartY` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `StartZ` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `FinishX` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `FinishY` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `FinishZ` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.
- `AccuracyXY` — Allowed XY destination tolerance in tiles.
- `AccuracyZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.
- `Run` — Boolean movement flag. TRUE requests running steps where the client/server allow it.

### Behavior

Builds a 3D path and returns X/Y/Z points. AccuracyZ is part of the destination condition and Run influences step sequencing.

### Notes / limitations

An empty array is a valid no-path result. The path is based on the currently loaded map and client collision data.

### Examples

```basic
VAR result = UO.GetPathArray3D(0, 0, 0, 0, 0, 0, 0, 0, 12, TRUE)
```

---

## `UO.GetPauseScriptOnDisconnectStatus`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает состояние настройки «Пауза скрипта при отключении»: True — включено, False — выключено. Когда включено, скрипт автоматически ставится на паузу при отключении и возобновляется при переподключении.

### Current Yoko signatures / Return

- `UO.GetPauseScriptOnDisconnectStatus()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetPauseScriptOnDisconnectStatus"]` → `BRIDGE CONTRACT -> IApiBridge.GetPauseScriptOnDisconnectStatus`

**Pascal compatibility signature:** `function GetPauseScriptOnDisconnectStatus: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetPauseScriptOnDisconnectStatus()
```

---

## `UO.GetPetsCurrent`

### Direct runtime overloads

- `UO.GetPetsCurrent() -> Integer`
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
VAR result = UO.GetPetsCurrent()
```

---

## `UO.GetPetsMax`

### Direct runtime overloads

- `UO.GetPetsMax() -> Integer`
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
VAR result = UO.GetPetsMax()
```

---

## `UO.GetPhysicalResist`

### Direct runtime overloads

- `UO.GetPhysicalResist() -> Integer`
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
VAR result = UO.GetPhysicalResist()
```

---

## `UO.GetPing`

### Direct runtime overloads

- `UO.GetPing() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Last measured 0x73 server-echo RTT in milliseconds; 0 means no valid sample.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Returns the last measured RTT from the actual 0x73 server echo tracked by NetStatistics.

### Notes / limitations

0 means no valid 0x73 RTT sample has been recorded yet; it is not an ICMP ping measurement.

### Examples

```basic
VAR result = UO.GetPing()
```

---

## `UO.GetPlayerStatusText`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает строку статуса мобайла с ObjID .

### Current Yoko signatures / Return

- `UO.GetPlayerStatusText(ObjID)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetPlayerStatusText"]` → `BRIDGE CONTRACT -> IApiBridge.GetHP` → `BRIDGE CONTRACT -> IApiBridge.GetMaxHP` → `BRIDGE CONTRACT -> IApiBridge.GetName`

**Pascal compatibility signature:** `function GetPlayerStatusText(ObjID: Cardinal): String;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetPlayerStatusText(self)
```

---

## `UO.GetPoisoned`

### Direct runtime overloads

- `UO.GetPoisoned() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetPoisoned(serial:Integer) -> Integer`
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
VAR result = UO.GetPoisoned()
```

```basic
VAR result = UO.GetPoisoned(self)
```

---

## `UO.GetPoisonResist`

### Direct runtime overloads

- `UO.GetPoisonResist() -> Integer`
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
VAR result = UO.GetPoisonResist()
```

---

## `UO.GetPrice`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает цену объекта с ObjID . Актуально для предметов в списке товаров вендора.

### Current Yoko signatures / Return

- `UO.GetPrice(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetPrice"]` → `BRIDGE CONTRACT -> IApiBridge.GetPrice`

**Pascal compatibility signature:** `function GetPrice(ObjID: Cardinal): Cardinal;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetPrice(self)
```

---
