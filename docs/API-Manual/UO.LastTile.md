# UO.LastTile

ClassicUO • Runtime API • `UO.LastTile.md`

## Точный синтаксис / Registered signatures

```text
UO.LastTile() -> String
UO.LastTile(index:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.LastTile`

### Direct runtime overloads

- `UO.LastTile() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
- `UO.LastTile(index:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `index` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by this command.

### Accepted values / constants

- `index` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 0, 1. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.LastTile()
END SUB
```

```basic
SUB Main()
    VAR result = UO.LastTile(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.LastTile()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 0 # index
    VAR result = UO.LastTile(arg1)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR result = UO.LastTile()
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
    VAR result = UO.LastTile()
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.LastTile`
