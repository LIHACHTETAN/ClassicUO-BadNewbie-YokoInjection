# UO.RenameMobile

ClassicUO • Runtime API • `UO.RenameMobile.md`

## Точный синтаксис / Registered signatures

```text
UO.RenameMobile(MobID:Any, NewName:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.RenameMobile`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос на переименование указанного мобайла. MobID — serial (ID) мобайла для переименования. NewName — новое имя. Переименование возможно только для мобайлов, для которых сервер разрешает переименование (обычно — собственные питомцы игрока). Сервер молча отклонит запрос, если мобайл не может быть переименован. Используйте MobileCanBeRenamed для предварительной проверки. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.RenameMobile(MobID:Integer, NewName:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RenameMobile"]` → `BRIDGE CONTRACT -> IApiBridge.RenameMobile`

**Pascal compatibility signature:** `procedure RenameMobile(MobID: Cardinal; NewName: String);`

### Parameters

- `MobID` — Numeric identifier (Integer). Use the ID domain documented by this command; 0 is a sentinel only when Behavior/Notes explicitly says so.
- `NewName` — Text/String value (String); pass literal text as a quoted BASIC string.

### Accepted values / constants

- `MobID` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `NewName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.RenameMobile(self, 'example')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.RenameMobile(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # MobID
    VAR arg2 = 2 # NewName
    UO.RenameMobile(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # MobID
    VAR arg2 = 2 # NewName
    UO.RenameMobile(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
