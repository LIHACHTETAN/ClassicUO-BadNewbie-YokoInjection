# UO.ProxyIP

ClassicUO • Runtime API • `UO.ProxyIP.md`

## Точный синтаксис / Registered signatures

```text
UO.ProxyIP() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ProxyIP`

### Current Basic signatures / Return

- `UO.ProxyIP() -> String`
  - **Return type:** `String`
  - **Return contract:** Returns the configured Basic proxy address. In the current embedded runtime, proxy mode is not implemented, therefore the value is an empty string.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reports proxy state only. It deliberately does **not** return the game-server IP as a fake proxy address.

### Notes / limitations

Use the normal server/address APIs for the actual game endpoint. `ProxyIP` remains empty until a real proxy layer is configured/implemented.

### Examples

```basic
SUB Main()
    VAR proxy = UO.ProxyIP()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ProxyIP()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.ProxyIP()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.ProxyIP()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
