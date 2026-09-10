# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

For повторяет блок по числовому диапазону, включая достижимую границу. Подходит для индексов массива и заданного числа операций; For Each перебирает сами значения элементов.

## Точный синтаксис

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## Параметры

- `counter / VAR` — Числовая переменная счётчика. VAR объявляет её внутри процедуры; без VAR используется доступная переменная. При Option Explicit On объявите её заранее либо напишите For Var. Тип задавайте отдельно: DIM counter AS Integer; AS в заголовке числового For не поддерживается.
- `start` — Начальное числовое выражение. Вычисляется один раз и присваивается счётчику до вычисления limit и increment.
- `limit` — Конечная включённая граница, вычисляемая один раз при входе. При положительном шаге проверяется counter <= limit, при отрицательном — counter >= limit.
- `increment` — Необязательный числовой шаг; по умолчанию 1. Допустимы отрицательные и дробные значения; ноль вызывает перехватываемую ошибку. Тип счётчика должен допускать шаг и продвижение.
- `statements / Next / exit` — Тело и Next пишутся на отдельных строках. Имя после Next необязательно, но должно совпадать со счётчиком. Continue For переходит к следующему шагу; Exit For выходит из ближайшего For/For Each, Break — из ближайшего цикла любого вида.

## Возвращает

For, Next и Exit For ничего не возвращают. Счётчик — число, а не автоматически ID предмета. После обычного завершения этот движок оставляет последнее использованное значение, а не значение за границей. При пропуске цикла остаётся start, при досрочном выходе — текущее значение. Примеры возвращают из Main Integer 12, 28 и 395.

## Поведение

- При входе: присвоить start, сохранить limit и шаг, отклонить нулевой шаг, проверить первое значение. Если направление шага не ведёт к границе, тело пропускается. При start=limit тело выполняется один раз.
- Next проверяет counter+step и присваивает его только для следующей допустимой итерации. Поэтому 1 To 5 Step 3 даёт 1 и 4. Изменение исходных переменных limit/step не меняет сохранённые границы; изменение самого счётчика влияет на следующий шаг.
- Структура и имя Next проверяются до выполнения; ошибка структуры — SC020. Вложенным циклам нужны разные счётчики. При выходе из Try выполняется Finally. Пауза и остановка доступны; автоматической задержки и таймаута у For нет.

## Примеры

### 1. Сумма ячеек массива

```vb
# values[2] создаёт индексы 0, 1, 2 со значениями 2, 4, 6. Sum получает массив ByVal, начинает с index=0 и сохраняет границу length-1=2. Шаг по умолчанию 1 посещает три ячейки; total=12 возвращается в Main.
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

**Разбор параметров и выполнения:**

values[2] создаёт индексы 0, 1, 2 со значениями 2, 4, 6. Sum получает массив ByVal, начинает с index=0 и сохраняет границу length-1=2. Шаг по умолчанию 1 посещает три ячейки; total=12 возвращается в Main.

### 2. Удаление с конца

```vb
# В items находятся -1, 3, -2, 5. Начало Count()-1=3, граница 0, шаг -1. Удаление отрицательного элемента сдвигает только уже просмотренные индексы, поэтому ожидающий обработки элемент не пропускается. Остаются 3 и 5; Count()*10+3+5 возвращает 28.
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

**Разбор параметров и выполнения:**

В items находятся -1, 3, -2, 5. Начало Count()-1=3, граница 0, шаг -1. Удаление отрицательного элемента сдвигает только уже просмотренные индексы, поэтому ожидающий обработки элемент не пропускается. Остаются 3 и 5; Count()*10+3+5 возвращает 28.

### 3. Сохранённые границы и итоговый счётчик

```vb
# ReadLimit увеличивает calls через ByRef и возвращает value. Начало 1, граница 5 и шаг 2 вычисляются по одному разу: calls=3. Присваивания upper=99 и stride=1 внутри тела не меняют этот цикл. Он посещает 1, 3, 5; total=9, index остаётся 5. Main возвращает 300+90+5=395.
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

**Разбор параметров и выполнения:**

ReadLimit увеличивает calls через ByRef и возвращает value. Начало 1, граница 5 и шаг 2 вычисляются по одному разу: calls=3. Присваивания upper=99 и stride=1 внутри тела не меняют этот цикл. Он посещает 1, 3, 5; total=9, index остаётся 5. Main возвращает 300+90+5=395.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
