# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

For повторює блок у числовому діапазоні, включно з досяжною межею. Підходить для індексів масиву або визначеної кількості дій; For Each перебирає значення елементів.

## Точний синтаксис

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## Параметри

- `counter / VAR` — Числова змінна лічильника. VAR оголошує її у процедурі; без VAR використовується доступна змінна. З Option Explicit On оголосіть її заздалегідь або вживайте For Var. Тип задавайте окремо: DIM counter AS Integer; AS у заголовку числового For не підтримується.
- `start` — Початковий числовий вираз: обчислюється один раз і присвоюється до обчислення limit та increment.
- `limit` — Включена кінцева межа, що обчислюється один раз при вході. Додатний крок перевіряє counter <= limit, від’ємний — counter >= limit.
- `increment` — Необов’язковий числовий крок, стандартно 1. Може бути від’ємним чи дробовим; нуль спричиняє перехоплювану помилку. Тип лічильника має підтримувати крок і просування.
- `statements / Next / exit` — Тіло й Next пишуться окремими рядками. Ім’я після Next необов’язкове, але повинно збігатися з лічильником. Continue For переходить до наступного кроку, Exit For виходить з найближчого For/For Each, Break — з найближчого циклу будь-якого виду.

## Повертає

For, Next та Exit For нічого не повертають. Лічильник — число, а не автоматично ID предмета. Після звичайного завершення рушій зберігає останнє використане значення, а не значення за межею. Пропущений цикл залишає start, ранній вихід — поточне значення. Приклади повертають з Main Integer 12, 28, 395.

## Поведінка

- Вхід: присвоїти start, зберегти limit і крок, відхилити нульовий крок, перевірити перше значення. Напрямок від межі пропускає тіло; start=limit виконує його один раз.
- Next перевіряє counter+step і присвоює лише значення для допустимої наступної ітерації: 1 To 5 Step 3 відвідує 1 та 4. Зміни змінних межі/кроку не змінюють збережених значень; зміна самого лічильника впливає на наступний крок.
- Структура й ім’я Next перевіряються до виконання; помилка структури — SC020. Вкладені цикли потребують різних лічильників. Вихід із Try виконує Finally. Пауза й зупинка доступні, автоматичної затримки або таймауту немає.

## Приклади

### 1. Сума комірок

```vb
# values[2] створює індекси 0,1,2 зі значеннями 2,4,6. Sum отримує масив ByVal, починає index=0 та зберігає length-1=2. Стандартний крок 1 відвідує три комірки; total=12 повертається до Main.
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**Пояснення параметрів і виконання:**

values[2] створює індекси 0,1,2 зі значеннями 2,4,6. Sum отримує масив ByVal, починає index=0 та зберігає length-1=2. Стандартний крок 1 відвідує три комірки; total=12 повертається до Main.

### 2. Видалення з кінця

```vb
# items містить -1,3,-2,5. Початок Count()-1=3, межа 0, крок -1. Видалення від’ємного елемента зсуває лише вже переглянуті індекси, не пропускаючи наступних елементів. Залишаються 3 та 5; Count()*10+3+5 повертає 28.
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**Пояснення параметрів і виконання:**

items містить -1,3,-2,5. Початок Count()-1=3, межа 0, крок -1. Видалення від’ємного елемента зсуває лише вже переглянуті індекси, не пропускаючи наступних елементів. Залишаються 3 та 5; Count()*10+3+5 повертає 28.

### 3. Збережені межі й лічильник

```vb
# ReadLimit збільшує calls через ByRef і повертає value. Початок 1, межа 5, крок 2 обчислюються по одному разу: calls=3. Присвоєння upper=99, stride=1 у тілі не змінюють цей цикл. Значення 1,3,5 дають total=9, index залишається 5. Main повертає 300+90+5=395.
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**Пояснення параметрів і виконання:**

ReadLimit збільшує calls через ByRef і повертає value. Початок 1, межа 5, крок 2 обчислюються по одному разу: calls=3. Присвоєння upper=99, stride=1 у тілі не змінюють цей цикл. Значення 1,3,5 дають total=9, index залишається 5. Main повертає 300+90+5=395.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
