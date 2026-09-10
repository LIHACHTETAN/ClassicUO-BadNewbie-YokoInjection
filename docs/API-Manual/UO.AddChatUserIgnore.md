# UO.AddChatUserIgnore

ClassicUO • Runtime API • `UO.AddChatUserIgnore.md`

## Точный синтаксис / Registered signatures

```text
UO.AddChatUserIgnore(UserName:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.AddChatUserIgnore`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Добавляет имя мобайла в список игнорируемых в чате. Сообщения от этого мобайла не будут отображаться в журнале, но по-прежнему доступны скриптовым методам, таким как InJournal . Полезно для фильтрации спама от определённых игроков с сохранением возможности программной обработки их сообщений. Примечание: Метод не действует на подключённых (attached) клиентов — применяется только к внутреннему журналу Stealth.

### Current Basic signatures / Return

- `UO.AddChatUserIgnore(UserName:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddChatUserIgnore"]` → `BRIDGE CONTRACT -> IApiBridge.AddChatUserIgnore`

**Pascal compatibility signature:** `procedure AddChatUserIgnore(UserName: String);`

### Parameters

- `UserName` — Named runtime value (String); use the exact registered/saved name expected by AddChatUserIgnore.

### Accepted values / constants

- `UserName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.AddChatUserIgnore('example')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.AddChatUserIgnore(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # UserName
    UO.AddChatUserIgnore(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # UserName
    UO.AddChatUserIgnore(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
