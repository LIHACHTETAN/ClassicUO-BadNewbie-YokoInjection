# UO.UseVirtue

ClassicUO • Runtime API • `UO.UseVirtue.md`

## Точный синтаксис / Registered signatures

```text
UO.UseVirtue(VirtueName:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UseVirtue`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Активирует указанную добродетель. VirtueName (Pascal) — имя добродетели строкой (например, 'Honor' , 'Valor' , 'Compassion' ). Если имя не распознано, логируется ошибка. VirtueID (Python) — индекс добродетели целым числом. Также принимает значения перечисления Virtue . Обратите внимание на различие: Pascal использует имя (String), Python — индекс (int) или перечисление Virtue . На официальных шардах вызывает гамп системы добродетелей.

### Current Basic signatures / Return

- `UO.UseVirtue(VirtueName:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseVirtue"]` → `BRIDGE CONTRACT -> IApiBridge.UseVirtue`

**Pascal compatibility signature:** `procedure UseVirtue(VirtueName: String);`

### Parameters

- `VirtueName` — Named runtime value (Integer); use the exact registered/saved name expected by UseVirtue.

### Accepted values / constants

- `VirtueName` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.UseVirtue('example')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.UseVirtue(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # VirtueName
    VAR result = UO.UseVirtue(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # VirtueName
    VAR result = UO.UseVirtue(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
