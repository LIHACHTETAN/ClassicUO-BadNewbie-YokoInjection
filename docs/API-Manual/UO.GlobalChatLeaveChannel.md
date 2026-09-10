# UO.GlobalChatLeaveChannel

ClassicUO • Runtime API • `UO.GlobalChatLeaveChannel.md`

## Точный синтаксис / Registered signatures

```text
UO.GlobalChatLeaveChannel() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GlobalChatLeaveChannel`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Покидает текущий канал глобального чата. Метод автоматически определяет имя активного канала и отправляет пакет выхода из него. Параметры не требуются.

### Current Basic signatures / Return

- `UO.GlobalChatLeaveChannel() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GlobalChatLeaveChannel"]` → `BRIDGE CONTRACT -> IApiBridge.GlobalChatLeave`

**Pascal compatibility signature:** `procedure GlobalChatLeaveChannel;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.GlobalChatLeaveChannel()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.GlobalChatLeaveChannel()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.GlobalChatLeaveChannel()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.GlobalChatLeaveChannel()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
