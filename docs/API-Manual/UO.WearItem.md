# UO.WearItem

ClassicUO • Runtime API • `UO.WearItem.md`

## Точный синтаксис / Registered signatures

```text
UO.WearItem(Layer:Any, ObjID:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.WearItem`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Экипирует ранее подобранный предмет на указанный слой экипировки. Layer — индекс слоя экипировки. См. ConstantsAndEnums . Вспомогательные методы, возвращающие значения слоёв, вынесены на отдельную страницу: Layers . Должен быть ненулевым. ObjID — serial (ID) экипируемого предмета. Возвращает True при успешной экипировке, False — в противном случае. Метод требует, чтобы предмет был предварительно подобран (через DragItem или аналогичный метод). Если ничего не держится ( PickupedItem = 0 ), метод возвращает False . Если слой равен 0 или ID игрока равен 0 , метод также возвращает False .

### Current Basic signatures / Return

- `UO.WearItem(Layer:Integer, ObjID:Integer) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WearItem"]` → `BRIDGE CONTRACT -> IApiBridge.Equip`

**Pascal compatibility signature:** `function WearItem(Layer: Byte; ObjID: Cardinal): Boolean;`

### Parameters

- `Layer` — Equipment layer name or numeric layer identifier accepted by the runtime overload.
- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `Layer` — Named layers: Rhand, Lhand, Shoes, Pants, Shirt, Hat, Gloves, Ring, Talisman, Neck, Hair, Waist, Torso, Brace, Face, Beard, Tunic, Ear, Arms, Cloak, BackpackLayer, Robe, Skirt, Legs, Mount, Bank; numeric layer where supported.
- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.WearItem('Rhand', self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.WearItem(1, 2)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # Layer
    VAR arg2 = 2 # ObjID
    VAR result = UO.WearItem(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Layer
    VAR arg2 = 2 # ObjID
    VAR result = UO.WearItem(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
