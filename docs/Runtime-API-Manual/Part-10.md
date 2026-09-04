# Runtime API Manual — Part 10

Commands: **GetARStatus** through **GetFlying**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.GetARStatus`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает статус автопереподключения для текущего персонажа: True — включено, False — выключено.

### Current Yoko signatures / Return

- `UO.GetARStatus()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetARStatus"]` → `BRIDGE CONTRACT -> IApiBridge.GetAutoReconnect`

**Pascal compatibility signature:** `function GetARStatus: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetARStatus()
```

---

## `UO.GetAutoBuyDelay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает задержку (в миллисекундах), применяемую после каждой операции авто-покупки через AutoBuy или AutoBuyEx . Значение по умолчанию: 3 мс.

### Current Yoko signatures / Return

- `UO.GetAutoBuyDelay()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetAutoBuyDelay"]` → `STATE -> InjectionApiState.AutoBuyDelay` → `BRIDGE CONTRACT -> IApiBridge.GetAutoBuyDelay`

**Pascal compatibility signature:** `function GetAutoBuyDelay: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetAutoBuyDelay()
```

---

## `UO.GetAutoSellDelay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает задержку (в миллисекундах), применяемую после каждой операции авто-продажи через AutoSell . Значение по умолчанию: 3 мс.

### Current Yoko signatures / Return

- `UO.GetAutoSellDelay()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetAutoSellDelay"]` → `STATE -> InjectionApiState.AutoSellDelay` → `BRIDGE CONTRACT -> IApiBridge.GetAutoSellDelay`

**Pascal compatibility signature:** `function GetAutoSellDelay: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetAutoSellDelay()
```

---

## `UO.GetBuffBarInfo`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает список активных баффов и дебаффов персонажа. В Pascal возвращает TBuffBarInfo — запись с Count и массивом Buffs . В Python возвращает list[BuffBarInfo] . Если персонаж не подключён, возвращает запись с Count = 0 (Pascal) или пустой список (Python). Примечание: Поле Seconds в каждой записи баффа содержит длительность на момент применения , а не оставшееся время.

### Current Yoko signatures / Return

- `UO.GetBuffBarInfo()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetBuffBarInfo"]` → `BRIDGE CONTRACT -> IApiBridge.GetBuffBarInfo`

**Pascal compatibility signature:** `function GetBuffBarInfo: TBuffBarInfo;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetBuffBarInfo()
```

---

## `UO.GetCharsListForShard`

### Current Yoko signatures / Return

- `UO.GetCharsListForShard() -> Array[String]`
  - **Return type:** `Array`
  - **Return contract:** Array of non-empty character names known for the current shard. Empty array is valid when no character list has been received and no current character is available.

### Parameters

- None. The current selected/connected shard is used.

### Behavior

Returns the **actual character names received from the server's character-selection packet** for the current account/shard. ClassicUO caches that list in memory so the API can still return it after entering the world. If no cached list exists, the active `LoginScene.Characters` list is used; while already in game, the current player's name is the final fallback.

This command no longer returns the Yoko profile serial as a fake character list.

### Notes / limitations

- The list reflects what the server supplied for the current shard/account during this client session.
- It does not invent character names by scanning profile directories.
- Empty slots from the server character list are removed.

### Examples

```basic
VAR chars = UO.GetCharsListForShard()
UO.Print(chars)
```
---

## `UO.GetCliloc`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текст тултипа объекта с ObjID в виде готовой строки. Возвращает пустую строку, если у объекта нет тултипа. Синоним для GetTooltip . В Python метод называется GetTooltip . Для получения структурированных данных тултипа (cliloc ID с параметрами) используйте GetToolTipRec .

### Current Yoko signatures / Return

- `UO.GetCliloc(ObjID)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetCliloc"]` → `BRIDGE CONTRACT -> IApiBridge.GetTooltip`

**Pascal compatibility signature:** `function GetCliloc(ObjID: Cardinal): String;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetCliloc(self)
```

---

## `UO.GetClilocByID`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает локализованную cliloc-строку по указанному ClilocID . Если передан массив Params , метод подставляет значения параметров вместо токенов ~placeholder~ в шаблоне cliloc-строки. Параметры с префиксом # интерпретируются как вложенные cliloc ID и разрешаются рекурсивно. Возвращает пустую строку, если персонаж не подключён или файлы UO Data не загружены.

