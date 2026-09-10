# UO.Press

ClassicUO • Runtime API • `UO.Press.md`

Эмулирует нажатие клавиши по Windows virtual-key коду. Необязательные count и delay задают число повторений и задержку после каждого нажатия: по умолчанию 1 и 105 мс. Press является алиасом KeyPress. Ввод получает активное окно ОС; команда сама не активирует клиент.

## Точный синтаксис / Registered signatures

```text
UO.Press(key:Integer) -> Unit
UO.Press(key:Integer, count:Integer) -> Unit
UO.Press(key:Integer, count:Integer, delay:Integer) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.Press(1)
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # key
    VAR arg2 = 2 # count
    VAR arg3 = 100 # delay
    UO.Press(arg1, arg2, arg3)
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    UO.Press(1, 2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 1 # key
        UO.Press(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 1 # key
    UO.Press(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.Press`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
