# Runtime API Manual — Part 24

Commands: **OpenContainer** through **PredictedX**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `524c4a06be8a621b5b5e24dabc4795c2c7da682f9c23e0b516f2de0a437ee254`

---

## `UO.OpenContainer`

### Direct runtime overloads

- `UO.OpenContainer(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.OpenContainer(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.OpenContainer(0)
```

```basic
UO.OpenContainer(0, 0)
```

---

## `UO.OpenDoor`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос на открытие двери перед персонажем. Сервер определяет, какая дверь (если есть) находится перед персонажем, исходя из его позиции и направления.

### Current Yoko signatures / Return

- `UO.OpenDoor()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["OpenDoor"]` → `BRIDGE CONTRACT -> IApiBridge.OpenDoor`

**Pascal compatibility signature:** `procedure OpenDoor;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.OpenDoor()
```

---

## `UO.OpenIDE`

### Direct runtime overloads

- `UO.OpenIDE(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.OpenIDE() -> Unit`
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
UO.OpenIDE(0)
```

```basic
UO.OpenIDE()
```

---

## `UO.Paralysed`

### Direct runtime overloads

- `UO.Paralysed() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.Paralysed(serial:Integer) -> Integer`
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
VAR result = UO.Paralysed()
```

```basic
VAR result = UO.Paralysed(self)
```

---

## `UO.Paralyzed`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если собственный персонаж в данный момент парализован (заморожен), иначе False . Для проверки состояния паралича другого мобайла используйте IsParalyzed .

### Current Yoko signatures / Return

- `UO.Paralyzed()`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Paralyzed"]` → `BRIDGE CONTRACT -> IApiBridge.GetLocked` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function Paralyzed: Boolean;`

### Additional current runtime overloads

- `UO.Paralyzed(serial:Integer) -> Integer`
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
VAR result = UO.Paralyzed()
```

```basic
VAR result = UO.Paralyzed(self)
```

---

## `UO.PartyAcceptInvite`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Принимает ожидающее приглашение в пати. Приглашение должно быть получено до вызова этого метода (ID пригласившего сохраняется внутренне).

### Current Yoko signatures / Return

- `UO.PartyAcceptInvite()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartyAcceptInvite"]` → `BRIDGE CONTRACT -> IApiBridge.PartyAcceptInvite`

**Pascal compatibility signature:** `procedure PartyAcceptInvite;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.PartyAcceptInvite()
```

---

## `UO.PartyCanLootMe`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает, разрешено ли членам пати забирать предметы с трупа персонажа. Value — True — разрешить лут, False — запретить. Отправляет соответствующий пакет серверу. Персонаж должен состоять в пати, чтобы настройка имела эффект.

### Current Yoko signatures / Return

- `UO.PartyCanLootMe(Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartyCanLootMe"]` → `BRIDGE CONTRACT -> IApiBridge.PartyCanLoot`

**Pascal compatibility signature:** `procedure PartyCanLootMe(Value: Boolean);`

### Parameters

- `Value` — String/text value interpreted according to the command.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.PartyCanLootMe('value')
```

---

## `UO.PartyDeclineInvite`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отклоняет ожидающее приглашение в пати. Приглашение должно быть получено до вызова этого метода.

### Current Yoko signatures / Return

- `UO.PartyDeclineInvite()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartyDeclineInvite"]` → `BRIDGE CONTRACT -> IApiBridge.PartyDeclineInvite`

**Pascal compatibility signature:** `procedure PartyDeclineInvite;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.PartyDeclineInvite()
```

---

## `UO.PartyLeave`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Покидает текущую пати. Внутренне отправляет серверу пакет «удалить себя».

### Current Yoko signatures / Return

- `UO.PartyLeave()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartyLeave"]` → `BRIDGE CONTRACT -> IApiBridge.PartyLeave`

**Pascal compatibility signature:** `procedure PartyLeave;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.PartyLeave()
```

---

## `UO.PartyMembersList`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает список серийных номеров (ID) членов пати. Возвращает пустой массив/список, если персонаж не состоит в пати.

### Current Yoko signatures / Return

- `UO.PartyMembersList()`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartyMembersList"]` → `BRIDGE CONTRACT -> IApiBridge.PartyMembersList`

**Pascal compatibility signature:** `function PartyMembersList: TArray ;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PartyMembersList()
```

---

## `UO.PartyPrivateMessageTo`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет личное сообщение конкретному члену пати. ObjID — серийный номер (ID) члена пати для отправки сообщения. Msg — текст сообщения.

### Current Yoko signatures / Return

- `UO.PartyPrivateMessageTo(ObjID, Msg)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartyPrivateMessageTo"]` → `BRIDGE CONTRACT -> IApiBridge.PartySay`

