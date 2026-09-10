# UO.RemoveFigure

ClassicUO • Runtime API • `UO.RemoveFigure.md`

## Точный синтаксис / Registered signatures

```text
UO.RemoveFigure(FigureID:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.RemoveFigure`

### Current Basic signatures / Return

- `UO.RemoveFigure(FigureID:Integer) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** `1` if the figure existed and was removed from the visual World Map collection; `0` if the ID was not present.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.RemoveMapFigure` -> `WorldMapGump`.

### Parameters

- `FigureID` — ID previously returned by `UO.AddFigure`.

### Accepted values / constants

- `FigureID` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Removes the corresponding client-side overlay from `WorldMapGump` and from Basic runtime figure state.

### Notes / limitations

Local client operation only; no server packet is sent.

### Examples

```basic
SUB Main()
    IF UO.RemoveFigure(figureId) = 0 THEN
        UO.Print('Figure already absent')
    END IF
END SUB
```



## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.RemoveFigure(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # FigureID
    VAR result = UO.RemoveFigure(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # FigureID
    VAR result = UO.RemoveFigure(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
