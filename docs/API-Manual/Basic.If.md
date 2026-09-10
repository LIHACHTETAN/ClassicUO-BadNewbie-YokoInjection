# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

IF выбирает не более одной ветки. Сначала проверяется IF, затем условия ELSEIF до первого истинного результата; если ни одно не подошло, выполняется ELSE при его наличии. Затем выполнение обычно продолжается после END IF.

## Точный синтаксис

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

## Параметры

- `condition` — condition: выражение, однократно проверяемое при входе. Числовой ноль ложен, ненулевые числа истинны. Предпочитайте явные сравнения или логические результаты API.
- `elseifCondition` — elseifCondition: дополнительное необязательное условие; проверяется только после ложного результата всех предыдущих условий. ELSEIF пишется одним словом.
- `statements / ELSE` — statements / ELSE: инструкции на следующих строках. ELSE необязателен, не имеет условия и допускается один раз, последним. THEN и END IF обязательны; используйте многострочный блок.

## Возвращает

Нет значения (Unit). IF — инструкция управления, а не функция. Значение может вернуть условие или RETURN внутри выбранной ветки. Логические 1/0 можно сравнивать с TRUE/FALSE; IF count принимает любое ненулевое количество, а IF count=TRUE соответствует только 1.

## Поведение

- Компилятор создаёт условные переходы и переходы к выходу. Ложная ветка переходит к следующему условию или ELSE; выбранная пропускает остальные альтернативы. У вложенного IF свой ELSE. RETURN выходит из процедуры с выполнением окружающего FINALLY.
- Для совместимости IF сравнивает значение с числовым нулём, а не преобразует все виды через CBool. Текст "0", пустой текст, массив, объект и Unit не равны числовому нулю и выбирают истинную ветку. Текст преобразуйте явно либо сравнивайте нужное свойство. AndAlso/OrElse требуют числовые операнды.
- Объявления в пропущенной ветке не создают переменные при выполнении. Общий результат объявляйте и инициализируйте до IF. Option Explicit проверяет имена, но не доказывает присваивание на каждом пути. Несколько ELSE отклоняются с SC015 до запуска, в том числе без Option Explicit.

## Примеры

### 1. Четыре варианта значения

```vb
# Classify(value) по очереди проверяет <0, =0 и <10, затем использует ELSE. Аргументы -2, 0, 7, 20 возвращают negative, zero, small, large. Main соединяет их в "negative:zero:small:large". За вызов функции выполняется только один RETURN.
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

**Разбор параметров и выполнения:**

Classify(value) по очереди проверяет <0, =0 и <10, затем использует ELSE. Аргументы -2, 0, 7, 20 возвращают negative, zero, small, large. Main соединяет их в "negative:zero:small:large". За вызов функции выполняется только один RETURN.

### 2. Вложенные решения

```vb
# Action(enabled, amount) сначала проверяет enabled. Если истина, amount>0 выбирает work, иначе idle. Внешний ELSE возвращает disabled. Main вызывает (TRUE,5), (TRUE,0), (FALSE,5) и возвращает "work:idle:disabled". Каждый END IF закрывает свой блок.
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

**Разбор параметров и выполнения:**

Action(enabled, amount) сначала проверяет enabled. Если истина, amount>0 выбирает work, иначе idle. Внешний ELSE возвращает disabled. Main вызывает (TRUE,5), (TRUE,0), (FALSE,5) и возвращает "work:idle:disabled". Каждый END IF закрывает свой блок.

### 3. Порядок проверки условий

```vb
# Check(calls,value) увеличивает calls через ByRef и возвращает value. Первое условие ложно, второе истинно; третье условие и ELSE пропускаются. result равен 7, calls равен 2. Main возвращает calls*10+result=27. Все функции и начальные значения приведены целиком.
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

**Разбор параметров и выполнения:**

Check(calls,value) увеличивает calls через ByRef и возвращает value. Первое условие ложно, второе истинно; третье условие и ELSE пропускаются. result равен 7, calls равен 2. Main возвращает calls*10+result=27. Все функции и начальные значения приведены целиком.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
