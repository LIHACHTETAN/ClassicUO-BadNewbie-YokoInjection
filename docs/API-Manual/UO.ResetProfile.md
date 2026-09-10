# UO.ResetProfile

ClassicUO • Runtime API • `UO.ResetProfile.md`

## Точный синтаксис / Registered signatures

```text
UO.ResetProfile() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ResetProfile`

### Current Basic signatures / Return

- `UO.ResetProfile() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Resets the **currently loaded ClassicUO/Basic character profile** to `default.json` (or built-in defaults when no default file exists). The profile identity is preserved: account/user name, connected server name and character name are copied back into the reset profile. The result is saved to the current server-specific `profile.json`.

The profile directory is not `v2`: it remains under `Data/Profiles/<connected server name>/<character serial>/` (or the configured ProfilesPath equivalent).

### Notes / limitations

- This resets settings for the currently loaded character profile; it does not delete the profile directory.
- Server/account/character identity is preserved intentionally.
- If no character profile is active, the command reports an error and performs no reset.
- Runtime/UI objects that read profile settings use the new profile after the reset; settings that require recreating a window may become visually apparent after reopening that window.

### Examples

```basic
SUB Main()
    UO.ResetProfile()
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.ResetProfile()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.ResetProfile()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.ResetProfile()
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
