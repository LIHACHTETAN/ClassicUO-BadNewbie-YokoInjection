# UO.MoveBoat

ClassicUO • Runtime API • `UO.MoveBoat.md`

## Точный синтаксис / Registered signatures

```text
UO.MoveBoat(Direction:Any, Speed:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.MoveBoat`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Управляет лодкой, которой правит персонаж, через пакетное HS-управление (тот же механизм, что и управление мышью в официальном клиенте; пакет 0xBF, субкоманда 0x33). Direction — абсолютное мировое направление (0–7): 0 — север, 1 — северо-восток, 2 — восток, 3 — юго-восток, 4 — юг, 5 — юго-запад, 6 — запад, 7 — северо-запад. Сервер сам разворачивает лодку, если запрошенное направление отличается от текущего курса — отдельная команда «поворот» не нужна. Speed : 0 — стоп, 1 — медленно, 2 — быстро. Значения больше 2 обрезаются до 2. Лодка продолжает плыть в заданном направлении, пока не будет вызван StopBoat (или MoveBoat(dir, 0) ), не сменится направление или лодка не упрётся в препятствие. Метод работает только при выполнении условий: Версия клиента в профиле 7.0.9.0 или выше (High Seas). На более старой версии вызов лишь пишет предупреждение в системный журнал. Шард поддерживает HS-управление мышью. На OSI и ServUO-шардах персонаж должен сначала взять штурвал (pilot-режим — двойной клик по штурвалу / контекстное меню). Шарды на ModernUO этот пакет не реализуют вовсе (лодки там управляются только речевыми командами).

### Current Basic signatures / Return

- `UO.MoveBoat(Direction:Integer, Speed:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MoveBoat"]` → `BRIDGE CONTRACT -> IApiBridge.MoveBoat`

**Pascal compatibility signature:** `procedure MoveBoat(Direction, Speed : Byte);`

### Parameters

- `Direction` — Ultima Online movement/facing direction value.
- `Speed` — Boat speed enum: 0=stop, 1=slow, 2=fast; values above 2 are clamped to 2.

### Accepted values / constants

- `Direction` — 0=N, 1=NE, 2=E, 3=SE, 4=S, 5=SW, 6=W, 7=NW; string aliases only where Behavior lists them.
- `Speed` — Boat speed enum: 0=stop, 1=slow, 2=fast; values above 2 are clamped to 2.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.MoveBoat(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.MoveBoat(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Direction
    VAR arg2 = 2 # Speed
    UO.MoveBoat(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Direction
    VAR arg2 = 2 # Speed
    UO.MoveBoat(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
