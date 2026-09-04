# Runtime API Manual — Part 20

Commands: **IsWorldCellPassable** through **LineCount**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.IsWorldCellPassable`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Проверяет, можно ли пройти из текущей ячейки в целевую, учитывая рельеф, статику и динамические объекты. CurrX , CurrY , CurrZ — координаты текущей позиции. DestX , DestY — координаты целевой ячейки. DestZ (Pascal) — параметр var ; при возврате содержит рассчитанную Z-координату целевой ячейки. WorldNum — номер карты (фасета). Pascal: Возвращает True , если ячейка проходима. Параметр DestZ обновляется значением Z на целевой позиции. Python: Возвращает кортеж (passable: bool, dest_z: int) — флаг проходимости и рассчитанную Z-координату. Возвращает False , если персонаж не подключён или данные карты не загружены.

### Current Yoko signatures / Return

- `UO.IsWorldCellPassable(CurrX, CurrY, CurrZ, DestX, DestY, var DestZ, WorldNum)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsWorldCellPassable"]` → `BRIDGE CONTRACT -> IApiBridge.CheckWorldStep`

**Pascal compatibility signature:** `function IsWorldCellPassable(CurrX: Word; CurrY: Word; CurrZ: ShortInt; DestX: Word; DestY: Word; var DestZ: ShortInt; WorldNum: Byte): Boolean;`

### Parameters

- `CurrX` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `CurrY` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `CurrZ` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `DestX` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `DestY` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `var DestZ` — World/tile Z coordinate.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.

### Behavior

Evaluates passability against the currently loaded world/map data and uses the destination Z input in the passability result/fallback semantics.

### Notes / limitations

Only the currently loaded map/facet is authoritative. DestZ participates in the result and is not a dummy parameter.

### Examples

```basic
VAR result = UO.IsWorldCellPassable(0, 0, 0, 0, 0, 0, 0)
```

---

## `UO.IsYellowHits`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если у указанного мобайла жёлтая полоса здоровья (указывает на неуязвимость или особый статус), иначе False . ObjID — ID мобайла для проверки. Возвращает False , если объект не существует или персонаж не подключён. Примечание: Этот флаг был актуален только для ранних версий Ultima Online. Современные серверы больше не присылают этот флаг. Метод сохранён для обратной совместимости.

### Current Yoko signatures / Return

