# UO.OpenContainer

ClassicUO • Runtime API • `UO.OpenContainer.md`

## Точный синтаксис / Registered signatures

```text
UO.OpenContainer(id:Any) -> Unit
UO.OpenContainer(id:Any, timeout:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.OpenContainer`

### Direct runtime overloads

- `UO.OpenContainer(id:ObjectRef) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.OpenContainer(id:ObjectRef, timeout:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `id` — Object/mobile serial or a supported Basic object reference such as self/backpack/lasttarget/saved object name; hexadecimal and decimal serials are accepted by Variant overloads.
- `timeout` — Delay/timeout in milliseconds; use a non-negative integer (for example 3000 = 3 seconds).

### Accepted values / constants

- `id` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `timeout` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 1, 2. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.OpenContainer(0)
END SUB
```

```basic
SUB Main()
    UO.OpenContainer(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.OpenContainer(self)
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = self # id
    VAR arg2 = 1000 # timeout
    UO.OpenContainer(arg1, arg2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = self # id
        UO.OpenContainer(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = self # id
    UO.OpenContainer(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.OpenContainer`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
