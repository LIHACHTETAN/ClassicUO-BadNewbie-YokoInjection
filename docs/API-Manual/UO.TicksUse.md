# UO.TicksUse

ClassicUO • Runtime API • `UO.TicksUse.md`

Возвращает сохранённую метку UO.Timer для применения объекта. Единица — десятая доля секунды.

## Точный синтаксис / Registered signatures

```text
UO.TicksUse() -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.TicksUse()
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.TicksUse()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.TicksUse()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.TicksUse`