- `UO.IsYellowHits(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsYellowHits"]` → `BRIDGE CONTRACT -> IApiBridge.GetYellowBar` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function IsYellowHits(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsYellowHits(self)
```

---

## `UO.Journal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текст журнала по указанному индексу строки. StringIndex — индекс строки (как возвращают InJournal , HighJournal , LowJournal и т.д.). После успешного извлечения свойства Line* обновляются данными из найденной записи. Возвращает пустую строку, если строка с указанным индексом не существует. В этом случае свойства Line* очищаются.

### Current Yoko signatures / Return

- `UO.Journal(StringIndex)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Journal"]`

**Pascal compatibility signature:** `function Journal(StringIndex: Integer): String;`

### Parameters

- `StringIndex` — String/text value interpreted according to the command.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Journal('value')
```

---

## `UO.JournalColor`

### Direct runtime overloads

- `UO.JournalColor(arg1:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.JournalColor(0)
```

---

## `UO.JournalSerial`

### Direct runtime overloads

- `UO.JournalSerial(arg1:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.JournalSerial(0)
```

---

## `UO.JournalTimer`

### Direct runtime overloads

- `UO.JournalTimer(arg1:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.JournalTimer(0)
```

---

## `UO.KeyPress`

### Direct runtime overloads

- `UO.KeyPress(arg1:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.KeyPress(arg1:Integer, arg2:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.KeyPress(arg1:Integer, arg2:Integer, arg3:Integer) -> Unit`
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
UO.KeyPress(0)
```

```basic
UO.KeyPress(0, 0)
```

```basic
UO.KeyPress(0, 0, 0)
```

---

## `UO.LastAttack`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) последнего мобайла, которого атаковал персонаж. Возвращает 0 , если персонаж никого не атаковал.

### Current Yoko signatures / Return

- `UO.LastAttack()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LastAttack"]` → `BRIDGE CONTRACT -> IApiBridge.LastAttack`

**Pascal compatibility signature:** `function LastAttack: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastAttack()
```

---

## `UO.LastContainer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) последнего контейнера, который был открыт или с которым взаимодействовали. Возвращает 0 , если ни один контейнер не был открыт.

### Current Yoko signatures / Return

- `UO.LastContainer()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LastContainer"]` → `BRIDGE CONTRACT -> IApiBridge.GetLastContainer`

**Pascal compatibility signature:** `function LastContainer: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastContainer()
```

---

## `UO.LastGump`

### Direct runtime overloads

- `UO.LastGump(arg1:String) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant with the same field-dependent Integer/String conversion as GetGump.
- `UO.LastGump(arg1:String, arg2:Integer) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant with the same field-dependent Integer/String conversion as GetGump.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastGump(0)
```

```basic
VAR result = UO.LastGump(0, 0)
```

---

## `UO.LastJournalMessage`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текст последней (самой новой) записи журнала. После вызова свойства Line* обновляются данными из последней записи журнала. Возвращает пустую строку, если журнал пуст.

### Current Yoko signatures / Return

- `UO.LastJournalMessage()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LastJournalMessage"]`

**Pascal compatibility signature:** `function LastJournalMessage: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastJournalMessage()
```

---

## `UO.LastMessage`

### Direct runtime overloads

- `UO.LastMessage() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastMessage()
```

---

## `UO.LastObject`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) последнего объекта, который был использован через UseObject , UseType или аналогичные методы. Возвращает 0 , если ни один объект не был использован.

### Current Yoko signatures / Return

- `UO.LastObject()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LastObject"]` → `BRIDGE CONTRACT -> IApiBridge.GetLastObject`

**Pascal compatibility signature:** `function LastObject: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastObject()
```

---

## `UO.LastStatus`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) последнего мобайла или объекта, для которого был получен статус. Возвращает 0 , если статус ещё не был получен.

### Current Yoko signatures / Return

- `UO.LastStatus()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LastStatus"]` → `BRIDGE CONTRACT -> IApiBridge.LastStatus`

**Pascal compatibility signature:** `function LastStatus: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastStatus()
```

---

## `UO.LastStatusX`

### Direct runtime overloads

- `UO.LastStatusX() -> Integer`
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
VAR result = UO.LastStatusX()
```

---

## `UO.LastStatusY`

### Direct runtime overloads

- `UO.LastStatusY() -> Integer`
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
VAR result = UO.LastStatusY()
```

---

## `UO.LastStepQUsedDoor`

### Current Yoko signatures / Return

- `UO.LastStepQUsedDoor() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Returns `1` when the latest `StepQ` recognized and attempted to open a real door in the requested direction; otherwise `0`.
- `UO.LastStepQUsedDoor(value) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Compatibility setter/getter form; returns the stored value.

### Parameters

- `value` — compatibility state value for the setter form.

### Behavior

When `moveOpenDoor` is enabled, `StepQ` now probes the actual ClassicUO door in the step direction and updates this state automatically before queuing the step. If no represented door is found, the normal OpenDoor fallback is still attempted but the automatic recognized-door flag remains `0`.

### Notes / limitations

The automatic value represents a door recognized by ClassicUO's world object model. A shard-specific/fallback open-door action with no represented door object cannot be positively identified.

### Examples

```basic
UO.StepQ(2, True)
IF UO.LastStepQUsedDoor() = 1 THEN
    UO.Print('Door used by StepQ')
END IF
```

---

## `UO.LastTarget`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) последнего объекта или мобайла, на который был применен таргет. Возвращает 0 , если таргет ещё не был выбран.

### Current Yoko signatures / Return

- `UO.LastTarget()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LastTarget"]` → `BRIDGE CONTRACT -> IApiBridge.LastTarget`

**Pascal compatibility signature:** `function LastTarget: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastTarget()
```

---

## `UO.LastTargetX`

### Direct runtime overloads

- `UO.LastTargetX() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastTargetX()
```

---

## `UO.LastTargetY`

### Direct runtime overloads

- `UO.LastTargetY() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastTargetY()
```

---

## `UO.LastTile`

### Direct runtime overloads

- `UO.LastTile() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
- `UO.LastTile(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LastTile()
```

```basic
VAR result = UO.LastTile(0)
```

---

## `UO.Launch`

### Direct runtime overloads

- `UO.Launch(arg1:String) -> Unit`
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
UO.Launch(0)
```

---

## `UO.LClick`

### Direct runtime overloads

- `UO.LClick(arg1:Integer, arg2:Integer) -> Unit`
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
UO.LClick(0, 0)
```

---

## `UO.LDblClick`

### Direct runtime overloads

- `UO.LDblClick(arg1:Integer, arg2:Integer) -> Unit`
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
UO.LDblClick(0, 0)
```

---

## `UO.Life`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Фактически это вызов GetHP с параметром Self . Для проверки здоровья других мобайлов используйте GetHP . Returns 0 if the character is not connected. Возвращает текущее количество очков здоровья персонажа. HP — алиас для этого метода. Фактически это вызов GetHP с параметром Self . Для проверки здоровья других мобайлов используйте GetHP . Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Life()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Life"]` → `BRIDGE CONTRACT -> IApiBridge.GetHP` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function Life: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Life()
```

---

## `UO.Light`

### Manifest-registered overloads

- `UO.Light() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Light(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Light()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Light(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `value` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Light()
```

```basic
UO.Light('value')
```

---

## `UO.LineCount`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает количество совпадений, найденных последним вызовом InJournal или InJournalBetweenTimes . Это свойство обновляется после каждой операции поиска по журналу.

### Current Yoko signatures / Return

- `UO.LineCount()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["LineCount"]` → `BRIDGE CONTRACT -> IApiBridge.JournalMatchCount`

**Pascal compatibility signature:** `function LineCount: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.LineCount()
```

---
