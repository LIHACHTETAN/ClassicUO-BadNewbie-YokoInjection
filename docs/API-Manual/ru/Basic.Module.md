# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Module объединяет функции, процедуры, VAR/DIM и CONST под одним именем. Снаружи используются имена Tools.Sum или Counter.count; внутри модуля можно писать короткое имя своего участника.

## Точный синтаксис

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## Параметры

- `moduleName` — moduleName: простой идентификатор, например Tools. Регистр не учитывается. UO зарезервирован. Модули с одинаковым именем и вложенные Module не допускаются.
- `members` — members: SUB/FUNCTION, скалярные VAR/DIM, CONST, Include и допустимая директива Option Explicit. Участники могут содержать обычные массивы или объекты как значения. Объявление массива DIM[...] непосредственно в модуле не поддерживается; его можно создать функцией и сохранить в VAR.
- `member / arguments` — member / arguments: имя участника и аргументы его функции. Запись Tools.Sum(2, 3) передаёт 2 в left и 3 в right. Доступ к полю Counter.count не требует скобок.

## Возвращает

Сам Module ничего не возвращает и не вызывается как Module(...). Значение Tools.Sum(...) задаёт RETURN этой функции. Поле возвращает сохранённое значение. Результат сравнения равен Integer 1 или 0: в условиях и сравнении с TRUE/FALSE эти значения соответствуют истине/лжи. Произвольное число, ID или количество не следует описывать как булев результат.

## Поведение

- Размещайте Module на уровне файла и завершайте End Module. Include может загружать целый модуль или его участников; вложенный файл сохраняет свои файл и строку в ошибках. Option Explicit остаётся директивой физического файла.
- Подготовка собирает полные имена, связывает короткие ссылки с текущим модулем и проверяет доступ до запуска. Явно объявленный локальный параметр, VAR, CONST или DIM имеет приоритет над полем с таким же именем. Иначе сначала ищется поле текущего модуля, затем обычная глобальная переменная.
- Поля модуля инициализируются при начале отдельного запуска в порядке объявлений. Вложенные вызовы этого запуска видят общие изменения полей. Новый запуск создаёт новые значения; разные одновременно запущенные скрипты не делят это состояние. Это не сохранение настроек на диск.
- Функции/процедуры без модификатора в модуле публичные; поля и константы по умолчанию приватные. Private разрешён только внутри Module. См. раздел Public / Private.
- IDE показывает полные имена процедур. Публичную процедуру без обязательных аргументов можно запускать из списка; приватная остаётся внутренним помощником. Подсказки, переход к объявлению и просмотр переменных учитывают текущий модуль.

## Примеры

### 1. Одинаковые имена в разных модулях

```vb
# Tools.Sum складывает left=2 и right=3, возвращая 5. Other.Sum умножает те же аргументы и возвращает 6. Полные имена различают функции; Main возвращает Integer 11.
Option Explicit On
Module Tools
    Public Function Sum(ByVal left, ByVal right)
        Return left + right
    End Function
End Module
Module Other
    Public Function Sum(ByVal left, ByVal right)
        Return left * right
    End Function
End Module
Sub Main()
    Return Tools.Sum(2, 3) + Other.Sum(2, 3)
End Sub
```

**Разбор параметров и выполнения:**

Tools.Sum складывает left=2 и right=3, возвращая 5. Other.Sum умножает те же аргументы и возвращает 6. Полные имена различают функции; Main возвращает Integer 11.

### 2. Общее поле одного запуска

```vb
# count начинается с 0. Каждый Increment изменяет одно и то же поле на 1; после двух вызовов before=2. Присваивание Counter.count=5 видно функции Read. Main возвращает 2*10+5, то есть Integer 25. Новый запуск снова начинает с 0.
Option Explicit On
Module Counter
    Public Var count As Integer = 0
    Public Sub Increment()
        count += 1
    End Sub
    Public Function Read()
        Return count
    End Function
End Module
Sub Main()
    Counter.Increment()
    Counter.Increment()
    Var before = Counter.Read()
    Counter.count = 5
    Return before * 10 + Counter.Read()
End Sub
```

**Разбор параметров и выполнения:**

count начинается с 0. Каждый Increment изменяет одно и то же поле на 1; после двух вызовов before=2. Присваивание Counter.count=5 видно функции Read. Main возвращает 2*10+5, то есть Integer 25. Новый запуск снова начинает с 0.

### 3. Булев результат функции

```vb
# maximum=4 доступен внутри Limits. Allowed(3) возвращает Integer 1, Allowed(7) — Integer 0. Сравнения accepted=TRUE и rejected=FALSE проверяют именно эти результаты; при успехе Main возвращает Integer 10.
Option Explicit On
Module Limits
    Private Const maximum = 4
    Public Function Allowed(ByVal amount)
        Return amount <= maximum
    End Function
End Module
Sub Main()
    Var accepted = Limits.Allowed(3)
    Var rejected = Limits.Allowed(7)
    If accepted = TRUE AndAlso rejected = FALSE Then
        Return 10
    End If
    Return 0
End Sub
```

**Разбор параметров и выполнения:**

maximum=4 доступен внутри Limits. Allowed(3) возвращает Integer 1, Allowed(7) — Integer 0. Сравнения accepted=TRUE и rejected=FALSE проверяют именно эти результаты; при успехе Main возвращает Integer 10.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
