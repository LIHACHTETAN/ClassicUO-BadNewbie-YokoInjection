# Runtime API Manual — Part 22

Commands: **MaxWeight** through **MoverStop**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.MaxWeight`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает максимальный переносимый вес персонажа (из расширенной информации о статусе). Если сервер предоставляет полную расширенную информацию (DataFlag >= 5), значение берётся непосредственно из серверного пакета. Для старых версий сервера или сокращённой расширенной информации значение рассчитывается локально на основе Силы персонажа: Клиент версии 5.0+: (Str / 2) * 7 + 40 Старые версии клиента: Str * 4 + 25 Возвращает 0 , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.MaxWeight()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MaxWeight"]` → `BRIDGE CONTRACT -> IApiBridge.MaxWeight`

**Pascal compatibility signature:** `function MaxWeight: Word;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MaxWeight()
```

---

## `UO.MenuHookPresent`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если есть ожидающие хуки меню, установленные через AutoMenu , иначе False . Хук меню потребляется при получении соответствующего меню от сервера. Возвращает False , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.MenuHookPresent()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MenuHookPresent"]` → `BRIDGE CONTRACT -> IApiBridge.MenuHookPresent`

**Pascal compatibility signature:** `function MenuHookPresent: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MenuHookPresent()
```

---

## `UO.MenuPresent`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если серверное меню в данный момент отображено (ожидает ответа), иначе False . Возвращает False , если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.MenuPresent()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MenuPresent"]` → `BRIDGE CONTRACT -> IApiBridge.MenuPresent`

**Pascal compatibility signature:** `function MenuPresent: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MenuPresent()
```

---

## `UO.MFGI`

### Manifest-registered overloads

- `UO.MFGI() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.MFGI()`
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
VAR result = UO.MFGI()
```

```basic
UO.MFGI()
```

---

## `UO.MobileCanBeRenamed`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает True , если указанный мобайл может быть переименован (например, пет или фолловер), иначе False . MobID — ID мобайла для проверки. Метод проверяет как флаг мобайла, так и флаг возможности переименования объекта. Возвращает False , если объект не существует, не является мобайлом или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.MobileCanBeRenamed(MobID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MobileCanBeRenamed"]` → `BRIDGE CONTRACT -> IApiBridge.CanChangeName`

**Pascal compatibility signature:** `function MobileCanBeRenamed(MobID: Cardinal): Boolean;`

### Parameters

- `MobID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MobileCanBeRenamed(self)
```

---

## `UO.Morph`

### Direct runtime overloads

