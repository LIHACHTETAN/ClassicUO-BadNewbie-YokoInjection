# UO.FindList

ClassicUO • Runtime API • `UO.FindList.md`

## Точный синтаксис / Registered signatures

```text
UO.FindList(list:Any) -> String
UO.FindList(list:Any, container:Any) -> String
UO.FindList(list:Any, container:Any, distance:Any) -> String
UO.FindList(list:Any, container:Any, distance:Any, notoriety:Any) -> String
UO.FindList(list:Any, container:Any, distance:Any, notoriety:Any, nearest:Any) -> String
UO.FindList(list:Any, container:Any, distance:Any, notoriety:Any, nearest:Any, maxZ:Any) -> String
UO.FindList(list:Any, container:Any, distance:Any, notoriety:Any, nearest:Any, maxZ:Any, includeIgnored:Any) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindList`

### Direct runtime overloads

- `UO.FindList(list:String) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.
- `UO.FindList(list:String, container:ObjectRef) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.
- `UO.FindList(list:String, container:ObjectRef, distance:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.
- `UO.FindList(list:String, container:ObjectRef, distance:Integer, notoriety:Variant) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.
- `UO.FindList(list:String, container:ObjectRef, distance:Integer, notoriety:Variant, nearest:Boolean) -> String`
  - **Return type:** `String`
  - **Return contract:** Hexadecimal serial string selected by the named/list Search Core filter; empty string means no match.

### Parameters

- `list` — Named runtime value (String); use the exact registered/saved name expected by FindList.
- `container` — Container/object destination. Use backpack/ground/self/saved object name or a valid hexadecimal/decimal serial where that overload permits it.
- `distance` — Distance/radius/tolerance in tiles as a non-negative Integer; command-specific clamping/defaults are documented in Behavior.
- `notoriety` — Notoriety code: 0 unknown, 1 blue, 2 green, 3 attackable grey, 4 criminal grey, 5 orange enemy, 6 red murderer, 7 invulnerable yellow.
- `nearest` — Boolean-like runtime value: TRUE/1 enables the option and FALSE/0 disables it unless the command documents another numeric mode.

### Accepted values / constants

- `list` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `container` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `distance` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `notoriety` — 0=unknown, 1=innocent/blue, 2=ally/green, 3=attackable/grey, 4=criminal/grey, 5=enemy/orange, 6=murderer/red, 7=invulnerable/yellow.
- `nearest` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

Registered arities: 1, 2, 3, 4, 5. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Resolves the named list created in runtime state, then executes the same Search Core used by FindType/FindNotoriety. The list name is not treated as a numeric type string.

### Notes / limitations

The named list must exist in runtime state. Missing/empty lists produce the documented no-match result instead of inventing a type from the list name.

### Examples

```basic
SUB Main()
    VAR result = UO.FindList(0)
END SUB
```

```basic
SUB Main()
    VAR result = UO.FindList(0, 0, 0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.FindList(1)
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 7 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # list
    VAR arg2 = backpack # container
    VAR arg3 = 5 # distance
    VAR arg4 = -1 # notoriety
    VAR arg5 = 1 # nearest
    VAR arg6 = 6 # maxZ
    VAR arg7 = 7 # includeIgnored
    VAR result = UO.FindList(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.FindList(1, backpack)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.FindList(1, backpack, 5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.FindList(1, backpack, 5, -1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    VAR result = UO.FindList(1, backpack, 5, -1, 1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 6 аргументов

```vb
SUB Main()
    VAR result = UO.FindList(1, backpack, 5, -1, 1, 6)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = 1 # list
    VAR result = UO.FindList(arg1)
    IF len(result) > 0 THEN
        UO.Print(result)
    ELSE
        UO.Print('Empty')
    END IF
END SUB
```

### Поиск текста в результате

```vb
SUB Main()
    VAR arg1 = 1 # list
    VAR result = UO.FindList(arg1)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_15`
