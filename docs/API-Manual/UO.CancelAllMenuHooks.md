# UO.CancelAllMenuHooks

ClassicUO • Runtime API • `UO.CancelAllMenuHooks.md`

## Точный синтаксис / Registered signatures

```text
UO.CancelAllMenuHooks() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.CancelAllMenuHooks`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Удаляет все ловушки на меню, установленные через AutoMenu и WaitMenu . Вызывайте перед установкой новых хуков, чтобы убедиться, что не осталось устаревших ловушек. Алиас: CancelMenu (устаревший синоним). В Python метод называется CancelMenu .

### Current Basic signatures / Return

- `UO.CancelAllMenuHooks() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CancelAllMenuHooks"]` → `BRIDGE CONTRACT -> IApiBridge.ClearMenuHooks`

**Pascal compatibility signature:** `procedure CancelAllMenuHooks;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.CancelAllMenuHooks()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.CancelAllMenuHooks()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.CancelAllMenuHooks()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.CancelAllMenuHooks()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
