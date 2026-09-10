# UO.ClientHide

ClassicUO • Runtime API • `UO.ClientHide.md`

Вызывает локальное скрытие указанного serial через клиентский bridge. Возвращает 1 после вызова, поэтому этот результат не доказывает, что объект существовал или был скрыт. Для интерактивного выбора используйте Hide().

## Точный синтаксис / Registered signatures

```text
UO.ClientHide(ObjID:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.ClientHide(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # ObjID
    VAR result = UO.ClientHide(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ObjID
    VAR result = UO.ClientHide(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
