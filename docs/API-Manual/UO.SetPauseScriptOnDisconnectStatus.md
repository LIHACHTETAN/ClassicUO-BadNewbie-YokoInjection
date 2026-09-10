# UO.SetPauseScriptOnDisconnectStatus

ClassicUO • Runtime API • `UO.SetPauseScriptOnDisconnectStatus.md`

## Точный синтаксис / Registered signatures

```text
UO.SetPauseScriptOnDisconnectStatus(Value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetPauseScriptOnDisconnectStatus`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Включает или отключает автоматическую приостановку скрипта при отключении персонажа от сервера. Value — True для приостановки скрипта при отключении, False для продолжения выполнения. При включении выполнение скрипта приостанавливается при отключении и возобновляется при восстановлении соединения (например, через автопереподключение). Это предотвращает выполнение игровых команд во время отключения, которые иначе были бы молча отброшены. Используйте GetPauseScriptOnDisconnectStatus для чтения текущего состояния. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.SetPauseScriptOnDisconnectStatus(Value:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetPauseScriptOnDisconnectStatus"]` → `BRIDGE CONTRACT -> IApiBridge.SetPauseScriptOnDisconnectStatus`

**Pascal compatibility signature:** `procedure SetPauseScriptOnDisconnectStatus(Value: Boolean);`

### Parameters

- `Value` — Boolean value. The concrete accepted domain is command-specific and is stated in Behavior/Notes; do not assume String conversion when the overload is numeric.

### Accepted values / constants

- `Value` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Operates on the active Basic/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetPauseScriptOnDisconnectStatus(TRUE)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetPauseScriptOnDisconnectStatus(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Value
    UO.SetPauseScriptOnDisconnectStatus(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Value
    UO.SetPauseScriptOnDisconnectStatus(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
