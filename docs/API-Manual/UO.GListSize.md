# UO.GListSize

ClassicUO • Runtime API • `UO.GListSize.md`

Возвращает количество пар имя/значение в локальном GList.

## Точный синтаксис / Registered signatures

```text
UO.GListSize() -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GListSize()
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.GListSize()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.GListSize()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GListSize`
