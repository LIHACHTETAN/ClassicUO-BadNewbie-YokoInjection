# UO.EquipItems

ClassicUO • Runtime API • `UO.EquipItems.md`

## Точный синтаксис / Registered signatures

```text
UO.EquipItems(Items:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.EquipItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Надевает несколько предметов сразу из переданного списка ID. Каждый предмет автоматически размещается на соответствующем слое на основе его типа. Возвращает True , если все предметы были успешно экипированы, False в противном случае.

### Current Basic signatures / Return

- `UO.EquipItems(Items:Array) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["EquipItems"]` → `BRIDGE CONTRACT -> IApiBridge.Equip` → `BRIDGE CONTRACT -> IApiBridge.GetLayer`

**Pascal compatibility signature:** `function EquipItems(Items: TArray ): Boolean;`

### Parameters

- `Items` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `Items` — Runtime Array/list value with element type/shape described by Behavior.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.EquipItems(1000)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.EquipItems(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # Items
    VAR result = UO.EquipItems(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Items
    VAR result = UO.EquipItems(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
