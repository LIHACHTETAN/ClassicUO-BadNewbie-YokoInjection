# UO.AddFigure

ClassicUO • Runtime API • `UO.AddFigure.md`

## Точный синтаксис / Registered signatures

```text
UO.AddFigure(Figure:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.AddFigure`

### Current Basic signatures / Return

- `UO.AddFigure(Figure:MapFigure) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Positive figure ID on success; `0` when the figure payload is invalid or cannot be registered.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.SetMapFigure` -> `WorldMapGump`.

### Parameters

- `Figure` — Basic `TMapFigure` adaptation.

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

- `Figure` — MapFigure. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Creates a persistent client-side overlay entry used by the actual ClassicUO `WorldMapGump`. The map renders line, ellipse, rectangle, direction-arrow and text figure kinds. World-coordinate figures follow the current map transform/zoom; screen-coordinate figures are relative to the map gump. The returned ID is used by `UpdateFigure` and `RemoveFigure`.

### Notes / limitations

- The figure is local to this ClassicUO client; no server packet is sent.
- Only figures whose `worldNum` matches the currently displayed facet are drawn.
- Historical `brushColor`/`brushStyle` fields are retained for compatibility; the current Basic renderer guarantees outline/text rendering and does not claim pixel-identical Delphi brush hatching.
- `fkDirection` with world coordinates and `x2=0,y2=0` draws from the current player toward `x1,y1`, matching the common Stealth usage pattern.
- Figures remain in the client-side map collection until removed/cleared or the process ends.

### Examples

```basic
SUB Main()
    # Red world-space rectangle with a label
    DIM fig(11)
    fig[0] = 2
    fig[1] = 0
    fig[2] = UO.GetX(self)-3
    fig[3] = UO.GetY(self)-3
    fig[4] = UO.GetX(self)+3
    fig[5] = UO.GetY(self)+3
    fig[6] = 0
    fig[7] = 1
    fig[8] = 255
    fig[9] = UO.WorldNum()
    fig[10] = 'Area'
    VAR figureId = UO.AddFigure(fig)
END SUB
```

```basic
SUB Main()
    # Direction arrow from player toward a world point
    DIM dirFig(11)
    dirFig[0] = 3
    dirFig[1] = 0
    dirFig[2] = UO.GetX(self)+10
    dirFig[3] = UO.GetY(self)
    dirFig[4] = 0
    dirFig[5] = 0
    dirFig[6] = 0
    dirFig[7] = 1
    dirFig[8] = 65280
    dirFig[9] = UO.WorldNum()
    dirFig[10] = 'East'
    VAR arrowId = UO.AddFigure(dirFig)
END SUB
```

# Search / World



## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.AddFigure(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # Figure
    VAR result = UO.AddFigure(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Figure
    VAR result = UO.AddFigure(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
