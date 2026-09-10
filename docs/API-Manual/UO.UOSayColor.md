# UO.UOSayColor

ClassicUO • Runtime API • `UO.UOSayColor.md`

## Точный синтаксис / Registered signatures

```text
UO.UOSayColor(Text:Any, Color:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UOSayColor`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет речевое сообщение от персонажа в игровой мир с указанным цветом. Text — текст сообщения. Color — значение UO hue для цвета текста. Персонаж должен находиться в игровом мире. Если нет — логируется отладочное сообщение и вызов игнорируется. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.UOSayColor(Text:String, Color:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UOSayColor"]` → `BRIDGE CONTRACT -> IApiBridge.Say`

**Pascal compatibility signature:** `procedure UOSayColor(Text: String; Color: Word);`

### Parameters

- `Text` — Text/String value (String); pass literal text as a quoted BASIC string.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Accepted values / constants

- `Text` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `Color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.UOSayColor('example text', -1)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.UOSayColor('example', -1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 'example' # Text
    VAR arg2 = -1 # Color
    UO.UOSayColor(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'example' # Text
    VAR arg2 = -1 # Color
    UO.UOSayColor(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
