# ShopBuyRestock

ClassicUO • Runtime API • `ShopBuyRestock.md`

## Точный синтаксис / Registered signatures

```text
ShopBuyRestock -> String (runtime value)
ShopBuyRestock = 26 (0x1A)
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

Значение читается из состояния текущего runtime. Пример ниже показывает обращение к нему; для изменения используйте поддерживаемую команду Set, если параметр доступен для записи.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Чтение значения

```vb
SUB Main()
    VAR value = ShopBuyRestock
    UO.Print(CStr(value))
END SUB
```

### Использование в процедуре

```vb
SUB ShowValue()
    VAR value = ShopBuyRestock
    UO.Print(CStr(value))
END SUB

SUB Main()
    ShowValue()
END SUB
```
