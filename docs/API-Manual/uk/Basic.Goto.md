# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

GoTo переводить виконання до іменованої мітки в поточній процедурі або функції. Мітка позначає місце коду, а не окрему процедуру. Для звичайного керування використовуйте If, цикли та Return.

## Точний синтаксис

```text
GoTo label
label:
```

## Параметри

- `label` — Ім’я, оголошене окремим рядком label: у тій самій процедурі. Пишіть GoTo label без лапок, дужок і двокрапки після цілі. Мітка може бути вище або нижче; регістр не важливий. Інша процедура може мати таке саме ім’я мітки. Крапки в імені дозволені, але не означають член модуля. Числа, обчислювані вирази та мітки іншої процедури не підтримуються як цілі.

## Повертає

GoTo та label: нічого не повертають і не повідомляють успіх через 1/0 або TRUE/FALSE. Приклади явно повертають із Main Integer -1, 6 та 123, обчислені самим скриптом.

## Поведінка

- Підготовка записує адреси міток і визначає переходи після читання всієї процедури. Виконання використовує готову адресу без пошуку в тексті. Значення змінних зберігаються; попередні дії не скасовуються.
- Невідома ціль дає SC009 і блокує запуск у клієнті. Повтор мітки в одній процедурі, навіть з іншим регістром, дає SC021 до ініціалізації. Для Include зберігається початковий файл і рядок помилки. Зайві символи після цілі можуть викликати попередження; пишіть точний синтаксис.
- Вихід з активних Try виконує Finally від внутрішнього до зовнішнього перед переходом до цілі. Перехід усередині того самого активного Try зберігає блок. Помилка у Finally може завадити досягненню цілі.
- Входьте в цикли та Try/Catch/Finally через їхній звичайний початок. Стрибок усередину не відновлює пропущену ініціалізацію та стан блоків; це не спосіб їх поновлення. Для циклів використовуйте Continue або Exit.
- Перехід назад не має автоматичного обмеження спроб, таймауту чи затримки. Явно змінюйте умову виходу. Звичайне виконання також проходить крізь мітку, тому оминайте непотрібний код через GoTo або Return. Обробник помилок установлює On Error, а не GoTo.

## Приклади

### 1. Перехід уперед

```vb
# amount=0 обирає NoItems і result=-1. Потік проходить Finished та повертає -1. За amount=4 звичайна гілка записує 40 і GoTo Finished оминає NoItems. Обидві мітки належать Main і не є викликами функцій.
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**Пояснення параметрів і виконання:**

amount=0 обирає NoItems і result=-1. Потік проходить Finished та повертає -1. За amount=4 звичайна гілка записує 40 і GoTo Finished оминає NoItems. Обидві мітки належать Main і не є викликами функцій.

### 2. Обмежений повтор

```vb
# attempt починається з 0 і збільшується перед умовою. Again та again означають одну мітку. Проходи додають 1, 2, 3; потім attempt<3 хибне і результат дорівнює 6. total оголошений до мітки, тому перехід його не обнуляє.
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**Пояснення параметрів і виконання:**

attempt починається з 0 і збільшується перед умовою. Again та again означають одну мітку. Проходи додають 1, 2, 3; потім attempt<3 хибне і результат дорівнює 6. total оголошений до мітки, тому перехід його не обнуляє.

### 3. Вихід із вкладених Try

```vb
# trace стає 1; GoTo Finished пропускає trace=99. Внутрішній Finally додає цифру 2, зовнішній — 3. Далі Finished повертає 123. Кожен Finally виконується один раз під час цього переходу.
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**Пояснення параметрів і виконання:**

trace стає 1; GoTo Finished пропускає trace=99. Внутрішній Finally додає цифру 2, зовнішній — 3. Далі Finished повертає 123. Кожен Finally виконується один раз під час цього переходу.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
