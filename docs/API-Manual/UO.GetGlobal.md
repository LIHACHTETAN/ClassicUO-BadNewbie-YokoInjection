# UO.GetGlobal

ClassicUO • Runtime API • `UO.GetGlobal.md`

## Точный синтаксис / Registered signatures

```text
UO.GetGlobal(GlobalRegion:Any, VarName:Any) -> Any
UO.GetGlobal(name:String) -> String
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetGlobal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает значение глобальной переменной VarName из указанного GlobalRegion . В Pascal GlobalRegion — строка: 'stealth' (видна всем персонажам) или 'char' (видна только скриптам текущего персонажа). Регистронезависимо. В Python GlobalRegion принимает enum Global : Global.Stealth (0) или Global.Char (1).

### Current Basic signatures / Return

- `UO.GetGlobal(GlobalRegion:Integer, VarName:String) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetGlobal"]` → `STATE -> InjectionApiState.GlobalVariables`

**Pascal compatibility signature:** `function GetGlobal(GlobalRegion: String; VarName: String): String;`

### Additional current runtime overloads

- `UO.GetGlobal(name:String) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `GlobalRegion` — Global scope selector: 0/'stealth' for runtime-wide globals, 1/'char' for current-character globals.
- `VarName` — Named runtime value (String); use the exact registered/saved name expected by GetGlobal.
- `name` — Named runtime value (String); use the exact registered/saved name expected by GetGlobal.

### Accepted values / constants

- `GlobalRegion` — Global scope selector: 0/'stealth' for runtime-wide globals, 1/'char' for current-character globals.
- `VarName` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `name` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 1, 2. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.GetGlobal(0, 'example')
END SUB
```

```basic
SUB Main()
    VAR result = UO.GetGlobal(0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetGlobal('example')
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # GlobalRegion
    VAR arg2 = 2 # VarName
    VAR result = UO.GetGlobal(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Обработка пустого текста

```vb
SUB Main()
    VAR arg1 = 'example' # name
    VAR result = UO.GetGlobal(arg1)
    IF len(result) > 0 THEN
        UO.Print(result)
    ELSE
        UO.Print('Empty')
    END IF
END SUB
```

### Поиск текста в результате

```vb
SUB Main()
    VAR arg1 = 'example' # name
    VAR result = UO.GetGlobal(arg1)
    IF contains(LCase(result), 'example') THEN
        UO.Print('Match')
    END IF
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.State.Globals.GetGlobal`
