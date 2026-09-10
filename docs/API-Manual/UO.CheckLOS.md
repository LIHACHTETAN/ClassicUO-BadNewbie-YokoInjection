# UO.CheckLOS

ClassicUO • Runtime API • `UO.CheckLOS.md`

Положительный результат требует достижения конечной точки. Превышение лимита обхода и недопустимые координаты не считаются успехом.

## Точный синтаксис / Registered signatures

```text
UO.CheckLOS(Xfrom:Any, Yfrom:Any, Zfrom:Any, Xto:Any, Yto:Any, Zto:Any, WorldNum:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.CheckLOS`

### Current Basic signatures / Return

- `UO.CheckLOS(Xfrom:Integer, Yfrom:Integer, Zfrom:Integer, Xto:Integer, Yto:Integer, Zto:Integer, WorldNum:Integer) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** `1` when the Basic/ClassicUO LOS path is clear; `0` when it is blocked, the requested map is not the loaded map, or a required world step cannot be validated.

### Parameters

- `Xfrom`, `Yfrom`, `Zfrom` — starting world coordinates.
- `Xto`, `Yto`, `Zto` — destination world coordinates.
- `WorldNum` — map/facet index. The current implementation requires this to match the currently loaded ClassicUO map.
- `Xfrom` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `Yfrom` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `Zfrom` — Signed world Z/elevation or vertical tolerance as Integer, according to this command's Behavior contract.
- `Xto` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `Yto` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `Zto` — Signed world Z/elevation or vertical tolerance as Integer, according to this command's Behavior contract.

### Accepted values / constants

- `Xfrom` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Yfrom` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Zfrom` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Xto` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Yto` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Zto` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `WorldNum` — Standard facet IDs: 0=Felucca, 1=Trammel, 2=Ilshenar, 3=Malas, 4=Tokuno, 5=Ter Mur, subject to shard/client support.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

The command traces from the start point to the destination and validates world movement cells. When `UO.LOSOptions()` is non-zero, every traced cell is additionally checked against the loaded ClassicUO land/static/multi/item tile data. The selected LOS algorithm family and flags affect `NoShoot`, windows and diagonal-corner behavior.

At the destination the vertical difference must be within the current portable LOS tolerance; otherwise the result is `0`.

### Notes / limitations

This is a **Basic / ClassicUO adaptation** designed for current runtime behavior. It does not claim bit-identical results with every historical external Stealth LOS engine. Arbitrary offline facets are not loaded solely for this call; pass the current `UO.WorldNum()` unless the corresponding map is actually active.

For the meaning of algorithm values and flags, see `UO.LOSOptions`.

### Examples

```basic
SUB Main()
    VAR x1 = UO.GetX('self')
    VAR y1 = UO.GetY('self')
    VAR z1 = UO.GetZ('self')

    UO.LOSOptions(3)
    VAR visible = UO.CheckLOS(x1, y1, z1, x1 + 10, y1, z1, UO.WorldNum())
    UO.Print(visible)
END SUB
```

```basic
SUB Main()
    # Require diagonal corner clearance too
    UO.LOSOptions(3 + 256)
    VAR visible = UO.CheckLOS(1000, 1000, 0, 1010, 1010, 0, UO.WorldNum())
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.CheckLOS(1, 2, 3, 4, 5, 6, 7)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # Xfrom
    VAR arg2 = 2 # Yfrom
    VAR arg3 = 3 # Zfrom
    VAR arg4 = 4 # Xto
    VAR arg5 = 5 # Yto
    VAR arg6 = 6 # Zto
    VAR arg7 = 7 # WorldNum
    VAR result = UO.CheckLOS(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Xfrom
    VAR arg2 = 2 # Yfrom
    VAR arg3 = 3 # Zfrom
    VAR arg4 = 4 # Xto
    VAR arg5 = 5 # Yto
    VAR arg6 = 6 # Zto
    VAR arg7 = 7 # WorldNum
    VAR result = UO.CheckLOS(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
