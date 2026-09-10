# UO.AlwaysRun

ClassicUO • Runtime API • `UO.AlwaysRun.md`

## Точный синтаксис / Registered signatures

```text
UO.AlwaysRun() -> Integer
UO.AlwaysRun(enabled:Integer) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.AlwaysRun`

### Direct runtime overloads

- `UO.AlwaysRun() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.AlwaysRun(enabled:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `enabled` — Boolean-like runtime value: TRUE/1 enables the option and FALSE/0 disables it unless the command documents another numeric mode.

### Accepted values / constants

- `enabled` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

Registered arities: 0, 1. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.AlwaysRun()
END SUB
```

```basic
SUB Main()
    UO.AlwaysRun(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.AlwaysRun()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # enabled
    UO.AlwaysRun(arg1)
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.AlwaysRun()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.AlwaysRun()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.AlwaysRun`
