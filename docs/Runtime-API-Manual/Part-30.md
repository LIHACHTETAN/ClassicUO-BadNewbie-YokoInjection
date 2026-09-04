# Runtime API Manual — Part 30

Commands: **TargetID** through **Undress**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.TargetID`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает ID текущего курсора цели. Если курсор цели активен ( IsTargeting = True ), но его ID равен 0 , возвращается специальная константа для обратной совместимости. Возвращает 0 , если курсор цели не активен.

### Current Yoko signatures / Return

- `UO.TargetID()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TargetID"]` → `BRIDGE CONTRACT -> IApiBridge.LastTarget`

**Pascal compatibility signature:** `function TargetID: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TargetID()
```

---

## `UO.Targeting`

### Direct runtime overloads

- `UO.Targeting() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Targeting()
```

---

## `UO.TargetPresent`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если сейчас активен курсор таргета — то есть сервер запросил цель и Stealth ожидает ответа на таргет. Возвращает False , если ожидающего запроса таргета нет. Обычно используется для проверки того, пришёл ли запрос таргета (например, после каста заклинания или использования умения), перед тем как ответить на него методом WaitTargetObject , CancelTarget или аналогичным.

### Current Yoko signatures / Return

- `UO.TargetPresent()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TargetPresent"]`

**Pascal compatibility signature:** `function TargetPresent: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TargetPresent()
```

---

## `UO.TargetToObject`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отвечает на активный курсор цели, нацеливаясь на указанный объект. ObjID — serial (ID) объекта-цели. Не выполняет действий, если курсор цели не активен. Объект должен существовать в мире; если нет, ответ о цели всё равно отправляется (валидность определяет сервер). Используйте WaitForTarget для ожидания курсора цели перед вызовом, или WaitTargetObject для предварительной установки цели до действия, вызывающего курсор.

### Current Yoko signatures / Return

- `UO.TargetToObject(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TargetToObject"]` → `BRIDGE CONTRACT -> IApiBridge.WaitTargetObject`

**Pascal compatibility signature:** `procedure TargetToObject(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.TargetToObject(self)
```

---

## `UO.TargetToTile`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отвечает на активный курсор цели, нацеливаясь на конкретный тайл по указанным координатам. Tile — graphic ID тайла-цели. X , Y — горизонтальная и вертикальная координаты карты. Z — высота цели. Не выполняет действий, если курсор цели не активен. Используется, когда заклинание или действие требует нацеливания на тайл карты, а не на объект (например, заклинания с областью действия). Используйте WaitForTarget для ожидания курсора цели перед вызовом, или WaitTargetTile для предварительной установки цели до действия, вызывающего курсор.

### Current Yoko signatures / Return

- `UO.TargetToTile(Tile, X, Y, Z)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TargetToTile"]`

**Pascal compatibility signature:** `procedure TargetToTile(Tile: Word; X: Word; Y: Word; Z: ShortInt);`

### Parameters

- `Tile` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `Z` — World/tile Z coordinate.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.TargetToTile(0, UO.GetX(self), UO.GetY(self), UO.GetZ(self))
```

---

## `UO.TargetToXYZ`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отвечает на активный курсор цели, нацеливаясь на координаты карты без указания graphic тайла. X , Y — горизонтальная и вертикальная координаты карты. Z — высота цели. Эквивалентно вызову TargetToTile(0, X, Y, Z) — graphic тайла устанавливается в 0 (земля). Не выполняет действий, если курсор цели не активен. Используйте WaitForTarget для ожидания курсора цели перед вызовом, или WaitTargetXYZ для предварительной установки цели до действия, вызывающего курсор.

### Current Yoko signatures / Return

- `UO.TargetToXYZ(X, Y, Z)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TargetToXYZ"]`

**Pascal compatibility signature:** `procedure TargetToXYZ(X: Word; Y: Word; Z: ShortInt);`

### Parameters

- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `Z` — World/tile Z coordinate.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.TargetToXYZ(UO.GetX(self), UO.GetY(self), UO.GetZ(self))
```

---

## `UO.Terminate`

### Direct runtime overloads

- `UO.Terminate(arg1:String) -> Unit`
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
UO.Terminate(0)
```

---

## `UO.TextClear`

### Direct runtime overloads

- `UO.TextClear() -> Unit`
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
UO.TextClear()
```

---

## `UO.TextClose`

### Direct runtime overloads

- `UO.TextClose() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.TextClose()
```

---

## `UO.TextOpen`

### Direct runtime overloads

- `UO.TextOpen() -> Unit`
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
UO.TextOpen()
```

---

## `UO.TextPrint`

### Direct runtime overloads

