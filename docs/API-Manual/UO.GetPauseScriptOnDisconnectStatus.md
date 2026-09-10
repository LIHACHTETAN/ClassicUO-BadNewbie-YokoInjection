# UO.GetPauseScriptOnDisconnectStatus

ClassicUO • Runtime API • `UO.GetPauseScriptOnDisconnectStatus.md`

## Точный синтаксис / Registered signatures

```text
UO.GetPauseScriptOnDisconnectStatus() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetPauseScriptOnDisconnectStatus`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает состояние настройки «Пауза скрипта при отключении»: True — включено, False — выключено. Когда включено, скрипт автоматически ставится на паузу при отключении и возобновляется при переподключении.

### Current Basic signatures / Return

- `UO.GetPauseScriptOnDisconnectStatus() -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetPauseScriptOnDisconnectStatus"]` → `BRIDGE CONTRACT -> IApiBridge.GetPauseScriptOnDisconnectStatus`

**Pascal compatibility signature:** `function GetPauseScriptOnDisconnectStatus: Boolean;`

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
    VAR result = UO.GetPauseScriptOnDisconnectStatus()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetPauseScriptOnDisconnectStatus()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.GetPauseScriptOnDisconnectStatus()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.GetPauseScriptOnDisconnectStatus()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
