# UO.EquipLastWeapon

ClassicUO • Runtime API • `UO.EquipLastWeapon.md`

## Точный синтаксис / Registered signatures

```text
UO.EquipLastWeapon() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.EquipLastWeapon`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Надевает последнее ранее экипированное оружие. Полезно для быстрого переключения между двумя видами оружия одной командой. Примечание: Работает только с версией клиента 5.0 и выше.

### Current Basic signatures / Return

- `UO.EquipLastWeapon() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["EquipLastWeapon"]` → `BRIDGE CONTRACT -> IApiBridge.EquipLastWeapon`

**Pascal compatibility signature:** `procedure EquipLastWeapon;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.EquipLastWeapon()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.EquipLastWeapon()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.EquipLastWeapon()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.EquipLastWeapon()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
