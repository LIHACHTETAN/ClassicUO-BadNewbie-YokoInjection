# UO.SetContextMenuHook

ClassicUO • Runtime API • `UO.SetContextMenuHook.md`

## Точный синтаксис / Registered signatures

```text
UO.SetContextMenuHook(MenuID:Any, EntryNumber:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetContextMenuHook`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Устанавливает перехватчик, который автоматически выбирает указанный пункт из любого полученного контекстного меню для заданного объекта. MenuID — serial (ID) объекта, контекстное меню которого перехватывается. EntryNumber — индекс пункта контекстного меню (с нуля), который будет автоматически выбран. При получении контекстного меню для совпадающего объекта указанный пункт автоматически выбирается и отправляется серверу, как если бы игрок по нему кликнул. Перехватчик остаётся активным и срабатывает при каждом совпадающем контекстном меню — он не сбрасывается после первого использования. Чтобы сменить объект или пункт, вызовите SetContextMenuHook повторно; чтобы отключить — вызовите SetContextMenuHook(0, 0) . Используйте RequestContextMenu для вызова контекстного меню после установки перехватчика.

### Current Basic signatures / Return

- `UO.SetContextMenuHook(MenuID:Integer, EntryNumber:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetContextMenuHook"]` → `BRIDGE CONTRACT -> IApiBridge.SetContextMenuHook`

**Pascal compatibility signature:** `procedure SetContextMenuHook(MenuID: Cardinal; EntryNumber: Byte);`

### Parameters

- `MenuID` — Numeric identifier (Integer). Use the ID domain documented by this command; 0 is a sentinel only when Behavior/Notes explicitly says so.
- `EntryNumber` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by Behavior/Notes.

### Accepted values / constants

- `MenuID` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `EntryNumber` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetContextMenuHook(self, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetContextMenuHook(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # MenuID
    VAR arg2 = 2 # EntryNumber
    UO.SetContextMenuHook(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # MenuID
    VAR arg2 = 2 # EntryNumber
    UO.SetContextMenuHook(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
