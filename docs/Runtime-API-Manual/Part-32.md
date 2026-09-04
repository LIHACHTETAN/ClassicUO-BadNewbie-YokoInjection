# Runtime API Manual — Part 32

Commands: **UseSkill** through **WaitingMenu**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `524c4a06be8a621b5b5e24dabc4795c2c7da682f9c23e0b516f2de0a437ee254`

---

## `UO.UseSkill`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Активирует указанный навык. SkillName (Pascal) — имя навыка строкой (например, 'Anatomy' , 'Stealth' , 'Tracking' ). Регистронезависимое. Если имя не распознано, логируется ошибка и возвращается False . SkillID (Python) — целочисленный индекс навыка. Для получения индекса по названию навыка используйте GetSkillID . В Pascal возвращает True при успешной активации, False при неизвестном имени навыка. В Python возвращает None . Обратите внимание на различие параметров: Pascal использует имя навыка (String), Python — индекс навыка (int).

### Current Yoko signatures / Return

- `UO.UseSkill(SkillName)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseSkill"]` → `BRIDGE CONTRACT -> IApiBridge.UseSkill`

**Pascal compatibility signature:** `function UseSkill(SkillName: String): Boolean;`

### Additional current runtime overloads

- `UO.UseSkill(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `SkillName` — String/text value interpreted according to the command.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.UseSkill('value')
```

```basic
VAR result = UO.UseSkill(0, 0)
```

---

## `UO.UseType`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет объект указанного типа и цвета на персонаже (сначала слои экипировки, затем рюкзак), затем использует (double-click) его. ObjType — graphic (тип) объекта. $FFFF — любой тип. Color — цвет объекта. $FFFF — любой цвет. Возвращает serial (ID) найденного и использованного объекта, или 0 если подходящий объект не найден. Порядок поиска: Слои экипировки персонажа (кроме самого рюкзака). Рюкзак (рекурсивно). Если объект найден в слоях и его ID совпадает с ID рюкзака, он пропускается, чтобы избежать случайного открытия рюкзака. Логирует ошибку, если подходящий объект не найден.

### Current Yoko signatures / Return

- `UO.UseType(ObjType, Color)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseType"]` → `BRIDGE CONTRACT -> IApiBridge.UseType`

**Pascal compatibility signature:** `function UseType(ObjType: Word; Color: Word): Cardinal;`

### Additional current runtime overloads

- `UO.UseType(arg1:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.UseType(arg1:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.UseType(0x0190, -1)
```

```basic
VAR result = UO.UseType(0)
```

```basic
VAR result = UO.UseType(0)
```

---

## `UO.UseVirtue`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Активирует указанную добродетель. VirtueName (Pascal) — имя добродетели строкой (например, 'Honor' , 'Valor' , 'Compassion' ). Если имя не распознано, логируется ошибка. VirtueID (Python) — индекс добродетели целым числом. Также принимает значения перечисления Virtue . Обратите внимание на различие: Pascal использует имя (String), Python — индекс (int) или перечисление Virtue . На официальных шардах вызывает гамп системы добродетелей.

### Current Yoko signatures / Return

- `UO.UseVirtue(VirtueName)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseVirtue"]` → `BRIDGE CONTRACT -> IApiBridge.UseVirtue`

**Pascal compatibility signature:** `procedure UseVirtue(VirtueName: String);`

### Parameters

- `VirtueName` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UseVirtue('value')
```

---

## `UO.UseWorldObject`

### Direct runtime overloads

- `UO.UseWorldObject(arg1:Any) -> Unit`
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
UO.UseWorldObject(0)
```

---

## `UO.VendorMenu`

### Manifest-registered overloads

- `UO.VendorMenu(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.VendorMenu(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.VendorMenu(vendor)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.VendorMenu(menu, choice)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `vendor` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `menu` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `choice` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.VendorMenu(0)
```

```basic
UO.VendorMenu(0, 0)
```

---

## `UO.Version`

### Current Yoko signatures / Return

- `UO.Version() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Prints the current embedded product name and real Yoko product version to the client information output.

### Parameters

- None.

### Behavior

Prints a value equivalent to `ClassicUO / BadNewbie / Yoko Injection v<current version>`. The version comes from the active client product version and is no longer a generic compatibility-runtime string.

### Notes / limitations

This command prints version information and intentionally returns no value. Use `StealthInfo()` when a script needs version data as values.

### Examples

```basic
UO.Version()
```

---

## `UO.Wait`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Приостанавливает выполнение скрипта на указанное время. WaitTimeMS — задержка в миллисекундах. Значение 0 возвращает управление немедленно. Внутренне использует интервалы опроса 20 мс и обрабатывает события скрипта (обратные вызовы обработчиков событий) во время ожидания. Скрипт остаётся реактивным к событиям во время паузы. Также учитывается состояние приостановки скрипта — если скрипт приостановлен (например, при отключении с SetPauseScriptOnDisconnectStatus ), ожидание начала задержки происходит после снятия паузы. Sleep — алиас для этого метода.

### Current Yoko signatures / Return

- `UO.Wait(WaitTimeMS)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Wait"]` → `BRIDGE CONTRACT -> IApiBridge.Wait`

**Pascal compatibility signature:** `procedure Wait(WaitTimeMS: Cardinal);`

### Parameters

