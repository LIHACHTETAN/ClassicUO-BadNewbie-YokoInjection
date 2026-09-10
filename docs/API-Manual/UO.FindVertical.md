# UO.FindVertical

ClassicUO • Runtime API • `UO.FindVertical.md`

## Точный синтаксис / Registered signatures

```text
UO.FindVertical() -> Any
UO.FindVertical(value:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindVertical`

### Current Basic signatures / Return

- `UO.FindVertical() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Current vertical ground-search radius in Z tiles.
  - **Runtime route:** `InjectionApiUO.ExecuteStealthCompatibility["FindVertical"] -> IApiBridge.GetFindVertical`.
- `UO.FindVertical(value:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No return value. The stored value is clamped to the supported range.
  - **Runtime route:** `InjectionApiUO.ExecuteStealthCompatibility["FindVertical"] -> IApiBridge.SetFindVertical`.

### Parameters

- `value` — `Integer`; requested vertical/Z search radius in tiles. Accepted effective range: **0..120**. Values below 0 become 0; values above 120 become 120.

### Accepted values / constants

- `value` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

The shared FindVertical state defaults to 2 tiles; setter values above 120 are clamped to 120.

### Behavior

Gets or sets the shared vertical tolerance used by ground-based Search Core operations such as `FindType`, `FindTypeEx` and `FindTypesArrayEx` when an overload does not provide its own explicit Z limit. Default profile/runtime value is **2**.

### Notes / limitations

`FindVertical` affects **ground searches**; it is not a general world-view or container-recursion setting. The maximum effective value is 120 even if a larger integer is supplied.

### Examples

```basic
SUB Main()
    VAR oldZ = UO.FindVertical()
    UO.FindVertical(12)
END SUB
```

```basic
SUB Main()
    UO.FindVertical(255)  # effective value becomes 120
    VAR effectiveZ = UO.FindVertical()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.FindVertical()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # value
    VAR result = UO.FindVertical(arg1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.FindVertical()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.FindVertical()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
