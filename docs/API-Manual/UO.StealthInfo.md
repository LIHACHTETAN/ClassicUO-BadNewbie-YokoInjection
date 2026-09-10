# UO.StealthInfo

ClassicUO • Runtime API • `UO.StealthInfo.md`

## Точный синтаксис / Registered signatures

```text
UO.StealthInfo() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.StealthInfo`

### Current Basic signatures / Return

- `UO.StealthInfo() -> AboutData`
  - **Return type:** `AboutData`
  - **Return contract:** Returns `[productName, productVersion, clientPath]` from the active ClassicUO/Basic bridge.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Returns information about the actual product version and embedded ClassicUO / BadNewbie / Basic IDE runtime as `[productName, productVersion, clientPath]`. The version is sourced from the current Basic IDE product version instead of the old hard-coded compatibility value `1.0`.
### Notes / limitations

This is a Basic-adapted information array, not the original Stealth record structure.

### Examples

```basic
SUB Main()
    VAR info = UO.StealthInfo()
    UO.Print(info)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.StealthInfo()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.StealthInfo()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.StealthInfo()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
