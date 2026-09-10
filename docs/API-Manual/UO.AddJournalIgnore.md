# UO.AddJournalIgnore

ClassicUO • Runtime API • `UO.AddJournalIgnore.md`

Добавляет регистронезависимый текстовый фильтр в JournalManager самого ClassicUO. Утверждение исторической справки, будто фильтр действует только во внешнем Stealth, к этой реализации не относится.

## Точный синтаксис / Registered signatures

```text
UO.AddJournalIgnore(Str:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.AddJournalIgnore('example')
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 'example' # Str
    UO.AddJournalIgnore(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'example' # Str
    UO.AddJournalIgnore(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
