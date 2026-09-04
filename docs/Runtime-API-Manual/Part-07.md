# Runtime API Manual — Part 07

Commands: **DressSavedSet** through **EUO2Type**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.DressSavedSet`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Синоним для EquipDressSet . Надевает комплект экипировки, ранее сохранённый через SetDress . Полное описание, параметры и примеры см. в EquipDressSet . Возвращает True , если все предметы успешно надеты, False — в противном случае.

### Current Yoko signatures / Return

- `UO.DressSavedSet()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DressSavedSet"]`

**Pascal compatibility signature:** `function DressSavedSet: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DressSavedSet()
```

---

## `UO.DressSpeed`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Задаёт задержку (в миллисекундах) между отдельными операциями экипировки/снятия в EquipItems , UnequipItems и связанных методах одевания/раздевания. Ограничивается диапазоном 10–10000 мс. В Python используйте GetDressSpeed() / SetDressSpeed(value) .

### Current Yoko signatures / Return

- `UO.DressSpeed()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DressSpeed"]` → `STATE -> InjectionApiState.DressSpeed`
- `UO.DressSpeed(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DressSpeed"]` → `STATE -> InjectionApiState.DressSpeed`

**Pascal compatibility signature:** `var DressSpeed: Integer;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DressSpeed()
```

```basic
UO.DressSpeed('value')
```

---

## `UO.Drop`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Поднимает предмет с serial ObjID и сбрасывает его на землю в координаты X, Y, Z. Count <= 0 перемещает весь стек. Runtime входит в MoveItemChecked, проверяет ObjID, при включённом DropCheckCoord отклоняет координаты земли дальше двух тайлов, получает предмет из World.Items, затем вызывает ClassicUO GameActions.PickUp и GameActions.DropItem. Возвращает TRUE/1, если клиент принял обе стадии, иначе FALSE/0.

### Current Yoko signatures / Return

- `UO.Drop(ObjID, Count, X, Y, Z)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Drop"]`

**Pascal compatibility signature:** `function Drop(ObjID: Cardinal; Count: Integer; X: Integer; Y: Integer; Z: ShortInt): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Count` — Quantity/count. 0 may mean all/default only where explicitly supported.
- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `Z` — World/tile Z coordinate.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Drop(self, 1, UO.GetX(self), UO.GetY(self), UO.GetZ(self))
```

---

## `UO.DropCheckCoord`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Управляет проверкой координат назначения перед сбросом предмета. Когда True , система проверяет допустимость координат назначения перед выполнением сброса. Когда False , координаты отправляются без проверки. В Python используйте GetDropCheckCoord() / SetDropCheckCoord(value) .

### Current Yoko signatures / Return

- `UO.DropCheckCoord()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropCheckCoord"]` → `STATE -> InjectionApiState.DropCheckCoord`
- `UO.DropCheckCoord(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropCheckCoord"]` → `STATE -> InjectionApiState.DropCheckCoord`

**Pascal compatibility signature:** `var DropCheckCoord: Boolean;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DropCheckCoord()
```

```basic
UO.DropCheckCoord('value')
```

---

## `UO.DropDelay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Задаёт задержку (в миллисекундах) после операций сброса ( Drop , DropHere , DropItem , MoveItem и т.д.). Ограничивается диапазоном 50–10000 мс. В Python используйте GetDropDelay() / SetDropDelay(value) .

### Current Yoko signatures / Return

- `UO.DropDelay()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropDelay"]` → `BRIDGE CONTRACT -> IApiBridge.GetDropDelay` → `BRIDGE CONTRACT -> IApiBridge.SetDropDelay`
- `UO.DropDelay(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropDelay"]` → `BRIDGE CONTRACT -> IApiBridge.GetDropDelay` → `BRIDGE CONTRACT -> IApiBridge.SetDropDelay`

**Pascal compatibility signature:** `var DropDelay: Integer;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DropDelay()
```

```basic
UO.DropDelay('value')
```

---

## `UO.DropHere`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Сбрасывает предмет на землю под ногами персонажа. Удобный метод, который внутри вызывает DragItem , а затем DropItem с координатами персонажа. Если предмет является частью стека из более чем одного предмета, сбрасывается весь стек . Возвращает True при успехе, False при неудаче.

