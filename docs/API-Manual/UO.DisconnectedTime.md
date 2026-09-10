# UO.DisconnectedTime

ClassicUO • Runtime API • `UO.DisconnectedTime.md`

## Точный синтаксис / Registered signatures

```text
UO.DisconnectedTime() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.DisconnectedTime`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает дату и время последнего отключения от сервера. Если подключения ещё не было, возвращает время загрузки профиля персонажа в Stealth.

### Current Basic signatures / Return

- `UO.DisconnectedTime() -> Decimal`
  - **Return type:** `Decimal`
  - **Return contract:** Decimal numeric runtime value.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DisconnectedTime"]` → `STATE -> InjectionApiState.DisconnectedTime`

**Pascal compatibility signature:** `function DisconnectedTime: TDateTime;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Operates on the active Basic/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.DisconnectedTime()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.DisconnectedTime()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.DisconnectedTime()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.DisconnectedTime()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
