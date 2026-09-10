# UO.GetWalkUnmountTimer

ClassicUO • Runtime API • `UO.GetWalkUnmountTimer.md`

## Точный синтаксис / Registered signatures

```text
UO.GetWalkUnmountTimer() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetWalkUnmountTimer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает текущую задержку ходьбы (в миллисекундах), используемую, когда персонаж идёт пешком. Этот таймер управляет интервалом между шагами при ходьбе без маунта. Значение можно изменить с помощью SetWalkUnmountTimer .

### Current Basic signatures / Return

- `UO.GetWalkUnmountTimer() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetWalkUnmountTimer"]` → `STATE -> InjectionApiState.WalkUnmountTimer`

**Pascal compatibility signature:** `function GetWalkUnmountTimer: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.GetWalkUnmountTimer()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetWalkUnmountTimer()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.GetWalkUnmountTimer()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.GetWalkUnmountTimer()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
