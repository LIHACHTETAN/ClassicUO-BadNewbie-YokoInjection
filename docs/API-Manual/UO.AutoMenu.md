# UO.AutoMenu

ClassicUO • Runtime API • `UO.AutoMenu.md`

## Точный синтаксис / Registered signatures

```text
UO.AutoMenu(prompt:Any, choice:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.AutoMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Устанавливает многоразовую ловушку на меню. Работает так же, как WaitMenu , но хук постоянный — он срабатывает каждый раз при появлении подходящего меню, пока не будет явно удалён через CancelMenu . Когда заголовок входящего меню содержит MenuCaption , а в меню есть элемент, содержащий ElementCaption , этот элемент выбирается автоматически. Для одноразовой ловушки используйте WaitMenu . Для удаления всех хуков используйте CancelMenu .

### Current Basic signatures / Return

- `UO.AutoMenu(MenuCaption:String, ElementCaption:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `LEGACY DISPATCH -> InjectionApiUO.ExecuteLegacyCommand["AutoMenu"]`

**Pascal compatibility signature:** `procedure AutoMenu(MenuCaption: String; ElementCaption: String);`

### Parameters

- `MenuCaption` — Named runtime value (runtime value); use the exact registered/saved name expected by AutoMenu.
- `ElementCaption` — Named runtime value (runtime value); use the exact registered/saved name expected by AutoMenu.

### Accepted values / constants

- `MenuCaption` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `ElementCaption` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.AutoMenu(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.AutoMenu(1, 2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 1 # prompt
        VAR arg2 = 2 # choice
        UO.AutoMenu(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 1 # prompt
    VAR arg2 = 2 # choice
    UO.AutoMenu(arg1, arg2)
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
