# UO.Cast

ClassicUO • Runtime API • `UO.Cast.md`

Отправляет запрос на применение заклинания/навыка. Строковая форма с одним аргументом возвращает 1 при принятии запроса клиентом и 0 при неизвестном имени или отказе. Это не подтверждение успешного эффекта на сервере. Форма с target сначала ставит цель в очередь, затем отправляет действие. Компактные формы с target=0/-1 ищут персонажа по фильтрам; явный serial используется напрямую. Последний флаг wait/waitTarget включает ожидание расходования очереди target до 1000 мс; при тайм-ауте возвращается 0 и очередь очищается. Флаг не является длительностью в миллисекундах.

## Точный синтаксис / Registered signatures

```text
UO.Cast(SpellID:Any) -> Any
UO.Cast(spell:Any, target:Any, distance:Any) -> Integer
UO.Cast(spell:Any, target:Any, distance:Any, notoriety:Any) -> Integer
UO.Cast(spell:Any, target:Any, distance:Any, notoriety:Any, nearest:Any) -> Integer
UO.Cast(spell:Any, target:Any, distance:Any, notoriety:Any, nearest:Any, maxZ:Any) -> Integer
UO.Cast(spell:Any, target:Any, distance:Any, notoriety:Any, nearest:Any, maxZ:Any, wait:Any) -> Integer
UO.Cast(spellName:Any, target:Any) -> Integer
UO.Cast(spellName:String) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Практический пример

```vb
SUB Main()
    VAR accepted = UO.Cast('Heal', self)
    UO.Print(CStr(accepted))
END SUB
```

### Расширенная перегрузка: 7 аргументов

```vb
SUB Main()
    VAR arg1 = 'Heal' # spell
    VAR arg2 = self # target
    VAR arg3 = 5 # distance
    VAR arg4 = -1 # notoriety
    VAR arg5 = 1 # nearest
    VAR arg6 = 6 # maxZ
    VAR arg7 = 7 # wait
    VAR result = UO.Cast(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.Cast('Heal', self)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.Cast('Heal', self, 5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.Cast('Heal', self, 5, -1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    VAR result = UO.Cast('Heal', self, 5, -1, 1)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 6 аргументов

```vb
SUB Main()
    VAR result = UO.Cast('Heal', self, 5, -1, 1, 6)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 'Heal' # spellName
    VAR result = UO.Cast(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 'Heal' # spellName
    VAR result = UO.Cast(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.<Register>b__40_25`
- `InjectionScript.Runtime.InjectionApiUO.Cast`
