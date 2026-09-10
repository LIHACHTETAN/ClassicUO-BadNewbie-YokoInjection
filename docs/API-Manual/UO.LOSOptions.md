# UO.LOSOptions

ClassicUO • Runtime API • `UO.LOSOptions.md`

## Точный синтаксис / Registered signatures

```text
UO.LOSOptions() -> Any
UO.LOSOptions(value:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.LOSOptions`

### Current Basic signatures / Return

- `UO.LOSOptions() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Returns the currently configured LOS option bitmask.
- `UO.LOSOptions(value:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Stores `value` and returns the resulting bitmask.

### Parameters

- `value` — integer bitmask. The low byte selects the compatibility algorithm family; optional flags are OR-ed into the value:
  - `1` — Sphere compatibility mode.
  - `2` — SphereAdv compatibility mode.
  - `3` — RunUO compatibility mode.
  - `4` — POL compatibility mode.
  - `0x100` / `256` — check both adjacent cardinal cells during a diagonal LOS step.
  - `0x200` / `512` — in POL mode, respect the tile `NoShoot` flag.
  - `0x400` / `1024` — in POL mode, allow LOS through tiles flagged as windows.

### Accepted values / constants

- `value` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 0, 1. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

`LOSOptions` is no longer a state-only setting. `UO.CheckLOS(...)` consumes the current value on every check. The Basic implementation evaluates the currently loaded ClassicUO map, land, static, multi and world-item tile data. Walls and impassable tiles block LOS; RunUO mode also respects `NoShoot`; POL can opt into `NoShoot` and window-through behavior with the flags above.

The optional `0x100` flag adds corner validation: on a diagonal ray step both adjacent cardinal cells must remain clear.

### Notes / limitations

This is a **Basic / ClassicUO adaptation** of the historical Stealth LOS options, not a byte-for-byte reimplementation of the external Stealth Sphere/RunUO/POL engines. Checks are limited to the **currently loaded ClassicUO map/facet**. If `value` contains an unknown algorithm number in the low byte, the ClassicUO implementation falls back to RunUO-style handling.

`LOSOptions(0)` disables the additional tile-option pass and leaves `CheckLOS` using the portable movement/world-step visibility path.

### Examples

```basic
SUB Main()
    # RunUO-style LOS
    UO.LOSOptions(3)
    VAR visible = UO.CheckLOS(UO.GetX('self'), UO.GetY('self'), UO.GetZ('self'), 1500, 1600, 0, UO.WorldNum())
    UO.Print(visible)
END SUB
```

```basic
SUB Main()
    # POL + NoShoot + allow windows
    UO.LOSOptions(4 + 512 + 1024)
END SUB
```

```basic
SUB Main()
    # Sphere-compatible selection + diagonal corner validation
    UO.LOSOptions(1 + 256)
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.LOSOptions()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # value
    VAR result = UO.LOSOptions(arg1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.LOSOptions()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.LOSOptions()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
