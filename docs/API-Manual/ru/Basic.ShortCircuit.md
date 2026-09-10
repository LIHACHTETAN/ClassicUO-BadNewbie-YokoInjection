# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

AndAlso и OrElse соединяют условия и пропускают ненужный правый операнд. AndAlso пропускает его, если слева ложь; OrElse — если слева истина. Так можно защитить обращение к массиву и избежать лишних вызовов.

## Точный синтаксис

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## Параметры

- `left` — left: выражение, вычисляемое первым и один раз. Ноль Integer или Decimal означает ложь, любое ненулевое числовое значение — истину.
- `right` — right: выражение, вычисляемое один раз только при необходимости. Пропущенные обращения к массиву, вызовы функций и их действия не выполняются. Вычисленный операнд должен быть числовым; текст явно преобразуйте через CBool.

## Возвращает

Integer 1 (TRUE) или 0 (FALSE), а не исходный операнд. Допустимы сравнения result=1 и result=TRUE, result=0 и result=FALSE. В движке истина равна 1, в отличие от числового -1 в VB.NET. Обычное количество остаётся количеством; логическое преобразование относится к этой операции.

## Поведение

- Сравнения вычисляются внутри операндов. AndAlso имеет приоритет над OrElse; одинаковые операторы идут слева направо. Скобки меняют группировку. Пропущенное выражение всё равно разбирается и проверяется Option Explicit.
- Для совместимости соседние AND/OR/XOR сохраняют прежнюю группировку слева направо с вычислением обеих частей внутри операнда, до AndAlso/OrElse. Поэтому TRUE OR FALSE AndAlso FALSE даёт FALSE, а TRUE OrElse FALSE AND FALSE — TRUE. Смешивая старые и новые операторы, ставьте скобки. AND, OR, && и || продолжают вычислять обе стороны.
- Движок получает левое значение, проверяет его числовую истинность и либо возвращает логический результат, либо вычисляет нужное правое выражение. Ошибки вычисляемой части передаются в CATCH; FINALLY и проверки паузы/остановки сохраняются. Пропуск вызова означает пропуск всех его действий.

## Примеры

### 1. Безопасно проверить первый элемент

```vb
# FirstEquals получает items и expected. Сначала проверяется GetArrayLength(items)>0: у пустого массива items[0] не читается. Main передаёт [42] и пустой массив, получает 1 и 0 и возвращает 10. Вспомогательная функция приведена целиком, возвращает логический результат и не меняет массив.
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

**Разбор параметров и выполнения:**

FirstEquals получает items и expected. Сначала проверяется GetArrayLength(items)>0: у пустого массива items[0] не читается. Main передаёт [42] и пустой массив, получает 1 и 0 и возвращает 10. Вспомогательная функция приведена целиком, возвращает логический результат и не меняет массив.

### 2. Запасной вызов один раз

```vb
# Probe увеличивает calls через ByRef и возвращает TRUE. TRUE OrElse Probe(calls) пропускает Probe; FALSE OrElse Probe(calls) вызывает его один раз. Оба условия возвращают 1, а Main возвращает итоговое количество вызовов — 1.
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

**Разбор параметров и выполнения:**

Probe увеличивает calls через ByRef и возвращает TRUE. TRUE OrElse Probe(calls) пропускает Probe; FALSE OrElse Probe(calls) вызывает его один раз. Оба условия возвращают 1, а Main возвращает итоговое количество вызовов — 1.

### 3. Защитить деление и показать приоритет

```vb
# AverageExceeds(total, count, limit) делит total на count только при count>0. Аргументы (25,0,10) дают 0, (25,2,10) дают 1, поскольку 12.5>10. TRUE OrElse FALSE AndAlso FALSE даёт 1: правая группа AndAlso пропускается. Main возвращает "0:1:1".
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

**Разбор параметров и выполнения:**

AverageExceeds(total, count, limit) делит total на count только при count>0. Аргументы (25,0,10) дают 0, (25,2,10) дают 1, поскольку 12.5>10. TRUE OrElse FALSE AndAlso FALSE даёт 1: правая группа AndAlso пропускается. Main возвращает "0:1:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
