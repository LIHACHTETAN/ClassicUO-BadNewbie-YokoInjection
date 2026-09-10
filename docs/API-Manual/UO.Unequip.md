# UO.Unequip

ClassicUO • Runtime API • `UO.Unequip.md`

## Точный синтаксис / Registered signatures

```text
UO.Unequip(Layer:Any) -> Any
UO.Unequip(layer:String) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Unequip`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Снимает предмет с указанного слоя экипировки и помещает его в рюкзак. Layer — индекс слоя экипировки. См. ConstantsAndEnums для значений слоёв. Вспомогательные методы, возвращающие значения слоёв, вынесены на отдельную страницу: Layers . Возвращает True , если предмет успешно снят, False — если слой пуст или операция не удалась. В Python метод называется UnEquip .

### Current Basic signatures / Return

- `UO.Unequip(Layer:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Unequip"]` → `BRIDGE CONTRACT -> IApiBridge.Unequip`

**Pascal compatibility signature:** `function Unequip(Layer: Byte): Boolean;`

### Parameters

- `Layer` — Equipment layer name or numeric layer identifier accepted by the runtime overload.

### Accepted values / constants

- `Layer` — Named layers: Rhand, Lhand, Shoes, Pants, Shirt, Hat, Gloves, Ring, Talisman, Neck, Hair, Waist, Torso, Brace, Face, Beard, Tunic, Ear, Arms, Cloak, BackpackLayer, Robe, Skirt, Legs, Mount, Bank; numeric layer where supported.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.Unequip('Rhand')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.Unequip('example')
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 'example' # layer
    VAR result = UO.Unequip(arg1)
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
    VAR result = UO.Unequip(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.Unequip`
