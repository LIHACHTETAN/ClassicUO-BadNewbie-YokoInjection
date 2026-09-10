# UO.GetScriptPath

ClassicUO • Runtime API • `UO.GetScriptPath.md`

## Точный синтаксис / Registered signatures

```text
UO.GetScriptPath(ScriptIndex:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetScriptPath`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает полный путь к файлу скрипта с индексом ScriptIndex . Возвращает пустую строку, если скрипт с данным индексом не существует.

### Current Basic signatures / Return

- `UO.GetScriptPath(ScriptIndex:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetScriptPath"]` → `BRIDGE CONTRACT -> IApiBridge.GetScriptPath`

**Pascal compatibility signature:** `function GetScriptPath(ScriptIndex: Word): String;`

### Parameters

- `ScriptIndex` — Integer control/count/index value (runtime value); exact zero/sentinel meaning is documented by this command.

### Accepted values / constants

- `ScriptIndex` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.GetScriptPath(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetScriptPath(0)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 0 # ScriptIndex
    VAR result = UO.GetScriptPath(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 0 # ScriptIndex
    VAR result = UO.GetScriptPath(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
