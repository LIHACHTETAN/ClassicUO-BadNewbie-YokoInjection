# UO.TargetByResource

ClassicUO • Runtime API • `UO.TargetByResource.md`

## Точный синтаксис / Registered signatures

```text
UO.TargetByResource(ObjID:Any, Resource:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.TargetByResource`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу пакет «target by resource», нацеливаясь на указанный объект с типом ресурса. ObjID — serial (ID) объекта-цели (например, инструмент вроде кирки). Resource — индекс типа ресурса (0–4): Значение Имя Описание 0 trt_ore Руда (mining) 1 trt_sand Песок 2 trt_wood Дерево (lumberjacking) 3 trt_graves Могилы 4 trt_redmushrooms Красные грибы В DWScript параметр Resource может быть также строкой (например, 'sand' , 'graves' ), которая внутренне преобразуется в соответствующее значение перечисления. Перед отправкой: если курсор цели уже активен — вызов отменяется с предупреждением. Если объект не существует — логируется ошибка. Если значение ресурса вне диапазона 0–4 — логируется ошибка. Перед отправкой пакета применяется задержка 30мс. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.TargetByResource(ObjID:Integer, Resource:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TargetByResource"]` → `BRIDGE CONTRACT -> IApiBridge.FindType` → `BRIDGE CONTRACT -> IApiBridge.UseObject` → `BRIDGE CONTRACT -> IApiBridge.WaitTargetObject`

**Pascal compatibility signature:** `procedure TargetByResource(ObjID: Cardinal; Resource: Word);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Resource` — Resource enum: 0=ore, 1=sand, 2=wood, 3=graves, 4=red mushrooms; supported string aliases are accepted by the runtime compatibility parser.

### Accepted values / constants

- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `Resource` — Resource enum: 0=ore, 1=sand, 2=wood, 3=graves, 4=red mushrooms; supported string aliases are accepted by the runtime compatibility parser.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.TargetByResource(self, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.TargetByResource(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # ObjID
    VAR arg2 = 2 # Resource
    UO.TargetByResource(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ObjID
    VAR arg2 = 2 # Resource
    UO.TargetByResource(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
