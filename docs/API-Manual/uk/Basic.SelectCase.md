# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Select Case обирає одну гілку, порівнюючи збережене значення з варіантами по черзі. Підходить для категорій предметів, режимів скрипту та числових діапазонів. Це конструкція Basic без UO.; ігрові виклики у виразах потребують UO.

## Точний синтаксис

```text
Select Case expression
    Case value1, value2
        statements
        Exit Select
    Case from To to
        statements
    Case Is >= value
        statements
    Case Else
        statements
End Select
```

## Параметри

- `expression` — Обов’язковий вираз після Select Case: змінна, літерал або виклик функції. Обчислюється рівно один раз за кожного входу, навіть для порожнього блоку чи блоку лише з Case Else.
- `value / from / to` — Case приймає значення або варіанти через кому; кожен може бути виразом. from To to включає обидві межі. Зворотний діапазон не збігається. Верхню межу обчислюють лише після успішної перевірки нижньої. Коми між аргументами функції не розділяють варіанти.
- `Is comparison value` — Оператори =, <>, <, <=, > та >=. Is необов’язкове: Case Is >= 5 і Case >= 5 рівнозначні. Це звичайне порівняння значень рушія, не перевірка типу об’єкта.
- `Case Else` — Необов’язкова запасна гілка, коли попередні Case не збіглися. Лише одна й обов’язково остання. Без неї відсутність збігу продовжує виконання після End Select.
- `Exit Select` — Вихід із найближчого Select Case за його End Select. Зовнішній цикл і процедуру не завершує. Поза Select Case спричиняє помилку завантаження.

## Повертає

Select Case, Case, End Select та Exit Select нічого не повертають. Це не логічні виклики для порівняння з TRUE чи 1. У прикладах String або Integer явно повертає функція через Return. У порівняннях TRUE дорівнює числу 1, FALSE — 0; Case True збігається з 1, а не з будь-яким ненульовим числом.

## Поведінка

- Підготовка створює SelectInstruction, послідовні перевірки CaseInstruction та готові переходи. Значення зберігається всередині поточного виклику без службової локальної змінної. Рекурсія та вкладені блоки мають незалежні значення; новий вхід оновлює збережений вибір.
- CaseMatches перевіряє варіанти зліва направо до першого збігу. Обрана гілка виконується один раз, решта пропускається переходом. Зміни змінних усередині Case не перечитують збережений вибір. Попередні побічні дії не скасовуються.
- Числа й рядки порівнюються за звичайними правилами рушія; регістр рядків важливий. Option Compare Text і автоматичні перетворення VB.NET не реалізовані. Для числа й тексту явно перетворіть значення.
- End Select обов’язковий. Код до першого Case або For/Next, розділений між гілками, не допускається. Невірна структура блоку перешкоджає завантаженню. Входьте через Select Case, не через GoTo всередину.
- Помилки надходять поточному обробнику. On Error Resume Next пропускає весь вибір, якщо його вираз дав помилку; помилка Case переводить до наступного Case. Resume повторює помилкову інструкцію. Exit Select виконує активні Finally, які залишає. Перевірки паузи й зупинки діють між інструкціями; очікування чи таймаут не додаються.

## Приклади

### 1. Класифікація кількості

```vb
# DescribeAmount отримує amount через ByVal. Case 0 повертає empty, 1 To 4 включає 1 і 4, Is >= 5 повертає large. Від’ємні числа обирають Case Else. Main викликає функцію з -1, 0, 4, 5 та поєднує відповіді: negative:empty:small:large. Назви задані скриптом і не є вбудованими режимами.
Option Explicit On
Function DescribeAmount(ByVal amount)
    Select Case amount
        Case 0
            Return "empty"
        Case 1 To 4
            Return "small"
        Case Is >= 5
            Return "large"
        Case Else
            Return "negative"
    End Select
End Function

Sub Main()
    Return DescribeAmount(-1) & ":" & DescribeAmount(0) & ":" & DescribeAmount(4) & ":" & DescribeAmount(5)
End Sub
```

**Пояснення параметрів і виконання:**

DescribeAmount отримує amount через ByVal. Case 0 повертає empty, 1 To 4 включає 1 і 4, Is >= 5 повертає large. Від’ємні числа обирають Case Else. Main викликає функцію з -1, 0, 4, 5 та поєднує відповіді: negative:empty:small:large. Назви задані скриптом і не є вбудованими режимами.

### 2. Спостереження за викликами

```vb
# ReadMode збільшує reads через ByRef та один раз повертає 2. Candidate збільшує checks і повертає value. Candidate(checks,1) не збігається, Candidate(checks,2) збігається, тому Candidate(checks,3) пропущено. selected отримує 7; Main повертає 1*100+2*10+7=127 без звернення до гри.
Option Explicit On
Function ReadMode(ByRef reads)
    reads += 1
    Return 2
End Function

Function Candidate(ByRef checks, ByVal value)
    checks += 1
    Return value
End Function

Sub Main()
    Dim reads = 0
    Dim checks = 0
    Dim selected = 0
    Select Case ReadMode(reads)
        Case Candidate(checks, 1)
            selected = -1
        Case Candidate(checks, 2), Candidate(checks, 3)
            selected = 7
        Case Else
            selected = -9
    End Select
    Return reads * 100 + checks * 10 + selected
End Sub
```

**Пояснення параметрів і виконання:**

ReadMode збільшує reads через ByRef та один раз повертає 2. Candidate збільшує checks і повертає value. Candidate(checks,1) не збігається, Candidate(checks,2) збігається, тому Candidate(checks,3) пропущено. selected отримує 7; Main повертає 1*100+2*10+7=127 без звернення до гри.

### 3. Вихід із вкладеного вибору

```vb
# route містить harvest і обирає перший варіант. trace стає 1. Внутрішній Case 2 виконує Exit Select, оминаючи trace=99; Finally додає цифру 2. Зовнішня гілка додає 3 й Main повертає 123. Зовнішній Case Else пропущено. Інший рядок у route поверне -1.
Option Explicit On
Sub Main()
    Dim route = "harvest"
    Dim trace = 0
    Select Case route
        Case "harvest", "loot"
            trace = 1
            Select Case 2
                Case 2
                    Try
                        Exit Select
                        trace = 99
                    Finally
                        trace = trace * 10 + 2
                    End Try
            End Select
            trace = trace * 10 + 3
        Case Else
            trace = -1
    End Select
    Return trace
End Sub
```

**Пояснення параметрів і виконання:**

route містить harvest і обирає перший варіант. trace стає 1. Внутрішній Case 2 виконує Exit Select, оминаючи trace=99; Finally додає цифру 2. Зовнішня гілка додає 3 й Main повертає 123. Зовнішній Case Else пропущено. Інший рядок у route поверне -1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
