# UO.HTTP_Header

ClassicUO • Runtime API • `UO.HTTP_Header.md`

## Точный синтаксис / Registered signatures

```text
UO.HTTP_Header() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.HTTP_Header`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает тело HTTP-ответа от последнего запроса HTTP_Get или HTTP_Post . Известный баг (сохранён для обратной совместимости): Несмотря на название, HTTP_Header на самом деле возвращает тело ответа, а не заголовки. Заголовки возвращаются через HTTP_Body . Эта путаница имён — исторический баг, сохранённый, чтобы не ломать существующие скрипты. Возвращает пустую строку, если HTTP-запрос не выполнялся или персонаж не подключён.

### Current Basic signatures / Return

- `UO.HTTP_Header() -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Header"]` → `STATE -> InjectionApiState.HttpHeader`

**Pascal compatibility signature:** `function HTTP_Header: String;`

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
    VAR result = UO.HTTP_Header()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.HTTP_Header()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.HTTP_Header()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.HTTP_Header()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
