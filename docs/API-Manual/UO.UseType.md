# UO.UseType

ClassicUO • Runtime API • `UO.UseType.md`

## Точный синтаксис / Registered signatures

```text
UO.UseType(ObjType:Any, Color:Any) -> Any
UO.UseType(type:Any, color:Any, container:Any) -> Integer
UO.UseType(type:Any, color:Any, container:Any, distance:Any) -> Integer
UO.UseType(type:Any, color:Any, container:Any, distance:Any, nearest:Any) -> Integer
UO.UseType(type:Any, color:Any, container:Any, distance:Any, nearest:Any, maxZ:Any) -> Integer
UO.UseType(type:Integer) -> Integer
UO.UseType(type:Integer, color:Integer) -> Integer
UO.UseType(type:Integer, color:String) -> Integer
UO.UseType(type:String) -> Integer
UO.UseType(type:String, color:Integer) -> Integer
UO.UseType(type:String, color:String) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UseType`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Ищет объект указанного типа и цвета на персонаже (сначала слои экипировки, затем рюкзак), затем использует (double-click) его. ObjType — graphic (тип) объекта. $FFFF — любой тип. Color — цвет объекта. $FFFF — любой цвет. Возвращает serial (ID) найденного и использованного объекта, или 0 если подходящий объект не найден. Порядок поиска: Слои экипировки персонажа (кроме самого рюкзака). Рюкзак (рекурсивно). Если объект найден в слоях и его ID совпадает с ID рюкзака, он пропускается, чтобы избежать случайного открытия рюкзака. Логирует ошибку, если подходящий объект не найден.

### Current Basic signatures / Return

- `UO.UseType(ObjType:String, Color:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseType"]` → `BRIDGE CONTRACT -> IApiBridge.UseType`

**Pascal compatibility signature:** `function UseType(ObjType: Word; Color: Word): Cardinal;`

### Additional current runtime overloads

- `UO.UseType(type:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
- `UO.UseType(type:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `type` — Graphic/body/tile ID. Use a decimal or 0x-prefixed hexadecimal value; wildcard -1/0xFFFF is valid only for overloads whose behavior documents wildcard matching.

### Accepted values / constants

- `ObjType` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `Color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `type` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.

### Defaults / omitted arguments

Registered arities: 1, 2. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.UseType(0x0190, -1)
END SUB
```

```basic
SUB Main()
    VAR result = UO.UseType(0)
END SUB
```

```basic
SUB Main()
    VAR result = UO.UseType(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.UseType(0x0EED)
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 6 аргументов

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR arg2 = -1 # color
    VAR arg3 = backpack # container
    VAR arg4 = 5 # distance
    VAR arg5 = 1 # nearest
    VAR arg6 = 6 # maxZ
    VAR result = UO.UseType(arg1, arg2, arg3, arg4, arg5, arg6)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.UseType(0x0EED, -1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.UseType(0x0EED, -1, backpack)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.UseType(0x0EED, -1, backpack, 5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    VAR result = UO.UseType(0x0EED, -1, backpack, 5, 1)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR result = UO.UseType(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 0x0EED # type
    VAR result = UO.UseType(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_18`
- `InjectionScript.Runtime.InjectionApiUO.UseType`
