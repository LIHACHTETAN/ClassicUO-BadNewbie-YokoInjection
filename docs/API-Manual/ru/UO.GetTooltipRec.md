# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Читает структурированные свойства: cliloc ID и параметры каждой записи OPL.

## Точный синтаксис

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## Параметры

- `ObjID` — Обязательный serial/ID объекта, не type и не cliloc. Допускается Integer, десятичная/hex-строка, self, backpack, lasttarget, finditem или имя AddObject. 0 означает отсутствие объекта.

## Возвращает

Array<Array> — отдельный снимок строк свойств. Каждая строка равна [clilocID:Integer, parameters:Array<String>]. rows[i][0] — номер локализованного сообщения, rows[i][1] — массив параметров. GetArrayLength(rows) — число свойств; GetArrayLength(parameters) — число параметров одного свойства. Пустой массив при ObjID=0 или отсутствии полученных записей. Это не список ID предметов и не готовый текст.

## Поведение

- Данные TClilocRec из внешнего справочника представлены средствами BASIC: массивом строк. Count соответствует GetArrayLength(rows), Items[i].ClilocID — rows[i][0], Items[i].Params — rows[i][1].
- Запись из кэша возвращается сразу. При отсутствии OPL запрашиваются свойства с ожиданием до 120 мс; отмена процедуры прерывает ожидание. Известная пустая OPL не вызывает ожидание.
- Начальные служебные табуляции пропускаются как в ClilocLoader. Пустые внутренние параметры сохраняют позиции; #число сохраняется строкой для последующей локализации. Неизвестные параметры дают пустой массив.
- Изменение возвращённого массива не меняет кэш клиента. Для текста используйте GetTooltip/GetCliloc; для перевода одной строки — GetClilocByID(clilocID, parameters).
- Первичный справочник: https://stealth.od.ua/api/GetTooltipRec/ .

## Примеры

### Посмотреть номера всех свойств

```vb
# Посмотреть номера всех свойств
#
# Читает структурированные свойства: cliloc ID и параметры каждой записи OPL.
#
# Array<Array> — отдельный снимок строк свойств. Каждая строка равна [clilocID:Integer,
# parameters:Array<String>]. rows[i][0] — номер локализованного сообщения, rows[i][1] — массив
# параметров. GetArrayLength(rows) — число свойств; GetArrayLength(parameters) — число
# параметров одного свойства. Пустой массив при ObjID=0 или отсутствии полученных записей. Это
# не список ID предметов и не готовый текст.

SUB Main()
    # ObjID=lasttarget — объект. rows содержит свойства, i — индекс от 0. row[0] является cliloc, а
    # не serial.
    # Цикл не выполняется для пустого массива. Каждая запись обрабатывается один раз.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**Разбор параметров и выполнения:**

- ObjID=lasttarget — объект. rows содержит свойства, i — индекс от 0. row[0] является cliloc, а не serial.
- Цикл не выполняется для пустого массива. Каждая запись обрабатывается один раз.

### Перевести каждую запись с её параметрами

```vb
# Перевести каждую запись с её параметрами
#
# Читает структурированные свойства: cliloc ID и параметры каждой записи OPL.
#
# Array<Array> — отдельный снимок строк свойств. Каждая строка равна [clilocID:Integer,
# parameters:Array<String>]. rows[i][0] — номер локализованного сообщения, rows[i][1] — массив
# параметров. GetArrayLength(rows) — число свойств; GetArrayLength(parameters) — число
# параметров одного свойства. Пустой массив при ObjID=0 или отсутствии полученных записей. Это
# не список ID предметов и не готовый текст.

SUB Main()
    # GetClilocByID получает clilocID=row[0] и массив подстановок=row[1].
    # Параметры сохраняют порядок. Не передавайте весь row вместо массива параметров.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR text = UO.GetClilocByID(row[0], row[1])
        UO.Print(text)
        i = i + 1
    WEND
END SUB
```

**Разбор параметров и выполнения:**

- GetClilocByID получает clilocID=row[0] и массив подстановок=row[1].
- Параметры сохраняют порядок. Не передавайте весь row вместо массива параметров.

### Получить числовой параметр известного свойства

```vb
# Получить числовой параметр известного свойства
#
# Читает структурированные свойства: cliloc ID и параметры каждой записи OPL.
#
# Array<Array> — отдельный снимок строк свойств. Каждая строка равна [clilocID:Integer,
# parameters:Array<String>]. rows[i][0] — номер локализованного сообщения, rows[i][1] — массив
# параметров. GetArrayLength(rows) — число свойств; GetArrayLength(parameters) — число
# параметров одного свойства. Пустой массив при ObjID=0 или отсутствии полученных записей. Это
# не список ID предметов и не готовый текст.

SUB Main()
    # wanted — пример ID свойства; замените нужным cliloc. args[0] — первый параметр, исходно
    # String.
    # Перед Val проверяются число параметров и числовой формат. Параметр может быть текстом или
    # ссылкой #cliloc.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR wanted = 1060401
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR args = row[1]
        IF row[0] = wanted AND GetArrayLength(args) > 0 THEN
            IF IsNumeric(args[0]) THEN
                UO.Print('Value: ' + STR(Val(args[0])))
            END IF
        END IF
        i = i + 1
    WEND
END SUB
```

**Разбор параметров и выполнения:**

- wanted — пример ID свойства; замените нужным cliloc. args[0] — первый параметр, исходно String.
- Перед Val проверяются число параметров и числовой формат. Параметр может быть текстом или ссылкой #cliloc.
