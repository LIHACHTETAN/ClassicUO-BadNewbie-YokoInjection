# UO.StopBoat

ClassicUO • Runtime API • `UO.StopBoat.md`

## Точный синтаксис / Registered signatures

```text
UO.StopBoat() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.StopBoat`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Останавливает лодку, которой правит персонаж. Эквивалент MoveBoat(0, 0) — отправляет HS-пакет управления (0xBF, субкоманда 0x33) со скоростью 0; направление в стоп-запросе сервер игнорирует. Требования те же, что и у MoveBoat : версия клиента в профиле 7.0.9.0+ , шард с поддержкой HS-управления мышью, на OSI/ServUO персонаж должен быть в pilot-режиме (за штурвалом).

### Current Basic signatures / Return

- `UO.StopBoat() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["StopBoat"]` → `BRIDGE CONTRACT -> IApiBridge.StopBoat`

**Pascal compatibility signature:** `procedure StopBoat;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.StopBoat()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.StopBoat()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.StopBoat()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.StopBoat()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
