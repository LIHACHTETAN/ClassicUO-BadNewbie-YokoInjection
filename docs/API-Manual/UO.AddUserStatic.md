# UO.AddUserStatic

ClassicUO • Runtime API • `UO.AddUserStatic.md`

## Точный синтаксис / Registered signatures

```text
UO.AddUserStatic(StaticItem:Any, WorldNum:Any) -> Any
UO.AddUserStatic(graphic:Any, x:Any, y:Any, z:Any, hue:Any, map:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.AddUserStatic`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Добавляет пользовательский статик-объект в данные шарда и возвращает его индекс. Индекс может быть использован для удаления через RemoveUserStatic . Пользовательские статики ведут себя точно так же, как обычные статики шарда при расчёте пути и шагов. Это полезно, когда область заблокирована динамическими объектами (например, заборами), о которых pathfinder не знает заранее. Добавив эти объекты как пользовательские статики, pathfinder учтёт их с самого начала. Важно: Пользовательские статики добавляются в данные шарда , а не к конкретному персонажу. Они будут применяться ко всем персонажам, использующим те же файлы шарда. Пользовательские статики не очищаются при отключении. Используйте ClearUserStatics для их удаления. Возвращает -1 при ошибке. В Python метод называется CreateUserStatic + есть синоним AddUserStatic с набором параметров.

### Current Basic signatures / Return

- `UO.AddUserStatic(StaticItem:StaticItem, WorldNum:Facet) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddUserStatic"]` → `STATE -> InjectionApiState.NextUserStaticId` → `STATE -> InjectionApiState.UserStatics` → `BRIDGE CONTRACT -> IApiBridge.GetX` → `BRIDGE CONTRACT -> IApiBridge.GetY` → `BRIDGE CONTRACT -> IApiBridge.GetZ`

**Pascal compatibility signature:** `function AddUserStatic(const StaticItem: TStaticItem; WorldNum: Byte): Integer;`

### Additional current runtime overloads

- `UO.AddUserStatic(graphic:Integer, x:Integer, y:Integer, z:Integer, hue:Integer, map:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `StaticItem` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.
- `graphic` — Graphic/body/tile ID. Use a decimal or 0x-prefixed hexadecimal value; wildcard -1/0xFFFF is valid only for overloads whose behavior documents wildcard matching.
- `x` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `y` — World/client coordinate as an Integer; interpretation (world tile versus screen pixel) is command-specific and documented in Behavior.
- `z` — Signed world Z/elevation or vertical tolerance as an Integer, according to this command's Behavior contract.
- `hue` — Hue/color value. Use decimal or 0x-prefixed hexadecimal; -1 means any/default hue only where the command explicitly supports it.
- `map` — Facet/map index. Standard values are 0=Felucca, 1=Trammel, 2=Ilshenar, 3=Malas, 4=Tokuno, 5=Ter Mur where supported by the shard/client data.

### Accepted values / constants

- `StaticItem` — StaticItem. Only forms documented by this card and the in-client runtime Inspector are accepted.
- `WorldNum` — Standard facet IDs: 0=Felucca, 1=Trammel, 2=Ilshenar, 3=Malas, 4=Tokuno, 5=Ter Mur, subject to shard/client support.
- `graphic` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `x` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `y` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `z` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `hue` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `map` — Standard facet IDs: 0=Felucca, 1=Trammel, 2=Ilshenar, 3=Malas, 4=Tokuno, 5=Ter Mur, subject to shard/client support.

### Defaults / omitted arguments

Registered arities: 2, 6. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.AddUserStatic(self, 0)
END SUB
```

```basic
SUB Main()
    VAR result = UO.AddUserStatic(0, 0, 0, 0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.AddUserStatic(1, 2)
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 6 аргументов

```vb
SUB Main()
    VAR arg1 = 0x0EED # graphic
    VAR arg2 = UO.GetX() # x
    VAR arg3 = UO.GetY() # y
    VAR arg4 = UO.GetZ() # z
    VAR arg5 = -1 # hue
    VAR arg6 = 6 # map
    VAR result = UO.AddUserStatic(arg1, arg2, arg3, arg4, arg5, arg6)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # StaticItem
    VAR arg2 = 2 # WorldNum
    VAR result = UO.AddUserStatic(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # StaticItem
    VAR arg2 = 2 # WorldNum
    VAR result = UO.AddUserStatic(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_14`
