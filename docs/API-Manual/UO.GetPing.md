# UO.GetPing

ClassicUO • Runtime API • `UO.GetPing.md`

Без аргумента возвращает сохранённый ServerPing из статистики соединения. Форма с timeout инициирует проверку ping через клиентское соединение и ждёт ответ до указанного срока в миллисекундах. Не перепутайте с отдельной функцией ICMP Ping произвольного узла.

## Точный синтаксис / Registered signatures

```text
UO.GetPing() -> Integer
UO.GetPing(timeout:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetPing()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1000 # timeout
    VAR result = UO.GetPing(arg1)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.GetPing()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.GetPing()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GetPing`
