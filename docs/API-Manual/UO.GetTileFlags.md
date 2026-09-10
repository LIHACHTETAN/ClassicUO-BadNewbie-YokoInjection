# UO.GetTileFlags

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->

Читает битовую маску свойств graphic из записи tiledata.

## Точный синтаксис

```text
UO.GetTileFlags(group:Any, tileId:Any) -> Any
```

Выберите одну из зарегистрированных форм. Параметры передаются позиционно. Any означает значение BASIC с преобразованием внутри команды; Unit — отсутствие возвращаемого значения.

## Параметры

- `group` — 0 — таблица земли (land); 1 — таблица статических graphic. Реализация считает любое ненулевое group второй таблицей; используйте 0 или 1.
- `tileId` — Graphic/type записи в tiledata, обычно целое 0…65535. Это не serial предмета и не индекс статики внутри клетки.

## Возвращает

Integer — младшие 32 бита флагов tiledata. Установленный старший бит даёт отрицательное знаковое число. 0 означает отсутствие этих флагов либо недопустимый tileId; это не самостоятельный признак ошибки и не Boolean. Несколько свойств могут быть установлены одновременно.

## Поведение

- Эта команда читает справочную запись graphic; координаты мира не нужны. group=0 и group=1 выбирают разные таблицы даже при одинаковом tileId.
- Свойство читается из данных graphic, а не из текущего состояния конкретного предмета.

## Примеры

### Пример 1. Прочитать свойство известного static graphic

```vb
# Прочитать свойство известного static graphic
#
# Читает битовую маску свойств graphic из записи tiledata.
#
# Integer — младшие 32 бита флагов tiledata. Установленный старший бит даёт отрицательное
# знаковое число. 0 означает отсутствие этих флагов либо недопустимый tileId; это не
# самостоятельный признак ошибки и не Boolean. Несколько свойств могут быть установлены
# одновременно.

SUB Main()
    # group=1 выбирает static tiledata; tileId=0x0CCA — graphic дерева.
    # value содержит результат, описанный в разделе «Возвращает»; его смысл не совпадает с serial.

    VAR value = UO.GetTileFlags(1, 0x0CCA)
    IF contains(value, 0x40) THEN
        UO.Print('Impassable flag is set')
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- group=1 выбирает static tiledata; tileId=0x0CCA — graphic дерева.
- value содержит результат, описанный в разделе «Возвращает»; его смысл не совпадает с serial.

### Пример 2. Прочитать свойство graphic найденного предмета

```vb
# Прочитать свойство graphic найденного предмета
#
# Читает битовую маску свойств graphic из записи tiledata.
#
# Integer — младшие 32 бита флагов tiledata. Установленный старший бит даёт отрицательное
# знаковое число. 0 означает отсутствие этих флагов либо недопустимый tileId; это не
# самостоятельный признак ошибки и не Boolean. Несколько свойств могут быть установлены
# одновременно.

SUB Main()
    # FindType возвращает serial. GetType превращает его в числовой graphic.
    # group=1 используется для предметов; в tileId передаётся graphic, не item.

    VAR item = UO.FindType(0x0EED, -1, 'backpack')
    IF item <> '' THEN
        VAR graphic = UO.GetType(item)
        VAR value = UO.GetTileFlags(1, graphic)
        UO.Print(CStr(value))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- FindType возвращает serial. GetType превращает его в числовой graphic.
- group=1 используется для предметов; в tileId передаётся graphic, не item.

### Пример 3. Прочитать свойство земли под персонажем

```vb
# Прочитать свойство земли под персонажем
#
# Читает битовую маску свойств graphic из записи tiledata.
#
# Integer — младшие 32 бита флагов tiledata. Установленный старший бит даёт отрицательное
# знаковое число. 0 означает отсутствие этих флагов либо недопустимый tileId; это не
# самостоятельный признак ошибки и не Boolean. Несколько свойств могут быть установлены
# одновременно.

SUB Main()
    # Первые два аргумента GetLandscapeTile — текущие мировые X/Y; третий — текущая карта.
    # land[0] содержит graphic земли. group=0 выбирает land tiledata. Для GetTileLayer/GetTileHeight
    # земля даёт 0.

    VAR land = UO.GetLandscapeTile(UO.GetX(), UO.GetY(), UO.WorldNum())
    IF GetArrayLength(land) >= 3 THEN
        VAR graphic = land[0]
        VAR value = UO.GetTileFlags(0, graphic)
        UO.Print(CStr(value))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- Первые два аргумента GetLandscapeTile — текущие мировые X/Y; третий — текущая карта.
- land[0] содержит graphic земли. group=0 выбирает land tiledata. Для GetTileLayer/GetTileHeight земля даёт 0.
