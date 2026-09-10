# UO.InviteToParty

ClassicUO • Runtime API • `UO.InviteToParty.md`

## Точный синтаксис / Registered signatures

```text
UO.InviteToParty(ObjID:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.InviteToParty`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет приглашение в пати указанному мобайлу. ObjID — ID мобайла для приглашения. Метод сначала проверяет, существует ли объект в мире клиента. Если найден, устанавливает таргет на указанного мобайла и отправляет запрос на приглашение в пати. Если объект не существует, в системный журнал записывается ошибка: "InviteToParty error: Object not found." .

### Current Basic signatures / Return

- `UO.InviteToParty(ObjID:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["InviteToParty"]` → `BRIDGE CONTRACT -> IApiBridge.PartyInvite`

**Pascal compatibility signature:** `procedure InviteToParty(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.InviteToParty(self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.InviteToParty(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # ObjID
    UO.InviteToParty(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ObjID
    UO.InviteToParty(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
