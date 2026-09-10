# UO.CalcDir

ClassicUO • Runtime API • `UO.CalcDir.md`

## Точный синтаксис / Registered signatures

```text
UO.CalcDir(Xfrom:Any, Yfrom:Any, Xto:Any, Yto:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.CalcDir`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Вычисляет направление для шага из точки ( Xfrom , Yfrom ) в точку ( Xto , Yto ). Возвращает значение направления (0–7, см. таблицу выше). Если обе точки совпадают (Xfrom = Xto и Yfrom = Yto), возвращает 100 .

### Current Basic signatures / Return

- `UO.CalcDir(Xfrom:Integer, Yfrom:Integer, Xto:Integer, Yto:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CalcDir"]`

**Pascal compatibility signature:** `function CalcDir(Xfrom: Word; Yfrom: Word; Xto: Word; Yto: Word): Byte;`

### Parameters

- `Xfrom` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `Yfrom` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `Xto` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `Yto` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.

### Accepted values / constants

- `Xfrom` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Yfrom` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Xto` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Yto` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.CalcDir(0, 0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.CalcDir(1, 2, 3, 4)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # Xfrom
    VAR arg2 = 2 # Yfrom
    VAR arg3 = 3 # Xto
    VAR arg4 = 4 # Yto
    VAR result = UO.CalcDir(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Xfrom
    VAR arg2 = 2 # Yfrom
    VAR arg3 = 3 # Xto
    VAR arg4 = 4 # Yto
    VAR result = UO.CalcDir(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
