# Runtime API Manual — Part 27

Commands: **SetARStatus** through **SetJournalLine**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.SetARStatus`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Включает или отключает автоматическое переподключение для текущего персонажа. Value — True для включения, False для отключения. При включении Stealth автоматически пытается переподключиться после отключения, используя таймер переподключения из профиля (параметр ReconnectTime в настройках профиля). Расширенные параметры настраиваются через SetARExtParams . Используйте GetARStatus для чтения текущего состояния. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.SetARStatus(Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetARStatus"]` → `BRIDGE CONTRACT -> IApiBridge.SetAutoReconnect`

**Pascal compatibility signature:** `procedure SetARStatus(Value: Boolean);`

### Parameters

- `Value` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetARStatus('value')
```

---

## `UO.SetAutoBuyDelay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает задержку (в миллисекундах) между автоматическими покупками, запускаемыми AutoBuy / AutoBuyEx . Value — задержка в миллисекундах. Когда система автопокупки обрабатывает списки покупок у NPC-торговца, эта задержка применяется между отдельными операциями покупки для предотвращения flood-защиты сервера. Используйте GetAutoBuyDelay для чтения текущего значения.

### Current Yoko signatures / Return

- `UO.SetAutoBuyDelay(Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetAutoBuyDelay"]` → `STATE -> InjectionApiState.AutoBuyDelay` → `BRIDGE CONTRACT -> IApiBridge.SetAutoBuyDelay`

**Pascal compatibility signature:** `procedure SetAutoBuyDelay(Value: Word);`

### Parameters

- `Value` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetAutoBuyDelay('value')
```

---

## `UO.SetAutoSellDelay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает задержку (в миллисекундах) между автоматическими продажами, запускаемыми AutoSell . Value — задержка в миллисекундах. Когда система автопродажи обрабатывает списки продажи у NPC-торговца, эта задержка применяется между отдельными операциями продажи для предотвращения flood-защиты сервера. Используйте GetAutoSellDelay для чтения текущего значения.

### Current Yoko signatures / Return

- `UO.SetAutoSellDelay(Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetAutoSellDelay"]` → `STATE -> InjectionApiState.AutoSellDelay` → `BRIDGE CONTRACT -> IApiBridge.SetAutoSellDelay`

**Pascal compatibility signature:** `procedure SetAutoSellDelay(Value: Word);`

### Parameters

- `Value` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetAutoSellDelay('value')
```

---

## `UO.SetBadLocation`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Помечает тайл карты как непроходимый для системы поиска пути. X — горизонтальная координата карты. Y — вертикальная координата карты. После вызова этого метода система поиска пути ( MoveXY , MoveXYZ , GetPathArray , GetPathArray3D ) будет считать указанный тайл заблокированным и прокладывать маршрут в обход. Полезно для пометки тайлов, которые технически проходимы, но содержат препятствия, не распознаваемые стандартным поиском пути (например, объекты кастомных шардов, тайлы с NPC или ловушки). Используйте ClearBadLocationList для очистки всего списка заблокированных локаций. Не выполняет действий, если персонаж не подключён или данные UO не загружены.

### Current Yoko signatures / Return

- `UO.SetBadLocation(X, Y)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetBadLocation"]` → `STATE -> InjectionApiState.BadLocations`

**Pascal compatibility signature:** `procedure SetBadLocation(X: Word; Y: Word);`

### Parameters

- `X` — World/tile X coordinate.
- `Y` — World/tile Y coordinate.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetBadLocation(UO.GetX(self), UO.GetY(self))
```

---

## `UO.SetBadObject`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Помечает объекты заданного типа и цвета как непроходимые в указанном радиусе для системы поиска пути. ObjType — graphic (тип) блокируемого объекта. $FFFF — любой тип. Color — цвет блокируемого объекта. $FFFF — любой цвет. Radius — радиус (в тайлах) вокруг объекта, в пределах которого тайлы считаются заблокированными. После вызова тайлы, занятые совпадающими объектами, будут считаться непроходимыми системой поиска пути ( MoveXY , MoveXYZ , GetPathArray , GetPathArray3D ). Полезно для обхода определённых мировых объектов, технически проходимых, но требующих обхода (например, энергетические поля, огненные поля). Используйте ClearBadObjectList для очистки всего списка заблокированных объектов. Не выполняет действий, если персонаж не подключён или данные UO не загружены.

### Current Yoko signatures / Return

- `UO.SetBadObject(ObjType, Color, Radius)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetBadObject"]` → `STATE -> InjectionApiState.BadObjects`

