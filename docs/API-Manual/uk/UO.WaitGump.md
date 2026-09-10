# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: uk -->

Реєструє послідовність одноразових відповідей кнопками. Скрипт продовжується відразу; відсутність вікна не блокує його на 30 секунд.

## Точний синтаксис

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

## Параметри

- `triggerId` — Integer ButtonID або числова String. Один рядок може містити послідовність через | або кому. Форми з 2..16 аргументами приймають послідовності, зокрема масиви та вкладені послідовності. Усі ID розбираються до реєстрації. Порожня послідовність, понад 256 очікуваних кнопок клієнта або вкладеність понад 32 рівні спричиняють помилку без часткової реєстрації.
- `Value` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger1` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger2` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger3` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger4` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger5` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger6` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger7` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger8` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger9` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger10` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger11` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger12` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger13` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger14` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger15` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.
- `trigger16` — Елемент послідовності: Integer ButtonID, числова String, рядок з |/комою або Array таких елементів. Порядок — зліва направо; діють межі та правила triggerId. Value — назва єдиного параметра Any, який також приймає масив.

## Повертає

Unit — нічого не повертає: ані успіх, ані нове значення, ані підтвердження сервера.

## Поведінка

- Потрібна справжня кнопка Activate з відповідним ButtonID; перемикачі сторінок та сторонні вікна пропускаються. Наступні ID не оминають перший очікуваний. За одне надходження розмітки — щонайбільше одна відповідь у кожне вікно. Оновлена розмітка може використати той самий об’єкт вікна.
- Наступний WaitGump того самого скрипту доповнює його чергу. Пошук не обмежений GumpID: для точного вибору використовуйте NumGumpButton або SendGumpSelect. ButtonID=0 потребує справжньої кнопки Activate з ID 0; це не універсальне закриття.
- Звичайне завершення процедури зберігає очікування. Скасування власника або Terminate з його іменем видаляє його дії; TerminateAll видаляє всі, включно з діями завершених процедур. Зміна світу очищає чергу. Дії не записуються в профіль.

## Приклади

### Одна відповідь

```vb
# Одна відповідь
#
# Реєструє послідовність одноразових відповідей кнопками. Скрипт продовжується відразу;
# відсутність вікна не блокує його на 30 секунд.
#
# Unit — нічого не повертає: ані успіх, ані нове значення, ані підтвердження сервера.

SUB Main()
    # 100 — ButtonID відповіді. WaitGump реєструє його перед UseObject; продовження скрипту не
    # означає підтвердження сервером.

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Пояснення параметрів і виконання:**

- 100 — ButtonID відповіді. WaitGump реєструє його перед UseObject; продовження скрипту не означає підтвердження сервером.

### Кілька етапів

```vb
# Кілька етапів
#
# Реєструє послідовність одноразових відповідей кнопками. Скрипт продовжується відразу;
# відсутність вікна не блокує його на 30 секунд.
#
# Unit — нічого не повертає: ані успіх, ані нове значення, ані підтвердження сервера.

SUB Main()
    # 7, 22 і 1 — ButtonID послідовних форм, що перевіряються в цьому порядку. Кількість аргументів
    # не задає затримку; виклик реєструє всю послідовність.

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**Пояснення параметрів і виконання:**

- 7, 22 і 1 — ButtonID послідовних форм, що перевіряються в цьому порядку. Кількість аргументів не задає затримку; виклик реєструє всю послідовність.

### Скасувати очікування

```vb
# Скасувати очікування
#
# Реєструє послідовність одноразових відповідей кнопками. Скрипт продовжується відразу;
# відсутність вікна не блокує його на 30 секунд.
#
# Unit — нічого не повертає: ані успіх, ані нове значення, ані підтвердження сервера.

SUB Main()
    # Рядок 7|22|1 задає ту саму послідовність. TerminateAll очищає всі очікувані дії гампів і
    # зупиняє всі процедури; це глобальна дія.

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**Пояснення параметрів і виконання:**

- Рядок 7|22|1 задає ту саму послідовність. TerminateAll очищає всі очікувані дії гампів і зупиняє всі процедури; це глобальна дія.
