# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: uk -->

Str(value) форматує скалярне значення Basic як текст.

## Точний синтаксис

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## Параметри

- `value` — Один обов’язковий Integer, Decimal або String. Перевантаження обирається за фактичним видом значення. Для Array, Object та Unit перевантаження Str відсутнє.

## Повертає

String: числовий текст незалежно від мови або незмінений вхідний String. Перед додатним числом пробіл не додається. Параметра точності немає.

## Поведінка

- Функції виконуються локально без звернень до гри. Відсутній аргумент є помилкою. Характеристики читають UO.Int() та UO.Str(), а не Int()/Str(). Int використовує BasicDouble і Math.Floor; Str обирає InternalSubrutines.Str за видом аргументу та форматує незалежно від мови.

## Приклади

### Str — 1

```vb
# Str — 1
#
# Str(value) форматує скалярне значення Basic як текст.
#
# String: числовий текст незалежно від мови або незмінений вхідний String. Перед додатним числом
# пробіл не додається. Параметра точності немає.

SUB Main()
    # value=42 — Integer. Str повертає "42" без початкового пробілу; Main повертає цей String.

    RETURN Str(42)
END SUB
```

**Пояснення параметрів і виконання:**

- value=42 — Integer. Str повертає "42" без початкового пробілу; Main повертає цей String.

### Str — 2

```vb
# Str — 2
#
# Str(value) форматує скалярне значення Basic як текст.
#
# String: числовий текст незалежно від мови або незмінений вхідний String. Перед додатним числом
# пробіл не додається. Параметра точності немає.

SUB Main()
    # amount=-12.5 — Decimal. Str записує "-12.5" у text з крапкою за будь-якої мови. Main повертає
    # text, а amount залишається числом.

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**Пояснення параметрів і виконання:**

- amount=-12.5 — Decimal. Str записує "-12.5" у text з крапкою за будь-якої мови. Main повертає text, а amount залишається числом.

### Str — 3

```vb
# Str — 3
#
# Str(value) форматує скалярне значення Basic як текст.
#
# String: числовий текст незалежно від мови або незмінений вхідний String. Перед додатним числом
# пробіл не додається. Параметра точності немає.

SUB Main()
    # ItemLabel отримує name="ore", count=3. Str(name) зберігає ім’я, Str(count) дає "3". Функція
    # з’єднує рядки через " x"; Main повертає "ore x3".

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**Пояснення параметрів і виконання:**

- ItemLabel отримує name="ore", count=3. Str(name) зберігає ім’я, Str(count) дає "3". Функція з’єднує рядки через " x"; Main повертає "ore x3".
