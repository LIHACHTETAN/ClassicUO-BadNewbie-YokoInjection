# UO.GetTileXYM

ClassicUO • Runtime API • `UO.GetTileXYM.md`

## Точный синтаксис / Registered signatures

```text
UO.GetTileXYM(x:Any, y:Any, map:Any, tileStart:Any, tileEnd:Any, uoPath:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetTileXYM`

### Direct runtime overloads

- `UO.GetTileXYM(x:Integer, y:Integer, map:Integer, tileStart:Variant, tileEnd:Variant, uoPath:String) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.

### Parameters

- `x` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `y` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `map` — Facet/map index. Standard values are 0=Felucca, 1=Trammel, 2=Ilshenar, 3=Malas, 4=Tokuno, 5=Ter Mur where supported by the shard/client data.
- `tileStart` — Variant value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.
- `tileEnd` — Variant value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.
- `uoPath` — Text value (String); pass it as a quoted BASIC string.

### Accepted values / constants

- `x` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `y` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `map` — Standard facet IDs: 0=Felucca, 1=Trammel, 2=Ilshenar, 3=Malas, 4=Tokuno, 5=Ter Mur, subject to shard/client support.
- `tileStart` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.
- `tileEnd` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.
- `uoPath` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.GetTileXYM(0, 0, 0, 0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetTileXYM(UO.GetX(), UO.GetY(), 3, 4, 5, 'example.txt')
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = UO.GetX() # x
    VAR arg2 = UO.GetY() # y
    VAR arg3 = 3 # map
    VAR arg4 = 4 # tileStart
    VAR arg5 = 5 # tileEnd
    VAR arg6 = 'example.txt' # uoPath
    VAR result = UO.GetTileXYM(arg1, arg2, arg3, arg4, arg5, arg6)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = UO.GetX() # x
    VAR arg2 = UO.GetY() # y
    VAR arg3 = 3 # map
    VAR arg4 = 4 # tileStart
    VAR arg5 = 5 # tileEnd
    VAR arg6 = 'example.txt' # uoPath
    VAR result = UO.GetTileXYM(arg1, arg2, arg3, arg4, arg5, arg6)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GetTileXYM`
