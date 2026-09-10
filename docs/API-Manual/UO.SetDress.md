# UO.SetDress

ClassicUO • Runtime API • `UO.SetDress.md`

## Точный синтаксис / Registered signatures

```text
UO.SetDress() -> Unit
UO.SetDress(name:String) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetDress`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Сохраняет текущий набор экипировки персонажа как «dress set» (набор одежды/экипировки). Фиксирует все предметы, экипированные на персонаже во всех действующих слоях экипировки, и сохраняет их как активную конфигурацию одежды. Сохранённый набор может быть впоследствии заново надет с помощью методов Equip или EquipItems после снятия экипировки. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.SetDress() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetDress"]`

**Pascal compatibility signature:** `procedure SetDress;`

### Additional current runtime overloads

- `UO.SetDress(name:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `name` — Named runtime value (String); use the exact registered/saved name expected by SetDress.

### Accepted values / constants

- `name` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 0, 1. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetDress()
END SUB
```

```basic
SUB Main()
    UO.SetDress(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetDress()
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 'example' # name
    UO.SetDress(arg1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.SetDress()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.SetDress()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.SetDress`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
