# UO.PartyPrivateMessageTo

ClassicUO • Runtime API • `UO.PartyPrivateMessageTo.md`

## Точный синтаксис / Registered signatures

```text
UO.PartyPrivateMessageTo(ObjID:Any, Msg:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.PartyPrivateMessageTo`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет личное сообщение конкретному члену пати. ObjID — серийный номер (ID) члена пати для отправки сообщения. Msg — текст сообщения.

### Current Basic signatures / Return

- `UO.PartyPrivateMessageTo(ObjID:Integer, Msg:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PartyPrivateMessageTo"]` → `BRIDGE CONTRACT -> IApiBridge.PartySay`

**Pascal compatibility signature:** `procedure PartyPrivateMessageTo(ObjID: Cardinal; Msg: String);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Msg` — Text value (runtime value); pass it as a quoted BASIC string.

### Accepted values / constants

- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `Msg` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.PartyPrivateMessageTo(self, 1000)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.PartyPrivateMessageTo(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # ObjID
    VAR arg2 = 2 # Msg
    UO.PartyPrivateMessageTo(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ObjID
    VAR arg2 = 2 # Msg
    UO.PartyPrivateMessageTo(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
