# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

On Error задає обробку подальших помилок виконання у поточній процедурі або функції. Це конструкція мови, а не виклик API. Для структурованої обробки й завершення використовуйте Try/Catch/Finally.

## Точний синтаксис

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## Параметри

- `label` — Наявна мітка тієї ж процедури, записана окремим рядком label:. Може бути перед чи після On Error, регістр неважливий. Це не функція, текст у лапках або номер рядка. Невідома мітка дає SC009; клієнт блокує такий скрипт.
- `Resume Next / On Error` — On Error Resume Next автоматично продовжує після помилкової інструкції без переходу до мітки. Успішні інструкції не змінюються. Область дії — поточний виклик процедури, а не всі скрипти.
- `0` — On Error GoTo 0 вимикає режим. Нуль є спеціальним керувальним значенням, не міткою й не Boolean-результатом. Інші числові мітки та GoTo -1 не підтримуються.
- `Resume / Resume Next` — У обробнику Resume повторює помилкову інструкцію, Resume Next продовжує після неї. Потрібна збережена помилка виконання; після переходу її адреса очищається. Мітку чи таймаут ці форми не приймають.

## Повертає

On Error і Resume нічого не повертають. Перехоплена помилка не стає TRUE/FALSE й автоматично не виправляє присвоєння. Приклади явно повертають Integer 5,18,10. Попередні побічні дії автоматично не відкочуються.

## Поведінка

- Підготовка визначає мітки після читання всієї процедури, тож працюють обидва напрямки. Виконання зберігає режим; при винятку спочатку розглядається Try, потім On Error.
- Рушій запам’ятовує адресу помилкової інструкції. Режим мітки переходить до обробника, автоматичний Resume Next — за інструкцію. Resume повторно обчислює вирази й виклики: спочатку усуньте причину та врахуйте повторення дій.
- On Error GoTo 0 не стирає збереженої адреси: обробник може вимкнути себе, виправити дані та виконати Resume. Вимикайте режим перед діями обробника, здатними спричинити помилку, щоб уникнути повторного входу.
- Синтаксичні помилки й скасування не перехоплюються. Повернення командою 0, FALSE чи іншого статусу відмови без винятку не запускає On Error; перевіряйте результат команди.
- Звичайний потік має обходити обробник через Return або GoTo. Викликана процедура має власний режим. Її неперехоплена помилка може перейти до викликача; Resume тоді повторює весь виклик, а не внутрішній рядок. Автоматичних меж спроб і затримок немає.

## Приклади

### 1. Пропустити одне присвоєння

```vb
# values[0] створює одну комірку, індекс 5 недопустимий. result=1. On Error Resume Next пропускає невдале читання до присвоєння, залишаючи 1. GoTo 0 вимикає режим; result+=4 дає 5. Main повертає 5, а не успішність читання.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**Пояснення параметрів і виконання:**

values[0] створює одну комірку, індекс 5 недопустимий. result=1. On Error Resume Next пропускає невдале читання до присвоєння, залишаючи 1. GoTo 0 вимикає режим; result+=4 дає 5. Main повертає 5, а не успішність читання.

### 2. Виправити й повторити

```vb
# ReadCell зберігає 8 у комірці 0, але index=2. Помилка переходить до FixIndex. GoTo 0 вимикає подальшу обробку; handled=1, index=0. Resume повторює result=values[index], записуючи 8. Return запобігає звичайному входу до обробника. Main отримує 18.
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**Пояснення параметрів і виконання:**

ReadCell зберігає 8 у комірці 0, але index=2. Помилка переходить до FixIndex. GoTo 0 вимикає подальшу обробку; handled=1, index=0. Resume повторює result=values[index], записуючи 8. Return запобігає звичайному входу до обробника. Main отримує 18.

### 3. Обробник перед командою

```vb
# Початковий GoTo Work оминає Failed. On Error GoTo Failed підключає попередню мітку. Індекс 2 спричиняє помилку до зміни result. Обробник вимикає себе, збільшує handled і через Resume Next доходить до Return. Результат 1*10+0=10. Мітки не є окремими процедурами.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**Пояснення параметрів і виконання:**

Початковий GoTo Work оминає Failed. On Error GoTo Failed підключає попередню мітку. Індекс 2 спричиняє помилку до зміни result. Обробник вимикає себе, збільшує handled і через Resume Next доходить до Return. Результат 1*10+0=10. Мітки не є окремими процедурами.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
