# UO.ColorPrint

ClassicUO • Runtime API • `UO.ColorPrint.md`

## Точный синтаксис / Registered signatures

```text
UO.ColorPrint(color:Any, msg:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ColorPrint`

### Direct runtime overloads

- `UO.ColorPrint(color:Hue, msg:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `color` — Hue/color value. Use decimal or 0x-prefixed hexadecimal; -1 means any/default hue only where the command explicitly supports it.
- `msg` — Text value (String); pass it as a quoted BASIC string.

### Accepted values / constants

- `color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `msg` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.ColorPrint(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.ColorPrint(-1, 2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = -1 # color
        VAR arg2 = 2 # msg
        UO.ColorPrint(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = -1 # color
    VAR arg2 = 2 # msg
    UO.ColorPrint(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.ColorPrint`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
