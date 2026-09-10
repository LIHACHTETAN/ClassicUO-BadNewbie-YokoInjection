# List

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

List() створює впорядкований список змінної довжини. Збережіть об’єкт у змінній: items.Add є методом об’єкта, окремої глобальної команди List.Add немає.

## Точний синтаксис

```text
List() -> Object:List
List(source:Array/List) -> Object:List
items.Add(value:Any) -> Unit
items.Insert(index:Number, value:Any) -> Unit
items.Item(index:Number) -> Any
items[index] = value
items.Set(index:Number, value:Any) -> Unit
items.Count() -> Integer
items.Contains(value:Any) -> Integer:1/0
items.IndexOf(value:Any) -> Integer:index/-1
items.Remove(value:Any) -> Integer:1/0
items.RemoveAt(index:Number) -> Unit
items.Clear() -> Unit
items.ToArray() -> Array
```

## Параметри

- `source` — source: без аргументу створюється порожня колекція. List приймає масив чи List, Dictionary — інший Dictionary. Копіюється зовнішній контейнер, вкладені об’єкти й масиви лишаються спільними посиланнями.
- `index / key` — index / key: позиція List — ціле число від 0; Insert також дозволяє Count(). Ключ Dictionary — текст чи скінченне число. Числові 1 та 1.0 є одним ключем, рядок "1" — іншим.
- `value` — value: ініціалізоване значення Basic, зокрема масив або вкладена колекція. Unit зберігати не можна. Порівнюються числа, текст з урахуванням регістру або тотожність посилань.
- `fallback` — fallback: Get повертає запасне значення за відсутності ключа, не додаючи його. Усі аргументи, зокрема вираз fallback, обчислюються до виклику методу.

## Повертає

Конструктор повертає Object:List. Item та індекс повертають збережене значення. Count — кількість елементів, IndexOf — позиція від 0 або -1. Contains/Remove повертають 1=TRUE чи 0=FALSE. Add/Insert/Set/RemoveAt/Clear повертають Unit; ToArray — новий Array.

## Поведінка

- Add додає в кінець, Insert вставляє перед позицією, Set/індекс замінює наявний елемент. Item/індекс читає його. Remove видаляє перше рівне значення, RemoveAt — позицію, Clear — весь вміст.
- Contains перевіряє наявність, IndexOf знаходить перший збіг. Від’ємний, дробовий, текстовий індекс чи вихід за межі дає перехоплювану помилку без зміни списку.
- For Each зберігає порядок списку. ToArray створює поверхневу копію: перебирайте її, коли змінюєте початковий список.
- Зміна колекції під час прямого For Each, включно з Set, викликає перехоплювану помилку на наступному кроці. Try/Finally коректно виконує вихід. Невдала зміна зберігає старі дані.
- Псевдоніми й аргументи ByVal мають спільну колекцію. Конструктор копії та знімки копіюють лише зовнішній контейнер. Індексований ByRef і складене присвоєння обчислюють контейнер/ключ один раз; заміна змінної не змінює місце запису.
- Це локальні дані скрипту: методи не пересувають ігрові предмети й не звертаються до мережі. Стос, збережений одним елементом, займає одну позицію списку.

## Приклади

### 1. Створення списку й сума

```vb
# Add створює [3,7], Insert(1,5) — [3,5,7], Set(0,2) — [2,5,7]. For Each додає три значення. Main повертає Integer 14.
Option Explicit On
Sub Main()
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

Add створює [3,7], Insert(1,5) — [3,5,7], Set(0,2) — [2,5,7]. For Each додає три значення. Main повертає Integer 14.

### 2. Незалежні копії та знімок

```vb
# seed=[4,6]. copied і snapshot зберігають ці значення. Початковий список стає [9,6]; Remove(6) повертає TRUE=1, RemoveAt(0) спустошує його, Clear залишає порожнім. Main повертає 4*100+6*10+1+0, Integer 461.
Option Explicit On
Sub Main()
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

seed=[4,6]. copied і snapshot зберігають ці значення. Початковий список стає [9,6]; Remove(6) повертає TRUE=1, RemoveAt(0) спустошує його, Clear залишає порожнім. Main повертає 4*100+6*10+1+0, Integer 461.

### 3. Пошук і зміна через ByRef

```vb
# NextIndex викликається один раз: calls=1, індекс 0. Bump змінює 5 на 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) повертає 6. Main повертає Integer 601.
Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
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

NextIndex викликається один раз: calls=1, індекс 0. Bump змінює 5 на 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) повертає 6. Main повертає Integer 601.

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/ListObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-8.0
-->
