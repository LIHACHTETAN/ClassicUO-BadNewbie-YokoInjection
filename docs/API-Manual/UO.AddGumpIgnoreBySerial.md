# UO.AddGumpIgnoreBySerial

ClassicUO • Runtime API • `UO.AddGumpIgnoreBySerial.md`

## Точный синтаксис / Registered signatures

```text
UO.AddGumpIgnoreBySerial(Serial:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.AddGumpIgnoreBySerial`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Добавляет серийный номер гампа в список игнорируемых. Все входящие гампы с этим серийным номером будут молча проигнорированы — они не появятся в очереди гампов и не будут доступны через GetGumpsCount или GetGumpInfo . На некоторых шардах каждому гампу присваивается уникальный серийный номер, на других — нет. Проверьте поведение гампов на вашем шарде. Если гампы имеют только уникальные ID, используйте AddGumpIgnoreByID . Важно: Игнорирование гампа не отменяет его на стороне сервера. Сервер считает, что гамп получен и отображён, и может ожидать ответа. Используйте методы игнорирования с осторожностью. Для очистки всех игнорирований используйте ClearGumpsIgnore .

### Current Basic signatures / Return

- `UO.AddGumpIgnoreBySerial(Serial:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddGumpIgnoreBySerial"]` → `STATE -> InjectionApiState.IgnoredGumpSerials`

**Pascal compatibility signature:** `procedure AddGumpIgnoreBySerial(Serial: Cardinal);`

### Parameters

- `Serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `Serial` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.AddGumpIgnoreBySerial(self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.AddGumpIgnoreBySerial(self)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = self # Serial
    UO.AddGumpIgnoreBySerial(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = self # Serial
    UO.AddGumpIgnoreBySerial(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
