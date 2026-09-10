# my

ClassicUO • Runtime API • `my.md`

## Точный синтаксис / Registered signatures

```text
my -> String (runtime value)
'my' — named object alias resolved from current client state
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

Значение читается из состояния текущего runtime. Пример ниже показывает обращение к нему; для изменения используйте поддерживаемую команду Set, если параметр доступен для записи.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Чтение значения

```vb
SUB Main()
    VAR value = 'my'
    UO.Print(CStr(value))
END SUB
```

### Использование в процедуре

```vb
SUB ShowValue()
    VAR value = 'my'
    UO.Print(CStr(value))
END SUB

SUB Main()
    ShowValue()
END SUB
```
