# UO.GetMobiles

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Возвращает ID загруженных персонажей, NPC и монстров по фильтрам.

## Точный синтаксис

```text
UO.GetMobiles() -> Any
UO.GetMobiles(distance:Any) -> Any
UO.GetMobiles(distance:Any, notoriety:Any) -> Any
UO.GetMobiles(distance:Any, notoriety:Any, body:Any) -> Any
UO.GetMobiles(distance:Any, notoriety:Any, body:Any, maxZ:Any) -> Any
UO.GetMobiles(distance:Any, notoriety:Any, body:Any, maxZ:Any, nearest:Any) -> Any
UO.GetMobiles(distance:Any, notoriety:Any, body:Any, maxZ:Any, nearest:Any, includeSelf:Any) -> Any
UO.GetMobiles(distance:Any, notoriety:Any, body:Any, maxZ:Any, nearest:Any, includeSelf:Any, aliveOnly:Any) -> Any
UO.GetMobiles(distance:Any, notoriety:Any, body:Any, maxZ:Any, nearest:Any, includeSelf:Any, aliveOnly:Any, visibleOnly:Any) -> Any
```

## Параметры

- `distance` — Радиус в клетках. По умолчанию/при отрицательном значении берётся FindDistance, 0 — только та же клетка.
- `notoriety` — Число, массив чисел или строка с разделителем |, например "3|4|5". -1/0xFFFF, пустая маска или any означают отсутствие ограничения. Маска только из ошибочного текста не совпадает ни с чем. Используется значение notoriety: 1 innocent, 2 ally, 3 gray, 4 criminal, 5 enemy, 6 murderer, 7 invulnerable; 0 — неизвестное состояние.
- `body` — Число, массив чисел или строка с разделителем |, например "3|4|5". -1/0xFFFF, пустая маска или any означают отсутствие ограничения. Маска только из ошибочного текста не совпадает ни с чем. Это graphic/body персонажа, например 0x0190 или 0x0191, не serial.
- `maxZ` — Максимальная абсолютная разность Z с self. По умолчанию/при отрицательном значении FindVertical; 0 требует одинаковую высоту.
- `nearest` — TRUE сортирует по расстоянию, затем по serial. По умолчанию FALSE.
- `includeSelf` — TRUE разрешает своего персонажа при выполнении остальных фильтров. По умолчанию FALSE.
- `aliveOnly` — TRUE исключает тех, для кого IsDead возвращает 1. По умолчанию FALSE. Это не сравнение HP с нулём.
- `visibleOnly` — TRUE требует IsVisible=1 по текущему состоянию клиента. По умолчанию FALSE. Это не проверка прямой видимости через стены CheckLOS.

## Возвращает

Array<Integer> — serial/ID Mobile, а не их body, имя или запись GetMobile. Нет совпадений — пустой Array. Даже форма без аргументов применяет FindDistance, FindVertical и Ignore и исключает self; это отличается от GetWorldItems() без аргументов.

## Поведение

- Читаются данные, уже загруженные клиентом. Команда не открывает контейнер, не перемещает предметы и не загружает объекты со всего сервера.
- Array — массив с индексами от 0. Сохраняйте его в VAR, проверяйте GetArrayLength перед доступом. Элементы могут исчезнуть из мира после создания снимка: перед действием проверяйте Exists(serial).
- Команда не меняет снимок FindItem/FindCount/GetFoundItems. Игнорируемые serial исключаются во всех формах. Сортировка включается только nearest=TRUE.
- Фильтры работают с данными клиента; отсутствие ID может означать выход из загруженной области, а не отсутствие персонажа на сервере.

## Примеры

### Список с текущими настройками поиска

```vb
# Список с текущими настройками поиска
#
# Возвращает ID загруженных персонажей, NPC и монстров по фильтрам.
#
# Array<Integer> — serial/ID Mobile, а не их body, имя или запись GetMobile. Нет совпадений —
# пустой Array. Даже форма без аргументов применяет FindDistance, FindVertical и Ignore и
# исключает self; это отличается от GetWorldItems() без аргументов.

SUB Main()
    # Параметров нет: используются FindDistance/FindVertical, без self.
    # Количество — число подходящих Mobile. Вещи и тайлы не включаются.

    VAR mobiles = UO.GetMobiles()
    UO.Print(STR(GetArrayLength(mobiles)))
END SUB
```

**Разбор параметров и выполнения:**

- Параметров нет: используются FindDistance/FindVertical, без self.
- Количество — число подходящих Mobile. Вещи и тайлы не включаются.

### Ближайший живой видимый противник

```vb
# Ближайший живой видимый противник
#
# Возвращает ID загруженных персонажей, NPC и монстров по фильтрам.
#
# Array<Integer> — serial/ID Mobile, а не их body, имя или запись GetMobile. Нет совпадений —
# пустой Array. Даже форма без аргументов применяет FindDistance, FindVertical и Ignore и
# исключает self; это отличается от GetWorldItems() без аргументов.

SUB Main()
    # distance=12; notoriety=3/4/5/6; любой body; перепад Z<=10; nearest=TRUE; self исключён;
    # aliveOnly и visibleOnly включены.
    # target — serial ближайшего совпадения. Пример не атакует и не делает вывод о проходимости
    # пути.

    VAR mobiles = UO.GetMobiles(12, '3|4|5|6', -1, 10, TRUE, FALSE, TRUE, TRUE)
    IF GetArrayLength(mobiles) > 0 THEN
        VAR target = mobiles[0]
        IF UO.Exists(target) THEN
            UO.Print(UO.GetName(target))
        END IF
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- distance=12; notoriety=3/4/5/6; любой body; перепад Z<=10; nearest=TRUE; self исключён; aliveOnly и visibleOnly включены.
- target — serial ближайшего совпадения. Пример не атакует и не делает вывод о проходимости пути.

### Люди двух body с включением себя

```vb
# Люди двух body с включением себя
#
# Возвращает ID загруженных персонажей, NPC и монстров по фильтрам.
#
# Array<Integer> — serial/ID Mobile, а не их body, имя или запись GetMobile. Нет совпадений —
# пустой Array. Даже форма без аргументов применяет FindDistance, FindVertical и Ignore и
# исключает self; это отличается от GetWorldItems() без аргументов.

SUB Main()
    # distance=20, любая notoriety, body=0x0190/0x0191, maxZ=20; сортировка выключена;
    # includeSelf=TRUE.
    # Неуказанные aliveOnly/visibleOnly равны FALSE. Это проверка body, которая не отличает
    # настоящего игрока от NPC с тем же body.

    VAR mobiles = UO.GetMobiles(20, -1, '0x0190|0x0191', 20, FALSE, TRUE)
    VAR i = 0
    WHILE i < GetArrayLength(mobiles)
        UO.Print('ID: 0x' + Hex(mobiles[i]))
        i = i + 1
    WEND
END SUB
```

**Разбор параметров и выполнения:**

- distance=20, любая notoriety, body=0x0190/0x0191, maxZ=20; сортировка выключена; includeSelf=TRUE.
- Неуказанные aliveOnly/visibleOnly равны FALSE. Это проверка body, которая не отличает настоящего игрока от NPC с тем же body.
