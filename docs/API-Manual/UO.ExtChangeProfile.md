# UO.ExtChangeProfile

ClassicUO • Runtime API • `UO.ExtChangeProfile.md`

## Точный синтаксис / Registered signatures

```text
UO.ExtChangeProfile(ProfileName:Any) -> Any
UO.ExtChangeProfile(ProfileName:Any, ShardName:Any) -> Any
UO.ExtChangeProfile(ProfileName:Any, ShardName:Any, CharName:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ExtChangeProfile`

### Current Basic signatures / Return

- `UO.ExtChangeProfile(ProfileName:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ExtChangeProfile"]`
- `UO.ExtChangeProfile(ProfileName:String, ShardName:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ExtChangeProfile"]`
- `UO.ExtChangeProfile(ProfileName:String, ShardName:String, CharName:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ExtChangeProfile"]`

### Parameters

- `ProfileName` — canonical Basic character profile name, normally `0x<serial>`.
- `ShardName` — optional human-readable server/shard name. Empty uses the current/last selected server.
- `CharName` — optional character name. Empty uses the character identity stored with that profile when available.

### Accepted values / constants

- `ProfileName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `ShardName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `CharName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 1, 2, 3. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Extended profile selection for a disconnected client. The command validates that the target profile exists beneath the selected server-name folder, saves/unloads the current profile, stores the selected shard in ClassicUO settings and supplies the target character to the real login character-selection flow.

### Notes / limitations

- The server folder uses the actual display server name, not `V2`, not `IP:port`, and not the internal shard identity key.
- If `CharName` is empty, the `.character-name` metadata saved with the canonical profile is used.
- The command does not bypass server authentication and cannot select a character the shard does not return.
- Use `UO.Connect()` after a successful return when an immediate reconnect is desired.

### Examples

```basic
SUB Main()
    VAR rc = UO.ExtChangeProfile('0x12345678', 'Age of Power', 'LIHACH')
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
    VAR result = UO.ExtChangeProfile('example.txt')
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = 'example.txt' # ProfileName
    VAR arg2 = 2 # ShardName
    VAR arg3 = 3 # CharName
    VAR result = UO.ExtChangeProfile(arg1, arg2, arg3)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.ExtChangeProfile('example.txt', 2)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 'example.txt' # ProfileName
    VAR result = UO.ExtChangeProfile(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'example.txt' # ProfileName
    VAR result = UO.ExtChangeProfile(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
