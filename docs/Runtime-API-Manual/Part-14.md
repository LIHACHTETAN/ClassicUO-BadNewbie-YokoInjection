# Runtime API Manual — Part 14

Commands: **GetProfile** through **GetStaticArt**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.GetProfile`

### Direct runtime overloads

- `UO.GetProfile(arg1:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetProfile(0)
```

---

## `UO.GetQuantity`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает размер стека (количество) объекта с ObjID . Возвращает 1 для нестекируемых предметов. Возвращает 0 , если объект не существует.

### Current Yoko signatures / Return

- `UO.GetQuantity(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetQuantity"]` → `BRIDGE CONTRACT -> IApiBridge.GetQuantity`

**Pascal compatibility signature:** `function GetQuantity(ObjID: Cardinal): Integer;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetQuantity(self)
```

---

## `UO.GetQuestArrow`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает информацию о стрелке квеста/сокровища (большая серая стрелка в клиенте). В Pascal возвращает True , если стрелка активна, и заполняет параметр point координатами. Возвращает False , если стрелка не активна или персонаж отключён. В Python возвращает объект Point напрямую; валидность нужно проверять по его полям. Примечание: На некоторых шардах позиция стрелки может не соответствовать реальному расположению сокровища.

### Current Yoko signatures / Return

- `UO.GetQuestArrow(point)`
  - **Return type:** `Array`
  - **Return contract:** Adapted Array [exists, x, y] instead of mutating a Pascal var/out point.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetQuestArrow"]` → `BRIDGE CONTRACT -> IApiBridge.GetQuestArrow`

**Pascal compatibility signature:** `function GetQuestArrow(var point: TPoint): Boolean;`

### Parameters

- `point` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Returns the quest-arrow state directly as [exists, x, y]. This is the Yoko adaptation of the historical Pascal var/out point.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetQuestArrow(0)
```

---

## `UO.GetRace`

### Direct runtime overloads

- `UO.GetRace() -> Integer`
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
VAR result = UO.GetRace()
```

---

## `UO.GetResist`

### Direct runtime overloads

- `UO.GetResist(resistance:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `resistance` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetResist(0)
```

---

## `UO.GetResistCold`

### Direct runtime overloads

- `UO.GetResistCold() -> Integer`
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
VAR result = UO.GetResistCold()
```

---

## `UO.GetResistEnergy`

### Direct runtime overloads

- `UO.GetResistEnergy() -> Integer`
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
VAR result = UO.GetResistEnergy()
```

---

## `UO.GetResistFire`

### Direct runtime overloads

- `UO.GetResistFire() -> Integer`
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
VAR result = UO.GetResistFire()
```

---

## `UO.GetResistPhysical`

### Direct runtime overloads

- `UO.GetResistPhysical() -> Integer`
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
VAR result = UO.GetResistPhysical()
```

---

## `UO.GetResistPoison`

### Direct runtime overloads

- `UO.GetResistPoison() -> Integer`
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
VAR result = UO.GetResistPoison()
```

---

## `UO.GetRun`

### Direct runtime overloads

- `UO.GetRun() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.GetRun(arg1:Any) -> Integer`
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
VAR result = UO.GetRun()
```

```basic
VAR result = UO.GetRun(0)
```

---

## `UO.GetRunMountTimer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает задержку (в миллисекундах) между шагами при беге в верхом (на лошади и т. д.), используемую функциями Move* и Step*.

### Current Yoko signatures / Return

- `UO.GetRunMountTimer()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetRunMountTimer"]` → `STATE -> InjectionApiState.RunMountTimer`

**Pascal compatibility signature:** `function GetRunMountTimer: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetRunMountTimer()
```

---

## `UO.GetRunUnMountTimer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает задержку (в миллисекундах) между шагами при беге пешком (без маунта), используемую функциями Move* и Step*.

### Current Yoko signatures / Return

- `UO.GetRunUnMountTimer()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetRunUnMountTimer"]` → `STATE -> InjectionApiState.RunUnmountTimer`

**Pascal compatibility signature:** `function GetRunUnmountTimer: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetRunUnMountTimer()
```

---

## `UO.GetScriptName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя скрипта с индексом ScriptIndex . Возвращает пустую строку, если скрипт с данным индексом не существует.

### Current Yoko signatures / Return

- `UO.GetScriptName(ScriptIndex)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetScriptName"]` → `BRIDGE CONTRACT -> IApiBridge.GetScriptName`

**Pascal compatibility signature:** `function GetScriptName(ScriptIndex: Word): String;`

### Parameters

- `ScriptIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetScriptName(0)
```

---

## `UO.GetScriptPath`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает полный путь к файлу скрипта с индексом ScriptIndex . Возвращает пустую строку, если скрипт с данным индексом не существует.

### Current Yoko signatures / Return

- `UO.GetScriptPath(ScriptIndex)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetScriptPath"]` → `BRIDGE CONTRACT -> IApiBridge.GetScriptPath`

**Pascal compatibility signature:** `function GetScriptPath(ScriptIndex: Word): String;`

### Parameters

- `ScriptIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetScriptPath(0)
```

---

## `UO.GetScriptsCount`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает общее количество активных скриптов текущего персонажа. В Python метод называется GetScriptCount .

### Current Yoko signatures / Return

- `UO.GetScriptsCount()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetScriptsCount"]` → `BRIDGE CONTRACT -> IApiBridge.GetScriptsCount`

**Pascal compatibility signature:** `function GetScriptsCount: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetScriptsCount()
```

---

## `UO.GetScriptsList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает список всех активных скриптов текущего персонажа. В нормальных условиях содержит как минимум одну запись (вызывающий скрипт). Каждый элемент — запись TScriptItemInfo , содержащая индекс скрипта в списке скриптов Stealth.

### Current Yoko signatures / Return

- `UO.GetScriptsList()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetScriptsList"]` → `BRIDGE CONTRACT -> IApiBridge.GetScriptsList`

**Pascal compatibility signature:** `function GetScriptsList: TArray ;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetScriptsList()
```

---

## `UO.GetScriptState`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает состояние выполнения скрипта с индексом ScriptIndex . Возвращает st_Unknown , если скрипт с данным индексом не существует.

### Current Yoko signatures / Return

- `UO.GetScriptState(ScriptIndex)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetScriptState"]` → `BRIDGE CONTRACT -> IApiBridge.GetScriptState`

**Pascal compatibility signature:** `function GetScriptState(ScriptIndex: Word): TScriptState;`

### Parameters

- `ScriptIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetScriptState(0)
```

---

## `UO.GetSerial`

### Direct runtime overloads

- `UO.GetSerial(arg1:String) -> String`
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
VAR result = UO.GetSerial(0)
```

---

## `UO.GetSex`

### Direct runtime overloads

- `UO.GetSex() -> Integer`
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
VAR result = UO.GetSex()
```

---

## `UO.GetShopList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает содержимое последнего списка товаров вендора в виде массива строк. Формат каждой строки: "Nr: N|ID:|$ID|type|$Type|Color|$Color|Name|Name|Price|Price|Cliloc|Tooltip|Quantity|Qty" . Список товаров заполняется, когда игрок открывает меню покупки у вендора (командой “buy” или через контекстное меню).

### Current Yoko signatures / Return

- `UO.GetShopList()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.GetShopList"]`

**Pascal compatibility signature:** `function GetShopList: TArray ;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetShopList()
```

---

## `UO.GetSkillCap`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает максимальное значение (кап) указанного навыка. В Pascal навык задаётся именем (строка). В Python — индексом (целое число). Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetSkillCap(SkillName)`
  - **Return type:** `Decimal`
  - **Return contract:** Decimal numeric runtime value.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetSkillCap"]` → `BRIDGE CONTRACT -> IApiBridge.GetSkillValue`

**Pascal compatibility signature:** `function GetSkillCap(SkillName: String): Double;`

### Parameters

- `SkillName` — String/text value interpreted according to the command.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetSkillCap('value')
```

---

## `UO.GetSkillCurrentValue`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущее значение навыка с учётом модификаторов (баффы, бонусы от экипировки и т. д.). Для базового значения без модификаторов используйте GetSkillValue . В Pascal навык задаётся именем (строка). В Python — индексом (целое число). Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetSkillCurrentValue(SkillName)`
  - **Return type:** `Decimal`
  - **Return contract:** Decimal numeric runtime value.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetSkillCurrentValue"]` → `BRIDGE CONTRACT -> IApiBridge.GetSkillValue`

**Pascal compatibility signature:** `function GetSkillCurrentValue(SkillName: String): Double;`

### Parameters

- `SkillName` — String/text value interpreted according to the command.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetSkillCurrentValue('value')
```

---

## `UO.GetSkillLockState`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает состояние блокировки указанного навыка. Значения: 0 = навык растёт (стрелка вверх), 1 = навык падает (стрелка вниз), 2 = навык заблокирован.

### Current Yoko signatures / Return

- `UO.GetSkillLockState(SkillName)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetSkillLockState"]` → `BRIDGE CONTRACT -> IApiBridge.GetSkillLockState`

**Pascal compatibility signature:** `function GetSkillLockState(SkillName: String): ShortInt;`

### Parameters

- `SkillName` — String/text value interpreted according to the command.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetSkillLockState('value')
```

---

## `UO.GetSkillValue`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает базовое значение навыка без модификаторов (без баффов, без бонусов экипировки). Для эффективного значения с модификаторами используйте GetSkillCurrentValue . В Pascal навык задаётся именем (строка). В Python — индексом (целое число). Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.GetSkillValue(SkillName)`
  - **Return type:** `Decimal`
  - **Return contract:** Decimal numeric runtime value.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetSkillValue"]` → `BRIDGE CONTRACT -> IApiBridge.GetSkillValue`

**Pascal compatibility signature:** `function GetSkillValue(SkillName: String): Double;`

### Parameters

- `SkillName` — String/text value interpreted according to the command.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GetSkillValue('value')
```

---

## `UO.GetStam`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущую выносливость (stamina) мобайла с ObjID .

### Current Yoko signatures / Return

- `UO.GetStam(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetStam"]` → `BRIDGE CONTRACT -> IApiBridge.GetStamina` → `BRIDGE CONTRACT -> IApiBridge.Stamina`

**Pascal compatibility signature:** `function GetStam(ObjID: Cardinal): Integer;`

### Additional current runtime overloads

- `UO.GetStam() -> Integer`
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
VAR result = UO.GetStam(self)
```

```basic
VAR result = UO.GetStam()
```

---

## `UO.GetStamina`

### Direct runtime overloads

- `UO.GetStamina() -> Integer`
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
VAR result = UO.GetStamina()
```

---

## `UO.GetStaticArt`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает объект TBitmap для статик-арта с указанным ObjType и Hue . Если Hue = 0 , арт берётся с оригинальными цветами. Возвращает nil (Pascal) или пустой буфер (Python), если персонаж не подключён или файлы UO Data не загружены. В Python метод называется GetStaticArtBitmap и возвращает содержимое BMP-файла в виде list[int] — BMP используется как единственный формат, гарантированно совместимый с Delphi TBitmap.

### Current Yoko signatures / Return

- `UO.GetStaticArt(ObjType, Hue)`
  - **Return type:** `Array`
  - **Return contract:** Byte Array containing a complete 24-bit BMP image; empty array means no decodable art.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetStaticArt"]` → `BRIDGE CONTRACT -> IApiBridge.GetStaticArt`

**Pascal compatibility signature:** `function GetStaticArt(ObjType: Cardinal; Hue: Word): TBitmap;`

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Hue` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Behavior

Loads the requested static art from the active ClassicUO asset loaders (MUL/UOP), applies hue/partial-hue rules and encodes a complete 24-bit BMP byte array.

### Notes / limitations

Requires decodable art assets in the active ClassicUO data source. Empty Array means art is unavailable/undecodable.

### Examples

```basic
VAR result = UO.GetStaticArt(0x0190, -1)
```

---
