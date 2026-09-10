# UO.IsTreeTile

ClassicUO • Runtime API • `UO.IsTreeTile.md`

## Точный синтаксис / Registered signatures

```text
UO.IsTreeTile(x:Any, y:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.IsTreeTile`

### Direct runtime overloads

- `UO.IsTreeTile(x:Integer, y:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `x` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `y` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.

### Accepted values / constants

- `x` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `y` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.IsTreeTile(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.IsTreeTile(UO.GetX(), UO.GetY())
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = UO.GetX() # x
    VAR arg2 = UO.GetY() # y
    VAR result = UO.IsTreeTile(arg1, arg2)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = UO.GetX() # x
    VAR arg2 = UO.GetY() # y
    VAR result = UO.IsTreeTile(arg1, arg2)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.IsTreeTile`
