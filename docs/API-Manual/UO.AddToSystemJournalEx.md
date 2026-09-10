# UO.AddToSystemJournalEx

ClassicUO • Runtime API • `UO.AddToSystemJournalEx.md`

## Точный синтаксис / Registered signatures

```text
UO.AddToSystemJournalEx(Text:Any, TextColor:Any, BGColor:Any, FontSize:Any, FontName:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.AddToSystemJournalEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Записывает форматированное сообщение в системный журнал Stealth (панель System Journal в нижней части главного окна Stealth). Поддерживает escape-последовательность \n (linebreak) для переноса строки. Можно настроить: TextColor — цвет текста в виде целочисленного RGB-значения. 0 = чёрный (по умолчанию) BGColor — цвет фона в виде целочисленного RGB-значения. -1 = фон по умолчанию FontSize — размер шрифта в пунктах. 10 = по умолчанию FontName — имя семейства шрифта. 'Consolas' = по умолчанию

### Current Basic signatures / Return

- `UO.AddToSystemJournalEx(Text:String, TextColor:Integer, BGColor:Integer, FontSize:Integer, FontName:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddToSystemJournalEx"]` → `BRIDGE CONTRACT -> IApiBridge.PrintFormattedJournal`

**Pascal compatibility signature:** `procedure AddToSystemJournalEx(Text: String; TextColor: Integer; BGColor: Integer; FontSize: Integer; FontName: String);`

### Parameters

- `Text` — Text/String value (String); pass literal text as a quoted BASIC string.
- `TextColor` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `BGColor` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `FontSize` — Font identifier/name. Exact support depends on the client UI route documented for the command.
- `FontName` — Named runtime value (String); use the exact registered/saved name expected by AddToSystemJournalEx.

### Accepted values / constants

- `Text` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `TextColor` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `BGColor` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `FontSize` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `FontName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.AddToSystemJournalEx('example text', -1, -1, 0, 'example')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.AddToSystemJournalEx('example', 2, 3, 4, 5)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 'example' # Text
    VAR arg2 = 2 # TextColor
    VAR arg3 = 3 # BGColor
    VAR arg4 = 4 # FontSize
    VAR arg5 = 5 # FontName
    UO.AddToSystemJournalEx(arg1, arg2, arg3, arg4, arg5)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'example' # Text
    VAR arg2 = 2 # TextColor
    VAR arg3 = 3 # BGColor
    VAR arg4 = 4 # FontSize
    VAR arg5 = 5 # FontName
    UO.AddToSystemJournalEx(arg1, arg2, arg3, arg4, arg5)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
