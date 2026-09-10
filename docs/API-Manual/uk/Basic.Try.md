# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Try обробляє помилки виконання у своєму тілі та викликаних помічниках. Catch приймає помилку, Finally завершує операцію, Throw створює або повторно викидає помилку. Повернення API-командою 0 чи false є звичайним результатом: перевіряйте його явно; воно саме не викликає Catch.

## Точний синтаксис

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

## Параметри

- `Try / statements` — Try відкриває захищений блок. Потрібен один Catch, один Finally або обидва, а далі End Try. Блоки можна вкладати. Після успішного тіла Catch пропускається. Кілька Catch, фільтри When та Exit Try у цьому піднаборі не реалізовані.
- `Catch / name / As type` — Змінну Catch можна не вказувати. Якщо вказано name, вона отримує повідомлення String. As String позначає це подання; As Exception — сумісний запис, а не об’єкт .NET чи фільтр типів. Інші типи заборонено. Нове ім’я стає локальним у процедурі й затінює однойменне глобальне. Наявна локальна змінна отримує значення з дотриманням її типу/Const. Якщо вона потрібна й без виконання Catch, оголосіть String перед Try.
- `Finally / End Try` — Finally необов’язковий за наявності Catch; його тіло може бути порожнім. Звичайне завершення, помилки, Return, Exit Sub/Function і переходи циклу/GoTo назовні виконують відповідні Finally. End Try обов’язковий. Скасування скрипта навмисно оминає Catch і скриптовий Finally, щоб аварійну зупинку не можна було затримати.
- `Throw stringExpression` — Throw stringExpression один раз обчислює повідомлення й створює нову помилку. Потрібен String; інші значення явно перетворюйте через CStr. Це форма Basic, а не Throw New Exception(...) із VB.NET. Без обробника помилкою завершується поточний запуск, а не всі інші скрипти.
- `Throw` — Порожній Throw дозволений лише всередині Catch, зокрема вкладених блоків. Він повторно викидає активну помилку зі збереженням початкового тексту, файла й рядка. Викликаному з Catch помічнику потрібен власний Catch для такого Throw.

## Повертає

Try/Catch/Finally і Throw не повертають ID, число чи Boolean. Catch записує повідомлення в name; Throw передає керування замість повернення значення. Приклади явно повертають із Main два результати String та Integer 13. API-методи всередині зберігають власні правила повернення.

## Поведінка

- Підготовка перевіряє вкладеність і забороняє GoTo/On Error GoTo всередину Try, Catch або Finally. Генератор записує адреси обробника й завершення. Кожен виклик має власні активні обробники; помилка потрапляє в найближчий придатний Catch. Помилка всередині Catch проходить через його Finally назовні. Якщо структурного обробника немає, можуть діяти звичайні правила On Error.
- Очікуваний результат, помилка чи перехід зберігаються на час Finally; вкладене завершення йде зсередини назовні. Нова помилка у Finally замінює попередню. У Basic також дозволені Return і переходи назовні з Finally, які замінюють відкладене продовження; це відрізняється від VB.NET. Порожній Throw зберігає місце першої помилки, зокрема з викликаного помічника.
- Перевірки паузи/зупинки залишаються активними. Try не створює потоків, повторних спроб чи затримок. Підготовлені адреси використовуються повторно; винятки призначені для помилок, звичайні умови перевіряйте прямо. Аварійна зупинка пропускає скриптове завершення; ресурси хоста мають окремі правила звільнення в рушії.

## Приклади

### 1. Перевірити параметр і зберегти повідомлення

```vb
# CheckedAmount отримує amount=-2 як Integer через ByVal; від’ємне значення викликає Throw "amount must be non-negative". Catch отримує цей String у problem і копіює в message. As Exception не створює об’єкт. Finally задає finished=1. Main повертає "amount must be non-negative:1". За невід’ємного amount функція повернула б значення без Catch.
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

**Пояснення параметрів і виконання:**

CheckedAmount отримує amount=-2 як Integer через ByVal; від’ємне значення викликає Throw "amount must be non-negative". Catch отримує цей String у problem і копіює в message. As Exception не створює об’єкт. Finally задає finished=1. Main повертає "amount must be non-negative:1". За невід’ємного amount функція повернула б значення без Catch.

### 2. Передати помилку назовні повторно

```vb
# Внутрішній Throw створює "missing item". Внутрішній Catch задає trace=1; порожній Throw зберігає ту саму помилку. Внутрішній Finally дописує 2, зовнішній Catch копіює outerProblem у message й дописує 3, зовнішній Finally дописує 4. Main повертає "1234:missing item". trace показує порядок виконання, а не код помилки.
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

**Пояснення параметрів і виконання:**

Внутрішній Throw створює "missing item". Внутрішній Catch задає trace=1; порожній Throw зберігає ту саму помилку. Внутрішній Finally дописує 2, зовнішній Catch копіює outerProblem у message й дописує 3, зовнішній Finally дописує 4. Main повертає "1234:missing item". trace показує порядок виконання, а не код помилки.

### 3. Завершити кожну розпочату ітерацію

```vb
# number набуває значень 1, 2, 3. До total додається лише 1: Continue For пропускає 2, Exit For закінчує цикл на 3. У всіх трьох розпочатих Try виконується Finally, тому finished=3. Main повертає 1*10+3=13. Finally не потребує помилки; перехід циклу відкладається до завершення ітерації.
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

**Пояснення параметрів і виконання:**

number набуває значень 1, 2, 3. До total додається лише 1: Continue For пропускає 2, Exit For закінчує цикл на 3. У всіх трьох розпочатих Try виконується Finally, тому finished=3. Main повертає 1*10+3=13. Finally не потребує помилки; перехід циклу відкладається до завершення ітерації.

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
