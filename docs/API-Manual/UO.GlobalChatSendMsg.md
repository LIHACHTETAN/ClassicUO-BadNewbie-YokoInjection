# UO.GlobalChatSendMsg

ClassicUO • Runtime API • `UO.GlobalChatSendMsg.md`

## Точный синтаксис / Registered signatures

```text
UO.GlobalChatSendMsg(MsgText:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GlobalChatSendMsg`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет сообщение в текущий канал глобального чата. MsgText — текст отправляемого сообщения. Персонаж должен находиться в чат-канале (см. GlobalChatJoinChannel ), чтобы сообщение было доставлено.

### Current Basic signatures / Return

- `UO.GlobalChatSendMsg(MsgText:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GlobalChatSendMsg"]` → `BRIDGE CONTRACT -> IApiBridge.GlobalChatSend`

**Pascal compatibility signature:** `procedure GlobalChatSendMsg(MsgText: String);`

### Parameters

- `MsgText` — Text/String value (String); pass literal text as a quoted BASIC string.

### Accepted values / constants

- `MsgText` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.GlobalChatSendMsg(1000)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.GlobalChatSendMsg(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # MsgText
    UO.GlobalChatSendMsg(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # MsgText
    UO.GlobalChatSendMsg(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
