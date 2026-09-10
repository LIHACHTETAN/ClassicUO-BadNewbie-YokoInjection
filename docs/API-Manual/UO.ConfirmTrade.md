# UO.ConfirmTrade

ClassicUO • Runtime API • `UO.ConfirmTrade.md`

## Точный синтаксис / Registered signatures

```text
UO.ConfirmTrade(TradeNum:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ConfirmTrade`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Подтверждает обмен, устанавливая флажок подтверждения для обмена с индексом TradeNum в списке активных обменов.

### Current Basic signatures / Return

- `UO.ConfirmTrade(TradeNum:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ConfirmTrade"]` → `BRIDGE CONTRACT -> IApiBridge.ConfirmTrade`

**Pascal compatibility signature:** `procedure ConfirmTrade(TradeNum: Byte);`

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
    UO.ConfirmTrade(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ConfirmTrade(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # TradeNum
    VAR result = UO.ConfirmTrade(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # TradeNum
    VAR result = UO.ConfirmTrade(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
