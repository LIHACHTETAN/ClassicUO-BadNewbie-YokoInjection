# UO.FillNewWindow

ClassicUO • Runtime API • `UO.FillNewWindow.md`

## Точный синтаксис / Registered signatures

```text
UO.FillNewWindow(S:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FillNewWindow`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Добавляет строку в информационное окно Stealth. Содержимое информационного окна можно очистить через ClearInfoWindow . Примечание: Настройка SetSilentMode не влияет на этот метод — строки всегда добавляются независимо от тихого режима.

### Current Basic signatures / Return

- `UO.FillNewWindow(S:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FillNewWindow"]` → `BRIDGE CONTRACT -> IApiBridge.TextClear` → `BRIDGE CONTRACT -> IApiBridge.TextOpen` → `BRIDGE CONTRACT -> IApiBridge.TextPrint`

**Pascal compatibility signature:** `procedure FillNewWindow(S: String);`

### Parameters

- `S` — Text/String value (String); pass literal text as a quoted BASIC string.

### Accepted values / constants

- `S` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.FillNewWindow(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.FillNewWindow(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # S
    UO.FillNewWindow(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # S
    UO.FillNewWindow(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
