# UO.FindDistance

ClassicUO • Runtime API • `UO.FindDistance.md`

## Точный синтаксис / Registered signatures

```text
UO.FindDistance() -> Any
UO.FindDistance(value:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindDistance`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Задаёт горизонтальный радиус поиска (в тайлах) для поиска на земле методами FindType , FindTypeEx , FindTypesArrayEx и связанными. Значение по умолчанию: 2 . Максимальное значение: 90 — значения выше 90 обрезаются. Влияет только на поиск с контейнером Ground ( $FFFFFFFF ). Не влияет на поиск в контейнерах или рюкзаке. В Python используйте GetFindDistance() / SetFindDistance(value) .

### Current Basic signatures / Return

- `UO.FindDistance() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindDistance"]` → `BRIDGE CONTRACT -> IApiBridge.GetFindDistance` → `BRIDGE CONTRACT -> IApiBridge.SetFindDistance`
- `UO.FindDistance(value:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindDistance"]` → `BRIDGE CONTRACT -> IApiBridge.GetFindDistance` → `BRIDGE CONTRACT -> IApiBridge.SetFindDistance`

**Pascal compatibility signature:** `var FindDistance: Cardinal;`

### Parameters

- `value` — Integer value. The concrete accepted domain is command-specific and is stated in Behavior/Notes; do not assume String conversion when the overload is numeric.

### Accepted values / constants

- `value` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

The compatibility search-distance state historically defaults to 2; explicit distance arguments on search overloads override shared state for that call.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.FindDistance()
END SUB
```

```basic
SUB Main()
    UO.FindDistance(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.FindDistance()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # value
    VAR result = UO.FindDistance(arg1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.FindDistance()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.FindDistance()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
