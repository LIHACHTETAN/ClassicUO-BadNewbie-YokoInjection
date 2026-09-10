# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

For Each послідовно перебирає елементи масиву або нативної колекції з підтримкою переліку без числового індексу. Це оператор циклу всередині процедури чи функції, а не виклик API.

## Точний синтаксис

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## Параметри

- `item` — item: змінна перебору. Використовує наявну локальну змінну, параметр або доступне поле; інакше створює локальну змінну процедури, навіть з Option Explicit On. Запис у константу заборонений.
- `type` — type: необов’язковий AS type, наприклад Integer. Оголошує локальну змінну й перетворює кожен елемент. Без AS наявна змінна зберігає свій тип.
- `collection` — collection: вираз обчислюється один раз при вході. Дозволені масив і нативний об’єкт з підтримкою переліку; скалярні значення недопустимі. Вкладений масив спочатку видає рядки; для комірок потрібен вкладений цикл.
- `statements / NEXT item` — statements / NEXT item: тіло і завершення. Ім’я після NEXT необов’язкове, але має збігатися зі змінною перебору. NEXT пишеться окремим рядком.

## Повертає

For Each і Next не повертають значення. item отримує сам елемент, а не автоматично індекс, довжину, ID чи кількість у стосі. RETURN у тілі завершує всю функцію. Приклади повертають Integer 12, 105 і 10.

## Поведінка

- Підготовка пов’язує FOR EACH з NEXT і перевіряє структуру до ініціалізації; невідповідність дає SC020. collection обчислюється один раз, движок зберігає посилання й окрему позицію, яку зміна item не пересуває.
- Масив читається за зростанням індексів. Порожній масив пропускає тіло та зберігає попереднє значення наявної змінної без AS. Неініціалізований елемент і помилка AS викликають помилки, які можна перехопити.
- Присвоєння item не змінює елемент масиву. Вкладені масиви й об’єкти є посиланнями: зміна комірки row змінює сам рядок. Переприсвоєння collection не замінює поточний масив; зміни його наступних елементів видно під час читання.
- Continue For переходить до наступного елемента найближчого For або For Each, Exit For виходить. Помилка, RETURN і зупинка звільняють нативний перелічувач. Колекція може забороняти зміни під час перебору; автоматичної копії немає.
- Змінна залишається доступною у процедурі після циклу з останнім присвоєним значенням. Запуски мають незалежні позиції. IDE підтримує підказки, шаблони й перехід до оголошення; пауза і зупинка зберігаються.

## Приклади

### 1. Сума без індексу

```vb
# values з верхньою межею 2 містить 2, 4, 6. SumItems отримує масив; item послідовно отримує числа. total зростає від 0 до 12, RETURN передає Integer 12 до Main. NEXT item закриває цей цикл.
Option Explicit On
Function SumItems(values)
    Var total = 0
    For Each item In values
        total += item
    Next item
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return SumItems(values)
End Sub
```

**Пояснення параметрів і виконання:**

values з верхньою межею 2 містить 2, 4, 6. SumItems отримує масив; item послідовно отримує числа. total зростає від 0 до 12, RETURN передає Integer 12 до Main. NEXT item закриває цей цикл.

### 2. Одне обчислення і перетворення

```vb
# calls передається ByRef до SelectItems і стає 1. Повертається ["2", "3"]. AS Integer перетворює рядки на 2 і 3, total=5. item=100 не змінює джерело чи порядок. Main повертає calls*100+total, Integer 105.
Option Explicit On
Function SelectItems(ByRef calls)
    calls += 1
    Dim values[1]
    values[0] = "2"
    values[1] = "3"
    Return values
End Function
Sub Main()
    Var calls = 0
    Var total = 0
    For Each item As Integer In SelectItems(calls)
        total += item
        item = 100
    Next
    Return calls * 100 + total
End Sub
```

**Пояснення параметрів і виконання:**

calls передається ByRef до SelectItems і стає 1. Повертається ["2", "3"]. AS Integer перетворює рядки на 2 і 3, total=5. item=100 не змінює джерело чи порядок. Main повертає calls*100+total, Integer 105.

### 3. Вкладені масиви

```vb
# rows[1][1] має два рядки по дві комірки. row отримує посилання на рядок, cell — 1, 2, 3, 4. Кожен NEXT завершує свій цикл. SumGrid і Main повертають Integer 10; ID чи кількість предметів не обчислюються автоматично.
Option Explicit On
Function SumGrid(rows)
    Var total = 0
    For Each row In rows
        For Each cell In row
            total += cell
        Next cell
    Next row
    Return total
End Function
Sub Main()
    Dim rows[1][1]
    rows[0][0] = 1
    rows[0][1] = 2
    rows[1][0] = 3
    rows[1][1] = 4
    Return SumGrid(rows)
End Sub
```

**Пояснення параметрів і виконання:**

rows[1][1] має два рядки по дві комірки. row отримує посилання на рядок, cell — 1, 2, 3, 4. Кожен NEXT завершує свій цикл. SumGrid і Main повертають Integer 10; ID чи кількість предметів не обчислюються автоматично.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
