# UO.Inj2EUO

ClassicUO • Runtime API • `UO.Inj2EUO.md`

Преобразует 32-битный serial в буквенную запись с основанием 26 (A=0). Serial=0 даёт "A". Обратная функция — EUO2Inj.

## Точный синтаксис / Registered signatures

```text
UO.Inj2EUO(serialValue:Any) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.Inj2EUO(1)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = 1 # serialValue
    VAR result = UO.Inj2EUO(arg1)
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
    VAR arg1 = 1 # serialValue
    VAR result = UO.Inj2EUO(arg1)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.Inj2EUO`
