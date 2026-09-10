# UO.PrivateGetTile

ClassicUO • Runtime API • `UO.PrivateGetTile.md`

## Точный синтаксис / Registered signatures

```text
UO.PrivateGetTile(x:Integer, y:Integer, unknown:Integer, minTile:Integer, maxTile:Integer) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.PrivateGetTile`

### Direct runtime overloads

- `UO.PrivateGetTile(x:Integer, y:Integer, unknown:Integer, minTile:Integer, maxTile:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `x` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `y` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `unknown` — Integer value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.
- `minTile` — Integer value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.
- `maxTile` — Integer value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `x` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `y` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `unknown` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `minTile` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `maxTile` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.PrivateGetTile(0, 0, 0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.PrivateGetTile(UO.GetX(), UO.GetY(), 3, 4, 5)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = UO.GetX() # x
    VAR arg2 = UO.GetY() # y
    VAR arg3 = 3 # unknown
    VAR arg4 = 4 # minTile
    VAR arg5 = 5 # maxTile
    VAR result = UO.PrivateGetTile(arg1, arg2, arg3, arg4, arg5)
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
    VAR arg1 = UO.GetX() # x
    VAR arg2 = UO.GetY() # y
    VAR arg3 = 3 # unknown
    VAR arg4 = 4 # minTile
    VAR arg5 = 5 # maxTile
    VAR result = UO.PrivateGetTile(arg1, arg2, arg3, arg4, arg5)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.PrivateGetTile`
