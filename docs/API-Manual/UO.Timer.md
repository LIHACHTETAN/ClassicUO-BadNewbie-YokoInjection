# UO.Timer

ClassicUO • Runtime API • `UO.Timer.md`

Возвращает время с запуска runtime в десятых долях секунды как Integer. Разность 10 соответствует примерно одной секунде. Отличается от Timer() без UO., который возвращает секунды как Decimal. Значение ограничивается диапазоном Integer при очень долгой работе.

## Точный синтаксис / Registered signatures

```text
UO.Timer() -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Практический пример

```vb
SUB Main()
    VAR started = UO.Timer()
    wait(100)
    UO.Print(CStr(UO.Timer() - started))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.Timer()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.Timer()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.Timer`
