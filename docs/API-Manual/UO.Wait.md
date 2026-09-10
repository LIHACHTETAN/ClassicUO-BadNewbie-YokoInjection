# UO.Wait

ClassicUO • Runtime API • `UO.Wait.md`

## Точный синтаксис / Registered signatures

```text
UO.Wait(WaitTimeMS:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Wait`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Приостанавливает выполнение скрипта на указанное время. WaitTimeMS — задержка в миллисекундах. Значение 0 возвращает управление немедленно. Внутренне использует интервалы опроса 20 мс и обрабатывает события скрипта (обратные вызовы обработчиков событий) во время ожидания. Скрипт остаётся реактивным к событиям во время паузы. Также учитывается состояние приостановки скрипта — если скрипт приостановлен (например, при отключении с SetPauseScriptOnDisconnectStatus ), ожидание начала задержки происходит после снятия паузы. Sleep — алиас для этого метода.

### Current Basic signatures / Return

- `UO.Wait(WaitTimeMS:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Wait"]` → `BRIDGE CONTRACT -> IApiBridge.Wait`

**Pascal compatibility signature:** `procedure Wait(WaitTimeMS: Cardinal);`

### Parameters

- `WaitTimeMS` — Integer value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `WaitTimeMS` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.Wait(1000)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.Wait(1000)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1000 # WaitTimeMS
    UO.Wait(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1000 # WaitTimeMS
    UO.Wait(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
