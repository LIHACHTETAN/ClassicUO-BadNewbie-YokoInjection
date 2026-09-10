# UO.TradeName

ClassicUO • Runtime API • `UO.TradeName.md`

Возвращает имя другой стороны из активного окна обмена по индексу окна от 0. Это данные клиентского окна, а не поиск персонажа по миру.

## Точный синтаксис / Registered signatures

```text
UO.TradeName(windowIndex:Any) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.TradeName(0)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = 0 # windowIndex
    VAR result = UO.TradeName(arg1)
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
    VAR arg1 = 0 # windowIndex
    VAR result = UO.TradeName(arg1)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.TradeName`
