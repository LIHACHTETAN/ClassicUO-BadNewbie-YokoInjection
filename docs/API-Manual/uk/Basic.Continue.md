# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Continue пропускає решту тіла найближчого зовнішнього циклу вказаного виду. Continue For працює для числового For і For Each, Continue Do — для Do/Loop та Repeat/Until, Continue While — для While/Wend.

## Точний синтаксис

```text
Continue For
Continue Do
Continue While
```

## Параметри

- `kind` — kind: обов’язкове For, Do або While після Continue. Дужки й аргументи результату не потрібні. Цикл має охоплювати оператор у тій самій процедурі; вкладений цикл іншого виду не перехоплює перехід.

## Повертає

Continue не повертає значення й не використовується у виразах. Це не TRUE/FALSE і не перезапуск процедури. Функція згодом може повернути результат через RETURN; приклади повертають Integer 10, 3 і 34.

## Поведінка

- For виконує NEXT з урахуванням STEP та перевіряє наступне значення щодо межі; For Each отримує наступний елемент. Після завершення перебору цикл закінчується. Ініціалізація лічильника й вираз колекції не обчислюються повторно.
- Do з умовою на початку перевіряє її знову на початку; умова в Loop перевіряється в кінці. Repeat/Until використовує UNTIL. Безумовний Do/Loop триває до виходу чи зупинки. While перевіряє WHILE знову; Continue Do не обирає While/Wend.
- Підготовка визначає адресу найближчого циклу потрібного виду. За відсутності такого циклу SC020 виникає до ініціалізації навіть без Option Explicit. Перевіряються NEXT та завершення. Сумісність старого FOR/NEXT через межу IF збережена.
- Перехід із TRY/CATCH спочатку виконує всі перетнуті FINALLY зсередини назовні, кожен один раз. Якщо весь цикл усередині TRY, його FINALLY не виконується на кожній ітерації. RETURN або помилка у FINALLY замінює відкладений перехід.
- Continue не додає затримки. Змінюйте умову або використовуйте належне очікування під час опитування, інакше цикл може бути нескінченним. Пауза й зупинка перевіряються. Покинуті нативні перелічувачі звільняються; запуски незалежні. Exit For/Do/While виходить із вибраного циклу.

## Приклади

### 1. Пропуск елементів

```vb
# values містить -2, 4, 0, 6. item<=0 викликає Continue For для -2 та 0, пропускаючи total+=item. Це працює й у For Each. SumPositive та Main повертають Integer 10, суму 4+6.
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**Пояснення параметрів і виконання:**

values містить -2, 4, 0, 6. item<=0 викликає Continue For для -2 та 0, пропускаючи total+=item. Це працює й у For Each. SumPositive та Main повертають Integer 10, суму 4+6.

### 2. Зовнішній цикл за видом

```vb
# AdvanceTo отримує limit=3, count починається з 0. Усередині While True count збільшується, а Continue Do переходить до зовнішнього Do. Його умова перевіряється щоразу; count=3 завершує цикл і повертає Integer 3.
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**Пояснення параметрів і виконання:**

AdvanceTo отримує limit=3, count починається з 0. Усередині While True count збільшується, а Continue Do переходить до зовнішнього Do. Його умова перевіряється щоразу; count=3 завершує цикл і повертає Integer 3.

### 3. Завершення пропущеної ітерації

```vb
# Process отримує limit=3 і skip=2. i проходить 1, 2, 3. Друга ітерація пропускає total+=i, але Finally збільшує cleanup усі три рази. total=4, cleanup=3; RETURN cleanup*10+total повертає Integer 34.
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**Пояснення параметрів і виконання:**

Process отримує limit=3 і skip=2. i проходить 1, 2, 3. Друга ітерація пропускає total+=i, але Finally збільшує cleanup усі три рази. total=4, cleanup=3; RETURN cleanup*10+total повертає Integer 34.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
