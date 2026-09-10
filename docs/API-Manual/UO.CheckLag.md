# UO.CheckLag

ClassicUO • Runtime API • `UO.CheckLag.md`

## Точный синтаксис / Registered signatures

```text
UO.CheckLag() -> Integer
UO.CheckLag(timeout:Any, retries:Any) -> Integer
UO.CheckLag(timeoutMS:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.CheckLag`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет пинг-запрос серверу UO и ждёт ответа в течение указанного таймаута. Возвращает True , если сервер ответил в пределах timeoutMS миллисекунд, False , если таймаут истёк (лаг или проблема соединения). Часто используется для проверки того, что сервер обработал предыдущие действия, перед отправкой новых. В Python таймаут по умолчанию — 10000 мс.

### Current Basic signatures / Return

- `UO.CheckLag(timeoutMS:int= 10000) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** 0x73 server-echo status; nonzero means matching echo before timeout, 0 means timeout/offline/no ACK.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CheckLag"]` → `BRIDGE CONTRACT -> IApiBridge.CheckLag`

**Pascal compatibility signature:** `function CheckLag(timeoutMS: Integer): Boolean;`

### Parameters

- `timeoutMS` — Timeout/delay in milliseconds. 0 has command-specific meaning; see Notes / limitations.

### Accepted values / constants

- `timeoutMS` — int. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Sends a tokenized 0x73 ping packet and waits for the matching server echo up to timeoutMS. It does not substitute IsOnline() for a network round trip.

### Notes / limitations

Requires a connected server that echoes 0x73. Timeout/offline/no matching ACK returns the documented failure value.

### Examples

```basic
SUB Main()
    VAR result = UO.CheckLag(1000)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.CheckLag()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = 1000 # timeout
    VAR arg2 = 2 # retries
    VAR result = UO.CheckLag(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 1 аргументов

```vb
SUB Main()
    VAR result = UO.CheckLag(1000)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.CheckLag()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.CheckLag()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.CheckLag`
