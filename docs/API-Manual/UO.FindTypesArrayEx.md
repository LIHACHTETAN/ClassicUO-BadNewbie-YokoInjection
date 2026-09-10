# UO.FindTypesArrayEx

ClassicUO • Runtime API • `UO.FindTypesArrayEx.md`

## Точный синтаксис / Registered signatures

```text
UO.FindTypesArrayEx(ObjTypes:Any, Colors:Any, Containers:Any, InSub:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindTypesArrayEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Ищет объекты, соответствующие любой комбинации из массивов типов ObjTypes , цветов Colors и контейнеров Containers . Внутри метод перебирает каждую комбинацию тип/цвет/контейнер и выполняет простой поиск для каждой. Все результаты агрегируются.

### Current Basic signatures / Return

- `UO.FindTypesArrayEx(ObjTypes:Array, Colors:Array, Containers:Array, InSub:Boolean) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindTypesArrayEx"]` → `BRIDGE CONTRACT -> IApiBridge.FindTypes`

**Pascal compatibility signature:** `function FindTypesArrayEx(ObjTypes: array of Word; Colors: array of Word; Containers: array of Cardinal; InSub: Boolean): Cardinal;`

### Parameters

- `ObjTypes` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Colors` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `Containers` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `InSub` — Boolean value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `ObjTypes` — Runtime Array/list value with element type/shape described by Behavior.
- `Colors` — Runtime Array/list value with element type/shape described by Behavior.
- `Containers` — Runtime Array/list value with element type/shape described by Behavior.
- `InSub` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.FindTypesArrayEx(0x0190, -1, backpack, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    DIM sampleArray(2)
    sampleArray[0] = 1
    sampleArray[1] = 2
    VAR result = UO.FindTypesArrayEx(1, sampleArray, 3, 4)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    DIM sampleArray(2)
    sampleArray[0] = 1
    sampleArray[1] = 2
    VAR arg1 = 1 # ObjTypes
    VAR arg2 = sampleArray # Colors
    VAR arg3 = 3 # Containers
    VAR arg4 = 4 # InSub
    VAR result = UO.FindTypesArrayEx(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    DIM sampleArray(2)
    sampleArray[0] = 1
    sampleArray[1] = 2
    VAR arg1 = 1 # ObjTypes
    VAR arg2 = sampleArray # Colors
    VAR arg3 = 3 # Containers
    VAR arg4 = 4 # InSub
    VAR result = UO.FindTypesArrayEx(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
