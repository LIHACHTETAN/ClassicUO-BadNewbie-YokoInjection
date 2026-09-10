# UO.ConvertIntegerToFlags

ClassicUO • Runtime API • `UO.ConvertIntegerToFlags.md`

## Точный синтаксис / Registered signatures

```text
UO.ConvertIntegerToFlags(Group:Any, Value:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ConvertIntegerToFlags`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Преобразует числовое значение битовой маски во флаги данных тайла. Group определяет тип тайла: 1 для ландшафтных, 2 для статических. Другие значения игнорируются, возвращается пустой результат. Возвращает пустой результат, если файлы UO Data не загружены или Group не равен 1 или 2. В Pascal возвращает TTileDataFlagSet (тип множество). В Python возвращает list[str] со строковыми именами флагов.

### Current Basic signatures / Return

- `UO.ConvertIntegerToFlags(Group:Integer, Value:Integer) -> TileDataFlagSet`
  - **Return type:** `TileDataFlagSet`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ConvertIntegerToFlags"]` → `BRIDGE CONTRACT -> IApiBridge.ConvertTileFlags`

**Pascal compatibility signature:** `function ConvertIntegerToFlags(Group: Byte; Value: Cardinal): TTileDataFlagSet;`

### Parameters

- `Group` — Named runtime value (Integer); use the exact registered/saved name expected by ConvertIntegerToFlags.
- `Value` — Integer value. The concrete accepted domain is command-specific and is stated in Behavior/Notes; do not assume String conversion when the overload is numeric.

### Accepted values / constants

- `Group` — Tile-data group enum: 1=land tile flags, 2=static tile flags; other values return an empty result.
- `Value` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Operates on the active Basic/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.ConvertIntegerToFlags(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ConvertIntegerToFlags(1, 2)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # Group
    VAR arg2 = 2 # Value
    VAR result = UO.ConvertIntegerToFlags(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Group
    VAR arg2 = 2 # Value
    VAR result = UO.ConvertIntegerToFlags(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