### Current Yoko signatures / Return

- `UO.GetClilocByID(ClilocID, Params)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetClilocByID"]` → `BRIDGE CONTRACT -> IApiBridge.GetClilocById`

**Pascal compatibility signature:** `function GetClilocByID(ClilocID: Cardinal; Params: TArray ): String;`

### Parameters

- `ClilocID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Params` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetClilocByID(self, 1000)
```

---

## `UO.GetColdResist`

### Direct runtime overloads

- `UO.GetColdResist() -> Integer`
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
VAR result = UO.GetColdResist()
```

---

## `UO.GetColor`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает цвет (hue) объекта с ObjID . Значение цвета 0 означает, что объект имеет свой цвет по умолчанию.

### Current Yoko signatures / Return

- `UO.GetColor(ObjID)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.GetColor"]`

**Pascal compatibility signature:** `function GetColor(ObjID: Cardinal): Word;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetColor(self)
```

---

## `UO.GetContent`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает содержимое контейнера с ID в виде массива записей TContentItemData . Каждая запись содержит серийный номер предмета, его graphic, цвет, позицию внутри контейнера, количество в стеке и ID родительского контейнера.

### Current Yoko signatures / Return

- `UO.GetContent(ID)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetContent"]` → `BRIDGE CONTRACT -> IApiBridge.GetContent`

**Pascal compatibility signature:** `function GetContent(ID: Cardinal): TArray ;`

### Parameters

- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetContent(self)
```

---

## `UO.GetContextMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает элементы последнего полученного контекстного меню в виде массива строк. Формат каждой строки: "tag|clilocID|clilocText|flags|color" (все числа в hex). Контекстное меню заполняется при ответе сервера на вызов RequestContextMenu . Используйте ClearContextMenu перед запросом нового меню.

### Current Yoko signatures / Return

- `UO.GetContextMenu()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetContextMenu"]` → `BRIDGE CONTRACT -> IApiBridge.GetContextMenu`

**Pascal compatibility signature:** `function GetContextMenu: TArray ;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetContextMenu()
```

---

## `UO.GetDead`

### Direct runtime overloads

- `UO.GetDead() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetDead(serial:Integer) -> Integer`
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
VAR result = UO.GetDead()
```

```basic
VAR result = UO.GetDead(self)
```

---

## `UO.GetDex`

### Current Yoko signatures / Return

- `UO.GetDex() -> Integer`
- `UO.GetDex(ObjID) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Returns the current player's Dexterity when called without arguments or when `ObjID=self`. For another mobile serial, the current ClassicUO world model does not expose that attribute and Yoko returns `0`.

### Parameters

- `ObjID` — optional mobile serial. In the current ClassicUO bridge, DEX is available only for the active player (`self`).

### Behavior

Reads Dexterity from `PlayerMobile`. `UO.GetDex()` is equivalent to reading the active player's value. `UO.GetDex(self)` reads the same value.

### Notes / limitations

- **SELF ONLY for a meaningful non-zero value in the current runtime.** ClassicUO's generic loaded `Mobile` object does not contain server-authoritative Dexterity; only `PlayerMobile` exposes it.
- Passing another mobile does not trigger a server stat request and returns `0` rather than fabricating data.
- `0` for another serial means “attribute unavailable through the current world model”, not necessarily that the mobile's real DEX is zero.
- This deliberately differs from historical Stealth descriptions that may imply arbitrary-mobile stat availability.

### Examples

```basic
VAR value = UO.GetDex()
UO.Print('DEX: ' + CStr(value))
```

```basic
VAR value = UO.GetDex(self)
```

## `UO.GetDexterity`

### Direct runtime overloads

