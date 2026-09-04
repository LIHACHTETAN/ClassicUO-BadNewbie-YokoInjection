# Runtime API Manual — Part 26

Commands: **ReqProfile** through **SetArm**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.ReqProfile`

### Manifest-registered overloads

- `UO.ReqProfile() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.ReqProfile(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.ReqProfile()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.ReqProfile(mobile)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `mobile` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Operates on the active Yoko/ClassicUO runtime, network or profile state through the registered implementation route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ReqProfile()
```

```basic
UO.ReqProfile(self)
```

---

## `UO.RequestContextMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос контекстного меню для указанного объекта. ObjID — serial (ID) объекта, для которого запрашивается контекстное меню. Запрос отправляется только если флаги возможностей сервера включают поддержку контекстных меню. Если контекстные меню на шарде не включены, вызов ничего не делает. Ответ приходит асинхронно. Используйте GetContextMenu для получения пунктов меню после небольшой задержки. Рекомендуется вызывать ClearContextMenu перед запросом, чтобы получить свежие данные. Для автоматического выбора пункта контекстного меню при его получении используйте SetContextMenuHook . Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.RequestContextMenu(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RequestContextMenu"]` → `BRIDGE CONTRACT -> IApiBridge.RequestContextMenu`

**Pascal compatibility signature:** `procedure RequestContextMenu(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.RequestContextMenu(self)
```

---

## `UO.RequestStats`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу пакет запроса статуса для указанного мобайла. ObjID — serial (ID) мобайла, для которого запрашивается статус. Используется для принудительного получения обновлённой информации о статусе (HP, Mana, Stamina, Str, Dex, Int и т.д.) мобайла. После ответа сервера методы GetHP , GetStr , GetDex , GetInt вернут обновлённые значения. Обратите внимание, что GetHP автоматически отправляет запрос статуса, если обнаруживает нулевые HP/MaxHP у живого мобайла, поэтому явные вызовы RequestStats в основном нужны для получения свежих данных других статов или для мобайлов, у которых HP уже известны. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.RequestStats(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RequestStats"]` → `BRIDGE CONTRACT -> IApiBridge.RequestStats`

**Pascal compatibility signature:** `procedure RequestStats(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.RequestStats(self)
```

---

## `UO.ReqVirtuesGump`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет серверу запрос на открытие окна добродетелей (Virtues gump) для текущего персонажа. На официальных шардах дополнительно устанавливается внутренний флаг запроса, который влияет на обработку входящего пакета гампа. Гамп появляется асинхронно — используйте WaitGump или GetGumpsCount для ожидания и взаимодействия с ним.

### Current Yoko signatures / Return

- `UO.ReqVirtuesGump()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ReqVirtuesGump"]` → `BRIDGE CONTRACT -> IApiBridge.RequestVirtuesGump`

**Pascal compatibility signature:** `procedure ReqVirtuesGump;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ReqVirtuesGump()
```

---

## `UO.Resend`

### Manifest-registered overloads

- `UO.Resend() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Resend()`
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
VAR result = UO.Resend()
```

```basic
UO.Resend()
```

---

## `UO.ResetProfile`

### Current Yoko signatures / Return

- `UO.ResetProfile() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The active character profile is replaced with a fresh copy of the configured default profile and immediately saved.

### Parameters

- None.

### Behavior

Resets the **currently loaded ClassicUO/Yoko character profile** to `default.json` (or built-in defaults when no default file exists). The profile identity is preserved: account/user name, connected server name and character name are copied back into the reset profile. The result is saved to the current server-specific `profile.json`.

The profile directory is not `v2`: it remains under `Data/Profiles/<connected server name>/<character serial>/` (or the configured ProfilesPath equivalent).

### Notes / limitations

- This resets settings for the currently loaded character profile; it does not delete the profile directory.
- Server/account/character identity is preserved intentionally.
- If no character profile is active, the command reports an error and performs no reset.
- Runtime/UI objects that read profile settings use the new profile after the reset; settings that require recreating a window may become visually apparent after reopening that window.

### Examples

```basic
UO.ResetProfile()
```
---

## `UO.ResistCold`

### Direct runtime overloads

- `UO.ResistCold() -> Integer`
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
VAR result = UO.ResistCold()
```

---

## `UO.ResistEnergy`

### Direct runtime overloads

- `UO.ResistEnergy() -> Integer`
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
VAR result = UO.ResistEnergy()
```

---

## `UO.ResistFire`

### Direct runtime overloads

- `UO.ResistFire() -> Integer`
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
VAR result = UO.ResistFire()
```

---

## `UO.ResistPhysical`

### Direct runtime overloads

- `UO.ResistPhysical() -> Integer`
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
VAR result = UO.ResistPhysical()
```

---

## `UO.ResistPoison`

### Direct runtime overloads

- `UO.ResistPoison() -> Integer`
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
VAR result = UO.ResistPoison()
```

---

## `UO.Salute`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Выполняет анимацию салюта (эмоцию) персонажем. Отправляет серверу пакет действия 'salute' , что запускает анимацию салюта, видимую находящимся поблизости игрокам. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Salute()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Salute"]` → `BRIDGE CONTRACT -> IApiBridge.Salute`

**Pascal compatibility signature:** `procedure Salute;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Salute()
```

---

## `UO.SaveConfig`

### Direct runtime overloads

- `UO.SaveConfig() -> Unit`
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
UO.SaveConfig()
```

---

## `UO.SaveHotkeys`

### Current Yoko signatures / Return

- `UO.SaveHotkeys() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Saves the active ClassicUO macro/hotkey definitions through `World.Macros.Save()`.

### Parameters

- None in the current embedded Yoko overload.

### Behavior

Writes the current macro list to the active profile's `macros.xml`. The file is stored under the current server-name/character profile directory.

### Notes / limitations

This is the embedded ClassicUO macro profile, not a separate legacy Injection hotkey-file format.

### Examples

```basic
UO.SaveHotkeys()
```

---

## `UO.Say`

### Direct runtime overloads

- `UO.Say(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Say(0)
```

---

## `UO.SayU`

### Manifest-registered overloads

- `UO.SayU(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.SayU(text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `text` — String/text value interpreted according to the command.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.SayU(0)
```

```basic
UO.SayU('value')
```

---

## `UO.ScanInt`

### Direct runtime overloads

- `UO.ScanInt(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ScanInt(0, 0)
```

---

## `UO.SelectGump`

### Direct runtime overloads

- `UO.SelectGump(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SelectGump(0)
```

---

## `UO.SelectIgnoreList`

### Manifest-registered overloads

- `UO.SelectIgnoreList(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.SelectIgnoreList(list)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `list` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.SelectIgnoreList(0)
```

```basic
UO.SelectIgnoreList(0)
```

---

## `UO.Self`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает serial (ID) текущего персонажа (игрока). Это основной способ получения ID объекта игрока, который используется в качестве параметра во многих других методах API. SelfID и PlayerID — алиасы для этого метода. Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.Self()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Self"]` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function Self: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Self()
```

---

## `UO.Sell`

### Manifest-registered overloads

- `UO.Sell(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Sell(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Sell(arg1:Any, arg2:Any, arg3:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Sell(type)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Sell(type, color)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Sell(type, color, quantity)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `quantity` — Quantity/count. 0 may mean all/default only where explicitly supported.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Sell(0)
```

```basic
UO.Sell(0x0190, -1, 1)
```

---

## `UO.SendGumpSelect`

### Direct runtime overloads

- `UO.SendGumpSelect(arg1:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SendGumpSelect(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SendGumpSelect(0)
```

```basic
UO.SendGumpSelect(0)
```

---

## `UO.SendShopReply`

### Direct runtime overloads

- `UO.SendShopReply(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SendShopReply(0)
```

---

## `UO.ServerPrint`

### Direct runtime overloads

- `UO.ServerPrint(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ServerPrint(0)
```

---

## `UO.Set`

### Direct runtime overloads

- `UO.Set(arg1:String, arg2:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Set(arg1:String, arg2:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Set(0, 0)
```

```basic
UO.Set(0, 0)
```

---

## `UO.SetARExtParams`

### Current Yoko signatures / Return

- `UO.SetARExtParams() -> Unit`
- `UO.SetARExtParams(ShardName) -> Unit`
- `UO.SetARExtParams(ShardName, CharName) -> Unit`
- `UO.SetARExtParams(ShardName, CharName, UseAtEveryConnect) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command updates the reconnect selection state used by the real ClassicUO login flow.

### Parameters

- `ShardName` — display name of the shard/server to select on reconnect. Empty or omitted uses the current connected shard name.
- `CharName` — character name to select after the server character list arrives. Empty or omitted uses the current character name when available.
- `UseAtEveryConnect` — Boolean/integer flag. `0` makes the requested character override one-shot; non-zero keeps the character selection override for subsequent reconnects. The shard display selection is saved through ClassicUO's normal `LastServerName` settings path.

### Behavior

The values are no longer stored as inert runtime-only strings. Yoko passes them into the actual ClassicUO reconnect selection pipeline:

1. the shard name updates ClassicUO's selected server preference;
2. the character name is supplied through `LastCharacterManager`;
3. the next `UO.Connect()` / reconnect uses those preferences when the server list and character list are received.

The command does **not** enable automatic reconnect by itself. Use the normal AutoReconnect/`SetARStatus` API for that policy.

### Notes / limitations

- `ShardName` is the human-readable server/shard name, not `IP:port` and not the internal profile identity key.
- Selection can only succeed if the requested shard/character is actually returned by the server.
- The connected server's profile folder is created using the actual display server name, for example `Data/Profiles/Age of Power/0x12345678/`.

### Examples

```basic
UO.SetARExtParams('Age of Power', 'LIHACH', 1)
```

```basic
# Use current shard/current character as reconnect selection.
UO.SetARExtParams()
```
---

## `UO.SetArm`

### Direct runtime overloads

- `UO.SetArm(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetArm(0)
```

---
