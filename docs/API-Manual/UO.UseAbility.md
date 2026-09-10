# UO.UseAbility

ClassicUO • Runtime API • `UO.UseAbility.md`

Активирует способность оружия по её имени или числовому ID. CastAbility является алиасом UseAbility. Возвращает 0 при неверном ID/отсутствии персонажа; принятие запроса не гарантирует успешный удар на сервере.

## Точный синтаксис / Registered signatures

```text
UO.UseAbility(abilityId:Integer) -> Integer
UO.UseAbility(abilityName:String) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.UseAbility('example')
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 'example' # abilityName
    VAR result = UO.UseAbility(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 'example' # abilityName
    VAR result = UO.UseAbility(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.UseAbility`
