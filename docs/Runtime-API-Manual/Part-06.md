# Runtime API Manual — Part 06

Commands: **ConvertIntegerToFlags** through **Dress**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.ConvertIntegerToFlags`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Преобразует числовое значение битовой маски во флаги данных тайла. Group определяет тип тайла: 1 для ландшафтных, 2 для статических. Другие значения игнорируются, возвращается пустой результат. Возвращает пустой результат, если файлы UO Data не загружены или Group не равен 1 или 2. В Pascal возвращает TTileDataFlagSet (тип множество). В Python возвращает list[str] со строковыми именами флагов.

### Current Yoko signatures / Return

- `UO.ConvertIntegerToFlags(Group, Value)`
  - **Return type:** `Array`
  - **Return contract:** Array runtime value. Empty array is a valid no-data/no-match result; check GetArrayLength before indexing.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ConvertIntegerToFlags"]` → `BRIDGE CONTRACT -> IApiBridge.ConvertTileFlags`

**Pascal compatibility signature:** `function ConvertIntegerToFlags(Group: Byte; Value: Cardinal): TTileDataFlagSet;`

### Parameters

- `Group` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Value` — String/text value interpreted according to the command.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ConvertIntegerToFlags(0, 'value')
```

---

## `UO.Count`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет предметы с типом ObjType в рюкзаке персонажа (только верхний уровень, без подконтейнеров) и возвращает общее количество с учётом стеков ( FindFullQuantity ). Удобная обёртка над FindTypeEx с Color = $FFFF , Container = Backpack , InSub = False . Метод сохраняет и восстанавливает текущие поля поиска, поэтому не влияет на текущий поиск через FindType/FindTypeEx.

### Current Yoko signatures / Return

- `UO.Count(ObjType)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.Count"]`

**Pascal compatibility signature:** `function Count(ObjType: Word): Integer;`

### Additional current runtime overloads

- `UO.Count(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.Count(arg1:Any, arg2:Any, arg3:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Count(0x0190)
```

```basic
VAR result = UO.Count(0, 0)
```

```basic
VAR result = UO.Count(0, 0, 0)
```

---

## `UO.CountEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет предметы с типом ObjType и цветом Color в указанном контейнере Container (только верхний уровень, без подконтейнеров) и возвращает общее количество с учётом стеков ( FindFullQuantity ). Используйте $FFFF для ObjType (любой тип) и $FFFF для Color (любой цвет). Метод сохраняет и восстанавливает текущие поля поиска.

### Current Yoko signatures / Return

- `UO.CountEx(ObjType, Color, Container)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CountEx"]` → `BRIDGE CONTRACT -> IApiBridge.FindFullQuantity` → `BRIDGE CONTRACT -> IApiBridge.FindType`

**Pascal compatibility signature:** `function CountEx(ObjType: Word; Color: Word; Container: Cardinal): Integer;`

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `Container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CountEx(0x0190, -1, backpack)
```

---

## `UO.CountGround`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет предметы с типом ObjType на земле и возвращает общее количество с учётом стеков ( FindFullQuantity ). Радиус поиска ограничен FindDistance (по горизонтали) и FindVertical (по вертикали). Метод сохраняет и восстанавливает текущие поля поиска.

### Current Yoko signatures / Return

- `UO.CountGround(ObjType)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.CountGround"]`

**Pascal compatibility signature:** `function CountGround(ObjType: Word): Integer;`

### Additional current runtime overloads

- `UO.CountGround(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.CountGround(0x0190)
```

```basic
VAR result = UO.CountGround(0, 0)
```

---

## `UO.Date`

### Direct runtime overloads

- `UO.Date() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Date()
```

---

## `UO.Dead`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если персонаж мёртв, False в противном случае. Возвращает False , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Dead()`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.Dead"]`

**Pascal compatibility signature:** `function Dead: Boolean;`

### Additional current runtime overloads

- `UO.Dead(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.Dead(serial:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Dead()
```

```basic
VAR result = UO.Dead(0)
```

```basic
VAR result = UO.Dead(self)
```

---

## `UO.DeleteFindList`

### Manifest-registered overloads

- `UO.DeleteFindList(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.DeleteFindList(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.DeleteFindList(arg1:Any, arg2:Any, arg3:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.DeleteFindList(list)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.DeleteFindList(list, type)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.DeleteFindList(list, type, color)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `list` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DeleteFindList(0)
```

```basic
UO.DeleteFindList(0, 0x0190, -1)
```

---

## `UO.DeleteIgnoreList`

### Manifest-registered overloads

- `UO.DeleteIgnoreList(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.DeleteIgnoreList(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.DeleteIgnoreList(arg1:Any, arg2:Any, arg3:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.DeleteIgnoreList(list)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.DeleteIgnoreList(list, type)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.DeleteIgnoreList(list, type, color)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `list` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DeleteIgnoreList(0)
```

