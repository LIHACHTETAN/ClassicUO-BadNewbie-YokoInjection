# UO.SetGlobal

ClassicUO • Runtime API • `UO.SetGlobal.md`

## Точный синтаксис / Registered signatures

```text
UO.SetGlobal(GlobalRegion:Any, VarName:Any, VarValue:Any) -> Unit
UO.SetGlobal(name:String, value:Decimal) -> Unit
UO.SetGlobal(name:String, value:Integer) -> Unit
UO.SetGlobal(name:String, value:String) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetGlobal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Устанавливает значение глобальной переменной в указанной области видимости. GlobalRegion — область видимости переменной: 'stealth' для глобальных переменных Stealth (общих для всех персонажей и скриптов), или 'char' для переменных конкретного персонажа. VarName — имя переменной (регистронезависимое). VarValue — строковое значение для сохранения. Глобальные переменные сохраняются в течение сессии Stealth и считываются через GetGlobal . Обычно используются для межскриптового обмена данными: один скрипт устанавливает значение, другой читает. В Python параметр GlobalRegion — это int (не строка): используйте соответствующую константу.

### Current Basic signatures / Return

- `UO.SetGlobal(GlobalRegion:Integer, VarName:String, VarValue:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetGlobal"]` → `STATE -> InjectionApiState.GlobalVariables`

**Pascal compatibility signature:** `procedure SetGlobal(GlobalRegion: String; VarName: String; VarValue: String);`

### Additional current runtime overloads

- `UO.SetGlobal(name:String, value:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetGlobal(name:String, value:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetGlobal(name:String, value:Decimal) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `GlobalRegion` — Global scope selector: 0/'stealth' for runtime-wide globals, 1/'char' for current-character globals.
- `VarName` — Named runtime value (String); use the exact registered/saved name expected by SetGlobal.
- `VarValue` — String value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.
- `name` — Named runtime value (String); use the exact registered/saved name expected by SetGlobal.
- `value` — Decimal / Integer / String value. The concrete accepted domain is command-specific and is stated in Behavior/Notes; do not assume String conversion when the overload is numeric.

### Accepted values / constants

- `GlobalRegion` — Global scope selector: 0/'stealth' for runtime-wide globals, 1/'char' for current-character globals.
- `VarName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `VarValue` — String value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.
- `name` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `value` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 2, 3. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetGlobal(0, 'example', 'example')
END SUB
```

```basic
SUB Main()
    UO.SetGlobal(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetGlobal('example', 'example')
END SUB
```

### Расширенная перегрузка: 3 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # GlobalRegion
    VAR arg2 = 2 # VarName
    VAR arg3 = 3 # VarValue
    UO.SetGlobal(arg1, arg2, arg3)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 'example' # name
        VAR arg2 = 'example' # value
        UO.SetGlobal(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 'example' # name
    VAR arg2 = 'example' # value
    UO.SetGlobal(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.State.Globals.SetGlobal`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
