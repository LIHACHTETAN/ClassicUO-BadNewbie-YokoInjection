# UO.Target

ClassicUO • Runtime API • `UO.Target.md`

Разные перегрузки выполняют разные операции. Target() отменяет текущий/подготовленный target. Target(object) ставит объект в очередь, как WaitTargetObject. Target(targetKey,target) отправляет протокольный ответ с явным идентификатором прицела; target может быть serial, именованным объектом или строкой 'lasttile'. Семь аргументов задают targetKey, объект, targetType, graphic/type, x,y,z; targetType=0 — объект, 1 — клетка. Для обычного скрипта предпочтительны WaitTargetObject/WaitTargetTile: targetKey для низкоуровневой формы должен соответствовать серверному запросу.

## Точный синтаксис / Registered signatures

```text
UO.Target() -> Unit
UO.Target(object:Any) -> Unit
UO.Target(targetKey:Any, target:Any) -> Unit
UO.Target(targetKey:Any, target:Any, targetType:Any, type:Any, x:Any, y:Any, z:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Параметры

- `targetKey` — Идентификатор серверного запроса target. Это не serial выбранного объекта.
- `targetType` — Тип протокольной цели: 0 — объект, 1 — клетка.
- `target` — Serial/именованный объект; в двухаргументной форме допустим lasttile.
- `object` — Serial или имя загруженного объекта.
- `type` — Graphic ID, 0–65535.
- `x` — X игровой клетки.
- `y` — Y игровой клетки.
- `z` — Высота -128…127.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Отменить target

```vb
SUB Main()
    UO.Target()
END SUB
```

### Поставить свою цель в очередь

```vb
SUB Main()
    UO.Target(self)
END SUB
```

### Дать низкоуровневый ответ на текущий прицел

```vb
SUB Main()
    IF UO.WaitForTarget(3000) THEN
        UO.Target(UO.TargetID(), self)
    END IF
END SUB
```

### Расширенная перегрузка: 7 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # targetKey
    VAR arg2 = self # target
    VAR arg3 = 3 # targetType
    VAR arg4 = 0x0EED # type
    VAR arg5 = UO.GetX() # x
    VAR arg6 = UO.GetY() # y
    VAR arg7 = UO.GetZ() # z
    UO.Target(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
END SUB
```

### Перегрузка: 1 аргументов

```vb
SUB Main()
    UO.Target(self)
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    UO.Target(1, self)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.Target()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.Target()
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass66_0.<RegisterLegacyManualAliases>b__1`
- `InjectionScript.Runtime.InjectionApiUO.Target`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
