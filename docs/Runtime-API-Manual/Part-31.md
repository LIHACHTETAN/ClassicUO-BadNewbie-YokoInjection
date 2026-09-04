# Runtime API Manual — Part 31

Commands: **Unequip** through **UseSelfPaperdollScroll**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `524c4a06be8a621b5b5e24dabc4795c2c7da682f9c23e0b516f2de0a437ee254`

---

## `UO.Unequip`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Снимает предмет с указанного слоя экипировки и помещает его в рюкзак. Layer — индекс слоя экипировки. См. ConstantsAndEnums для значений слоёв. Вспомогательные методы, возвращающие значения слоёв, вынесены на отдельную страницу: Layers . Возвращает True , если предмет успешно снят, False — если слой пуст или операция не удалась. В Python метод называется UnEquip .

### Current Yoko signatures / Return

- `UO.Unequip(Layer)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Unequip"]` → `BRIDGE CONTRACT -> IApiBridge.Unequip`

**Pascal compatibility signature:** `function Unequip(Layer: Byte): Boolean;`

### Parameters

- `Layer` — Equipment layer name or numeric layer identifier accepted by the runtime overload.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Unequip('Rhand')
```

---

## `UO.UnequipItems`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Снимает несколько экипированных предметов и помещает их в рюкзак. Items — массив serial (ID) объектов для снятия. Возвращает True , если все предметы успешно сняты, False при ошибке или если персонаж не подключён. Несуществующие предметы пропускаются. Задержка между операциями снятия контролируется переменной DressSpeed (ограничена 10–10000 мс). Только DWScript. В PascalScript тип параметра — TCardinalDynArray вместо TArray .

### Current Yoko signatures / Return

- `UO.UnequipItems(Items)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UnequipItems"]` → `BRIDGE CONTRACT -> IApiBridge.GetLayer` → `BRIDGE CONTRACT -> IApiBridge.Unequip`

**Pascal compatibility signature:** `function UnequipItems(Items: TArray ): Boolean;`

### Parameters

- `Items` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.UnequipItems(1000)
```

---

## `UO.UnsetArm`

### Direct runtime overloads

- `UO.UnsetArm(arg1:String) -> Unit`
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
UO.UnsetArm(0)
```

---

## `UO.UnsetCatchBag`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Сбрасывает текущий «catch bag». После вызова предметы, получаемые персонажем, больше не будут автоматически перемещаться в назначенный контейнер. Эквивалентно вызову SetCatchBag(0) .

### Current Yoko signatures / Return

- `UO.UnsetCatchBag()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UnsetCatchBag"]`

**Pascal compatibility signature:** `procedure UnsetCatchBag;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UnsetCatchBag()
```

---

## `UO.UnsetDress`

### Direct runtime overloads

