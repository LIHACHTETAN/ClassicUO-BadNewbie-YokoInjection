# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

While проверяет условие перед каждой итерацией и повторяет тело, пока оно истинно. В этом движке блок закрывается Wend; написание End While из VB.NET не поддерживается.

## Точный синтаксис

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## Параметры

- `condition` — Выражение проверяется перед каждым проходом, включая первый и завершающий. Используйте сравнение или числовое логическое значение: 0/False завершает цикл, 1/True продолжает; прочие ненулевые числа тоже продолжают. Текст не преобразуется в Boolean.
- `statements` — Команды тела выполняют работу и изменяют условие. Если первая проверка ложна, тело полностью пропускается.
- `Wend / exit` — Wend возвращает к условию. Continue While снова его проверяет; Exit While выходит из ближайшего While, в том числе через вложенный цикл другого вида. Break выходит из ближайшего цикла любого вида.

## Возвращает

While, Wend, Exit While и Break ничего не возвращают. RETURN внутри тела завершает всю процедуру/функцию. Примеры возвращают Integer 6, 1 и 406. Результат поиска 1 — индекс массива, а не логический признак успеха.

## Поведение

- Движок проверяет условие, выполняет тело и возвращается к проверке. В отличие от For, он не сохраняет числовую границу и не меняет счётчик автоматически.
- Продвижение нужно писать явно. При постоянной проверке игрового состояния добавляйте подходящий Wait и ограничение времени: сам While не спит и не имеет таймаута. Пауза и остановка движка остаются доступны.
- Continue и выход выполняют Finally тех блоков Try, которые покидают. Заголовок, команды и Wend пишите на отдельных строках внутри процедуры или функции.

## Примеры

### 1. Сумма цифр

```vb
# DigitSum получает number=123 по ByVal. MOD 10 берёт последнюю цифру, Fix(number/10) убирает её: 123→12→1→0. total складывает 3+2+1=6. Последняя ложная проверка завершает цикл; Main получает 6. Вход 0 сразу дал бы 0 без выполнения тела.
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**Разбор параметров и выполнения:**

DigitSum получает number=123 по ByVal. MOD 10 берёт последнюю цифру, Fix(number/10) убирает её: 123→12→1→0. total складывает 3+2+1=6. Последняя ложная проверка завершает цикл; Main получает 6. Вход 0 сразу дал бы 0 без выполнения тела.

### 2. Поиск первого совпадения

```vb
# FirstAbove получает values=[4,7,9] и threshold=6. Проверка границы защищает values[index]. На индексе 1 условие 7>6 сохраняет found=1; Exit While прекращает просмотр. Если совпадений нет, остаётся -1. Main возвращает индекс 1, отсчитываемый с нуля.
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**Разбор параметров и выполнения:**

FirstAbove получает values=[4,7,9] и threshold=6. Проверка границы защищает values[index]. На индексе 1 условие 7>6 сохраняет found=1; Exit While прекращает просмотр. Если совпадений нет, остаётся -1. Main возвращает индекс 1, отсчитываемый с нуля.

### 3. Число проверок условия

```vb
# CanContinue принимает checks по ByRef, index и limit=3 по ByVal. Увеличивает checks и возвращает index<limit как 1/0. Проверки проходят при index=0,1,2,3: четыре вызова для трёх итераций. total=1+2+3=6; Main возвращает 400+6=406.
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**Разбор параметров и выполнения:**

CanContinue принимает checks по ByRef, index и limit=3 по ByVal. Увеличивает checks и возвращает index<limit как 1/0. Проверки проходят при index=0,1,2,3: четыре вызова для трёх итераций. total=1+2+3=6; Main возвращает 400+6=406.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
