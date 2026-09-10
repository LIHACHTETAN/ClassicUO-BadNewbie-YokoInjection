# UO.SetEventProc

ClassicUO • Runtime API • `UO.SetEventProc.md`

## Точный синтаксис / Registered signatures

```text
UO.SetEventProc(Eventname:Any, Procname:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetEventProc`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Регистрирует (или снимает) процедуру скрипта как обработчик определённого игрового события. Eventname — тип события, TPacketEvent . Procname — имя процедуры в скрипте для вызова при наступлении события. Передайте пустую строку '' для снятия обработчика. Если обработчик уже назначен — выводится предупреждение. Сначала снимите старый: SetEventProc(event, '') , затем установите новый. Ряд устаревших имён событий вызывает предупреждение (см. таблицу выше). В Python типы событий доступны как члены перечисления EventType (автоимпорт), второй параметр принимает ссылку на функцию или None для снятия. Полный список типов событий, сигнатуры обработчиков и описание параметров callback-ов — в мануале по событиям .

### Current Basic signatures / Return

- `UO.SetEventProc(Eventname:EventName, Procname:ProcedureName) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetEventProc"]`

**Pascal compatibility signature:** `procedure SetEventProc(Eventname: TPacketEvent; Procname: String);`

### Parameters

- `Eventname` — Current Basic compatibility event identifier.
- `Procname` — Loaded Basic SUB name to execute; an empty string unregisters the handler.
### Accepted values / constants

- `Eventname` — Current Basic compatibility events: SeeNewPlayer, Death, ChangeHitPoints, ChangeMana, ChangeStamina; optional leading ev; other historical TPacketEvent names are rejected.
- `Procname` — Loaded zero-argument Basic SUB name; empty string unregisters the handler.

### Defaults / omitted arguments

Both parameters are required. Procname='' unregisters the handler; a non-empty Procname registers a repeating handler for a supported current Basic event.

### Behavior

Registers a repeating handler through the same live-state event engine as `UO.SetEvent`. `Procname=''` unregisters the event. Registration does not execute the handler immediately; the handler is evaluated on subsequent `UO.Wait` yields when the documented event transition occurs.
### Notes / limitations

This Basic compatibility route does **not** claim the complete historical Stealth `TPacketEvent` callback surface. The current supported event names are `SeeNewPlayer`, `Death`, `ChangeHitPoints`, `ChangeMana`, and `ChangeStamina` (case-insensitive; optional leading `ev` is accepted). Unsupported names are rejected with a system message instead of being silently registered. The handler must be a loaded zero-argument Basic SUB.
### Examples

```basic
SUB Main()
    UO.SetEventProc('ChangeHitPoints', 'OnHpChange')
END SUB
```

```basic
SUB Main()
    UO.SetEventProc('ChangeHitPoints', '')
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetEventProc(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Eventname
    VAR arg2 = 2 # Procname
    UO.SetEventProc(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Eventname
    VAR arg2 = 2 # Procname
    UO.SetEventProc(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
