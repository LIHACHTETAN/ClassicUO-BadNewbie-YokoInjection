# UO.FindTypeEx

ClassicUO • Runtime API • `UO.FindTypeEx.md`

## Точный синтаксис / Registered signatures

```text
UO.FindTypeEx(ObjType:Any, Color:Any, Container:Any, InSub:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FindTypeEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Ищет объекты с указанным типом ObjType и цветом Color в заданном контейнере Container . ObjType — graphic (тип) искомого объекта. $FFFF (65535) — любой тип. Color — цвет объекта. $FFFF (65535) — любой цвет. Container — где искать: Backpack (рюкзак), Ground / $FFFFFFFF (земля в радиусе FindDistance / FindVertical ), или ID конкретного контейнера. InSub — True для рекурсивного поиска по вложенным контейнерам. Возвращает ID последнего найденного объекта, или 0 если ничего не найдено или персонаж не подключён. Радиус поиска задаётся FindDistance (по горизонтали, макс. 90) и FindVertical (по вертикали, макс. 120). После успешного поиска обновляются: FindItem , FindCount , FindFullQuantity , FindQuantity , GetFindedList . Объекты, добавленные в список игнорирования через Ignore , исключаются из результатов.

### Current Basic signatures / Return

- `UO.FindTypeEx(ObjType:Integer, Color:Integer, Container:Integer, InSub:Boolean) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["FindTypeEx"]` → `BRIDGE CONTRACT -> IApiBridge.FindType`

**Pascal compatibility signature:** `function FindTypeEx(ObjType: Word; Color: Word; Container: Cardinal; InSub: Boolean): Cardinal;`

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `Container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `InSub` — Boolean value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `ObjType` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `Color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `Container` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
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
    VAR result = UO.FindTypeEx(0x0190, -1, backpack, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.FindTypeEx(1, -1, backpack, 4)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # ObjType
    VAR arg2 = -1 # Color
    VAR arg3 = backpack # Container
    VAR arg4 = 4 # InSub
    VAR result = UO.FindTypeEx(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ObjType
    VAR arg2 = -1 # Color
    VAR arg3 = backpack # Container
    VAR arg4 = 4 # InSub
    VAR result = UO.FindTypeEx(arg1, arg2, arg3, arg4)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
