# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Module об’єднує функції, процедури, VAR/DIM і CONST під одним ім’ям. Ззовні пишіть Tools.Sum або Counter.count; усередині модуля дозволені короткі імена його учасників.

## Точний синтаксис

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## Параметри

- `moduleName` — moduleName: простий ідентифікатор без урахування регістру, наприклад Tools. UO зарезервовано. Повторні імена модулів і вкладені Module заборонені.
- `members` — members: SUB/FUNCTION, скалярні VAR/DIM, CONST, Include і коректна директива Option Explicit. Поле може містити масив чи об’єкт. DIM[...] безпосередньо в модулі не підтримується; створіть масив функцією та збережіть у VAR.
- `member / arguments` — member / arguments: ім’я учасника й аргументи функції. Tools.Sum(2, 3) передає left=2 і right=3. Поле Counter.count читається без дужок.

## Повертає

Module не повертає значення й не викликається як Module(...). Tools.Sum(...) повертає значення RETURN функції; поле — збережене значення. Порівняння повертає Integer 1/0, що відповідає TRUE/FALSE в умовах і порівняннях. Довільне число, ID або кількість не є автоматично булевим результатом.

## Поведінка

- Оголошуйте Module на рівні файлу, завершуйте End Module. Include може підключати весь модуль або його учасників; помилки зберігають файл і рядок бібліотеки. Option Explicit належить фізичному файлу.
- Підготовка збирає повні імена, зв’язує короткі посилання з поточним модулем і перевіряє доступ до запуску. Явний локальний параметр, VAR, CONST або DIM перекриває однойменне поле. Інакше шукається поле модуля, потім звичайна глобальна змінна.
- Поля ініціалізуються в порядку оголошень на початку окремого запуску. Вкладені виклики цього запуску бачать спільні зміни полів. Новий запуск починається заново; паралельні скрипти не ділять стан модуля. На диск налаштування не зберігаються.
- Функції/процедури модуля типово Public; поля/константи типово Private. Private дозволено тільки в Module. Див. Public / Private.
- IDE показує повні імена процедур. Публічну процедуру без обов’язкових аргументів можна запускати зі списку; приватні помічники залишаються внутрішніми. Підказки, навігація та перегляд змінних ураховують модуль.

## Приклади

### 1. Однакові імена в різних модулях

```vb
# Tools.Sum додає left=2 і right=3 та повертає 5. Other.Sum множить їх і повертає 6. Повні імена розрізняють функції; Main повертає Integer 11.
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

**Пояснення параметрів і виконання:**

Tools.Sum додає left=2 і right=3 та повертає 5. Other.Sum множить їх і повертає 6. Повні імена розрізняють функції; Main повертає Integer 11.

### 2. Спільне поле запуску

```vb
# count починається з 0. Кожен Increment додає 1 до того самого поля; після двох викликів before=2. Counter.count=5 бачить Read. Main повертає 2*10+5, Integer 25. Новий запуск знову починається з 0.
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

**Пояснення параметрів і виконання:**

count починається з 0. Кожен Increment додає 1 до того самого поля; після двох викликів before=2. Counter.count=5 бачить Read. Main повертає 2*10+5, Integer 25. Новий запуск знову починається з 0.

### 3. Булевий результат

```vb
# maximum=4 доступний усередині Limits. Allowed(3) повертає Integer 1, Allowed(7) — Integer 0. accepted=TRUE і rejected=FALSE перевіряють ці результати. За успіху Main повертає Integer 10.
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

**Пояснення параметрів і виконання:**

maximum=4 доступний усередині Limits. Allowed(3) повертає Integer 1, Allowed(7) — Integer 0. accepted=TRUE і rejected=FALSE перевіряють ці результати. За успіху Main повертає Integer 10.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
