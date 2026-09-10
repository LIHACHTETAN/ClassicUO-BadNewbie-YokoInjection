# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Try обрабатывает ошибки выполнения в своём теле и вызываемых помощниках. Catch принимает ошибку, Finally завершает операцию, а Throw создаёт или повторно выбрасывает ошибку. Возврат API-командой 0 или false — обычный результат: проверяйте его явно; сам по себе он не вызывает Catch.

## Точный синтаксис

```text
Try
    statements
Catch
    handlerStatements
Finally
    cleanupStatements
End Try
Catch name
Catch name As Exception
Catch name As String
Throw stringExpression
Throw
```

## Параметры

- `Try / statements` — Try открывает защищённый блок. Нужен один Catch, один Finally либо оба, затем End Try. Блоки можно вкладывать. При успешном выполнении Catch пропускается. Несколько Catch, фильтры When и Exit Try в этом подмножестве не реализованы.
- `Catch / name / As type` — У Catch можно не указывать переменную. Если имя name указано, в него записывается текст ошибки String. As String обозначает это представление; As Exception — совместимая запись, а не объект .NET или фильтр типов. Другие типы запрещены. Новое имя становится локальной переменной процедуры и перекрывает одноимённую глобальную. Существующей локальной переменной присваивается значение с соблюдением её типа/Const. Если переменная нужна и без срабатывания Catch, объявите String перед Try.
- `Finally / End Try` — Finally необязателен при наличии Catch; его тело может быть пустым. Обычное завершение, ошибки, Return, Exit Sub/Function и выходящие из блока переходы цикла/GoTo выполняют соответствующие Finally. End Try обязателен. Отмена скрипта намеренно обходит Catch и скриптовый Finally, чтобы аварийную остановку нельзя было задержать.
- `Throw stringExpression` — Throw stringExpression вычисляет сообщение один раз и создаёт новую ошибку скрипта. Допускается только String; другое значение преобразуйте через CStr. Это форма Basic, а не Throw New Exception(...) из VB.NET. Без обработчика завершается с ошибкой текущий запуск скрипта, а не все остальные скрипты.
- `Throw` — Throw без сообщения разрешён только внутри Catch, включая вложенные блоки. Он повторно выбрасывает текущую ошибку, сохраняя исходный текст, файл и строку. Вызванный из Catch помощник не может использовать пустой Throw вне собственного Catch.

## Возвращает

Try/Catch/Finally и Throw не возвращают ID, число или Boolean. Catch записывает сообщение в name, а Throw передаёт управление вместо возврата значения. Примеры явно возвращают из Main два результата String и Integer 13. API-методы внутри сохраняют собственные правила возврата.

## Поведение

- Подготовка проверяет вложенность и запрещает GoTo/On Error GoTo внутрь Try, Catch или Finally. Генератор сохраняет адреса обработчика и завершения. Каждый вызов имеет собственные активные обработчики; ошибка сначала попадает в ближайший подходящий Catch. Ошибка внутри Catch проходит через его Finally к внешнему обработчику. Если структурного обработчика нет, могут применяться обычные правила On Error.
- Перед Finally сохраняется ожидающий возврат, ошибка или переход наружу; вложенное завершение идёт изнутри наружу. Новая ошибка в Finally заменяет ожидающую. В Basic также разрешены Return и выходящие переходы из Finally, которые заменяют отложенное продолжение; это отличается от VB.NET. Пустой Throw сохраняет место первой ошибки, в том числе ошибки вызванного помощника.
- Проверки паузы/остановки продолжают работать. Try не создаёт потоков, повторных попыток или задержек. Подготовленные адреса используются повторно; обработка исключений предназначена для ошибок, обычные условия проверяйте непосредственно. Аварийная остановка пропускает скриптовое завершение; ресурсы, которыми владеет хост, имеют отдельные правила освобождения в движке.

## Примеры

### 1. Проверить параметр и сохранить сообщение

