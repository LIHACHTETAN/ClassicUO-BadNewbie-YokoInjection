# UO.RemoveRing

ClassicUO • Runtime API • `UO.RemoveRing.md`

Снимает предмет со слоя Ring через Unequip.

## Точный синтаксис / Registered signatures

```text
UO.RemoveRing() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.RemoveRing()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.RemoveRing()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.RemoveRing()
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
