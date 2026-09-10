# UO.BandageSelf

ClassicUO • Runtime API • `UO.BandageSelf.md`

## Точный синтаксис / Registered signatures

```text
UO.BandageSelf() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.BandageSelf`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Пытается использовать бинты на текущем персонаже. Метод ищет бинты (тип $0E21 ) в рюкзаке персонажа и, если находит, использует их с целью на самого себя. Если бинты не найдены, метод записывает сообщение об ошибке в системный журнал: "BandageSelf error: Bandages not found." . Примечание: Работает только с версией клиента 5.0.4 и выше.

### Current Basic signatures / Return

- `UO.BandageSelf() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["BandageSelf"]` → `BRIDGE CONTRACT -> IApiBridge.Self` → `BRIDGE CONTRACT -> IApiBridge.UseType` → `BRIDGE CONTRACT -> IApiBridge.WaitTargetObject`

**Pascal compatibility signature:** `procedure BandageSelf;`

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
    UO.BandageSelf()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.BandageSelf()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.BandageSelf()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.BandageSelf()
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.BandageSelf`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
