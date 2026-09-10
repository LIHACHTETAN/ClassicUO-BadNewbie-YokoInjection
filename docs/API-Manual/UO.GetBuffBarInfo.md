# UO.GetBuffBarInfo

ClassicUO • Runtime API • `UO.GetBuffBarInfo.md`

## Точный синтаксис / Registered signatures

```text
UO.GetBuffBarInfo() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetBuffBarInfo`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает список активных баффов и дебаффов персонажа. В Pascal возвращает TBuffBarInfo — запись с Count и массивом Buffs . В Python возвращает list[BuffBarInfo] . Если персонаж не подключён, возвращает запись с Count = 0 (Pascal) или пустой список (Python). Примечание: Поле Seconds в каждой записи баффа содержит длительность на момент применения , а не оставшееся время.

### Current Basic signatures / Return

- `UO.GetBuffBarInfo() -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetBuffBarInfo"]` → `BRIDGE CONTRACT -> IApiBridge.GetBuffBarInfo`

**Pascal compatibility signature:** `function GetBuffBarInfo: TBuffBarInfo;`

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
    VAR result = UO.GetBuffBarInfo()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetBuffBarInfo()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.GetBuffBarInfo()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.GetBuffBarInfo()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
