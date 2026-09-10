# UO.Equip

ClassicUO • Runtime API • `UO.Equip.md`

Слой проверяется до перемещения предмета и должен совпадать с реальным слоем экипировки предмета. Неподходящий предмет не поднимается.

## Точный синтаксис / Registered signatures

```text
UO.Equip(Layer:Any, ObjID:Any) -> Any
UO.Equip(layer:String, id:Integer) -> Integer
UO.Equip(layer:String, id:String) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Equip`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Надевает предмет с ObjID на указанный слой экипировки Layer персонажа. Возвращает True при успешной экипировке, False , если персонаж не подключён или операция не удалась. Предмет должен находиться в рюкзаке или на земле.

### Current Basic signatures / Return

- `UO.Equip(Layer:String, ObjID:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Equip"]` → `BRIDGE CONTRACT -> IApiBridge.Equip`

**Pascal compatibility signature:** `function Equip(Layer: Byte; ObjID: Cardinal): Boolean;`

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
    VAR result = UO.Equip('Rhand', self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.Equip('example', self)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 'example' # layer
    VAR arg2 = self # id
    VAR result = UO.Equip(arg1, arg2)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 'example' # layer
    VAR arg2 = self # id
    VAR result = UO.Equip(arg1, arg2)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.Equip`
