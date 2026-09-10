# UO.Dye

ClassicUO • Runtime API • `UO.Dye.md`

## Точный синтаксис / Registered signatures

```text
UO.Dye(dyeObject:Any) -> Unit
UO.Dye(dyeObject:Any, target:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Dye`

### Manifest-registered overloads

- `UO.Dye(dyeObject:ObjectRef) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Dye(dyeObject:ObjectRef, target:ObjectRef) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- `dyeObject` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `target` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `dyeObject` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `target` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

Registered arities: 1, 2. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.Dye(0)
END SUB
```

```basic
SUB Main()
    UO.Dye(self, self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.Dye(1)
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # dyeObject
    VAR arg2 = self # target
    UO.Dye(arg1, arg2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 1 # dyeObject
        UO.Dye(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 1 # dyeObject
    UO.Dye(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass66_0.<RegisterLegacyManualAliases>b__1`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
