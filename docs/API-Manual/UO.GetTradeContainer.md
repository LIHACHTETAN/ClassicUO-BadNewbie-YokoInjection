# UO.GetTradeContainer

ClassicUO • Runtime API • `UO.GetTradeContainer.md`

## Точный синтаксис / Registered signatures

```text
UO.GetTradeContainer(TradeNum:Any, Num:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetTradeContainer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает ID контейнера в указанном окне безопасного обмена. TradeNum — индекс активного окна обмена (начиная с 1, как возвращает TradeCount ). Num — какой контейнер получить: 1 — ваш собственный, 2 — контейнер оппонента. Возвращает 0 , если Num не равен 1 или 2 , окно обмена не существует или персонаж не подключён. Полученный ID контейнера можно передать в GetContent или методы поиска для просмотра предметов внутри.

### Current Basic signatures / Return

- `UO.GetTradeContainer(TradeNum:Integer, Num:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetTradeContainer"]` → `BRIDGE CONTRACT -> IApiBridge.GetTradeContainer`

**Pascal compatibility signature:** `function GetTradeContainer(TradeNum: Byte; Num: Byte): Cardinal;`

### Parameters

- `TradeNum` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by Behavior/Notes.
- `Num` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by Behavior/Notes.

### Accepted values / constants

- `TradeNum` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Num` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.GetTradeContainer(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetTradeContainer(1, 2)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # TradeNum
    VAR arg2 = 2 # Num
    VAR result = UO.GetTradeContainer(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # TradeNum
    VAR arg2 = 2 # Num
    VAR result = UO.GetTradeContainer(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
