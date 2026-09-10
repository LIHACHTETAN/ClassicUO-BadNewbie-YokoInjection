# UO.GetLandTileData

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Читает расширенную справочную запись земли из tiledata.

## Точный синтаксис

```text
UO.GetLandTileData(Tile:Any) -> Any
```

## Параметры

- `Tile` — Graphic/type записи, не serial и не индекс внутри клетки. Таблица земли выбрана самим именем команды.

## Возвращает

Array из 7 полей для допустимого graphic. Все поля Integer, кроме name (String):

- `[0] graphic` — graphic/type записи.
- `[1] flags` — младшие 32 бита флагов.
- `[2] name` — название из tiledata (String).
- `[3] texId` — ID текстуры земли.
- `[4] wet` — 1 если установлен wet, иначе 0.
- `[5] impassable` — 1 если impassable, иначе 0.
- `[6] noDiagonal` — 1 если noDiagonal, иначе 0.

Для недопустимого graphic справочные свойства отсутствуют: возвращается короткий массив `[переданный graphic, 0, ""]`. Проверяйте полную длину перед чтением свойств. Это не Pascal record и не список объектов.

## Поведение

- Команда читает tiledata и не требует предмета с этим graphic в мире. Флаги описывают ресурс; результат не заменяет полноценную проверку маршрута.

## Примеры

### Прочитать имя записи

```vb
# Прочитать имя записи
#
# Читает расширенную справочную запись земли из tiledata.
#
# Array из 7 полей для допустимого graphic. Все поля Integer, кроме name (String):
#
# - `[0] graphic` — graphic/type записи.
# - `[1] flags` — младшие 32 бита флагов.
# - `[2] name` — название из tiledata (String).
# - `[3] texId` — ID текстуры земли.
# - `[4] wet` — 1 если установлен wet, иначе 0.
# - `[5] impassable` — 1 если impassable, иначе 0.
# - `[6] noDiagonal` — 1 если noDiagonal, иначе 0.
#
# Для недопустимого graphic справочные свойства отсутствуют: возвращается короткий массив
# `[переданный graphic, 0, ""]`. Проверяйте полную длину перед чтением свойств. Это не Pascal
# record и не список объектов.

SUB Main()
    # Tile — числовой graphic выбранной таблицы.
    # data[2] содержит имя. Проверка длины отделяет полноценную запись от короткой записи
    # недопустимого graphic.

    VAR data = UO.GetLandTileData(0x0003)
    IF GetArrayLength(data) = 7 THEN
        UO.Print(data[2])
    ELSE
        UO.Print('Tiledata entry is unavailable')
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- Tile — числовой graphic выбранной таблицы.
- data[2] содержит имя. Проверка длины отделяет полноценную запись от короткой записи недопустимого graphic.

### Проверить отдельный логический флаг

```vb
# Проверить отдельный логический флаг
#
# Читает расширенную справочную запись земли из tiledata.
#
# Array из 7 полей для допустимого graphic. Все поля Integer, кроме name (String):
#
# - `[0] graphic` — graphic/type записи.
# - `[1] flags` — младшие 32 бита флагов.
# - `[2] name` — название из tiledata (String).
# - `[3] texId` — ID текстуры земли.
# - `[4] wet` — 1 если установлен wet, иначе 0.
# - `[5] impassable` — 1 если impassable, иначе 0.
# - `[6] noDiagonal` — 1 если noDiagonal, иначе 0.
#
# Для недопустимого graphic справочные свойства отсутствуют: возвращается короткий массив
# `[переданный graphic, 0, ""]`. Проверяйте полную длину перед чтением свойств. Это не Pascal
# record и не список объектов.

SUB Main()
    # data[5] — отдельное поле impassable: 1=true, 0=false.
    # Эта проверка не учитывает другие объекты в клетке или способности персонажа.

    VAR data = UO.GetLandTileData(0x0003)
    IF GetArrayLength(data) = 7 THEN
        IF data[5] THEN
            UO.Print('Impassable flag is set')
        ELSE
            UO.Print('Impassable flag is not set')
        END IF
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- data[5] — отдельное поле impassable: 1=true, 0=false.
- Эта проверка не учитывает другие объекты в клетке или способности персонажа.

### Вывести graphic и общую маску флагов

```vb
# Вывести graphic и общую маску флагов
#
# Читает расширенную справочную запись земли из tiledata.
#
# Array из 7 полей для допустимого graphic. Все поля Integer, кроме name (String):
#
# - `[0] graphic` — graphic/type записи.
# - `[1] flags` — младшие 32 бита флагов.
# - `[2] name` — название из tiledata (String).
# - `[3] texId` — ID текстуры земли.
# - `[4] wet` — 1 если установлен wet, иначе 0.
# - `[5] impassable` — 1 если impassable, иначе 0.
# - `[6] noDiagonal` — 1 если noDiagonal, иначе 0.
#
# Для недопустимого graphic справочные свойства отсутствуют: возвращается короткий массив
# `[переданный graphic, 0, ""]`. Проверяйте полную длину перед чтением свойств. Это не Pascal
# record и не список объектов.

SUB Main()
    # data[0] повторяет переданный graphic, data[1] — общая маска флагов.
    # Маска может содержать одновременно несколько битов; её численное значение не является serial.

    VAR data = UO.GetLandTileData(0x0003)
    IF GetArrayLength(data) = 7 THEN
        UO.Print('Graphic: ' + CStr(data[0]))
        UO.Print('Flags: ' + CStr(data[1]))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- data[0] повторяет переданный graphic, data[1] — общая маска флагов.
- Маска может содержать одновременно несколько битов; её численное значение не является serial.
