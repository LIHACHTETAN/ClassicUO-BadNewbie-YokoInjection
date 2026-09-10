# UO.DropDelay

ClassicUO • Runtime API • `UO.DropDelay.md`

## Точный синтаксис / Registered signatures

```text
UO.DropDelay() -> Any
UO.DropDelay(value:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.DropDelay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Задаёт задержку (в миллисекундах) после операций сброса ( Drop , DropHere , DropItem , MoveItem и т.д.). Ограничивается диапазоном 50–10000 мс. В Python используйте GetDropDelay() / SetDropDelay(value) .

### Current Basic signatures / Return

- `UO.DropDelay() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropDelay"]` → `BRIDGE CONTRACT -> IApiBridge.GetDropDelay` → `BRIDGE CONTRACT -> IApiBridge.SetDropDelay`
- `UO.DropDelay(value:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropDelay"]` → `BRIDGE CONTRACT -> IApiBridge.GetDropDelay` → `BRIDGE CONTRACT -> IApiBridge.SetDropDelay`

**Pascal compatibility signature:** `var DropDelay: Integer;`

### Parameters

- `value` — Post-drop delay in milliseconds; clamped to 50..10000 ms.

### Accepted values / constants

- `value` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 0, 1. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.DropDelay()
END SUB
```

```basic
SUB Main()
    UO.DropDelay(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.DropDelay()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # value
    VAR result = UO.DropDelay(arg1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.DropDelay()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.DropDelay()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
