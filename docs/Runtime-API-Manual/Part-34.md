# Runtime API Manual — Part 34

Commands: **WearItem** through **Z**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.WearItem`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Экипирует ранее подобранный предмет на указанный слой экипировки. Layer — индекс слоя экипировки. См. ConstantsAndEnums . Вспомогательные методы, возвращающие значения слоёв, вынесены на отдельную страницу: Layers . Должен быть ненулевым. ObjID — serial (ID) экипируемого предмета. Возвращает True при успешной экипировке, False — в противном случае. Метод требует, чтобы предмет был предварительно подобран (через DragItem или аналогичный метод). Если ничего не держится ( PickupedItem = 0 ), метод возвращает False . Если слой равен 0 или ID игрока равен 0 , метод также возвращает False .

### Current Yoko signatures / Return

- `UO.WearItem(Layer, ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WearItem"]` → `BRIDGE CONTRACT -> IApiBridge.Equip`

**Pascal compatibility signature:** `function WearItem(Layer: Byte; ObjID: Cardinal): Boolean;`

### Parameters

- `Layer` — Equipment layer name or numeric layer identifier accepted by the runtime overload.
- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WearItem('Rhand', self)
```

---

## `UO.Weight`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущий общий вес персонажа (в стоунах). Это значение включает вес тела персонажа, всех экипированных предметов и всего содержимого рюкзака (включая вложенные контейнеры). Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Weight()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Weight"]` → `BRIDGE CONTRACT -> IApiBridge.Weight`

**Pascal compatibility signature:** `function Weight: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Weight()
```

---

## `UO.WorldNum`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает номер текущего мира (фасета), в котором находится персонаж. Значение Фасет 0 Felucca 1 Trammel 2 Ilshenar 3 Malas 4 Tokuno 5 Ter Mur

### Current Yoko signatures / Return

- `UO.WorldNum()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WorldNum"]` → `BRIDGE CONTRACT -> IApiBridge.WorldNumber`

**Pascal compatibility signature:** `function WorldNum: Byte;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WorldNum()
```

---

## `UO.X`

### Direct runtime overloads

- `UO.X() -> Integer`
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
VAR result = UO.X()
```

---

## `UO.Y`

### Direct runtime overloads

- `UO.Y() -> Integer`
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
VAR result = UO.Y()
```

---

## `UO.Z`

### Direct runtime overloads

- `UO.Z() -> Integer`
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
VAR result = UO.Z()
```

---
