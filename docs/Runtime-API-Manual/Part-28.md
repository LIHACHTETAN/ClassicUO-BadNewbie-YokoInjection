# Runtime API Manual — Part 28

Commands: **SetMulPath** through **SkillVal**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `524c4a06be8a621b5b5e24dabc4795c2c7da682f9c23e0b516f2de0a437ee254`

---

## `UO.SetMulPath`

### Direct runtime overloads

- `UO.SetMulPath(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetMulPath(0)
```

---

## `UO.SetPauseScriptOnDisconnectStatus`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Включает или отключает автоматическую приостановку скрипта при отключении персонажа от сервера. Value — True для приостановки скрипта при отключении, False для продолжения выполнения. При включении выполнение скрипта приостанавливается при отключении и возобновляется при восстановлении соединения (например, через автопереподключение). Это предотвращает выполнение игровых команд во время отключения, которые иначе были бы молча отброшены. Используйте GetPauseScriptOnDisconnectStatus для чтения текущего состояния. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.SetPauseScriptOnDisconnectStatus(Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetPauseScriptOnDisconnectStatus"]` → `BRIDGE CONTRACT -> IApiBridge.SetPauseScriptOnDisconnectStatus`

**Pascal compatibility signature:** `procedure SetPauseScriptOnDisconnectStatus(Value: Boolean);`

### Parameters

- `Value` — String/text value interpreted according to the command.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetPauseScriptOnDisconnectStatus('value')
```

---

## `UO.SetRec`

### Manifest-registered overloads

- `UO.SetRec() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Compatibility metadata exposes an adapted return slot; the command itself is zero-argument and returns no script value.

### Legacy Yoko overloads

- `UO.SetRec()`
  - **Return type:** `Unit`
  - **Return contract:** No value. Arms a one-shot recorder for the next legacy `UO.*` compatibility command.

### Parameters

- None. The command is strictly zero-argument.

### Behavior

The recovered Injection help identifies `UO.SetRec()` as a Script.dll-only command introduced by `<=1501.17`, but the historical help page was unfinished and the public Injection source archives do not contain its Script.dll implementation. ClassicUO Yoko v50 therefore provides an explicit deterministic replacement instead of a no-op: `UO.SetRec()` clears the previous recorded action and arms recording. The next command routed through the legacy `UO.*` compatibility dispatcher executes normally and is saved together with its typed arguments. `UO.UseRec()` can then replay the saved command.

### Notes / limitations

- Recording is one-shot: after one compatible command is captured, the recorder automatically disarms.
- `UO.SetRec()` and `UO.UseRec()` themselves are never captured.
- The stored command is kept in Yoko runtime state and survives the normal runtime-state snapshot/restore path.
- `remain()` returns `0` immediately after `UO.SetRec()` and `1` after a command has been captured.
- This v50 behavior is a documented ClassicUO/Yoko compatibility definition because no authoritative public Script.dll implementation of the historical semantics is available.

### Examples

```basic
UO.SetRec()
UO.SetDefault('healbag', 0x40001234)  # executes and is recorded
IF remain() = 1 THEN
    UO.UseRec()                       # repeats SetDefault with the same arguments
END IF
```

---

## `UO.SetReceivingContainer`

### Direct runtime overloads

- `UO.SetReceivingContainer(arg1:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetReceivingContainer(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetReceivingContainer(0)
```

```basic
UO.SetReceivingContainer(0)
```

---

## `UO.SetRunMountTimer`

### Current Yoko signatures / Return

