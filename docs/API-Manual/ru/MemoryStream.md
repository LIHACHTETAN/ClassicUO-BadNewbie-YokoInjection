# MemoryStream

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Создаёт пустой двоичный поток в памяти для совместимых команд, например HTTP_Get(URL,stream).

## Точный синтаксис

```text
MemoryStream() -> Any
```

## Параметры

Параметров нет.

## Возвращает

Object MemoryStream, не Array и не строка. Его методы: Length()/Position() возвращают Integer размер/позицию в байтах; ReadByte() — 0..255 либо -1 в конце; ToArray() — Array Integer-байтов. Clear(), Rewind(), SaveToFile(fileName) возвращают Unit.

## Поведение

- Параметров конструктора нет. Clear обнуляет длину и позицию; Rewind ставит позицию на 0; ReadByte продвигает её на один байт при успехе.
- ToArray создаёт копию всех байтов независимо от позиции чтения. SaveToFile(fileName) полностью записывает эти байты в указанный файл, заменяя прежнее содержимое. Родительская папка должна существовать.
- Два отдельных MemoryStream() — разные объекты даже с одинаковыми байтами. Присваивание второй переменной сохраняет ссылку на тот же объект.

## Примеры

### Проверить пустой поток

```vb
# Проверить пустой поток
#
# Создаёт пустой двоичный поток в памяти для совместимых команд, например HTTP_Get(URL,stream).
#
# Object MemoryStream, не Array и не строка. Его методы: Length()/Position() возвращают Integer
# размер/позицию в байтах; ReadByte() — 0..255 либо -1 в конце; ToArray() — Array
# Integer-байтов. Clear(), Rewind(), SaveToFile(fileName) возвращают Unit.

SUB Main()
    # Аргументов нет; новый поток пуст.
    # Length() даёт 0, ReadByte() даёт -1. -1 не является допустимым байтом.

    VAR stream = MemoryStream()
    UO.Print(STR(stream.Length()))
    UO.Print(STR(stream.ReadByte()))
END SUB
```

**Разбор параметров и выполнения:**

- Аргументов нет; новый поток пуст.
- Length() даёт 0, ReadByte() даёт -1. -1 не является допустимым байтом.

### Получить двоичные данные по HTTP

```vb
# Получить двоичные данные по HTTP
#
# Создаёт пустой двоичный поток в памяти для совместимых команд, например HTTP_Get(URL,stream).
#
# Object MemoryStream, не Array и не строка. Его методы: Length()/Position() возвращают Integer
# размер/позицию в байтах; ReadByte() — 0..255 либо -1 в конце; ToArray() — Array
# Integer-байтов. Clear(), Rewind(), SaveToFile(fileName) возвращают Unit.

SUB Main()
    # HTTP_Get получает URL и объект stream. Используйте собственный нужный URL; при запуске этот
    # пример обращается в сеть.
    # ToArray возвращает копию байтов, не декодированный текст. Размер 0 сам по себе не подтверждает
    # успешный HTTP-ответ; учитывайте контракт HTTP_Get.

    VAR stream = MemoryStream()
    UO.HTTP_Get('https://example.com/', stream)
    VAR bytes = stream.ToArray()
    UO.Print('Downloaded bytes: ' + STR(GetArrayLength(bytes)))
END SUB
```

**Разбор параметров и выполнения:**

- HTTP_Get получает URL и объект stream. Используйте собственный нужный URL; при запуске этот пример обращается в сеть.
- ToArray возвращает копию байтов, не декодированный текст. Размер 0 сам по себе не подтверждает успешный HTTP-ответ; учитывайте контракт HTTP_Get.

### Перечитать первый байт и затем очистить

```vb
# Перечитать первый байт и затем очистить
#
# Создаёт пустой двоичный поток в памяти для совместимых команд, например HTTP_Get(URL,stream).
#
# Object MemoryStream, не Array и не строка. Его методы: Length()/Position() возвращают Integer
# размер/позицию в байтах; ReadByte() — 0..255 либо -1 в конце; ToArray() — Array
# Integer-байтов. Clear(), Rewind(), SaveToFile(fileName) возвращают Unit.

SUB Main()
    # После HTTP_Get проверяется наличие байтов перед чтением. Rewind возвращает позицию на начало.
    # Два чтения первого байта совпадают; Clear в конце удаляет все данные потока. Сам объект
    # остаётся пригодным для следующего запроса.

    VAR stream = MemoryStream()
    UO.HTTP_Get('https://example.com/', stream)
    IF stream.Length() > 0 THEN
        VAR first = stream.ReadByte()
        stream.Rewind()
        UO.Print(STR(first = stream.ReadByte()))
    END IF
    stream.Clear()
END SUB
```

**Разбор параметров и выполнения:**

- После HTTP_Get проверяется наличие байтов перед чтением. Rewind возвращает позицию на начало.
- Два чтения первого байта совпадают; Clear в конце удаляет все данные потока. Сам объект остаётся пригодным для следующего запроса.
