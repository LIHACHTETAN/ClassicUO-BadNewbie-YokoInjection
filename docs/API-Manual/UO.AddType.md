# UO.AddType

ClassicUO • Runtime API • `UO.AddType.md`

## Точный синтаксис / Registered signatures

```text
UO.AddType(name:Any) -> Unit
UO.AddType(name:Any, type:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.AddType`

### Manifest-registered overloads

- `UO.AddType(name:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.AddType(name:String, type:GraphicId) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- `name` — Named runtime value (String); use the exact registered/saved name expected by AddType.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.

### Accepted values / constants

- `name` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `type` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.

### Defaults / omitted arguments

Registered arities: 1, 2. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.AddType(0)
END SUB
```

```basic
SUB Main()
    UO.AddType('example', 0x0190)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.AddType('example')
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = 'example' # name
    VAR arg2 = 0x0EED # type
    UO.AddType(arg1, arg2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 'example' # name
        UO.AddType(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 'example' # name
    UO.AddType(arg1)
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
