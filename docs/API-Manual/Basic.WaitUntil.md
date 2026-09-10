# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Wait Until повторяет проверку условия до успеха либо истечения времени. Это расширение Basic, а не оператор VB.NET. Ожидание выполняется в текущем скрипте и не создаёт поток или другую процедуру.

## Точный синтаксис

```text
Wait Until condition Timeout milliseconds
```

## Параметры

- `condition` — condition — выражение, проверяемое сразу и затем между короткими ожиданиями. Используйте Boolean или сравнение: числовой 0 означает false, остальные значения подчиняются правилам If. Строка "false" не равна Boolean false. Можно вызывать UO-команды и свои функции; их ошибки передаются обработчику. Побочные действия функции повторяются при каждой проверке.
- `Timeout milliseconds` — Timeout обязателен. milliseconds вычисляется один раз до первой проверки условия. Нужен Integer от 0 до 2147483647; отрицательное число, дробь или String вызывают ошибку до выполнения condition. Ноль разрешает только немедленную проверку. Вне этого места timeout может оставаться обычным именем переменной.

## Возвращает

Сам оператор ничего не возвращает. При успехе выполняется следующая строка. При истечении времени возникает ошибка с файлом и строкой; её принимает Try/Catch либо настроенный On Error, иначе текущий запуск завершается ошибкой. Автоматического возврата false нет. В примере 2 своя функция явно возвращает True/1 или False/0.

## Поведение

- Движок сохраняет длительность и запускает монотонный Stopwatch. Условие проверяется сразу: успешная первая проверка завершает ожидание даже при нулевом лимите. При false запускается цикл. В нём проверяются отмена и пауза, вычисляется остаток времени и выполняется ожидание не более 10 мс перед следующей проверкой. Постоянного занятого цикла нет; планировщик Windows может увеличить интервал.
- На паузе проверки условия прекращаются, но прошедшее реальное время входит в лимит. После продолжения истёкший таймаут обрабатывается до следующей проверки. Стоп прерывает ожидание и, как другая аварийная отмена, пропускает скриптовые Catch/Finally. Принудительно прервать заблокировавшуюся функцию самого условия этот оператор не может: делайте такие функции короткими. Уже начавшаяся проверка заканчивается до обработки её результата или ошибки.
- Ошибка condition сохраняется, а не заменяется таймаутом. Обычная обработка ошибки или таймаута выполняет соответствующие Finally. Переменные принадлежат текущему вызову; повторный вход начинает новый отсчёт. End Wait и дополнительного параметра частоты нет. Wait(milliseconds) остаётся отдельной обычной функцией задержки.

## Примеры

### 1. Проверять функцию с ограничением времени

```vb
# checks начинается с 0. Ready получает её ByRef и увеличивает при каждой проверке; required=3 передаётся ByVal. budget=5000 разрешает до пяти секунд. Проверки 1 и 2 возвращают false, третья — true. Main возвращает Integer 3. Это определённый пример опроса, а не имитация соединения с сервером; вместо его условия подставьте нужную проверку состояния.
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

**Разбор параметров и выполнения:**

checks начинается с 0. Ready получает её ByRef и увеличивает при каждой проверке; required=3 передаётся ByVal. budget=5000 разрешает до пяти секунд. Проверки 1 и 2 возвращают false, третья — true. Main возвращает Integer 3. Это определённый пример опроса, а не имитация соединения с сервером; вместо его условия подставьте нужную проверку состояния.

### 2. Вернуть Boolean из своей функции

```vb
# TryWait получает ready=False и budget=0. Единственная немедленная проверка неуспешна, возникает таймаут. Catch problem преобразует ошибку в Return False; Main возвращает 0, который можно сравнить с False. При ready=True возврат был бы 1/True. Обёртка ловит все ошибки выполнения, не только таймаут: проверяйте problem, если их нужно различать. ready здесь — переданное значение Boolean, а не функция обратного вызова.
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

**Разбор параметров и выполнения:**

TryWait получает ready=False и budget=0. Единственная немедленная проверка неуспешна, возникает таймаут. Catch problem преобразует ошибку в Return False; Main возвращает 0, который можно сравнить с False. При ready=True возврат был бы 1/True. Обёртка ловит все ошибки выполнения, не только таймаут: проверяйте problem, если их нужно различать. ready здесь — переданное значение Boolean, а не функция обратного вызова.

### 3. Сохранить ошибку условия и выполнить завершение

```vb
# CheckStatus получает state=-1 и при первой проверке выбрасывает "disconnected". Лимит 3000 мс не подменяет эту ошибку. Catch копирует problem в message, Finally устанавливает finished=True/1. Main возвращает "disconnected:1". state=1 сразу выполнил бы условие, state=0 оставался бы false до таймаута. Пример собственной проверки состояния работает без подключения к игре.
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

**Разбор параметров и выполнения:**

CheckStatus получает state=-1 и при первой проверке выбрасывает "disconnected". Лимит 3000 мс не подменяет эту ошибку. Catch копирует problem в message, Finally устанавливает finished=True/1. Main возвращает "disconnected:1". state=1 сразу выполнил бы условие, state=0 оставался бы false до таймаута. Пример собственной проверки состояния работает без подключения к игре.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
