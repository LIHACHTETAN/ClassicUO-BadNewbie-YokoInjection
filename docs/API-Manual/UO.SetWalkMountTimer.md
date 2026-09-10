# UO.SetWalkMountTimer

ClassicUO • Runtime API • `UO.SetWalkMountTimer.md`

## Точный синтаксис / Registered signatures

```text
UO.SetWalkMountTimer(Value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetWalkMountTimer`

### Current Basic signatures / Return

- `UO.SetWalkMountTimer(Value:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The active Basic movement timing is updated immediately.

### Parameters

- `Value` — movement step timing in milliseconds, clamped to `10..2000`.

### Accepted values / constants

- `Value` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Sets the ClassicUO player movement completion delay used when **walking while mounted**. The value is propagated from Basic runtime state into `MovementSpeed.TimeToCompleteMovement`; it is no longer a state-only compatibility variable.

Default compatibility value: `200` ms.

### Notes / limitations

- Extremely small values can still be limited in practice by server movement acknowledgements/denials and network latency.
- This changes the local Basic/ClassicUO movement timing policy; it cannot force a shard to accept movement faster than the server protocol permits.

### Examples

```basic
SUB Main()
    UO.SetWalkMountTimer(200)
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetWalkMountTimer(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Value
    UO.SetWalkMountTimer(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Value
    UO.SetWalkMountTimer(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
