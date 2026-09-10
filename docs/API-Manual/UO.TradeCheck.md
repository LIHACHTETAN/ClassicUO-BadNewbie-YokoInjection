# UO.TradeCheck

ClassicUO • Runtime API • `UO.TradeCheck.md`

## Точный синтаксис / Registered signatures

```text
UO.TradeCheck(TradeNum:Any, Num:Any) -> Any
UO.TradeCheck(windowIndex:Any) -> Integer
UO.TradeCheck(windowIndex:Any, checkbox:Any, stateValue:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.TradeCheck`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает состояние «галочки» (принятия) участника окна безопасной торговли. TradeNum — индекс окна торговли (используйте TradeCount для получения числа активных торговых окон). Num — какого участника проверять: 1 = свой (ваша сторона), 2 = сторона оппонента. Значение 0 или больше 2 — невалидны, возвращается False . Возвращает True , если указанный участник отметил (принял) торговлю, False — в противном случае или при ошибке. Возвращает False , если персонаж не подключён.

### Current Basic signatures / Return

- `UO.TradeCheck(TradeNum:Integer, Num:Integer) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TradeCheck"]` → `BRIDGE CONTRACT -> IApiBridge.TradeCheck`

**Pascal compatibility signature:** `function TradeCheck(TradeNum: Byte; Num: Byte): Boolean;`

### Additional current runtime overloads

- `UO.TradeCheck(windowIndex:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.TradeCheck(windowIndex:Integer, checkbox:Boolean, stateValue:Boolean) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `TradeNum` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by Behavior/Notes.
- `Num` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by Behavior/Notes.
- `windowIndex` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by this command.
- `checkbox` — Boolean-like value: TRUE/1 enables the option and FALSE/0 disables it unless Behavior documents another numeric mode.
- `stateValue` — Boolean-like value: TRUE/1 enables the option and FALSE/0 disables it unless Behavior documents another numeric mode.

### Accepted values / constants

- `TradeNum` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Num` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `windowIndex` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `checkbox` — TRUE/FALSE or 1/0.
- `stateValue` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

Registered arities: 1, 2, 3. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.TradeCheck(0, 0)
END SUB
```

```basic
SUB Main()
    VAR result = UO.TradeCheck(0)
END SUB
```

```basic
SUB Main()
    VAR result = UO.TradeCheck(0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.TradeCheck(0)
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = 0 # windowIndex
    VAR arg2 = 2 # checkbox
    VAR arg3 = 3 # stateValue
    VAR result = UO.TradeCheck(arg1, arg2, arg3)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.TradeCheck(1, 2)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 0 # windowIndex
    VAR result = UO.TradeCheck(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 0 # windowIndex
    VAR result = UO.TradeCheck(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.TradeCheck`
