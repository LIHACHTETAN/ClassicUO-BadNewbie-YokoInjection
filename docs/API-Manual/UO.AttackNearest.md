# UO.AttackNearest

ClassicUO • Runtime API • `UO.AttackNearest.md`

Выбирает персонажа по notoriety и дополнительным фильтрам distance, body, maxZ, nearest, color, classMask, aliveOnly, visibleOnly, затем посылает запрос атаки. classMask сопоставляется с загруженным текстом имени, титула и экипировки, а не со скрытым серверным классом. Возвращаемое ненулевое значение — выбранный serial; 0 — подходящей цели нет. Поддерживается 1–9 аргументов.

## Точный синтаксис / Registered signatures

```text
UO.AttackNearest(notoriety:Any) -> Integer
UO.AttackNearest(notoriety:Any, distance:Any) -> Integer
UO.AttackNearest(notoriety:Any, distance:Any, body:Any) -> Integer
UO.AttackNearest(notoriety:Any, distance:Any, body:Any, maxZ:Any) -> Integer
UO.AttackNearest(notoriety:Any, distance:Any, body:Any, maxZ:Any, nearest:Any) -> Integer
UO.AttackNearest(notoriety:Any, distance:Any, body:Any, maxZ:Any, nearest:Any, color:Any) -> Integer
UO.AttackNearest(notoriety:Any, distance:Any, body:Any, maxZ:Any, nearest:Any, color:Any, classMask:Any) -> Integer
UO.AttackNearest(notoriety:Any, distance:Any, body:Any, maxZ:Any, nearest:Any, color:Any, classMask:Any, aliveOnly:Any) -> Integer
UO.AttackNearest(notoriety:Any, distance:Any, body:Any, maxZ:Any, nearest:Any, color:Any, classMask:Any, aliveOnly:Any, visibleOnly:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.AttackNearest(-1)
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 9 аргументов

```vb
SUB Main()
    VAR arg1 = -1 # notoriety
    VAR arg2 = 5 # distance
    VAR arg3 = -1 # body
    VAR arg4 = 4 # maxZ
    VAR arg5 = 1 # nearest
    VAR arg6 = -1 # color
    VAR arg7 = 7 # classMask
    VAR arg8 = 8 # aliveOnly
    VAR arg9 = 9 # visibleOnly
    VAR result = UO.AttackNearest(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.AttackNearest(-1, 5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.AttackNearest(-1, 5, -1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.AttackNearest(-1, 5, -1, 4)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    VAR result = UO.AttackNearest(-1, 5, -1, 4, 1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 6 аргументов

```vb
SUB Main()
    VAR result = UO.AttackNearest(-1, 5, -1, 4, 1, -1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 7 аргументов

```vb
SUB Main()
    VAR result = UO.AttackNearest(-1, 5, -1, 4, 1, -1, 7)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 8 аргументов

```vb
SUB Main()
    VAR result = UO.AttackNearest(-1, 5, -1, 4, 1, -1, 7, 8)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = -1 # notoriety
    VAR result = UO.AttackNearest(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = -1 # notoriety
    VAR result = UO.AttackNearest(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<RegisterCompactSearchApi>b__351_4`
