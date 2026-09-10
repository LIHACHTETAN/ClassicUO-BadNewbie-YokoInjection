# messagebox

ClassicUO • Runtime API • `messagebox.md`

Печатает строку через клиентский bridge. messagebox является совместимым именем message и не открывает модальный диалог.

Compatibility alias of message: prints through the client bridge; it does not open a modal dialog.

## Точный синтаксис / Registered signatures

```text
messagebox(text:String) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Практический пример

```vb
SUB Main()
    messagebox('Hello')
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 'example' # text
        messagebox(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 'example' # text
    messagebox(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApi.Message`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
