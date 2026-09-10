# UO.FindNotoriety

ClassicUO • Runtime API • `UO.FindNotoriety.md`

## Точный синтаксис / Registered signatures

```text
UO.FindNotoriety(type:Any, notoriety:Any) -> Any
UO.FindNotoriety(type:Any, notoriety:Any, distance:Any) -> Any
UO.FindNotoriety(type:Any, notoriety:Any, distance:Any, nearest:Any) -> Any
UO.FindNotoriety(type:Any, notoriety:Any, distance:Any, nearest:Any, maxZ:Any) -> Any
UO.FindNotoriety(type:Any, notoriety:Any, distance:Any, nearest:Any, maxZ:Any, color:Any) -> Any
UO.FindNotoriety(type:Any, notoriety:Any, distance:Any, nearest:Any, maxZ:Any, color:Any, container:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindNotoriety`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Ищет mobile с указанными body/graphic ObjType и статусом Notoriety на земле. Это не гарантированный поиск только игроков: mobile может быть персонажем игрока либо NPC, а универсального отличия на всех шардах нет. ObjType = 0xFFFF означает любой тип. Notoriety: 1 Innocent/синий, 2 Ally/зелёный, 3 Attackable/серый, 4 Criminal/серый, 5 Enemy/оранжевый, 6 Murderer/красный, 7 Invulnerable/жёлтый. Радиус задают FindDistance и FindVertical. Возвращает ID последнего найденного mobile либо 0. После вызова обновляются FindItem, FindCount и GetFoundItems/GetFindedList.

### Current Basic runtime signatures / Return

- `UO.FindNotoriety(type:Integer, notoriety:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindNotoriety"]` → `BRIDGE CONTRACT -> IApiBridge.FindNotoriety`
- `UO.FindNotoriety(type:GraphicId, notoriety:Variant, distance:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
- `UO.FindNotoriety(type:GraphicId, notoriety:Variant, distance:Integer, nearest:Boolean) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
- `UO.FindNotoriety(type:GraphicId, notoriety:Variant, distance:Integer, nearest:Boolean, maxZ:Variant) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
- `UO.FindNotoriety(type:GraphicId, notoriety:Variant, distance:Integer, nearest:Boolean, maxZ:Variant, color:Hue) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.
- `UO.FindNotoriety(type:GraphicId, notoriety:Variant, distance:Integer, nearest:Boolean, maxZ:Variant, color:Hue, container:ObjectRef) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Mobile/object serial; 0 means no matching mobile.

### Historical compatibility reference

- Pascal: `function FindNotoriety(ObjType: Word; Notoriety: Byte): Cardinal;`
- Historical Basic/Stealth syntax: `UO.FindNotoriety(ObjType, Notoriety)`

### Parameters

- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `notoriety` — Actual ClassicUO Mobile.Notoriety value or supported mask/string form; it is not inferred from hue/name/body.
- `distance` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.
- `nearest` — Boolean ordering flag. TRUE selects/orders nearest matches first; FALSE preserves the runtime search order.
- `maxZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.

### Accepted values / constants

- `type` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `notoriety` — 0=unknown, 1=innocent/blue, 2=ally/green, 3=attackable/grey, 4=criminal/grey, 5=enemy/orange, 6=murderer/red, 7=invulnerable/yellow.
- `distance` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `nearest` — TRUE/FALSE or 1/0.
- `maxZ` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.
- `color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `container` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

Registered arities: 2, 3, 4, 5, 6, 7. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Scans loaded World.Mobiles using the real Mobile.Notoriety field, body/type, distance/Z and Ignore rules. The registered result uses first-match semantics unless nearest ordering is requested.

### Notes / limitations

Uses real notoriety values; do not treat hue, body or name as substitutes. 0 means no matching mobile.

### Examples

```basic
SUB Main()
    VAR result = UO.FindNotoriety(0x0190, 5)
END SUB
```

```basic
SUB Main()
    VAR result = UO.FindNotoriety(0x0190, 5, 18, TRUE, 12, -1, backpack)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.FindNotoriety(0x0EED, -1)
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 7 аргументов

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR arg2 = -1 # notoriety
    VAR arg3 = 5 # distance
    VAR arg4 = 1 # nearest
    VAR arg5 = 5 # maxZ
    VAR arg6 = -1 # color
    VAR arg7 = backpack # container
    VAR result = UO.FindNotoriety(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.FindNotoriety(0x0EED, -1, 5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.FindNotoriety(0x0EED, -1, 5, 1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    VAR result = UO.FindNotoriety(0x0EED, -1, 5, 1, 5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 6 аргументов

```vb
SUB Main()
    VAR result = UO.FindNotoriety(0x0EED, -1, 5, 1, 5, -1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR arg2 = -1 # notoriety
    VAR result = UO.FindNotoriety(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 0x0EED # type
    VAR arg2 = -1 # notoriety
    VAR result = UO.FindNotoriety(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<RegisterCompactSearchApi>b__351_0`
