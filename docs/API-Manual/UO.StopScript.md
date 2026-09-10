# UO.StopScript

ClassicUO • Runtime API • `UO.StopScript.md`

## Точный синтаксис / Registered signatures

```text
UO.StopScript(ScriptIndex:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.StopScript`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет запрос на остановку конкретного скрипта по его индексу. ScriptIndex — индекс скрипта (с нуля) в пуле скриптов. Остановка выполняется асинхронно через очередь событий персонажа. Используйте GetScriptsCount (Python: GetScriptCount ) и GetScriptsList для определения индекса целевого скрипта.

### Current Basic signatures / Return

- `UO.StopScript(ScriptIndex:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StopScript"]` → `BRIDGE CONTRACT -> IApiBridge.StopScript`

**Pascal compatibility signature:** `procedure StopScript(ScriptIndex: Word);`

### Parameters

- `ScriptIndex` — Integer control/count/index value (runtime value); exact zero/sentinel meaning is documented by this command.

### Accepted values / constants

- `ScriptIndex` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Operates on the active Basic/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.StopScript(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.StopScript(0)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 0 # ScriptIndex
    UO.StopScript(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 0 # ScriptIndex
    UO.StopScript(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
