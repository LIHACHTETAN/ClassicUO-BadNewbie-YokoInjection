# UO.TicksDead

ClassicUO • Runtime API • `UO.TicksDead.md`

При первом чтении в состоянии смерти сохраняет UO.Timer и возвращает эту метку. Это десятые доли секунды, не длительность с момента смерти; отсутствие зафиксированной смерти даёт 0.

## Точный синтаксис / Registered signatures

```text
UO.TicksDead() -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.TicksDead()
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.TicksDead()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.TicksDead()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.TicksDead`
