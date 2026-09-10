# UO.GetInfo

ClassicUO • Runtime API • `UO.GetInfo.md`

В текущей реализации принимает точную строку "character" и возвращает имя своего персонажа. Для любого другого значения возвращает строку "UNKNOWN". Это не команда окна Info и не универсальный запрос произвольного свойства.

## Точный синтаксис / Registered signatures

```text
UO.GetInfo(arg:String) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Практический пример

```vb
SUB Main()
    UO.Print(UO.GetInfo('character'))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = 'example' # arg
    VAR result = UO.GetInfo(arg1)
    IF len(result) > 0 THEN
        UO.Print(result)
    ELSE
        UO.Print('Empty')
    END IF
END SUB
```

### Поиск текста в результате

```vb
SUB Main()
    VAR arg1 = 'example' # arg
    VAR result = UO.GetInfo(arg1)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GetInfo`
