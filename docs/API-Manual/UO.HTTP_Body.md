# UO.HTTP_Body

ClassicUO • Runtime API • `UO.HTTP_Body.md`

## Точный синтаксис / Registered signatures

```text
UO.HTTP_Body() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.HTTP_Body`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает HTTP-заголовки ответа от последнего запроса HTTP_Get или HTTP_Post . Известный баг (сохранён для обратной совместимости): Несмотря на название, HTTP_Body на самом деле возвращает заголовки ответа, а не тело. Тело возвращается через HTTP_Header . Эта путаница имён — исторический баг, сохранённый, чтобы не ломать существующие скрипты. Возвращает пустую строку, если HTTP-запрос не выполнялся или персонаж не подключён.

### Current Basic signatures / Return

- `UO.HTTP_Body() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Body"]` → `STATE -> InjectionApiState.HttpBody`

**Pascal compatibility signature:** `function HTTP_Body: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Operates on the active Basic/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.HTTP_Body()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.HTTP_Body()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.HTTP_Body()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.HTTP_Body()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
