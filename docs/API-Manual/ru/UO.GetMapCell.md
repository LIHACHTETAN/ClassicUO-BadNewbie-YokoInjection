# UO.GetMapCell

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Читает graphic, высоту и флаги земли в одной клетке карты.

## Точный синтаксис

```text
UO.GetMapCell(X:Any, Y:Any, WorldNum:Any) -> Any
```

## Параметры

- `X` — Мировая координата X клетки текущей карты, не положение в гампе.
- `Y` — Мировая координата Y клетки текущей карты.
- `WorldNum` — Номер карты/фасета; используйте UO.WorldNum(). Читается только текущая загруженная карта.

## Возвращает

Array из трёх Integer: [0] graphic/type земли, [1] мировая Z основания land, [2] младшие 32 бита флагов tiledata. Недоступная клетка или другая карта дают пустой Array. Это не serial, Boolean или Pascal record; не используйте поля .Tile/.Z. Для количества полей вызывайте GetArrayLength(cell).

## Поведение

- Команда читает локальную карту и не запускает движение или target. Клетка за пределами размеров карты не подменяется клеткой соседнего столбца.
- Высота Z, graphic/type, цвет hue, флаги и слой экипировки имеют разный смысл. Нулевой graphic или Z=0 могут быть допустимыми данными; проверяйте форму результата.

### Внутренние функции: от вызова до результата

Это цепочка настоящих C#-методов клиента. Имена внутренних методов не являются дополнительными UO-командами. Запускаемый код и все вспомогательные процедуры приведены ниже.

#### 1. ExecuteStealthCompatibility

Ветка GetMapCell принимает три аргумента X/Y/WorldNum и преобразует их в Integer.

Копирует int[] из bridge.GetLandscapeTile в Array значений скрипта, сохраняя порядок всех трёх полей.

Исходник проекта: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; функция `ExecuteStealthCompatibility`.

#### 2. GetLandscapeTile

Получает X/Y/карту через Invoke на игровом потоке. При несовпадении карты возвращает пустой int[]; иначе ищет Land в списке клетки.

Возвращает [graphic, Z, flags32] либо пустой массив. Z — основание land, flags32 — младшие 32 бита tiledata. GetSurfaceZ отдельно читает AverageZ.

Исходник проекта: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; функция `GetLandscapeTile`.

#### 3. GetChunk2

Получает X/Y блока карты и флаг load. Проверяет обе оси до вычисления линейного индекса; отрицательные и слишком большие координаты дают null.

Возвращает загруженный/переиспользуемый Chunk или null. При load=true может прочитать блок из ресурсов; холодное чтение не имеет жёсткой гарантии времени.

Исходник проекта: `src/ClassicUO.Client/Game/Map/Map.cs`; функция `GetChunk2`.

Чтение не перемещает персонажа и не отправляет команды серверу. Геометрия меняется между запросами; полученный массив — результат этого чтения, а не подписка на изменения.


## Примеры

### Прочитать землю под персонажем

```vb
# Прочитать землю под персонажем
#
# Читает graphic, высоту и флаги земли в одной клетке карты.
#
# Array из трёх Integer: [0] graphic/type земли, [1] мировая Z основания land, [2] младшие 32
# бита флагов tiledata. Недоступная клетка или другая карта дают пустой Array. Это не serial,
# Boolean или Pascal record; не используйте поля .Tile/.Z. Для количества полей вызывайте
# GetArrayLength(cell).

SUB Main()
    # X/Y берутся у self, WorldNum — текущая карта. cell сохраняет все поля одного вызова.
    # Индексы начинаются с 0. cell[1] — высота, а не признак успешного поиска; пустой массив
    # проверяется до индексации.

    VAR cell = UO.GetMapCell(UO.GetX(), UO.GetY(), UO.WorldNum())
    IF GetArrayLength(cell) = 3 THEN
        UO.Print('Type: ' + CStr(cell[0]))
        UO.Print('Land Z: ' + CStr(cell[1]))
        UO.Print('Flags: ' + CStr(cell[2]))
    ELSE
        UO.Print('Map cell unavailable')
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- X/Y берутся у self, WorldNum — текущая карта. cell сохраняет все поля одного вызова.
- Индексы начинаются с 0. cell[1] — высота, а не признак успешного поиска; пустой массив проверяется до индексации.

### Сравнить две соседние клетки

```vb
# Сравнить две соседние клетки
#
# Читает graphic, высоту и флаги земли в одной клетке карты.
#
# Array из трёх Integer: [0] graphic/type земли, [1] мировая Z основания land, [2] младшие 32
# бита флагов tiledata. Недоступная клетка или другая карта дают пустой Array. Это не serial,
# Boolean или Pascal record; не используйте поля .Tile/.Z. Для количества полей вызывайте
# GetArrayLength(cell).

SUB Main()
    # Второй вызов читает клетку восточнее, оба используют одну карту.
    # Разность высот земли не доказывает проходимость: стены, статики и другие объекты проверяются
    # отдельно.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR here = UO.GetMapCell(x, y, map)
    VAR east = UO.GetMapCell(x + 1, y, map)
    IF GetArrayLength(here) = 3 AND GetArrayLength(east) = 3 THEN
        UO.Print('Land difference: ' + CStr(east[1] - here[1]))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- Второй вызов читает клетку восточнее, оба используют одну карту.
- Разность высот земли не доказывает проходимость: стены, статики и другие объекты проверяются отдельно.

### Сравнить основание земли со средней поверхностью

```vb
# Сравнить основание земли со средней поверхностью
#
# Читает graphic, высоту и флаги земли в одной клетке карты.
#
# Array из трёх Integer: [0] graphic/type земли, [1] мировая Z основания land, [2] младшие 32
# бита флагов tiledata. Недоступная клетка или другая карта дают пустой Array. Это не serial,
# Boolean или Pascal record; не используйте поля .Tile/.Z. Для количества полей вызывайте
# GetArrayLength(cell).

SUB Main()
    # GetMapCell читает Land.Z; GetSurfaceZ читает Land.AverageZ.
    # Оба значения являются высотой. На наклонной земле они могут различаться; это не высота пола
    # дома.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR cell = UO.GetMapCell(x, y, map)
    IF GetArrayLength(cell) = 3 THEN
        VAR average = UO.GetSurfaceZ(x, y, map)
        UO.Print('Base: ' + CStr(cell[1]) + ', average: ' + CStr(average))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- GetMapCell читает Land.Z; GetSurfaceZ читает Land.AverageZ.
- Оба значения являются высотой. На наклонной земле они могут различаться; это не высота пола дома.
