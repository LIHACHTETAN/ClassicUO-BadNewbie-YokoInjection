# Runtime API Manual — Part 02

Commands: **AddUserStatic** through **BookSetText**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.AddUserStatic`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Добавляет пользовательский статик-объект в данные шарда и возвращает его индекс. Индекс может быть использован для удаления через RemoveUserStatic . Пользовательские статики ведут себя точно так же, как обычные статики шарда при расчёте пути и шагов. Это полезно, когда область заблокирована динамическими объектами (например, заборами), о которых pathfinder не знает заранее. Добавив эти объекты как пользовательские статики, pathfinder учтёт их с самого начала. Важно: Пользовательские статики добавляются в данные шарда , а не к конкретному персонажу. Они будут применяться ко всем персонажам, использующим те же файлы шарда. Пользовательские статики не очищаются при отключении. Используйте ClearUserStatics для их удаления. Возвращает -1 при ошибке. В Python метод называется CreateUserStatic + есть синоним AddUserStatic с набором параметров.

### Current Yoko signatures / Return

- `UO.AddUserStatic(StaticItem, WorldNum)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddUserStatic"]` → `STATE -> InjectionApiState.NextUserStaticId` → `STATE -> InjectionApiState.UserStatics` → `BRIDGE CONTRACT -> IApiBridge.GetX` → `BRIDGE CONTRACT -> IApiBridge.GetY` → `BRIDGE CONTRACT -> IApiBridge.GetZ`

**Pascal compatibility signature:** `function AddUserStatic(const StaticItem: TStaticItem; WorldNum: Byte): Integer;`

### Additional current runtime overloads

- `UO.AddUserStatic(arg1, arg2, arg3, arg4, arg5, arg6) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `StaticItem` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `WorldNum` — Map/facet identifier. Tile/static APIs are limited to the currently loaded ClassicUO map unless stated otherwise.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg6` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AddUserStatic(self, 0)
```

```basic
VAR result = UO.AddUserStatic(0, 0, 0, 0, 0, 0)
```

---

## `UO.Alarm`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Вызывает визуальную тревогу: иконка Stealth в системном трее начинает мигать красным. Мигание продолжается до тех пор, пока пользователь не нажмёт на иконку Stealth в трее, что сбросит тревогу. Полезно для уведомления пользователя о критических игровых событиях (смерть, атака, мало здоровья и т. д.), когда он не за экраном.

### Current Yoko signatures / Return

- `UO.Alarm()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Alarm"]`

**Pascal compatibility signature:** `procedure Alarm;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Alarm()
```

---

## `UO.Alive`

### Direct runtime overloads

- `UO.Alive() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer Boolean (1/0). No-argument getter reads self/current client state; serial overloads read the requested loaded mobile/object where registered.
- `UO.Alive(serial:Integer) -> Integer`
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
VAR result = UO.Alive()
```

```basic
VAR result = UO.Alive(self)
```

---

## `UO.AlwaysRun`

### Direct runtime overloads

