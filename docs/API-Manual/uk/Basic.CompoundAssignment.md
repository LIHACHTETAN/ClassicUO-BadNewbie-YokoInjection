# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Змінюйте наявну змінну або елемент масиву через +=, -=, *=, /=. Рушій читає поточне значення, виконує операцію та записує результат, не обчислюючи ціль двічі.

## Точний синтаксис

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## Параметри

- `target` — target: наявне скалярне ім’я або елемент items[index], grid[x][y]. Елементи мають бути ініціалізовані, індекси допустимі та починаються з нуля. Інструкція не оголошує змінну.
- `operator` — += і &= додають числа або поєднують дві String; -= віднімає; *= множить; /= ділить. Препроцесор замінює &= на +=, тому 5 &= 3 зберігає 8. Для String і числа потрібен явний CStr. Оператор пишеться одним токеном.
- `value` — value: вираз, який обчислюється один раз після цілі та індексів. Його вид має відповідати операції. Перед додаванням числа до String перетворіть його через CStr.

## Повертає

Немає значення (Unit). Це інструкція, а не вираз чи прапорець успіху. Прочитайте target наступним рядком для отримання збереженого результату. При записі скаляра діє AS: Integer 5 після /=2 зберігає Integer 2, а нетипізована числова змінна отримує Decimal 2.5.

## Поведінка

- Посилання на кожний масив фіксується до обчислення його індексу. Індекси обчислюються один раз зліва направо, межі перевіряються до правого операнда. Вибрана комірка залишається ціллю, навіть якщо функція ByRef в індексі чи праворуч замінить змінну масиву або батьківську комірку.
- Правила ті самі, що для +, -, *, /: цілі переповнюються у межах знакових 32 бітів, / дає Decimal, при діленні на нуль можливі Infinity/NaN. Додавання String/числа помилкове. Елементи масиву не мають скалярного перетворення AS.
- Неоголошена ціль, неініціалізований елемент, неправильний індекс, несумісна операція, запис CONST чи невдале перетворення спричиняють оброблювану помилку. Кінцевий запис не відбувається, але вже виконані дії функцій-операндів не скасовуються. CONST та AS перевіряються при записі скаляра після можливого виконання правої частини.
- Option Explicit перевіряє імена до запуску. Точки зупинки та спостереження використовують початковий рядок; цикли зберігають перевірки паузи й зупинки. Читання, розрахунок і запис не є атомарною синхронізацією паралельних процедур.

## Приклади

### 1. Усі чотири операції

```vb
# amount починається з 10. +=2 дає 12, -=3 дає 9, *=4 дає 36, /=2 дає Decimal 18. Main повертає збережене значення; інструкції присвоєння самі значення не повертають.
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**Пояснення параметрів і виконання:**

amount починається з 10. +=2 дає 12, -=3 дає 9, *=4 дає 36, /=2 дає Decimal 18. Main повертає збережене значення; інструкції присвоєння самі значення не повертають.

### 2. Індекс обчислюється один раз

```vb
# NextIndex збільшує параметр calls, переданий ByRef, та повертає індекс 0. items[0] починається з 5, +=2 змінює його на 7. NextIndex викликається один раз, тому calls=1. Main повертає items[0]*10+calls=71. Допоміжну функцію наведено повністю.
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**Пояснення параметрів і виконання:**

NextIndex збільшує параметр calls, переданий ByRef, та повертає індекс 0. items[0] починається з 5, +=2 змінює його на 7. NextIndex викликається один раз, тому calls=1. Main повертає items[0]*10+calls=71. Допоміжну функцію наведено повністю.

### 3. Обробити захист константи

```vb
# limit оголошений як CONST 5. Спроба limit+=1 спричиняє помилку запису; CATCH зберігає її у problem і ставить caught=TRUE. limit залишається 5. Main повертає "5:1" з явними CStr. Прапорець описує обробку помилки, не результат присвоєння. Рядок складається у змінній: report=CStr(limit), потім report &= ":" і report &= CStr(caught). Кожне &= оновлює report; Return report повертає "5:1".
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**Пояснення параметрів і виконання:**

limit оголошений як CONST 5. Спроба limit+=1 спричиняє помилку запису; CATCH зберігає її у problem і ставить caught=TRUE. limit залишається 5. Main повертає "5:1" з явними CStr. Прапорець описує обробку помилки, не результат присвоєння. Рядок складається у змінній: report=CStr(limit), потім report &= ":" і report &= CStr(caught). Кожне &= оновлює report; Return report повертає "5:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
