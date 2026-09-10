# UO.UnequipItems

ClassicUO • Runtime API • `UO.UnequipItems.md`

## Точный синтаксис / Registered signatures

```text
UO.UnequipItems(Items:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UnequipItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Снимает несколько экипированных предметов и помещает их в рюкзак. Items — массив serial (ID) объектов для снятия. Возвращает True , если все предметы успешно сняты, False при ошибке или если персонаж не подключён. Несуществующие предметы пропускаются. Задержка между операциями снятия контролируется переменной DressSpeed (ограничена 10–10000 мс). Только DWScript. В PascalScript тип параметра — TCardinalDynArray вместо TArray .

### Current Basic signatures / Return

- `UO.UnequipItems(Items:Array) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UnequipItems"]` → `BRIDGE CONTRACT -> IApiBridge.GetLayer` → `BRIDGE CONTRACT -> IApiBridge.Unequip`

**Pascal compatibility signature:** `function UnequipItems(Items: TArray ): Boolean;`

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
    VAR result = UO.UnequipItems(1000)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.UnequipItems(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # Items
    VAR result = UO.UnequipItems(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Items
    VAR result = UO.UnequipItems(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