- `UO.AlwaysRun() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.AlwaysRun(arg1:Integer) -> Unit`
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
VAR result = UO.AlwaysRun()
```

```basic
UO.AlwaysRun(0)
```

---

## `UO.ApiNameExists`

### Direct runtime overloads

- `UO.ApiNameExists(arg1:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ApiNameExists(0)
```

---

## `UO.ApiParameterExists`

### Direct runtime overloads

- `UO.ApiParameterExists(arg1:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ApiParameterExists(0)
```

---

## `UO.ApiSignatureExists`

### Direct runtime overloads

- `UO.ApiSignatureExists(arg1:String, arg2:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ApiSignatureExists(0, 0)
```

---

## `UO.Arm`

### Direct runtime overloads

- `UO.Arm(arg1:String) -> Unit`
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
UO.Arm(0)
```

---

## `UO.Armor`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает значение физической брони персонажа (свойство «Armor», отображаемое в статусе персонажа). Возвращает 0 , если персонаж не подключён к серверу UO.

### Current Yoko signatures / Return

- `UO.Armor()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Armor"]` → `BRIDGE CONTRACT -> IApiBridge.Armor`

**Pascal compatibility signature:** `function Armor: SmallInt;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or changes the requested mobile/player stat/state through the current ClassicUO world model and registered API bridge.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Armor()
```

---

## `UO.Attack`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Атакует мобайла с указанным ObjID . Если персонаж не находится в режиме War, Stealth автоматически включит его перед отправкой команды атаки. Если ObjID равен 0 или объект не существует, метод ничего не делает.

### Current Yoko signatures / Return

- `UO.Attack(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Attack"]` → `BRIDGE CONTRACT -> IApiBridge.Attack`

**Pascal compatibility signature:** `procedure Attack(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.Attack(self)
```

---

## `UO.AttackNearest`

### Direct runtime overloads

- `UO.AttackNearest(notoriety) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.AttackNearest(notoriety, distance) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.AttackNearest(notoriety, distance, body) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.AttackNearest(notoriety, distance, body, maxZ) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.AttackNearest(notoriety, distance, body, maxZ, nearest) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.AttackNearest(notoriety, distance, body, maxZ, nearest, color) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.AttackNearest(notoriety, distance, body, maxZ, nearest, color, classMask) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `notoriety` — Actual ClassicUO Mobile.Notoriety value or supported mask/string form; it is not inferred from hue/name/body.
- `distance` — Distance/radius in tiles. Explicit distance overrides the shared FindDistance state for overloads that provide it.
- `body` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `maxZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.
- `nearest` — Boolean ordering flag. TRUE selects/orders nearest matches first; FALSE preserves the runtime search order.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `classMask` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the shared Search Core to select a matching mobile, then issues the ClassicUO attack action for the selected serial.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AttackNearest(5)
```

```basic
VAR result = UO.AttackNearest(5, 18, 0x0190, 12, TRUE, -1, 'value')
```

---

## `UO.AutoBuy`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает автоматический хук для покупки у вендоров. Когда от вендора приходит список покупки (или если он уже открыт), Stealth автоматически купит предметы, соответствующие указанному типу и цвету. Хук постоянный — он остаётся активным, пока не будет явно удалён вызовом AutoBuy с Quantity = 0 . Для удаления всех хуков покупки/продажи используйте ClearShopList . Для более гибкой фильтрации (по цене и имени) используйте AutoBuyEx .

### Current Yoko signatures / Return

- `UO.AutoBuy(ItemType, ItemColor, Quantity)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AutoBuy"]` → `BRIDGE CONTRACT -> IApiBridge.SetAutoBuyRule`

**Pascal compatibility signature:** `procedure AutoBuy(ItemType: Word; ItemColor: Word; Quantity: Word);`

### Parameters

- `ItemType` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `ItemColor` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Quantity` — Quantity/count. 0 may mean all/default only where explicitly supported.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AutoBuy(0x0190, -1, 1)
```

---

## `UO.AutoBuyEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Расширенная версия AutoBuy с дополнительной фильтрацией по цене и имени предмета. Устанавливает автоматический хук для покупки у вендоров. Когда от вендора приходит список покупки (или если он уже открыт), Stealth автоматически купит предметы, соответствующие всем указанным критериям. Хук постоянный — он остаётся активным, пока не будет явно удалён вызовом AutoBuy с Quantity = 0 .

### Current Yoko signatures / Return

- `UO.AutoBuyEx(ItemType, ItemColor, Quantity, Price, Name)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AutoBuyEx"]` → `BRIDGE CONTRACT -> IApiBridge.SetAutoBuyRule`

**Pascal compatibility signature:** `procedure AutoBuyEx(ItemType: Word; ItemColor: Word; Quantity: Word; Price: Cardinal; Name: String);`

### Parameters

- `ItemType` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `ItemColor` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Quantity` — Quantity/count. 0 may mean all/default only where explicitly supported.
- `Price` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Name` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AutoBuyEx(0x0190, -1, 1, 0, 'value')
```

---

## `UO.AutoMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает многоразовую ловушку на меню. Работает так же, как WaitMenu , но хук постоянный — он срабатывает каждый раз при появлении подходящего меню, пока не будет явно удалён через CancelMenu . Когда заголовок входящего меню содержит MenuCaption , а в меню есть элемент, содержащий ElementCaption , этот элемент выбирается автоматически. Для одноразовой ловушки используйте WaitMenu . Для удаления всех хуков используйте CancelMenu .

### Current Yoko signatures / Return

- `UO.AutoMenu(MenuCaption, ElementCaption)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `LEGACY DISPATCH -> InjectionApiUO.ExecuteLegacyCommand["AutoMenu"]`

**Pascal compatibility signature:** `procedure AutoMenu(MenuCaption: String; ElementCaption: String);`

### Parameters

- `MenuCaption` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `ElementCaption` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AutoMenu(0, 0)
```

---

## `UO.AutoSell`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает автоматический хук для продажи вендорам. Когда от вендора приходит список продажи (или если он уже открыт), Stealth автоматически продаст предметы, соответствующие указанному типу и цвету. Хук постоянный — он остаётся активным, пока не будет явно удалён вызовом AutoSell с Quantity = 0 . Для удаления всех хуков покупки/продажи используйте ClearShopList .

### Current Yoko signatures / Return

- `UO.AutoSell(ItemType, ItemColor, Quantity)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AutoSell"]` → `BRIDGE CONTRACT -> IApiBridge.SetAutoSellRule`

**Pascal compatibility signature:** `procedure AutoSell(ItemType: Word; ItemColor: Word; Quantity: Word);`

### Parameters

- `ItemType` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `ItemColor` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `Quantity` — Quantity/count. 0 may mean all/default only where explicitly supported.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AutoSell(0x0190, -1, 1)
```

---

## `UO.Backpack`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает ID рюкзака текущего персонажа. Возвращает 0 , если персонаж не подключён к серверу UO. ID рюкзака часто используется как параметр Container для методов поиска и манипуляции предметами, таких как FindType , FindTypeEx , MoveItem и Count .

### Current Yoko signatures / Return

- `UO.Backpack()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Backpack"]` → `BRIDGE CONTRACT -> IApiBridge.Backpack`

**Pascal compatibility signature:** `function Backpack: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Backpack()
```

---

## `UO.BandageSelf`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Пытается использовать бинты на текущем персонаже. Метод ищет бинты (тип $0E21 ) в рюкзаке персонажа и, если находит, использует их с целью на самого себя. Если бинты не найдены, метод записывает сообщение об ошибке в системный журнал: "BandageSelf error: Bandages not found." . Примечание: Работает только с версией клиента 5.0.4 и выше.

### Current Yoko signatures / Return

- `UO.BandageSelf()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["BandageSelf"]` → `BRIDGE CONTRACT -> IApiBridge.Self` → `BRIDGE CONTRACT -> IApiBridge.UseType` → `BRIDGE CONTRACT -> IApiBridge.WaitTargetObject`

**Pascal compatibility signature:** `procedure BandageSelf;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.BandageSelf()
```

---

## `UO.BookClearText`

### Current Yoko signatures / Return

- `UO.BookClearText() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Clears the Yoko book buffer and, when an editable book is open, sends empty content for its pages.

### Parameters

- None.

### Behavior

Clears all pages of the currently open editable ClassicUO book through the same real page-update packet path used by `BookSetPageText`.

### Notes / limitations

A writable book must be open for a server-side book change. With no open book, only the compatibility buffer can be cleared and an error is reported for the missing live target.

### Examples

```basic
UO.BookClearText()
```
---

## `UO.BookGetPageText`

### Current Yoko signatures / Return

- `UO.BookGetPageText(Page) -> String`
  - **Return type:** `String`
  - **Return contract:** Text of the requested 1-based page; empty string is valid for an empty/unavailable page.

### Parameters

- `Page` — 1-based page number.

### Behavior

Reads page text from the currently open `ModernBookGump` first. If no live page text is available, the Yoko compatibility buffer is used as a fallback.

### Notes / limitations

The server may not have delivered every book page yet. Opening/navigating the book can cause ClassicUO to request missing page data.

### Examples

```basic
VAR page1 = UO.BookGetPageText(1)
UO.Print(page1)
```
---

## `UO.BookSetHeader`

### Current Yoko signatures / Return

- `UO.BookSetHeader(Title, Author) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. On a valid editable open book, ClassicUO immediately sends the real book-header update packet.

### Parameters

- `Title` — new book title.
- `Author` — new book author.

### Behavior

Finds the currently open `ModernBookGump`, verifies that it is editable, updates the visible title/author controls and sends `Send_BookHeaderChanged` (or the old-protocol header packet when required by the client version).

### Notes / limitations

- A writable book must already be open.
- Read-only books and missing book windows are rejected with a runtime error message and no packet is sent.
- Server rules remain authoritative and may reject an otherwise valid client request.

### Examples

```basic
UO.BookSetHeader('Field Notes', 'LIHACH')
```
---

## `UO.BookSetPageText`

### Current Yoko signatures / Return

- `UO.BookSetPageText(Page, Text) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. A valid editable page is updated locally and sent to the server with a real book-page packet.

### Parameters

- `Page` — 1-based page number.
- `Text` — page text. Newlines split the text into book lines.

### Behavior

Writes a page into the currently open editable `ModernBookGump`, updates the page buffer/UI and sends `Send_BookPageData` for that page.

### Notes / limitations

- `Page` must be in `1..BookPageCount`.
- A page is limited to ClassicUO's current book-line capacity (`10` lines, with the current book control's per-line character limit).
- Invalid page, too many/too-long lines, read-only book or no open book results in an error and no page update.

### Examples

```basic
UO.BookSetPageText(1, 'Line one' + Chr(10) + 'Line two')
```
---

## `UO.BookSetText`

### Current Yoko signatures / Return

- `UO.BookSetText(Text) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Accepted text is divided into pages and each page is sent through the real ClassicUO book-page packet path.

### Parameters

- `Text` — full book text. Newlines form lines; form-feed (`Chr(12)`) may be used as an explicit page separator.

### Behavior

Updates the currently open editable book rather than only storing a Yoko-side string. Without explicit form-feed separators, lines are divided automatically into groups of up to ten lines per page. Each affected page is updated locally and sent to the server.

### Notes / limitations

- The text must fit the open book's page count and current per-page/per-line limits.
- A read-only or missing book is not modified.
- Server validation remains authoritative.

### Examples

```basic
UO.BookSetText('First page line 1' + Chr(10) + 'First page line 2')
```
---
