# UO.Dist

ClassicUO • Runtime API • `UO.Dist.md`

## Точный синтаксис / Registered signatures

```text
UO.Dist(Xfrom:Any, Yfrom:Any, Xto:Any, Yto:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Dist`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает расстояние в тайлах между двумя точками ( X1 , Y1 ) и ( X2 , Y2 ). Расстояние вычисляется как Max(|X2-X1|, |Y2-Y1|) (расстояние Чебышёва), что соответствует реальному расстоянию в тайлах в UO.

### Current Basic signatures / Return

- `UO.Dist(Xfrom:Integer, Yfrom:Integer, Xto:Integer, Yto:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Dist"]` → `BRIDGE CONTRACT -> IApiBridge.GetDistance`

**Pascal compatibility signature:** `function Dist(Xfrom: Word; Yfrom: Word; Xto: Word; Yto: Word): Word;`

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
    VAR result = UO.Dist(0, 0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.Dist(1, 2, 3, 4)
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
    VAR result = UO.Dist(arg1, arg2, arg3, arg4)
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
    VAR result = UO.Dist(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
