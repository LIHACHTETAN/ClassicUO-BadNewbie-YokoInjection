# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

For Each по порядку перебирает элементы массива или перечисляемой нативной коллекции без числового индекса. Это оператор цикла внутри процедуры или функции, а не вызываемая команда API.

## Точный синтаксис

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## Параметры

- `item` — item: переменная перебора. Используется существующая локальная переменная, параметр или доступное поле; иначе создаётся локальная переменная процедуры, в том числе с Option Explicit On. В константу записывать нельзя.
- `type` — type: необязательный AS type, например Integer. Объявляет локальную переменную перебора и преобразует каждый элемент при присваивании. Без AS существующая переменная сохраняет объявленный тип.
- `collection` — collection: выражение вычисляется один раз при входе. Допускаются массив и нативный объект с поддержкой перечисления. Число или строка сами по себе недопустимы. Вложенный массив выдаёт сначала строки; для ячеек нужен вложенный цикл.
- `statements / NEXT item` — statements / NEXT item: тело и завершение цикла. Имя после NEXT необязательно; указанное имя должно совпадать с переменной перебора. NEXT пишется отдельной строкой.

## Возвращает

For Each и Next не возвращают значения. В item попадает значение элемента; это не автоматически индекс, длина массива, ID предмета или количество в стопке. Всё зависит от содержимого коллекции. RETURN внутри тела завершает всю функцию с указанным значением; примеры возвращают Integer 12, 105 и 10.

## Поведение

- При подготовке FOR EACH связывается с NEXT, структура проверяется до выполнения инициализаторов. Несовпадающий NEXT даёт SC020. После однократного вычисления collection движок хранит ссылку и отдельную позицию перебора; изменение item не передвигает эту позицию.
- Массив обходится по возрастанию индексов. Пустой массив пропускает тело и сохраняет прежнее значение существующей переменной без AS. Неинициализированный элемент вызывает перехватываемую ошибку; ошибки преобразования AS тоже можно обработать через Catch.
- Присваивание item меняет переменную, а не элемент массива. Вложенные массивы и объекты передаются ссылками: изменение ячейки row изменяет саму строку. Новое присваивание переменной collection не переключает текущий перебор; изменения следующих элементов того же массива будут видны при чтении.
- Continue For переходит к следующему элементу ближайшего For или For Each; Exit For выходит из него. При ошибке, RETURN или остановке нативный перечислитель освобождается. Нативная коллекция может запрещать изменения во время обхода; автоматической копии коллекции нет.
- Переменная доступна в своей процедуре после цикла и хранит последнее присвоенное значение. Разные запуски имеют отдельные позиции перебора. IDE подсказывает имя переменной, вставляет шаблоны циклов и переходит к объявлению; проверка паузы и остановки сохраняется.

## Примеры

### 1. Сумма массива без индекса

```vb
# values имеет верхнюю границу 2: три элемента 2, 4, 6. SumItems получает массив; item по очереди содержит каждое число. total начинается с 0 и становится 12. RETURN передаёт Integer 12 в Main. NEXT item закрывает именно этот перебор.
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

**Разбор параметров и выполнения:**

values имеет верхнюю границу 2: три элемента 2, 4, 6. SumItems получает массив; item по очереди содержит каждое число. total начинается с 0 и становится 12. RETURN передаёт Integer 12 в Main. NEXT item закрывает именно этот перебор.

### 2. Однократный вызов и преобразование

```vb
# calls передаётся ByRef в SelectItems и становится 1. Функция возвращает ["2", "3"]. AS Integer преобразует строки в 2 и 3, total становится 5. item=100 не меняет массив и порядок обхода. Main возвращает calls*100+total, Integer 105.
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

**Разбор параметров и выполнения:**

calls передаётся ByRef в SelectItems и становится 1. Функция возвращает ["2", "3"]. AS Integer преобразует строки в 2 и 3, total становится 5. item=100 не меняет массив и порядок обхода. Main возвращает calls*100+total, Integer 105.

### 3. Вложенные массивы

```vb
# rows[1][1] содержит две строки по две ячейки. row получает ссылку на строку, затем cell получает 1, 2, 3, 4. Каждый NEXT закрывает свой цикл. SumGrid и Main возвращают Integer 10. ID и количество предметов автоматически не вычисляются.
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

**Разбор параметров и выполнения:**

rows[1][1] содержит две строки по две ячейки. row получает ссылку на строку, затем cell получает 1, 2, 3, 4. Каждый NEXT закрывает свой цикл. SumGrid и Main возвращают Integer 10. ID и количество предметов автоматически не вычисляются.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
