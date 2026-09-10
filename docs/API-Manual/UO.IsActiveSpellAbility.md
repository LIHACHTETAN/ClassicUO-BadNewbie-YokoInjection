# UO.IsActiveSpellAbility

ClassicUO • Runtime API • `UO.IsActiveSpellAbility.md`

## Точный синтаксис / Registered signatures

```text
UO.IsActiveSpellAbility(SpellName:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.IsActiveSpellAbility`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если указанное заклинание или способность в данный момент активны на персонаже, иначе False . Pascal: SpellName — название заклинания строкой (например, 'Cunning' , 'Bless' ). Пробелы в имени автоматически заменяются на подчёркивания. Если имя не распознано, в системный журнал записывается ошибка: "ActiveSpellAbility error: unknown spell name" . Python: SpellID — индекс заклинания в виде целого числа. Также можно использовать значения из перечисления Spell (см. ConstantsAndEnums ). Возвращает False , если персонаж не подключён.

### Current Basic signatures / Return

- `UO.IsActiveSpellAbility(SpellName:Integer) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsActiveSpellAbility"]` → `BRIDGE CONTRACT -> IApiBridge.IsActiveSpell`

**Pascal compatibility signature:** `function IsActiveSpellAbility(SpellName: String): Boolean;`

### Parameters

- `SpellName` — Named runtime value (Integer); use the exact registered/saved name expected by IsActiveSpellAbility.

### Accepted values / constants

- `SpellName` — Registered spell name or numeric spell ID, matching the overload form.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.IsActiveSpellAbility('Recall')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.IsActiveSpellAbility('Heal')
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 'Heal' # SpellName
    VAR result = UO.IsActiveSpellAbility(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'Heal' # SpellName
    VAR result = UO.IsActiveSpellAbility(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
