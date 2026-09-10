# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

With об’єднує операції над одним збереженим об’єктом. Крапка перед іменем вибирає його метод. Basic також дозволяє With UO і With moduleName як явне зазначення простору імен; ці дві форми є розширеннями рушія.

## Точний синтаксис

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## Параметри

- `objectExpression / UO / moduleName` — Обов’язковий отримувач: об’єкт List(), Dictionary(), змінна з таким об’єктом або функція, що його повертає. Вираз обчислюється один раз при вході, навіть для порожнього тіла. Числа, рядки, масиви й Unit тут не підходять. Локальна змінна з об’єктом має пріоритет над однойменним модулем.
- `.Method(arguments) / .field` — Для об’єктів викликайте методи з дужками: .Add(value), .Item(index), .Count(). Параметри та результати не змінюються: див. Basic.List/Basic.Dictionary. Довільні поля й властивості об’єктів тут не підтримуються. У модуля доступні .field і .Procedure(arguments) з дотриманням Private. У With UO запис .Command(...) означає UO.Command(...); поза блоком ігрові команди й далі потребують UO.
- `statements / End With` — Тіло може бути порожнім або містити виклики, присвоєння, умови й правильно вкладені цикли/блоки. End With обов’язковий. Початкова крапка поза тілом спричиняє помилку. До інших об’єктів можна звертатися за повним іменем.

## Повертає

With — керувальний блок, а не функція: він не повертає ID, Boolean чи ознаку успіху. Кожен викликаний метод зберігає власний результат. Return у прикладах явно повертає Integer з Main; 127, 28 і 72 — розрахунки прикладів.

## Поведінка

- Підготовка перевіряє блок і зв’язує відносні імена. При вході інтерпретатор обчислює вираз і зберігає посилання на об’єкт в області поточного виклику. Зміна початкової змінної не змінює це посилання. Повторний вхід через заголовок обчислює вираз заново; рекурсивні виклики мають окремі посилання.
- Заголовок вкладеного With обчислюється в зовнішньому контексті; у тілі крапка вже означає внутрішній об’єкт. End With відновлює зовнішній контекст. Return, переходи циклу та GoTo назовні прибирають покинуті області після відповідних Finally. Перехід усередину тіла With заборонено.
- Невідповідний отримувач або невідомий метод спричиняє помилку, а не false. Її може обробити Catch/On Error. On Error Resume Next пропускає весь блок, якщо помилка виникла при обчисленні отримувача. With не повторює дії, не чекає й не створює потік. Перевірки паузи/зупинки зберігаються. Зв’язані імена кешуються з підготовленим скриптом; отримувач не обчислюється повторно для кожного методу.

## Приклади

### 1. Одне обчислення

```vb
# Choose отримує values через ByVal, а calls через ByRef, збільшує calls до 1 та повертає початковий список. Обидва .Add додають до збереженого списку 2 і 7, хоча між ними values отримує новий список. Item використовує індекси 0 і 1. Main повертає 1*100+2*10+7=127.
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**Пояснення параметрів і виконання:**

Choose отримує values через ByVal, а calls через ByRef, збільшує calls до 1 та повертає початковий список. Обидва .Add додають до збереженого списку 2 і 7, хоча між ними values отримує новий список. Item використовує індекси 0 і 1. Main повертає 1*100+2*10+7=127.

### 2. Вкладені об’єкти та завершення

```vb
# groups зберігає список child за рядковим ключем "child". .Item("child") отримує об’єкт через зовнішній словник. Внутрішні .Add(2) та .Add(7) у Finally змінюють список. Після End With .Set("result",8) знову звертається до словника. Count() дає два елементи, Item("result") — 8, тому Main повертає 28.
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**Пояснення параметрів і виконання:**

groups зберігає список child за рядковим ключем "child". .Item("child") отримує об’єкт через зовнішній словник. Внутрішні .Add(2) та .Add(7) у Finally змінюють список. Після End With .Set("result",8) знову звертається до словника. Count() дає два елементи, Item("result") — 8, тому Main повертає 28.

### 3. Поля модуля та простір UO

```vb
# With Tools уточнює .total, .AddAmount і .CountItems. total отримує 4; AddAmount приймає amount=3 через ByVal, тож виходить 7. CountItems приймає масив із двох елементів і через With UO викликає UO.GetArrayLength(values), отримуючи 2. Main обчислює 7*10+2=72. Правила доступу модуля зберігаються.
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**Пояснення параметрів і виконання:**

With Tools уточнює .total, .AddAmount і .CountItems. total отримує 4; AddAmount приймає amount=3 через ByVal, тож виходить 7. CountItems приймає масив із двох елементів і через With UO викликає UO.GetArrayLength(values), отримуючи 2. Main обчислює 7*10+2=72. Правила доступу модуля зберігаються.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
