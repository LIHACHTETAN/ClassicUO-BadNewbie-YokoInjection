# UO.SetWarMode

ClassicUO • Runtime API • `UO.SetWarMode.md`

## Точный синтаксис / Registered signatures

```text
UO.SetWarMode(Value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetWarMode`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Включает или отключает режим войны (боевую стойку) персонажа. Value — True для входа в режим войны, False для выхода. Отправляет серверу пакет переключения режима войны. В режиме войны персонаж принимает боевую стойку, и щелчки по мобайлам инициируют атаки. Обратите внимание, что Attack автоматически включает режим войны, поэтому вызывать SetWarMode(True) перед атакой обычно не нужно. Однако SetWarMode(False) полезен для явного выхода из боевой стойки. Используйте IsWarMode для проверки текущего состояния.

### Current Basic signatures / Return

- `UO.SetWarMode(Value:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetWarMode"]`

**Pascal compatibility signature:** `procedure SetWarMode(Value: Boolean);`

### Parameters

- `Value` — War-mode flag: TRUE/1 enters war mode; FALSE/0 leaves war mode.

### Accepted values / constants

- `Value` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetWarMode(TRUE)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetWarMode(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Value
    UO.SetWarMode(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Value
    UO.SetWarMode(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
