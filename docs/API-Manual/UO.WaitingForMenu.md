# UO.WaitingForMenu

ClassicUO • Runtime API • `UO.WaitingForMenu.md`

## Точный синтаксис / Registered signatures

```text
UO.WaitingForMenu(delay:Any) -> Integer
UO.WaitingForMenu(delay:Any, menuCount:Any) -> Integer
UO.WaitingForMenu(delay:Any, menuCount:Any, blockMenu:Any) -> Integer
UO.WaitingForMenu(delay:Any, menuCount:Any, blockMenu:Any, menuName:Any) -> Integer
UO.WaitingForMenu(delayValue:Any, menuCountValue:Any, blockMenuValue:Any, menuNameValue:Any, skillOrSerial:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.WaitingForMenu`

### Direct runtime overloads

- `UO.WaitingForMenu(maxDelay:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean contract: 1 means success/condition satisfied; 0 means failure, timeout, clear-state, or no matching object/menu as described by Behavior.
- `UO.WaitingForMenu(maxDelay:Integer, menuCount:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean contract: 1 means success/condition satisfied; 0 means failure, timeout, clear-state, or no matching object/menu as described by Behavior.
- `UO.WaitingForMenu(maxDelay:Integer, menuCount:Integer, blockMenu:Boolean) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean contract: 1 means success/condition satisfied; 0 means failure, timeout, clear-state, or no matching object/menu as described by Behavior.
- `UO.WaitingForMenu(maxDelay:Integer, menuCount:Integer, blockMenu:Boolean, menuName:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean contract: 1 means success/condition satisfied; 0 means failure, timeout, clear-state, or no matching object/menu as described by Behavior.
- `UO.WaitingForMenu(maxDelay:Integer, menuCount:Integer, blockMenu:Boolean, menuName:String, skillOrSerial:SkillName|ObjectRef) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean contract: 1 means success/condition satisfied; 0 means failure, timeout, clear-state, or no matching object/menu as described by Behavior.

### Parameters

- `skillOrSerial` — Optional trigger before waiting: skill name String, object serial/reference, or 0/empty to perform no trigger.
- `maxDelay` — Maximum wait in milliseconds. 0 performs an immediate check; negative values are normalized by the runtime to a non-negative wait.
- `menuCount` — Ordinal menu occurrence to accept. Values <= 1 select the first matching occurrence; larger values wait for that many distinct menu appearances.
- `blockMenu` — Menu blocking flag: FALSE/0 lets the server menu remain visible; TRUE/1 sends the server cancel/right-click response and closes the matched menu locally.
- `menuName` — Exact case-sensitive server menu caption. Empty string accepts any menu caption.

### Accepted values / constants

- `maxDelay` — Maximum wait in milliseconds. 0 performs an immediate check; negative values are normalized by the runtime to a non-negative wait.
- `menuCount` — Ordinal menu occurrence to accept. Values <= 1 select the first matching occurrence; larger values wait for that many distinct menu appearances.
- `blockMenu` — Menu blocking flag: FALSE/0 lets the server menu remain visible; TRUE/1 sends the server cancel/right-click response and closes the matched menu locally.
- `menuName` — Exact case-sensitive server menu caption. Empty string accepts any menu caption.
- `skillOrSerial` — Optional trigger before waiting: skill name String, object serial/reference, or 0/empty to perform no trigger.

### Defaults / omitted arguments

Omitted trailing parameters use: menuCount=1 effective first occurrence, blockMenu=FALSE, menuName='' (any caption), skillOrSerial=0 (no trigger).

### Behavior

Waits for a server menu and returns 1 only when the requested occurrence/name is satisfied. menuCount selects the ordinal distinct menu appearance; menuName is matched case-sensitively. blockMenu=TRUE sends the menu cancel/right-click response and closes the matched menu. skillOrSerial optionally uses a skill or object before the wait starts.
### Notes / limitations

A timeout or unmatched menu returns 0. Empty menuName accepts any caption. The menu identity is tracked so one unchanged open menu is not counted repeatedly. Blocking is a real server-menu cancel action, not only a local visual hide.
### Examples

```basic
SUB Main()
    VAR ok = UO.WaitingForMenu(3000, 1, FALSE, 'Bank')
END SUB
```

```basic
SUB Main()
    VAR ok = UO.WaitingForMenu(5000, 1, TRUE, 'Choose item', 'Blacksmithy')
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.WaitingForMenu(100)
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 5 аргументов

```vb
SUB Main()
    VAR arg1 = 100 # delayValue
    VAR arg2 = 2 # menuCountValue
    VAR arg3 = 3 # blockMenuValue
    VAR arg4 = 4 # menuNameValue
    VAR arg5 = 'Hiding' # skillOrSerial
    VAR result = UO.WaitingForMenu(arg1, arg2, arg3, arg4, arg5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    VAR result = UO.WaitingForMenu(100, 2)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.WaitingForMenu(100, 2, 3)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.WaitingForMenu(100, 2, 3, 4)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 100 # delay
    VAR result = UO.WaitingForMenu(arg1)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 100 # delay
    VAR result = UO.WaitingForMenu(arg1)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.WaitingForMenu`
