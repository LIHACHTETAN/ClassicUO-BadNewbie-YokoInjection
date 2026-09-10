# UO.PlayWav

ClassicUO • Runtime API • `UO.PlayWav.md`

## Точный синтаксис / Registered signatures

```text
UO.PlayWav(FileName:Any) -> Any
UO.PlayWav(file:String) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.PlayWav`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Воспроизводит WAV-файл асинхронно. FileName — путь к WAV-файлу. Возвращает True , если воспроизведение началось успешно, False — если файл не существует. Метод в основном поддерживается на Windows. На macOS и Android в системный журнал записывается информационное сообщение, и вызов не имеет эффекта.

### Current Basic signatures / Return

- `UO.PlayWav(FileName:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["PlayWav"]` → `BRIDGE CONTRACT -> IApiBridge.PlayWav`

**Pascal compatibility signature:** `function PlayWav(FileName: String): Boolean;`

### Parameters

- `FileName` — Text/String value (String); pass literal text as a quoted BASIC string.

### Accepted values / constants

- `FileName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.PlayWav('example.txt')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.PlayWav('example.txt')
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 'example.txt' # file
    VAR result = UO.PlayWav(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 'example.txt' # file
    VAR result = UO.PlayWav(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.PlayWav`
