# UO.SetEasyUO

ClassicUO • Runtime API • `UO.SetEasyUO.md`

## Точный синтаксис / Registered signatures

```text
UO.SetEasyUO(number:Any, value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetEasyUO`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Записывает значение в общий реестр EasyUO (только Windows). num — номер ключа (целое число). Regvalue — строковое значение для записи. Метод записывает в реестр Windows по пути HKEY_CURRENT_USER\Software\EasyUO , используя ключ * . Обеспечивает обмен данными со скриптами EasyUO через общее хранилище в реестре. Используйте GetEasyUO для чтения значений из того же реестра. Только Windows. На остальных платформах метод ничего не делает.

### Current Basic signatures / Return

- `UO.SetEasyUO(num:Variant, Regvalue:Variant) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.SetEasyUO"]`

**Pascal compatibility signature:** `procedure SetEasyUO(num: Integer; Regvalue: String);`

### Parameters

- `num` — Integer control/count/index value (Variant); exact zero/sentinel meaning is documented by Behavior/Notes.
- `Regvalue` — Variant value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `num` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.
- `Regvalue` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetEasyUO(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetEasyUO(1, 2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 1 # number
        VAR arg2 = 2 # value
        UO.SetEasyUO(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 1 # number
    VAR arg2 = 2 # value
    UO.SetEasyUO(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.SetEasyUO`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
