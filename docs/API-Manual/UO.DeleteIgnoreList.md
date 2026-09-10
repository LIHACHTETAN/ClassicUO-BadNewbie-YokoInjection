# UO.DeleteIgnoreList

ClassicUO • Runtime API • `UO.DeleteIgnoreList.md`

## Точный синтаксис / Registered signatures

```text
UO.DeleteIgnoreList(list:Any) -> Unit
UO.DeleteIgnoreList(list:Any, type:Any) -> Unit
UO.DeleteIgnoreList(list:Any, type:Any, color:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.DeleteIgnoreList`

### Manifest-registered overloads

- `UO.DeleteIgnoreList(list:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.DeleteIgnoreList(list:String, type:GraphicId) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.DeleteIgnoreList(list:String, type:GraphicId, color:Hue) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- `list` — Named runtime value (String); use the exact registered/saved name expected by DeleteIgnoreList.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Accepted values / constants

- `list` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `type` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.

### Defaults / omitted arguments

Registered arities: 1, 2, 3. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.DeleteIgnoreList(0)
END SUB
```

```basic
SUB Main()
    UO.DeleteIgnoreList(0, 0x0190, -1)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.DeleteIgnoreList(1)
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # list
    VAR arg2 = 0x0EED # type
    VAR arg3 = -1 # color
    UO.DeleteIgnoreList(arg1, arg2, arg3)
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    UO.DeleteIgnoreList(1, 0x0EED)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 1 # list
        UO.DeleteIgnoreList(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 1 # list
    UO.DeleteIgnoreList(arg1)
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
