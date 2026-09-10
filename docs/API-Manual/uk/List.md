# List

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: uk -->

List() створює впорядкований список змінної довжини. Збережіть об’єкт у змінній: items.Add є методом об’єкта, окремої глобальної команди List.Add немає.

## Точний синтаксис

```text
List() -> Object
List(source:Any) -> Object
```

## Параметри

- `source` — source: без аргументу створюється порожня колекція. List приймає масив чи List, Dictionary — інший Dictionary. Копіюється зовнішній контейнер, вкладені об’єкти й масиви лишаються спільними посиланнями.

## Повертає

Конструктор повертає Object:List. Item та індекс повертають збережене значення. Count — кількість елементів, IndexOf — позиція від 0 або -1. Contains/Remove повертають 1=TRUE чи 0=FALSE. Add/Insert/Set/RemoveAt/Clear повертають Unit; ToArray — новий Array.

## Поведінка

- index / key: позиція List — ціле число від 0; Insert також дозволяє Count(). Ключ Dictionary — текст чи скінченне число. Числові 1 та 1.0 є одним ключем, рядок "1" — іншим.
- value: ініціалізоване значення Basic, зокрема масив або вкладена колекція. Unit зберігати не можна. Порівнюються числа, текст з урахуванням регістру або тотожність посилань.
- fallback: Get повертає запасне значення за відсутності ключа, не додаючи його. Усі аргументи, зокрема вираз fallback, обчислюються до виклику методу.
- Add додає в кінець, Insert вставляє перед позицією, Set/індекс замінює наявний елемент. Item/індекс читає його. Remove видаляє перше рівне значення, RemoveAt — позицію, Clear — весь вміст.
- Contains перевіряє наявність, IndexOf знаходить перший збіг. Від’ємний, дробовий, текстовий індекс чи вихід за межі дає перехоплювану помилку без зміни списку.
- For Each зберігає порядок списку. ToArray створює поверхневу копію: перебирайте її, коли змінюєте початковий список.
- Зміна колекції під час прямого For Each, включно з Set, викликає перехоплювану помилку на наступному кроці. Try/Finally коректно виконує вихід. Невдала зміна зберігає старі дані.
- Псевдоніми й аргументи ByVal мають спільну колекцію. Конструктор копії та знімки копіюють лише зовнішній контейнер. Індексований ByRef і складене присвоєння обчислюють контейнер/ключ один раз; заміна змінної не змінює місце запису.
- Це локальні дані скрипту: методи не пересувають ігрові предмети й не звертаються до мережі. Стос, збережений одним елементом, займає одну позицію списку.

## Приклади

### Створення списку й сума

```vb
# Створення списку й сума
#
# List() створює впорядкований список змінної довжини. Збережіть об’єкт у змінній: items.Add є
# методом об’єкта, окремої глобальної команди List.Add немає.
#
# Конструктор повертає Object:List. Item та індекс повертають збережене значення. Count —
# кількість елементів, IndexOf — позиція від 0 або -1. Contains/Remove повертають 1=TRUE чи
# 0=FALSE. Add/Insert/Set/RemoveAt/Clear повертають Unit; ToArray — новий Array.

Option Explicit On
Sub Main()
    # Add створює [3,7], Insert(1,5) — [3,5,7], Set(0,2) — [2,5,7]. For Each додає три значення.
    # Main повертає Integer 14.

    Var items = List()
    items.Add(3)
    items.Add(7)
    items.Insert(1, 5)
    items.Set(0, 2)
    Var total = 0
    For Each item In items
        total += item
    Next
    Return total
End Sub
```

**Пояснення параметрів і виконання:**

- Add створює [3,7], Insert(1,5) — [3,5,7], Set(0,2) — [2,5,7]. For Each додає три значення. Main повертає Integer 14.

### Незалежні копії та знімок

```vb
# Незалежні копії та знімок
#
# List() створює впорядкований список змінної довжини. Збережіть об’єкт у змінній: items.Add є
# методом об’єкта, окремої глобальної команди List.Add немає.
#
# Конструктор повертає Object:List. Item та індекс повертають збережене значення. Count —
# кількість елементів, IndexOf — позиція від 0 або -1. Contains/Remove повертають 1=TRUE чи
# 0=FALSE. Add/Insert/Set/RemoveAt/Clear повертають Unit; ToArray — новий Array.

Option Explicit On
Sub Main()
    # seed=[4,6]. copied і snapshot зберігають ці значення. Початковий список стає [9,6]; Remove(6)
    # повертає TRUE=1, RemoveAt(0) спустошує його, Clear залишає порожнім. Main повертає
    # 4*100+6*10+1+0, Integer 461.

    Dim seed[1]
    seed[0] = 4
    seed[1] = 6
    Var items = List(seed)
    Var copied = List(items)
    Var snapshot = items.ToArray()
    items[0] = 9
    Var removed = items.Remove(6)
    items.RemoveAt(0)
    items.Clear()
    Return snapshot[0]*100 + copied[1]*10 + removed + items.Count()
End Sub
```

**Пояснення параметрів і виконання:**

- seed=[4,6]. copied і snapshot зберігають ці значення. Початковий список стає [9,6]; Remove(6) повертає TRUE=1, RemoveAt(0) спустошує його, Clear залишає порожнім. Main повертає 4*100+6*10+1+0, Integer 461.

### Пошук і зміна через ByRef

```vb
# Пошук і зміна через ByRef
#
# List() створює впорядкований список змінної довжини. Збережіть об’єкт у змінній: items.Add є
# методом об’єкта, окремої глобальної команди List.Add немає.
#
# Конструктор повертає Object:List. Item та індекс повертають збережене значення. Count —
# кількість елементів, IndexOf — позиція від 0 або -1. Contains/Remove повертають 1=TRUE чи
# 0=FALSE. Add/Insert/Set/RemoveAt/Clear повертають Unit; ToArray — новий Array.

Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    # NextIndex викликається один раз: calls=1, індекс 0. Bump змінює 5 на 6. Contains(6)=TRUE,
    # IndexOf(6)=0, Item(0) повертає 6. Main повертає Integer 601.

    Var items = List()
    items.Add(5)
    Var calls = 0
    Bump(items[NextIndex(calls)])
    If items.Contains(6) AndAlso items.IndexOf(6) = 0 Then
        Return items.Item(0)*100 + calls
    End If
    Return -1
End Sub
```

**Пояснення параметрів і виконання:**

- NextIndex викликається один раз: calls=1, індекс 0. Bump змінює 5 на 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) повертає 6. Main повертає Integer 601.
