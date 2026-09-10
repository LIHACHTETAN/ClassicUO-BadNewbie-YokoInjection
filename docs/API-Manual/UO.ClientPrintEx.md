# UO.ClientPrintEx

ClassicUO • Runtime API • `UO.ClientPrintEx.md`

## Точный синтаксис / Registered signatures

```text
UO.ClientPrintEx(SenderID:Any, Color:Any, Font:Any, Text:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ClientPrintEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Расширенная версия ClientPrint . Отправляет текстовое сообщение подключённому клиенту с настраиваемым форматированием. Сообщение отправляется только клиенту — оно не передаётся на сервер и не видно другим игрокам.

### Current Basic signatures / Return

- `UO.ClientPrintEx(SenderID:Integer, Color:Integer, Font:Integer, Text:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ClientPrintEx"]` → `BRIDGE CONTRACT -> IApiBridge.CharPrintEx`

**Pascal compatibility signature:** `procedure ClientPrintEx(SenderID: Cardinal; Color: Word; Font: Word; Text: String);`

### Parameters

- `SenderID` — Numeric identifier (Integer). Use the ID domain documented by this command; 0 is a sentinel only when Behavior/Notes explicitly says so.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `Font` — Font identifier/name. Exact support depends on the client UI route documented for the command.
- `Text` — Text/String value (String); pass literal text as a quoted BASIC string.

### Accepted values / constants

- `SenderID` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `Font` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Text` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.ClientPrintEx(self, -1, 0, 'example text')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.ClientPrintEx(1, -1, 3, 'example')
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # SenderID
    VAR arg2 = -1 # Color
    VAR arg3 = 3 # Font
    VAR arg4 = 'example' # Text
    UO.ClientPrintEx(arg1, arg2, arg3, arg4)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # SenderID
    VAR arg2 = -1 # Color
    VAR arg3 = 3 # Font
    VAR arg4 = 'example' # Text
    UO.ClientPrintEx(arg1, arg2, arg3, arg4)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
