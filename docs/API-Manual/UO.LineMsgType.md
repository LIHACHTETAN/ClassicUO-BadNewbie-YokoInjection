# UO.LineMsgType

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->

Возвращает тип сетевого сообщения выбранной записи журнала.

## Точный синтаксис

```text
UO.LineMsgType() -> Any
```

Выберите одну из зарегистрированных форм. Параметры передаются позиционно. Any означает значение BASIC с преобразованием внутри команды; Unit — отсутствие возвращаемого значения.

## Параметры

Параметров нет.

## Возвращает

Integer — код MessageType: 0 Regular, 1 System, 2 Emote, 3 Limit3Spell, 6 Label, 7 Focus, 8 Whisper, 9 Yell, 10 Spell, 13 Guild, 14 Alliance, 15 Command, 16 GmChat, 192 Encoded, 255 Party. Без выбора 0. Это коды Classic UO; не заменяйте их отличающимися числами из сторонних примеров.

## Поведение

- Поиск и Journal/GetJournal/LastJournalMessage сохраняют текст и поля одной записи в текущем скрипте. Новые сообщения не подменяют эти поля. Если запись вытеснена из ограниченного журнала, сохранённые поля остаются, но LineIndex/GetFoundedTextIndex возвращают -1. Следующий поиск или чтение выбирает другую запись; неудачный поиск, неверный индекс и очистка через этот скрипт сбрасывают выбор.
- Getter не запускает поиск и не выбирает самую новую строку. Нулевые/пустые значения могут быть действующими данными; учитывайте результат поиска.
- Первичный справочник: https://stealth.od.ua/api/LineMsgType/ .

## Примеры

### Пример 1. Читать поле после поиска

```vb
# Читать поле после поиска
#
# Возвращает тип сетевого сообщения выбранной записи журнала.
#
# Integer — код MessageType: 0 Regular, 1 System, 2 Emote, 3 Limit3Spell, 6 Label, 7 Focus, 8
# Whisper, 9 Yell, 10 Spell, 13 Guild, 14 Alliance, 15 Command, 16 GmChat, 192 Encoded, 255
# Party. Без выбора 0. Это коды Classic UO; не заменяйте их отличающимися числами из сторонних
# примеров.

SUB Main()
    # notice — пример искомого текста. Getter вызывается без параметров только после успешного
    # поиска.
    # Integer — код MessageType: 0 Regular, 1 System, 2 Emote, 3 Limit3Spell, 6 Label, 7 Focus, 8
    # Whisper, 9 Yell, 10 Spell, 13 Guild, 14 Alliance, 15 Command, 16 GmChat, 192 Encoded, 255
    # Party. Без выбора 0. Это коды Classic UO; не заменяйте их отличающимися числами из сторонних
    # примеров.

    IF UO.InJournal('notice') > 0 THEN
        VAR value = UO.LineMsgType()
        UO.Print('Message type: ' + STR(value))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- notice — пример искомого текста. Getter вызывается без параметров только после успешного поиска.
- Integer — код MessageType: 0 Regular, 1 System, 2 Emote, 3 Limit3Spell, 6 Label, 7 Focus, 8 Whisper, 9 Yell, 10 Spell, 13 Guild, 14 Alliance, 15 Command, 16 GmChat, 192 Encoded, 255 Party. Без выбора 0. Это коды Classic UO; не заменяйте их отличающимися числами из сторонних примеров.

### Пример 2. Прочитать поле конкретной строки

```vb
# Прочитать поле конкретной строки
#
# Возвращает тип сетевого сообщения выбранной записи журнала.
#
# Integer — код MessageType: 0 Regular, 1 System, 2 Emote, 3 Limit3Spell, 6 Label, 7 Focus, 8
# Whisper, 9 Yell, 10 Spell, 13 Guild, 14 Alliance, 15 Command, 16 GmChat, 192 Encoded, 255
# Party. Без выбора 0. Это коды Classic UO; не заменяйте их отличающимися числами из сторонних
# примеров.

SUB Main()
    # Journal(0) выбирает новую запись. index и value читаются до Print.
    # Проверка index позволяет отличить отсутствие записи от допустимого нулевого или пустого поля.

    VAR text = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR value = UO.LineMsgType()
    IF index >= 0 THEN
        UO.Print(STR(value))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- Journal(0) выбирает новую запись. index и value читаются до Print.
- Проверка index позволяет отличить отсутствие записи от допустимого нулевого или пустого поля.

### Пример 3. Сохранить поле перед следующим поиском

```vb
# Сохранить поле перед следующим поиском
#
# Возвращает тип сетевого сообщения выбранной записи журнала.
#
# Integer — код MessageType: 0 Regular, 1 System, 2 Emote, 3 Limit3Spell, 6 Label, 7 Focus, 8
# Whisper, 9 Yell, 10 Spell, 13 Guild, 14 Alliance, 15 Command, 16 GmChat, 192 Encoded, 255
# Party. Без выбора 0. Это коды Classic UO; не заменяйте их отличающимися числами из сторонних
# примеров.

SUB Main()
    # Первый поиск выбирает success, второй заменяет или сбрасывает выбор. saved уже содержит копию
    # нужного поля.
    # Сохранённая VAR не меняется при новом поиске, очистке или поступлении сообщений.

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.LineMsgType()
        VAR nextMatch = UO.InJournal('failed')
        UO.Print('Saved: ' + STR(saved))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- Первый поиск выбирает success, второй заменяет или сбрасывает выбор. saved уже содержит копию нужного поля.
- Сохранённая VAR не меняется при новом поиске, очистке или поступлении сообщений.
