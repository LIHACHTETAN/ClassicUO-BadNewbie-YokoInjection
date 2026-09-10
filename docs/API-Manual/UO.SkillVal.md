# UO.SkillVal

ClassicUO • Runtime API • `UO.SkillVal.md`

## Точный синтаксис / Registered signatures

```text
UO.SkillVal(skill:Any, variant:Any) -> Integer
UO.SkillVal(skillName:String) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SkillVal`

### Direct runtime overloads

- `UO.SkillVal(skillName:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.

### Parameters

- `skillName` — Named runtime value (String); use the exact registered/saved name expected by SkillVal.

### Accepted values / constants

- `skillName` — Exact/case-insensitive skill name accepted by the runtime skill table, or the numeric/object alternative explicitly shown by the signature.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.SkillVal(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.SkillVal('Hiding')
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = 'Hiding' # skill
    VAR arg2 = 2 # variant
    VAR result = UO.SkillVal(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 'Hiding' # skillName
    VAR result = UO.SkillVal(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 'Hiding' # skillName
    VAR result = UO.SkillVal(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_12`
- `InjectionScript.Runtime.InjectionApiUO.SkillVal`
