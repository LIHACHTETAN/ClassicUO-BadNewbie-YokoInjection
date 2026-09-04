# Runtime API Manual — Part 19

Commands: **IsFlying** through **IsWaterTile**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.IsFlying`

### Direct runtime overloads

- `UO.IsFlying() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.IsFlying(serial:Integer) -> Integer`
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
VAR result = UO.IsFlying()
```

```basic
VAR result = UO.IsFlying(self)
```

---

## `UO.IsFrozen`

### Direct runtime overloads

- `UO.IsFrozen() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.IsFrozen(serial:Integer) -> Integer`
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
VAR result = UO.IsFrozen()
```

```basic
VAR result = UO.IsFrozen(self)
```

---

## `UO.IsGump`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если в кеше есть гампы, False , если гампов нет. Возвращает False , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsGump()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsGump"]` → `BRIDGE CONTRACT -> IApiBridge.GetGumpCount`

**Pascal compatibility signature:** `function IsGump: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsGump()
```

---

## `UO.IsGumpCanBeClosed`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если гамп с указанным индексом может быть закрыт пользователем, False — если он помечен как незакрываемый. GumpIndex — индекс гампа (начиная с 0, как используется в GetGumpInfo , GetGumpsCount ). Возвращает False , если персонаж не подключён. Некоторые серверные гампы помечены как незакрываемые — игрок должен ответить на них (например, нажать кнопку), а не просто закрыть.

### Current Yoko signatures / Return

- `UO.IsGumpCanBeClosed(GumpIndex)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsGumpCanBeClosed"]` → `BRIDGE CONTRACT -> IApiBridge.IsGumpCanBeClosed`

**Pascal compatibility signature:** `function IsGumpCanBeClosed(GumpIndex: Word): Boolean;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsGumpCanBeClosed(0)
```

---

## `UO.IsHidden`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайл is hidden (invisible), False otherwise. ObjID — ID of the мобайл to check. Returns False if the object does not exist or the character is disconnected. To check the player’s own hidden state, use Hidden . Возвращает True , если указанный мобайл скрыт (невидим), иначе False . ObjID — ID мобайла для проверки. Возвращает False , если объект не существует или персонаж не подключён. Для проверки состояния скрытности собственного персонажа используйте Hidden .

### Current Yoko signatures / Return

- `UO.IsHidden(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsHidden"]` → `BRIDGE CONTRACT -> IApiBridge.Hidden` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function IsHidden(ObjID: Cardinal): Boolean;`

### Additional current runtime overloads

- `UO.IsHidden() -> Integer`
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
VAR result = UO.IsHidden(self)
```

```basic
VAR result = UO.IsHidden()
```

---

## `UO.IsHouse`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если указанный объект является мульти-объектом (дом, корабль или другая многотайловая структура), иначе False . ObjID — ID объекта для проверки. Возвращает False , если объект не существует или персонаж не подключён. Несмотря на название, метод проверяет флаг мульти-объекта, поэтому возвращает True для любых многотайловых структур (дома, замки, корабли и т.д.), а не только для домов.

### Current Yoko signatures / Return

- `UO.IsHouse(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsHouse"]` → `BRIDGE CONTRACT -> IApiBridge.IsHouse`

**Pascal compatibility signature:** `function IsHouse(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsHouse(self)
```

---

## `UO.IsMineTile`

### Direct runtime overloads

- `UO.IsMineTile(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsMineTile(0, 0)
```

---

## `UO.IsMovable`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если указанный объект является перемещаемым, иначе False . ObjID — ID объекта для проверки. Проверка сочетает флаг «movable» с проверкой веса из данных тайла — вес статического тайла объекта должен превышать 90, чтобы объект считался перемещаемым. Возвращает False , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsMovable(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsMovable"]` → `BRIDGE CONTRACT -> IApiBridge.IsMovable`

**Pascal compatibility signature:** `function IsMovable(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsMovable(self)
```

---

## `UO.IsMoving`

### Direct runtime overloads

- `UO.IsMoving() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsMoving()
```

---

## `UO.IsNpc`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если указанный объект является мобайлом (NPC или персонаж игрока), иначе False . ObjID — ID объекта для проверки. Несмотря на название, метод проверяет флаг мобайла, поэтому возвращает True для любого мобайла — как NPC, так и персонажей игроков. Для различения NPC и игроков можно использовать GetNotoriety , возможные отличия в имени или GetTitle , наличие контейнера в Buy/Sell layer и прочие варианты, применимые к конкретному шарду. Однозначного варианта, гарантирующего 100% отличие NPC от игрока на любом шарде — нет. Возвращает False , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsNPC(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

**Pascal compatibility signature:** `function IsNPC(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsNpc(self)
```

---

## `UO.IsObjectExists`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если объект с указанным ID существует в локальном кэше объектов, иначе False . ObjID — ID объекта для проверки. Проверяется локальный кэш клиента, а не сервер. Объект может существовать на сервере, но ещё не быть известным клиенту, если он находится вне зоны видимости. Возвращает False , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsObjectExists(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsObjectExists"]` → `BRIDGE CONTRACT -> IApiBridge.Exists`

**Pascal compatibility signature:** `function IsObjectExists(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsObjectExists(self)
```