### Current Yoko signatures / Return

- `UO.DropHere(ItemID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropHere"]` → `BRIDGE CONTRACT -> IApiBridge.GetX` → `BRIDGE CONTRACT -> IApiBridge.GetY` → `BRIDGE CONTRACT -> IApiBridge.GetZ` → `BRIDGE CONTRACT -> IApiBridge.MoveItem` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function DropHere(ItemID: Cardinal): Boolean;`

### Parameters

- `ItemID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DropHere(self)
```

---

## `UO.DropItem`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Сбрасывает предмет, удерживаемый «на пальце» (ранее взятый через DragItem ), в контейнер, на землю или на другой предмет для стекирования. Возвращает True при успехе, False , если предмет не удерживается. Поведение MoveIntoID зависит от цели: Цель Поведение Ground ( $FFFFFFFF ) Сброс на землю по координатам (X, Y, Z). X/Y в диапазоне -2..+2 считаются относительными смещениями от персонажа. ID контейнера Сброс в указанный контейнер. X, Y обычно 0 . ID предмета Попытка стекирования с указанным предметом. После успешного сброса метод ожидает DropDelay миллисекунд (от 50 до 10000 мс). Если DropCheckCoord включён и координаты выглядят подозрительно, координаты сброса рандомизируются.

### Current Yoko signatures / Return

- `UO.DropItem(MoveIntoID, X, Y, Z)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropItem"]` → `BRIDGE CONTRACT -> IApiBridge.DropDraggedItem`

**Pascal compatibility signature:** `function DropItem(MoveIntoID: Cardinal; X: Integer; Y: Integer; Z: ShortInt): Boolean;`

### Parameters

- `MoveIntoID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `Z` — World/tile Z coordinate.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.DropItem(self, UO.GetX(self), UO.GetY(self), UO.GetZ(self))
```

---

## `UO.Dump`

### Manifest-registered overloads

- `UO.Dump() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Dump(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Dump()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Dump(object)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `object` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Dump()
```

```basic
UO.Dump(self)
```

---

## `UO.Dye`

### Manifest-registered overloads

- `UO.Dye(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Dye(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Dye(dyeObject)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Dye(dyeObject, target)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `dyeObject` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `target` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Dye(0)
```

```basic
UO.Dye(self, self)
```

---

## `UO.EasyObject`

### Manifest-registered overloads

- `UO.EasyObject(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.EasyObject(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.EasyObject(name)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.EasyObject(name, object)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `name` — String/text value interpreted according to the command.
- `object` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EasyObject(0)
```

```basic
UO.EasyObject('value', self)
```

---

## `UO.EmoteAction`

### Manifest-registered overloads

- `UO.EmoteAction(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.EmoteAction(action)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `action` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EmoteAction(0)
```

```basic
UO.EmoteAction(0)
```

---

## `UO.EmptyContainer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Перемещает все предметы из Container в DestContainer с задержкой DelayMS миллисекунд между каждым перемещением. Возвращает False , если исходный контейнер пуст. Иначе возвращает результат операций перемещения. Если Container равен DestContainer , метод выводит предупреждение и возвращает False для защиты от бесконечного цикла.

### Current Yoko signatures / Return

- `UO.EmptyContainer(Container, DestContainer, DelayMS)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["EmptyContainer"]` → `BRIDGE CONTRACT -> IApiBridge.EmptyContainer`

**Pascal compatibility signature:** `function EmptyContainer(Container: Cardinal; DestContainer: Cardinal; DelayMS: Word): Boolean;`

### Parameters

- `Container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `DestContainer` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `DelayMS` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EmptyContainer(backpack, backpack, 1000)
```

---

## `UO.EnergyResist`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение сопротивления энергии персонажа. Работает только с эрой сервера Samurai Empire и выше, и сервер должен отправлять расширенную статистику. Иначе всегда возвращает 0 .

### Current Yoko signatures / Return

- `UO.EnergyResist()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["EnergyResist"]` → `BRIDGE CONTRACT -> IApiBridge.EnergyResistance`

**Pascal compatibility signature:** `function EnergyResist: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EnergyResist()
```

---

