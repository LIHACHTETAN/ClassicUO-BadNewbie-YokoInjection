# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

With объединяет операции над одним сохранённым объектом. Точка перед именем выбирает его метод. В Basic также есть With UO и With moduleName — явное указание пространства имён; эти две формы являются расширениями движка.

## Точный синтаксис

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

## Параметры

- `objectExpression / UO / moduleName` — Обязательный получатель: объект List(), Dictionary(), переменная с таким объектом либо функция, возвращающая объект. Выражение вычисляется один раз при входе, даже для пустого тела. Числа, строки, массивы и Unit здесь не подходят. Локальная переменная с объектом имеет приоритет над одноимённым модулем.
- `.Method(arguments) / .field` — У объектов вызывайте методы со скобками: .Add(value), .Item(index), .Count(). Параметры и результаты сохраняют обычный смысл: см. Basic.List/Basic.Dictionary. Произвольные поля и свойства объектов здесь не поддерживаются. У модуля доступны .field и .Procedure(arguments) с соблюдением Private. В With UO запись .Command(...) означает UO.Command(...); вне блока игровые команды по-прежнему требуют UO.
- `statements / End With` — Тело может быть пустым или содержать вызовы, присваивания, условия и правильно вложенные циклы/блоки. End With обязателен. Обращение с начальной точкой вне тела — ошибка. К другим объектам можно обращаться по полному имени.

## Возвращает

With — управляющий блок, а не функция: он не возвращает ID, Boolean или признак успеха. Каждый вызванный метод сохраняет собственный результат. Return в примерах явно возвращает Integer из Main; 127, 28 и 72 — расчёты примеров.

## Поведение

- При подготовке движок проверяет блок и связывает относительные имена. При входе интерпретатор вычисляет выражение и сохраняет ссылку на объект в области текущего вызова. Присваивание исходной переменной другого объекта эту ссылку не меняет. Повторный вход через заголовок вычисляет выражение заново; рекурсивные вызовы имеют отдельные ссылки.
- Заголовок вложенного With вычисляется в контексте внешнего блока; в его теле точка относится уже к внутреннему объекту. End With восстанавливает внешний контекст. Return, переходы цикла и GoTo наружу освобождают покидаемые области после соответствующих Finally. Переход внутрь тела With запрещён.
- Неподходящий получатель или неизвестный метод вызывает ошибку, а не false. Её может обработать Catch/On Error. Если ошибка возникла при вычислении получателя, On Error Resume Next пропускает весь блок. With сам не повторяет действия, не ждёт и не создаёт поток. Проверки паузы/остановки сохраняются. Связанные имена кэшируются с подготовленным скриптом; получатель не вычисляется заново при каждом вызове метода.

## Примеры

### 1. Одно вычисление получателя

```vb
# Choose получает values через ByVal, а calls через ByRef; увеличивает calls до 1 и возвращает исходный список. Оба .Add добавляют в сохранённый список значения 2 и 7, хотя между ними переменной values присвоен новый список. Item использует индексы 0 и 1. Main возвращает 1*100+2*10+7=127.
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

**Разбор параметров и выполнения:**

Choose получает values через ByVal, а calls через ByRef; увеличивает calls до 1 и возвращает исходный список. Оба .Add добавляют в сохранённый список значения 2 и 7, хотя между ними переменной values присвоен новый список. Item использует индексы 0 и 1. Main возвращает 1*100+2*10+7=127.

### 2. Вложенные объекты и завершение

```vb
# groups хранит список child под строковым ключом "child". .Item("child") получает объект через внешний словарь. Внутренние .Add(2) и .Add(7) в Finally меняют список. После End With запись .Set("result",8) снова обращается к словарю. Count() возвращает два элемента, Item("result") — 8, поэтому Main возвращает 28.
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

**Разбор параметров и выполнения:**

groups хранит список child под строковым ключом "child". .Item("child") получает объект через внешний словарь. Внутренние .Add(2) и .Add(7) в Finally меняют список. После End With запись .Set("result",8) снова обращается к словарю. Count() возвращает два элемента, Item("result") — 8, поэтому Main возвращает 28.

### 3. Поля модуля и пространство UO

```vb
# With Tools уточняет имена .total, .AddAmount и .CountItems. total получает 4, а AddAmount получает amount=3 через ByVal: получается 7. CountItems принимает массив из двух элементов и через With UO вызывает UO.GetArrayLength(values), получая 2. Main вычисляет 7*10+2=72. Правила доступа модуля сохраняются.
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

**Разбор параметров и выполнения:**

With Tools уточняет имена .total, .AddAmount и .CountItems. total получает 4, а AddAmount получает amount=3 через ByVal: получается 7. CountItems принимает массив из двух элементов и через With UO вызывает UO.GetArrayLength(values), получая 2. Main вычисляет 7*10+2=72. Правила доступа модуля сохраняются.

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
