# UO.GetCharsListForShard

ClassicUO • Runtime API • `UO.GetCharsListForShard.md`

## Точный синтаксис / Registered signatures

```text
UO.GetCharsListForShard() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetCharsListForShard`

### Current Basic signatures / Return

- `UO.GetCharsListForShard() -> Array`
  - **Return type:** `Array`
  - **Return contract:** Array of non-empty character names known for the current shard. Empty array is valid when no character list has been received and no current character is available.

### Parameters

- None. The current selected/connected shard is used.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Returns the **actual character names received from the server's character-selection packet** for the current account/shard. ClassicUO caches that list in memory so the API can still return it after entering the world. If no cached list exists, the active `LoginScene.Characters` list is used; while already in game, the current player's name is the final fallback.

This command no longer returns the Basic profile serial as a fake character list.

### Notes / limitations

- The list reflects what the server supplied for the current shard/account during this client session.
- It does not invent character names by scanning profile directories.
- Empty slots from the server character list are removed.

### Examples

```basic
SUB Main()
    VAR chars = UO.GetCharsListForShard()
    UO.Print(chars)
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetCharsListForShard()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.GetCharsListForShard()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.GetCharsListForShard()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
