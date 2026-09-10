# UO.ReadStaticsXY

ClassicUO • Runtime API • `UO.ReadStaticsXY.md`

## Точный синтаксис / Registered signatures

```text
UO.ReadStaticsXY(X:Any, Y:Any, WorldNum:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ReadStaticsXY`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает все статические объекты в указанных мировых координатах в виде записи TStaticCell . X , Y — координаты тайла на карте. WorldNum — номер мира (фасета): 0 = Felucca, 1 = Trammel, 2 = Ilshenar, 3 = Malas, 4 = Tokuno, 5 = Ter Mur. Возвращаемый TStaticCell содержит массив Statics из записей TStaticItem и поле StaticCount . Каждая запись включает graphic тайла, абсолютные координаты X/Y, высоту Z и цвет статического объекта. Возвращает пустую запись (StaticCount = 0), если статика в данной позиции нет или персонаж не подключён. В Python метод возвращает список объектов StaticItemRealXY (словари с целочисленными значениями). В отличие от GetStaticTilesArray , которая ищет в прямоугольной области и возвращает TFoundTile (без цвета), ReadStaticsXY возвращает данные для одной позиции тайла с полной информацией, включая цвет.

### Current Basic signatures / Return

- `UO.ReadStaticsXY(X:Integer, Y:Integer, WorldNum:Integer) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ReadStaticsXY"]` → `BRIDGE CONTRACT -> IApiBridge.GetStaticTiles`

**Pascal compatibility signature:** `function ReadStaticsXY(X: Word; Y: Word; WorldNum: Byte): TStaticCell;`

### Parameters

- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.

### Accepted values / constants

- `X` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Y` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `WorldNum` — Standard facet IDs: 0=Felucca, 1=Trammel, 2=Ilshenar, 3=Malas, 4=Tokuno, 5=Ter Mur, subject to shard/client support.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.ReadStaticsXY(UO.GetX(self), UO.GetY(self), 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ReadStaticsXY(UO.GetX(), UO.GetY(), 3)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = UO.GetX() # X
    VAR arg2 = UO.GetY() # Y
    VAR arg3 = 3 # WorldNum
    VAR result = UO.ReadStaticsXY(arg1, arg2, arg3)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = UO.GetX() # X
    VAR arg2 = UO.GetY() # Y
    VAR arg3 = 3 # WorldNum
    VAR result = UO.ReadStaticsXY(arg1, arg2, arg3)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
