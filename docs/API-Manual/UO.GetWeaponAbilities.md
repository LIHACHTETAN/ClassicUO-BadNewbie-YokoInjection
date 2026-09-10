# UO.GetWeaponAbilities

ClassicUO • Runtime API • `UO.GetWeaponAbilities.md`

Возвращает массив положительных ID способностей оружия текущего персонажа. Флаг активной способности удаляется из ID. Если персонажа/способностей нет, массив пустой.

## Точный синтаксис / Registered signatures

```text
UO.GetWeaponAbilities() -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Практический пример

```vb
SUB Main()
    VAR abilities = UO.GetWeaponAbilities()
    IF GetArrayLength(abilities) > 0 THEN
        UO.Print(CStr(abilities[0]))
    END IF
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.GetWeaponAbilities()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.GetWeaponAbilities()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.GetWeaponAbilities`
