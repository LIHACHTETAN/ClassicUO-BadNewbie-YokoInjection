# UO.WaitGumpEntry

ClassicUO • Runtime API • `UO.WaitGumpEntry.md`

## Точный синтаксис / Registered signatures

```text
UO.WaitGumpEntry(index:Any, text:Any) -> Unit
UO.WaitGumpEntry(index:Any, text:Any, index2:Any, text2:Any) -> Unit
UO.WaitGumpEntry(index:Any, text:Any, index2:Any, text2:Any, index3:Any, text3:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.WaitGumpEntry`

### Manifest-registered overloads

- `UO.WaitGumpEntry(index:Integer, text:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitGumpEntry(index:Integer, text:String, index2:Integer, text2:Variant) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitGumpEntry(index:Integer, text:String, index2:Integer, text2:Variant, index3:Integer, text3:Variant) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- `index` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by this command.
- `text` — Text/String value (String); pass literal text as a quoted BASIC string.
- `index2` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by this command.
- `text2` — Variant value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.
- `index3` — Integer control/count/index value (Integer); exact zero/sentinel meaning is documented by this command.
- `text3` — Variant value with command-specific semantics. The accepted domain and any sentinel values are enumerated in the Accepted values / constants and Behavior sections below.

### Accepted values / constants

- `index` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `text` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `index2` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `text2` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.
- `index3` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `text3` — Variant. Only forms documented by this card and the in-client runtime Inspector are accepted.

### Defaults / omitted arguments

Registered arities: 2, 4, 6. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.WaitGumpEntry(0, 0)
END SUB
```

```basic
SUB Main()
    UO.WaitGumpEntry(0, 'example text', 0, 'example text', 0, 'example text')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.WaitGumpEntry(0, 'example')
END SUB
```

### Расширенная перегрузка: 6 аргументов

```vb
SUB Main()
    VAR arg1 = 0 # index
    VAR arg2 = 'example' # text
    VAR arg3 = 0 # index2
    VAR arg4 = 4 # text2
    VAR arg5 = 0 # index3
    VAR arg6 = 6 # text3
    UO.WaitGumpEntry(arg1, arg2, arg3, arg4, arg5, arg6)
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    UO.WaitGumpEntry(0, 'example', 0, 4)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 0 # index
        VAR arg2 = 'example' # text
        UO.WaitGumpEntry(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 0 # index
    VAR arg2 = 'example' # text
    UO.WaitGumpEntry(arg1, arg2)
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
