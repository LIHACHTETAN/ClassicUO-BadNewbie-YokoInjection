# UO.ChangeProfile

ClassicUO • Runtime API • `UO.ChangeProfile.md`

## Точный синтаксис / Registered signatures

```text
UO.ChangeProfile(Name:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ChangeProfile`

### Current Basic signatures / Return

- `UO.ChangeProfile(Name:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** `0` = accepted; `-2` = client is connected/connecting; `-3` = more than one Basic script is running; `-4` = requested Basic profile does not exist or cannot be resolved.

### Parameters

- `Name` — exact Basic profile name. In this ClassicUO integration a character profile is the canonical serial folder name, for example `0x12345678`.

### Accepted values / constants

- `Name` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Switches the **disconnected** Basic/ClassicUO profile selection to another existing character profile on the current server. Character metadata saved with the profile is used to configure the next login/reconnect. The current profile is saved and unloaded before the new selection is accepted.

Profiles are stored under the connected server display name:

`Data/Profiles/<server name>/<0xSerial>/`

### Notes / limitations

- The client must be disconnected; an in-game or connecting client returns `-2`.
- Only one Basic script may be active; otherwise `-3` is returned.
- `Name` is case-sensitive at the API level and must resolve to an existing canonical character profile; missing profiles return `-4`.
- The command selects the profile/reconnect target; it does not itself force an immediate network connection. Use `UO.Connect()` when appropriate.

### Examples

```basic
SUB Main()
    VAR rc = UO.ChangeProfile('0x12345678')
    IF rc = 0 THEN
        UO.Connect()
    END IF
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ChangeProfile('example')
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 'example' # Name
    VAR result = UO.ChangeProfile(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'example' # Name
    VAR result = UO.ChangeProfile(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
