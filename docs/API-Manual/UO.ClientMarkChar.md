# UO.ClientMarkChar

ClassicUO • Runtime API • `UO.ClientMarkChar.md`

Обновляет клиентскую сохранённую цель: actionIndex=1 — LastTarget, 2 — LastAttack, 3 — обе. Другие значения сообщают об ошибке. Само обновление метки не атакует и не отвечает на серверный target.

## Точный синтаксис / Registered signatures

```text
UO.ClientMarkChar(actionIndex:Any, id:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.ClientMarkChar(0, self)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 0 # actionIndex
        VAR arg2 = self # id
        UO.ClientMarkChar(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 0 # actionIndex
    VAR arg2 = self # id
    UO.ClientMarkChar(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.ClientMarkChar`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
