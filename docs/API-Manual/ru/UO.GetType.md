# UO.GetType

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Читает числовой graphic предмета или body персонажа.

## Точный синтаксис

```text
UO.GetType(ObjID:Any) -> Any
```

## Параметры

- `ObjID` — Обязательный serial/ID игрового объекта либо строковый алиас "self", "backpack", "lasttarget" или имя AddObject. Это не graphic/type и не имя типа Basic. Чтобы прочитать себя, явно передайте "self"; формы без аргументов нет.

## Возвращает

Integer — graphic/type предмета либо body персонажа, например 0x0EED (3821) для золота. Значение 0 возвращается, если объект не найден. GetType не возвращает serial или текст "0x…"; строковую форму даёт GetGraphic.

## Поведение

- Команда читает локальные данные клиента. Она не посылает target и не меняет объект на сервере.
- Число 0 может быть допустимым значением данных. Отсутствие объекта проверяйте Exists(serial), а не только значением его свойства.

## Примеры

### Сравнить числовой type с константой

```vb
# Сравнить числовой type с константой
#
# Читает числовой graphic предмета или body персонажа.
#
# Integer — graphic/type предмета либо body персонажа, например 0x0EED (3821) для золота.
# Значение 0 возвращается, если объект не найден. GetType не возвращает serial или текст "0x…";
# строковую форму даёт GetGraphic.

SUB Main()
    # ObjID="lastobject" — алиас конкретного объекта.
    # 0x0EED является числом graphic; сравнение не ищет объект с таким serial.

    VAR graphic = UO.GetType('lastobject')
    IF graphic = 0x0EED THEN
        UO.Print('Gold graphic')
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- ObjID="lastobject" — алиас конкретного объекта.
- 0x0EED является числом graphic; сравнение не ищет объект с таким serial.

### Получить type собственного рюкзака

```vb
# Получить type собственного рюкзака
#
# Читает числовой graphic предмета или body персонажа.
#
# Integer — graphic/type предмета либо body персонажа, например 0x0EED (3821) для золота.
# Значение 0 возвращается, если объект не найден. GetType не возвращает serial или текст "0x…";
# строковую форму даёт GetGraphic.

SUB Main()
    # ObjID="backpack" — текущий рюкзак.
    # CStr форматирует возвращённое число для вывода.

    VAR graphic = UO.GetType('backpack')
    UO.Print('Backpack type: ' + CStr(graphic))
END SUB
```

**Разбор параметров и выполнения:**

- ObjID="backpack" — текущий рюкзак.
- CStr форматирует возвращённое число для вывода.

### Проверить существование объекта до чтения type

```vb
# Проверить существование объекта до чтения type
#
# Читает числовой graphic предмета или body персонажа.
#
# Integer — graphic/type предмета либо body персонажа, например 0x0EED (3821) для золота.
# Значение 0 возвращается, если объект не найден. GetType не возвращает serial или текст "0x…";
# строковую форму даёт GetGraphic.

SUB Main()
    # Пустая строка FindType проверяется до Exists.
    # Exists возвращает логическое 1/0; GetType возвращает номер graphic.

    VAR item = UO.FindType(0x0EED, -1, 'backpack')
    IF item <> '' THEN
        IF UO.Exists(item) THEN
            UO.Print('Type: ' + CStr(UO.GetType(item)))
        END IF
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- Пустая строка FindType проверяется до Exists.
- Exists возвращает логическое 1/0; GetType возвращает номер graphic.
