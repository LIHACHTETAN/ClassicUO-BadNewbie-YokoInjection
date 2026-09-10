# UO.ClientTargetResponse

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->

Копирует результат последнего локального ClientRequest* в массив.

## Точный синтаксис

```text
UO.ClientTargetResponse() -> Any
```

Выберите одну из зарегистрированных форм. Параметры передаются позиционно. Any означает значение BASIC с преобразованием внутри команды; Unit — отсутствие возвращаемого значения.

## Параметры

Параметров нет.

## Возвращает

Array из пяти Integer: [0]=serial объекта (0 у земли/статики), [1]=graphic/type, [2]=X, [3]=Y, [4]=Z. Пустой массив возвращается до выбора, после сброса новым запросом, при отмене или неподходящем выборе. Отсутствуют hue, map, индекс статического слоя и признак land/static. Это не объект с именованными полями.

## Поведение

- Чтение не потребляет результат: его можно прочитать повторно. Новый ClientRequest* заменяет его.
- Всегда проверяйте GetArrayLength(result)=5 перед обращением по индексам.

## Примеры

### Пример 1. Выбрать предмет или персонажа

```vb
# Выбрать предмет или персонажа
#
# Копирует результат последнего локального ClientRequest* в массив.
#
# Array из пяти Integer: [0]=serial объекта (0 у земли/статики), [1]=graphic/type, [2]=X, [3]=Y,
# [4]=Z. Пустой массив возвращается до выбора, после сброса новым запросом, при отмене или
# неподходящем выборе. Отсутствуют hue, map, индекс статического слоя и признак land/static. Это
# не объект с именованными полями.

SUB Main()
    # 5000 — тайм-аут ожидания клика в миллисекундах. Новый запрос сбрасывает предыдущий результат.
    # Массив из пяти полей означает выбранный объект. result[0] — serial, а не type.

    UO.ClientRequestObjectTarget()
    IF UO.WaitForClientTargetResponse(5000) THEN
        VAR result = UO.ClientTargetResponse()
        IF GetArrayLength(result) = 5 THEN
            UO.Print('Serial: ' + UO.Int2Hex(result[0]))
        ELSE
            UO.Print('Selection cancelled')
        END IF
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- 5000 — тайм-аут ожидания клика в миллисекундах. Новый запрос сбрасывает предыдущий результат.
- Массив из пяти полей означает выбранный объект. result[0] — serial, а не type.

### Пример 2. Прочитать координаты выбранного тайла

```vb
# Прочитать координаты выбранного тайла
#
# Копирует результат последнего локального ClientRequest* в массив.
#
# Array из пяти Integer: [0]=serial объекта (0 у земли/статики), [1]=graphic/type, [2]=X, [3]=Y,
# [4]=Z. Пустой массив возвращается до выбора, после сброса новым запросом, при отмене или
# неподходящем выборе. Отсутствуют hue, map, индекс статического слоя и признак land/static. Это
# не объект с именованными полями.

SUB Main()
    # result[1] — graphic, result[2]/[3]/[4] — X/Y/Z. У тайла мира serial result[0] равен 0.
    # Тип, координаты и serial — отдельные поля. Индекса статического слоя в этом массиве нет.

    UO.ClientRequestTileTarget()
    IF UO.WaitForClientTargetResponse(5000) THEN
        VAR result = UO.ClientTargetResponse()
        IF GetArrayLength(result) = 5 THEN
            UO.Print('Type: ' + UO.Int2Hex(result[1]))
            UO.Print(STR(result[2]) + ',' + STR(result[3]) + ',' + STR(result[4]))
        END IF
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- result[1] — graphic, result[2]/[3]/[4] — X/Y/Z. У тайла мира serial result[0] равен 0.
- Тип, координаты и serial — отдельные поля. Индекса статического слоя в этом массиве нет.

### Пример 3. Отмена является ответом, но не объектом

```vb
# Отмена является ответом, но не объектом
#
# Копирует результат последнего локального ClientRequest* в массив.
#
# Array из пяти Integer: [0]=serial объекта (0 у земли/статики), [1]=graphic/type, [2]=X, [3]=Y,
# [4]=Z. Пустой массив возвращается до выбора, после сброса новым запросом, при отмене или
# неподходящем выборе. Отсутствуют hue, map, индекс статического слоя и признак land/static. Это
# не объект с именованными полями.

SUB Main()
    # CancelTarget отменяет локальный выбор; callback возвращает пустой результат.
    # ClientTargetResponsePresent даёт 1, но длина массива равна 0. Не обращайтесь к result[0] без
    # проверки длины.

    UO.ClientRequestObjectTarget()
    UO.CancelTarget()
    IF UO.ClientTargetResponsePresent() THEN
        VAR result = UO.ClientTargetResponse()
        UO.Print('Fields: ' + STR(GetArrayLength(result)))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- CancelTarget отменяет локальный выбор; callback возвращает пустой результат.
- ClientTargetResponsePresent даёт 1, но длина массива равна 0. Не обращайтесь к result[0] без проверки длины.
