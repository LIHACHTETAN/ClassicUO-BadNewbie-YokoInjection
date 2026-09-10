# UO.SetMulPath

ClassicUO • Runtime API • `UO.SetMulPath.md`

Сохраняет строку mulPath в состоянии этого runtime. Это поле не используется для переключения игровых данных: команда не перезагружает MUL и не меняет settings.json. Настройте путь к игре через конфигурацию клиента.

## Точный синтаксис / Registered signatures

```text
UO.SetMulPath(pathValue:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetMulPath('C:/UltimaOnline')
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 'C:/UltimaOnline' # pathValue
        UO.SetMulPath(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 'C:/UltimaOnline' # pathValue
    UO.SetMulPath(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.SetMulPath`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
