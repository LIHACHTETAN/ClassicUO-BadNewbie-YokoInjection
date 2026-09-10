# UO.PartyDeclineInvite

ClassicUO • Runtime API • `UO.PartyDeclineInvite.md`

## Точный синтаксис / Registered signatures

```text
UO.PartyDeclineInvite() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.PartyDeclineInvite`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отклоняет ожидающее приглашение в пати. Приглашение должно быть получено до вызова этого метода.

### Current Basic signatures / Return

- `UO.PartyDeclineInvite() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartyDeclineInvite"]` → `BRIDGE CONTRACT -> IApiBridge.PartyDeclineInvite`

**Pascal compatibility signature:** `procedure PartyDeclineInvite;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.PartyDeclineInvite()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.PartyDeclineInvite()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.PartyDeclineInvite()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.PartyDeclineInvite()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
