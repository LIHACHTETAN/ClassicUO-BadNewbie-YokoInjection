# UO.StartScript

ClassicUO • Runtime API • `UO.StartScript.md`

## Точный синтаксис / Registered signatures

```text
UO.StartScript(ScriptPath:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.StartScript`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Запускает скрипт из указанного файла. ScriptPath — путь к файлу скрипта ( .dsc , .sc , .py и т.д.). Может быть абсолютным или относительным к каталогу скриптов Stealth. Возвращает новое общее количество запущенных скриптов после запуска, или $FFFF (65535) при неудаче (файл не найден, объект персонажа недоступен и т.д.). Метод ожидает увеличения числа скриптов в пуле, подтверждая успешный запуск.

### Current Basic signatures / Return

- `UO.StartScript(ScriptPath:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StartScript"]` → `BRIDGE CONTRACT -> IApiBridge.StartScript`

**Pascal compatibility signature:** `function StartScript(ScriptPath: String): Word;`

### Parameters

- `ScriptPath` — String value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `ScriptPath` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Operates on the active Basic/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.StartScript(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.StartScript('example.txt')
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 'example.txt' # ScriptPath
    VAR result = UO.StartScript(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'example.txt' # ScriptPath
    VAR result = UO.StartScript(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
