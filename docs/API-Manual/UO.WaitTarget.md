# UO.WaitTarget

ClassicUO • Runtime API • `UO.WaitTarget.md`

Компактный выбор автоматической цели. Конкретный serial/именованный объект ставится в очередь напрямую. Значения 0 и -1 включают поиск по загруженным персонажам/предметам с фильтрами type, color, distance, notoriety, nearest и maxZ; учитывается Ignore. При отсутствии совпадения подготовленная цель очищается. Команда не начинает каст или применение предмета.

## Точный синтаксис / Registered signatures

```text
UO.WaitTarget(target:Any) -> Unit
UO.WaitTarget(target:Any, type:Any) -> Unit
UO.WaitTarget(target:Any, type:Any, color:Any) -> Unit
UO.WaitTarget(target:Any, type:Any, color:Any, distance:Any) -> Unit
UO.WaitTarget(target:Any, type:Any, color:Any, distance:Any, notoriety:Any) -> Unit
UO.WaitTarget(target:Any, type:Any, color:Any, distance:Any, notoriety:Any, nearest:Any) -> Unit
UO.WaitTarget(target:Any, type:Any, color:Any, distance:Any, notoriety:Any, nearest:Any, maxZ:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Практический пример

```vb
SUB Main()
    UO.WaitTarget(self)
END SUB
```

### Расширенная перегрузка: 7 аргументов

```vb
SUB Main()
    VAR arg1 = self # target
    VAR arg2 = 0x0EED # type
    VAR arg3 = -1 # color
    VAR arg4 = 5 # distance
    VAR arg5 = -1 # notoriety
    VAR arg6 = 1 # nearest
    VAR arg7 = 7 # maxZ
    UO.WaitTarget(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    UO.WaitTarget(self, 0x0EED)
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    UO.WaitTarget(self, 0x0EED, -1)
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    UO.WaitTarget(self, 0x0EED, -1, 5)
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    UO.WaitTarget(self, 0x0EED, -1, 5, -1)
END SUB
```

### Перегрузка: 6 аргументов

```vb
SUB Main()
    UO.WaitTarget(self, 0x0EED, -1, 5, -1, 1)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = self # target
        UO.WaitTarget(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = self # target
    UO.WaitTarget(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_19`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
