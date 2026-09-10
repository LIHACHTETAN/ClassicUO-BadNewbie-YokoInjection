# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Do перевіряє умову перед тілом або після нього. While повторює при істині, Until — до істини. Repeat … Until є підтримуваною старою формою з перевіркою після тіла.

## Точний синтаксис

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## Параметри

- `condition / While / Until` — Логічний вираз: числові 0/False та 1/True. While продовжує при істині, Until при істині виходить. Вираз обчислюється на кожній перевірці; текст не розбирається як Boolean.
- `position / Repeat` — Умова після Do може пропустити перший прохід. Після Loop або Until у Repeat перевіряється щонайменше після одного проходу. Дозволено лише одну позицію умови. Безумовний Do … Loop потребує явного виходу.
- `statements / exit` — Тіло циклу. Continue Do переходить до наступної перевірки; Exit Do залишає найближчий Do або Repeat. Break залишає найближчий цикл будь-якого виду. RETURN завершує всю процедуру/функцію.

## Повертає

Do, Loop, Repeat, Until та Exit Do нічого не повертають. Приклади явно повертають з Main Integer 1,33,83 — поєднання лічильників, а не логічні результати команд.

## Поведінка

- Підготовка зіставляє блоки й перевіряє переходи. Умови одночасно на початку та в кінці одного Do спричиняють SC020. Рушій перевіряє вираз у вибраній позиції й повторює тіло за правилом While/Until.
- Continue Do з умовою в кінці обов’язково перевіряє цю умову; з умовою на початку повертає до заголовка. Під час виходу з Try його Finally виконується рівно один раз.
- Repeat спочатку виконує тіло: перевіряйте порожній масив до входу. Автоматичного таймауту немає. Для очікування гри використовуйте свідомий Wait та часову межу; пауза й зупинка працюють.

## Приклади

### 1. Перевірка перед і після

```vb
# ready=True вже задовольняє Until. Перший Do Until ready має нуль ітерацій: before=0. Другий перевіряє лише після збільшення after, тому after=1. Main повертає before*10+after=1.
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**Пояснення параметрів і виконання:**

ready=True вже задовольняє Until. Перший Do Until ready має нуль ітерацій: before=0. Другий перевіряє лише після збільшення after, тому after=1. Main повертає before*10+after=1.

### 2. Обмежені спроби із завершенням

```vb
# attempts починається з 0 й зростає щопроходу. Перші два Continue Do виконують Finally і перевірку attempts<4. На третій спробі Exit Do теж виконує Finally. attempts=3, cleanup=3, результат 33. Це локальна модель, а не реальні мережеві повтори.
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**Пояснення параметрів і виконання:**

attempts починається з 0 й зростає щопроходу. Перші два Continue Do виконують Finally і перевірку attempts<4. На третій спробі Exit Do теж виконує Finally. attempts=3, cleanup=3, результат 33. Це локальна модель, а не реальні мережеві повтори.

### 3. Старий цикл до маркера

```vb
# values містить 3,5,0 і гарантовано не порожній. Repeat читає комірку, збільшує index і суму. Until зупиняється при value=0 або межі масиву; OrElse пропускає другу перевірку після знайденого нуля. total=8 та index=3 дають 83.
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**Пояснення параметрів і виконання:**

values містить 3,5,0 і гарантовано не порожній. Repeat читає комірку, збільшує index і суму. Until зупиняється при value=0 або межі масиву; OrElse пропускає другу перевірку після знайденого нуля. total=8 та index=3 дають 83.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
