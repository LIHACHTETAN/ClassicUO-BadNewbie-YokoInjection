# UO.FindMobile

ClassicUO • Runtime API • `UO.FindMobile.md`

## Точный синтаксис / Registered signatures

```text
UO.FindMobile() -> Integer
UO.FindMobile(stateFilter:Any) -> Integer
UO.FindMobile(stateFilter:Any, rangeFilter:Any) -> Integer
UO.FindMobile(stateFilter:Any, rangeFilter:Any, verticalFilter:Any) -> Integer
UO.FindMobile(stateFilter:Any, rangeFilter:Any, verticalFilter:Any, directionFilter:Any, kindFilter:Any) -> Integer
UO.FindMobile(stateFilter:Any, rangeFilter:Any, verticalFilter:Any, directionOrKind:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindMobile`

### Direct runtime overloads

- `UO.FindMobile() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.FindMobile(stateFilter:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.FindMobile(stateFilter:String, rangeFilter:String|Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.FindMobile(stateFilter:String, rangeFilter:String|Integer, verticalFilter:String|Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.FindMobile(stateFilter:String, rangeFilter:String|Integer, verticalFilter:String|Integer, directionOrKind:String|Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.FindMobile(stateFilter:String, rangeFilter:String|Integer, verticalFilter:String|Integer, directionFilter:String|Integer, kindFilter:String|Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `stateFilter` — Mobile life-state filter: 'all', 'alive', or 'dead'.
- `rangeFilter` — Distance/radius/tolerance in tiles as a non-negative Integer; command-specific clamping/defaults are documented in Behavior.
- `verticalFilter` — Vertical filter: 'all', 'above', 'below', or a numeric Z/tolerance value accepted by the runtime parser.
- `directionOrKind` — Direction value: 0=N, 1=NE, 2=E, 3=SE, 4=S, 5=SW, 6=W, 7=NW; command-specific multi-step strings are documented where supported.
- `directionFilter` — Direction value: 0=N, 1=NE, 2=E, 3=SE, 4=S, 5=SW, 6=W, 7=NW; command-specific multi-step strings are documented where supported.
- `kindFilter` — Mobile kind filter: 'all', 'human', 'npc', or 'mob'/'monster' according to the loaded ClassicUO mobile classification.

### Accepted values / constants

- `stateFilter` — Mobile life-state filter: 'all', 'alive', or 'dead'.
- `rangeFilter` — Range filter: 'all', 'near', 'medium', 'far', or a non-negative numeric tile radius.
- `verticalFilter` — Vertical filter: 'all', 'above', 'below', or a numeric Z/tolerance value accepted by the runtime parser.
- `directionOrKind` — Direction filter: 'all', 'north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest', or numeric direction 0..7. In the 4-argument form the slot can alternatively hold a kind filter.
- `directionFilter` — Direction filter: 'all', 'north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest', or numeric direction 0..7. In the 4-argument form the slot can alternatively hold a kind filter.
- `kindFilter` — Mobile kind filter: 'all', 'human', 'npc', or 'mob'/'monster' according to the loaded ClassicUO mobile classification.

### Defaults / omitted arguments

The zero-argument form uses state/range/vertical/direction/kind='all'. Shorter overloads leave omitted trailing filters at 'all'.

### Behavior

Searches loaded ClassicUO mobiles with progressively narrower state/range/vertical/direction/kind filters. The zero-argument form is equivalent to all filters set to 'all'. Returns the selected mobile serial or 0 when no mobile matches.
### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR anyMobile = UO.FindMobile()
END SUB
```

```basic
SUB Main()
    VAR enemy = UO.FindMobile('alive', 18, 'all', 'east', 'human')
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.FindMobile()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 5 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # stateFilter
    VAR arg2 = 2 # rangeFilter
    VAR arg3 = 3 # verticalFilter
    VAR arg4 = 4 # directionFilter
    VAR arg5 = 5 # kindFilter
    VAR result = UO.FindMobile(arg1, arg2, arg3, arg4, arg5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 1 аргументов

```vb
SUB Main()
    VAR result = UO.FindMobile(1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.FindMobile(1, 2)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.FindMobile(1, 2, 3)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.FindMobile(1, 2, 3, 4)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.FindMobile()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.FindMobile()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_8`
- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_9`
- `InjectionScript.Runtime.InjectionApiUO.FindMobile`