- `WaitTimeMS` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Wait(1000)
```

---

## `UO.WaitForClientTargetResponse`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ожидает ответа клиента на ранее выданный запрос клиентского таргета. MaxWaitTimeMS — максимальное время ожидания в миллисекундах. -1 — ждать бесконечно. Возвращает True , если клиент ответил на запрос таргета в пределах таймаута, False — если таймаут истёк или скрипт был остановлен. Опрос каждые 100 мс, поэтому фактическое ожидание может превысить таймаут до 100 мс. Используется вместе с ClientRequestObjectTarget или ClientRequestTileTarget для ожидания ручного выбора цели пользователем, затем результат получается через ClientTargetResponse .

### Current Yoko signatures / Return

- `UO.WaitForClientTargetResponse(MaxWaitTimeMS)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitForClientTargetResponse"]` → `BRIDGE CONTRACT -> IApiBridge.WaitForClientTargetResponse`

**Pascal compatibility signature:** `function WaitForClientTargetResponse(MaxWaitTimeMS: Integer): Boolean;`

### Parameters

- `MaxWaitTimeMS` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WaitForClientTargetResponse(1000)
```

---

## `UO.WaitForTarget`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ожидает появления серверного курсора цели. MaxWaitTimeMS — максимальное время ожидания в миллисекундах. Возвращает True , если курсор цели появился до таймаута, False — если таймаут истёк. Опрос каждые 100 мс, поэтому фактическое ожидание может превысить таймаут до 100 мс. После возврата True используйте TargetToObject , TargetToTile или TargetToXYZ для ответа на курсор. Или CancelTarget для его отмены. Для предварительной установки цели до появления курсора используйте WaitTargetObject , WaitTargetTile и т.д.

### Current Yoko signatures / Return

- `UO.WaitForTarget(MaxWaitTimeMS)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitForTarget"]` → `BRIDGE CONTRACT -> IApiBridge.WaitUntilTargeting`

**Pascal compatibility signature:** `function WaitForTarget(MaxWaitTimeMS: Integer): Boolean;`

### Parameters

- `MaxWaitTimeMS` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WaitForTarget(1000)
```

---

## `UO.WaitGump`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет кнопку гампа с указанным значением возврата и нажимает её; если не найдена — устанавливает ловушку на входящие гампы. Value — значение возврата кнопки (строка в Pascal, целое число в Python). В Pascal строка преобразуется в целое число. Метод сначала перебирает все гампы, хранящиеся в кеше Stealth, в поисках первой кнопки с совпадающим ReturnValue . Если найдена — нажимается немедленно. Если среди существующих гампов совпадение не найдено, устанавливается ловушка на входящие гампы — при получении нового гампа от сервера с подходящей кнопкой она будет нажата автоматически. Устарел. Этот метод неточен, поскольку ищет по всем гампам без разбора. Рекомендуется использовать методы семейства NumGumpButton , которые нацеливаются на конкретный гамп по индексу и обеспечивают гораздо более точный контроль.

### Current Yoko signatures / Return

- `UO.WaitGump(Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitGump"]` → `BRIDGE CONTRACT -> IApiBridge.WaitGump`

**Pascal compatibility signature:** `procedure WaitGump(Value: String);`

### Parameters

- `Value` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitGump('value')
```

---

## `UO.WaitGumpCheck`

### Manifest-registered overloads

- `UO.WaitGumpCheck(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.WaitGumpCheck(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.WaitGumpCheck(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any, arg6:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.WaitGumpCheck(index, state)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitGumpCheck(index, state, index2, state2)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitGumpCheck(index, state, index2, state2, index3, state3)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg6` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `index` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `state` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `index2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `state2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `index3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `state3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WaitGumpCheck(0, 0)
```

```basic
UO.WaitGumpCheck(0, 0, 0, 0, 0, 0)
```

---

## `UO.WaitGumpEntry`

### Manifest-registered overloads

- `UO.WaitGumpEntry(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.WaitGumpEntry(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.WaitGumpEntry(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any, arg6:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.WaitGumpEntry(index, text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitGumpEntry(index, text, index2, text2)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitGumpEntry(index, text, index2, text2, index3, text3)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg6` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `index` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `text` — String/text value interpreted according to the command.
- `index2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `text2` — String/text value interpreted according to the command.
- `index3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `text3` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WaitGumpEntry(0, 0)
```

```basic
UO.WaitGumpEntry(0, 'value', 0, 'value', 0, 'value')
```

---

## `UO.Waiting`

### Direct runtime overloads

- `UO.Waiting() -> Integer`
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
VAR result = UO.Waiting()
```

---

## `UO.WaitingForJournalText`

### Direct runtime overloads

- `UO.WaitingForJournalText(arg1:Any, arg2:Any, arg3:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitingForJournalText(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitingForJournalText(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitingForJournalText(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any, arg6:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg6` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitingForJournalText(0, 0, 0)
```

```basic
UO.WaitingForJournalText(0, 0, 0, 0, 0, 0)
```

---

## `UO.WaitingForMenu`

### Direct runtime overloads

- `UO.WaitingForMenu(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitingForMenu(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitingForMenu(arg1:Any, arg2:Any, arg3:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitingForMenu(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitingForMenu(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitingForMenu(0)
```

```basic
UO.WaitingForMenu(0, 0, 0, 0, 0)
```

---

## `UO.WaitingMenu`

### Direct runtime overloads

- `UO.WaitingMenu() -> Integer`
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
VAR result = UO.WaitingMenu()
```

---