- `UO.SetRunMountTimer(Value) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The active Yoko movement timing is updated immediately.

### Parameters

- `Value` — movement step timing in milliseconds, clamped to `10..2000`.

### Behavior

Sets the ClassicUO player movement completion delay used when **running while mounted**. The value is propagated from Yoko runtime state into `MovementSpeed.TimeToCompleteMovement`; it is no longer a state-only compatibility variable.

Default compatibility value: `100` ms.

### Notes / limitations

- Extremely small values can still be limited in practice by server movement acknowledgements/denials and network latency.
- This changes the local Yoko/ClassicUO movement timing policy; it cannot force a shard to accept movement faster than the server protocol permits.

### Examples

```basic
UO.SetRunMountTimer(100)
```
---

## `UO.SetRunUnmountTimer`

### Current Yoko signatures / Return

- `UO.SetRunUnmountTimer(Value) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The active Yoko movement timing is updated immediately.

### Parameters

- `Value` — movement step timing in milliseconds, clamped to `10..2000`.

### Behavior

Sets the ClassicUO player movement completion delay used when **running on foot**. The value is propagated from Yoko runtime state into `MovementSpeed.TimeToCompleteMovement`; it is no longer a state-only compatibility variable.

Default compatibility value: `200` ms.

### Notes / limitations

- Extremely small values can still be limited in practice by server movement acknowledgements/denials and network latency.
- This changes the local Yoko/ClassicUO movement timing policy; it cannot force a shard to accept movement faster than the server protocol permits.

### Examples

```basic
UO.SetRunUnmountTimer(200)
```
---

## `UO.SetScriptName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает отображаемое имя для работающего скрипта по его индексу. ScriptIndex — индекс скрипта (с нуля) в пуле скриптов. Value — новое отображаемое имя скрипта. Изменяет имя, показываемое в списке скриптов интерфейса. Не влияет на имя файла скрипта или его выполнение. Полезно для идентификации скриптов при одновременном запуске нескольких экземпляров. Используйте GetScriptName для чтения текущего имени скрипта, и GetScriptsCount (Python: GetScriptCount ) для получения общего числа работающих скриптов.

### Current Yoko signatures / Return

- `UO.SetScriptName(ScriptIndex, Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetScriptName"]` → `BRIDGE CONTRACT -> IApiBridge.SetScriptName`

**Pascal compatibility signature:** `procedure SetScriptName(ScriptIndex: Word; Value: String);`

### Parameters

