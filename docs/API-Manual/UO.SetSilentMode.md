# UO.SetSilentMode

ClassicUO • Runtime API • `UO.SetSilentMode.md`

## Точный синтаксис / Registered signatures

```text
UO.SetSilentMode(Value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetSilentMode`

### Current Basic signatures / Return

- `UO.SetSilentMode(Value:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value.

### Parameters

- `Value` — Boolean-compatible value. `True` suppresses automatic Info Window dumps; `False` enables them.

### Accepted values / constants

- `Value` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Controls automatic diagnostic output to the Info Window. When silent mode is disabled (`False`), Gump description/query helpers may both return their data and mirror the lines into the Info Window. When silent mode is enabled (`True`), those helpers return data without automatic Info Window output.

### Notes / limitations

`FillInfoWindow`/explicit Info Window writes are not suppressed by this setting.

### Examples

```basic
SUB Main()
    UO.SetSilentMode(False)
    VAR lines = UO.GetGumpButtonsDescription(0)

    UO.SetSilentMode(True)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetSilentMode(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Value
    UO.SetSilentMode(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Value
    UO.SetSilentMode(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