## `UO.Equip`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Надевает предмет с ObjID на указанный слой экипировки Layer персонажа. Возвращает True при успешной экипировке, False , если персонаж не подключён или операция не удалась. Предмет должен находиться в рюкзаке или на земле.

### Current Yoko signatures / Return

- `UO.Equip(Layer, ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Equip"]` → `BRIDGE CONTRACT -> IApiBridge.Equip`

**Pascal compatibility signature:** `function Equip(Layer: Byte; ObjID: Cardinal): Boolean;`

### Parameters

- `Layer` — Equipment layer name or numeric layer identifier accepted by the runtime overload.
- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Equip('Rhand', self)
```

---

## `UO.EquipDressSet`

### Current Yoko signatures / Return

- `UO.EquipDressSet() -> Boolean`
  - **Return type:** `Boolean` (`1/0`)
  - **Return contract:** Returns `False` when no saved Stealth-compatible dress set exists; returns `True` when the saved set exists and equip/unequip requests were submitted.

### Parameters

- None.

### Behavior

Applies the saved compatibility dress set using the current Yoko equip route and configured dress speed. The command no longer returns unconditional `True` when no dress set exists.

### Notes / limitations

`True` means the dress set existed and client requests were submitted. Final server-side equipment state can still be affected by shard restrictions, item movement, lag, or equipment rules.

### Examples

```basic
IF UO.EquipDressSet() THEN
    UO.Print('Dress request submitted')
END IF
```

---

## `UO.EquipItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Надевает несколько предметов сразу из переданного списка ID. Каждый предмет автоматически размещается на соответствующем слое на основе его типа. Возвращает True , если все предметы были успешно экипированы, False в противном случае.

### Current Yoko signatures / Return

- `UO.EquipItems(Items)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["EquipItems"]` → `BRIDGE CONTRACT -> IApiBridge.Equip` → `BRIDGE CONTRACT -> IApiBridge.GetLayer`

**Pascal compatibility signature:** `function EquipItems(Items: TArray ): Boolean;`

### Parameters

- `Items` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EquipItems(1000)
```

---

## `UO.EquipLastWeapon`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Надевает последнее ранее экипированное оружие. Полезно для быстрого переключения между двумя видами оружия одной командой. Примечание: Работает только с версией клиента 5.0 и выше.

### Current Yoko signatures / Return

- `UO.EquipLastWeapon()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["EquipLastWeapon"]` → `BRIDGE CONTRACT -> IApiBridge.EquipLastWeapon`

**Pascal compatibility signature:** `procedure EquipLastWeapon;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.EquipLastWeapon()
```

---

## `UO.EquipT`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Надевает первый найденный предмет с типом ObjType из рюкзака на указанный слой экипировки Layer . Возвращает True при успешной экипировке, False , если персонаж не подключён, предмет не найден, или операция не удалась.

### Current Yoko signatures / Return

- `UO.Equipt(Layer, ObjType)`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

**Pascal compatibility signature:** `function Equipt(Layer: Byte; ObjType: Word): Boolean;`

### Parameters

- `Layer` — Equipment layer name or numeric layer identifier accepted by the runtime overload.
- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EquipT('Rhand', 0x0190)
```

---

## `UO.EUO2ID`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Преобразует строку ID объекта в формате EasyUO в числовой ID Stealth. EUO — строка из заглавных букв и цифр (формат EasyUO). Возвращает 0 , если преобразование не удалось. В Python метод называется EUO2StealthID .

### Current Yoko signatures / Return

- `UO.EUO2ID(EUO)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["EUO2ID"]`

**Pascal compatibility signature:** `function EUO2ID(EUO: String): Cardinal;`

### Parameters

- `EUO` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EUO2ID(0)
```

---

## `UO.EUO2Inj`

### Direct runtime overloads

- `UO.EUO2Inj(arg1:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EUO2Inj(0)
```

---

## `UO.EUO2Type`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Преобразует строку типа в формате EasyUO в числовой тип Stealth. Возвращает 0 , если преобразование не удалось. В Python метод называется EUO2StealthType .

### Current Yoko signatures / Return

- `UO.EUO2Type(EUO)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["EUO2Type"]`

**Pascal compatibility signature:** `function EUO2Type(EUO: String): Word;`

### Parameters

- `EUO` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.EUO2Type(0)
```

---
