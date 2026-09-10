# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

DIM створює динамічний масив; REDIM замінює його сховище. PRESERVE копіює значення за спільними індексами. Розмірність задає включну верхню межу, а не кількість елементів. Перед читанням заповніть комірки.

## Точний синтаксис

```text
DIM name[upper]
DIM name(upper) AS type
DIM grid[xUpper][yUpper]
DIM grid(xUpper, yUpper)
REDIM name[upper]
REDIM PRESERVE name[upper]
name[index] = value
GetArrayLength(name)
```

## Параметри

- `name` — name: ім’я масиву. DIM оголошує його; REDIM записує нове сховище в наявну змінну. Читання й запис: items[i], grid[x][y], у квадратних дужках.
- `upper` — upper: вираз, що перетворюється на Integer й обчислюється один раз зліва направо. DIM items[2] створює три комірки, 0..2. -1 дає порожню розмірність; менша межа та переповнення довжини є помилками. Практичний розмір обмежує пам’ять.
- `PRESERVE` — PRESERVE: необов’язкове слово після REDIM. Рекурсивно копіює перетин індексів; при зменшенні значення поза новими межами втрачаються. Без нього комірки не ініціалізовані.
- `AS type` — AS type: дозволена анотація оголошення масиву DIM; не задає тип, початкові значення чи перетворення елементів. Один масив може містити різні види значень.

## Повертає

DIM і REDIM не повертають значення (Unit). items[i] повертає збережене значення його фактичного виду: Integer, Decimal, String, Array або Object. Читання неініціалізованої комірки викликає помилку, а не 0 чи FALSE. GetArrayLength(array) повертає зовнішню довжину як Integer; для не-масиву — 0.

## Поведінка

- В оголошенні дозволені круглі дужки: DIM grid(1, 2) означає grid[1][2], два рядки по три комірки. Виклики функцій у межах зберігаються. Доступ до елемента: grid[1][2]; круглі дужки у виразі означають виклик функції.
- Присвоєння й передавання ByVal копіюють посилання, а не елементи. Зміни спільної комірки видно через інші посилання. REDIM прив’язує новий масив; старі посилання зберігають попередній. PRESERVE копіює спільні координати вкладених масивів, але не клонує довільні об’єкти повністю.
- Індекси починаються з нуля. Ініціалізатор DIM/REDIM, наприклад DIM items[2]=5, відхиляється з SC014: заповнюйте комірки окремими рядками. Хибний індекс і читання відсутнього чи неініціалізованого елемента викликають оброблювані помилки.
- Це діалект Basic проєкту. Динамічні види елементів і багатовимірний PRESERVE відрізняються від типізованих масивів VB.NET. Логічне значення в комірці — 1/0; довільне число чи довжина масиву не є прапорцем успіху.
- RETURN array повертає посилання на масив; дані зберігаються після завершення функції. Присвоєння іншій змінній не копіює елементи. Спільна функція може створити масив для поля Module. Окремі запуски створюють нові масиви при повторному виконанні DIM.

## Приклади

### 1. Сума заповнених елементів

```vb
# Abs(-2) дає верхню межу 2: Main створює 3 комірки й записує 2, 4, 6. Sum отримує спільне посилання ByVal, перебирає 0..GetArrayLength(items)-1 і повертає 12. Повністю наведена функція не змінює комірки та підтримує порожній масив.
Option Explicit On
FUNCTION Sum(ByVal items)
    VAR total = 0
    VAR i = 0
    FOR i = 0 TO GetArrayLength(items) - 1
        total += items[i]
    NEXT
    RETURN total
END FUNCTION
SUB Main()
    DIM items(Abs(-2))
    items[0] = 2
    items[1] = 4
    items[2] = 6
    RETURN Sum(items)
END SUB
```

**Пояснення параметрів і виконання:**

Abs(-2) дає верхню межу 2: Main створює 3 комірки й записує 2, 4, 6. Sum отримує спільне посилання ByVal, перебирає 0..GetArrayLength(items)-1 і повертає 12. Повністю наведена функція не змінює комірки та підтримує порожній масив.

### 2. Збільшити зі збереженням

```vb
# values містить 7 і 8. REDIM PRESERVE values(2) створює 3 комірки та копіює індекси 0 і 1. Нову комірку 2 заповнюємо значенням 9. Main повертає 7*100+8*10+9=789.
Option Explicit On
SUB Main()
    DIM values[1]
    values[0] = 7
    values[1] = 8
    REDIM PRESERVE values(2)
    values[2] = 9
    RETURN values[0] * 100 + values[1] * 10 + values[2]
END SUB
```

**Пояснення параметрів і виконання:**

values містить 7 і 8. REDIM PRESERVE values(2) створює 3 комірки та копіює індекси 0 і 1. Нову комірку 2 заповнюємо значенням 9. Main повертає 7*100+8*10+9=789.

### 3. Спільні посилання та нове сховище

```vb
# grid має два рядки по дві комірки. alias посилається на той самий масив: alias[0][1]=9 змінює і grid. PRESERVE збільшує grid до трьох рядків, зберігає 9, а alias лишається з двома рядками. Результат "9:3:2": значення, нова зовнішня довжина, довжина старого посилання.
Option Explicit On
SUB Main()
    DIM grid[1][1]
    grid[0][1] = 4
    VAR alias = grid
    alias[0][1] = 9
    REDIM PRESERVE grid[2][1]
    RETURN CStr(grid[0][1]) + ":" + CStr(GetArrayLength(grid)) + ":" + CStr(GetArrayLength(alias))
END SUB
```

**Пояснення параметрів і виконання:**

grid має два рядки по дві комірки. alias посилається на той самий масив: alias[0][1]=9 змінює і grid. PRESERVE збільшує grid до трьох рядків, зберігає 9, а alias лишається з двома рядками. Результат "9:3:2": значення, нова зовнішня довжина, довжина старого посилання.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
