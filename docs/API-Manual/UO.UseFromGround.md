# UO.UseFromGround

ClassicUO • Runtime API • `UO.UseFromGround.md`

## Точный синтаксис / Registered signatures

```text
UO.UseFromGround(type:Any) -> Integer
UO.UseFromGround(type:Any, color:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UseFromGround`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Ищет объект указанного типа и цвета на земле, затем использует (double-click) его. ObjType — graphic (тип) объекта. $FFFF — любой тип. Color — цвет объекта. $FFFF — любой цвет. Возвращает serial (ID) найденного и использованного объекта, или 0 если подходящий объект на земле не найден. Поиск использует FindTypeEx с Ground в качестве контейнера и InSub = False . Радиус поиска управляется FindDistance и FindVertical . Логирует ошибку в системный журнал, если объект не найден.

### Current Basic signatures / Return

- `UO.UseFromGround(ObjType:GraphicId, Color:Hue) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseFromGround"]` → `BRIDGE CONTRACT -> IApiBridge.FindType` → `BRIDGE CONTRACT -> IApiBridge.UseObject`

**Pascal compatibility signature:** `function UseFromGround(ObjType: Word; Color: Word): Cardinal;`

### Additional current runtime overloads

- `UO.UseFromGround(type:GraphicId) -> Integer`
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

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.UseFromGround(0x0190, -1)
END SUB
```

```basic
SUB Main()
    VAR result = UO.UseFromGround(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.UseFromGround(0x0EED)
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR arg2 = -1 # color
    VAR result = UO.UseFromGround(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR result = UO.UseFromGround(arg1)
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
    VAR result = UO.UseFromGround(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.UseFromGround`
