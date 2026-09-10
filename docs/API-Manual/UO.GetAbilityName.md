# UO.GetAbilityName

ClassicUO • Runtime API • `UO.GetAbilityName.md`

Возвращает имя способности оружия по ID, начиная с 1. Неизвестный ID возвращает пустую строку.

## Точный синтаксис / Registered signatures

```text
UO.GetAbilityName(abilityId:Integer) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetAbilityName(1)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = 1 # abilityId
    VAR result = UO.GetAbilityName(arg1)
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
    VAR arg1 = 1 # abilityId
    VAR result = UO.GetAbilityName(arg1)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GetAbilityName`
