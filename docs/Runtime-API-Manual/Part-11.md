# Runtime API Manual — Part 11

Commands: **GetFollowers** through **GetIgnoreList**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.GetFollowers`

### Direct runtime overloads

- `UO.GetFollowers() -> Integer`
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
VAR result = UO.GetFollowers()
```

---

## `UO.GetFollowersMax`

### Direct runtime overloads

- `UO.GetFollowersMax() -> Integer`
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
VAR result = UO.GetFollowersMax()
```

---

## `UO.GetFoundedText`

### Direct runtime overloads

- `UO.GetFoundedText() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetFoundedText()
```

---

## `UO.GetFoundedTextColor`

### Direct runtime overloads

- `UO.GetFoundedTextColor() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetFoundedTextColor()
```

---

## `UO.GetFoundedTextID`

### Direct runtime overloads

- `UO.GetFoundedTextID() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetFoundedTextID()
```

---

## `UO.GetFoundedTextIndex`

### Direct runtime overloads

- `UO.GetFoundedTextIndex() -> Integer`
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
VAR result = UO.GetFoundedTextIndex()
```

---

## `UO.GetFoundedTextSerial`

### Direct runtime overloads

- `UO.GetFoundedTextSerial() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetFoundedTextSerial()
```

---

## `UO.GetFoundedTextTimer`

### Direct runtime overloads

- `UO.GetFoundedTextTimer() -> Integer`
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
VAR result = UO.GetFoundedTextTimer()
```

---

## `UO.GetFoundItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Современная замена для GetFindedList . Возвращает результаты поиска в виде массива Cardinal. Если ничего не найдено, возвращает пустой массив. Поиск выполняется через FindType , FindTypeEx , FindNotoriety , FindTypesArrayEx и т. д. В отличие от GetFindedList , который заполняет TStringList строками в hex-формате, этот метод возвращает числовые ID напрямую — без необходимости преобразования. В Python эквивалентная функция — GetFoundList (алиас для GetFindedList , который уже возвращает list[int] ).

### Current Yoko signatures / Return

- `UO.GetFoundItems()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetFoundItems"]` → `BRIDGE CONTRACT -> IApiBridge.GetFoundItems`

**Pascal compatibility signature:** `function GetFoundItems: TCardinalDynArray;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetFoundItems()
```

---

## `UO.GetFrozen`

### Direct runtime overloads

- `UO.GetFrozen() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetFrozen(serial:Integer) -> Integer`
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
VAR result = UO.GetFrozen()
```

```basic
VAR result = UO.GetFrozen(self)
```

---

## `UO.GetGlobal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение глобальной переменной VarName из указанного GlobalRegion . В Pascal GlobalRegion — строка: 'stealth' (видна всем персонажам) или 'char' (видна только скриптам текущего персонажа). Регистронезависимо. В Python GlobalRegion принимает enum Global : Global.Stealth (0) или Global.Char (1).

### Current Yoko signatures / Return

- `UO.GetGlobal(GlobalRegion, VarName)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGlobal"]` → `STATE -> InjectionApiState.GlobalVariables`

**Pascal compatibility signature:** `function GetGlobal(GlobalRegion: String; VarName: String): String;`

### Additional current runtime overloads

- `UO.GetGlobal(arg1:String) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `GlobalRegion` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `VarName` — String/text value interpreted according to the command.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGlobal(0, 'value')
```

```basic
VAR result = UO.GetGlobal(0)
```

---

## `UO.GetGold`

### Direct runtime overloads

- `UO.GetGold() -> Integer`
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
VAR result = UO.GetGold()
```

---

## `UO.GetGraphic`

### Direct runtime overloads

- `UO.GetGraphic(arg1:String) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
- `UO.GetGraphic(arg1:Integer) -> String`
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
VAR result = UO.GetGraphic(0)
```

```basic
VAR result = UO.GetGraphic(0)
```

---

## `UO.GetGump`

### Direct runtime overloads

- `UO.GetGump(arg1:String) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant. Numeric gump identifiers (buttonlen/button/textlen/injid/replyed/inclient/objectcount) return Integer; other identifiers return String. Missing numeric values become 0 and missing text becomes empty string.
- `UO.GetGump(arg1:String, arg2:Integer) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant. Numeric gump identifiers (buttonlen/button/textlen/injid/replyed/inclient/objectcount) return Integer; other identifiers return String. Missing numeric values become 0 and missing text becomes empty string.
- `UO.GetGump(arg1:Integer, arg2:String) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant. Numeric gump identifiers (buttonlen/button/textlen/injid/replyed/inclient/objectcount) return Integer; other identifiers return String. Missing numeric values become 0 and missing text becomes empty string.
- `UO.GetGump(arg1:Integer, arg2:String, arg3:Integer) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant. Numeric gump identifiers (buttonlen/button/textlen/injid/replyed/inclient/objectcount) return Integer; other identifiers return String. Missing numeric values become 0 and missing text becomes empty string.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGump(0)
```

```basic
VAR result = UO.GetGump(0, 0, 0)
```

---

## `UO.GetGumpButtonsDescription`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает описания кнопок гампа с индексом GumpIndex в списке гампов. Содержит информацию только о кнопках (в отличие от GetGumpShortLines или GetGumpFullLines , которые включают другие элементы). Не возвращает ничего, если индекс гампа вне диапазона или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetGumpButtonsDescription(GumpIndex)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGumpButtonsDescription"]` → `BRIDGE CONTRACT -> IApiBridge.GetGumpButtonsDescription`

**Pascal compatibility signature:** `function GetGumpButtonsDescription(GumpIndex: Word): TArray ;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpButtonsDescription(0)
```

