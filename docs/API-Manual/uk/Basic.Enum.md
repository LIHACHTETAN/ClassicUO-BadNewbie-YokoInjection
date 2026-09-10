# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Enum об’єднує іменовані константи Integer для станів і режимів скрипту. Оголошуйте на рівні файлу або Module, поза Sub/Function. Це підтримувана частина переліків VB.NET, без створення об’єкта .NET Enum.

## Точний синтаксис

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## Параметри

- `Public / Private` — Public діє за замовчуванням, також у Module. Private дозволено лише в Module: тип та елементи недоступні іншим модулям і рівню файлу.
- `name` — Просте ім’я, наприклад Mode, без крапок; регістр не має значення. UO й назви вбудованих типів зарезервовані. Повне ім’я не може повторювати Enum, Module або глобальну змінну.
- `As Integer` — Необов’язково; базовий тип лише знаковий 32-бітний Integer: -2147483648..2147483647. Інші типи відхиляються. As Mode у змінній, параметрі чи результаті Function використовує зберігання й перетворення Integer, без обмеження значення переліком елементів. Без ініціалізації значення дорівнює 0.
- `member` — Одне просте ім’я на рядок, щонайменше один елемент. Повторення, True та False заборонено. Перший елемент без виразу отримує 0, кожен наступний — попереднє значення плюс 1. Різні імена можуть мати однакові числа.
- `constantExpression` — Необов’язковий константний вираз: цілі десяткові/0x числа, дужки, унарний мінус, + - * / Mod, попередні елементи та вже оголошені числові Const. Результат має бути цілим у діапазоні, проміжне ділення може бути дробовим. Використана Const також має давати цілий Integer, без типу або As Integer/Long/Short/Byte. Функції, змінні, рядки, порівняння й читання масивів заборонені. Посилання вперед, цикли залежностей і глибина понад 128 рівнів відхиляються.
- `name.member` — Читання Mode.Ready; ззовні модуля — Tools.Mode.Ready, всередині Tools — Mode.Ready. With Mode дозволяє .Ready. Елементи незмінні: присвоєння, += та зворотний запис ByRef не можуть змінювати константу. Enum не викликається як функція.

## Повертає

Оголошення не повертає значення й не потребує дужок виклику. Елемент повертає Integer, наприклад Mode.Working = 3. Це стан, не автоматична ознака успіху. Порівняння state = Mode.Finished повертає 1/True або 0/False; для нього придатні обидві форми. Значення стану 0 може означати Idle, не помилку.

## Поведінка

- EnumCatalog під час підготовки обчислює попередні числові константи без виконання скрипту/API, призначає автоматичні значення, перевіряє імена, доступ і діапазон. SC026 блокує запуск навіть без Option Explicit. Синтаксичні помилки також блокують виконання; неповний текст у редакторі дає діагностику.
- DefinitionCollector додає незмінні елементи перед глобальними ініціалізаторами й Optional: вони можуть посилатися на Enum нижче у файлі. Усередині Enum доступні лише попередні константи. Підготовлений скрипт зберігає каталог, завантаження іншого його замінює.
- ScriptBindings один раз визначає модульні імена й Private. Виконання читає константи, без повторних обчислень у циклах і рефлексії. As Mode нормалізується до Integer, що може показувати відлагоджувач. Enum можна винести в Include. Flags, методів System.Enum, неявного імпорту й отримання списку елементів немає.

## Приклади

### 1. Назвати стани

```vb
# Idle=0 та Queued=1 призначаються автоматично. Working=10 змінює відлік, Finished=11. state As TaskState отримує 10; Main повертає String "0:1:10:11", використовуючи CStr для чисел. Назви можна замінити власними; оголошення не запускає процедури.
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**Пояснення параметрів і виконання:**

Idle=0 та Queued=1 призначаються автоматично. Working=10 змінює відлік, Finished=11. state As TaskState отримує 10; Main повертає String "0:1:10:11", використовуючи CStr для чисел. Назви можна замінити власними; оголошення не запускає процедури.

### 2. Приховати стан модуля

```vb
# Controller.Mode доступний лише Controller. NextMode отримує distance ByVal As Integer, не змінюючи аргумент виклику. distance<=1 вибирає Arrived=5, інакше Walking=4; state спочатку 0. Main передає 3 і 1, отримує 4 і 5 та повертає Integer 45. Це вхідні дані прикладу, не рух персонажа. Ззовні дозволено Controller.NextMode, але не Controller.Mode.Arrived.
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**Пояснення параметрів і виконання:**

Controller.Mode доступний лише Controller. NextMode отримує distance ByVal As Integer, не змінюючи аргумент виклику. distance<=1 вибирає Arrived=5, інакше Walking=4; state спочатку 0. Main передає 3 і 1, отримує 4 і 5 та повертає Integer 45. Це вхідні дані прикладу, не рух персонажа. Ззовні дозволено Controller.NextMode, але не Controller.Mode.Arrived.

### 3. Змінити стан і повернути Boolean

```vb
# Попередня Const FirstState=2 задає Idle=2, Working=3, Finished=4. Advance отримує state ByRef і змінює змінну Main; With Mode скорочує імена, Select Case обирає перехід. Два виклики дають 2→3→4. IsFinal отримує копію ByVal та порівнює з Finished: Main повертає 1/True. Після одного переходу було б 0/False. Наступний Advance створив би "No next state". Константи Mode незмінні.
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**Пояснення параметрів і виконання:**

Попередня Const FirstState=2 задає Idle=2, Working=3, Finished=4. Advance отримує state ByRef і змінює змінну Main; With Mode скорочує імена, Select Case обирає перехід. Два виклики дають 2→3→4. IsFinal отримує копію ByVal та порівнює з Finished: Main повертає 1/True. Після одного переходу було б 0/False. Наступний Advance створив би "No next state". Константи Mode незмінні.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
