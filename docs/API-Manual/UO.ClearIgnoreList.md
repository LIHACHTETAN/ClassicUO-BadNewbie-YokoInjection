# UO.ClearIgnoreList

ClassicUO • Runtime API • `UO.ClearIgnoreList.md`

## Точный синтаксис / Registered signatures

```text
UO.ClearIgnoreList() -> Unit
UO.ClearIgnoreList(list:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ClearIgnoreList`

### Manifest-registered overloads

- `UO.ClearIgnoreList() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.ClearIgnoreList(list:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- `list` — Named runtime value (String); use the exact registered/saved name expected by ClearIgnoreList.

### Accepted values / constants

- `list` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 0, 1. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.ClearIgnoreList()
END SUB
```

```basic
SUB Main()
    UO.ClearIgnoreList(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.ClearIgnoreList()
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # list
    UO.ClearIgnoreList(arg1)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.ClearIgnoreList()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.ClearIgnoreList()
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
