# UO.UsePrimaryAbility

ClassicUO • Runtime API • `UO.UsePrimaryAbility.md`

## Точный синтаксис / Registered signatures

```text
UO.UsePrimaryAbility() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UsePrimaryAbility`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Активирует основную способность оружия (primary ability) текущего экипированного оружия. Не выполняет действий, если персонаж не подключён. Используйте GetActiveAbility для проверки текущей активной способности, и IsActiveSpellAbility для проверки активности заклинательной способности.

### Current Basic signatures / Return

- `UO.UsePrimaryAbility() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UsePrimaryAbility"]` → `BRIDGE CONTRACT -> IApiBridge.UsePrimaryAbility`

**Pascal compatibility signature:** `procedure UsePrimaryAbility;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.UsePrimaryAbility()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.UsePrimaryAbility()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.UsePrimaryAbility()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.UsePrimaryAbility()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