- `UO.UnsetDress(arg1:String) -> Unit`
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
UO.UnsetDress(0)
```

---

## `UO.UnsetReceivingContainer`

### Direct runtime overloads

- `UO.UnsetReceivingContainer() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UnsetReceivingContainer()
```

---

## `UO.UOAMessage`

### Manifest-registered overloads

- `UO.UOAMessage(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.UOAMessage(text)`
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
VAR result = UO.UOAMessage(0)
```

```basic
UO.UOAMessage('value')
```

---

## `UO.UOSay`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет речевое сообщение от персонажа в игровой мир (видимое находящимся поблизости игрокам). Text — текст сообщения. Персонаж должен находиться в игровом мире (после экрана логина). Если персонаж ещё не в игровом мире, логируется отладочное сообщение и вызов игнорируется. Использует цвет речи по умолчанию ( 0 ). Для задания пользовательского цвета используйте UOSayColor . Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.UOSay(Text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UOSay"]`

**Pascal compatibility signature:** `procedure UOSay(Text: String);`

### Parameters

- `Text` — String/text value interpreted according to the command.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UOSay('value')
```

---

## `UO.UOSayColor`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Отправляет речевое сообщение от персонажа в игровой мир с указанным цветом. Text — текст сообщения. Color — значение UO hue для цвета текста. Персонаж должен находиться в игровом мире. Если нет — логируется отладочное сообщение и вызов игнорируется. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.UOSayColor(Text, Color)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UOSayColor"]` → `BRIDGE CONTRACT -> IApiBridge.Say`

**Pascal compatibility signature:** `procedure UOSayColor(Text: String; Color: Word);`

### Parameters

- `Text` — String/text value interpreted according to the command.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UOSayColor('value', -1)
```

---

## `UO.UpdateFigure`

### Current Yoko signatures / Return

- `UO.UpdateFigure(FigureID, Figure) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** `1` when the existing visual figure is updated; `0` when `FigureID` does not exist or the new figure payload is invalid.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.SetMapFigure` -> `WorldMapGump`.

### Parameters

- `FigureID` — ID returned by `UO.AddFigure`.
- `Figure` — replacement Yoko `TMapFigure` adaptation.

Yoko represents the historical `TMapFigure` record as an array (or `|`-separated compatibility string):

`[kind, coord, x1, y1, x2, y2, brushColor, brushStyle, color, worldNum, text]`

- `kind`: `0=fkLine`, `1=fkEllipse`, `2=fkRectangle`, `3=fkDirection`, `4=fkText`.
- `coord`: `0=fcWorld`, `1=fcScreen`.
- `x1,y1,x2,y2`: figure coordinates.
- `brushColor`: historical fill/brush color field.
- `brushStyle`: historical brush-style field (`0=solid`, `1=clear`, etc.).
- `color`: outline/text color in Delphi `TColor` byte order (`0x00BBGGRR`).
- `worldNum`: facet/map index; omitted value defaults to the current world.
- `text`: label text; optional.

### Behavior

Replaces the stored geometry/style/text for an existing figure and the next World Map render uses the updated values.

### Notes / limitations

The same local-only and brush-rendering limitations as `AddFigure` apply. Unknown IDs are not created implicitly; use `AddFigure` to allocate a new ID.

### Examples

```basic
VAR fig = [4, 0, UO.GetX(self), UO.GetY(self), 0, 0, 0, 1, 65535, UO.WorldNum(), 'Updated']
IF UO.UpdateFigure(figureId, fig) = 0 THEN
    UO.Print('Figure not found')
END IF
```

## `UO.UpdateObject`

### Direct runtime overloads

- `UO.UpdateObject(arg1:Any) -> Unit`
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
UO.UpdateObject(0)
```

---

## `UO.UseAbility`

### Direct runtime overloads

- `UO.UseAbility(arg1:String) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
- `UO.UseAbility(arg1:Integer) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.UseAbility(0)
```

```basic
VAR result = UO.UseAbility(0)
```

---

## `UO.UseFromGround`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет объект указанного типа и цвета на земле, затем использует (double-click) его. ObjType — graphic (тип) объекта. $FFFF — любой тип. Color — цвет объекта. $FFFF — любой цвет. Возвращает serial (ID) найденного и использованного объекта, или 0 если подходящий объект на земле не найден. Поиск использует FindTypeEx с Ground в качестве контейнера и InSub = False . Радиус поиска управляется FindDistance и FindVertical . Логирует ошибку в системный журнал, если объект не найден.

### Current Yoko signatures / Return

- `UO.UseFromGround(ObjType, Color)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseFromGround"]` → `BRIDGE CONTRACT -> IApiBridge.FindType` → `BRIDGE CONTRACT -> IApiBridge.UseObject`

**Pascal compatibility signature:** `function UseFromGround(ObjType: Word; Color: Word): Cardinal;`

### Additional current runtime overloads

- `UO.UseFromGround(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.UseFromGround(0x0190, -1)
```

```basic
VAR result = UO.UseFromGround(0)
```

---

## `UO.UseItemOnMobile`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Использует предмет непосредственно на мобайле (цели) без необходимости курсора цели. ItemSerial — serial (ID) используемого предмета. TargetSerial — serial (ID) мобайла-цели. Это однопакетная операция, объединяющая «использование предмета» и «нацеливание на мобайла» в одно действие. Быстрее традиционной последовательности «использовать → нацелить». Требуется версия клиента 5.0.4 или выше. При более старой версии логируется ошибка и вызов игнорируется. Оба объекта (предмет и мобайл-цель) должны существовать, иначе логируется ошибка. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.UseItemOnMobile(ItemSerial, TargetSerial)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseItemOnMobile"]` → `BRIDGE CONTRACT -> IApiBridge.UseObject` → `BRIDGE CONTRACT -> IApiBridge.WaitTargetObject`

**Pascal compatibility signature:** `procedure UseItemOnMobile(ItemSerial: Cardinal; TargetSerial: Cardinal);`

### Parameters

- `ItemSerial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `TargetSerial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UseItemOnMobile(1000, self)
```

---

## `UO.UseObject`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Использует (double-click) указанный объект. ObjID — serial (ID) используемого объекта. Объект должен существовать в мире. Если нет — ошибка логируется в системный журнал и вызов игнорируется. Основной метод взаимодействия с объектами: открытие контейнеров, использование инструментов, активация предметов и т.д. Значение LastObject обновляется ID использованного объекта. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.UseObject(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseObject"]` → `BRIDGE CONTRACT -> IApiBridge.UseObject`

**Pascal compatibility signature:** `procedure UseObject(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UseObject(self)
```

---

## `UO.UseOtherPaperdollScroll`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Открывает скролл статуса персонажа (Character Status, из окна папердолла) для указанного мобайла. ObjID — serial (ID) мобайла. Несмотря на название, этот метод не открывает сам paperdoll — он отправляет пакет «paperdoll scroll», который на разных шардах может открыть текстовое окно со статусом, многостраничный гамп или другой UI, специфичный для шарда. Точный результат зависит от реализации сервера. Мобайл должен существовать в мире. Если нет — логируется ошибка. Для открытия скролла своего персонажа используйте UseSelfPaperdollScroll .

### Current Yoko signatures / Return

- `UO.UseOtherPaperdollScroll(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseOtherPaperdollScroll"]` → `BRIDGE CONTRACT -> IApiBridge.UseObject`

**Pascal compatibility signature:** `procedure UseOtherPaperdollScroll(ObjID: Cardinal);`

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UseOtherPaperdollScroll(self)
```

---

## `UO.UsePrimaryAbility`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Активирует основную способность оружия (primary ability) текущего экипированного оружия. Не выполняет действий, если персонаж не подключён. Используйте GetActiveAbility для проверки текущей активной способности, и IsActiveSpellAbility для проверки активности заклинательной способности.

### Current Yoko signatures / Return

- `UO.UsePrimaryAbility()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UsePrimaryAbility"]` → `BRIDGE CONTRACT -> IApiBridge.UsePrimaryAbility`

**Pascal compatibility signature:** `procedure UsePrimaryAbility;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UsePrimaryAbility()
```

---

## `UO.UseProxy`

### Current Yoko signatures / Return

- `UO.UseProxy() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** `0` means proxy mode is not enabled in the current embedded runtime.

### Parameters

- None.

### Behavior

Compatibility query for proxy mode. The current ClassicUO/Yoko embedded runtime does not expose a separate proxy transport, so this returns `0` rather than pretending the normal game connection is a proxy.

### Notes / limitations

This command is retained for script compatibility. A future real proxy implementation must update `UseProxy`, `ProxyIP`, and `ProxyPort` together.

### Examples

```basic
IF UO.UseProxy() = 0 THEN
    UO.Print('Proxy disabled')
END IF
```

---

## `UO.UseRec`

### Manifest-registered overloads

- `UO.UseRec() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Compatibility metadata exposes an adapted return slot; the zero-argument command returns no script value.

### Legacy Yoko overloads

- `UO.UseRec()`
  - **Return type:** `Unit`
  - **Return contract:** No value. Replays the command most recently captured by `UO.SetRec()`.

### Parameters

- None. The command is strictly zero-argument.

### Behavior

`UO.UseRec()` decodes the command and typed arguments stored by the v50 `UO.SetRec()` recorder and routes them back through the same legacy compatibility dispatcher. Playback does not consume the recording, so the same action may be replayed repeatedly. If no valid recording exists, `UO.UseRec()` performs no action; in a connected client it reports that no recorded action is available.

### Notes / limitations

- Call `UO.SetRec()`, execute one recordable legacy `UO.*` command, then call `UO.UseRec()`.
- Replay is guarded against recursive re-recording.
- `remain()` returns `1` while a valid recorded action is available and `0` when none is stored.
- The historical Script.dll help did not define playback internals; the behavior above is the explicit v50 ClassicUO/Yoko compatibility contract.

### Examples

```basic
UO.SetRec()
UO.SetDefault('healbag', 0x40001234)

IF remain() = 1 THEN
    UO.UseRec()
END IF
```

---

## `UO.UserObject`

### Direct runtime overloads

- `UO.UserObject(arg1:Any) -> Unit`
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
UO.UserObject(0)
```

---

## `UO.UserStaticExists`

### Direct runtime overloads

- `UO.UserStaticExists(arg1:Any) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads the currently loaded ClassicUO map/tile/art asset data using the active client asset loaders.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.UserStaticExists(0)
```

---

## `UO.UseSecondaryAbility`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Активирует вторичную способность оружия (secondary ability) текущего экипированного оружия. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.UseSecondaryAbility()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseSecondaryAbility"]` → `BRIDGE CONTRACT -> IApiBridge.UseSecondaryAbility`

**Pascal compatibility signature:** `procedure UseSecondaryAbility;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UseSecondaryAbility()
```

---

## `UO.UseSelfPaperdollScroll`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Открывает скролл статуса персонажа (Character Status, из окна папердолла) для текущего персонажа. Несмотря на название, этот метод не открывает сам paperdoll — он отправляет пакет «paperdoll scroll». Результат зависит от реализации сервера: может открыться текстовое окно со статусом, многостраничный гамп или другой UI, специфичный для шарда. Для открытия скролла другого мобайла используйте UseOtherPaperdollScroll .

### Current Yoko signatures / Return

- `UO.UseSelfPaperdollScroll()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseSelfPaperdollScroll"]` → `BRIDGE CONTRACT -> IApiBridge.Self` → `BRIDGE CONTRACT -> IApiBridge.UseObject`

**Pascal compatibility signature:** `procedure UseSelfPaperdollScroll;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.UseSelfPaperdollScroll()
```

---
