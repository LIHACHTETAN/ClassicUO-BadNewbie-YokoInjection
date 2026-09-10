# UO.ReceiveObjectName

ClassicUO • Runtime API • `UO.ReceiveObjectName.md`

Посылает одиночный клик по объекту для запроса имени. Если задан timeout, ждёт появления непустого имени до этого срока с проверкой не реже 25 мс; timeout в миллисекундах. Без второго аргумента длительного ожидания нет. Команда ничего не возвращает; имя читайте через GetName.

## Точный синтаксис / Registered signatures

```text
UO.ReceiveObjectName(id:Any) -> Unit
UO.ReceiveObjectName(id:Any, timeout:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.ReceiveObjectName(self)
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = self # id
    VAR arg2 = 1000 # timeout
    UO.ReceiveObjectName(arg1, arg2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = self # id
        UO.ReceiveObjectName(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = self # id
    UO.ReceiveObjectName(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.ReceiveObjectName`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
