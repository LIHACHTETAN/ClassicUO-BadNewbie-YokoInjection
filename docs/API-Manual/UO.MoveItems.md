# UO.MoveItems

ClassicUO • Runtime API • `UO.MoveItems.md`

## Точный синтаксис / Registered signatures

```text
UO.MoveItems(Container:Any, ItemsType:Any, ItemsColor:Any, MoveIntoID:Any, X:Any, Y:Any, Z:Any, DelayMS:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.MoveItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Перемещает все предметы с указанным типом и цветом из контейнера-источника в контейнер-получатель. Container — ID контейнера-источника. ItemsType — графический тип для поиска. $FFFF — любой тип. ItemsColor — цвет для поиска. $FFFF — любой цвет. MoveIntoID — ID контейнера-получателя, или 0 для сброса на землю. X , Y , Z — координаты внутри контейнера-получателя или мировые координаты. 0, 0, 0 для размещения по умолчанию. DelayMS — задержка в миллисекундах между перемещением каждого предмета. В Python дополнительно поддерживается необязательный параметр max_count (по умолчанию 0 = переместить все). Возвращает True , если хотя бы один предмет был перемещён, False — в противном случае.

### Current Basic signatures / Return

- `UO.MoveItems(Container:Integer, ItemsType:Integer, ItemsColor:Integer, MoveIntoID:Integer, X:Integer, Y:Integer, Z:Integer, DelayMS:Integer) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MoveItems"]` → `BRIDGE CONTRACT -> IApiBridge.MoveItems`

**Pascal compatibility signature:** `function MoveItems(Container: Cardinal; ItemsType: Word; ItemsColor: Word; MoveIntoID: Cardinal; X: Integer; Y: Integer; Z: ShortInt; DelayMS: Integer): Boolean;`

### Parameters

- `Container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `ItemsType` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `ItemsColor` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `MoveIntoID` — Container/object destination. Use backpack/ground/self/saved object name or a valid hexadecimal/decimal serial where that overload permits it.
- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `Z` — World/tile Z coordinate.
- `DelayMS` — Delay/timeout in milliseconds; use a non-negative integer (for example 3000 = 3 seconds).

### Accepted values / constants

- `Container` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `ItemsType` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `ItemsColor` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `MoveIntoID` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `X` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Y` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Z` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `DelayMS` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.MoveItems(backpack, 0x0190, -1, self, UO.GetX(self), UO.GetY(self), UO.GetZ(self), 1000)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.MoveItems(backpack, 2, 3, 4, UO.GetX(), UO.GetY(), UO.GetZ(), 100)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = backpack # Container
    VAR arg2 = 2 # ItemsType
    VAR arg3 = 3 # ItemsColor
    VAR arg4 = 4 # MoveIntoID
    VAR arg5 = UO.GetX() # X
    VAR arg6 = UO.GetY() # Y
    VAR arg7 = UO.GetZ() # Z
    VAR arg8 = 100 # DelayMS
    VAR result = UO.MoveItems(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = backpack # Container
    VAR arg2 = 2 # ItemsType
    VAR arg3 = 3 # ItemsColor
    VAR arg4 = 4 # MoveIntoID
    VAR arg5 = UO.GetX() # X
    VAR arg6 = UO.GetY() # Y
    VAR arg7 = UO.GetZ() # Z
    VAR arg8 = 100 # DelayMS
    VAR result = UO.MoveItems(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
