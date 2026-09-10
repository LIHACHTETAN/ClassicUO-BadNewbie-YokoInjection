# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

AndAlso та OrElse поєднують умови, пропускаючи непотрібний правий операнд. AndAlso пропускає його, коли ліворуч хибність; OrElse — коли істина. Це захищає доступ до масиву й усуває зайві виклики.

## Точний синтаксис

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## Параметри

- `left` — left: вираз, що обчислюється першим і один раз. Нуль Integer або Decimal означає хибність, будь-яке ненульове число — істину.
- `right` — right: вираз, що обчислюється один раз лише за потреби. Пропущені читання масиву, виклики та їхні дії не відбуваються. Обчислений операнд має бути числовим; текст явно перетворюйте через CBool.

## Повертає

Integer 1 (TRUE) або 0 (FALSE), а не початковий операнд. Можна порівнювати result=1 або result=TRUE, result=0 або result=FALSE. У рушії істина — 1, на відміну від числового -1 у VB.NET. Звичайна кількість лишається кількістю; логічне перетворення стосується цієї операції.

## Поведінка

- Порівняння обчислюються всередині операндів. AndAlso має пріоритет над OrElse; однакові оператори йдуть зліва направо. Дужки змінюють групування. Пропущений вираз усе одно розбирається й перевіряється Option Explicit.
- Для сумісності суміжні AND/OR/XOR зберігають попереднє групування зліва направо з обчисленням обох частин усередині операнда, перед AndAlso/OrElse. TRUE OR FALSE AndAlso FALSE дає FALSE; TRUE OrElse FALSE AND FALSE — TRUE. Змішуючи старі й нові оператори, ставте дужки. AND, OR, && та || обчислюють обидві сторони.
- Рушій обчислює ліве значення, перевіряє числову істинність і повертає логічний результат або обчислює потрібну праву частину. Помилки обчислюваної частини потрапляють у CATCH; FINALLY і перевірки паузи/зупинки зберігаються. Пропущений виклик не виконує жодних своїх дій.

## Приклади

### 1. Перевірити перший елемент безпечно

```vb
# FirstEquals отримує items та expected. Спочатку перевіряється GetArrayLength(items)>0, тому для порожнього масиву items[0] не читається. Main передає [42] і порожній масив, отримує 1 та 0 й повертає 10. Повністю наведена функція не змінює масив.
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**Пояснення параметрів і виконання:**

FirstEquals отримує items та expected. Спочатку перевіряється GetArrayLength(items)>0, тому для порожнього масиву items[0] не читається. Main передає [42] і порожній масив, отримує 1 та 0 й повертає 10. Повністю наведена функція не змінює масив.

### 2. Запасний виклик один раз

```vb
# Probe збільшує calls через ByRef і повертає TRUE. TRUE OrElse Probe(calls) пропускає виклик; FALSE OrElse Probe(calls) викликає його один раз. Обидві умови дають 1, а Main повертає кількість викликів — 1.
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**Пояснення параметрів і виконання:**

Probe збільшує calls через ByRef і повертає TRUE. TRUE OrElse Probe(calls) пропускає виклик; FALSE OrElse Probe(calls) викликає його один раз. Обидві умови дають 1, а Main повертає кількість викликів — 1.

### 3. Захистити ділення та пояснити пріоритет

```vb
# AverageExceeds(total, count, limit) ділить лише при count>0. (25,0,10) дає 0; (25,2,10) дає 1, бо 12.5>10. TRUE OrElse FALSE AndAlso FALSE дає 1, пропускаючи праву групу AndAlso. Main повертає "0:1:1".
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**Пояснення параметрів і виконання:**

AverageExceeds(total, count, limit) ділить лише при count>0. (25,0,10) дає 0; (25,2,10) дає 1, бо 12.5>10. TRUE OrElse FALSE AndAlso FALSE дає 1, пропускаючи праву групу AndAlso. Main повертає "0:1:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
