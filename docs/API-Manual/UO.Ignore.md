# UO.Ignore

ClassicUO • Runtime API • `UO.Ignore.md`

## Точный синтаксис / Registered signatures

```text
UO.Ignore(ObjID:Any) -> Unit
UO.Ignore(id:Any, stateValue:Any) -> Unit
UO.Ignore(id:Integer) -> Unit
UO.Ignore(id:String) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Ignore`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Добавляет указанный объект в список игнорирования. Игнорируемые объекты исключаются из всех последующих операций поиска ( FindType , FindTypeEx , FindTypesArrayEx и т.д.). ObjID — ID объекта для игнорирования. Если 0 , вызов молча пропускается. Если объект уже в списке игнорирования, вызов не имеет эффекта (дубликаты не создаются). Список игнорирования привязан к скрипту и сохраняется до завершения скрипта или вызова IgnoreReset .

### Current Basic signatures / Return

- `UO.Ignore(ObjID:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Ignore"]` → `BRIDGE CONTRACT -> IApiBridge.Ignore`

**Pascal compatibility signature:** `procedure Ignore(ObjID: Cardinal);`

### Additional current runtime overloads

- `UO.Ignore(id:ObjectRef, stateValue:Boolean) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `id` — Object/mobile serial or a supported Basic object reference such as self/backpack/lasttarget/saved object name; hexadecimal and decimal serials are accepted by Variant overloads.
- `stateValue` — Boolean-like value: TRUE/1 enables the option and FALSE/0 disables it unless Behavior documents another numeric mode.

### Accepted values / constants

- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `id` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `stateValue` — TRUE/FALSE or 1/0.

### Defaults / omitted arguments

Registered arities: 1, 2. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.Ignore(self)
END SUB
```

```basic
SUB Main()
    UO.Ignore(0, 0)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.Ignore(self)
END SUB
```

### Расширенная перегрузка: 2 аргументов

```vb
SUB Main()
    VAR arg1 = self # id
    VAR arg2 = 2 # stateValue
    UO.Ignore(arg1, arg2)
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = self # id
        UO.Ignore(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = self # id
    UO.Ignore(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
- `InjectionScript.Runtime.InjectionApiUO.Ignore`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
