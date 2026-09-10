# UO.GetTileLayer

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->

Читает номер слоя экипировки из записи tiledata.

## Точный синтаксис

```text
UO.GetTileLayer(group:Any, tileId:Any) -> Integer
```

Выберите одну из зарегистрированных форм. Параметры передаются позиционно. Any означает значение BASIC с преобразованием внутри команды; Unit — отсутствие возвращаемого значения.

## Параметры

- `group` — 0 — таблица земли (land); 1 — таблица статических graphic. Реализация считает любое ненулевое group второй таблицей; используйте 0 или 1.
- `tileId` — Graphic/type записи в tiledata, обычно целое 0…65535. Это не serial предмета и не индекс статики внутри клетки.

## Возвращает

Integer — номер слоя экипировки graphic: например 1=Rhand, 2=Lhand, 21=Backpack. Для земли, отсутствующей записи или нулевого слоя возвращается 0. Это не порядок статики в клетке, не этаж и не Z.

## Поведение

- Эта команда читает справочную запись graphic; координаты мира не нужны. group=0 и group=1 выбирают разные таблицы даже при одинаковом tileId.
- Свойство читается из данных graphic, а не из текущего состояния конкретного предмета.

## Примеры

### Пример 1. Прочитать свойство известного static graphic

```vb
# Прочитать свойство известного static graphic
#
# Читает номер слоя экипировки из записи tiledata.
#
# Integer — номер слоя экипировки graphic: например 1=Rhand, 2=Lhand, 21=Backpack. Для земли,
# отсутствующей записи или нулевого слоя возвращается 0. Это не порядок статики в клетке, не
# этаж и не Z.

SUB Main()
    # group=1 выбирает static tiledata; tileId=0x0CCA — graphic дерева.
    # value содержит результат, описанный в разделе «Возвращает»; его смысл не совпадает с serial.

    VAR value = UO.GetTileLayer(1, 0x0CCA)
    IF value = 1 THEN
        UO.Print('Right-hand graphic')
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
# Читает номер слоя экипировки из записи tiledata.
#
# Integer — номер слоя экипировки graphic: например 1=Rhand, 2=Lhand, 21=Backpack. Для земли,
# отсутствующей записи или нулевого слоя возвращается 0. Это не порядок статики в клетке, не
# этаж и не Z.

SUB Main()
    # FindType возвращает serial. GetType превращает его в числовой graphic.
    # group=1 используется для предметов; в tileId передаётся graphic, не item.

    VAR item = UO.FindType(0x0EED, -1, 'backpack')
    IF item <> '' THEN
        VAR graphic = UO.GetType(item)
        VAR value = UO.GetTileLayer(1, graphic)
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
# Читает номер слоя экипировки из записи tiledata.
#
# Integer — номер слоя экипировки graphic: например 1=Rhand, 2=Lhand, 21=Backpack. Для земли,
# отсутствующей записи или нулевого слоя возвращается 0. Это не порядок статики в клетке, не
# этаж и не Z.

SUB Main()
    # Первые два аргумента GetLandscapeTile — текущие мировые X/Y; третий — текущая карта.
    # land[0] содержит graphic земли. group=0 выбирает land tiledata. Для GetTileLayer/GetTileHeight
    # земля даёт 0.

    VAR land = UO.GetLandscapeTile(UO.GetX(), UO.GetY(), UO.WorldNum())
    IF GetArrayLength(land) >= 3 THEN
        VAR graphic = land[0]
        VAR value = UO.GetTileLayer(0, graphic)
        UO.Print(CStr(value))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- Первые два аргумента GetLandscapeTile — текущие мировые X/Y; третий — текущая карта.
- land[0] содержит graphic земли. group=0 выбирает land tiledata. Для GetTileLayer/GetTileHeight земля даёт 0.
