# UO.UpdateFigure

ClassicUO • Runtime API • `UO.UpdateFigure.md`

## Точный синтаксис / Registered signatures

```text
UO.UpdateFigure(FigureID:Any, figure:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UpdateFigure`

### Current Basic signatures / Return

- `UO.UpdateFigure(FigureID:Integer, Figure:MapFigure) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** `1` when the existing visual figure is updated; `0` when `FigureID` does not exist or the new figure payload is invalid.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.SetMapFigure` -> `WorldMapGump`.

### Parameters

- `FigureID` — ID returned by `UO.AddFigure`.
- `Figure` — replacement Basic `TMapFigure` adaptation.

Basic represents the historical `TMapFigure` record as an array (or `|`-separated compatibility string):

`[kind, coord, x1, y1, x2, y2, brushColor, brushStyle, color, worldNum, text]`

- `kind`: `0=fkLine`, `1=fkEllipse`, `2=fkRectangle`, `3=fkDirection`, `4=fkText`.
- `coord`: `0=fcWorld`, `1=fcScreen`.
- `x1,y1,x2,y2`: figure coordinates.
- `brushColor`: historical fill/brush color field.
- `brushStyle`: historical brush-style field (`0=solid`, `1=clear`, etc.).
- `color`: outline/text color in Delphi `TColor` byte order (`0x00BBGGRR`).
- `worldNum`: facet/map index; omitted value defaults to the current world.
- `text`: label text; optional.

### Accepted values / constants

- `FigureID` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Figure` — MapFigure. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Replaces the stored geometry/style/text for an existing figure and the next World Map render uses the updated values.

### Notes / limitations

The same local-only and brush-rendering limitations as `AddFigure` apply. Unknown IDs are not created implicitly; use `AddFigure` to allocate a new ID.

### Examples

```basic
SUB Main()
    DIM fig(11)
    fig[0] = 4
    fig[1] = 0
    fig[2] = UO.GetX(self)
    fig[3] = UO.GetY(self)
    fig[4] = 0
    fig[5] = 0
    fig[6] = 0
    fig[7] = 1
    fig[8] = 65535
    fig[9] = UO.WorldNum()
    fig[10] = 'Updated'
    IF UO.UpdateFigure(figureId, fig) = 0 THEN
        UO.Print('Figure not found')
    END IF
END SUB
```



## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.UpdateFigure(1, 2)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # FigureID
    VAR arg2 = 2 # figure
    VAR result = UO.UpdateFigure(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # FigureID
    VAR arg2 = 2 # figure
    VAR result = UO.UpdateFigure(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
