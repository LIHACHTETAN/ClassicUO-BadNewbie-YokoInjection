# Runtime API Manual — Part 17

Commands: **Grab** through **Ignore**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.Grab`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Подбирает указанный предмет и перемещает его в рюкзак через маршрут Yoko/ClassicUO Grab. Порядок аргументов Yoko: сначала Count, затем ObjID. Count — количество предметов из стопки (0 означает всю стопку), ObjID — serial предмета либо сохранённое имя объекта. Возвращает True/1, когда запрос перемещения принят, иначе False/0.

### Current Yoko signatures / Return

- `UO.Grab(Count, ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Grab"]` → `BRIDGE CONTRACT -> IApiBridge.Grab`

**Pascal compatibility signature:** `function Grab(Count: Integer; ObjID: Cardinal): Boolean;`

### Additional current runtime overloads

- `UO.Grab() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.Grab(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `Count` — Quantity/count. 0 may mean all/default only where explicitly supported.
- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Grab(1, self)
```

```basic
VAR result = UO.Grab()
```

```basic
VAR result = UO.Grab(0)
```

---

## `UO.Ground`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает специальное значение, обозначающее землю как цель или место назначения в методах работы с предметами и поиска. Эта функция возвращает 0 . Используйте эту функцию вместо «магического числа», когда метод ожидает параметр контейнера/назначения, который может указывать на землю, например в DropItem , FindType , FindTypeEx или FindTypesArrayEx .

### Current Yoko signatures / Return

- `UO.Ground()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Ground"]`

**Pascal compatibility signature:** `function Ground: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Ground()
```

---

## `UO.GumpAutoCheckBox`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает значение чекбокса, которое будет автоматически применено к гампу, содержащему указанный чекбокс. CheckBoxID — ID элемента чекбокса в гампе. Value — 1 — отметить, 0 — снять отметку. При получении гампа Stealth перебирает все существующие гампы, а затем входящие, пока не найдёт тот, который содержит элемент с заданным CheckBoxID . Хук применяется к первому подходящему гампу. Для точного управления конкретным гампом рекомендуется использовать NumGumpCheckBox , который обращается к гампу по его индексу.

### Current Yoko signatures / Return

- `UO.GumpAutoCheckBox(CheckBoxID, Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GumpAutoCheckBox"]` → `BRIDGE CONTRACT -> IApiBridge.SetGumpValue`

**Pascal compatibility signature:** `procedure GumpAutoCheckBox(CheckBoxID: Integer; Value: Integer);`

### Parameters

- `CheckBoxID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Value` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.GumpAutoCheckBox(self, 'value')
```

---

## `UO.GumpAutoRadiobutton`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает значение радиокнопки, которое будет автоматически применено к гампу, содержащему указанную радиокнопку. RadiobuttonID — ID элемента радиокнопки в гампе. Value — 1 — выбрать, 0 — снять выбор. При получении гампа Stealth перебирает все существующие гампы, а затем входящие, пока не найдёт тот, который содержит элемент с заданным RadiobuttonID . Хук применяется к первому подходящему гампу. Для точного управления конкретным гампом рекомендуется использовать NumGumpRadiobutton , который обращается к гампу по его индексу.

### Current Yoko signatures / Return

- `UO.GumpAutoRadiobutton(RadiobuttonID, Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GumpAutoRadiobutton"]` → `BRIDGE CONTRACT -> IApiBridge.SetGumpValue`

**Pascal compatibility signature:** `procedure GumpAutoRadiobutton(RadiobuttonID: Integer; Value: Integer);`

### Parameters

- `RadiobuttonID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Value` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.GumpAutoRadiobutton(self, 'value')
```

---

## `UO.GumpAutoTextEntry`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает значение текстового поля, которое будет автоматически применено к гампу, содержащему указанное текстовое поле. TextEntryID — ID элемента текстового поля в гампе. Value — текстовая строка для заполнения. При получении гампа Stealth перебирает все существующие гампы, а затем входящие, пока не найдёт тот, который содержит элемент с заданным TextEntryID . Хук применяется к первому подходящему гампу. Для точного управления конкретным гампом рекомендуется использовать NumGumpTextEntry , который обращается к гампу по его индексу.

### Current Yoko signatures / Return

- `UO.GumpAutoTextEntry(TextEntryID, Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GumpAutoTextEntry"]` → `BRIDGE CONTRACT -> IApiBridge.SetGumpValue`

**Pascal compatibility signature:** `procedure GumpAutoTextEntry(TextEntryID: Integer; Value: String);`

### Parameters

- `TextEntryID` — String/text value interpreted according to the command.
- `Value` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.GumpAutoTextEntry(self, 'value')
```

---

## `UO.GumpExists`

### Direct runtime overloads

- `UO.GumpExists(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.GumpExists(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GumpExists(0)
```

```basic
VAR result = UO.GumpExists(0, 0)
```

---

## `UO.GumpObject`

### Manifest-registered overloads

- `UO.GumpObject(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.GumpObject(gumpId)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `gumpId` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.GumpObject(0)
```

```basic
UO.GumpObject(self)
```

---

## `UO.Help`

### Manifest-registered overloads

- `UO.Help() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Help()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Help()
```

```basic
UO.Help()
```

---

## `UO.HelpRequest`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос на показ окна помощи (аналогично нажатию кнопки «Help» в игровом клиенте).

### Current Yoko signatures / Return

- `UO.HelpRequest()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HelpRequest"]` → `BRIDGE CONTRACT -> IApiBridge.HelpRequest`

**Pascal compatibility signature:** `procedure HelpRequest;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.HelpRequest()
```

---

## `UO.Hex2Int`

### Direct runtime overloads

- `UO.Hex2Int(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Hex2Int(0)
```

---

## `UO.Hidden`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайл is hidden, use IsHidden . Возвращает True , если персонаж в данный момент скрыт (невидим), иначе False . Проверяет состояние скрытности собственного персонажа. Для проверки скрытности другого мобайла используйте IsHidden .

### Current Yoko signatures / Return

- `UO.Hidden()`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.Hidden"]`

**Pascal compatibility signature:** `function Hidden: Boolean;`

### Additional current runtime overloads

- `UO.Hidden(arg1:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.Hidden(serial:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Hidden()
```

```basic
VAR result = UO.Hidden(0)
```

```basic
VAR result = UO.Hidden(self)
```

---

## `UO.Hide`

### Direct runtime overloads

- `UO.Hide() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Opens an object Target. If the user selects a loaded item/mobile, that object is hidden locally in this ClassicUO client.
- `UO.Hide(serial) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Hides the specified loaded item/mobile immediately without opening Target.

### Parameters

- `serial` — loaded item/mobile serial (`Integer`, normally written as hexadecimal such as `0x40000044`). `0`, self, or a serial not present in the loaded world is rejected/no-op.

### Behavior

`UO.Hide` is a **client-side visibility command**, not the Ultima Online **Hiding** skill.

- `UO.Hide()` opens a normal object Target. Selecting a loaded item or mobile sets its local drawing state to hidden.
- `UO.Hide(serial)` performs the same local hide directly by serial and does **not** open Target.
- The object remains in world state; it is not destroyed and no delete-object packet is sent to the server.
- A later server resend, world reload, reconnect, or object recreation may make the object visible again.

### Notes / limitations

- Only the two forms above are supported. `Hide(x, y, z)` does **not** exist.
- The player's own mobile is intentionally refused.
- This affects only the local ClassicUO rendering state; it does not make the object invisible to other players or to the server.
- `CancelTarget()` / Escape can cancel the interactive `Hide()` form before selection.

### Examples

Interactive Target:

```basic
UO.Hide()
```

Hide a known object immediately:

```basic
VAR obj = 0x40000044
UO.Hide(obj)
```

Typical guarded use:

```basic
VAR obj = UO.GetLastTarget()
IF obj <> 0 THEN
    UO.Hide(obj)
END IF
```

---

## `UO.HighJournal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает индекс строки последней (самой новой) записи журнала. Возвращает -1 , если журнал пуст. Обычно используется с SetJournalLine для установки начальной точки поиска через InJournal , а также с LowJournal для определения полного диапазона записей журнала.

### Current Yoko signatures / Return

- `UO.HighJournal()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HighJournal"]` → `BRIDGE CONTRACT -> IApiBridge.JournalEntryCount`

**Pascal compatibility signature:** `function HighJournal: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.HighJournal()
```

---

## `UO.HP`

### Direct runtime overloads

- `UO.HP() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.HP()
```

---

## `UO.HTTP_Body`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает HTTP-заголовки ответа от последнего запроса HTTP_Get или HTTP_Post . Известный баг (сохранён для обратной совместимости): Несмотря на название, HTTP_Body на самом деле возвращает заголовки ответа, а не тело. Тело возвращается через HTTP_Header . Эта путаница имён — исторический баг, сохранённый, чтобы не ломать существующие скрипты. Возвращает пустую строку, если HTTP-запрос не выполнялся или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.HTTP_Body()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Body"]` → `STATE -> InjectionApiState.HttpBody`

**Pascal compatibility signature:** `function HTTP_Body: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.HTTP_Body()
```

---

## `UO.HTTP_Get`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Выполняет HTTP GET-запрос по указанному URL. URL — адрес запроса. После выполнения запроса используйте HTTP_Header для получения тела ответа и HTTP_Body для получения заголовков. См. примечания к HTTP_Body и HTTP_Header об исторической путанице имён. В DWS доступен необязательный второй параметр LStream ( TMemoryStream ). Если задан, сырое тело ответа записывается в этот поток вместо внутреннего строкового буфера. Полезно для скачивания бинарных данных (изображений, файлов). Если имя хоста не удаётся разрешить, метод записывает ошибку в системный журнал и завершается без выполнения запроса.

### Current Yoko signatures / Return

- `UO.HTTP_Get(URL, LStream)`
  - **Return type:** `Unit`
  - **Return contract:** Unit. With LStream, raw response bytes are written to the supported MemoryStream/File target.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Get"]` → `STATE -> InjectionApiState.HttpBody` → `STATE -> InjectionApiState.HttpHeader` → `BRIDGE CONTRACT -> IApiBridge.HttpRequest`
- `UO.HTTP_Get(URL, LStream)`
  - **Return type:** `Unit`
  - **Return contract:** Unit. With LStream, raw response bytes are written to the supported MemoryStream/File target.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Get"]` → `STATE -> InjectionApiState.HttpBody` → `STATE -> InjectionApiState.HttpHeader` → `BRIDGE CONTRACT -> IApiBridge.HttpRequest`

**Pascal compatibility signature:** `procedure HTTP_Get(URL: String; LStream: TMemoryStream = nil);`

### Parameters

- `URL` — HTTP/HTTPS URL string.
- `LStream` — Yoko MemoryStream/File-compatible output target for raw response bytes.

### Behavior

Performs an HTTP GET. The one-argument form returns/uses the registered text semantics; the LStream overload writes raw response bytes to a supported Yoko MemoryStream/File target.

### Notes / limitations

Network errors/timeouts remain runtime failures. For binary payloads use LStream/MemoryStream rather than converting bytes through UTF-8 text.

### Examples

```basic
UO.HTTP_Get('https://example.com/', 0)
```

---

## `UO.HTTP_Header`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает тело HTTP-ответа от последнего запроса HTTP_Get или HTTP_Post . Известный баг (сохранён для обратной совместимости): Несмотря на название, HTTP_Header на самом деле возвращает тело ответа, а не заголовки. Заголовки возвращаются через HTTP_Body . Эта путаница имён — исторический баг, сохранённый, чтобы не ломать существующие скрипты. Возвращает пустую строку, если HTTP-запрос не выполнялся или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.HTTP_Header()`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Header"]` → `STATE -> InjectionApiState.HttpHeader`

**Pascal compatibility signature:** `function HTTP_Header: String;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.HTTP_Header()
```

---

## `UO.HTTP_Post`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Выполняет HTTP POST-запрос по указанному URL с переданными данными и возвращает тело ответа. URL — адрес запроса. PostData — данные для тела POST-запроса. Возвращаемое значение — текст тела ответа. После запроса HTTP_Header также содержит тело ответа, а HTTP_Body — заголовки (см. примечания об исторической путанице имён в этих методах). Если имя хоста не удаётся разрешить, метод записывает ошибку в системный журнал и возвращает пустую строку. PascalScript поддерживает только форму с TStringList . DWScript поддерживает как форму с TStringList , так и дополнительную перегрузку, принимающую простую String .

### Current Yoko signatures / Return

- `UO.HTTP_Post(URL, PostData)`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["HTTP_Post"]` → `STATE -> InjectionApiState.HttpBody` → `STATE -> InjectionApiState.HttpHeader` → `BRIDGE CONTRACT -> IApiBridge.HttpRequest`

**Pascal compatibility signature:** `function HTTP_Post(URL: String; PostData: TStringList): String;`

### Parameters

- `URL` — HTTP/HTTPS URL string.
- `PostData` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.HTTP_Post('https://example.com/', 0)
```

---

## `UO.Ignore`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Добавляет указанный объект в список игнорирования. Игнорируемые объекты исключаются из всех последующих операций поиска ( FindType , FindTypeEx , FindTypesArrayEx и т.д.). ObjID — ID объекта для игнорирования. Если 0 , вызов молча пропускается. Если объект уже в списке игнорирования, вызов не имеет эффекта (дубликаты не создаются). Список игнорирования привязан к скрипту и сохраняется до завершения скрипта или вызова IgnoreReset .

### Current Yoko signatures / Return

- `UO.Ignore(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Ignore"]` → `BRIDGE CONTRACT -> IApiBridge.Ignore`

**Pascal compatibility signature:** `procedure Ignore(ObjID: Cardinal);`

### Additional current runtime overloads

- `UO.Ignore(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Ignore(self)
```

```basic
UO.Ignore(0, 0)
```

---
