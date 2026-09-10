# UO.UseProxy

ClassicUO • Runtime API • `UO.UseProxy.md`

## Точный синтаксис / Registered signatures

```text
UO.UseProxy() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UseProxy`

### Current Basic signatures / Return

- `UO.UseProxy() -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** `0` means proxy mode is not enabled in the current embedded runtime.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Compatibility query for proxy mode. The current ClassicUO/Basic embedded runtime does not expose a separate proxy transport, so this returns `0` rather than pretending the normal game connection is a proxy.

### Notes / limitations

This command is retained for script compatibility. A future real proxy implementation must update `UseProxy`, `ProxyIP`, and `ProxyPort` together.

### Examples

```basic
SUB Main()
    IF UO.UseProxy() = 0 THEN
        UO.Print('Proxy disabled')
    END IF
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.UseProxy()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.UseProxy()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.UseProxy()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
