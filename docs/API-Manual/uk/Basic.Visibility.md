# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Public відкриває учасника модуля зовнішньому коду. Private дозволяє доступ тільки функціям, процедурам та ініціалізаторам свого модуля. Модифікатор ставиться перед оголошенням, а не викликом.

## Точний синтаксис

```text
Public declaration
Private declaration
```

## Параметри

- `visibility` — visibility: Public або Private. Без модифікатора SUB/FUNCTION модуля публічні, VAR/DIM/CONST приватні.
- `declaration` — declaration: SUB/FUNCTION, скалярний VAR/DIM або CONST. Public дозволений також для Module й оголошень рівня файлу. Private на рівні файлу й у тілі процедури заборонений. Ім’я учасника оголошуйте без крапки.

## Повертає

Public і Private не повертають значення та не змінюють тип поля чи результат функції. Normalize(12) повертає Integer 10 через RETURN; NextCount() повертає нову кількість, а не TRUE/FALSE.

## Поведінка

- У Module доступні короткі й повні імена власних учасників. Ззовні дозволено тільки Public через ModuleName.Member. Public не переносить поле до простору коротких глобальних імен.
- Доступ перевіряється до запуску навіть з Option Explicit Off. Чужий Private дає SC019; некоректне оголошення модуля/модифікатора — SC018 або синтаксичну помилку. Ініціалізатори після цих помилок не виконуються.
- Публічна функція може викликати приватний допоміжний код: важливе місце оголошення функції, а не зовнішній ініціатор. Private не можна окремо запустити з IDE, гарячої клавіші чи зовнішнього API процедур.
- Public Const залишається незмінним, Public Var — змінним полем. Явна локальна змінна перекриває однойменне поле лише у своїй процедурі. Private не шифрує вихідний файл і не приховує код від власника.
- Короткі імена й доступ до Private у відлагоджувачі залежать від вибраного кадру. Усередині модуля поле доступне; у зовнішньому кадрі вираз ModuleName.privateField відхиляється.

## Приклади

### 1. Публічна оболонка і приватний помічник

```vb
# value=12 надходить до Limits.Normalize, потім Clamp. maximum=10 обмежує значення; обидві функції повертають Integer 10. Main викликає лише Normalize. Прямий зовнішній Limits.Clamp(12) заборонений.
Option Explicit On
Module Limits
    Private Const maximum = 10
    Private Function Clamp(ByVal value)
        If value > maximum Then
            Return maximum
        End If
        Return value
    End Function
    Public Function Normalize(ByVal value)
        Return Clamp(value)
    End Function
End Module
Sub Main()
    Return Limits.Normalize(12)
End Sub
```

**Пояснення параметрів і виконання:**

value=12 надходить до Limits.Normalize, потім Clamp. maximum=10 обмежує значення; обидві функції повертають Integer 10. Main викликає лише Normalize. Прямий зовнішній Limits.Clamp(12) заборонений.

### 2. Приватне поле й локальна змінна

```vb
# VAR value=7 без модифікатора приватна в Store. Read повертає поле 7; LocalValue має власну value=9 і не змінює поле. Main повертає 7*10+9, Integer 79.
Option Explicit On
Module Store
    Var value = 7
    Public Function Read()
        Return value
    End Function
    Public Function LocalValue()
        Var value = 9
        Return value
    End Function
End Module
Sub Main()
    Return Store.Read() * 10 + Store.LocalValue()
End Sub
```

**Пояснення параметрів і виконання:**

VAR value=7 без модифікатора приватна в Store. Read повертає поле 7; LocalValue має власну value=9 і не змінює поле. Main повертає 7*10+9, Integer 79.

### 3. Публічна константа, внутрішній лічильник

```vb
# Public Const increment=2 читається як Counter.increment. Private count починається з 1. NextCount додає increment, зберігає й повертає 3. Main повертає 3*10+2, Integer 32. Зовнішній доступ до Counter.count та зміна increment заборонені.
Option Explicit On
Module Counter
    Public Const increment = 2
    Private Var count = 1
    Public Function NextCount()
        count += increment
        Return count
    End Function
End Module
Sub Main()
    Var result = Counter.NextCount()
    Return result * 10 + Counter.increment
End Sub
```

**Пояснення параметрів і виконання:**

Public Const increment=2 читається як Counter.increment. Private count починається з 1. NextCount додає increment, зберігає й повертає 3. Main повертає 3*10+2, Integer 32. Зовнішній доступ до Counter.count та зміна increment заборонені.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
