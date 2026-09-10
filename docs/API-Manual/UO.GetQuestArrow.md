# UO.GetQuestArrow

ClassicUO • Runtime API • `UO.GetQuestArrow.md`

## Точный синтаксис / Registered signatures

```text
UO.GetQuestArrow(point:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetQuestArrow`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает информацию о стрелке квеста/сокровища (большая серая стрелка в клиенте). В Pascal возвращает True , если стрелка активна, и заполняет параметр point координатами. Возвращает False , если стрелка не активна или персонаж отключён. В Python возвращает объект Point напрямую; валидность нужно проверять по его полям. Примечание: На некоторых шардах позиция стрелки может не соответствовать реальному расположению сокровища.

### Current Basic signatures / Return

- `UO.GetQuestArrow(point:Point) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Adapted Array [exists, x, y] instead of mutating a Pascal var/out point.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetQuestArrow"]` → `BRIDGE CONTRACT -> IApiBridge.GetQuestArrow`

**Pascal compatibility signature:** `function GetQuestArrow(var point: TPoint): Boolean;`

### Parameters

- `point` — Point value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `point` — Point. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Returns the quest-arrow state directly as [exists, x, y]. This is the Basic adaptation of the historical Pascal var/out point.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.GetQuestArrow(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetQuestArrow(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # point
    VAR result = UO.GetQuestArrow(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # point
    VAR result = UO.GetQuestArrow(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
