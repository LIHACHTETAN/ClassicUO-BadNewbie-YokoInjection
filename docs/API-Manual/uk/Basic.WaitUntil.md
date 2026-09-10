# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Wait Until повторює перевірку умови до успіху або вичерпання часу. Це розширення Basic, а не оператор VB.NET. Воно працює в поточному скрипті без створення потоку чи іншої процедури.

## Точний синтаксис

```text
Wait Until condition Timeout milliseconds
```

## Параметри

- `condition` — condition перевіряється одразу, потім між короткими очікуваннями. Використовуйте Boolean або порівняння: числовий 0 означає false, решта значень відповідає правилам If. Рядок "false" не є Boolean false. Можна викликати UO та власні функції; їхні помилки передаються далі, а побічні дії повторюються при кожній перевірці.
- `Timeout milliseconds` — Timeout обов’язковий. milliseconds обчислюється один раз перед першою перевіркою. Потрібен Integer 0..2147483647; від’ємні числа, дроби та String спричиняють помилку до виконання condition. Нуль дозволяє лише негайну перевірку. В інших місцях timeout може бути звичайною змінною.

## Повертає

Оператор не повертає значення. Успіх продовжує наступний рядок; вичерпання часу створює помилку з файлом і рядком. Її обробляє Try/Catch або налаштований On Error, інакше поточний запуск завершується помилкою. Автоматичного false немає. Приклад 2 явно повертає True/1 або False/0 із власної функції.

## Поведінка

- Двигун зберігає тривалість і запускає монотонний Stopwatch. Перша перевірка негайна; її успіх дозволений навіть за нульового ліміту. Після false цикл перевіряє скасування та паузу, визначає залишок часу й очікує не більше 10 мс перед новою перевіркою. Постійного зайнятого циклу немає; планувальник ОС може збільшити інтервал.
- Пауза зупиняє опитування, але реальний час входить у ліміт. Після відновлення прострочений ліміт спричиняє помилку до нової перевірки. Стоп перериває очікування, оминаючи скриптові Catch/Finally, як інше аварійне скасування. Оператор не може примусово перервати заблокований виклик усередині condition: використовуйте короткі функції. Почата перевірка завершується перед обробкою її результату чи помилки.
- Помилка condition не замінюється таймаутом. Звичайні помилки й таймаути виконують відповідні Finally. Змінні належать поточному виклику, повторний вхід запускає новий відлік. End Wait і додаткового параметра частоти немає. Wait(milliseconds) залишається окремою функцією затримки.

## Приклади

### 1. Опитувати функцію з лімітом

```vb
# checks починається з 0; Ready отримує її ByRef і збільшує при кожній перевірці. required=3 передається ByVal, budget=5000 дозволяє до п’яти секунд. Перші дві перевірки повертають false, третя — true. Main повертає Integer 3. Це визначений приклад опитування, не імітація сервера; замініть умову потрібною перевіркою стану.
Option Explicit On
Function Ready(ByRef checks As Integer, ByVal required As Integer) As Boolean
    checks += 1
    Return checks >= required
End Function

Sub Main()
    Dim checks As Integer = 0
    Const budget = 5000
    Wait Until Ready(checks, 3) Timeout budget
    Return checks
End Sub
```

**Пояснення параметрів і виконання:**

checks починається з 0; Ready отримує її ByRef і збільшує при кожній перевірці. required=3 передається ByVal, budget=5000 дозволяє до п’яти секунд. Перші дві перевірки повертають false, третя — true. Main повертає Integer 3. Це визначений приклад опитування, не імітація сервера; замініть умову потрібною перевіркою стану.

### 2. Повернути Boolean зі своєї функції

```vb
# TryWait отримує ready=False і budget=0. Негайна перевірка неуспішна й створює таймаут. Catch problem виконує Return False; Main повертає 0, сумісний із порівнянням з False. ready=True повернуло б 1/True. Обгортка ловить усі помилки виконання: аналізуйте problem, якщо потрібне розрізнення. ready — значення Boolean, не функція зворотного виклику.
Option Explicit On
Function TryWait(ByVal ready As Boolean, ByVal budget As Integer) As Boolean
    Try
        Wait Until ready Timeout budget
        Return True
    Catch problem
        Return False
    End Try
End Function

Sub Main()
    Dim success = TryWait(False, 0)
    Return success
End Sub
```

**Пояснення параметрів і виконання:**

TryWait отримує ready=False і budget=0. Негайна перевірка неуспішна й створює таймаут. Catch problem виконує Return False; Main повертає 0, сумісний із порівнянням з False. ready=True повернуло б 1/True. Обгортка ловить усі помилки виконання: аналізуйте problem, якщо потрібне розрізнення. ready — значення Boolean, не функція зворотного виклику.

### 3. Зберегти помилку умови

```vb
# CheckStatus зі state=-1 одразу створює "disconnected". Ліміт 3000 мс не замінює помилку. Catch копіює problem у message; Finally задає finished=True/1. Main повертає "disconnected:1". state=1 дав би негайний успіх; state=0 залишався б false до таймауту. Приклад працює без підключення до гри.
Option Explicit On
Function CheckStatus(ByVal state As Integer) As Boolean
    If state < 0 Then
        Throw "disconnected"
    End If
    Return state = 1
End Function

Sub Main()
    Dim message = ""
    Dim finished = False
    Try
        Wait Until CheckStatus(-1) Timeout 3000
    Catch problem
        message = problem
    Finally
        finished = True
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Пояснення параметрів і виконання:**

CheckStatus зі state=-1 одразу створює "disconnected". Ліміт 3000 мс не замінює помилку. Catch копіює problem у message; Finally задає finished=True/1. Main повертає "disconnected:1". state=1 дав би негайний успіх; state=0 залишався б false до таймауту. Приклад працює без підключення до гри.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
