# UO.GListSet

ClassicUO • Runtime API • `UO.GListSet.md`

Добавляет пару имя/значение в локальный GList или заменяет значение уже существующего имени. Сравнение имён регистронезависимое.

## Точный синтаксис / Registered signatures

```text
UO.GListSet(nameValue:Any, value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Сохранить число

```vb
SUB Main()
    UO.GListSet('count', 5)
    UO.Print(CStr(UO.GListGet('count')))
END SUB
```

### Заменить значение без учёта регистра

```vb
SUB Main()
    UO.GListSet('count', 5)
    UO.GListSet('COUNT', 8)
    UO.Print(CStr(UO.GListGet('count')))
END SUB
```

### Сохранить строку

```vb
SUB Main()
    UO.GListSet('route_name', 'home')
    UO.Print(CStr(UO.GListGet('route_name')))
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 1 # nameValue
        VAR arg2 = 2 # value
        UO.GListSet(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 1 # nameValue
    VAR arg2 = 2 # value
    UO.GListSet(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GListSet`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
