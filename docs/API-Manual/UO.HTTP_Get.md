# UO.HTTP_Get

ClassicUO • Runtime API • `UO.HTTP_Get.md`

## Точный синтаксис / Registered signatures

```text
UO.HTTP_Get(URL:Any) -> Unit
UO.HTTP_Get(URL:Any, LStream:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.HTTP_Get`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Выполняет HTTP GET-запрос по указанному URL. URL — адрес запроса. После выполнения запроса используйте HTTP_Header для получения тела ответа и HTTP_Body для получения заголовков. См. примечания к HTTP_Body и HTTP_Header об исторической путанице имён. В DWS доступен необязательный второй параметр LStream ( TMemoryStream ). Если задан, сырое тело ответа записывается в этот поток вместо внутреннего строкового буфера. Полезно для скачивания бинарных данных (изображений, файлов). Если имя хоста не удаётся разрешить, метод записывает ошибку в системный журнал и завершается без выполнения запроса.

### Current Basic signatures / Return

- `UO.HTTP_Get(URL:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Get"]`
- `UO.HTTP_Get(URL:String, LStream:MemoryStream|File|0) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Get"]`

**Pascal compatibility signature:** `procedure HTTP_Get(URL: String; LStream: TMemoryStream = nil);`

### Parameters

- `URL` — HTTP/HTTPS URL string.
- `LStream` — Basic MemoryStream/File-compatible output target for raw response bytes.

### Accepted values / constants

- `URL` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `LStream` — MemoryStream(), File(path), or 0/omitted only where the signature permits it.

### Defaults / omitted arguments

Omitting LStream stores the response body in the runtime HTTP body buffer; supplying a stream writes raw response bytes to it.

### Behavior

Performs an HTTP GET. The one-argument form returns/uses the registered text semantics; the LStream overload writes raw response bytes to a supported Basic MemoryStream/File target.

### Notes / limitations

Network errors/timeouts remain runtime failures. For binary payloads use LStream/MemoryStream rather than converting bytes through UTF-8 text.

### Examples

```basic
SUB Main()
    UO.HTTP_Get('https://example.com/')
END SUB
```

```basic
SUB Main()
    VAR stream = MemoryStream()
    UO.HTTP_Get('https://example.com/file.bin', stream)
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.HTTP_Get('https://example.com/')
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = 'https://example.com/' # URL
    VAR arg2 = 2 # LStream
    UO.HTTP_Get(arg1, arg2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 'https://example.com/' # URL
    UO.HTTP_Get(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'https://example.com/' # URL
    UO.HTTP_Get(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
