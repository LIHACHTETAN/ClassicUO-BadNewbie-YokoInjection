# Runtime API Manual — Part 29

Commands: **Snap** through **TargetByResource**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.Snap`

### Direct runtime overloads

- `UO.Snap(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Snap() -> Unit`
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
UO.Snap(0)
```

```basic
UO.Snap()
```

---

## `UO.Snoop`

### Manifest-registered overloads

- `UO.Snoop() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Snoop(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Snoop()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Snoop(container)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Snoop()
```

```basic
UO.Snoop(backpack)
```

---

## `UO.Sound`

### Manifest-registered overloads

- `UO.Sound(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Sound(soundId)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `soundId` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Sound(0)
```

```basic
UO.Sound(self)
```

---

## `UO.Specmove`

### Manifest-registered overloads

- `UO.Specmove(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Specmove(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Specmove(direction)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Specmove(direction, running)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `direction` — Ultima Online movement/facing direction value.
- `running` — Boolean movement flag. TRUE requests running steps where the client/server allow it.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Specmove(0)
```

```basic
UO.Specmove(0, TRUE)
```

---

## `UO.Stam`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущую выносливость (stamina) персонажа. Это сокращённое свойство, эквивалентное GetStam . Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Stam()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Stam"]` → `BRIDGE CONTRACT -> IApiBridge.Stamina`

**Pascal compatibility signature:** `function Stam: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Stam()
```

---

## `UO.Stamina`

### Direct runtime overloads

- `UO.Stamina() -> Integer`
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
VAR result = UO.Stamina()
```

---

## `UO.StartScript`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Запускает скрипт из указанного файла. ScriptPath — путь к файлу скрипта ( .dsc , .sc , .py и т.д.). Может быть абсолютным или относительным к каталогу скриптов Stealth. Возвращает новое общее количество запущенных скриптов после запуска, или $FFFF (65535) при неудаче (файл не найден, объект персонажа недоступен и т.д.). Метод ожидает увеличения числа скриптов в пуле, подтверждая успешный запуск.

### Current Yoko signatures / Return

- `UO.StartScript(ScriptPath)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StartScript"]` → `BRIDGE CONTRACT -> IApiBridge.StartScript`

**Pascal compatibility signature:** `function StartScript(ScriptPath: String): Word;`

### Parameters

- `ScriptPath` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.StartScript(0)
```

---

## `UO.StealthCnt`

### Direct runtime overloads

- `UO.StealthCnt() -> Integer`
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
VAR result = UO.StealthCnt()
```

---

## `UO.StealthInfo`

### Current Yoko signatures / Return

- `UO.StealthInfo() -> Array`
  - **Return type:** `Array`
  - **Return contract:** Returns `[productName, productVersion, clientPath]` from the active ClassicUO/Yoko bridge.

### Parameters

- None.

### Behavior

Returns information about the **actual embedded ClassicUO / BadNewbie / Yoko Injection runtime**. The version is sourced from the current Yoko IDE product version instead of the old hard-coded compatibility value `1.0`.

### Notes / limitations

This is a Yoko-adapted information array, not the original Stealth record structure.

### Examples

```basic
VAR info = UO.StealthInfo()
UO.Print(info)
```

---

## `UO.StealthPath`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает путь в файловой системе к каталогу приложения Stealth. Это корневой каталог, в котором установлен/запущен Stealth.

### Current Yoko signatures / Return

- `UO.StealthPath()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StealthPath"]` → `BRIDGE CONTRACT -> IApiBridge.ClientPath`

**Pascal compatibility signature:** `function StealthPath: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.StealthPath()
```

---

## `UO.StealthProfilePath`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает путь в файловой системе к каталогу текущего профиля Stealth. В Python метод называется GetStealthProfilePath .

### Current Yoko signatures / Return

- `UO.StealthProfilePath()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StealthProfilePath"]` → `BRIDGE CONTRACT -> IApiBridge.CurrentProfilePath`

**Pascal compatibility signature:** `function StealthProfilePath: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.StealthProfilePath()
```

---

## `UO.Step`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Выполняет один шаг в указанном направлении с подтверждением от сервера. Direction — направление шага (0–7). См. ConstantsAndEnums для значений направлений. Running — True для бега, False для ходьбы. Возвращает код результата: Код Значение 0 Неизвестная ошибка / отключён 2 Переполнение буфера шагов 3 Клиентская проверка: точка непроходима 4 Таймаут ожидания ответа сервера 5 Шаг отклонён сервером 6 Запрос на шаг отправлен, ожидается подтверждение 7 Шаг принят сервером В отличие от StepQ , этот метод ожидает подтверждение или отклонение шага сервером перед возвратом. Это медленнее, но надёжнее для точного позиционирования. Учитывает переменную moveCheckStamina — если stamina ниже порога, шаг пропускается и возвращается 0 . Также учитывает moveExitOnDisconnect — при отключении немедленно возвращает 0 .

### Current Yoko signatures / Return

- `UO.Step(Direction, Running)`
  - **Return type:** `Integer`
  - **Return contract:** Movement result code after ACK/DENY for the exact sequence.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Step"]` → `STATE -> InjectionApiState.MoveCheckStamina` → `STATE -> InjectionApiState.MoveExitOnDisconnect` → `STATE -> InjectionApiState.MoveOpenDoor` → `BRIDGE CONTRACT -> IApiBridge.IsOnline` → `BRIDGE CONTRACT -> IApiBridge.OpenDoor`

**Pascal compatibility signature:** `function Raw_Move(Direction: Byte; Running: Boolean): Boolean; // Equivalent to: Result := Step(Direction, Running) = 7;`

### Parameters

- `Direction` — Ultima Online movement/facing direction value.
- `Running` — Boolean movement flag. TRUE requests running steps where the client/server allow it.

### Behavior

Queues the movement request and waits for the ACK/DENY associated with that exact sequence, returning the runtime movement result code.

### Notes / limitations

Server ACK/DENY and client walker state determine the final result code; another worker's ACK cannot satisfy the exact-sequence wait.

### Examples

```basic
VAR result = UO.Step(0, TRUE)
```

---

## `UO.StepQ`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Выполняет один шаг в указанном направлении в режиме очереди, без ожидания подтверждения от сервера. Direction — направление шага (0–7). См. ConstantsAndEnums . Running — True для бега, False для ходьбы. Возвращает ID запроса на шаг (неотрицательное) при успехе или отрицательное значение при ошибке: Значение Смысл >= 0 Запрос на шаг поставлен в очередь (ID запроса) -1 Ошибка (отключён, скрипт остановлен, данные не загружены, мало stamina) -2 Клиентская проверка: точка непроходима 256 Персонаж повернулся в нужном направлении без шага (сценарий открытия двери) В отличие от Step , StepQ не ждёт подтверждения сервера. Позволяет ставить несколько шагов в очередь для более быстрого перемещения, но с менее точной обратной связью. Учитывает переменные перемещения: moveOpenDoor (автооткрытие дверей, до 3 попыток; помечает тайл как bad при заблокированной двери), moveExitOnDisconnect , moveCheckStamina . ID двери, открытой во время этого шага, сохраняется и доступен через LastStepQUsedDoor .

### Current Yoko signatures / Return

- `UO.StepQ(Direction, Running)`
  - **Return type:** `Integer`
  - **Return contract:** Queued movement sequence/request ID; negative values indicate client/runtime rejection.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StepQ"]` → `STATE -> InjectionApiState.MoveCheckStamina` → `STATE -> InjectionApiState.MoveExitOnDisconnect` → `STATE -> InjectionApiState.MoveOpenDoor` → `BRIDGE CONTRACT -> IApiBridge.IsOnline` → `BRIDGE CONTRACT -> IApiBridge.OpenDoor`

**Pascal compatibility signature:** `function StepQ(Direction: Byte; Running: Boolean): Integer;`

### Parameters

- `Direction` — Ultima Online movement/facing direction value.
- `Running` — Boolean movement flag. TRUE requests running steps where the client/server allow it.

### Behavior

Queues one movement request through PlayerMobile.Walker and returns the real walk sequence/request identifier without waiting for acknowledgement.

### Notes / limitations

The returned sequence is tied to the real Walker request. Do not assume success until a later ACK or Step result confirms it.

### Examples

```basic
VAR result = UO.StepQ(0, TRUE)
```

---

## `UO.StopAllScripts`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет запрос на остановку всех работающих скриптов текущего персонажа. Остановка выполняется асинхронно через очередь событий персонажа. Скриптам отправляется сигнал остановки, после чего они завершаются пулом скриптов. Обратите внимание, что вызов этого метода остановит и скрипт, который его вызвал.

### Current Yoko signatures / Return

- `UO.StopAllScripts()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StopAllScripts"]` → `BRIDGE CONTRACT -> IApiBridge.StopAllScripts`

**Pascal compatibility signature:** `procedure StopAllScripts;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.StopAllScripts()
```

---

## `UO.StopBoat`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Останавливает лодку, которой правит персонаж. Эквивалент MoveBoat(0, 0) — отправляет HS-пакет управления (0xBF, субкоманда 0x33) со скоростью 0; направление в стоп-запросе сервер игнорирует. Требования те же, что и у MoveBoat : версия клиента в профиле 7.0.9.0+ , шард с поддержкой HS-управления мышью, на OSI/ServUO персонаж должен быть в pilot-режиме (за штурвалом).

### Current Yoko signatures / Return

- `UO.StopBoat()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StopBoat"]` → `BRIDGE CONTRACT -> IApiBridge.StopBoat`

**Pascal compatibility signature:** `procedure StopBoat;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.StopBoat()
```

---

## `UO.StopScript`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет запрос на остановку конкретного скрипта по его индексу. ScriptIndex — индекс скрипта (с нуля) в пуле скриптов. Остановка выполняется асинхронно через очередь событий персонажа. Используйте GetScriptsCount (Python: GetScriptCount ) и GetScriptsList для определения индекса целевого скрипта.

### Current Yoko signatures / Return

- `UO.StopScript(ScriptIndex)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StopScript"]` → `BRIDGE CONTRACT -> IApiBridge.StopScript`

**Pascal compatibility signature:** `procedure StopScript(ScriptIndex: Word);`

### Parameters

- `ScriptIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.StopScript(0)
```

---

## `UO.Str`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущее значение характеристики Strength (Сила) персонажа. Это сокращённое свойство, эквивалентное GetStr . Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Str()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Str"]` → `BRIDGE CONTRACT -> IApiBridge.Strength`

**Pascal compatibility signature:** `function Str: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Str()
```

---

## `UO.Strength`

### Direct runtime overloads

- `UO.Strength() -> Integer`
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
VAR result = UO.Strength()
```

---

## `UO.SubExists`

### Direct runtime overloads

- `UO.SubExists(arg1:String) -> Integer`
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
VAR result = UO.SubExists(0)
```

---

## `UO.Target`

### Direct runtime overloads

- `UO.Target(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Target(arg1:Any, arg2:Any, arg3:Any, arg4:Any, arg5:Any, arg6:Any, arg7:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Legacy Yoko overloads

- `UO.Target()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Target(object)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg6` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg7` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `object` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Target(0, 0)
```

```basic
UO.Target(self)
```

---

## `UO.TargetByResource`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу пакет «target by resource», нацеливаясь на указанный объект с типом ресурса. ObjID — serial (ID) объекта-цели (например, инструмент вроде кирки). Resource — индекс типа ресурса (0–4): Значение Имя Описание 0 trt_ore Руда (mining) 1 trt_sand Песок 2 trt_wood Дерево (lumberjacking) 3 trt_graves Могилы 4 trt_redmushrooms Красные грибы В DWScript параметр Resource может быть также строкой (например, 'sand' , 'graves' ), которая внутренне преобразуется в соответствующее значение перечисления. Перед отправкой: если курсор цели уже активен — вызов отменяется с предупреждением. Если объект не существует — логируется ошибка. Если значение ресурса вне диапазона 0–4 — логируется ошибка. Перед отправкой пакета применяется задержка 30мс. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.TargetByResource(ObjID, Resource)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TargetByResource"]` → `BRIDGE CONTRACT -> IApiBridge.FindType` → `BRIDGE CONTRACT -> IApiBridge.UseObject` → `BRIDGE CONTRACT -> IApiBridge.WaitTargetObject`

**Pascal compatibility signature:** `procedure TargetByResource(ObjID: Cardinal; Resource: Word);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Resource` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.TargetByResource(self, 0)
```

---
