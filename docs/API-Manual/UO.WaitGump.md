# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->

Регистрирует последовательность одноразовых ответов на кнопки. Скрипт продолжает работу сразу; отсутствие окна не вызывает 30-секундную задержку.

## Точный синтаксис

```text
UO.WaitGump(Value:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any, trigger16:Any) -> Unit
UO.WaitGump(triggerId:Integer) -> Unit
UO.WaitGump(triggerId:String) -> Unit
```

Выберите одну из зарегистрированных форм. Параметры передаются позиционно. Any означает значение BASIC с преобразованием внутри команды; Unit — отсутствие возвращаемого значения.

## Параметры

- `triggerId` — Integer ButtonID или числовая String. Одна строка может содержать последовательность через | или запятую. Формы с 2..16 аргументами принимают последовательность; в них также допустимы массивы и вложенные последовательности. Все ID разбираются до регистрации. Пустая последовательность, более 256 ожидающих кнопок клиента или вложенность более 32 уровней вызывают ошибку без частичной регистрации.
- `Value` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger1` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger2` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger3` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger4` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger5` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger6` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger7` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger8` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger9` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger10` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger11` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger12` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger13` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger14` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger15` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.
- `trigger16` — Элемент последовательности: Integer ButtonID, числовая String, строка с |/запятой или Array таких элементов. Порядок — слева направо. Применяются общие границы и правила triggerId. Value — имя единственного параметра формы Any, также принимающей массив.

## Возвращает

Unit — ничего не возвращает: ни успех, ни новое значение, ни подтверждение сервера.

## Поведение

- Ищет реальную кнопку Activate с нужным ButtonID; кнопки переключения страницы и окна без нужной кнопки пропускаются. Последующие ID не обходят первый ожидающий. На одну доставку разметки — не больше одного ответа в одно окно. Обновлённая разметка может использовать тот же объект окна.
- Следующий WaitGump того же скрипта дополняет его ожидающую последовательность. Поиск не ограничен GumpID: для точного выбора используйте NumGumpButton или SendGumpSelect. ButtonID=0 сработает только при существующей кнопке Activate с ID 0; это не универсальное закрытие.
- Обычное завершение процедуры сохраняет ожидание. Отмена владельца или Terminate с его именем удаляет его ожидания; TerminateAll удаляет все, включая оставшиеся после завершения процедур. Смена мира очищает очередь. Ожидания не сохраняются в профиль.

## Примеры

### Пример 1. Один ответ

```vb
# Один ответ
#
# Регистрирует последовательность одноразовых ответов на кнопки. Скрипт продолжает работу сразу;
# отсутствие окна не вызывает 30-секундную задержку.
#
# Unit — ничего не возвращает: ни успех, ни новое значение, ни подтверждение сервера.

SUB Main()
    # 100 — ButtonID ответа. WaitGump регистрирует его перед UseObject; дальнейшее выполнение не
    # означает, что сервер уже принял ответ.

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Разбор параметров и выполнения:**

- 100 — ButtonID ответа. WaitGump регистрирует его перед UseObject; дальнейшее выполнение не означает, что сервер уже принял ответ.

### Пример 2. Несколько шагов

```vb
# Несколько шагов
#
# Регистрирует последовательность одноразовых ответов на кнопки. Скрипт продолжает работу сразу;
# отсутствие окна не вызывает 30-секундную задержку.
#
# Unit — ничего не возвращает: ни успех, ни новое значение, ни подтверждение сервера.

SUB Main()
    # 7, 22 и 1 — ButtonID последовательных форм. Эти ID проверяются по порядку. Число аргументов не
    # задаёт задержку; вызов регистрирует всю последовательность.

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**Разбор параметров и выполнения:**

- 7, 22 и 1 — ButtonID последовательных форм. Эти ID проверяются по порядку. Число аргументов не задаёт задержку; вызов регистрирует всю последовательность.

### Пример 3. Отмена ожиданий

```vb
# Отмена ожиданий
#
# Регистрирует последовательность одноразовых ответов на кнопки. Скрипт продолжает работу сразу;
# отсутствие окна не вызывает 30-секундную задержку.
#
# Unit — ничего не возвращает: ни успех, ни новое значение, ни подтверждение сервера.

SUB Main()
    # Строка 7|22|1 задаёт ту же последовательность. TerminateAll затем очищает все ожидающие
    # действия гампов и останавливает все процедуры; это глобальное действие.

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**Разбор параметров и выполнения:**

- Строка 7|22|1 задаёт ту же последовательность. TerminateAll затем очищает все ожидающие действия гампов и останавливает все процедуры; это глобальное действие.
