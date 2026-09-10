# UO.Launch

ClassicUO • Runtime API • `UO.Launch.md`

## Точный синтаксис / Registered signatures

```text
UO.Launch(file:Any) -> Integer
UO.Launch(file:Any, parameters:Any) -> Integer
UO.Launch(file:Any, parameters:Any, workingDirectory:Any) -> Integer
UO.Launch(file:Any, parameters:Any, workingDirectory:Any, hidden:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Launch`

### Direct runtime overloads

- `UO.Launch(fileName:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `fileName` — Text value (String); pass it as a quoted BASIC string.

### Accepted values / constants

- `fileName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.Launch(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.Launch('example.txt')
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 4 аргументов

```vb
SUB Main()
    VAR arg1 = 'example.txt' # file
    VAR arg2 = 2 # parameters
    VAR arg3 = 3 # workingDirectory
    VAR arg4 = 4 # hidden
    VAR result = UO.Launch(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.Launch('example.txt', 2)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.Launch('example.txt', 2, 3)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 'example.txt' # file
    VAR result = UO.Launch(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 'example.txt' # file
    VAR result = UO.Launch(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_22`
