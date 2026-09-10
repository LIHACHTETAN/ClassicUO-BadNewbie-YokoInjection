# List

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

List() создаёт упорядоченный список изменяемой длины. Сохраните полученный объект в переменную: items.Add — метод объекта, отдельной глобальной команды List.Add нет.

## Точный синтаксис

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

## Параметры

- `source` — source: без аргумента создаётся пустая коллекция. List принимает массив или List; Dictionary — другой Dictionary. Копируется внешний контейнер, вложенные объекты и массивы остаются общими ссылками.
- `index / key` — index / key: позиция List — целое числовое значение от 0; Insert допускает также Count(). Ключ Dictionary — текст или конечное число. Числовые 1 и 1.0 — один ключ, строка "1" — другой.
- `value` — value: инициализированное значение Basic, включая массивы и вложенные коллекции. Unit хранить нельзя. Сравниваются числовые значения, текст с учётом регистра либо идентичность ссылок массивов/объектов.
- `fallback` — fallback: Get возвращает это значение при отсутствии ключа, не добавляя его. Все аргументы, включая выражение fallback, вычисляются до вызова метода.

## Возвращает

Конструктор возвращает Object:List. Item и чтение индекса возвращают хранимое значение. Count — количество элементов, IndexOf — позиция от 0 либо -1. Contains/Remove возвращают 1=TRUE или 0=FALSE. Add/Insert/Set/RemoveAt/Clear возвращают Unit. ToArray — новый Array.

## Поведение

- Add добавляет в конец; Insert вставляет перед позицией; Set или запись по индексу заменяет существующий элемент. Item и индекс читают его. Remove удаляет первое равное значение, RemoveAt — элемент по позиции, Clear — всё содержимое.
- Contains проверяет наличие, IndexOf ищет первое совпадение. Отрицательный, дробный, текстовый или выходящий за границы индекс вызывает перехватываемую ошибку без изменения списка.
- For Each сохраняет порядок списка. ToArray создаёт поверхностную копию: перебирайте её, если одновременно меняете исходный список.
- Изменение коллекции во время непосредственного For Each, включая Set, вызывает перехватываемую ошибку на следующем шаге. Try/Finally выполняет выход корректно. Неудачное изменение сохраняет прежние данные.
- Псевдонимы и аргументы ByVal используют общую коллекцию. Конструктор копии и снимки копируют только внешний контейнер. Индексированный ByRef и составное присваивание вычисляют контейнер/ключ один раз; замена переменной не перенаправляет запись.
- Это локальные данные скрипта: методы не переносят предметы в игре и не обращаются к сети. Стопка, сохранённая одним элементом, занимает одну позицию списка.

## Примеры

### 1. Создание списка и сумма

```vb
# Add создаёт [3,7]; Insert(1,5) — [3,5,7]; Set(0,2) — [2,5,7]. For Each суммирует три значения. Main возвращает Integer 14.
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

**Разбор параметров и выполнения:**

Add создаёт [3,7]; Insert(1,5) — [3,5,7]; Set(0,2) — [2,5,7]. For Each суммирует три значения. Main возвращает Integer 14.

### 2. Независимые копии и снимок

```vb
# seed=[4,6]. copied и snapshot сохраняют эти значения. Исходный список становится [9,6]; Remove(6) возвращает TRUE=1, RemoveAt(0) опустошает его, Clear оставляет пустым. Main возвращает 4*100+6*10+1+0, Integer 461.
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

**Разбор параметров и выполнения:**

seed=[4,6]. copied и snapshot сохраняют эти значения. Исходный список становится [9,6]; Remove(6) возвращает TRUE=1, RemoveAt(0) опустошает его, Clear оставляет пустым. Main возвращает 4*100+6*10+1+0, Integer 461.

### 3. Поиск и изменение через ByRef

```vb
# NextIndex вызывается один раз: calls=1, индекс 0. Bump меняет хранимое 5 на 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) возвращает 6. Main возвращает Integer 601.
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

**Разбор параметров и выполнения:**

NextIndex вызывается один раз: calls=1, индекс 0. Bump меняет хранимое 5 на 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) возвращает 6. Main возвращает Integer 601.

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/ListObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-8.0
-->
