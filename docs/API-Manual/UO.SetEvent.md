# UO.SetEvent

ClassicUO • Runtime API • `UO.SetEvent.md`

## Точный синтаксис / Registered signatures

```text
UO.SetEvent(name:Any, stateValue:Any) -> Unit
UO.SetEvent(name:Any, stateValue:Any, repeatOrHandler:Any) -> Unit
UO.SetEvent(nameValue:Any, stateValue:Any, repeatValue:Any, subNameValue:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetEvent`

### Direct runtime overloads

- `UO.SetEvent(eventName:String, enabled:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
- `UO.SetEvent(eventName:String, enabled:Boolean, repeatOrHandler:Boolean|ProcedureName) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
- `UO.SetEvent(eventName:String, enabled:Boolean, repeat:Boolean, handler:ProcedureName) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.

### Parameters

- `eventName` — Legacy event identifier to monitor.
- `enabled` — Enables/registers (`TRUE/1`) or disables/unregisters (`FALSE/0`) the event.
- `repeatOrHandler` — Third-argument compatibility union: repeat flag or handler SUB string.
- `repeat` — Explicit one-shot/repeating flag in the four-argument form.
- `handler` — Loaded Basic SUB name to execute when the event fires.
### Accepted values / constants

- `eventName` — Legacy Basic event name: SeeNewPlayer, Death, ChangeHitPoints, ChangeMana, or ChangeStamina (case-insensitive; optional leading ev is normalized).
- `enabled` — TRUE/FALSE or 1/0.
- `repeatOrHandler` — TRUE/FALSE or 1/0 repeat flag; alternatively a SUB name or historical `exec <SUB>` / `_exec <SUB>` handler string.
- `repeat` — FALSE/0 = one-shot; TRUE/1 = remain armed after each matching event.
- `handler` — Loaded Basic SUB name, or historical `exec <SUB>` / `_exec <SUB>` form.

### Defaults / omitted arguments

Two arguments register/enable state tracking with repeat enabled but no handler. In the 3-argument form a non-numeric third value is the handler with repeat enabled; numeric/Boolean third value is the repeat flag. The 4-argument form explicitly supplies repeat and handler. enabled=FALSE unregisters the event.

### Behavior

Registers or removes a legacy Basic event handler. Registration captures the current state and does **not** execute the handler immediately. Supported live events are `SeeNewPlayer`, `Death`, `ChangeHitPoints`, `ChangeMana`, and `ChangeStamina`; they are evaluated while the script yields through `UO.Wait`. `repeat=FALSE/0` is one-shot and is automatically disabled after the first matching transition; `repeat=TRUE/1` remains armed. For historical compatibility, a non-numeric third argument such as `'exec OnChange'` is treated as the handler name and enables repeating mode.
### Notes / limitations

`enabled=FALSE/0` unregisters the event. Handler strings may be a SUB name or the historical `exec <SUB>` / `_exec <SUB>` form. The handler runs only if that SUB exists. `SeeNewPlayer` fires when a newly loaded non-self mobile appears relative to the registration/previous poll snapshot. Change events fire only on value transitions; `Death` fires on the alive-to-dead transition. Event dispatch is guarded against recursive re-entry while a handler is executing.
### Examples

```basic
SUB Main()
    UO.SetEvent('ChangeHitPoints', TRUE, TRUE, 'OnHpChange')
END SUB
```

```basic
SUB Main()
    UO.SetEvent('SeeNewPlayer', TRUE, 'exec OnPlayer')
END SUB
```

```basic
SUB Main()
    UO.SetEvent('ChangeMana', FALSE)
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetEvent('example', 2)
END SUB
```

### Расширенная перегрузка: 4 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # nameValue
    VAR arg2 = 2 # stateValue
    VAR arg3 = 3 # repeatValue
    VAR arg4 = 4 # subNameValue
    UO.SetEvent(arg1, arg2, arg3, arg4)
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    UO.SetEvent('example', 2, 3)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 'example' # name
        VAR arg2 = 2 # stateValue
        UO.SetEvent(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 'example' # name
    VAR arg2 = 2 # stateValue
    UO.SetEvent(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.SetEvent`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
