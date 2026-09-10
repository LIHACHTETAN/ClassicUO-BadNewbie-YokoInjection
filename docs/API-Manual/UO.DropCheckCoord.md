# UO.DropCheckCoord

ClassicUO • Runtime API • `UO.DropCheckCoord.md`

## Точный синтаксис / Registered signatures

```text
UO.DropCheckCoord() -> Any
UO.DropCheckCoord(value:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.DropCheckCoord`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Управляет проверкой координат назначения перед сбросом предмета. Когда True , система проверяет допустимость координат назначения перед выполнением сброса. Когда False , координаты отправляются без проверки. В Python используйте GetDropCheckCoord() / SetDropCheckCoord(value) .

### Current Basic signatures / Return

- `UO.DropCheckCoord() -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropCheckCoord"]` → `STATE -> InjectionApiState.DropCheckCoord`
- `UO.DropCheckCoord(value:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["DropCheckCoord"]` → `STATE -> InjectionApiState.DropCheckCoord`

**Pascal compatibility signature:** `var DropCheckCoord: Boolean;`

### Parameters

- `value` — Boolean drop-coordinate validation flag: TRUE/1 enables coordinate checks; FALSE/0 sends the requested coordinates without that validation.

### Accepted values / constants

- `value` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

Registered arities: 0, 1. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.DropCheckCoord()
END SUB
```

```basic
SUB Main()
    UO.DropCheckCoord(TRUE)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.DropCheckCoord()
    UO.Print(CStr(result))
END SUB
```

### Расширенная перегрузка: 1 аргументов

```vb
SUB Main()
    VAR arg1 = 1 # value
    VAR result = UO.DropCheckCoord(arg1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR result = UO.DropCheckCoord()
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR result = UO.DropCheckCoord()
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