**Pascal compatibility signature:** `procedure PartyPrivateMessageTo(ObjID: Cardinal; Msg: String);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Msg` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.PartyPrivateMessageTo(self, 1000)
```

---

## `UO.PartySay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет сообщение всем членам пати (широковещательное сообщение пати). Msg — текст сообщения.

### Current Yoko signatures / Return

- `UO.PartySay(Msg)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartySay"]` → `BRIDGE CONTRACT -> IApiBridge.PartySay`

**Pascal compatibility signature:** `procedure PartySay(Msg: String);`

### Parameters

- `Msg` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.PartySay(1000)
```

---

## `UO.PauseResumeScript`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ставит на паузу или возобновляет скрипт с указанным индексом. Если скрипт выполняется — он будет приостановлен; если приостановлен — возобновлён. В Python метод называется PauseResumeSelScript . ScriptIndex — индекс скрипта в списке скриптов (как возвращает GetScriptsList ).

### Current Yoko signatures / Return

- `UO.PauseResumeScript(ScriptIndex)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PauseResumeScript"]` → `BRIDGE CONTRACT -> IApiBridge.PauseResumeScript`

**Pascal compatibility signature:** `procedure PauseResumeScript(ScriptIndex: Word);`

### Parameters

- `ScriptIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.PauseResumeScript(0)
```

---

## `UO.PetsCurrent`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущее количество петов/фолловеров персонажа. Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.PetsCurrent()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PetsCurrent"]` → `BRIDGE CONTRACT -> IApiBridge.Followers`

**Pascal compatibility signature:** `function PetsCurrent: Byte;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PetsCurrent()
```

---

## `UO.PetsMax`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает максимальное количество петов/фолловеров, которых может иметь персонаж. В Python метод называется MaxPets . Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.PetsMax()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PetsMax"]` → `BRIDGE CONTRACT -> IApiBridge.FollowersMax`

**Pascal compatibility signature:** `function PetsMax: Byte;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PetsMax()
```

---

## `UO.PhysicalResist`

### Direct runtime overloads

- `UO.PhysicalResist() -> Integer`
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
VAR result = UO.PhysicalResist()
```

---

## `UO.Picking`

### Direct runtime overloads

- `UO.Picking() -> Integer`
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
VAR result = UO.Picking()
```

---

## `UO.PlayWav`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Воспроизводит WAV-файл асинхронно. FileName — путь к WAV-файлу. Возвращает True , если воспроизведение началось успешно, False — если файл не существует. Метод в основном поддерживается на Windows. На macOS и Android в системный журнал записывается информационное сообщение, и вызов не имеет эффекта.

### Current Yoko signatures / Return

- `UO.PlayWav(FileName)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PlayWav"]` → `BRIDGE CONTRACT -> IApiBridge.PlayWav`

**Pascal compatibility signature:** `function PlayWav(FileName: String): Boolean;`

### Parameters

- `FileName` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PlayWav('value')
```

---

## `UO.PMove`

### Direct runtime overloads

- `UO.PMove(arg1:Integer, arg2:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.PMove(arg1:Integer, arg2:Integer, arg3:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.PMove(0, 0)
```

```basic
UO.PMove(0, 0, 0)
```

---

## `UO.Poison`

### Manifest-registered overloads

- `UO.Poison() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Poison(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Poison()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Poison(target)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `target` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Poison()
```

```basic
UO.Poison(self)
```

---

## `UO.Poisoned`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если собственный персонаж в данный момент отравлен, иначе False . Для проверки состояния отравления другого мобайла используйте IsPoisoned .

### Current Yoko signatures / Return

- `UO.Poisoned()`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.Poisoned"]`

**Pascal compatibility signature:** `function Poisoned: Boolean;`

### Additional current runtime overloads

- `UO.Poisoned(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.Poisoned(serial:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Poisoned()
```

```basic
VAR result = UO.Poisoned(0)
```

```basic
VAR result = UO.Poisoned(self)
```

---

## `UO.PoisonResist`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение сопротивления яду персонажа. Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.PoisonResist()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PoisonResist"]` → `BRIDGE CONTRACT -> IApiBridge.PoisonResistance`

**Pascal compatibility signature:** `function PoisonResist: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PoisonResist()
```

---

## `UO.PredictedDirection`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает предсказанное направление персонажа на основе текущей траектории движения. Предсказанные координаты рассчитываются движком перемещения и показывают, где персонаж окажется после обработки ожидающих шагов движения.

### Current Yoko signatures / Return

- `UO.PredictedDirection()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PredictedDirection"]` → `BRIDGE CONTRACT -> IApiBridge.GetDir` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function PredictedDirection: Byte;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PredictedDirection()
```

---

## `UO.PredictedX`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает предсказанную координату X персонажа на основе текущей траектории движения.

### Current Yoko signatures / Return

- `UO.PredictedX()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PredictedX"]` → `BRIDGE CONTRACT -> IApiBridge.GetX` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function PredictedX: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.PredictedX()
```

---
