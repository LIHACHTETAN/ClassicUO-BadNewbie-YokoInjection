# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Public открывает участника модуля для внешнего кода. Private оставляет его доступным только функциям, процедурам и инициализаторам своего модуля. Модификатор пишется перед объявлением, а не перед вызовом.

## Точный синтаксис

```text
Public declaration
Private declaration
```

## Параметры

- `visibility` — visibility: Public или Private. Без модификатора SUB/FUNCTION внутри модуля публичные, VAR/DIM и CONST приватные.
- `declaration` — declaration: SUB/FUNCTION, скалярный VAR/DIM или CONST. Public допустим также для Module и объявлений уровня файла; Private на уровне файла и внутри тела процедуры запрещён. Имена участников объявляются без точки.

## Возвращает

Public и Private не возвращают значения. Они не меняют результат функции или тип поля. Normalize(12) в примере возвращает Integer 10 через RETURN; NextCount() возвращает новое количество, а не TRUE/FALSE.

## Поведение

- Внутри Module разрешены и короткие, и полные имена своих участников. Внешний код обращается только к Public через ModuleName.Member. Public не делает поле автоматически доступным без имени модуля.
- Проверка выполняется до запуска, в том числе при Option Explicit Off: обращение к чужому Private даёт SC019, некорректное объявление модуля/модификатора — SC018 или синтаксическую ошибку. Инициализаторы не выполняются после такой ошибки.
- Публичная функция может вызывать приватный помощник: доступ определяется местом объявления вызывающей функции, а не тем, кто запустил её. Private нельзя отдельно запустить из IDE, горячей клавиши или внешнего вызова процедуры.
- Public Const остаётся константой; Public Var остаётся изменяемым полем. Явная локальная переменная с тем же именем перекрывает поле только в своей процедуре. Приватность не шифрует файл и не скрывает код от его владельца.
- В отладчике короткие имена и Private проверяются относительно выбранного кадра. Внутри модуля поле видно; при выборе внешнего вызывающего кадра прямое выражение ModuleName.privateField отклоняется.

## Примеры

### 1. Публичная оболочка, приватный помощник

```vb
# value=12 передаётся в Limits.Normalize, затем в Clamp. maximum=10 ограничивает результат: Clamp и Normalize возвращают Integer 10. Main вызывает только публичный Normalize; прямой Limits.Clamp(12) снаружи запрещён.
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

**Разбор параметров и выполнения:**

value=12 передаётся в Limits.Normalize, затем в Clamp. maximum=10 ограничивает результат: Clamp и Normalize возвращают Integer 10. Main вызывает только публичный Normalize; прямой Limits.Clamp(12) снаружи запрещён.

### 2. Приватное поле и локальная переменная

```vb
# VAR value=7 без модификатора приватна в Store. Read возвращает поле 7. LocalValue объявляет собственную value=9, не изменяя поле. Main возвращает 7*10+9, Integer 79.
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

**Разбор параметров и выполнения:**

VAR value=7 без модификатора приватна в Store. Read возвращает поле 7. LocalValue объявляет собственную value=9, не изменяя поле. Main возвращает 7*10+9, Integer 79.

### 3. Константа наружу, счётчик внутрь

```vb
# Public Const increment=2 можно читать как Counter.increment. Private count начинается с 1. NextCount прибавляет increment, сохраняет 3 и возвращает 3. Main возвращает 3*10+2, Integer 32. Внешняя запись Counter.count и изменение increment запрещены.
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

**Разбор параметров и выполнения:**

Public Const increment=2 можно читать как Counter.increment. Private count начинается с 1. NextCount прибавляет increment, сохраняет 3 и возвращает 3. Main возвращает 3*10+2, Integer 32. Внешняя запись Counter.count и изменение increment запрещены.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
