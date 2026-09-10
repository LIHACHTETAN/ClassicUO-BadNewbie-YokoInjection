# UO.GlobalChatJoinChannel

ClassicUO • Runtime API • `UO.GlobalChatJoinChannel.md`

## Точный синтаксис / Registered signatures

```text
UO.GlobalChatJoinChannel(ChName:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GlobalChatJoinChannel`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Присоединяется к указанному каналу глобального чата. ChName — название канала для подключения. Отправляет серверу пакет присоединения к чату. Текущий активный канал можно проверить через GlobalChatActiveChannel .

### Current Basic signatures / Return

- `UO.GlobalChatJoinChannel(ChName:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GlobalChatJoinChannel"]` → `BRIDGE CONTRACT -> IApiBridge.GlobalChatJoin`

**Pascal compatibility signature:** `procedure GlobalChatJoinChannel(ChName: String);`

### Parameters

- `ChName` — Named runtime value (String); use the exact registered/saved name expected by GlobalChatJoinChannel.

### Accepted values / constants

- `ChName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.GlobalChatJoinChannel('example')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.GlobalChatJoinChannel(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # ChName
    UO.GlobalChatJoinChannel(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ChName
    UO.GlobalChatJoinChannel(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