- `UO.GetDexterity() -> Integer`
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
VAR result = UO.GetDexterity()
```

---

## `UO.GetDir`

### Direct runtime overloads

- `UO.GetDir(arg1:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.
- `UO.GetDir(arg1:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.
- `UO.GetDir() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetDir(0)
```

```basic
VAR result = UO.GetDir(0)
```

```basic
VAR result = UO.GetDir()
```

---

## `UO.GetDirection`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает направление (0–7), в котором обращён мобайл с ObjID . См. Directions для значений направлений. Примечание: Значение 0 (North) может быть как реальным направлением, так и значением по умолчанию для неподключённого/неизвестного персонажа.

### Current Yoko signatures / Return

- `UO.GetDirection(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetDirection"]` → `BRIDGE CONTRACT -> IApiBridge.GetDir`

**Pascal compatibility signature:** `function GetDirection(ObjID: Cardinal): Byte;`

### Additional current runtime overloads

- `UO.GetDirection() -> Integer`
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
VAR result = UO.GetDirection(self)
```

```basic
VAR result = UO.GetDirection()
```

---

## `UO.GetDistance`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает расстояние в тайлах от текущего персонажа до объекта с ObjID . Возвращает -1 , если объект не существует. Иначе возвращает расстояние в тайлах. В отличие от Dist (который принимает две произвольные пары координат), этот метод всегда измеряет от позиции текущего персонажа.

### Current Yoko signatures / Return

- `UO.GetDistance(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Tile distance. Object-based forms use -1 when the object is unavailable.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetDistance"]` → `BRIDGE CONTRACT -> IApiBridge.GetDistance`

**Pascal compatibility signature:** `function GetDistance(ObjID: Cardinal): Integer;`

### Additional current runtime overloads

- `UO.GetDistance(arg1:Integer, arg2:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Tile distance. Object-based forms use -1 when the object is unavailable.
- `UO.GetDistance(arg1:Any, arg2:Any, arg3:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Tile distance. Object-based forms use -1 when the object is unavailable.
- `UO.GetDistance(arg1:Integer, arg2:Integer, arg3:Integer, arg4:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Tile distance. Object-based forms use -1 when the object is unavailable.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Calculates tile distance. The 4-coordinate overload consumes both coordinate pairs; object forms resolve the object from the currently loaded world.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetDistance(self)
```

```basic
VAR result = UO.GetDistance(0, 0, 0, 0)
```

---

## `UO.GetEasyUO`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение глобальной переменной EasyUO по её индексу num . Переменные EasyUO — это устаревший механизм обмена данными между скриптами EasyUO и Stealth.

### Current Yoko signatures / Return

- `UO.GetEasyUO(num)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.GetEasyUO"]`

**Pascal compatibility signature:** `function GetEasyUO(num: Integer): String;`

### Parameters

- `num` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetEasyUO(0)
```

---

## `UO.GetEnergyResist`

### Direct runtime overloads

- `UO.GetEnergyResist() -> Integer`
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
VAR result = UO.GetEnergyResist()
```

---

## `UO.GetEquipment`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает список экипированных предметов мобайла с ID в виде массива записей TEquippedItemData .

### Current Yoko signatures / Return

- `UO.GetEquipment(ID)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetEquipment"]` → `BRIDGE CONTRACT -> IApiBridge.GetEquipment`

**Pascal compatibility signature:** `function GetEquipment(ID: Cardinal): TArray ;`

### Parameters

- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetEquipment(self)
```

---

## `UO.GetFindedList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает список ID объектов из последнего поиска через FindType , FindTypeEx , FindNotoriety и т. д. В Pascal заполняет TStringList ID в hex-формате и возвращает True при наличии результатов. В Python возвращает list[int] напрямую. Начиная с версии 7.9.0 доступна современная замена — GetFoundItems , возвращающая массив Cardinal напрямую без hex-преобразования. В Python эквивалентная функция — GetFoundList (алиас для GetFindedList ).

### Current Yoko signatures / Return

- `UO.GetFindedList(UserList)`
  - **Return type:** `Array`
  - **Return contract:** Adapted Array result; Yoko returns the list directly instead of mutating Pascal var/out.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetFindedList"]` → `BRIDGE CONTRACT -> IApiBridge.GetFoundItems`

**Pascal compatibility signature:** `function GetFindedList(var UserList: TStringList): Boolean;`

### Parameters

- `UserList` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Returns the found-list data directly as a Yoko Array. This adapts the historical Pascal var/out parameter instead of pretending to mutate an input argument.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetFindedList(0)
```

---

## `UO.GetFireResist`

### Direct runtime overloads

- `UO.GetFireResist() -> Integer`
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
VAR result = UO.GetFireResist()
```

---

## `UO.GetFlags`

### Direct runtime overloads

- `UO.GetFlags(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetFlags(0)
```

---

## `UO.GetFlying`

### Direct runtime overloads

- `UO.GetFlying() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetFlying(serial:Integer) -> Integer`
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
VAR result = UO.GetFlying()
```

```basic
VAR result = UO.GetFlying(self)
```

---
