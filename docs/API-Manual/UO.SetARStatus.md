# UO.SetARStatus

ClassicUO • Runtime API • `UO.SetARStatus.md`

## Точный синтаксис / Registered signatures

```text
UO.SetARStatus(Value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetARStatus`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Включает или отключает автоматическое переподключение для текущего персонажа. Value — True для включения, False для отключения. При включении Stealth автоматически пытается переподключиться после отключения, используя таймер переподключения из профиля (параметр ReconnectTime в настройках профиля). Расширенные параметры настраиваются через SetARExtParams . Используйте GetARStatus для чтения текущего состояния. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.SetARStatus(Value:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetARStatus"]` → `BRIDGE CONTRACT -> IApiBridge.SetAutoReconnect`

**Pascal compatibility signature:** `procedure SetARStatus(Value: Boolean);`

### Parameters

- `Value` — Auto-reconnect flag: TRUE/1 enables automatic reconnect; FALSE/0 disables it.

### Accepted values / constants

- `Value` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetARStatus(TRUE)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetARStatus(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Value
    UO.SetARStatus(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Value
    UO.SetARStatus(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