---

## `UO.GetGumpCount`

### Direct runtime overloads

- `UO.GetGumpCount() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpCount()
```

---

## `UO.GetGumpFullLines`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает полную информацию о гампе с индексом GumpIndex — включает все элементы, текстовые строки, кнопки и структурные детали. Не возвращает ничего, если индекс гампа вне диапазона или персонаж не подключён. Для частичной информации см. GetGumpShortLines (текст + кнопки) или GetGumpButtonsDescription (только кнопки).

### Current Yoko signatures / Return

- `UO.GetGumpFullLines(GumpIndex)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGumpFullLines"]` → `BRIDGE CONTRACT -> IApiBridge.GetGumpFullLines`

**Pascal compatibility signature:** `function GetGumpFullLines(GumpIndex: Word): TArray ;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpFullLines(0)
```

---

## `UO.GetGumpID`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает ID гампа с индексом GumpIndex в списке гампов Stealth. Возвращает 0 , если индекс вне диапазона или персонаж не подключён. Примечание: Gump ID может быть уникальным для каждого типа гампа, но это не гарантировано — зависит от шарда.

### Current Yoko signatures / Return

- `UO.GetGumpID(GumpIndex)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGumpID"]` → `BRIDGE CONTRACT -> IApiBridge.GetGumpId`

**Pascal compatibility signature:** `function GetGumpID(GumpIndex: Word): Cardinal;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpID(0)
```

---

## `UO.GetGumpInfo`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает полную структурированную информацию о гампе с индексом GumpIndex в виде записи TGumpInfo . Запись содержит все элементы гампа: кнопки, текстовые поля, чекбоксы, радиокнопки, изображения, HTML-области и многое другое. Возвращает пустую запись, если индекс вне диапазона или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetGumpInfo(GumpIndex)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGumpInfo"]` → `STATE -> InjectionApiState.IgnoredGumpIds` → `STATE -> InjectionApiState.IgnoredGumpSerials` → `BRIDGE CONTRACT -> IApiBridge.GetGumpButtonsDescription` → `BRIDGE CONTRACT -> IApiBridge.GetGumpFullLines` → `BRIDGE CONTRACT -> IApiBridge.GetGumpId`

**Pascal compatibility signature:** `function GetGumpInfo(GumpIndex: Word): TGumpInfo;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpInfo(0)
```

---

## `UO.GetGumpsCount`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает количество активных гампов текущего персонажа. Возвращает 0 , если персонаж не подключён или гампов нет. Обычно используется как GetGumpsCount - 1 для обращения к последнему (новейшему) гампу в списке.

### Current Yoko signatures / Return

- `UO.GetGumpsCount()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGumpsCount"]` → `BRIDGE CONTRACT -> IApiBridge.GetGumpCount`

**Pascal compatibility signature:** `function GetGumpsCount: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpsCount()
```

---

## `UO.GetGumpSerial`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер гампа с индексом GumpIndex в списке гампов Stealth. Возвращает 0 , если индекс вне диапазона или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetGumpSerial(GumpIndex)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGumpSerial"]` → `BRIDGE CONTRACT -> IApiBridge.GetGumpSerial`

**Pascal compatibility signature:** `function GetGumpSerial(GumpIndex: Word): Cardinal;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpSerial(0)
```

---

## `UO.GetGumpShortLines`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает сокращённую информацию о гампе с индексом GumpIndex — только текстовые поля, текстовые строки и кнопки. Не возвращает ничего, если индекс гампа вне диапазона или персонаж не подключён. Для полной информации используйте GetGumpFullLines . Для кнопок — GetGumpButtonsDescription .

### Current Yoko signatures / Return

- `UO.GetGumpShortLines(GumpIndex)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGumpShortLines"]` → `BRIDGE CONTRACT -> IApiBridge.GetGumpShortLines`

**Pascal compatibility signature:** `function GetGumpShortLines(GumpIndex: Word): TArray ;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpShortLines(0)
```

---

## `UO.GetGumpTextLines`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает только текстовые строки гампа с индексом GumpIndex , без информации о структуре элементов. Не возвращает ничего, если индекс гампа вне диапазона или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetGumpTextLines(GumpIndex)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGumpTextLines"]` → `BRIDGE CONTRACT -> IApiBridge.GetGumpTextLines`

**Pascal compatibility signature:** `function GetGumpTextLines(GumpIndex: Word): TArray ;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetGumpTextLines(0)
```

---

## `UO.GetHidden`

### Direct runtime overloads

- `UO.GetHidden() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.GetHidden(serial:Integer) -> Integer`
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
VAR result = UO.GetHidden()
```

```basic
VAR result = UO.GetHidden(self)
```

---

## `UO.GetHP`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущие HP (очки здоровья) мобайла с ObjID . Если HP и MaxHP мобайла равны 0 и он жив, Stealth автоматически запрашивает обновлённую статистику с сервера. Возвращает 0 , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetHP(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetHP"]` → `BRIDGE CONTRACT -> IApiBridge.GetHP` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function GetHP(ObjID: Cardinal): Integer;`

### Additional current runtime overloads

- `UO.GetHP() -> Integer`
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
VAR result = UO.GetHP(self)
```

```basic
VAR result = UO.GetHP()
```

---

## `UO.GetIgnoreList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущий список игнорирования (заполняется через Ignore , очищается через IgnoreReset ).

### Current Yoko signatures / Return

- `UO.GetIgnoreList()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetIgnoreList"]` → `BRIDGE CONTRACT -> IApiBridge.GetIgnoreList`

**Pascal compatibility signature:** `function GetIgnoreList: TArray ;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetIgnoreList()
```

---
