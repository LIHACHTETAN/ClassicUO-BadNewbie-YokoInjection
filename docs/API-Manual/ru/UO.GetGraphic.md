# UO.GetGraphic

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Читает graphic предмета или body персонажа и возвращает его в шестнадцатеричном тексте.

## Точный синтаксис

```text
UO.GetGraphic() -> String
UO.GetGraphic(id:Integer) -> String
UO.GetGraphic(id:String) -> String
```

## Параметры

- `id` — Serial конкретного объекта либо разрешаемый алиас, например "self", "backpack", "lasttarget" или имя, сохранённое AddObject. Graphic/type сюда не передаётся. В форме без аргументов используется self.

## Возвращает

String вида "0x0EED" — графический type/body объекта. Это не уникальный ID/serial. Для неизвестного объекта bridge возвращает graphic 0, который форматируется как "0x0000". Команда не возвращает true/false.

## Поведение

- Команда читает локальные данные клиента. Она не посылает target и не меняет объект на сервере.
- Число 0 может быть допустимым значением данных. Отсутствие объекта проверяйте Exists(serial), а не только значением его свойства.

## Примеры

### Проверить type найденного предмета

```vb
# Проверить type найденного предмета
#
# Читает graphic предмета или body персонажа и возвращает его в шестнадцатеричном тексте.
#
# String вида "0x0EED" — графический type/body объекта. Это не уникальный ID/serial. Для
# неизвестного объекта bridge возвращает graphic 0, который форматируется как "0x0000". Команда
# не возвращает true/false.

SUB Main()
    # FindType получает type золота и возвращает serial.
    # GetGraphic(serial) возвращает текст "0x0EED"; переменные item и graphic имеют разный смысл.

    VAR item = UO.FindType(0x0EED, -1, 'backpack')
    IF item <> '' THEN
        VAR graphic = UO.GetGraphic(item)
        UO.Print('Graphic: ' + graphic)
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- FindType получает type золота и возвращает serial.
- GetGraphic(serial) возвращает текст "0x0EED"; переменные item и graphic имеют разный смысл.

### Прочитать body своего персонажа

```vb
# Прочитать body своего персонажа
#
# Читает graphic предмета или body персонажа и возвращает его в шестнадцатеричном тексте.
#
# String вида "0x0EED" — графический type/body объекта. Это не уникальный ID/serial. Для
# неизвестного объекта bridge возвращает graphic 0, который форматируется как "0x0000". Команда
# не возвращает true/false.

SUB Main()
    # Форма без аргумента использует self.
    # body — код внешнего вида персонажа, а не его serial.

    VAR body = UO.GetGraphic()
    UO.Print('Body graphic: ' + body)
END SUB
```

**Разбор параметров и выполнения:**

- Форма без аргумента использует self.
- body — код внешнего вида персонажа, а не его serial.

### Передать прочитанный graphic в новый поиск

```vb
# Передать прочитанный graphic в новый поиск
#
# Читает graphic предмета или body персонажа и возвращает его в шестнадцатеричном тексте.
#
# String вида "0x0EED" — графический type/body объекта. Это не уникальный ID/serial. Для
# неизвестного объекта bridge возвращает graphic 0, который форматируется как "0x0000". Команда
# не возвращает true/false.

SUB Main()
    # lastobject — образец; graphic — строка hex, которую FindType принимает как type.
    # -1 допускает любой цвет, backpack задаёт область поиска. sameType снова является serial.

    VAR graphic = UO.GetGraphic('lastobject')
    VAR sameType = UO.FindType(graphic, -1, 'backpack')
    IF sameType <> '' THEN
        UO.Print('Matching serial: ' + sameType)
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- lastobject — образец; graphic — строка hex, которую FindType принимает как type.
- -1 допускает любой цвет, backpack задаёт область поиска. sameType снова является serial.
