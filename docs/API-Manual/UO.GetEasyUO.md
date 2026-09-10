# UO.GetEasyUO

ClassicUO • Runtime API • `UO.GetEasyUO.md`

## Точный синтаксис / Registered signatures

```text
UO.GetEasyUO(number:Any) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetEasyUO`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает значение глобальной переменной EasyUO по её индексу num . Переменные EasyUO — это устаревший механизм обмена данными между скриптами EasyUO и Stealth.

### Current Basic signatures / Return

- `UO.GetEasyUO(num:Variant) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.GetEasyUO"]`

**Pascal compatibility signature:** `function GetEasyUO(num: Integer): String;`

### Parameters

- `num` — Integer control/count/index value (Variant); exact zero/sentinel meaning is documented by Behavior/Notes.

### Accepted values / constants

- `num` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.GetEasyUO(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetEasyUO(1)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = 1 # number
    VAR result = UO.GetEasyUO(arg1)
    IF len(result) > 0 THEN
        UO.Print(result)
    ELSE
        UO.Print('Empty')
    END IF
END SUB
```

### Поиск текста в результате

```vb
SUB Main()
    VAR arg1 = 1 # number
    VAR result = UO.GetEasyUO(arg1)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GetEasyUO`
