# Dictionary

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Dictionary() создаёт словарь ключ → значение. Методы вызываются у полученного объекта. Числовые и текстовые ключи различаются; "ore" и "Ore" — разные ключи.

## Точный синтаксис

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

## Параметры

- `source` — source: без аргумента создаётся пустая коллекция. List принимает массив или List; Dictionary — другой Dictionary. Копируется внешний контейнер, вложенные объекты и массивы остаются общими ссылками.
- `index / key` — index / key: позиция List — целое числовое значение от 0; Insert допускает также Count(). Ключ Dictionary — текст или конечное число. Числовые 1 и 1.0 — один ключ, строка "1" — другой.
- `value` — value: инициализированное значение Basic, включая массивы и вложенные коллекции. Unit хранить нельзя. Сравниваются числовые значения, текст с учётом регистра либо идентичность ссылок массивов/объектов.
- `fallback` — fallback: Get возвращает это значение при отсутствии ключа, не добавляя его. Все аргументы, включая выражение fallback, вычисляются до вызова метода.

## Возвращает

Конструктор возвращает Object:Dictionary. Item, чтение индекса и Get возвращают значение; Count — количество ключей. ContainsKey/Remove возвращают 1=TRUE или 0=FALSE. Add/Set/Clear возвращают Unit; Keys/Values — новые Array. For Each выдаёт записи: Key() возвращает ключ, Value() — значение.

## Поведение

- Add не перезаписывает существующий ключ, а выдаёт ошибку. Set и запись по ключу добавляют или заменяют значение. Item/индекс требуют наличия ключа, Get допускает запасное значение. Remove возвращает 0, если ключа нет; Clear очищает словарь.
- NaN, бесконечность, массивы, объекты и Unit не допускаются как ключи. Порядок ключей не гарантируется. Каждая запись перебора сохраняет собственную пару; сохранённая запись не меняется на следующей итерации.
- Keys/Values возвращают поверхностные копии. Для удаления/замены при переборе используйте Keys(); For Each по самому словарю выдаёт объекты записей.
- Изменение коллекции во время непосредственного For Each, включая Set, вызывает перехватываемую ошибку на следующем шаге. Try/Finally выполняет выход корректно. Неудачное изменение сохраняет прежние данные.
- Псевдонимы и аргументы ByVal используют общую коллекцию. Конструктор копии и снимки копируют только внешний контейнер. Индексированный ByRef и составное присваивание вычисляют контейнер/ключ один раз; замена переменной не перенаправляет запись.
- Это локальные данные скрипта: методы не переносят предметы в игре и не обращаются к сети. Стопка, сохранённая одним элементом, занимает одну позицию списка.

## Примеры

### 1. Тип ключа и запасное значение

```vb
# "ore" меняется с 5 на 8. Числовой ключ 1 хранит 2, текстовый "1" — 3. Get("wood",7) возвращает 7 без добавления ключа. Main возвращает 8*100+2*10+3+7, Integer 830.
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

**Разбор параметров и выполнения:**

"ore" меняется с 5 на 8. Числовой ключ 1 хранит 2, текстовый "1" — 3. Get("wood",7) возвращает 7 без добавления ключа. Main возвращает 8*100+2*10+3+7, Integer 830.

### 2. Записи, снимки и удаление

```vb
# Значения двух записей дают сумму 5. Снимок Keys() позволяет удалять при переборе. copied сохраняет ore=2, snapshot — два значения. После Clear Count()=0. Main возвращает 5*100+2*10+2+0, Integer 522.
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

**Разбор параметров и выполнения:**

Значения двух записей дают сумму 5. Снимок Keys() позволяет удалять при переборе. copied сохраняет ore=2, snapshot — два значения. После Clear Count()=0. Main возвращает 5*100+2*10+2+0, Integer 522.

### 3. Повторный ключ и обработка ошибки

```vb
# Первый Add сохраняет ore=4. Второй Add со значением 7 вызывает ошибку; Catch устанавливает caught=1. Исходное ore=4 сохраняется. Main возвращает 4*10+1, Integer 41.
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

**Разбор параметров и выполнения:**

Первый Add сохраняет ore=4. Второй Add со значением 7 вызывает ошибку; Catch устанавливает caught=1. Исходное ore=4 сохраняется. Main возвращает 4*10+1, Integer 41.

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/DictionaryObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-8.0
-->
