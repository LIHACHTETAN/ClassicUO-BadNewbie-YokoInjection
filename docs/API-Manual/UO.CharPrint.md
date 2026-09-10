# UO.CharPrint

ClassicUO • Runtime API • `UO.CharPrint.md`

## Точный синтаксис / Registered signatures

```text
UO.CharPrint(color:Integer, msg:String) -> Unit
UO.CharPrint(color:String, msg:String) -> Unit
UO.CharPrint(id:Any, color:Any, msg:Any) -> Unit
UO.CharPrint(id:Integer, color:Integer, msg:String) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.CharPrint`

### Direct runtime overloads

- `UO.CharPrint(color:Integer, msg:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.CharPrint(color:String, msg:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.CharPrint(id:Integer, color:Integer, msg:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.CharPrint(id:ObjectRef, color:Hue, msg:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `color` — Hue/color value. Use decimal or 0x-prefixed hexadecimal; -1 means any/default hue only where the command explicitly supports it.
- `msg` — Text value (Any / String); pass it as a quoted BASIC string.
- `id` — Object/mobile serial or a supported Basic object reference such as self/backpack/lasttarget/saved object name; hexadecimal and decimal serials are accepted by Variant overloads.

### Accepted values / constants

- `color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `msg` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `id` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

Registered arities: 2, 3. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.CharPrint(0, 0)
END SUB
```

```basic
SUB Main()
    UO.CharPrint(0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.CharPrint(-1, 'example')
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = self # id
    VAR arg2 = -1 # color
    VAR arg3 = 'example' # msg
    UO.CharPrint(arg1, arg2, arg3)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = -1 # color
        VAR arg2 = 'example' # msg
        UO.CharPrint(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = -1 # color
    VAR arg2 = 'example' # msg
    UO.CharPrint(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.CharPrint`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
