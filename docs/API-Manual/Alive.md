# alive

ClassicUO • Runtime API • `alive.md`

## Точный синтаксис / Registered signatures

```text
alive -> String (runtime value)
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

Значение читается из состояния текущего runtime. Пример ниже показывает обращение к нему; для изменения используйте поддерживаемую команду Set, если параметр доступен для записи.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Значение фильтра, не вызов

```vb
SUB Main()
    # alive — строковый фильтр, поэтому круглые скобки не нужны.
    RETURN alive
END SUB
```

### Передать фильтр в поиск

```vb
SUB Main()
    # alive: состояние, near: расстояние, all: цвет и репутация, mob: класс.
    VAR stateFilter = alive
    RETURN UO.FindMobile(stateFilter, near, all, all, mob)
END SUB
```

### Вспомогательная функция с параметром

```vb
SUB Main()
    RETURN FilterText(alive)
END SUB

FUNCTION FilterText(stateFilter)
    # stateFilter — полученный строковый селектор, не состояние персонажа.
    RETURN CStr(stateFilter)
END FUNCTION
```
