# Runtime API Manual — Part 01

Commands: **ActivateHandle** through **AddType**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`

---

## `UO.ActivateHandle`

### Direct runtime overloads

- `UO.ActivateHandle() -> Unit`
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
UO.ActivateHandle()
```

---

## `UO.AddChatUserIgnore`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Добавляет имя мобайла в список игнорируемых в чате. Сообщения от этого мобайла не будут отображаться в журнале, но по-прежнему доступны скриптовым методам, таким как InJournal . Полезно для фильтрации спама от определённых игроков с сохранением возможности программной обработки их сообщений. Примечание: Метод не действует на подключённых (attached) клиентов — применяется только к внутреннему журналу Stealth.

### Current Yoko signatures / Return

- `UO.AddChatUserIgnore(UserName)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddChatUserIgnore"]` → `BRIDGE CONTRACT -> IApiBridge.AddChatUserIgnore`

**Pascal compatibility signature:** `procedure AddChatUserIgnore(UserName: String);`

### Parameters

- `UserName` — String/text value interpreted according to the command.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AddChatUserIgnore('value')
```

---

## `UO.AddDir`

### Manifest-registered overloads

- `UO.AddDir(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.AddDir(directions)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `directions` — Ultima Online movement/facing direction value.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AddDir(0)
```

```basic
UO.AddDir(0)
```

---

## `UO.AddFigure`

### Current Yoko signatures / Return

- `UO.AddFigure(Figure) -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Positive figure ID on success; `0` when the figure payload is invalid or cannot be registered.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.SetMapFigure` -> `WorldMapGump`.

### Parameters

- `Figure` — Yoko `TMapFigure` adaptation.

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

Creates a persistent client-side overlay entry used by the actual ClassicUO `WorldMapGump`. The map renders line, ellipse, rectangle, direction-arrow and text figure kinds. World-coordinate figures follow the current map transform/zoom; screen-coordinate figures are relative to the map gump. The returned ID is used by `UpdateFigure` and `RemoveFigure`.

### Notes / limitations

- The figure is local to this ClassicUO client; no server packet is sent.
- Only figures whose `worldNum` matches the currently displayed facet are drawn.
- Historical `brushColor`/`brushStyle` fields are retained for compatibility; the current Yoko renderer guarantees outline/text rendering and does not claim pixel-identical Delphi brush hatching.
- `fkDirection` with world coordinates and `x2=0,y2=0` draws from the current player toward `x1,y1`, matching the common Stealth usage pattern.
- Figures remain in the client-side map collection until removed/cleared or the process ends.

### Examples

```basic
# Red world-space rectangle with a label
VAR fig = [2, 0, UO.GetX(self)-3, UO.GetY(self)-3, UO.GetX(self)+3, UO.GetY(self)+3, 0, 1, 255, UO.WorldNum(), 'Area']
VAR figureId = UO.AddFigure(fig)
```

```basic
# Direction arrow from player toward a world point
VAR dirFig = [3, 0, UO.GetX(self)+10, UO.GetY(self), 0, 0, 0, 1, 65280, UO.WorldNum(), 'East']
VAR arrowId = UO.AddFigure(dirFig)
```

# Search / World

## `UO.AddFindList`

### Manifest-registered overloads

- `UO.AddFindList(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.AddFindList(arg1:Any, arg2:Any, arg3:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.AddFindList(list, type)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.AddFindList(list, type, color)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `list` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AddFindList(0, 0)
```

```basic
UO.AddFindList(0, 0x0190, -1)
```

---

## `UO.AddGate`

### Manifest-registered overloads

- `UO.AddGate(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.AddGate(bookSerial)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `bookSerial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AddGate(0)
```

```basic
UO.AddGate(self)
```

---

## `UO.AddGumpIgnoreByID`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Добавляет ID гампа в список игнорируемых. Все входящие гампы с этим ID будут молча проигнорированы — они не появятся в очереди гампов и не будут доступны через GetGumpsCount или GetGumpInfo . На некоторых шардах каждому типу гампа присваивается уникальный ID, на других — нет. Проверьте поведение гампов на вашем шарде. Если гампы имеют только уникальные серийные номера, используйте AddGumpIgnoreBySerial . Важно: Игнорирование гампа не отменяет его на стороне сервера. Сервер считает, что гамп получен и отображён, и может ожидать ответа. Используйте методы игнорирования с осторожностью. Для очистки всех игнорирований используйте ClearGumpsIgnore .

### Current Yoko signatures / Return

- `UO.AddGumpIgnoreByID(ID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddGumpIgnoreByID"]` → `STATE -> InjectionApiState.IgnoredGumpIds`

**Pascal compatibility signature:** `procedure AddGumpIgnoreByID(ID: Cardinal);`

### Parameters

- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AddGumpIgnoreByID(self)
```

---

## `UO.AddGumpIgnoreBySerial`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Добавляет серийный номер гампа в список игнорируемых. Все входящие гампы с этим серийным номером будут молча проигнорированы — они не появятся в очереди гампов и не будут доступны через GetGumpsCount или GetGumpInfo . На некоторых шардах каждому гампу присваивается уникальный серийный номер, на других — нет. Проверьте поведение гампов на вашем шарде. Если гампы имеют только уникальные ID, используйте AddGumpIgnoreByID . Важно: Игнорирование гампа не отменяет его на стороне сервера. Сервер считает, что гамп получен и отображён, и может ожидать ответа. Используйте методы игнорирования с осторожностью. Для очистки всех игнорирований используйте ClearGumpsIgnore .

### Current Yoko signatures / Return

- `UO.AddGumpIgnoreBySerial(Serial)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddGumpIgnoreBySerial"]` → `STATE -> InjectionApiState.IgnoredGumpSerials`

**Pascal compatibility signature:** `procedure AddGumpIgnoreBySerial(Serial: Cardinal);`

### Parameters

- `Serial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AddGumpIgnoreBySerial(self)
```

---

## `UO.AddIgnoreList`

### Manifest-registered overloads

- `UO.AddIgnoreList(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.AddIgnoreList(arg1:Any, arg2:Any, arg3:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.AddIgnoreList(list, type)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.AddIgnoreList(list, type, color)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `list` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `color` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AddIgnoreList(0, 0)
```

```basic
UO.AddIgnoreList(0, 0x0190, -1)
```

---

## `UO.AddJournalIgnore`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Добавляет строку в список игнорируемых сообщений журнала. Входящие сообщения, содержащие Str как подстроку, не будут отображаться в журнале. Сравнение регистронезависимое и работает по частичному совпадению — сообщение не должно полностью совпадать со Str , достаточно содержать его. Примечание: Метод не действует на подключённых (attached) клиентов — применяется только к внутреннему журналу Stealth.

### Current Yoko signatures / Return

- `UO.AddJournalIgnore(Str)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddJournalIgnore"]` → `BRIDGE CONTRACT -> IApiBridge.AddJournalIgnore`

**Pascal compatibility signature:** `procedure AddJournalIgnore(Str: String);`

### Parameters

- `Str` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or searches the currently loaded ClassicUO world/runtime state using the registered positional overload and its documented filters.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AddJournalIgnore(0)
```

---

## `UO.AddObject`

### Direct runtime overloads

- `UO.AddObject(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.AddObject(arg1:String) -> Unit`
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
UO.AddObject(0, 0)
```

```basic
UO.AddObject(0)
```

---

## `UO.AddRecall`

### Manifest-registered overloads

- `UO.AddRecall(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.AddRecall(bookSerial)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `bookSerial` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AddRecall(0)
```

```basic
UO.AddRecall(self)
```

---

## `UO.AddStep`

### Manifest-registered overloads

- `UO.AddStep(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.AddStep(directions)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `directions` — Ultima Online movement/facing direction value.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AddStep(0)
```

```basic
UO.AddStep(0)
```

---

## `UO.AddToJournal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Добавляет текстовую строку в UO-журнал (основная вкладка журнала, не системный журнал). Сообщения, добавленные этим методом, видны в журнале и доступны для поиска через InJournal и InJournalBetweenTimes . Для записи в системный журнал используйте AddToSystemJournal .

### Current Yoko signatures / Return

- `UO.AddToJournal(Text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddToJournal"]`

**Pascal compatibility signature:** `procedure AddToJournal(Text: String);`

### Parameters

- `Text` — String/text value interpreted according to the command.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AddToJournal('value')
```

---

## `UO.AddToSystemJournal`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Записывает сообщение в системный журнал Stealth (панель System Journal в нижней части главного окна Stealth). Поддерживает escape-последовательность \n (linebreak) для переноса строки. Поведение различается в зависимости от скриптового движка: PascalScript: Принимает единственный параметр типа String . Для вывода нестроковых значений нужно вручную преобразовывать их в строку. DWScript: Принимает любое количество параметров любого типа . Компилятор автоматически преобразует все параметры в одну строку. Можно передавать записи, объекты, массивы, перечисления, множества и прочие типы напрямую — DWS выполнит их строковое представление. Очень удобно для отладки. Python: Принимает единственный параметр типа string . Для форматированного вывода с настройкой цвета, размера и шрифта используйте AddToSystemJournalEx .

### Current Yoko signatures / Return

- `UO.AddToSystemJournal(Text)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddToSystemJournal"]`

**Pascal compatibility signature:** `procedure AddToSystemJournal(Text: String);`

### Parameters

- `Text` — String/text value interpreted according to the command.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AddToSystemJournal('value')
```

---

## `UO.AddToSystemJournalEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Записывает форматированное сообщение в системный журнал Stealth (панель System Journal в нижней части главного окна Stealth). Поддерживает escape-последовательность \n (linebreak) для переноса строки. Можно настроить: TextColor — цвет текста в виде целочисленного RGB-значения. 0 = чёрный (по умолчанию) BGColor — цвет фона в виде целочисленного RGB-значения. -1 = фон по умолчанию FontSize — размер шрифта в пунктах. 10 = по умолчанию FontName — имя семейства шрифта. 'Consolas' = по умолчанию

### Current Yoko signatures / Return

- `UO.AddToSystemJournalEx(Text, TextColor, BGColor, FontSize, FontName)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["AddToSystemJournalEx"]` → `BRIDGE CONTRACT -> IApiBridge.PrintFormattedJournal`

**Pascal compatibility signature:** `procedure AddToSystemJournalEx(Text: String; TextColor: Integer; BGColor: Integer; FontSize: Integer; FontName: String);`

### Parameters

- `Text` — String/text value interpreted according to the command.
- `TextColor` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `BGColor` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.
- `FontSize` — Font identifier/name. Exact support depends on the client UI route documented for the command.
- `FontName` — String/text value interpreted according to the command.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.AddToSystemJournalEx('value', -1, -1, 0, 'value')
```

---

## `UO.AddType`

### Manifest-registered overloads

- `UO.AddType(arg1:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.
- `UO.AddType(arg1:Any, arg2:Any) -> Any`
  - **Return type:** `Any`
  - **Return contract:** Runtime-adapted value; inspect the in-client Manual/Inspector for the exact live overload metadata.

### Legacy Yoko overloads

- `UO.AddType(name)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.AddType(name, type)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `name` — String/text value interpreted according to the command.
- `type` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.AddType(0)
```

```basic
UO.AddType('value', 0x0190)
```

---
