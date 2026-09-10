# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

IF обирає не більше однієї гілки. Спочатку перевіряється IF, далі ELSEIF до першої істинної умови; якщо жодна не підійшла, виконується наявний ELSE. Потім виконання зазвичай триває після END IF.

## Точний синтаксис

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## Параметри

- `condition` — condition: вираз, що перевіряється один раз при вході. Числовий нуль хибний, ненульові числа істинні. Використовуйте явні порівняння чи логічні результати API.
- `elseifCondition` — elseifCondition: додаткова необов’язкова умова; перевіряється лише після хибності всіх попередніх. ELSEIF пишеться одним словом.
- `statements / ELSE` — statements / ELSE: інструкції на наступних рядках. ELSE необов’язковий, без умови, допускається один раз наприкінці. THEN і END IF обов’язкові; використовуйте багаторядковий блок.

## Повертає

Немає значення (Unit). IF — інструкція керування, не функція. Значення може дати умова чи RETURN обраної гілки. Логічні 1/0 можна порівнювати з TRUE/FALSE; IF count приймає будь-яку ненульову кількість, а IF count=TRUE відповідає лише 1.

## Поведінка

- Компілятор створює умовні переходи та переходи до виходу. Хибна гілка веде до наступної умови чи ELSE; обрана пропускає решту. Вкладений IF має власний ELSE. RETURN виходить із процедури, виконуючи зовнішній FINALLY.
- Для сумісності IF порівнює з числовим нулем, а не перетворює всі види через CBool. Текст "0", порожній текст, масиви, об’єкти та Unit не рівні числовому нулю, тож обирають істинну гілку. Текст перетворюйте явно чи порівнюйте потрібну властивість. AndAlso/OrElse вимагають числові операнди.
- Оголошення в пропущеній гілці не створюють змінних під час виконання. Спільні результати оголошуйте й ініціалізуйте до IF. Option Explicit перевіряє імена, але не присвоєння на кожному шляху. Кілька ELSE відхиляються з SC015 до запуску, навіть без Option Explicit.

## Приклади

### 1. Чотири варіанти

```vb
# Classify(value) перевіряє <0, =0, <10, потім ELSE. -2, 0, 7, 20 повертають negative, zero, small, large. Main об’єднує їх у "negative:zero:small:large". Один виклик виконує лише один RETURN.
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**Пояснення параметрів і виконання:**

Classify(value) перевіряє <0, =0, <10, потім ELSE. -2, 0, 7, 20 повертають negative, zero, small, large. Main об’єднує їх у "negative:zero:small:large". Один виклик виконує лише один RETURN.

### 2. Вкладені рішення

```vb
# Action(enabled, amount) спочатку перевіряє enabled. Якщо істина, amount>0 обирає work, інакше idle. Зовнішній ELSE дає disabled. Main викликає (TRUE,5), (TRUE,0), (FALSE,5) й повертає "work:idle:disabled". Кожен END IF закриває свій блок.
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**Пояснення параметрів і виконання:**

Action(enabled, amount) спочатку перевіряє enabled. Якщо істина, amount>0 обирає work, інакше idle. Зовнішній ELSE дає disabled. Main викликає (TRUE,5), (TRUE,0), (FALSE,5) й повертає "work:idle:disabled". Кожен END IF закриває свій блок.

### 3. Порядок перевірок

```vb
# Check(calls,value) збільшує calls через ByRef і повертає value. Перша умова хибна, друга істинна; третя та ELSE пропускаються. result=7, calls=2. Main повертає calls*10+result=27. Усі допоміжні функції й початкові значення наведені.
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**Пояснення параметрів і виконання:**

Check(calls,value) збільшує calls через ByRef і повертає value. Перша умова хибна, друга істинна; третя та ELSE пропускаються. result=7, calls=2. Main повертає calls*10+result=27. Усі допоміжні функції й початкові значення наведені.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
