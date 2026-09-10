# UO.FindMan

ClassicUO • Runtime API • `UO.FindMan.md`

## Точный синтаксис / Registered signatures

```text
UO.FindMan() -> Unit
UO.FindMan(notoriety:Any) -> Any
UO.FindMan(notoriety:Any, distance:Any) -> Any
UO.FindMan(notoriety:Any, distance:Any, nearest:Any) -> Any
UO.FindMan(notoriety:Any, distance:Any, nearest:Any, maxZ:Any) -> Any
UO.FindMan(notoriety:Any, distance:Any, nearest:Any, maxZ:Any, body:Any) -> Any
UO.FindMan(notoriety:Any, distance:Any, nearest:Any, maxZ:Any, body:Any, color:Any) -> Any
UO.FindMan(notoriety:Any, distance:Any, nearest:Any, maxZ:Any, body:Any, color:Any, includeSelf:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindMan`

### Direct runtime overloads

- `UO.FindMan(notoriety:Variant) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety:Variant, distance:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety:Variant, distance:Integer, nearest:Boolean) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety:Variant, distance:Integer, nearest:Boolean, maxZ:Variant) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety:Variant, distance:Integer, nearest:Boolean, maxZ:Variant, body:GraphicId) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety:Variant, distance:Integer, nearest:Boolean, maxZ:Variant, body:GraphicId, color:Hue) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.
- `UO.FindMan(notoriety:Variant, distance:Integer, nearest:Boolean, maxZ:Variant, body:GraphicId, color:Hue, includeSelf:Boolean) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.

### Legacy Basic overloads

- `UO.FindMan() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** Mobile serial selected by the configured filters; 0 means no match.

### Parameters

- `notoriety` — Actual ClassicUO Mobile.Notoriety value or supported mask/string form; it is not inferred from hue/name/body.
- `distance` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.
- `nearest` — Boolean ordering flag. TRUE selects/orders nearest matches first; FALSE preserves the runtime search order.
- `maxZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.
- `body` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `includeSelf` — Boolean. TRUE allows the player mobile to be included; FALSE excludes self.

### Accepted values / constants

- `notoriety` — 0=unknown, 1=innocent/blue, 2=ally/green, 3=attackable/grey, 4=criminal/grey, 5=enemy/orange, 6=murderer/red, 7=invulnerable/yellow.
- `distance` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `nearest` — TRUE/FALSE or 1/0.
- `maxZ` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.
- `body` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `includeSelf` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

Registered arities: 0, 1, 2, 3, 4, 5, 6, 7. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Scans loaded mobiles only and applies notoriety, distance, nearest, Z/body/color/self and Ignore filters supported by the selected overload.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.FindMan(5)
END SUB
```

```basic
SUB Main()
    UO.FindMan()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.FindMan()
END SUB
```

### Расширенная перегрузка: 7 аргументов

```vb
SUB Main()
    VAR arg1 = -1 # notoriety
    VAR arg2 = 5 # distance
    VAR arg3 = 1 # nearest
    VAR arg4 = 4 # maxZ
    VAR arg5 = 0x0EED # body
    VAR arg6 = -1 # color
    VAR arg7 = 7 # includeSelf
    VAR result = UO.FindMan(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 1 аргументов

```vb
SUB Main()
    VAR result = UO.FindMan(-1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.FindMan(-1, 5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.FindMan(-1, 5, 1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.FindMan(-1, 5, 1, 4)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    VAR result = UO.FindMan(-1, 5, 1, 4, 0x0EED)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 6 аргументов

```vb
SUB Main()
    VAR result = UO.FindMan(-1, 5, 1, 4, 0x0EED, -1)
    UO.Print(CStr(result))
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.FindMan()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.FindMan()
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass66_0.<RegisterLegacyManualAliases>b__1`
- `InjectionScript.Runtime.InjectionApiUO.<RegisterCompactSearchApi>b__351_3`
