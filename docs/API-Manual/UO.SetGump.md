# UO.SetGump

ClassicUO • Runtime API • `UO.SetGump.md`

## Точный синтаксис / Registered signatures

```text
UO.SetGump(gumpId:Any, identifier:Any, key:Any, stateValue:Any) -> Unit
UO.SetGump(identifier:Any, key:Any, stateValue:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetGump`

### Direct runtime overloads

- `UO.SetGump(identifier:String, key:String, stateValue:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetGump(gumpId:Variant, identifier:String, key:String, stateValue:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `identifier` — Named runtime value (String); use the exact registered/saved name expected by SetGump.
- `key` — Named runtime value (String); use the exact registered/saved name expected by SetGump.
- `stateValue` — Boolean-like value: TRUE/1 enables the option and FALSE/0 disables it unless Behavior documents another numeric mode.
- `gumpId` — Numeric identifier (Variant). Use the ID domain documented by this command; 0 is a sentinel only when Behavior/Notes explicitly says so.

### Accepted values / constants

- `identifier` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `key` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `stateValue` — TRUE/FALSE or 1/0.
- `gumpId` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

Registered arities: 3, 4. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetGump(0, 0, 0)
END SUB
```

```basic
SUB Main()
    UO.SetGump(0, 0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetGump(1, 2, 3)
END SUB
```

### Расширенная перегрузка: 4 аргументов

```vb
SUB Main()
    VAR arg1 = 0 # gumpId
    VAR arg2 = 2 # identifier
    VAR arg3 = 3 # key
    VAR arg4 = 4 # stateValue
    UO.SetGump(arg1, arg2, arg3, arg4)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 1 # identifier
        VAR arg2 = 2 # key
        VAR arg3 = 3 # stateValue
        UO.SetGump(arg1, arg2, arg3)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 1 # identifier
    VAR arg2 = 2 # key
    VAR arg3 = 3 # stateValue
    UO.SetGump(arg1, arg2, arg3)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.SetGump`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
