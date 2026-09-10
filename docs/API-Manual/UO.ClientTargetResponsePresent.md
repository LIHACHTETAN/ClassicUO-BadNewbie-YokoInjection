# UO.ClientTargetResponsePresent

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->

Проверяет, получен ли ответ на последний локальный запрос выбора.

## Точный синтаксис

```text
UO.ClientTargetResponsePresent() -> Any
```

Выберите одну из зарегистрированных форм. Параметры передаются позиционно. Any означает значение BASIC с преобразованием внутри команды; Unit — отсутствие возвращаемого значения.

## Параметры

Параметров нет.

## Возвращает

Integer 1 — callback уже ответил, включая отмену; 0 — новый выбор ещё не завершён. Значение 1 не гарантирует наличие объекта: при отмене ClientTargetResponse возвращает пустой Array.

Это логический результат: 1 = TRUE, 0 = FALSE. После VAR result = команда(...) можно писать IF result = TRUE THEN или IF result = 1 THEN; для отрицательного результата — IF result = FALSE THEN или IF result = 0 THEN. TRUE/FALSE пишутся без кавычек. Вызовите команду один раз и сохраните результат: повторный вызов может повторить действие или прочитать уже изменившееся состояние.

## Поведение

- Не означает наличие серверного прицела и не описывает очередь WaitTarget.
- Чтение результата не сбрасывает этот флаг; его сбрасывает следующий ClientRequest*.

## Примеры

### Пример 1. Выбрать предмет или персонажа

```vb
# Выбрать предмет или персонажа
#
# Проверяет, получен ли ответ на последний локальный запрос выбора.
#
# Integer 1 — callback уже ответил, включая отмену; 0 — новый выбор ещё не завершён. Значение 1
# не гарантирует наличие объекта: при отмене ClientTargetResponse возвращает пустой Array.
#
# Это логический результат: 1 = TRUE, 0 = FALSE. После VAR result = команда(...) можно писать IF
# result = TRUE THEN или IF result = 1 THEN; для отрицательного результата — IF result = FALSE
# THEN или IF result = 0 THEN. TRUE/FALSE пишутся без кавычек. Вызовите команду один раз и
# сохраните результат: повторный вызов может повторить действие или прочитать уже изменившееся
# состояние.

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
# Проверяет, получен ли ответ на последний локальный запрос выбора.
#
# Integer 1 — callback уже ответил, включая отмену; 0 — новый выбор ещё не завершён. Значение 1
# не гарантирует наличие объекта: при отмене ClientTargetResponse возвращает пустой Array.
#
# Это логический результат: 1 = TRUE, 0 = FALSE. После VAR result = команда(...) можно писать IF
# result = TRUE THEN или IF result = 1 THEN; для отрицательного результата — IF result = FALSE
# THEN или IF result = 0 THEN. TRUE/FALSE пишутся без кавычек. Вызовите команду один раз и
# сохраните результат: повторный вызов может повторить действие или прочитать уже изменившееся
# состояние.

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
# Проверяет, получен ли ответ на последний локальный запрос выбора.
#
# Integer 1 — callback уже ответил, включая отмену; 0 — новый выбор ещё не завершён. Значение 1
# не гарантирует наличие объекта: при отмене ClientTargetResponse возвращает пустой Array.
#
# Это логический результат: 1 = TRUE, 0 = FALSE. После VAR result = команда(...) можно писать IF
# result = TRUE THEN или IF result = 1 THEN; для отрицательного результата — IF result = FALSE
# THEN или IF result = 0 THEN. TRUE/FALSE пишутся без кавычек. Вызовите команду один раз и
# сохраните результат: повторный вызов может повторить действие или прочитать уже изменившееся
# состояние.

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
