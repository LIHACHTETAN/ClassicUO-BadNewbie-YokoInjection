# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Enum объединяет именованные константы Integer для состояний и режимов скрипта. Объявляется на уровне файла или Module, вне Sub/Function. Поддерживается полезная часть перечислений VB.NET; объект .NET Enum не создаётся.

## Точный синтаксис

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## Параметры

- `Public / Private` — Public действует по умолчанию, в том числе внутри Module. Private разрешён только внутри Module и скрывает тип и его элементы от других модулей и уровня файла.
- `name` — Одно простое имя, например Mode, без точек; регистр не важен. UO и имена встроенных типов зарезервированы. Нельзя повторять полное имя Enum, Module или глобальной переменной.
- `As Integer` — Необязательная часть. Поддерживается только знаковый Integer, 32 бита: -2147483648..2147483647. Другие базовые типы отклоняются. As Mode у переменной, параметра или результата Function использует хранение и преобразование Integer; значение не ограничивается перечисленными элементами. Без инициализации такая переменная равна 0.
- `member` — Одно простое имя элемента на строку; нужен хотя бы один элемент. Повторы имён, True и False запрещены. Без выражения первый элемент равен 0, следующий — предыдущему плюс 1. Разные имена могут иметь одинаковые значения.
- `constantExpression` — Необязательное константное выражение: целые десятичные/шестнадцатеричные 0x числа, скобки, унарный минус, + - * / Mod, предыдущие элементы и уже объявленные числовые Const. Итог должен быть целым в допустимом диапазоне; промежуточное деление может быть дробным. Выражение используемой Const тоже должно давать целый Integer, а её тип — отсутствовать либо быть Integer/Long/Short/Byte. Вызовы функций, переменные, строки, сравнения и чтение массивов запрещены. Ссылки на последующие элементы, циклы зависимостей Const и глубина более 128 уровней отклоняются.
- `name.member` — Чтение: Mode.Ready, снаружи модуля — Tools.Mode.Ready. Внутри Tools достаточно Mode.Ready; With Mode позволяет .Ready. Константы неизменяемы: присваивание, += и обратная запись через ByRef не могут менять элемент. Тип Enum нельзя вызывать как функцию.

## Возвращает

Само объявление ничего не возвращает и не требует скобок вызова. Чтение элемента возвращает Integer, например Mode.Working = 3. Это значение состояния, а не автоматический признак успеха. Сравнивайте с именованным состоянием. Boolean-выражение state = Mode.Finished возвращает 1/True либо 0/False; для такого сравнения подходят обе записи. Само значение состояния 0 может обозначать Idle, а не ошибку.

## Поведение

- При подготовке EnumCatalog обходит объявления, вычисляет предыдущие числовые константы без запуска скрипта/API, назначает автоматические значения и проверяет имена, доступ и диапазон. Ошибка SC026 блокирует запуск даже без Option Explicit. Синтаксические ошибки тоже блокируют выполнение; недописанное объявление в редакторе даёт диагностику.
- DefinitionCollector добавляет неизменяемые элементы до инициализации глобальных переменных и значений Optional: там можно обратиться к Enum, объявленному ниже в файле. Внутри самого Enum доступны только предыдущие константы. Подготовленный скрипт хранит фиксированный каталог; загрузка другого скрипта заменяет его.
- ScriptBindings один раз разрешает имена относительно модуля и проверяет Private. При выполнении читается обычная константа: циклы не пересчитывают Enum и не используют рефлексию. As Mode преобразуется в Integer; отладчик может показывать тип Integer. Объявление можно вынести в Include. Здесь нет атрибута Flags, методов System.Enum, неявного импорта элементов и автоматического получения списка элементов.

## Примеры

### 1. Назвать состояния скрипта

```vb
# TaskState автоматически получает Idle=0 и Queued=1. Working=10 меняет отсчёт, поэтому Finished=11. Переменная state As TaskState получает 10. Main возвращает String "0:1:10:11"; CStr превращает числа в текст для вывода. Названия можно заменить состояниями своего скрипта; объявление ничего не запускает.
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

**Разбор параметров и выполнения:**

TaskState автоматически получает Idle=0 и Queued=1. Working=10 меняет отсчёт, поэтому Finished=11. Переменная state As TaskState получает 10. Main возвращает String "0:1:10:11"; CStr превращает числа в текст для вывода. Названия можно заменить состояниями своего скрипта; объявление ничего не запускает.

### 2. Скрыть состояние внутри модуля

```vb
# Controller.Mode доступен только Controller. NextMode принимает distance ByVal As Integer: исходный аргумент вызывающего кода не меняется. distance<=1 выбирает Arrived=5, иначе Walking=4. Переменная state изначально равна Integer 0. Main передаёт 3 и 1, получает 4 и 5 и возвращает Integer 45. Передвижения здесь нет: distance — входные данные примера. Снаружи можно вызвать Controller.NextMode, но нельзя прочитать Controller.Mode.Arrived.
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

**Разбор параметров и выполнения:**

Controller.Mode доступен только Controller. NextMode принимает distance ByVal As Integer: исходный аргумент вызывающего кода не меняется. distance<=1 выбирает Arrived=5, иначе Walking=4. Переменная state изначально равна Integer 0. Main передаёт 3 и 1, получает 4 и 5 и возвращает Integer 45. Передвижения здесь нет: distance — входные данные примера. Снаружи можно вызвать Controller.NextMode, но нельзя прочитать Controller.Mode.Arrived.

### 3. Перейти между состояниями и вернуть Boolean

```vb
# FirstState=2 — предыдущая константа Integer. Mode.Idle=2, Working=3, Finished=4. Advance получает state ByRef и меняет переменную Main; With Mode сокращает имена, Select Case выбирает переход. Два вызова выполняют 2→3→4. IsFinal получает копию ByVal и сравнивает с Finished, возвращая 1/True. Поэтому Main возвращает Integer 1; после одного перехода IsFinal вернул бы 0/False. Ещё один Advance вызвал бы ошибку "No next state". Константы Mode при этом никогда не изменяются.
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

**Разбор параметров и выполнения:**

FirstState=2 — предыдущая константа Integer. Mode.Idle=2, Working=3, Finished=4. Advance получает state ByRef и меняет переменную Main; With Mode сокращает имена, Select Case выбирает переход. Два вызова выполняют 2→3→4. IsFinal получает копию ByVal и сравнивает с Finished, возвращая 1/True. Поэтому Main возвращает Integer 1; после одного перехода IsFinal вернул бы 0/False. Ещё один Advance вызвал бы ошибку "No next state". Константы Mode при этом никогда не изменяются.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
