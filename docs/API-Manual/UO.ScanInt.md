# UO.ScanInt

ClassicUO • Runtime API • `UO.ScanInt.md`

## Точный синтаксис / Registered signatures

```text
UO.ScanInt(textValue:Any, startValue:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ScanInt`

### Direct runtime overloads

- `UO.ScanInt(textValue:String, startValue:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `textValue` — Text/String value (String); pass literal text as a quoted BASIC string.
- `startValue` — Integer value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `textValue` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `startValue` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.ScanInt(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ScanInt(1, 2)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 1 # textValue
    VAR arg2 = 2 # startValue
    VAR result = UO.ScanInt(arg1, arg2)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 1 # textValue
    VAR arg2 = 2 # startValue
    VAR result = UO.ScanInt(arg1, arg2)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.ScanInt`
