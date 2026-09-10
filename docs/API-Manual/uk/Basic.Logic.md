# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

NOT інвертує умову. AND вимагає обидві умови, OR — хоча б одну, XOR — рівно одну. && є записом AND, || — записом OR. Регістр ключових слів не важливий.

## Точний синтаксис

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## Параметри

- `left` — Ліва умова бінарної операції. AND/OR вимагають Integer або Decimal: нуль хибний, будь-яке ненульове число істинне.
- `right` — Права умова, для AND/OR також числова. Обчислюються обидва операнди: хибна ліва частина AND чи істинна ліва частина OR не пропускає цей вираз.
- `NOT / grouping` — Для NOT беріть цілу інвертовану умову в дужки. У поєднаннях AND, OR і XOR дужки явно задають групування.

## Повертає

Integer 1 (TRUE) або Integer 0 (FALSE). Це логічні, а не побітові операції: 2 AND 4 повертає 1, не бітову маску. Повернений прапорець можна перевіряти через =TRUE чи =1, =FALSE чи =0.

## Поведінка

- AND, OR і XOR у цьому рушії мають один пріоритет і виконуються зліва направо: TRUE OR FALSE AND FALSE дає 0. TRUE OR (FALSE AND FALSE) дає 1. Враховуйте це правило сумісності при перенесенні коду VB.
- NOT(condition) обчислює умову й змінює її істинність. На початку порівняння NOT 1=2 означає NOT(1=2). Якщо інвертоване значення є операндом порівняння, пишіть (NOT value) у дужках.
- AND/OR відхиляють String, Array, Object і Unit. Сумісні NOT та XOR натомість перевіряють рівність числовому нулю: текст "0", порожній рядок, масиви, об’єкти й Unit вважаються ненульовими. Для них явно задавайте числову умову; CBool має власні правила перетворення.
- Кожний правий вираз виконується, зокрема виклики функцій, очікування та їхні помилки. Дужки змінюють групування, але не обов’язковість обчислення. Якщо наступний вираз дозволений лише після успішної умови, використовуйте вкладені IF.

## Приклади

### 1. Поєднати іменовані прапорці

```vb
# ready=TRUE, blocked=FALSE. NOT(blocked) дає 1, тому canRun стає 1. ready XOR blocked істинне, бо істинний рівно один прапорець. Main повертає canRun*10+exclusive=11.
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**Пояснення параметрів і виконання:**

ready=TRUE, blocked=FALSE. NOT(blocked) дає 1, тому canRun стає 1. ready XOR blocked істинне, бо істинний рівно один прапорець. Main повертає canRun*10+exclusive=11.

### 2. Побачити обидва обов’язкові виклики

```vb
# Mark збільшує параметр counter, переданий ByRef, та повертає TRUE. Main починає з counter=0. FALSE AND Mark(counter) все одно викликає Mark; TRUE OR Mark(counter) викликає його знову. Результати умов — 0 та 1, Main повертає counter=2. Функцію Mark наведено повністю.
Option Explicit On
FUNCTION Mark(ByRef counter)
    counter = counter + 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR counter = 0
    VAR first = FALSE AND Mark(counter)
    VAR second = TRUE OR Mark(counter)
    RETURN counter
END SUB
```

**Пояснення параметрів і виконання:**

Mark збільшує параметр counter, переданий ByRef, та повертає TRUE. Main починає з counter=0. FALSE AND Mark(counter) все одно викликає Mark; TRUE OR Mark(counter) викликає його знову. Результати умов — 0 та 1, Main повертає counter=2. Функцію Mark наведено повністю.

### 3. Явно задати групування

```vb
# legacy спочатку обчислює TRUE OR FALSE, потім AND FALSE й отримує 0. grouped спочатку обчислює FALSE AND FALSE у дужках, потім OR із TRUE й отримує 1. Main повертає legacy*10+grouped=1.
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**Пояснення параметрів і виконання:**

legacy спочатку обчислює TRUE OR FALSE, потім AND FALSE й отримує 0. grouped спочатку обчислює FALSE AND FALSE у дужках, потім OR із TRUE й отримує 1. Main повертає legacy*10+grouped=1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
