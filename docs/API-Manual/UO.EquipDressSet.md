# UO.EquipDressSet

ClassicUO • Runtime API • `UO.EquipDressSet.md`

## Точный синтаксис / Registered signatures

```text
UO.EquipDressSet() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.EquipDressSet`

### Current Basic signatures / Return

- `UO.EquipDressSet() -> Boolean`
  - **Return type:** `Boolean` (`1/0`)
  - **Return contract:** Returns `False` when no saved Stealth-compatible dress set exists; returns `True` when the saved set exists and equip/unequip requests were submitted.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Applies the saved compatibility dress set using the current Basic equip route and configured dress speed. The command no longer returns unconditional `True` when no dress set exists.

### Notes / limitations

`True` means the dress set existed and client requests were submitted. Final server-side equipment state can still be affected by shard restrictions, item movement, lag, or equipment rules.

### Examples

```basic
SUB Main()
    IF UO.EquipDressSet() THEN
        UO.Print('Dress request submitted')
    END IF
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.EquipDressSet()
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.EquipDressSet()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.EquipDressSet()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
