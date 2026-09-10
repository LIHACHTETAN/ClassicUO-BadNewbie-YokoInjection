# UO.SubExists

ClassicUO • Runtime API • `UO.SubExists.md`

Возвращает 1, если менеджер Basic находит процедуру с заданным именем, иначе 0. Наличие процедуры не означает, что она уже выполняется.

## Точный синтаксис / Registered signatures

```text
UO.SubExists(subrutineName:String) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.SubExists('example')
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 'example' # subrutineName
    VAR result = UO.SubExists(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 'example' # subrutineName
    VAR result = UO.SubExists(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.SubExists`
