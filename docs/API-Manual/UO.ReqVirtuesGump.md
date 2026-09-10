# UO.ReqVirtuesGump

ClassicUO • Runtime API • `UO.ReqVirtuesGump.md`

## Точный синтаксис / Registered signatures

```text
UO.ReqVirtuesGump() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ReqVirtuesGump`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос на открытие окна добродетелей (Virtues gump) для текущего персонажа. На официальных шардах дополнительно устанавливается внутренний флаг запроса, который влияет на обработку входящего пакета гампа. Гамп появляется асинхронно — используйте WaitGump или GetGumpsCount для ожидания и взаимодействия с ним.

### Current Basic signatures / Return

- `UO.ReqVirtuesGump() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ReqVirtuesGump"]` → `BRIDGE CONTRACT -> IApiBridge.RequestVirtuesGump`

**Pascal compatibility signature:** `procedure ReqVirtuesGump;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.ReqVirtuesGump()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.ReqVirtuesGump()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.ReqVirtuesGump()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.ReqVirtuesGump()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
