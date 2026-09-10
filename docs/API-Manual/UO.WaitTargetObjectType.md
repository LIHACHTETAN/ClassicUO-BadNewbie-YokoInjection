# UO.WaitTargetObjectType

ClassicUO • Runtime API • `UO.WaitTargetObjectType.md`

Готовит последовательность из двух целей: явно заданный объект id и найденный на земле предмет графики type/цвета color. Если один из объектов не найден, следующая автоматическая цель отменяется.

## Точный синтаксис / Registered signatures

```text
UO.WaitTargetObjectType(id:Any, type:Any) -> Unit
UO.WaitTargetObjectType(id:Any, type:Any, color:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.WaitTargetObjectType(self, 0x0EED)
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = self # id
    VAR arg2 = 0x0EED # type
    VAR arg3 = -1 # color
    UO.WaitTargetObjectType(arg1, arg2, arg3)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = self # id
        VAR arg2 = 0x0EED # type
        UO.WaitTargetObjectType(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = self # id
    VAR arg2 = 0x0EED # type
    UO.WaitTargetObjectType(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.WaitTargetObjectType`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
