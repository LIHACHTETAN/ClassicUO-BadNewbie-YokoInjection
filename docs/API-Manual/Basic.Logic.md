# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

NOT инвертирует условие. AND требует оба условия, OR — хотя бы одно, XOR — ровно одно. && является записью AND, || — записью OR. Регистр ключевых слов не важен.

## Точный синтаксис

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## Параметры

- `left` — Левое условие бинарной операции. AND/OR требуют Integer или Decimal: ноль ложен, любое ненулевое число истинно.
- `right` — Правое условие, для AND/OR тоже числовое. Вычисляются оба операнда: ложная левая часть AND или истинная левая часть OR не пропускает это выражение.
- `NOT / grouping` — Для NOT заключайте целиком инвертируемое условие в скобки. В сочетаниях AND, OR и XOR скобки явно задают группировку.

## Возвращает

Integer 1 (TRUE) или Integer 0 (FALSE). Это логические, а не побитовые операции: 2 AND 4 возвращает 1, а не битовую маску. Возвращённый флаг можно проверять через =TRUE или =1, =FALSE или =0.

## Поведение

- AND, OR и XOR имеют в этом движке один приоритет и выполняются слева направо: TRUE OR FALSE AND FALSE даёт 0. TRUE OR (FALSE AND FALSE) даёт 1. Учитывайте это правило совместимости при переносе кода VB.
- NOT(condition) вычисляет условие и меняет его истинность. В начале сравнения NOT 1=2 означает NOT(1=2). Если инвертированное значение должно быть операндом сравнения, пишите (NOT value) в скобках.
- AND/OR отвергают String, Array, Object и Unit. Совместимые NOT и XOR вместо этого проверяют равенство числовому нулю: текст "0", пустая строка, массивы, объекты и Unit считаются ненулевыми. Для них явно задавайте числовое условие; у CBool свои правила преобразования.
- Любое правое выражение выполняется, включая вызовы функций, ожидания и возникающие ошибки. Скобки меняют группировку, но не обязательность вычисления. Если позднее выражение должно запускаться только после успешного условия, используйте вложенные IF.

## Примеры

### 1. Объединить именованные флаги

```vb
# ready=TRUE, blocked=FALSE. NOT(blocked) даёт 1, поэтому canRun становится 1. ready XOR blocked истинно, поскольку истинен ровно один флаг. Main возвращает canRun*10+exclusive=11.
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**Разбор параметров и выполнения:**

ready=TRUE, blocked=FALSE. NOT(blocked) даёт 1, поэтому canRun становится 1. ready XOR blocked истинно, поскольку истинен ровно один флаг. Main возвращает canRun*10+exclusive=11.

### 2. Увидеть оба обязательных вызова

```vb
# Mark увеличивает параметр counter, переданный ByRef, и возвращает TRUE. Main начинает с counter=0. FALSE AND Mark(counter) всё равно вызывает Mark; TRUE OR Mark(counter) вызывает его ещё раз. Результаты условий — 0 и 1, а Main возвращает counter=2. Функция Mark приведена полностью.
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

**Разбор параметров и выполнения:**

Mark увеличивает параметр counter, переданный ByRef, и возвращает TRUE. Main начинает с counter=0. FALSE AND Mark(counter) всё равно вызывает Mark; TRUE OR Mark(counter) вызывает его ещё раз. Результаты условий — 0 и 1, а Main возвращает counter=2. Функция Mark приведена полностью.

### 3. Явно задать группировку

```vb
# legacy сначала вычисляет TRUE OR FALSE, затем AND FALSE и получает 0. grouped сначала вычисляет FALSE AND FALSE в скобках, затем OR с TRUE и получает 1. Main возвращает legacy*10+grouped=1.
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**Разбор параметров и выполнения:**

legacy сначала вычисляет TRUE OR FALSE, затем AND FALSE и получает 0. grouped сначала вычисляет FALSE AND FALSE в скобках, затем OR с TRUE и получает 1. Main возвращает legacy*10+grouped=1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
