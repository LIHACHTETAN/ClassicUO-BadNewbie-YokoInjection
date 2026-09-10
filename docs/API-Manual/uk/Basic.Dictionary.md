# Dictionary

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Dictionary() створює словник ключ → значення. Викликайте методи отриманого об’єкта. Числові й текстові ключі різні; "ore" та "Ore" — різні ключі.

## Точний синтаксис

```text
Dictionary() -> Object:Dictionary
Dictionary(source:Dictionary) -> Object:Dictionary
values.Add(key:String/Number, value:Any) -> Unit
values.Item(key:String/Number) -> Any
values[key] = value
values.Set(key:String/Number, value:Any) -> Unit
values.Get(key:String/Number, fallback:Any) -> Any
values.Count() -> Integer
values.ContainsKey(key:String/Number) -> Integer:1/0
values.Remove(key:String/Number) -> Integer:1/0
values.Clear() -> Unit
values.Keys() -> Array
values.Values() -> Array
entry.Key() -> String/Number
entry.Value() -> Any
```

## Параметри

- `source` — source: без аргументу створюється порожня колекція. List приймає масив чи List, Dictionary — інший Dictionary. Копіюється зовнішній контейнер, вкладені об’єкти й масиви лишаються спільними посиланнями.
- `index / key` — index / key: позиція List — ціле число від 0; Insert також дозволяє Count(). Ключ Dictionary — текст чи скінченне число. Числові 1 та 1.0 є одним ключем, рядок "1" — іншим.
- `value` — value: ініціалізоване значення Basic, зокрема масив або вкладена колекція. Unit зберігати не можна. Порівнюються числа, текст з урахуванням регістру або тотожність посилань.
- `fallback` — fallback: Get повертає запасне значення за відсутності ключа, не додаючи його. Усі аргументи, зокрема вираз fallback, обчислюються до виклику методу.

## Повертає

Конструктор повертає Object:Dictionary. Item/індекс/Get повертають значення; Count — кількість ключів. ContainsKey/Remove повертають 1=TRUE чи 0=FALSE. Add/Set/Clear повертають Unit; Keys/Values — нові Array. For Each видає записи: Key() повертає ключ, Value() — значення.

## Поведінка

- Add відхиляє наявний ключ без перезапису. Set/індекс створює або замінює значення. Item/індекс потребує наявного ключа; Get має запасне значення. Remove повертає 0, коли ключа немає; Clear очищає словник.
- NaN, нескінченність, масиви, об’єкти та Unit не можуть бути ключами. Порядок ключів не гарантується. Кожен запис перебору зберігає власну пару й не змінюється на наступній ітерації.
- Keys/Values повертають поверхневі копії. Для видалення/заміни під час перебору використовуйте Keys(); For Each самого словника видає об’єкти записів.
- Зміна колекції під час прямого For Each, включно з Set, викликає перехоплювану помилку на наступному кроці. Try/Finally коректно виконує вихід. Невдала зміна зберігає старі дані.
- Псевдоніми й аргументи ByVal мають спільну колекцію. Конструктор копії та знімки копіюють лише зовнішній контейнер. Індексований ByRef і складене присвоєння обчислюють контейнер/ключ один раз; заміна змінної не змінює місце запису.
- Це локальні дані скрипту: методи не пересувають ігрові предмети й не звертаються до мережі. Стос, збережений одним елементом, займає одну позицію списку.

## Приклади

### 1. Тип ключа й запасне значення

```vb
# "ore" змінюється з 5 на 8. Числовий ключ 1 зберігає 2, текстовий "1" — 3. Get("wood",7) повертає 7 без додавання ключа. Main повертає 8*100+2*10+3+7, Integer 830.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**Пояснення параметрів і виконання:**

"ore" змінюється з 5 на 8. Числовий ключ 1 зберігає 2, текстовий "1" — 3. Get("wood",7) повертає 7 без додавання ключа. Main повертає 8*100+2*10+3+7, Integer 830.

### 2. Записи, знімки та видалення

```vb
# Сума двох значень дорівнює 5. Знімок Keys() дозволяє видаляти під час перебору. copied зберігає ore=2, snapshot — два значення. Після Clear Count()=0. Main повертає 5*100+2*10+2+0, Integer 522.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 2)
    values.Add("wood", 3)
    Var copied = Dictionary(values)
    Var snapshot = values.Values()
    Var total = 0
    For Each entry In values
        If values.ContainsKey(entry.Key()) Then
            total += entry.Value()
        End If
    Next
    For Each key In values.Keys()
        values.Remove(key)
    Next
    values.Clear()
    Return total*100 + copied["ore"]*10 + GetArrayLength(snapshot) + values.Count()
End Sub
```

**Пояснення параметрів і виконання:**

Сума двох значень дорівнює 5. Знімок Keys() дозволяє видаляти під час перебору. copied зберігає ore=2, snapshot — два значення. Після Clear Count()=0. Main повертає 5*100+2*10+2+0, Integer 522.

### 3. Повторний ключ та обробка помилки

```vb
# Перший Add зберігає ore=4. Другий Add зі значенням 7 викликає помилку; Catch задає caught=1. Початкове ore=4 лишається. Main повертає 4*10+1, Integer 41.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 4)
    Var caught = 0
    Try
        values.Add("ore", 7)
    Catch problem
        caught = 1
    End Try
    Return values["ore"]*10 + caught
End Sub
```

**Пояснення параметрів і виконання:**

Перший Add зберігає ore=4. Другий Add зі значенням 7 викликає помилку; Catch задає caught=1. Початкове ore=4 лишається. Main повертає 4*10+1, Integer 41.

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/DictionaryObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-8.0
-->