```basic
UO.DeleteIgnoreList(0, 0x0190, -1)
```

---

## `UO.DeleteJournal`

### Direct runtime overloads

- `UO.DeleteJournal(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.DeleteJournal() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.DeleteJournal(0)
```

```basic
UO.DeleteJournal()
```

---

## `UO.DeleteObject`

### Direct runtime overloads

- `UO.DeleteObject(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.DeleteObject(0)
```

---

## `UO.Dex`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение характеристики Ловкость (Dexterity) персонажа. Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Dex()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Dex"]` → `BRIDGE CONTRACT -> IApiBridge.Dexterity`

**Pascal compatibility signature:** `function Dex: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Dex()
```

---

## `UO.Dexterity`

### Direct runtime overloads

- `UO.Dexterity() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Dexterity()
```

---

## `UO.Dir`

### Direct runtime overloads

- `UO.Dir() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Dir()
```

---

## `UO.Direction`

### Direct runtime overloads

- `UO.Direction() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer coordinate/direction value for the current player in the zero-argument alias form.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Direction()
```

---

## `UO.Disarm`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Снимает предметы из обеих рук (правой и левой) в рюкзак персонажа. Перебирает RhandLayer и LhandLayer , вызывая Unequip для каждого занятого слоя. Возвращает False , если персонаж не подключён или перемещение предмета из руки в рюкзак не удалось. Возвращает True , если обе руки пусты после вызова (включая случай, когда они были пусты изначально). В Python реализация использует MoveItem для каждого слоя руки.

### Current Yoko signatures / Return

- `UO.Disarm()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.Disarm"]`

**Pascal compatibility signature:** `function Disarm: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Disarm()
```

---

## `UO.Disconnect`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отключает текущего персонажа от сервера UO. Если персонаж уже отключён, метод ничего не делает.

### Current Yoko signatures / Return

- `UO.Disconnect()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Disconnect"]` → `BRIDGE CONTRACT -> IApiBridge.DisconnectClient`

**Pascal compatibility signature:** `procedure Disconnect;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Disconnect()
```

---

## `UO.DisconnectedTime`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает дату и время последнего отключения от сервера. Если подключения ещё не было, возвращает время загрузки профиля персонажа в Stealth.

### Current Yoko signatures / Return

- `UO.DisconnectedTime()`
  - **Return type:** `Decimal`
  - **Return contract:** Decimal numeric runtime value.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DisconnectedTime"]` → `STATE -> InjectionApiState.DisconnectedTime`

**Pascal compatibility signature:** `function DisconnectedTime: TDateTime;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DisconnectedTime()
```

---

## `UO.Dismount`

### Manifest-registered overloads

- `UO.Dismount() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Dismount()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Dismount()
```

```basic
UO.Dismount()
```

---

## `UO.Dist`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает расстояние в тайлах между двумя точками ( X1 , Y1 ) и ( X2 , Y2 ). Расстояние вычисляется как Max(|X2-X1|, |Y2-Y1|) (расстояние Чебышёва), что соответствует реальному расстоянию в тайлах в UO.

### Current Yoko signatures / Return

- `UO.Dist(Xfrom, Yfrom, Xto, Yto)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Dist"]` → `BRIDGE CONTRACT -> IApiBridge.GetDistance`

**Pascal compatibility signature:** `function Dist(Xfrom: Word; Yfrom: Word; Xto: Word; Yto: Word): Word;`

### Parameters

- `Xfrom` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Yfrom` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Xto` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Yto` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Dist(0, 0, 0, 0)
```

---

## `UO.Drag`

### Direct runtime overloads

- `UO.Drag(arg1:Integer, arg2:Integer, arg3:Integer, arg4:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Drag(0, 0, 0, 0)
```

---

## `UO.DragItem`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Берёт предмет, помещая его «на палец» (курсор). Предмет не перемещается в контейнер или на землю — для завершения перемещения используйте DropItem . Возвращает True при успехе, False , если: ObjID равен 0 (без лога). Персонаж мёртв. Другой предмет уже удерживается «на пальце». Предмет с данным ID не найден. Если предмет в стеке и Count превышает размер стека, берётся весь стек. Используйте 0 для Count , чтобы взять все предметы из стека.

### Current Yoko signatures / Return

- `UO.DragItem(ObjID, Count)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DragItem"]` → `BRIDGE CONTRACT -> IApiBridge.DragItem`

**Pascal compatibility signature:** `function DragItem(ObjID: Cardinal; Count: Integer): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Count` — Quantity/count. 0 may mean all/default only where explicitly supported.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DragItem(self, 1)
```

---

## `UO.Dress`

### Direct runtime overloads

- `UO.Dress(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Dress(0)
```

---
