# UO.WaitMenu

ClassicUO • Runtime API • `UO.WaitMenu.md`

## Точный синтаксис / Registered signatures

```text
UO.WaitMenu(MenuCaption:Any, ElementCaption:Any) -> Unit
UO.WaitMenu(prompt1:String, choice1:String, prompt2:String, choice2:String) -> Unit
UO.WaitMenu(prompt1:String, choice1:String, prompt2:String, choice2:String, prompt3:String, choice3:String) -> Unit
UO.WaitMenu(prompt:String, choice:String) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.WaitMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Предустанавливает одноразовый автоматический ответ на меню: при появлении меню с совпадающим заголовком автоматически выбирается указанный пункт, после чего ловушка снимается. MenuCaption — подстрока для поиска в заголовке меню. ElementCaption — подстрока для поиска в нужном пункте меню. Устанавливает одноразовую ловушку через менеджер меню. Когда сервер отправляет меню, заголовок которого содержит MenuCaption и в котором есть пункт, содержащий ElementCaption , этот пункт автоматически выбирается и ловушка удаляется. Можно установить несколько различных ловушек подряд, вызвав WaitMenu несколько раз с разными парами caption/element перед действием, вызывающим меню. Каждая ловушка срабатывает однократно для своего совпадающего меню. Для постоянной (многоразовой) ловушки, срабатывающей каждый раз при появлении подходящего меню, используйте AutoMenu . Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.WaitMenu(MenuCaption:String, ElementCaption:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitMenu"]` → `BRIDGE CONTRACT -> IApiBridge.WaitMenu`

**Pascal compatibility signature:** `procedure WaitMenu(MenuCaption: String; ElementCaption: String);`

### Additional current runtime overloads

- `UO.WaitMenu(prompt1:String, choice1:String, prompt2:String, choice2:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitMenu(prompt1:String, choice1:String, prompt2:String, choice2:String, prompt3:String, choice3:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `MenuCaption` — Named runtime value (runtime value); use the exact registered/saved name expected by WaitMenu.
- `ElementCaption` — Named runtime value (runtime value); use the exact registered/saved name expected by WaitMenu.
- `prompt1` — Text/String value (String); pass literal text as a quoted BASIC string.
- `choice1` — Text/String value (String); pass literal text as a quoted BASIC string.
- `prompt2` — Text/String value (String); pass literal text as a quoted BASIC string.
- `choice2` — Text/String value (String); pass literal text as a quoted BASIC string.
- `prompt3` — Text/String value (String); pass literal text as a quoted BASIC string.
- `choice3` — Text/String value (String); pass literal text as a quoted BASIC string.

### Accepted values / constants

- `MenuCaption` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `ElementCaption` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `prompt1` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `choice1` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `prompt2` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `choice2` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `prompt3` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `choice3` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 2, 4, 6. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or updates the current client UI/Gump state through the registered Basic/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.WaitMenu(0, 0)
END SUB
```

```basic
SUB Main()
    UO.WaitMenu(0, 0, 0, 0)
END SUB
```

```basic
SUB Main()
    UO.WaitMenu(0, 0, 0, 0, 0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.WaitMenu('example', 'example')
END SUB
```

### Расширенная перегрузка: 6 аргументов

```vb
SUB Main()
    VAR arg1 = 'example' # prompt1
    VAR arg2 = 'example' # choice1
    VAR arg3 = 'example' # prompt2
    VAR arg4 = 'example' # choice2
    VAR arg5 = 'example' # prompt3
    VAR arg6 = 'example' # choice3
    UO.WaitMenu(arg1, arg2, arg3, arg4, arg5, arg6)
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    UO.WaitMenu('example', 'example', 'example', 'example')
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 'example' # prompt
        VAR arg2 = 'example' # choice
        UO.WaitMenu(arg1, arg2)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 'example' # prompt
    VAR arg2 = 'example' # choice
    UO.WaitMenu(arg1, arg2)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.WaitMenu`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
