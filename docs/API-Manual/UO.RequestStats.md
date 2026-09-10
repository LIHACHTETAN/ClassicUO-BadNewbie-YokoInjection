# UO.RequestStats

ClassicUO • Runtime API • `UO.RequestStats.md`

## Точный синтаксис / Registered signatures

```text
UO.RequestStats(ObjID:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.RequestStats`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу пакет запроса статуса для указанного мобайла. ObjID — serial (ID) мобайла, для которого запрашивается статус. Используется для принудительного получения обновлённой информации о статусе (HP, Mana, Stamina, Str, Dex, Int и т.д.) мобайла. После ответа сервера методы GetHP , GetStr , GetDex , GetInt вернут обновлённые значения. Обратите внимание, что GetHP автоматически отправляет запрос статуса, если обнаруживает нулевые HP/MaxHP у живого мобайла, поэтому явные вызовы RequestStats в основном нужны для получения свежих данных других статов или для мобайлов, у которых HP уже известны. Не выполняет действий, если персонаж не подключён.

### Current Basic signatures / Return

- `UO.RequestStats(ObjID:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RequestStats"]` → `BRIDGE CONTRACT -> IApiBridge.RequestStats`

**Pascal compatibility signature:** `procedure RequestStats(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.RequestStats(self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.RequestStats(1)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # ObjID
    UO.RequestStats(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ObjID
    UO.RequestStats(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