- `ScriptIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Value` — String/text value interpreted according to the command.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetScriptName(0, 'value')
```

---

## `UO.SetSeason`

### Manifest-registered overloads

- `UO.SetSeason(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.SetSeason(season)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `season` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.SetSeason(0)
```

```basic
UO.SetSeason(0)
```

---

## `UO.SetShowZ`

### Direct runtime overloads

- `UO.SetShowZ(arg1:Any) -> Unit`
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
UO.SetShowZ(0)
```

---

## `UO.SetSilentMode`

### Current Yoko signatures / Return

- `UO.SetSilentMode(Value) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value.

### Parameters

- `Value` — Boolean-compatible value. `True` suppresses automatic Info Window dumps; `False` enables them.

### Behavior

Controls automatic diagnostic output to the Info Window. When silent mode is disabled (`False`), Gump description/query helpers may both return their data and mirror the lines into the Info Window. When silent mode is enabled (`True`), those helpers return data without automatic Info Window output.

### Notes / limitations

`FillInfoWindow`/explicit Info Window writes are not suppressed by this setting.

### Examples

```basic
UO.SetSilentMode(False)
VAR lines = UO.GetGumpButtonsDescription(0)

UO.SetSilentMode(True)
```

---

## `UO.SetSkillLockState`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос на изменение состояния блокировки навыка. SkillName — имя навыка строкой (например, 'Anatomy' , 'Mining' ). Регистронезависимое. Если имя навыка не распознано, ошибка логируется в системный журнал и вызов игнорируется. skillState — новое состояние блокировки: Значение Смысл 0 Up (рост навыка разрешён) 1 Down (потеря навыка разрешена) 2 Locked (без изменений) В Python метод называется SetSkillLockState и использует индекс навыка ( int ) вместо имени, также есть синоним ChangeSkillLockState . SkillLockState — алиас для этого метода в Pascal.

### Current Yoko signatures / Return

- `UO.SetSkillLockState(SkillName, skillState)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetSkillLockState"]` → `BRIDGE CONTRACT -> IApiBridge.SetSkillLockState`

**Pascal compatibility signature:** `procedure SetSkillLockState(SkillName: String; skillState: Byte);`

### Parameters

- `SkillName` — String/text value interpreted according to the command.
- `skillState` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetSkillLockState('value', 0)
```

---

## `UO.SetStatLockState`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос на изменение состояния блокировки характеристики персонажа. statNum — индекс характеристики: Значение Характеристика 0 Strength (Сила) 1 Dexterity (Ловкость) 2 Intelligence (Интеллект) statState — новое состояние блокировки: Значение Смысл 0 Up (рост разрешён) 1 Down (потеря разрешена) 2 Locked (без изменений) Значения statNum > 2 или statState > 2 игнорируются. Запрос также игнорируется, если сервер не поддерживает блокировку статов. В Python метод называется SetStatState . SetStatState — алиас для этого метода в Pascal.

### Current Yoko signatures / Return

- `UO.SetStatLockState(statNum, statState)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetStatLockState"]` → `BRIDGE CONTRACT -> IApiBridge.SetStatLockState`

**Pascal compatibility signature:** `procedure SetStatLockState(statNum: Byte; statState: Byte);`

### Parameters

- `statNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `statState` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetStatLockState(0, 0)
```

---

## `UO.SetStatState`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Алиас для SetStatLockState . Отправляет серверу запрос на изменение состояния блокировки характеристики персонажа. statNum — индекс характеристики: 0 = Strength, 1 = Dexterity, 2 = Intelligence. statState — состояние блокировки: 0 = Up, 1 = Down, 2 = Locked. Полное описание — в SetStatLockState . В Python это основное имя метода: SetStatState .

### Current Yoko signatures / Return

- `UO.SetStatState(statNum, statState)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetStatState"]` → `BRIDGE CONTRACT -> IApiBridge.SetStatLockState`

**Pascal compatibility signature:** `procedure SetStatState(statNum: Byte; statState: Byte);`

### Parameters

- `statNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `statState` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetStatState(0, 0)
```

---

## `UO.SetWalkMountTimer`

### Current Yoko signatures / Return

- `UO.SetWalkMountTimer(Value) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The active Yoko movement timing is updated immediately.

### Parameters

- `Value` — movement step timing in milliseconds, clamped to `10..2000`.

### Behavior

Sets the ClassicUO player movement completion delay used when **walking while mounted**. The value is propagated from Yoko runtime state into `MovementSpeed.TimeToCompleteMovement`; it is no longer a state-only compatibility variable.

Default compatibility value: `200` ms.

### Notes / limitations

- Extremely small values can still be limited in practice by server movement acknowledgements/denials and network latency.
- This changes the local Yoko/ClassicUO movement timing policy; it cannot force a shard to accept movement faster than the server protocol permits.

### Examples

```basic
UO.SetWalkMountTimer(200)
```
---

## `UO.SetWalkUnmountTimer`

### Current Yoko signatures / Return

- `UO.SetWalkUnmountTimer(Value) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The active Yoko movement timing is updated immediately.

### Parameters

- `Value` — movement step timing in milliseconds, clamped to `10..2000`.

### Behavior

Sets the ClassicUO player movement completion delay used when **walking on foot**. The value is propagated from Yoko runtime state into `MovementSpeed.TimeToCompleteMovement`; it is no longer a state-only compatibility variable.

Default compatibility value: `400` ms.

### Notes / limitations

- Extremely small values can still be limited in practice by server movement acknowledgements/denials and network latency.
- This changes the local Yoko/ClassicUO movement timing policy; it cannot force a shard to accept movement faster than the server protocol permits.

### Examples

```basic
UO.SetWalkUnmountTimer(400)
```
---

## `UO.SetWarMode`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Включает или отключает режим войны (боевую стойку) персонажа. Value — True для входа в режим войны, False для выхода. Отправляет серверу пакет переключения режима войны. В режиме войны персонаж принимает боевую стойку, и щелчки по мобайлам инициируют атаки. Обратите внимание, что Attack автоматически включает режим войны, поэтому вызывать SetWarMode(True) перед атакой обычно не нужно. Однако SetWarMode(False) полезен для явного выхода из боевой стойки. Используйте IsWarMode для проверки текущего состояния.

### Current Yoko signatures / Return

- `UO.SetWarMode(Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetWarMode"]`

**Pascal compatibility signature:** `procedure SetWarMode(Value: Boolean);`

### Parameters

- `Value` — String/text value interpreted according to the command.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetWarMode('value')
```

---

## `UO.Sex`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение пола текущего персонажа. Возвращает значение типа Byte , соответствующее типу тела: Значение Смысл 0 Мужской (Человек) 1 Женский (Человек) 2 Мужской (Эльф) 3 Женский (Эльф) 4 Мужской (Гаргулья) 5 Женский (Гаргулья) Точные числовые значения зависят от реализации сервера. Таблица выше показывает стандартные значения Ultima Online. Используйте IsFemale для простой булевой проверки, или Race для определения расы персонажа.

### Current Yoko signatures / Return

- `UO.Sex()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Sex"]` → `BRIDGE CONTRACT -> IApiBridge.Sex`

**Pascal compatibility signature:** `function Sex: Byte;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Sex()
```

---

## `UO.ShardName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает имя шарда, к которому персонаж сейчас подключён (или был подключён последним). Имя шарда соответствует имени, заданному в настройках профиля Stealth.

### Current Yoko signatures / Return

- `UO.ShardName()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ShardName"]` → `BRIDGE CONTRACT -> IApiBridge.ShardName`

**Pascal compatibility signature:** `function ShardName: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ShardName()
```

---

## `UO.ShardPath`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает путь в файловой системе к каталогу данных приложения для шарда. Это специфичный для Stealth каталог, в котором хранятся файлы данных шарда (кэшированные данные карт, пользовательские статики и т.д.). В Python метод называется GetShardPath .

### Current Yoko signatures / Return

- `UO.ShardPath()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ShardPath"]` → `BRIDGE CONTRACT -> IApiBridge.CurrentProfilePath`

**Pascal compatibility signature:** `function ShardPath: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ShardPath()
```

---

## `UO.Shop`

### Manifest-registered overloads

- `UO.Shop() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Shop()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Shop()
```

```basic
UO.Shop()
```

---

## `UO.ShowJournal`

### Manifest-registered overloads

- `UO.ShowJournal() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.ShowJournal()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ShowJournal()
```

```basic
UO.ShowJournal()
```

---

## `UO.ShutdownWindows`

### Manifest-registered overloads

- `UO.ShutdownWindows(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.ShutdownWindows(state)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `state` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ShutdownWindows(0)
```

```basic
UO.ShutdownWindows(0)
```

---

## `UO.SkillLockState`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Алиас для SetSkillLockState . Отправляет серверу запрос на изменение состояния блокировки навыка. SkillName — имя навыка строкой. Регистронезависимое. skillState — состояние блокировки: 0 = Up, 1 = Down, 2 = Locked. Полное описание — в SetSkillLockState . В Python метод называется SetSkillLockState и использует индекс навыка ( int ) вместо имени.

### Current Yoko signatures / Return

- `UO.SkillLockState(SkillName, skillState)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SkillLockState"]` → `BRIDGE CONTRACT -> IApiBridge.SetSkillLockState`

**Pascal compatibility signature:** `procedure SkillLockState(SkillName: String; skillState: Byte);`

### Parameters

- `SkillName` — String/text value interpreted according to the command.
- `skillState` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SkillLockState('value', 0)
```

---

## `UO.SkillVal`

### Direct runtime overloads

- `UO.SkillVal(arg1:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.SkillVal(0)
```

---
