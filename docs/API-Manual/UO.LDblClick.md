# UO.LDblClick

ClassicUO • Runtime API • `UO.LDblClick.md`

Перемещает указатель к x,y и эмулирует левый/правый одиночный/двойной щелчок согласно имени команды. Координаты относятся к окну клиента, а не клеткам игрового мира.

## Точный синтаксис / Registered signatures

```text
UO.LDblClick(x:Integer, y:Integer) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.LDblClick(UO.GetX(), UO.GetY())
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = UO.GetX() # x
        VAR arg2 = UO.GetY() # y
        UO.LDblClick(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = UO.GetX() # x
    VAR arg2 = UO.GetY() # y
    UO.LDblClick(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.LDblClick`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
