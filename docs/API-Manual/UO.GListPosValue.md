# UO.GListPosValue

ClassicUO • Runtime API • `UO.GListPosValue.md`

Возвращает значение элемента GList по индексу от 0. Недоступный индекс возвращает 0.

## Точный синтаксис / Registered signatures

```text
UO.GListPosValue(index:Integer) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GListPosValue(0)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 0 # index
    VAR result = UO.GListPosValue(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 0 # index
    VAR result = UO.GListPosValue(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GListPosValue`
