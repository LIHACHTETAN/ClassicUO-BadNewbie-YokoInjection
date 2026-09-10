# UO.InfoColor

ClassicUO • Runtime API • `UO.InfoColor.md`

Выводит цвет объекта в журнал в шестнадцатеричном виде 0xHHHH. Без аргумента используется lasttarget; возвращаемого значения нет.

## Точный синтаксис / Registered signatures

```text
UO.InfoColor() -> Unit
UO.InfoColor(object:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Практический пример

```vb
SUB Main()
    UO.InfoColor(self)
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = self # object
    UO.InfoColor(arg1)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.InfoColor()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.InfoColor()
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass66_0.<RegisterLegacyManualAliases>b__1`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
