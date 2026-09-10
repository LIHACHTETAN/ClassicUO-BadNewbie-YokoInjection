# UO.SaveHotkeys

ClassicUO • Runtime API • `UO.SaveHotkeys.md`

## Точный синтаксис / Registered signatures

```text
UO.SaveHotkeys() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SaveHotkeys`

### Current Basic signatures / Return

- `UO.SaveHotkeys() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None in the current embedded Basic overload.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Writes the current macro list to the active profile's `macros.xml`. The file is stored under the current server-name/character profile directory.

### Notes / limitations

This is the embedded ClassicUO macro profile, not a separate legacy Injection hotkey-file format.

### Examples

```basic
SUB Main()
    UO.SaveHotkeys()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SaveHotkeys()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.SaveHotkeys()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.SaveHotkeys()
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
