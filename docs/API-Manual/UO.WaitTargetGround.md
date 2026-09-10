# UO.WaitTargetGround

ClassicUO • Runtime API • `UO.WaitTargetGround.md`

Ищет загруженный предмет на земле по графике и необязательному цвету, затем ставит его serial в очередь target. Это поиск предмета, не статического тайла карты. При отсутствии результата отменяет следующий автоматический ответ.

## Точный синтаксис / Registered signatures

```text
UO.WaitTargetGround(type:Any) -> Unit
UO.WaitTargetGround(type:Any, color:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.WaitTargetGround(0x0EED)
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR arg2 = -1 # color
    UO.WaitTargetGround(arg1, arg2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 0x0EED # type
        UO.WaitTargetGround(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 0x0EED # type
    UO.WaitTargetGround(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.WaitTargetGround`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
