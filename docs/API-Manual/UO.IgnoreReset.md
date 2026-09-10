# UO.IgnoreReset

ClassicUO • Runtime API • `UO.IgnoreReset.md`

## Точный синтаксис / Registered signatures

```text
UO.IgnoreReset() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.IgnoreReset`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Очищает весь список игнорирования, делая все ранее игнорируемые объекты снова видимыми для операций поиска.

### Current Basic signatures / Return

- `UO.IgnoreReset() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.IgnoreReset"]`

**Pascal compatibility signature:** `procedure IgnoreReset;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.IgnoreReset()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.IgnoreReset()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.IgnoreReset()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.IgnoreReset()
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.IgnoreReset`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
