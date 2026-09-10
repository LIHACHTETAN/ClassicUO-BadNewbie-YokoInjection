# UO.ProxyPort

ClassicUO • Runtime API • `UO.ProxyPort.md`

## Точный синтаксис / Registered signatures

```text
UO.ProxyPort() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ProxyPort`

### Current Basic signatures / Return

- `UO.ProxyPort() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Returns the configured proxy port. Current embedded Basic proxy support is disabled/unimplemented, so the result is `0`.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reports proxy state only and does not mirror the game-server port.

### Notes / limitations

`0` is the explicit compatibility value until a separate proxy transport is implemented.

### Examples

```basic
SUB Main()
    VAR port = UO.ProxyPort()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ProxyPort()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.ProxyPort()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.ProxyPort()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
