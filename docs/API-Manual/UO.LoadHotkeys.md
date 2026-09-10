# UO.LoadHotkeys

ClassicUO • Runtime API • `UO.LoadHotkeys.md`

## Точный синтаксис / Registered signatures

```text
UO.LoadHotkeys() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.LoadHotkeys`

### Current Basic signatures / Return

- `UO.LoadHotkeys() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None in the current embedded Basic overload.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reloads the macro/hotkey definitions for the **current profile** from `macros.xml`. Because profile storage is server-scoped, the file is read from the active server-name profile folder for the current character.

### Notes / limitations

This command no longer calls `SaveConfig()` and does not overwrite the current profile as a substitute for loading hotkeys. If `macros.xml` is missing, ClassicUO's MacroManager creates its default macro file according to its normal load behavior.

### Examples

```basic
SUB Main()
    UO.LoadHotkeys()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.LoadHotkeys()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.LoadHotkeys()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.LoadHotkeys()
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
