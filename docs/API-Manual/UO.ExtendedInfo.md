# UO.ExtendedInfo

ClassicUO • Runtime API • `UO.ExtendedInfo.md`

## Точный синтаксис / Registered signatures

```text
UO.ExtendedInfo() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ExtendedInfo`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает расширенную информацию о персонаже в виде записи TExtendedInfo . Данные доступны только для серверов эры SE+ (Samurai Empire и выше), отправляющих расширенную статистику. В Python метод называется GetExtInfo .

### Current Basic signatures / Return

- `UO.ExtendedInfo() -> ExtendedInfo`
  - **Return type:** `ExtendedInfo`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ExtendedInfo"]` → `BRIDGE CONTRACT -> IApiBridge.ClientPath` → `BRIDGE CONTRACT -> IApiBridge.CurrentProfilePath` → `BRIDGE CONTRACT -> IApiBridge.GameServerAddress` → `BRIDGE CONTRACT -> IApiBridge.GameServerPort`

**Pascal compatibility signature:** `function ExtendedInfo: TExtendedInfo;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.ExtendedInfo()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ExtendedInfo()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.ExtendedInfo()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.ExtendedInfo()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
