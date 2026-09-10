# UO.UnsetCatchBag

ClassicUO • Runtime API • `UO.UnsetCatchBag.md`

## Точный синтаксис / Registered signatures

```text
UO.UnsetCatchBag() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UnsetCatchBag`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Сбрасывает текущий «catch bag». После вызова предметы, получаемые персонажем, больше не будут автоматически перемещаться в назначенный контейнер. Эквивалентно вызову SetCatchBag(0) .

### Current Basic signatures / Return

- `UO.UnsetCatchBag() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UnsetCatchBag"]`

**Pascal compatibility signature:** `procedure UnsetCatchBag;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.UnsetCatchBag()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.UnsetCatchBag()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.UnsetCatchBag()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.UnsetCatchBag()
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
