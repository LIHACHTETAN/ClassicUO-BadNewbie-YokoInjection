# UO.UseSecondaryAbility

ClassicUO • Runtime API • `UO.UseSecondaryAbility.md`

## Точный синтаксис / Registered signatures

```text
UO.UseSecondaryAbility() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UseSecondaryAbility`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Активирует вторичную способность оружия (secondary ability) текущего экипированного оружия. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.UseSecondaryAbility() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseSecondaryAbility"]` → `BRIDGE CONTRACT -> IApiBridge.UseSecondaryAbility`

**Pascal compatibility signature:** `procedure UseSecondaryAbility;`

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
    UO.UseSecondaryAbility()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.UseSecondaryAbility()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.UseSecondaryAbility()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.UseSecondaryAbility()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
