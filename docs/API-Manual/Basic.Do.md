# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Do допускает проверку до либо после тела. While продолжает при истинном условии, Until — до его истинности. Repeat … Until — поддерживаемая старая форма с проверкой после тела.

## Точный синтаксис

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## Параметры

- `condition / While / Until` — Логическое выражение: используйте числовые 0/False и 1/True. While продолжает при истине; Until при истине выходит. Выражение вычисляется заново при каждой проверке. Текст не разбирается как Boolean.
- `position / Repeat` — Условие после Do может пропустить первый проход. Условие после Loop или Until у Repeat проверяется после хотя бы одного прохода. Разрешено только одно место условия. У Do … Loop без условия должен быть явный выход.
- `statements / exit` — Тело цикла. Continue Do переходит к следующей проверке, Exit Do выходит из ближайшего Do либо Repeat. Break выходит из ближайшего цикла любого вида. RETURN завершает всю процедуру/функцию.

## Возвращает

Do, Loop, Repeat, Until и Exit Do значения не возвращают. Примеры явно возвращают из Main Integer 1, 33 и 83 — это числа, составленные из счётчиков, а не логические результаты команд.

## Поведение

- Подготовка сопоставляет блоки и проверяет переходы. Условия сразу в начале и конце одного Do дают SC020. При выполнении движок проверяет выражение в выбранном месте и повторяет тело согласно правилу While/Until.
- Continue Do при проверке в конце всё равно проверяет конечное условие; при проверке в начале возвращается к заголовку. Перед переходом из Try его Finally выполняется ровно один раз.
- Repeat сначала выполняет тело: пустой массив нужно проверить до входа. Автоматического таймаута нет. Для ожидания игрового события используйте осознанный Wait и ограничение времени; проверки паузы и остановки сохраняются.

## Примеры

### 1. Проверка до и после

```vb
# ready=True уже удовлетворяет Until. Первый Do Until ready выполняется ноль раз: before=0. Второй цикл проверяет условие после увеличения after, поэтому after=1. Main возвращает before*10+after=1.
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**Разбор параметров и выполнения:**

ready=True уже удовлетворяет Until. Первый Do Until ready выполняется ноль раз: before=0. Второй цикл проверяет условие после увеличения after, поэтому after=1. Main возвращает before*10+after=1.

### 2. Ограниченные попытки с завершением

```vb
# attempts начинается с 0 и увеличивается в каждом проходе. Первые два Continue Do выполняют Finally, затем проверяют attempts<4. На третьей попытке Exit Do также выполняет Finally. Получаются attempts=3 и cleanup=3; результат 33. Это локальная модель попыток, а не реальные сетевые повторы.
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**Разбор параметров и выполнения:**

attempts начинается с 0 и увеличивается в каждом проходе. Первые два Continue Do выполняют Finally, затем проверяют attempts<4. На третьей попытке Exit Do также выполняет Finally. Получаются attempts=3 и cleanup=3; результат 33. Это локальная модель попыток, а не реальные сетевые повторы.

### 3. Старый цикл до маркера

```vb
# values содержит 3,5,0 и заведомо не пуст. Repeat читает ячейку, увеличивает index и сумму. Until завершает цикл при value=0 либо достижении длины массива; OrElse не проверяет вторую часть, если найден ноль. total=8 и index=3 дают результат 83.
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**Разбор параметров и выполнения:**

values содержит 3,5,0 и заведомо не пуст. Repeat читает ячейку, увеличивает index и сумму. Until завершает цикл при value=0 либо достижении длины массива; OrElse не проверяет вторую часть, если найден ноль. total=8 и index=3 дают результат 83.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
