# UO.RequestContextMenu

ClassicUO • Runtime API • `UO.RequestContextMenu.md`

## Точный синтаксис / Registered signatures

```text
UO.RequestContextMenu(ObjID:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.RequestContextMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос контекстного меню для указанного объекта. ObjID — serial (ID) объекта, для которого запрашивается контекстное меню. Запрос отправляется только если флаги возможностей сервера включают поддержку контекстных меню. Если контекстные меню на шарде не включены, вызов ничего не делает. Ответ приходит асинхронно. Используйте GetContextMenu для получения пунктов меню после небольшой задержки. Рекомендуется вызывать ClearContextMenu перед запросом, чтобы получить свежие данные. Для автоматического выбора пункта контекстного меню при его получении используйте SetContextMenuHook . Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.RequestContextMenu(ObjID:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RequestContextMenu"]` → `BRIDGE CONTRACT -> IApiBridge.RequestContextMenu`

**Pascal compatibility signature:** `procedure RequestContextMenu(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.RequestContextMenu(self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.RequestContextMenu(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # ObjID
    UO.RequestContextMenu(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ObjID
    UO.RequestContextMenu(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
