# UO.FillInfoWindow

ClassicUO • Runtime API • `UO.FillInfoWindow.md`

## Точный синтаксис / Registered signatures

```text
UO.FillInfoWindow(S:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.FillInfoWindow`

### Current Basic signatures / Return

- `UO.FillInfoWindow(text:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Appends the supplied text to the Basic/ClassicUO **Info Window** and opens/brings that information surface into use.

### Parameters

- `text` — text line to append.

### Accepted values / constants

- `text` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Writes to the Info Window through the client text-information route. It does not merely emit a normal in-game/system chat message.

### Notes / limitations

`FillInfoWindow` is explicit output and is **not suppressed** by `SetSilentMode(True)`. Silent mode controls automatic diagnostic output from commands such as Gump line/description queries.

### Examples

```basic
SUB Main()
    UO.FillInfoWindow('Runebook inspection started')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.FillInfoWindow(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # S
    UO.FillInfoWindow(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # S
    UO.FillInfoWindow(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
