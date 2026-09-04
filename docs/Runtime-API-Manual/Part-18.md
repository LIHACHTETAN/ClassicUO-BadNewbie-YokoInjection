# Runtime API Manual — Part 18

Commands: **IgnoreOff** through **IsFemale**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.IgnoreOff`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Удаляет указанный объект из списка игнорирования, делая его снова видимым для операций поиска. ObjID — ID объекта, который нужно перестать игнорировать. Если объект отсутствует в списке игнорирования, вызов не имеет эффекта.

### Current Yoko signatures / Return

- `UO.IgnoreOff(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IgnoreOff"]` → `BRIDGE CONTRACT -> IApiBridge.Unignore`

**Pascal compatibility signature:** `procedure IgnoreOff(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.IgnoreOff(self)
```

---

## `UO.IgnoreReset`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Очищает весь список игнорирования, делая все ранее игнорируемые объекты снова видимыми для операций поиска.

### Current Yoko signatures / Return

- `UO.IgnoreReset()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.IgnoreReset"]`

**Pascal compatibility signature:** `procedure IgnoreReset;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.IgnoreReset()
```

---

## `UO.Info`

### Manifest-registered overloads

- `UO.Info() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Info(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Info()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Info(object)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `object` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Info()
```

```basic
UO.Info(self)
```

---

## `UO.InfoColor`

### Manifest-registered overloads

- `UO.InfoColor() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.InfoColor(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.InfoColor()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.InfoColor(object)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `object` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.InfoColor()
```

```basic
UO.InfoColor(self)
```

---

## `UO.InfoFindList`

### Manifest-registered overloads

- `UO.InfoFindList() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.InfoFindList()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.InfoFindList()
```

```basic
UO.InfoFindList()
```

---

## `UO.InfoGump`

### Current Yoko overloads

- `UO.InfoGump() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Opens the Yoko **Gump Inspector** for the last active server Gump.
- `UO.InfoGump(gump) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Opens the inspector for the requested Gump when it can be resolved by index, local serial, or server Gump ID.

### Parameters

- `gump` — Gump selector. The current bridge accepts an active-Gump index and also resolves matching local/server Gump IDs. Use `InfoGumps()` first when several Gumps are open and you do not know which selector to use.

### Behavior

Opens a dedicated **Yoko Gump Inspector**. The inspector is not a journal dump: it is an in-client information window built from the currently active ClassicUO Gump tree.

The inspector shows, when available:

- active Gump index;
- local `Serial`;
- server `GumpID`;
- screen `X` / `Y`;
- `Width` / `Height`;
- active `Page`;
- close capability;
- total control count;
- Buttons with **ButtonID**, action/page information and graphics;
- Checkbox / Radio controls with IDs, checked state and graphics;
- TextEntry values;
- text/HTML/cliloc-derived visible text where the ClassicUO control exposes it;
- a full per-control description for debugging scripts.

The inspected Gump also becomes the selected Gump used by `UO.SendGumpSelect(buttonId)`, so inspection and subsequent scripted button activation refer to the same window unless it is closed/disposed.

### Notes / limitations

- `InfoGump()` selects the **last active server Gump**.
- If the requested Gump cannot be resolved, no other Gump is silently substituted; an error is reported.
- The information reflects ClassicUO's currently loaded UI controls. Server-side data that was never sent to the client cannot be displayed.
- Control descriptions are intended for script development and may contain client-control type names in addition to shard-level IDs.

### Examples

Inspect the most recently opened Gump:

```basic
UO.InfoGump()
```

List all active Gumps first, then inspect Gump index `0`:

```basic
UO.InfoGumps()
UO.InfoGump(0)
```

After visually finding ButtonID `1001`, press it on the same selected Gump:

```basic
UO.InfoGump()
UO.SendGumpSelect(1001)
```

---

## `UO.InfoGumps`

### Current Yoko overloads

- `UO.InfoGumps() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Opens a list of all active server Gumps.
- `UO.InfoGumps(gump) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Compatibility form that opens the detailed inspector for the requested Gump.

### Parameters

- `gump` — optional active-Gump selector (index/local serial/server Gump ID) for the compatibility form.

### Behavior

Without arguments, opens the **Active Server Gumps** window. Each row identifies one currently active server Gump and includes the information needed to choose it for `InfoGump`, such as:

- index;
- `GumpID`;
- local `Serial`;
- screen position;
- size;
- active page;
- control count.

`InfoGumps()` is therefore the discovery/list command, while `InfoGump()` is the detailed control inspector.

### Notes / limitations

- Only active, non-disposed server Gumps are listed.
- Client-only UI Gumps with no server serial are intentionally excluded from this server-Gump list.
- The list is a snapshot; indexes can change when Gumps close/open. Resolve/inspect again before acting if the UI changed.

### Examples

Show every active server Gump:

```basic
UO.InfoGumps()
```

Inspect the first listed Gump:

```basic
UO.InfoGumps()
UO.InfoGump(0)
```

---

## `UO.InfoTile`

### Manifest-registered overloads

- `UO.InfoTile() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.InfoTile(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.InfoTile(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.InfoTile()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.InfoTile(x)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.InfoTile(x, y)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `x` — World/tile X coordinate.
- `y` — World/tile Y coordinate.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.InfoTile()
```

```basic
UO.InfoTile(UO.GetX(self), UO.GetY(self))
```

---

## `UO.Inj2EUO`

### Direct runtime overloads

- `UO.Inj2EUO(arg1:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Inj2EUO(0)
```

---

## `UO.InJournal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет указанную строку в журнале, просматривая записи от последней к первой. Str — текст для поиска (регистронезависимый поиск подстроки). Поддерживает поиск нескольких строк через разделитель | . Например, 'gold|silver|copper' найдёт строку, содержащую любое из этих слов. Возвращает индекс найденной строки или -1 , если совпадений не найдено. Поиск начинается от записи, установленной через SetJournalLine , и идёт назад к более старым записям. После успешного нахождения обновляются следующие свойства Line* данными из найденной записи: LineID , LineName , LineTime , LineMsgType , LineType , LineTextColor , LineTextFont , LineIndex , LineCount .

### Current Yoko signatures / Return

- `UO.InJournal(Str)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["InJournal"]`

**Pascal compatibility signature:** `function InJournal(Str: String): Integer;`

### Parameters

- `Str` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.InJournal(0)
```

---

## `UO.InJournalBetweenTimes`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет указанную строку в журнале, но только в заданном временном диапазоне. Str — текст для поиска (регистронезависимый поиск подстроки). Поддерживает разделитель | для поиска нескольких строк, как и InJournal . TimeBegin — начало временного диапазона ( TDateTime ). TimeEnd — конец временного диапазона ( TDateTime ). Порядок TimeBegin и TimeEnd не имеет значения — метод автоматически определяет меньшее значение как начало, а большее как конец. Возвращает индекс найденной строки или -1 , если совпадений не найдено в указанном временном диапазоне. После успешного нахождения свойства Line* обновляются так же, как и у InJournal .

### Current Yoko signatures / Return

- `UO.InJournalBetweenTimes(Str, TimeBegin, TimeEnd)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["InJournalBetweenTimes"]`

**Pascal compatibility signature:** `function InJournalBetweenTimes(Str: String; TimeBegin: TDateTime; TimeEnd: TDateTime): Integer;`

### Additional current runtime overloads

- `UO.InJournalBetweenTimes(arg1:String, arg2:Integer, arg3:Integer, arg4:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `Str` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `TimeBegin` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `TimeEnd` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.InJournalBetweenTimes(0, 0, 0)
```

```basic
VAR result = UO.InJournalBetweenTimes(0, 0, 0, 0)
```

---

## `UO.InParty`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если персонаж в данный момент состоит в пати, иначе False . Внутренне проверяет, не пуст ли список членов пати.

### Current Yoko signatures / Return

- `UO.InParty()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["InParty"]` → `BRIDGE CONTRACT -> IApiBridge.InParty`

**Pascal compatibility signature:** `function InParty: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.InParty()
```

---

## `UO.Int`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает текущее значение характеристики Интеллект персонажа. Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Int()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Int"]` → `BRIDGE CONTRACT -> IApiBridge.Intelligence`

**Pascal compatibility signature:** `function Int: Integer;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Int()
```

---

## `UO.Int2Hex`

### Direct runtime overloads

- `UO.Int2Hex(arg1:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Int2Hex(0)
```

---

## `UO.Intelligence`

### Direct runtime overloads

- `UO.Intelligence() -> Integer`
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
VAR result = UO.Intelligence()
```

---

## `UO.InviteToParty`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет приглашение в пати указанному мобайлу. ObjID — ID мобайла для приглашения. Метод сначала проверяет, существует ли объект в мире клиента. Если найден, устанавливает таргет на указанного мобайла и отправляет запрос на приглашение в пати. Если объект не существует, в системный журнал записывается ошибка: "InviteToParty error: Object not found." .

### Current Yoko signatures / Return

- `UO.InviteToParty(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["InviteToParty"]` → `BRIDGE CONTRACT -> IApiBridge.PartyInvite`

**Pascal compatibility signature:** `procedure InviteToParty(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.InviteToParty(self)
```

---

## `UO.IsActiveSpellAbility`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если указанное заклинание или способность в данный момент активны на персонаже, иначе False . Pascal: SpellName — название заклинания строкой (например, 'Cunning' , 'Bless' ). Пробелы в имени автоматически заменяются на подчёркивания. Если имя не распознано, в системный журнал записывается ошибка: "ActiveSpellAbility error: unknown spell name" . Python: SpellID — индекс заклинания в виде целого числа. Также можно использовать значения из перечисления Spell (см. ConstantsAndEnums ). Возвращает False , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsActiveSpellAbility(SpellName)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsActiveSpellAbility"]` → `BRIDGE CONTRACT -> IApiBridge.IsActiveSpell`

**Pascal compatibility signature:** `function IsActiveSpellAbility(SpellName: String): Boolean;`

### Parameters

- `SpellName` — String/text value interpreted according to the command.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsActiveSpellAbility('value')
```

---

## `UO.IsAlive`

### Direct runtime overloads

- `UO.IsAlive() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.IsAlive(serial:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- `serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsAlive()
```

```basic
VAR result = UO.IsAlive(self)
```

---

## `UO.IsContainer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если указанный объект является контейнером, иначе False . ObjID — ID объекта для проверки. Возвращает False , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsContainer(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsContainer"]` → `BRIDGE CONTRACT -> IApiBridge.IsContainer`

**Pascal compatibility signature:** `function IsContainer(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsContainer(self)
```

---

## `UO.IsDead`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайл is dead, False otherwise. ObjID — ID of the мобайл to check. Returns False if the object does not exist or the character is disconnected. To check the player’s own death state, use Dead . Возвращает True , если указанный мобайл мёртв, иначе False . ObjID — ID мобайла для проверки. Возвращает False , если объект не существует или персонаж не подключён. Для проверки состояния смерти собственного персонажа используйте Dead .

### Current Yoko signatures / Return

- `UO.IsDead(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsDead"]` → `BRIDGE CONTRACT -> IApiBridge.Dead` → `BRIDGE CONTRACT -> IApiBridge.IsDead`

**Pascal compatibility signature:** `function IsDead(ObjID: Cardinal): Boolean;`

### Additional current runtime overloads

- `UO.IsDead() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsDead(self)
```

```basic
VAR result = UO.IsDead()
```

---

## `UO.IsFemale`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайл has the female flag set, False otherwise. ObjID — ID of the мобайл to check. Returns False if the object does not exist or the character is disconnected. Возвращает True , если у указанного мобайла установлен флаг женского пола, иначе False . ObjID — ID мобайла для проверки. Возвращает False , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsFemale(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsFemale"]` → `BRIDGE CONTRACT -> IApiBridge.IsFemale` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function IsFemale(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsFemale(self)
```

---
