# UO.SetScriptName

ClassicUO • Runtime API • `UO.SetScriptName.md`

## Точный синтаксис / Registered signatures

```text
UO.SetScriptName(ScriptIndex:Any, Value:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetScriptName`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Устанавливает отображаемое имя для работающего скрипта по его индексу. ScriptIndex — индекс скрипта (с нуля) в пуле скриптов. Value — новое отображаемое имя скрипта. Изменяет имя, показываемое в списке скриптов интерфейса. Не влияет на имя файла скрипта или его выполнение. Полезно для идентификации скриптов при одновременном запуске нескольких экземпляров. Используйте GetScriptName для чтения текущего имени скрипта, и GetScriptsCount (Python: GetScriptCount ) для получения общего числа работающих скриптов.

### Current Basic signatures / Return

- `UO.SetScriptName(ScriptIndex:Integer, Value:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetScriptName"]` → `BRIDGE CONTRACT -> IApiBridge.SetScriptName`

**Pascal compatibility signature:** `procedure SetScriptName(ScriptIndex: Word; Value: String);`

### Parameters

- `ScriptIndex` — Integer control/count/index value (runtime value); exact zero/sentinel meaning is documented by this command.
- `Value` — String value. The concrete accepted domain is command-specific and is stated in Behavior/Notes; do not assume String conversion when the overload is numeric.

### Accepted values / constants

- `ScriptIndex` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Value` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Operates on the active Basic/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.SetScriptName(0, 'example')
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetScriptName(0, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 0 # ScriptIndex
    VAR arg2 = 2 # Value
    UO.SetScriptName(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 0 # ScriptIndex
    VAR arg2 = 2 # Value
    UO.SetScriptName(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
