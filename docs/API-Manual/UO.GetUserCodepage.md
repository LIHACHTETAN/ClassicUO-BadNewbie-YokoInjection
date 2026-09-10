# UO.GetUserCodepage

ClassicUO • Runtime API • `UO.GetUserCodepage.md`

Возвращает CodePage кодировки Encoding.Default текущего .NET runtime. Это не переключатель языка клиента и не обещание Windows ANSI-кодировки; современный .NET обычно возвращает UTF-8 (65001).

## Точный синтаксис / Registered signatures

```text
UO.GetUserCodepage() -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetUserCodepage()
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.GetUserCodepage()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.GetUserCodepage()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GetUserCodepage`