**Pascal compatibility signature:** `procedure SetBadObject(ObjType: Word; Color: Word; Radius: Byte);`

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `Radius` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetBadObject(0x0190, -1, 18)
```

---

## `UO.SetCatchBag`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Назначает контейнер в качестве «catch bag» — все предметы, получаемые персонажем (добыча, обмен и т.д.), автоматически перемещаются в этот контейнер. ObjID — serial (ID) контейнера. Передайте 0 для сброса catch bag (эквивалент вызова UnsetCatchBag ). Возвращает: Значение Смысл 0 Catch bag сброшен (ObjID = 0), или ошибка (персонаж не подключён, объект не найден или не является контейнером) 1 Catch bag установлен успешно Указанный объект должен существовать и быть контейнером. Если объект не найден или не является контейнером, catch bag не устанавливается и возвращается 0 .

### Current Yoko signatures / Return

- `UO.SetCatchBag(ObjID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetCatchBag"]`

**Pascal compatibility signature:** `function SetCatchBag(ObjID: Cardinal): Byte;`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.SetCatchBag(self)
```

---

## `UO.SetContextMenuHook`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает перехватчик, который автоматически выбирает указанный пункт из любого полученного контекстного меню для заданного объекта. MenuID — serial (ID) объекта, контекстное меню которого перехватывается. EntryNumber — индекс пункта контекстного меню (с нуля), который будет автоматически выбран. При получении контекстного меню для совпадающего объекта указанный пункт автоматически выбирается и отправляется серверу, как если бы игрок по нему кликнул. Перехватчик остаётся активным и срабатывает при каждом совпадающем контекстном меню — он не сбрасывается после первого использования. Чтобы сменить объект или пункт, вызовите SetContextMenuHook повторно; чтобы отключить — вызовите SetContextMenuHook(0, 0) . Используйте RequestContextMenu для вызова контекстного меню после установки перехватчика.

### Current Yoko signatures / Return

- `UO.SetContextMenuHook(MenuID, EntryNumber)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetContextMenuHook"]` → `BRIDGE CONTRACT -> IApiBridge.SetContextMenuHook`

**Pascal compatibility signature:** `procedure SetContextMenuHook(MenuID: Cardinal; EntryNumber: Byte);`

### Parameters

- `MenuID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `EntryNumber` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetContextMenuHook(self, 0)
```

---

## `UO.SetDefault`

### Manifest-registered overloads

- `UO.SetDefault(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.SetDefault(name, object)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `name` — String/text value interpreted according to the command.
- `object` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.SetDefault(0, 0)
```

```basic
UO.SetDefault('value', self)
```

---

## `UO.SetDress`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Сохраняет текущий набор экипировки персонажа как «dress set» (набор одежды/экипировки). Фиксирует все предметы, экипированные на персонаже во всех действующих слоях экипировки, и сохраняет их как активную конфигурацию одежды. Сохранённый набор может быть впоследствии заново надет с помощью методов Equip или EquipItems после снятия экипировки. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.SetDress()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetDress"]`

**Pascal compatibility signature:** `procedure SetDress;`

### Additional current runtime overloads

- `UO.SetDress(arg1:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetDress()
```

```basic
UO.SetDress(0)
```

---

## `UO.SetDressSpeed`

### Direct runtime overloads

- `UO.SetDressSpeed(arg1:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetDressSpeed(0)
```

---

## `UO.SetEasyUO`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Записывает значение в общий реестр EasyUO (только Windows). num — номер ключа (целое число). Regvalue — строковое значение для записи. Метод записывает в реестр Windows по пути HKEY_CURRENT_USER\Software\EasyUO , используя ключ * . Обеспечивает обмен данными со скриптами EasyUO через общее хранилище в реестре. Используйте GetEasyUO для чтения значений из того же реестра. Только Windows. На остальных платформах метод ничего не делает.

### Current Yoko signatures / Return

- `UO.SetEasyUO(num, Regvalue)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.SetEasyUO"]`

**Pascal compatibility signature:** `procedure SetEasyUO(num: Integer; Regvalue: String);`

### Parameters

- `num` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Regvalue` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetEasyUO(0, 'value')
```

---

## `UO.SetEvent`

### Direct runtime overloads

- `UO.SetEvent(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetEvent(arg1:Any, arg2:Any, arg3:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetEvent(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetEvent(0, 0)
```

```basic
UO.SetEvent(0, 0, 0)
```

```basic
UO.SetEvent(0, 0, 0, 0)
```

---

## `UO.SetEventProc`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Регистрирует (или снимает) процедуру скрипта как обработчик определённого игрового события. Eventname — тип события, TPacketEvent . Procname — имя процедуры в скрипте для вызова при наступлении события. Передайте пустую строку '' для снятия обработчика. Если обработчик уже назначен — выводится предупреждение. Сначала снимите старый: SetEventProc(event, '') , затем установите новый. Ряд устаревших имён событий вызывает предупреждение (см. таблицу выше). В Python типы событий доступны как члены перечисления EventType (автоимпорт), второй параметр принимает ссылку на функцию или None для снятия. Полный список типов событий, сигнатуры обработчиков и описание параметров callback-ов — в мануале по событиям .

### Current Yoko signatures / Return

- `UO.SetEventProc(Eventname, Procname)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetEventProc"]`

**Pascal compatibility signature:** `procedure SetEventProc(Eventname: TPacketEvent; Procname: String);`

### Parameters

- `Eventname` — String/text value interpreted according to the command.
- `Procname` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetEventProc('value', 'value')
```

---

## `UO.SetGlobal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает значение глобальной переменной в указанной области видимости. GlobalRegion — область видимости переменной: 'stealth' для глобальных переменных Stealth (общих для всех персонажей и скриптов), или 'char' для переменных конкретного персонажа. VarName — имя переменной (регистронезависимое). VarValue — строковое значение для сохранения. Глобальные переменные сохраняются в течение сессии Stealth и считываются через GetGlobal . Обычно используются для межскриптового обмена данными: один скрипт устанавливает значение, другой читает. В Python параметр GlobalRegion — это int (не строка): используйте соответствующую константу.

### Current Yoko signatures / Return

- `UO.SetGlobal(GlobalRegion, VarName, VarValue)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetGlobal"]` → `STATE -> InjectionApiState.GlobalVariables`

**Pascal compatibility signature:** `procedure SetGlobal(GlobalRegion: String; VarName: String; VarValue: String);`

### Additional current runtime overloads

- `UO.SetGlobal(arg1:String, arg2:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetGlobal(arg1:String, arg2:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetGlobal(arg1:String, arg2:Decimal) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `GlobalRegion` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `VarName` — String/text value interpreted according to the command.
- `VarValue` — String/text value interpreted according to the command.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetGlobal(0, 'value', 'value')
```

```basic
UO.SetGlobal(0, 0)
```

---

## `UO.SetGump`

### Direct runtime overloads

- `UO.SetGump(arg1:Any, arg2:Any, arg3:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.SetGump(arg1:Any, arg2:Any, arg3:Any, arg4:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetGump(0, 0, 0)
```

```basic
UO.SetGump(0, 0, 0, 0)
```

---

## `UO.SetJournalLine`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Заменяет текст записи журнала по указанному индексу. StringIndex — индекс (с нуля) строки журнала для изменения. Должен быть неотрицательным; отрицательные значения игнорируются. Text — новый текст записи журнала. Изменяет данные журнала только в памяти. Не влияет на серверный журнал, журнал в UO-клиенте, подключённом к Stealth, и любое другое внешнее отображение — только на локальный буфер, используемый Journal , InJournal и связанными методами внутри скрипта. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.SetJournalLine(StringIndex, Text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["SetJournalLine"]` → `BRIDGE CONTRACT -> IApiBridge.SetJournalLine`

**Pascal compatibility signature:** `procedure SetJournalLine(StringIndex: Integer; Text: String);`

### Additional current runtime overloads

- `UO.SetJournalLine(arg1:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `StringIndex` — String/text value interpreted according to the command.
- `Text` — String/text value interpreted according to the command.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.SetJournalLine('value', 'value')
```

```basic
UO.SetJournalLine(0)
```

---