---

## `UO.IsOnline`

### Direct runtime overloads

- `UO.IsOnline() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsOnline()
```

---

## `UO.IsParalysed`

### Direct runtime overloads

- `UO.IsParalysed() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.IsParalysed(serial:Integer) -> Integer`
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
VAR result = UO.IsParalysed()
```

```basic
VAR result = UO.IsParalysed(self)
```

---

## `UO.IsParalyzed`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайл is paralyzed (frozen), False otherwise. ObjID — ID of the мобайл to check. Returns False if the object does not exist or the character is disconnected. To check the player’s own paralysis state, use Paralyzed . Возвращает True , если указанный мобайл парализован (заморожен), иначе False . ObjID — ID мобайла для проверки. Возвращает False , если объект не существует или персонаж не подключён. Для проверки состояния паралича собственного персонажа используйте Paralyzed .

### Current Yoko signatures / Return

- `UO.IsParalyzed(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsParalyzed"]` → `BRIDGE CONTRACT -> IApiBridge.GetLocked` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function IsParalyzed(ObjID: Cardinal): Boolean;`

### Additional current runtime overloads

- `UO.IsParalyzed() -> Integer`
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
VAR result = UO.IsParalyzed(self)
```

```basic
VAR result = UO.IsParalyzed()
```

---

## `UO.IsPoisoned`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайл is poisoned, False otherwise. ObjID — ID of the мобайл to check. The detection method depends on the client protocol version: for Stygian Abyss (SA) packets, the dedicated poison field is used; for older protocols, the poison/flying mobile flag is checked. Returns False if the object does not exist or the character is disconnected. To check the player’s own poison state, use Poisoned . Возвращает True , если указанный мобайл отравлен, иначе False . ObjID — ID мобайла для проверки. Метод определения зависит от версии протокола клиента: для пакетов Stygian Abyss (SA) используется выделенное поле яда; для старых протоколов — проверяется мобайл-флаг poison/flying. Возвращает False , если объект не существует или персонаж не подключён. Для проверки состояния отравления собственного персонажа используйте Poisoned .

### Current Yoko signatures / Return

- `UO.IsPoisoned(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsPoisoned"]` → `BRIDGE CONTRACT -> IApiBridge.Poisoned` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function IsPoisoned(ObjID: Cardinal): Boolean;`

### Additional current runtime overloads

- `UO.IsPoisoned() -> Integer`
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
VAR result = UO.IsPoisoned(self)
```

```basic
VAR result = UO.IsPoisoned()
```

---

## `UO.IsRunning`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайл is currently running, False otherwise. ObjID — ID of the мобайл to check. Returns False if the object does not exist or the character is disconnected. Возвращает True , если указанный мобайл в данный момент бежит, иначе False . ObjID — ID мобайла для проверки. Возвращает False , если объект не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsRunning(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsRunning"]` → `BRIDGE CONTRACT -> IApiBridge.GetRun` → `BRIDGE CONTRACT -> IApiBridge.Self`

**Pascal compatibility signature:** `function IsRunning(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsRunning(self)
```

---

## `UO.IsTrade`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если окно безопасного обмена в данный момент открыто, иначе False . Возвращает False , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.IsTrade()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsTrade"]` → `BRIDGE CONTRACT -> IApiBridge.IsTrade`

**Pascal compatibility signature:** `function IsTrade: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsTrade()
```

---

## `UO.IsTreeTile`

### Direct runtime overloads

- `UO.IsTreeTile(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsTreeTile(0, 0)
```

---

## `UO.IsWaitTargetActive`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если ловушка таргета сейчас взведена, то есть предыдущий вызов WaitTargetObject , WaitTargetSelf , WaitTargetLast , WaitTargetTile , WaitTargetXYZ , WaitTargetType или WaitTargetGround поставил в очередь ответ на таргет, который ещё не сработал. Возвращает False , когда поставленный в очередь курсор цели уже использован или ловушка снята через CancelWaitTarget . Удобно, чтобы дождаться фактического использования поставленного таргета перед продолжением.

### Current Yoko signatures / Return

- `UO.IsWaitTargetActive()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsWaitTargetActive"]`

**Pascal compatibility signature:** `function IsWaitTargetActive: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsWaitTargetActive()
```

---

## `UO.IsWarMode`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

мобайл is in war mode (combat stance), False otherwise. ObjID — ID of the мобайл to check. Returns False if the object does not exist or the character is disconnected. To set the player’s own war mode, use SetWarMode . Возвращает True , если указанный мобайл находится в боевом режиме, иначе False . ObjID — ID мобайла для проверки. Возвращает False , если объект не существует или персонаж не подключён. Для установки боевого режима собственного персонажа используйте SetWarMode .

### Current Yoko signatures / Return

- `UO.IsWarMode(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["IsWarMode"]` → `BRIDGE CONTRACT -> IApiBridge.IsWarMode`

**Pascal compatibility signature:** `function IsWarMode(ObjID: Cardinal): Boolean;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsWarMode(self)
```

---

## `UO.IsWaterTile`

### Direct runtime overloads

- `UO.IsWaterTile(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.IsWaterTile(0, 0)
```

---
