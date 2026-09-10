# UO.UOSay

ClassicUO • Runtime API • `UO.UOSay.md`

## Точный синтаксис / Registered signatures

```text
UO.UOSay(Text:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UOSay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет речевое сообщение от персонажа в игровой мир (видимое находящимся поблизости игрокам). Text — текст сообщения. Персонаж должен находиться в игровом мире (после экрана логина). Если персонаж ещё не в игровом мире, логируется отладочное сообщение и вызов игнорируется. Использует цвет речи по умолчанию ( 0 ). Для задания пользовательского цвета используйте UOSayColor . Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.UOSay(Text:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UOSay"]`

**Pascal compatibility signature:** `procedure UOSay(Text: String);`

### Parameters

- `Text` — Text/String value (String); pass literal text as a quoted BASIC string.

### Accepted values / constants

- `Text` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.UOSay('example text')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.UOSay('example')
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 'example' # Text
    UO.UOSay(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'example' # Text
    UO.UOSay(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
