# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Select Case выбирает одну ветку, сравнивая сохранённое значение с вариантами по порядку. Подходит для категорий предметов, режимов скрипта и диапазонов чисел. Это конструкция Basic без UO.; игровые вызовы внутри выражений по-прежнему требуют UO.

## Точный синтаксис

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

## Параметры

- `expression` — Обязательное выражение после Select Case: переменная, литерал или вызов функции. Вычисляется ровно один раз при каждом входе, даже если блок пустой или содержит только Case Else.
- `value / from / to` — После Case указывают значение либо варианты через запятую; каждый вариант может быть выражением. from To to включает обе границы. Обратный диапазон не совпадает. Верхняя граница вычисляется, только если проверка нижней прошла. Запятые внутри аргументов функции не разделяют варианты.
- `Is comparison value` — Сравнение через =, <>, <, <=, > или >=. Is можно опустить: Case Is >= 5 и Case >= 5 равнозначны. Это обычное сравнение значений движка, а не проверка типа объекта.
- `Case Else` — Необязательная запасная ветка, если прежние Case не совпали. Должна быть последней и встречаться не более одного раза. Если её нет, отсутствие совпадения продолжает выполнение после End Select.
- `Exit Select` — Выходит из ближайшего вложенного Select Case к его End Select. Внешний цикл и процедуру не завершает. За пределами Select Case даёт ошибку загрузки.

## Возвращает

Select Case, Case, End Select и Exit Select ничего не возвращают. Это не логические вызовы, их нельзя сравнивать с TRUE или 1. В примерах String либо Integer явно возвращает функция через Return. В сравнении значений TRUE — число 1, FALSE — 0; поэтому Case True совпадает с 1, а не с любым ненулевым числом.

## Поведение

- При подготовке создаются SelectInstruction, проверки CaseInstruction по порядку и готовые переходы. При выполнении значение сохраняется внутри текущего вызова функции, без служебной переменной в списке локальных. Рекурсия и вложенные блоки имеют независимые значения; новый вход обновляет сохранённое значение.
- CaseMatches проверяет варианты слева направо до первого совпадения. Выбранная ветка выполняется один раз; затем переход пропускает остальные. Изменения переменных в выражении Case не заставляют заново читать значение выбора. Уже выполненные побочные действия не откатываются.
- Числа и строки сравниваются по обычным правилам движка; для строк регистр важен. Option Compare Text и автоматические преобразования VB.NET не реализованы. Для сравнения числа и текста явно преобразуйте значение.
- End Select обязателен. Нельзя помещать выполняемый код до первого Case или начинать For в одной ветке, а закрывать Next в другой. Неверная структура блокирует загрузку. Входите через Select Case, не через GoTo в середину блока.
- Ошибки передаются текущему обработчику. On Error Resume Next пропускает весь блок при ошибке выбора; при ошибке условия Case переходит к следующему Case. Явный Resume повторяет ошибочную инструкцию. Exit Select выполняет активные Finally, из которых выходит. Проверки остановки и паузы сохраняются между инструкциями; ожидание и таймаут не добавляются.

## Примеры

### 1. Разделить количество по диапазонам

```vb
# DescribeAmount принимает amount по значению — ByVal. Case 0 возвращает empty; 1 To 4 включает 1 и 4; Is >= 5 возвращает large. Отрицательные числа попадают в Case Else. Main вызывает функцию с -1, 0, 4 и 5 и объединяет ответы: negative:empty:small:large. Эти слова заданы скриптом, это не встроенные режимы.
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

**Разбор параметров и выполнения:**

DescribeAmount принимает amount по значению — ByVal. Case 0 возвращает empty; 1 To 4 включает 1 и 4; Is >= 5 возвращает large. Отрицательные числа попадают в Case Else. Main вызывает функцию с -1, 0, 4 и 5 и объединяет ответы: negative:empty:small:large. Эти слова заданы скриптом, это не встроенные режимы.

### 2. Увидеть, какие функции вызываются

```vb
# ReadMode увеличивает reads через ByRef и один раз возвращает 2. Candidate увеличивает checks и возвращает свой аргумент value. Candidate(checks,1) не совпадает; Candidate(checks,2) совпадает, поэтому Candidate(checks,3) пропускается. selected получает 7. Main возвращает 1*100+2*10+7=127: результат показывает все три значения без обращения к игре.
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

**Разбор параметров и выполнения:**

ReadMode увеличивает reads через ByRef и один раз возвращает 2. Candidate увеличивает checks и возвращает свой аргумент value. Candidate(checks,1) не совпадает; Candidate(checks,2) совпадает, поэтому Candidate(checks,3) пропускается. selected получает 7. Main возвращает 1*100+2*10+7=127: результат показывает все три значения без обращения к игре.

### 3. Выйти из вложенного выбора с завершением Finally

```vb
# route — строка harvest, она совпадает с первым вариантом. trace становится 1. Внутренний Case 2 выполняет Exit Select: trace=99 пропускается, но Finally дописывает цифру 2. Выполнение продолжается во внешней ветке и дописывает 3; Main возвращает 123. Внешний Case Else пропускается. Другая строка в route вернёт -1.
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

**Разбор параметров и выполнения:**

route — строка harvest, она совпадает с первым вариантом. trace становится 1. Внутренний Case 2 выполняет Exit Select: trace=99 пропускается, но Finally дописывает цифру 2. Выполнение продолжается во внешней ветке и дописывает 3; Main возвращает 123. Внешний Case Else пропускается. Другая строка в route вернёт -1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
