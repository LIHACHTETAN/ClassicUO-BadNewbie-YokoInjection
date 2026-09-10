# UO.CancelTrade

ClassicUO • Runtime API • `UO.CancelTrade.md`

## Точный синтаксис / Registered signatures

```text
UO.CancelTrade(TradeNum:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.CancelTrade`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отменяет окно обмена с индексом TradeNum из списка активных обменов. Возвращает True , если обмен успешно отменён, False , если индекс обмена недействителен или такой обмен не существует.

### Current Basic signatures / Return

- `UO.CancelTrade(TradeNum:Integer) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CancelTrade"]` → `BRIDGE CONTRACT -> IApiBridge.CancelTrade`

**Pascal compatibility signature:** `function CancelTrade(TradeNum: Byte): Boolean;`

### Parameters

- `TradeNum` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by Behavior/Notes.

### Accepted values / constants

- `TradeNum` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.CancelTrade(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.CancelTrade(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # TradeNum
    VAR result = UO.CancelTrade(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # TradeNum
    VAR result = UO.CancelTrade(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
