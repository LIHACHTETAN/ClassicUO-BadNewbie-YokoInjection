# UO.Buy

ClassicUO • Runtime API • `UO.Buy.md`

## Точный синтаксис / Registered signatures

```text
UO.Buy(type:Any) -> Unit
UO.Buy(type:Any, color:Any) -> Unit
UO.Buy(type:Any, color:Any, quantity:Any) -> Unit
UO.Buy(type:Any, color:Any, quantity:Any, maxPrice:Any) -> Unit
UO.Buy(type:Any, color:Any, quantity:Any, maxPrice:Any, name:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Buy`

### Manifest-registered overloads

- `UO.Buy(type:GraphicId) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Buy(type:GraphicId, color:Hue) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Buy(type:GraphicId, color:Hue, quantity:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Buy(type:GraphicId, color:Hue, quantity:Integer, maxPrice:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Buy(type:GraphicId, color:Hue, quantity:Integer, maxPrice:Integer, name:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `quantity` — Quantity/count. 0 may mean all/default only where explicitly supported.
- `maxPrice` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by this command.
- `name` — Named runtime value (String); use the exact registered/saved name expected by Buy.

### Accepted values / constants

- `type` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `quantity` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `maxPrice` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `name` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 1, 2, 3, 4, 5. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.Buy(0)
END SUB
```

```basic
SUB Main()
    UO.Buy(0x0190, -1, 1, 0, 'example')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.Buy(0x0EED)
END SUB
```

### Расширенная перегрузка: 5 аргументов

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR arg2 = -1 # color
    VAR arg3 = 3 # quantity
    VAR arg4 = 4 # maxPrice
    VAR arg5 = 'example' # name
    UO.Buy(arg1, arg2, arg3, arg4, arg5)
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    UO.Buy(0x0EED, -1)
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    UO.Buy(0x0EED, -1, 3)
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    UO.Buy(0x0EED, -1, 3, 4)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 0x0EED # type
        UO.Buy(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 0x0EED # type
    UO.Buy(arg1)
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
