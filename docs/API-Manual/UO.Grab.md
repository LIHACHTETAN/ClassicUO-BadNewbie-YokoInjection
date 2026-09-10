# UO.Grab

ClassicUO • Runtime API • `UO.Grab.md`

## Точный синтаксис / Registered signatures

```text
UO.Grab() -> Integer
UO.Grab(Count:Any, ObjID:Any) -> Any
UO.Grab(amount:Any, item:Any, container:Any) -> Integer
UO.Grab(amount:Any, item:Any, container:Any, timeout:Any) -> Integer
UO.Grab(amount:Integer, id:Integer) -> Integer
UO.Grab(amount:Integer, id:String) -> Integer
UO.Grab(amount:String, id:String) -> Integer
UO.Grab(id:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Grab`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Подбирает указанный предмет и перемещает его в рюкзак через маршрут Basic/ClassicUO Grab. Порядок аргументов Basic: сначала Count, затем ObjID. Count — количество предметов из стопки (0 означает всю стопку), ObjID — serial предмета либо сохранённое имя объекта. Возвращает True/1, когда запрос перемещения принят, иначе False/0.

### Current Basic signatures / Return

- `UO.Grab(Count:Integer, ObjID:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Grab"]` → `BRIDGE CONTRACT -> IApiBridge.Grab`

**Pascal compatibility signature:** `function Grab(Count: Integer; ObjID: Cardinal): Boolean;`

### Additional current runtime overloads

- `UO.Grab() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.Grab(id:ObjectRef) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `Count` — Quantity/count. 0 may mean all/default only where explicitly supported.
- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `id` — Object/mobile serial or a supported Basic object reference such as self/backpack/lasttarget/saved object name; hexadecimal and decimal serials are accepted by Variant overloads.

### Accepted values / constants

- `Count` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `id` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

Registered arities: 0, 1, 2. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.Grab(1, self)
END SUB
```

```basic
SUB Main()
    VAR result = UO.Grab()
END SUB
```

```basic
SUB Main()
    VAR result = UO.Grab(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.Grab()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 4 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # amount
    VAR arg2 = self # item
    VAR arg3 = backpack # container
    VAR arg4 = 1000 # timeout
    VAR result = UO.Grab(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 1 аргументов

```vb
SUB Main()
    VAR result = UO.Grab(self)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.Grab(1, self)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.Grab(1, self, backpack)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.Grab()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.Grab()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_20`
- `InjectionScript.Runtime.InjectionApiUO.Grab`
