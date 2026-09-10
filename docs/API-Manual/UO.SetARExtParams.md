# UO.SetARExtParams

ClassicUO • Runtime API • `UO.SetARExtParams.md`

## Точный синтаксис / Registered signatures

```text
UO.SetARExtParams() -> Unit
UO.SetARExtParams(ShardName:Any) -> Unit
UO.SetARExtParams(ShardName:Any, CharName:Any) -> Unit
UO.SetARExtParams(ShardName:Any, CharName:Any, UseAtEveryConnect:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetARExtParams`

### Current Basic signatures / Return

- `UO.SetARExtParams() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetARExtParams"]`
- `UO.SetARExtParams(ShardName:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetARExtParams"]`
- `UO.SetARExtParams(ShardName:String, CharName:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetARExtParams"]`
- `UO.SetARExtParams(ShardName:String, CharName:String, UseAtEveryConnect:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetARExtParams"]`

### Parameters

- `ShardName` — display name of the shard/server to select on reconnect. Empty or omitted uses the current connected shard name.
- `CharName` — character name to select after the server character list arrives. Empty or omitted uses the current character name when available.
- `UseAtEveryConnect` — Boolean/integer flag. `0` makes the requested character override one-shot; non-zero keeps the character selection override for subsequent reconnects. The shard display selection is saved through ClassicUO's normal `LastServerName` settings path.

### Accepted values / constants

- `ShardName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `CharName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `UseAtEveryConnect` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

Registered arities: 0, 1, 2, 3. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

The values are no longer stored as inert runtime-only strings. Basic passes them into the actual ClassicUO reconnect selection pipeline:

1. the shard name updates ClassicUO's selected server preference;
2. the character name is supplied through `LastCharacterManager`;
3. the next `UO.Connect()` / reconnect uses those preferences when the server list and character list are received.

The command does **not** enable automatic reconnect by itself. Use the normal AutoReconnect/`SetARStatus` API for that policy.

### Notes / limitations

- `ShardName` is the human-readable server/shard name, not `IP:port` and not the internal profile identity key.
- Selection can only succeed if the requested shard/character is actually returned by the server.
- The connected server's profile folder is created using the actual display server name, for example `Data/Profiles/Age of Power/0x12345678/`.

### Examples

```basic
SUB Main()
    UO.SetARExtParams('Age of Power', 'LIHACH', 1)
END SUB
```

```basic
SUB Main()
    # Use current shard/current character as reconnect selection.
    UO.SetARExtParams()
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetARExtParams()
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # ShardName
    VAR arg2 = 2 # CharName
    VAR arg3 = 3 # UseAtEveryConnect
    UO.SetARExtParams(arg1, arg2, arg3)
END SUB
```

### Перегрузка: 1 аргументов

```vb
SUB Main()
    UO.SetARExtParams(1)
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    UO.SetARExtParams(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.SetARExtParams()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.SetARExtParams()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
