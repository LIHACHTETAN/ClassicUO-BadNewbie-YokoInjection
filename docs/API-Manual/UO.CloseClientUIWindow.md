# UO.CloseClientUIWindow

ClassicUO • Runtime API • `UO.CloseClientUIWindow.md`

## Точный синтаксис / Registered signatures

```text
UO.CloseClientUIWindow(UIWindowType:Any, ID:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.CloseClientUIWindow`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Закрывает окно клиентского интерфейса указанного типа для объекта с данным ID .

### Current Basic signatures / Return

- `UO.CloseClientUIWindow(UIWindowType:Integer, ID:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CloseClientUIWindow"]` → `BRIDGE CONTRACT -> IApiBridge.CloseClientWindow`

**Pascal compatibility signature:** `procedure CloseClientUIWindow(UIWindowType: TUIWindowType; ID: Cardinal);`

### Parameters

- `UIWindowType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `UIWindowType` — 0=PaperDoll, 1=Status, 2=Profile, 3=Container.
- `ID` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional.

### Behavior

Closes a supported ClassicUO client window matching UIWindowType and ID. The bridge maps 0 to PaperDollGump, 1 to StatusGumpBase, 2 to ProfileGump, and 3 to ContainerGump; unsupported type values match nothing.
### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.CloseClientUIWindow(0x0190, self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.CloseClientUIWindow(1, self)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # UIWindowType
    VAR arg2 = self # ID
    UO.CloseClientUIWindow(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # UIWindowType
    VAR arg2 = self # ID
    UO.CloseClientUIWindow(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
