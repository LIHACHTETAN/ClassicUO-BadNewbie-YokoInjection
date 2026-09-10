# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: uk -->

Читає структуровані властивості об’єкта: ID cliloc і параметри підстановки кожного запису.

## Точний синтаксис

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## Параметри

- `ObjID` — Обов’язковий serial об’єкта, не graphic/type і не ID cliloc. Ціле число, десяткова/hex-строка, self, backpack, lasttarget, finditem або ім’я AddObject. 0 означає відсутність об’єкта.

## Повертає

Array<Array>: кожний рядок — [clilocID:Integer, parameters:Array<String>]. rows[i][0] — номер повідомлення; rows[i][1] — масив параметрів. GetArrayLength(rows) рахує властивості. Порожній масив: записів не отримано або ObjID=0. Це не serial предметів.

## Поведінка

- Дані з кешу повертаються одразу. За відсутності OPL надсилається запит з очікуванням до 120 мс; скасування процедури перериває очікування. Відома порожня OPL повертається одразу.
- Структура TClilocRec представлена масивом BASIC: Count — GetArrayLength(rows), Items — рядки. Початкові службові табуляції пропускаються; внутрішні порожні параметри зберігають позиції. #число лишається рядком для локалізації. Відсутні параметри дають порожній масив. Зміна знімка не змінює кеш клієнта.
- https://stealth.od.ua/api/GetTooltipRec/

## Приклади

### Перелічити ID властивостей

```vb
# Перелічити ID властивостей
#
# Читає структуровані властивості об’єкта: ID cliloc і параметри підстановки кожного запису.
#
# Array<Array>: кожний рядок — [clilocID:Integer, parameters:Array<String>]. rows[i][0] — номер
# повідомлення; rows[i][1] — масив параметрів. GetArrayLength(rows) рахує властивості. Порожній
# масив: записів не отримано або ObjID=0. Це не serial предметів.

SUB Main()
    # ObjID=lasttarget вибирає об’єкт. i починається з 0; row[0] — ID cliloc. Для порожнього масиву
    # цикл не виконується.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**Пояснення параметрів і виконання:**

- ObjID=lasttarget вибирає об’єкт. i починається з 0; row[0] — ID cliloc. Для порожнього масиву цикл не виконується.

### Перекласти кожну властивість

```vb
# Перекласти кожну властивість
#
# Читає структуровані властивості об’єкта: ID cliloc і параметри підстановки кожного запису.
#
# Array<Array>: кожний рядок — [clilocID:Integer, parameters:Array<String>]. rows[i][0] — номер
# повідомлення; rows[i][1] — масив параметрів. GetArrayLength(rows) рахує властивості. Порожній
# масив: записів не отримано або ObjID=0. Це не serial предметів.

SUB Main()
    # GetClilocByID отримує ClilocID=row[0] і Params=row[1], зберігаючи порядок параметрів. Не
    # передавайте весь row замість Params.

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

**Пояснення параметрів і виконання:**

- GetClilocByID отримує ClilocID=row[0] і Params=row[1], зберігаючи порядок параметрів. Не передавайте весь row замість Params.

### Прочитати числовий параметр

```vb
# Прочитати числовий параметр
#
# Читає структуровані властивості об’єкта: ID cliloc і параметри підстановки кожного запису.
#
# Array<Array>: кожний рядок — [clilocID:Integer, parameters:Array<String>]. rows[i][0] — номер
# повідомлення; rows[i][1] — масив параметрів. GetArrayLength(rows) рахує властивості. Порожній
# масив: записів не отримано або ObjID=0. Це не serial предметів.

SUB Main()
    # wanted=1060401 — приклад ID властивості; замініть потрібним. args[0] має тип String. Перед Val
    # перевірте довжину масиву та IsNumeric: параметр може бути текстом або #cliloc.

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

**Пояснення параметрів і виконання:**

- wanted=1060401 — приклад ID властивості; замініть потрібним. args[0] має тип String. Перед Val перевірте довжину масиву та IsNumeric: параметр може бути текстом або #cliloc.
