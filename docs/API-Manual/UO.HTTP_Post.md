# UO.HTTP_Post

ClassicUO • Runtime API • `UO.HTTP_Post.md`

## Точный синтаксис / Registered signatures

```text
UO.HTTP_Post(URL:Any, PostData:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.HTTP_Post`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Выполняет HTTP POST-запрос по указанному URL с переданными данными и возвращает тело ответа. URL — адрес запроса. PostData — данные для тела POST-запроса. Возвращаемое значение — текст тела ответа. После запроса HTTP_Header также содержит тело ответа, а HTTP_Body — заголовки (см. примечания об исторической путанице имён в этих методах). Если имя хоста не удаётся разрешить, метод записывает ошибку в системный журнал и возвращает пустую строку. PascalScript поддерживает только форму с TStringList . DWScript поддерживает как форму с TStringList , так и дополнительную перегрузку, принимающую простую String .

### Current Basic signatures / Return

- `UO.HTTP_Post(URL:String, PostData:String) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Post"]` → `STATE -> InjectionApiState.HttpBody` → `STATE -> InjectionApiState.HttpHeader` → `BRIDGE CONTRACT -> IApiBridge.HttpRequest`

**Pascal compatibility signature:** `function HTTP_Post(URL: String; PostData: TStringList): String;`

### Parameters

- `URL` — HTTP/HTTPS URL string.
- `PostData` — Text/String value (String); pass literal text as a quoted BASIC string.

### Accepted values / constants

- `URL` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `PostData` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Operates on the active Basic/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.HTTP_Post('https://example.com/', 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.HTTP_Post('https://example.com/', 2)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 'https://example.com/' # URL
    VAR arg2 = 2 # PostData
    VAR result = UO.HTTP_Post(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'https://example.com/' # URL
    VAR arg2 = 2 # PostData
    VAR result = UO.HTTP_Post(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
