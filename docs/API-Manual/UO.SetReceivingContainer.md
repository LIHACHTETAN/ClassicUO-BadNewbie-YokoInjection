# UO.SetReceivingContainer

ClassicUO • Runtime API • `UO.SetReceivingContainer.md`

## Точный синтаксис / Registered signatures

```text
UO.SetReceivingContainer() -> Unit
UO.SetReceivingContainer(id:Integer) -> Unit
UO.SetReceivingContainer(id:String) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetReceivingContainer`

### Direct runtime overloads

- `UO.SetReceivingContainer(id:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetReceivingContainer(id:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `id` — Object/mobile serial or a supported Basic object reference such as self/backpack/lasttarget/saved object name; hexadecimal and decimal serials are accepted by Variant overloads.

### Accepted values / constants

- `id` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetReceivingContainer(0)
END SUB
```

```basic
SUB Main()
    UO.SetReceivingContainer(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetReceivingContainer()
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = self # id
    UO.SetReceivingContainer(arg1)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.SetReceivingContainer()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.SetReceivingContainer()
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.SetReceivingContainer`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
