# UO.GetMultiAllParts

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ru -->

Читает записи компонент одного дома.

## Точный синтаксис

```text
UO.GetMultiAllParts(MultiID:Any) -> Any
```

## Параметры

- `MultiID` — Serial/ID конкретного объекта: Integer, десятичная/hex-строка или установленный алиас self, backpack, lasttarget, lastobject либо имя AddObject. Это не graphic/type. Должен быть ID загруженного дома в HouseManager.

## Возвращает

Array<Array<Integer>>. Каждая строка содержит 9 полей: [0] graphic/type компоненты, [1] hue, [2] мировой X, [3] мировой Y, [4] мировой Z, [5] multiOffsetX — смещение X от multi, [6] multiOffsetY — смещение Y, [7] multiOffsetZ — смещение Z, [8] multiSerial — serial дома. Нет компонент — пустой Array. Graphic не является ID; у отдельных статических компонент здесь нет собственного serial.

## Поведение

- Читаются данные, уже загруженные клиентом. Команда не открывает контейнер, не перемещает предметы и не загружает объекты со всего сервера.
- Array — массив с индексами от 0. Сохраняйте его в VAR, проверяйте GetArrayLength перед доступом. Элементы могут исчезнуть из мира после создания снимка: перед действием проверяйте Exists(serial).
- Возвращаются известные, не удалённые компоненты HouseManager. Отдельная статика карты и land в этот список не входят. Строки являются снимком; фиксированный порядок или сортировка по Z не обещаются.

## Примеры

### Посчитать компоненты

```vb
# Посчитать компоненты
#
# Читает записи компонент одного дома.
#
# Array<Array<Integer>>. Каждая строка содержит 9 полей: [0] graphic/type компоненты, [1] hue,
# [2] мировой X, [3] мировой Y, [4] мировой Z, [5] multiOffsetX — смещение X от multi, [6]
# multiOffsetY — смещение Y, [7] multiOffsetZ — смещение Z, [8] multiSerial — serial дома. Нет
# компонент — пустой Array. Graphic не является ID; у отдельных статических компонент здесь нет
# собственного serial.

SUB Main()
    # Сначала выбирается загруженный дом.
    # Длина — число компонент, не их высота и не число домов.

    VAR houses = UO.GetMultis()
    IF GetArrayLength(houses) = 0 THEN
        RETURN
    END IF
    VAR parts = UO.GetMultiAllParts(houses[0])
    UO.Print(STR(GetArrayLength(parts)))
END SUB
```

**Разбор параметров и выполнения:**

- Сначала выбирается загруженный дом.
- Длина — число компонент, не их высота и не число домов.

### Прочитать graphic и положение первой компоненты

```vb
# Прочитать graphic и положение первой компоненты
#
# Читает записи компонент одного дома.
#
# Array<Array<Integer>>. Каждая строка содержит 9 полей: [0] graphic/type компоненты, [1] hue,
# [2] мировой X, [3] мировой Y, [4] мировой Z, [5] multiOffsetX — смещение X от multi, [6]
# multiOffsetY — смещение Y, [7] multiOffsetZ — смещение Z, [8] multiSerial — serial дома. Нет
# компонент — пустой Array. Graphic не является ID; у отдельных статических компонент здесь нет
# собственного serial.

SUB Main()
    # parts[0] — первая строка массива. Её [0] — type, [2]/[3]/[4] — мировые X/Y/Z.
    # Индексы [5]/[6]/[7] вместо этого содержат относительные смещения.

    VAR houses = UO.GetMultis()
    IF GetArrayLength(houses) = 0 THEN
        RETURN
    END IF
    VAR parts = UO.GetMultiAllParts(houses[0])
    IF GetArrayLength(parts) > 0 THEN
        VAR part = parts[0]
        UO.Print('Type: 0x' + Hex(part[0]))
        UO.Print(STR(part[2]) + ',' + STR(part[3]) + ',' + STR(part[4]))
    END IF
END SUB
```

**Разбор параметров и выполнения:**

- parts[0] — первая строка массива. Её [0] — type, [2]/[3]/[4] — мировые X/Y/Z.
- Индексы [5]/[6]/[7] вместо этого содержат относительные смещения.

### Обойти компоненты и вывести владельцев

```vb
# Обойти компоненты и вывести владельцев
#
# Читает записи компонент одного дома.
#
# Array<Array<Integer>>. Каждая строка содержит 9 полей: [0] graphic/type компоненты, [1] hue,
# [2] мировой X, [3] мировой Y, [4] мировой Z, [5] multiOffsetX — смещение X от multi, [6]
# multiOffsetY — смещение Y, [7] multiOffsetZ — смещение Z, [8] multiSerial — serial дома. Нет
# компонент — пустой Array. Graphic не является ID; у отдельных статических компонент здесь нет
# собственного serial.

SUB Main()
    # [8] — serial дома, [7] — смещение Z компоненты.
    # Не передавайте part[0] в команду, ожидающую serial дома: это graphic отдельной компоненты.

    VAR houses = UO.GetMultis()
    IF GetArrayLength(houses) = 0 THEN
        RETURN
    END IF
    VAR parts = UO.GetMultiAllParts(houses[0])
    VAR i = 0
    WHILE i < GetArrayLength(parts)
        VAR part = parts[i]
        UO.Print('Multi: 0x' + Hex(part[8]) + ', offset Z: ' + STR(part[7]))
        i = i + 1
    WEND
END SUB
```

**Разбор параметров и выполнения:**

- [8] — serial дома, [7] — смещение Z компоненты.
- Не передавайте part[0] в команду, ожидающую serial дома: это graphic отдельной компоненты.
