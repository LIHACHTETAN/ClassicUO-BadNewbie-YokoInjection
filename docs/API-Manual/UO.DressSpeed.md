# UO.DressSpeed

ClassicUO • Runtime API • `UO.DressSpeed.md`

## Точный синтаксис / Registered signatures

```text
UO.DressSpeed() -> Any
UO.DressSpeed(value:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.DressSpeed`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Задаёт задержку (в миллисекундах) между отдельными операциями экипировки/снятия в EquipItems , UnequipItems и связанных методах одевания/раздевания. Ограничивается диапазоном 10–10000 мс. В Python используйте GetDressSpeed() / SetDressSpeed(value) .

### Current Basic signatures / Return

- `UO.DressSpeed() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DressSpeed"]` → `STATE -> InjectionApiState.DressSpeed`
- `UO.DressSpeed(value:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DressSpeed"]` → `STATE -> InjectionApiState.DressSpeed`

**Pascal compatibility signature:** `var DressSpeed: Integer;`

### Parameters

- `value` — Dress/undress per-item delay in milliseconds; clamped to 10..10000 ms.

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
    VAR result = UO.DressSpeed()
END SUB
```

```basic
SUB Main()
    UO.DressSpeed(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.DressSpeed()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # value
    VAR result = UO.DressSpeed(arg1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.DressSpeed()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.DressSpeed()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
