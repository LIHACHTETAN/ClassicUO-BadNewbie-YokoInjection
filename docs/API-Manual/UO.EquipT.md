# UO.EquipT

ClassicUO • Runtime API • `UO.EquipT.md`

## Точный синтаксис / Registered signatures

```text
UO.EquipT(layer:Any, type:Any) -> Unit
UO.EquipT(layer:Integer, type:Integer) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.EquipT`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Надевает первый найденный предмет с типом ObjType из рюкзака на указанный слой экипировки Layer . Возвращает True при успешной экипировке, False , если персонаж не подключён, предмет не найден, или операция не удалась.

### Current Basic signatures / Return

- `UO.EquipT(layer:Layer, type:GraphicId) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
- `UO.EquipT(layer:Integer, type:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean contract: 1 means success/condition satisfied; 0 means failure, timeout, clear-state, or no matching object/menu as described by Behavior.

**Pascal compatibility signature:** `function Equipt(Layer: Byte; ObjType: Word): Boolean;`

### Parameters

- `layer` — Equipment layer name or numeric layer. Named values include Rhand, Lhand, Shoes, Pants, Shirt, Hat, Gloves, Ring, Talisman, Neck, Hair, Waist, Torso, Brace, Face, Beard, Tunic, Ear, Arms, Cloak, BackpackLayer, Robe, Skirt, Legs, Mount, Bank.
- `type` — Graphic/body/tile ID. Use decimal or 0x-prefixed hexadecimal; wildcard -1/0xFFFF is valid only for overloads whose Behavior explicitly supports wildcard matching.

### Accepted values / constants

- `layer` — Named layers: Rhand, Lhand, Shoes, Pants, Shirt, Hat, Gloves, Ring, Talisman, Neck, Hair, Waist, Torso, Brace, Face, Beard, Tunic, Ear, Arms, Cloak, BackpackLayer, Robe, Skirt, Legs, Mount, Bank; numeric layer where supported.
- `type` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Finds the first matching item type in the backpack and equips it. With a named/string layer the general Basic overload performs the action and returns Unit. With two exact Integer arguments the legacy Equipt compatibility overload returns 1 on successful equip and 0 when no item is found or equip fails.
### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.EquipT('Rhand', 0x0190)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.EquipT(1, 0x0EED)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 1 # layer
        VAR arg2 = 0x0EED # type
        UO.EquipT(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 1 # layer
    VAR arg2 = 0x0EED # type
    UO.EquipT(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.EquipT`
- `InjectionScript.Runtime.InjectionApiUO.Equipt`
