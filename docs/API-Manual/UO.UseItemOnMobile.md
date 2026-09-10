# UO.UseItemOnMobile

ClassicUO • Runtime API • `UO.UseItemOnMobile.md`

## Точный синтаксис / Registered signatures

```text
UO.UseItemOnMobile(ItemSerial:Any, TargetSerial:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UseItemOnMobile`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Использует предмет непосредственно на мобайле (цели) без необходимости курсора цели. ItemSerial — serial (ID) используемого предмета. TargetSerial — serial (ID) мобайла-цели. Это однопакетная операция, объединяющая «использование предмета» и «нацеливание на мобайла» в одно действие. Быстрее традиционной последовательности «использовать → нацелить». Требуется версия клиента 5.0.4 или выше. При более старой версии логируется ошибка и вызов игнорируется. Оба объекта (предмет и мобайл-цель) должны существовать, иначе логируется ошибка. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.UseItemOnMobile(ItemSerial:Integer, TargetSerial:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseItemOnMobile"]` → `BRIDGE CONTRACT -> IApiBridge.UseObject` → `BRIDGE CONTRACT -> IApiBridge.WaitTargetObject`

**Pascal compatibility signature:** `procedure UseItemOnMobile(ItemSerial: Cardinal; TargetSerial: Cardinal);`

### Parameters

- `ItemSerial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `TargetSerial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `ItemSerial` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `TargetSerial` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.UseItemOnMobile(1000, self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.UseItemOnMobile(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # ItemSerial
    VAR arg2 = 2 # TargetSerial
    UO.UseItemOnMobile(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ItemSerial
    VAR arg2 = 2 # TargetSerial
    UO.UseItemOnMobile(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
