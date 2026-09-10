# UO.WaitTextEntry

ClassicUO • Runtime API • `UO.WaitTextEntry.md`

## Точный синтаксис / Registered signatures

```text
UO.WaitTextEntry(Value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.WaitTextEntry`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Ищет текущий ожидающий диалог ввода текста и отвечает на него; если такого нет, устанавливает ловушку на следующий входящий. Value — текст для автоматического ввода. Метод сначала проверяет, есть ли уже ожидающий диалог ввода текста. Если да — текст отправляется немедленно. Если нет — устанавливается ловушка: при получении от сервера диалога ввода текста указанный текст будет отправлен автоматически. Устарел. Этот метод неточен, поскольку отвечает на любой диалог ввода текста без разбора. Для более точного контроля рекомендуется использовать обработчики событий. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.WaitTextEntry(Value:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitTextEntry"]` → `BRIDGE CONTRACT -> IApiBridge.SetGumpValue`

**Pascal compatibility signature:** `procedure WaitTextEntry(Value: String);`

### Parameters

- `Value` — String value. The concrete accepted domain is command-specific and is stated in Behavior/Notes; do not assume String conversion when the overload is numeric.

### Accepted values / constants

- `Value` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.WaitTextEntry('example')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.WaitTextEntry(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Value
    UO.WaitTextEntry(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Value
    UO.WaitTextEntry(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