- `UO.TextPrint(arg1:String) -> Unit`
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
UO.TextPrint(0)
```

---

## `UO.TicksAnim`

### Direct runtime overloads

- `UO.TicksAnim() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TicksAnim()
```

---

## `UO.TicksDead`

### Direct runtime overloads

- `UO.TicksDead() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TicksDead()
```

---

## `UO.TicksSkill`

### Direct runtime overloads

- `UO.TicksSkill() -> Integer`
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
VAR result = UO.TicksSkill()
```

---

## `UO.TicksSpell`

### Direct runtime overloads

- `UO.TicksSpell() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TicksSpell()
```

---

## `UO.TicksTarget`

### Direct runtime overloads

- `UO.TicksTarget() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TicksTarget()
```

---

## `UO.TicksUse`

### Direct runtime overloads

- `UO.TicksUse() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TicksUse()
```

---

## `UO.Time`

### Direct runtime overloads

- `UO.Time() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Time()
```

---

## `UO.Timer`

### Direct runtime overloads

- `UO.Timer() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Timer()
```

---

## `UO.ToggleFly`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Переключает режим полёта для персонажа-Гаргульи. Метод работает только при выполнении всех условий: Сервер поддерживает расширение Stygian Abyss (флаг SA). Раса персонажа — Гаргулья (race = 3). Версия клиента 7.0.0.0 или выше. Если любое условие не выполнено, вызов ничего не делает. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.ToggleFly()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ToggleFly"]` → `BRIDGE CONTRACT -> IApiBridge.ToggleFly`

**Pascal compatibility signature:** `procedure ToggleFly;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.ToggleFly()
```

---

## `UO.Track`

### Direct runtime overloads

- `UO.Track(arg1:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Track(arg1:Any, arg2:Any, arg3:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Track() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Track(0)
```

```basic
UO.Track(0, 0, 0)
```

```basic
UO.Track()
```

---

## `UO.TradeCheck`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает состояние «галочки» (принятия) участника окна безопасной торговли. TradeNum — индекс окна торговли (используйте TradeCount для получения числа активных торговых окон). Num — какого участника проверять: 1 = свой (ваша сторона), 2 = сторона оппонента. Значение 0 или больше 2 — невалидны, возвращается False . Возвращает True , если указанный участник отметил (принял) торговлю, False — в противном случае или при ошибке. Возвращает False , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.TradeCheck(TradeNum, Num)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["TradeCheck"]` → `BRIDGE CONTRACT -> IApiBridge.TradeCheck`

**Pascal compatibility signature:** `function TradeCheck(TradeNum: Byte; Num: Byte): Boolean;`

### Additional current runtime overloads

- `UO.TradeCheck(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.TradeCheck(arg1:Any, arg2:Any, arg3:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `TradeNum` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Num` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TradeCheck(0, 0)
```

```basic
VAR result = UO.TradeCheck(0)
```

```basic
VAR result = UO.TradeCheck(0, 0, 0)
```

---

## `UO.TradeContainer`

### Direct runtime overloads

- `UO.TradeContainer(arg1:Any) -> String`
  - **Return type:** `String`
  - **Return contract:** String runtime value. Empty string may be a valid no-data/no-match result.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TradeContainer(0)
```

---

## `UO.TradeCount`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает количество активных окон безопасной торговли. Возвращает 0 , если торговых окон нет или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.TradeCount()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.TradeCount"]`

**Pascal compatibility signature:** `function TradeCount: Byte;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.TradeCount()
```

---

## `UO.TradeName`

### Direct runtime overloads

- `UO.TradeName(arg1:Any) -> String`
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
VAR result = UO.TradeName(0)
```

---

## `UO.TradeOpponent`

### Direct runtime overloads

- `UO.TradeOpponent(arg1:Any) -> String`
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
VAR result = UO.TradeOpponent(0)
```

---

## `UO.Undress`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Снимает все экипированные предметы персонажа в рюкзак. Перебирает все слои экипировки (правая рука, левая рука, обувь, штаны, рубашка, шлем, перчатки, кольцо, шея, пояс, торс, браслет, внешний торс, серьги, руки, плащ, мантия, юбка, ноги) и перемещает каждый экипированный предмет в рюкзак с задержкой DressSpeed между операциями. На клиентах версии 7.7.4+ (целочисленная версия ≥ 7007400) используется встроенный пакет UnequipItemsSetMacro вместо ручного перебора слоёв. Возвращает True , если все предметы успешно сняты. Возвращает False , если персонаж не подключён или перенос какого-либо предмета не удался.

### Current Yoko signatures / Return

- `UO.Undress()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Undress"]`

**Pascal compatibility signature:** `function Undress: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Undress()
```

---
