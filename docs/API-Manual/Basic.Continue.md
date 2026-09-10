# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Continue пропускает оставшуюся часть тела ближайшего внешнего цикла указанного вида. Continue For применяется к числовому For и For Each, Continue Do — к Do/Loop и Repeat/Until, Continue While — к While/Wend.

## Точный синтаксис

```text
Continue For
Continue Do
Continue While
```

## Параметры

- `kind` — kind: обязательное слово For, Do или While после Continue. Скобки и аргументы результата не нужны. Указанный цикл должен окружать оператор в той же процедуре. Вложенный цикл другого вида не перехватывает переход.

## Возвращает

Continue не возвращает значения и не используется в выражениях. Это не TRUE/FALSE и не перезапуск процедуры. Внешняя функция позже может вернуть результат через RETURN; примеры возвращают Integer 10, 3 и 34.

## Поведение

- For: числовой цикл выполняет NEXT, учитывает STEP и проверяет следующее значение относительно границы; For Each получает следующий элемент. Когда элементы закончились, цикл завершается. Начальное значение счётчика и выражение коллекции заново не вычисляются.
- Do: условие в строке Do проверяется снова в начале, условие в строке Loop — в конце. Repeat/Until использует условие UNTIL. Do/Loop без условия продолжается до явного выхода или остановки. While снова проверяет WHILE. Continue Do не выбирает While/Wend.
- При подготовке определяется адрес ближайшего цикла нужного вида. Continue вне такого цикла даёт SC020 до инициализаторов, даже без Option Explicit. Проверяются также имя NEXT и отсутствующие окончания. Старая форма FOR/NEXT через границу IF сохранена.
- Выход из TRY/CATCH через Continue сначала выполняет пересекаемые FINALLY от внутреннего к внешнему, каждый один раз. Если весь цикл расположен внутри TRY, его FINALLY не выполняется на каждой итерации. RETURN или ошибка в FINALLY заменяет отложенный переход.
- Continue не делает задержку. Меняйте условие или используйте подходящее ожидание при опросе, иначе цикл может стать бесконечным. Пауза и остановка продолжают проверяться. Покинутые нативные перечислители освобождаются, запуски независимы. Exit For/Do/While выходит из цикла вместо следующей итерации.

## Примеры

### 1. Пропустить неподходящие элементы

```vb
# values содержит -2, 4, 0, 6. При item<=0 команда Continue For пропускает total+=item для -2 и 0. Эта запись применяется и в For Each. SumPositive и Main возвращают Integer 10: сумму 4+6.
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**Разбор параметров и выполнения:**

values содержит -2, 4, 0, 6. При item<=0 команда Continue For пропускает total+=item для -2 и 0. Эта запись применяется и в For Each. SumPositive и Main возвращают Integer 10: сумму 4+6.

### 2. Выбрать внешний цикл по виду

```vb
# AdvanceTo получает limit=3, count начинается с 0. Внутри While True счётчик увеличивается, а Continue Do переходит к внешнему Do, не к While. После каждого перехода проверяется условие Do. При count=3 цикл заканчивается и возвращает Integer 3.
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**Разбор параметров и выполнения:**

AdvanceTo получает limit=3, count начинается с 0. Внутри While True счётчик увеличивается, а Continue Do переходит к внешнему Do, не к While. После каждого перехода проверяется условие Do. При count=3 цикл заканчивается и возвращает Integer 3.

### 3. Завершение действий при пропуске

```vb
# Process получает limit=3 и skip=2. i проходит 1, 2, 3. Вторая итерация пропускает total+=i, но Finally увеличивает cleanup все три раза. total=4, cleanup=3; RETURN cleanup*10+total возвращает Integer 34.
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**Разбор параметров и выполнения:**

Process получает limit=3 и skip=2. i проходит 1, 2, 3. Вторая итерация пропускает total+=i, но Finally увеличивает cleanup все три раза. total=4, cleanup=3; RETURN cleanup*10+total возвращает Integer 34.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
