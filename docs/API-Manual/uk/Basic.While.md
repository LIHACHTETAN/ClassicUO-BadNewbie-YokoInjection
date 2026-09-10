# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

While перевіряє умову перед кожною ітерацією та повторює тіло, доки вона істинна. Рушій закриває блок словом Wend; End While з VB.NET не підтримується.

## Точний синтаксис

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## Параметри

- `condition` — Вираз перевіряється перед кожним проходом, включно з першим і завершальним. Використовуйте порівняння або числовий Boolean: 0/False завершує, 1/True продовжує; інші ненульові числа також продовжують. Текст не перетворюється на Boolean.
- `statements` — Команди тіла виконують роботу й змінюють умову. Хибна перша перевірка пропускає все тіло.
- `Wend / exit` — Wend повертає до умови. Continue While перевіряє її знову; Exit While залишає найближчий While, навіть крізь внутрішній цикл іншого виду. Break залишає найближчий цикл будь-якого виду.

## Повертає

While, Wend, Exit While та Break нічого не повертають. RETURN у тілі завершує всю процедуру/функцію. Приклади повертають Integer 6,1,406. Результат пошуку 1 — індекс масиву, а не логічна ознака успіху.

## Поведінка

- Рушій перевіряє умову, виконує тіло та повертається до перевірки. На відміну від For, не зберігає числову межу й не змінює лічильник автоматично.
- Просування задавайте явно. Для постійного опитування гри додайте належний Wait і часову межу: While не спить та не має таймауту. Пауза й зупинка залишаються доступними.
- Continue та вихід виконують Finally блоків Try, які покидають. Заголовок, команди й Wend розміщуйте окремими рядками в процедурі або функції.

## Приклади

### 1. Сума цифр

```vb
# DigitSum приймає number=123 по ByVal. MOD 10 читає останню цифру, Fix(number/10) прибирає її: 123→12→1→0. total додає 3+2+1=6. Завершальна хибна перевірка виходить; Main отримує 6. Вхід 0 відразу повернув би 0.
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**Пояснення параметрів і виконання:**

DigitSum приймає number=123 по ByVal. MOD 10 читає останню цифру, Fix(number/10) прибирає її: 123→12→1→0. total додає 3+2+1=6. Завершальна хибна перевірка виходить; Main отримує 6. Вхід 0 відразу повернув би 0.

### 2. Перше співпадіння

```vb
# FirstAbove отримує values=[4,7,9], threshold=6. Перевірка межі захищає values[index]. За індексу 1 умова 7>6 зберігає found=1, а Exit While припиняє перегляд. Без збігів лишається -1; Main повертає індекс 1 з відліком від нуля.
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**Пояснення параметрів і виконання:**

FirstAbove отримує values=[4,7,9], threshold=6. Перевірка межі захищає values[index]. За індексу 1 умова 7>6 зберігає found=1, а Exit While припиняє перегляд. Без збігів лишається -1; Main повертає індекс 1 з відліком від нуля.

### 3. Кількість перевірок

```vb
# CanContinue приймає checks по ByRef, index і limit=3 по ByVal. Збільшує checks та повертає index<limit як 1/0. Перевірки при index=0,1,2,3 дають чотири виклики для трьох ітерацій. total=1+2+3=6; Main повертає 406.
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**Пояснення параметрів і виконання:**

CanContinue приймає checks по ByRef, index і limit=3 по ByVal. Збільшує checks та повертає index<limit як 1/0. Перевірки при index=0,1,2,3 дають чотири виклики для трьох ітерацій. total=1+2+3=6; Main повертає 406.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
