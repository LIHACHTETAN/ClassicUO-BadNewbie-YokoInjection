# UO.FindAtCoord

ClassicUO • Runtime API • `UO.FindAtCoord.md`

## Точный синтаксис / Registered signatures

```text
UO.FindAtCoord(X:Any, Y:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindAtCoord`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Ищет все объекты в указанных мировых координатах ( X , Y ) и возвращает ID последнего найденного объекта. Возвращает 0 , если ничего не найдено или персонаж не подключён. После успешного поиска обновляются FindCount , FindItem и GetFindedList .

### Current Basic signatures / Return

- `UO.FindAtCoord(X:Integer, Y:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindAtCoord"]` → `BRIDGE CONTRACT -> IApiBridge.FindAtCoord`

**Pascal compatibility signature:** `function FindAtCoord(X: Word; Y: Word): Cardinal;`

### Parameters

- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.

### Accepted values / constants

- `X` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Y` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.FindAtCoord(UO.GetX(self), UO.GetY(self))
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.FindAtCoord(UO.GetX(), UO.GetY())
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = UO.GetX() # X
    VAR arg2 = UO.GetY() # Y
    VAR result = UO.FindAtCoord(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = UO.GetX() # X
    VAR arg2 = UO.GetY() # Y
    VAR result = UO.FindAtCoord(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