- `UO.Morph(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Morph(arg1:Integer) -> Unit`
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
UO.Morph(0)
```

```basic
UO.Morph(0)
```

---

## `UO.Mount`

### Manifest-registered overloads

- `UO.Mount() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.Mount(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.Mount()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.Mount(mount)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `mount` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Mount()
```

```basic
UO.Mount(0)
```

---

## `UO.Move`

### Direct runtime overloads

- `UO.Move() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Move()
```

---

## `UO.moveBetweenTwoCorners`

### Current Yoko signatures / Return

- `UO.moveBetweenTwoCorners() -> Integer`
- `UO.moveBetweenTwoCorners(value) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** `1` when enabled, `0` when disabled. The setter form returns the resulting state.

### Parameters

- `value` — Boolean/integer flag (`0` = disabled, non-zero = enabled).

### Behavior

Controls whether the ClassicUO pathfinder may take a diagonal step **between two blocked side/corner cells**. The option is now passed into `Pathfinder.WalkTo` and evaluated separately from `moveThroughCorner`.

- `moveThroughCorner` controls a diagonal when **one** adjacent side is blocked.
- `moveBetweenTwoCorners` controls a diagonal when **both** adjacent sides are blocked.

### Notes / limitations

The destination tile itself must still be walkable. Server corrections or shard-specific movement rules may still reject a locally planned step.

### Examples

```basic
UO.moveBetweenTwoCorners(1)
VAR enabled = UO.moveBetweenTwoCorners()
```
---

## `UO.MoveBoat`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Управляет лодкой, которой правит персонаж, через пакетное HS-управление (тот же механизм, что и управление мышью в официальном клиенте; пакет 0xBF, субкоманда 0x33). Direction — абсолютное мировое направление (0–7): 0 — север, 1 — северо-восток, 2 — восток, 3 — юго-восток, 4 — юг, 5 — юго-запад, 6 — запад, 7 — северо-запад. Сервер сам разворачивает лодку, если запрошенное направление отличается от текущего курса — отдельная команда «поворот» не нужна. Speed : 0 — стоп, 1 — медленно, 2 — быстро. Значения больше 2 обрезаются до 2. Лодка продолжает плыть в заданном направлении, пока не будет вызван StopBoat (или MoveBoat(dir, 0) ), не сменится направление или лодка не упрётся в препятствие. Метод работает только при выполнении условий: Версия клиента в профиле 7.0.9.0 или выше (High Seas). На более старой версии вызов лишь пишет предупреждение в системный журнал. Шард поддерживает HS-управление мышью. На OSI и ServUO-шардах персонаж должен сначала взять штурвал (pilot-режим — двойной клик по штурвалу / контекстное меню). Шарды на ModernUO этот пакет не реализуют вовсе (лодки там управляются только речевыми командами).

### Current Yoko signatures / Return

- `UO.MoveBoat(Direction, Speed)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MoveBoat"]` → `BRIDGE CONTRACT -> IApiBridge.MoveBoat`

**Pascal compatibility signature:** `procedure MoveBoat(Direction, Speed : Byte);`

### Parameters

- `Direction` — Ultima Online movement/facing direction value.
- `Speed` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.MoveBoat(0, 0)
```

---

## `UO.moveCheckStamina`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Задаёт минимальный порог stamina для любого шага перемещения. Если текущая stamina персонажа ниже этого значения, шаги приостанавливаются до восстановления. Значение по умолчанию: 1 . Значение 0 полностью отключает проверку stamina. В Python используйте GetMoveCheckStamina() / SetMoveCheckStamina(value) .

### Current Yoko signatures / Return

- `UO.moveCheckStamina()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveCheckStamina"]` → `STATE -> InjectionApiState.MoveCheckStamina`
- `UO.moveCheckStamina(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveCheckStamina"]` → `STATE -> InjectionApiState.MoveCheckStamina`

**Pascal compatibility signature:** `var moveCheckStamina: Integer;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.moveCheckStamina()
```

```basic
UO.moveCheckStamina('value')
```

---

## `UO.moveExitOnDisconnect`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Управляет немедленным прерыванием перемещения при отключении персонажа. Когда True , методы MoveXY , Step , StepQ , newMoveXY немедленно возвращают результат неудачи при отключении. Когда False , они ожидают восстановления соединения (например, через автопереподключение) перед продолжением. Значение по умолчанию: зависит от настроек профиля. Переменная доступна только в Pascal (DWS + PascalScript). В Python система перемещения безусловно ставится на паузу при отключении ( while not Connected(): Wait(100) ), поэтому getter/setter не нужен.

### Current Yoko signatures / Return

- `UO.moveExitOnDisconnect()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveExitOnDisconnect"]` → `STATE -> InjectionApiState.MoveExitOnDisconnect`
- `UO.moveExitOnDisconnect(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveExitOnDisconnect"]` → `STATE -> InjectionApiState.MoveExitOnDisconnect`

**Pascal compatibility signature:** `var moveExitOnDisconnect: Boolean;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.moveExitOnDisconnect()
```

```basic
UO.moveExitOnDisconnect('value')
```

---

## `UO.moveHeuristicMult`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Множитель эвристической функции в алгоритме поиска пути A*. Большие значения заставляют поиск пути предпочитать более прямые маршруты (жадное поведение) ценой возможного пропуска коротких обходных путей. Меньшие значения дают более тщательный, но медленный поиск. Значение по умолчанию: 93 . В Python используйте GetMoveHeuristicMult() / SetMoveHeuristicMult(value) .

### Current Yoko signatures / Return

- `UO.moveHeuristicMult()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveHeuristicMult"]` → `STATE -> InjectionApiState.MoveHeuristicMultiplier`
- `UO.moveHeuristicMult(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveHeuristicMult"]` → `STATE -> InjectionApiState.MoveHeuristicMultiplier`

**Pascal compatibility signature:** `var moveHeuristicMult: Integer;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.moveHeuristicMult()
```

```basic
UO.moveHeuristicMult('value')
```

---

## `UO.MoveItem`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Перемещает предмет в указанный контейнер или на землю. Объединяет DragItem + DropItem в один вызов. ObjID — ID предмета для перемещения. Count — количество предметов из стопки. 0 — вся стопка. MoveIntoID — ID контейнера-получателя, или 0 для сброса на землю. X , Y , Z — координаты внутри контейнера или мировые координаты при сбросе на землю. 0, 0, 0 для размещения по умолчанию. Возвращает True при успешном перемещении, False — в противном случае.

### Current Yoko signatures / Return

- `UO.MoveItem(ObjID, Count, MoveIntoID, X, Y, Z)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MoveItem"]` → `BRIDGE CONTRACT -> IApiBridge.Backpack` → `BRIDGE CONTRACT -> IApiBridge.MoveItem`

**Pascal compatibility signature:** `function MoveItem(ObjID: Cardinal; Count: Integer; MoveIntoID: Cardinal; X: Integer; Y: Integer; Z: ShortInt): Boolean;`

### Additional current runtime overloads

- `UO.MoveItem(arg1:Any, arg2:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.MoveItem(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.MoveItem(arg1:Any, arg2:Any, arg3:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Count` — Quantity/count. 0 may mean all/default only where explicitly supported.
- `MoveIntoID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `Z` — World/tile Z coordinate.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MoveItem(self, 1, self, UO.GetX(self), UO.GetY(self), UO.GetZ(self))
```

```basic
VAR result = UO.MoveItem(0, 0, 0)
```

---

## `UO.MoveItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Перемещает все предметы с указанным типом и цветом из контейнера-источника в контейнер-получатель. Container — ID контейнера-источника. ItemsType — графический тип для поиска. $FFFF — любой тип. ItemsColor — цвет для поиска. $FFFF — любой цвет. MoveIntoID — ID контейнера-получателя, или 0 для сброса на землю. X , Y , Z — координаты внутри контейнера-получателя или мировые координаты. 0, 0, 0 для размещения по умолчанию. DelayMS — задержка в миллисекундах между перемещением каждого предмета. В Python дополнительно поддерживается необязательный параметр max_count (по умолчанию 0 = переместить все). Возвращает True , если хотя бы один предмет был перемещён, False — в противном случае.

### Current Yoko signatures / Return

- `UO.MoveItems(Container, ItemsType, ItemsColor, MoveIntoID, X, Y, Z, DelayMS)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MoveItems"]` → `BRIDGE CONTRACT -> IApiBridge.MoveItems`

**Pascal compatibility signature:** `function MoveItems(Container: Cardinal; ItemsType: Word; ItemsColor: Word; MoveIntoID: Cardinal; X: Integer; Y: Integer; Z: ShortInt; DelayMS: Integer): Boolean;`

### Parameters

- `Container` — Container serial or a runtime container sentinel such as backpack/ground, according to the command contract.
- `ItemsType` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `ItemsColor` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `MoveIntoID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.
- `Z` — World/tile Z coordinate.
- `DelayMS` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MoveItems(backpack, 0x0190, -1, self, UO.GetX(self), UO.GetY(self), UO.GetZ(self), 1000)
```

---

## `UO.MoveOff`

### Direct runtime overloads

- `UO.MoveOff() -> Unit`
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
UO.MoveOff()
```

---

## `UO.MoveOn`

### Direct runtime overloads

- `UO.MoveOn() -> Unit`
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
UO.MoveOn()
```

---

## `UO.moveOpenDoor`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Управляет автоматическим открытием дверей системой перемещения ( MoveXY , MoveXYZ , StepQ , newMoveXY ). Когда True , мувер пытается использовать (открыть) дверь, блокирующую следующий тайл. До 3 попыток; если дверь остаётся — тайл помечается как непроходимый через SetBadLocation и путь пересчитывается. Значение по умолчанию: False . В Python используйте GetMoveOpenDoor() / SetMoveOpenDoor(value) .

### Current Yoko signatures / Return

- `UO.moveOpenDoor()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveOpenDoor"]` → `STATE -> InjectionApiState.MoveOpenDoor`
- `UO.moveOpenDoor(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveOpenDoor"]` → `STATE -> InjectionApiState.MoveOpenDoor`

**Pascal compatibility signature:** `var moveOpenDoor: Boolean;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.moveOpenDoor()
```

```basic
UO.moveOpenDoor('value')
```

---

## `UO.MoverStop`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Останавливает текущее перемещение персонажа, инициированное MoveXY , MoveXYZ или newMoveXY . Метод перемещения вернёт False после этого вызова. В Pascal и Python этот метод может быть вызван из обработчика событий (см. SetEventProc ). В Python также может быть вызван из отдельного потока внутри скрипта.

### Current Yoko signatures / Return

- `UO.MoverStop()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MoverStop"]` → `BRIDGE CONTRACT -> IApiBridge.StopMoving`

**Pascal compatibility signature:** `procedure MoverStop;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.MoverStop()
```

---
