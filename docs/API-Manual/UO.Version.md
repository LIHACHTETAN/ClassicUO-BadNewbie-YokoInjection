# UO.Version

ClassicUO • Runtime API • `UO.Version.md`

## Точный синтаксис / Registered signatures

```text
UO.Version() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Version`

### Current Basic signatures / Return

- `UO.Version() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Prints the real Basic product version from the active ClassicUO / BadNewbie / Basic IDE client. The value is sourced from the live product-version bridge and is not a hard-coded compatibility placeholder.
### Notes / limitations

This command prints version information and intentionally returns no value. Use `StealthInfo()` when a script needs version data as values.

### Examples

```basic
SUB Main()
    UO.Version()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.Version()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.Version()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.Version()
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass66_0.<RegisterLegacyManualAliases>b__1`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
