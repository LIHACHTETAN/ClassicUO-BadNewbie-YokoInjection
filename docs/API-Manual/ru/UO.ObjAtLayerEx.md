# UO.ObjAtLayerEx

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Находит предмет на числовом слое экипировки заданного mobile.

## Точный синтаксис

```text
UO.ObjAtLayerEx(LayerType:Any, PlayerID:Any) -> Integer
```

## Параметры

- `LayerType` — Обязательный номер слоя 1..29. Числа 0 и вне диапазона возвращают 0. Здесь нужен номер, а не строковое имя Rhand; для правой руки передайте 1.
- `PlayerID` — Обязательный serial/ID конкретного объекта: Integer, hex-строка либо алиас self, backpack, lasttarget, lastobject, lastcontainer, laststatus, finditem, lastcorpse или имя AddObject. Это не graphic/type. Неустановленное имя разрешается в 0; никакой новый target команда не открывает. Объект должен быть mobile; для собственного персонажа передайте self.

## Возвращает

Integer — serial предмета на указанном слое указанного mobile. Integer 0 — слой недопустим или пуст, mobile неизвестен/удалён либо его экипировка ещё не получена. Это не номер слоя и не признак наличия предмета только в значениях 1/0: при успехе возвращается полный ID.

## Поведение

- Читается локальная модель клиента; запросов серверу, ожидания и перемещения нет.
- Результат относится к моменту чтения. После WAIT или другого действия объект и его флаги могут измениться.
- Читается уже известная экипировка выбранного mobile. Закрытые банковские/торговые контейнеры могут быть неизвестны; команда не запрашивает их открытие.
- Номера слоёв совпадают с ObjAtLayer. Строковые имена из этого списка относятся к форме ObjAtLayer(name), а здесь используйте соответствующие числа:
- 1 OneHanded/Rhand/RightHand; 2 TwoHanded/Lhand/LeftHand; 3 Shoes; 4 Pants; 5 Shirt; 6 Helmet/Hat; 7 Gloves; 8 Ring; 9 Talisman; 10 Necklace/Neck.
- 11 Hair; 12 Waist; 13 Torso; 14 Bracelet/Brace; 15 Face; 16 Beard; 17 Tunic; 18 Earrings/Ear; 19 Arms; 20 Cloak.
- 21 Backpack/Bpack/BackpackLayer; 22 Robe; 23 Skirt; 24 Legs; 25 Mount; 26 ShopBuyRestock/Rstk; 27 ShopBuy/NRstk; 28 ShopSell/Sell; 29 Bank.

## Примеры

### Проверить свою правую руку

```vb
# Проверить свою правую руку
#
# Находит предмет на числовом слое экипировки заданного mobile.
#
# Integer — serial предмета на указанном слое указанного mobile. Integer 0 — слой недопустим или
# пуст, mobile неизвестен/удалён либо его экипировка ещё не получена. Это не номер слоя и не
# признак наличия предмета только в значениях 1/0: при успехе возвращается полный ID.

SUB Main()
    # LayerType=1 — OneHanded; PlayerID=self — собственный персонаж.
    # В отличие от ObjAtLayer("Rhand"), эта форма возвращает числовой serial.

    VAR item = UO.ObjAtLayerEx(1, 'self')
    IF item <> 0 THEN
        UO.Print('Equipped item serial: ' + STR(item))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- LayerType=1 — OneHanded; PlayerID=self — собственный персонаж.
- В отличие от ObjAtLayer("Rhand"), эта форма возвращает числовой serial.

### Читать оружие выбранного mobile

```vb
# Читать оружие выбранного mobile
#
# Находит предмет на числовом слое экипировки заданного mobile.
#
# Integer — serial предмета на указанном слое указанного mobile. Integer 0 — слой недопустим или
# пуст, mobile неизвестен/удалён либо его экипировка ещё не получена. Это не номер слоя и не
# признак наличия предмета только в значениях 1/0: при успехе возвращается полный ID.

SUB Main()
    # Обе команды получают один сохранённый serial target. 1 и 2 — разные слои экипировки.
    # 0 может означать отсутствие предмета или ещё неизвестную экипировку; это не запрос серверу на
    # полный осмотр.

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR right = UO.ObjAtLayerEx(1, target)
        VAR left = UO.ObjAtLayerEx(2, target)
        UO.Print('Right layer: ' + STR(right))
        UO.Print('Left layer: ' + STR(left))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- Обе команды получают один сохранённый serial target. 1 и 2 — разные слои экипировки.
- 0 может означать отсутствие предмета или ещё неизвестную экипировку; это не запрос серверу на полный осмотр.

### Не путать надетую вещь с содержимым сумки

```vb
# Не путать надетую вещь с содержимым сумки
#
# Находит предмет на числовом слое экипировки заданного mobile.
#
# Integer — serial предмета на указанном слое указанного mobile. Integer 0 — слой недопустим или
# пуст, mobile неизвестен/удалён либо его экипировка ещё не получена. Это не номер слоя и не
# признак наличия предмета только в значениях 1/0: при успехе возвращается полный ID.

SUB Main()
    # ObjAtLayerEx возвращает только serial рюкзака на слое 21.
    # Поиск золота выполняется отдельным FindType. Возвращаемый bag не является количеством
    # предметов в рюкзаке.

    VAR bag = UO.ObjAtLayerEx(21, 'self')
    IF bag <> 0 THEN
        VAR gold = UO.FindType(0x0EED, -1, bag)
        UO.Print('Backpack serial: ' + STR(bag))
        UO.Print('Known gold item: ' + gold)
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- ObjAtLayerEx возвращает только serial рюкзака на слое 21.
- Поиск золота выполняется отдельным FindType. Возвращаемый bag не является количеством предметов в рюкзаке.
