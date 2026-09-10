# UO.EUO2Inj

ClassicUO • Runtime API • `UO.EUO2Inj.md`

Преобразует буквенную запись serial EasyUO (основание 26, A=0) в hex-строку Injection. Буквы нечувствительны к регистру; небуквенные символы пропускаются. Обратная функция — Inj2EUO.

## Точный синтаксис / Registered signatures

```text
UO.EUO2Inj(easyValue:Any) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.EUO2Inj(1)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = 1 # easyValue
    VAR result = UO.EUO2Inj(arg1)
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
    VAR arg1 = 1 # easyValue
    VAR result = UO.EUO2Inj(arg1)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.EUO2Inj`
