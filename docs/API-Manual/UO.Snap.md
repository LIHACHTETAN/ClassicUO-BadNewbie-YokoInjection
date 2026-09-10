# UO.Snap

ClassicUO • Runtime API • `UO.Snap.md`

Сохраняет снимок клиента через TakeScreenshot. Без аргументов выбираются стандартное имя, quality=100 и includeUi=1. quality ограничивается 1–100; includeUi определяет включение интерфейса. Возвращает результат клиентской операции сохранения.

## Точный синтаксис / Registered signatures

```text
UO.Snap() -> Integer
UO.Snap(file:Any, quality:Any, includeUI:Any) -> Integer
UO.Snap(name:String) -> Integer
UO.Snap(name:String, quality:Integer) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.Snap()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = 'example.txt' # file
    VAR arg2 = 2 # quality
    VAR arg3 = 3 # includeUI
    VAR result = UO.Snap(arg1, arg2, arg3)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 1 аргументов

```vb
SUB Main()
    VAR result = UO.Snap('example')
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.Snap('example', 2)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.Snap()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.Snap()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_13`
- `InjectionScript.Runtime.InjectionApiUO.Snap`
