# UO.GumpObject

ClassicUO • Runtime API • `UO.GumpObject.md`

## Точный синтаксис / Registered signatures

```text
UO.GumpObject(gumpId:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GumpObject`

### Manifest-registered overloads

- `UO.GumpObject(gumpId:Variant) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- `gumpId` — Numeric identifier (Variant). Use the ID domain documented by this command; 0 is a sentinel only when Behavior/Notes explicitly says so.

### Accepted values / constants

- `gumpId` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.GumpObject(0)
END SUB
```

```basic
SUB Main()
    UO.GumpObject(self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.GumpObject(0)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 0 # gumpId
        UO.GumpObject(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 0 # gumpId
    UO.GumpObject(arg1)
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
