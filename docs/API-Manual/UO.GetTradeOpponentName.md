# UO.GetTradeOpponentName

ClassicUO • Runtime API • `UO.GetTradeOpponentName.md`

## Точный синтаксис / Registered signatures

```text
UO.GetTradeOpponentName(TradeNum:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetTradeOpponentName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает имя оппонента в указанном окне безопасного обмена. TradeNum — индекс активного окна обмена (начиная с 1, как возвращает TradeCount ). Возвращает пустую строку, если окно обмена не существует или персонаж не подключён.

### Current Basic signatures / Return

- `UO.GetTradeOpponentName(TradeNum:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetTradeOpponentName"]` → `BRIDGE CONTRACT -> IApiBridge.GetTradeOpponentName`

**Pascal compatibility signature:** `function GetTradeOpponentName(TradeNum: Byte): String;`

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
    VAR result = UO.GetTradeOpponentName(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetTradeOpponentName(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # TradeNum
    VAR result = UO.GetTradeOpponentName(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # TradeNum
    VAR result = UO.GetTradeOpponentName(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