```vb
# CheckedAmount принимает amount=-2 как Integer через ByVal; отрицательное значение вызывает Throw "amount must be non-negative". Catch получает эту строку в problem и копирует в message. As Exception не создаёт объект. Finally устанавливает finished=1. Main возвращает "amount must be non-negative:1". При неотрицательном amount функция вернула бы значение и Catch не выполнился бы.
Option Explicit On
Function CheckedAmount(ByVal amount As Integer) As Integer
    If amount < 0 Then
        Throw "amount must be non-negative"
    End If
    Return amount
End Function

Sub Main()
    Dim message=""
    Dim finished=0
    Try
        CheckedAmount(-2)
    Catch problem As Exception
        message=problem
    Finally
        finished=1
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Разбор параметров и выполнения:**

CheckedAmount принимает amount=-2 как Integer через ByVal; отрицательное значение вызывает Throw "amount must be non-negative". Catch получает эту строку в problem и копирует в message. As Exception не создаёт объект. Finally устанавливает finished=1. Main возвращает "amount must be non-negative:1". При неотрицательном amount функция вернула бы значение и Catch не выполнился бы.

### 2. Повторно передать ошибку наружу

```vb
# Внутренний Throw создаёт "missing item". Внутренний Catch задаёт trace=1; пустой Throw сохраняет ту же ошибку. Внутренний Finally дописывает 2, внешний Catch копирует outerProblem в message и дописывает 3, внешний Finally дописывает 4. Main возвращает "1234:missing item". trace показывает порядок выполнения, а не код ошибки.
Option Explicit On
Sub Main()
    Dim trace=0
    Dim message=""
    Try
        Try
            Throw "missing item"
        Catch problem
            trace=1
            Throw
        Finally
            trace=trace*10+2
        End Try
    Catch outerProblem
        message=outerProblem
        trace=trace*10+3
    Finally
        trace=trace*10+4
    End Try
    Return CStr(trace) & ":" & message
End Sub
```

**Разбор параметров и выполнения:**

Внутренний Throw создаёт "missing item". Внутренний Catch задаёт trace=1; пустой Throw сохраняет ту же ошибку. Внутренний Finally дописывает 2, внешний Catch копирует outerProblem в message и дописывает 3, внешний Finally дописывает 4. Main возвращает "1234:missing item". trace показывает порядок выполнения, а не код ошибки.

### 3. Завершить каждую начатую итерацию

```vb
# number принимает 1, 2 и 3. В total добавляется только 1: Continue For пропускает 2, Exit For завершает цикл на 3. Во всех трёх начатых Try выполняется Finally, поэтому finished становится 3. Main возвращает 1*10+3=13. Для Finally не нужна ошибка; переход цикла откладывается до завершения текущей итерации.
Option Explicit On
Sub Main()
    Dim total=0
    Dim finished=0
    For Var number=1 To 3
        Try
            If number=2 Then
                Continue For
            End If
            If number=3 Then
                Exit For
            End If
            total+=number
        Finally
            finished+=1
        End Try
    Next
    Return total*10+finished
End Sub
```

**Разбор параметров и выполнения:**

number принимает 1, 2 и 3. В total добавляется только 1: Continue For пропускает 2, Exit For завершает цикл на 3. Во всех трёх начатых Try выполняется Finally, поэтому finished становится 3. Main возвращает 1*10+3=13. Для Finally не нужна ошибка; переход цикла откладывается до завершения текущей итерации.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: tryStatement / catchClause / finallyClause / throwStatement
Analysis/TryStructureValidator.cs: VisitTryStatement / VisitSubrutine / VisitCatchClause / VisitThrowStatement
Runtime/Instructions/Generator.cs: Generate(TryStatementContext)
Runtime/Instructions/TryInstruction.cs: TryInstruction / CatchInstruction / FinallyInstruction / EndTryInstruction
Runtime/Interpreter.cs: CallSubrutine / TryHandleStructuredError / Transfer / DeferReturn / Failure
Runtime/SemanticScope.cs: IsLocal / DefineVar / SetVar
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/try-catch-finally-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/throw-statement
-->
