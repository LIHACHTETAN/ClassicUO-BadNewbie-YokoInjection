# Runtime API Manual — Part 23

Commands: **moveThroughCorner** through **Online**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.moveThroughCorner`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Управляет разрешением «срезания углов» — диагонального движения мимо одного блокирующего тайла сбоку. Когда True , поиск пути разрешает диагональные шаги, задевающие один угол. Когда False — такие шаги блокируются. Значение по умолчанию: False . В Python используйте GetMoveThroughCorner() / SetMoveThroughCorner(value) .

### Current Yoko signatures / Return

- `UO.moveThroughCorner()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveThroughCorner"]` → `STATE -> InjectionApiState.MoveThroughCorner`
- `UO.moveThroughCorner(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveThroughCorner"]` → `STATE -> InjectionApiState.MoveThroughCorner`

**Pascal compatibility signature:** `var moveThroughCorner: Boolean;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.moveThroughCorner()
```

```basic
UO.moveThroughCorner('value')
```

---

## `UO.moveThroughNPC`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Задаёт минимальное количество stamina, необходимое для шага на тайл, занятый мобайлом (NPC или игроком). Если текущая stamina персонажа ниже этого значения, мобайл считается непроходимым для поиска пути. В Ultima Online прохождение через другого мобайла расходует stamina. Эта переменная задаёт порог, ниже которого поиск пути считает шаг невозможным и прокладывает маршрут в обход мобайла. Значение по умолчанию: 1000 (фактически делает мобайлов непроходимыми, если stamina не очень высокая). В Python используйте GetMoveThroughNPC() / SetMoveThroughNPC(value) .

### Current Yoko signatures / Return

- `UO.moveThroughNPC()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveThroughNPC"]` → `STATE -> InjectionApiState.MoveThroughNpc`
- `UO.moveThroughNPC(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveThroughNPC"]` → `STATE -> InjectionApiState.MoveThroughNpc`

**Pascal compatibility signature:** `var moveThroughNPC: Integer;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.moveThroughNPC()
```

```basic
UO.moveThroughNPC('value')
```

---

## `UO.moveTurnCost`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Дополнительная стоимость смены направления в алгоритме поиска пути A*. Большие значения заставляют поиск пути предпочитать более прямые маршруты с меньшим количеством поворотов. Значение 0 означает отсутствие штрафа за повороты. Значение по умолчанию: 14 . В Python используйте GetMoveTurnCost() / SetMoveTurnCost(value) .

### Current Yoko signatures / Return

- `UO.moveTurnCost()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveTurnCost"]` → `STATE -> InjectionApiState.MoveTurnCost`
- `UO.moveTurnCost(value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["moveTurnCost"]` → `STATE -> InjectionApiState.MoveTurnCost`

**Pascal compatibility signature:** `var moveTurnCost: Integer;`

### Parameters

- `value` — String/text value interpreted according to the command.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.moveTurnCost()
```

```basic
UO.moveTurnCost('value')
```

---

## `UO.MoveXY`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Перемещает персонажа к Xdst/Ydst через реальный маршрут ClassicUO Player.Pathfinder.WalkTo. Accuracy ограничивается 0–20; 0 требует точную клетку. Running принимает True/1 для бега либо False/0 для ходьбы. Совместимый аргумент Optimized принимается, но сейчас игнорируется. Мост использует moveCheckStamina, moveOpenDoor, moveThroughCorner, moveThroughNPC, moveHeuristicMult, moveTurnCost и moveExitOnDisconnect, затем вызывает WalkTo с текущим Z персонажа. Возвращает True/1 только когда ClassicUO подтверждает достижение, иначе False/0. Остановка — MoverStop. API Inspector показывает фактическое использование либо игнорирование каждой позиции.

### Current Yoko signatures / Return

- `UO.MoveXY(Xdst, Ydst, Optimized, Accuracy, Running)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MoveXY"]` → `STATE -> InjectionApiState.MoveCheckStamina` → `STATE -> InjectionApiState.MoveExitOnDisconnect` → `STATE -> InjectionApiState.MoveHeuristicMultiplier` → `STATE -> InjectionApiState.MoveOpenDoor` → `STATE -> InjectionApiState.MoveThroughCorner`

**Pascal compatibility signature:** `TMoverStepCallBack = function(X, Y: Word; Z: ShortInt): Boolean;`

### Parameters

- `Xdst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Ydst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Optimized` — Boolean path/movement optimization flag; changes the runtime path strategy/heuristic where supported.
- `Accuracy` — Allowed XY destination tolerance in tiles.
- `Running` — Boolean movement flag. TRUE requests running steps where the client/server allow it.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.MoveXY(0, 0, TRUE, 0, TRUE)
```

---

## `UO.MoveXYZ`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Перемещает персонажа к указанным координатам XYZ с использованием 3D-поиска пути ( GetPathArray3D ). Xdst , Ydst , Zdst — координаты назначения. AccuracyXY — горизонтальная точность в тайлах. Ограничивается 0–20. AccuracyZ — вертикальная точность. Ограничивается 0–255. Running — True — бег, False — ходьба. В DWScript дополнительно поддерживается необязательный параметр StepCallback — функция обратного вызова на каждом шаге. Если callback возвращает False , движение немедленно прекращается. TMoverStepCallBack = function(X, Y: Word; Z: ShortInt): Boolean; Метод аналогичен MoveXY , но использует 3D-поиск пути, учитывающий уровень Z. Полезен для многоуровневых зон (данжи, дома, корабли). На поведение метода влияют следующие переменные движения: moveOpenDoor , moveThroughNPC , moveThroughCorner , moveBetweenTwoCorners , moveCheckStamina , moveHeuristicMult , moveTurnCost , moveExitOnDisconnect . Возвращает True , если цель достигнута в пределах указанной точности, False — в противном случае.

### Current Yoko signatures / Return

- `UO.MoveXYZ(Xdst, Ydst, Zdst, AccuracyXY, AccuracyZ, Running)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["MoveXYZ"]` → `STATE -> InjectionApiState.MoveCheckStamina` → `STATE -> InjectionApiState.MoveExitOnDisconnect` → `STATE -> InjectionApiState.MoveHeuristicMultiplier` → `STATE -> InjectionApiState.MoveOpenDoor` → `STATE -> InjectionApiState.MoveThroughCorner`

**Pascal compatibility signature:** `TMoverStepCallBack = function(X, Y: Word; Z: ShortInt): Boolean;`

### Parameters

- `Xdst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Ydst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Zdst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `AccuracyXY` — Allowed XY destination tolerance in tiles.
- `AccuracyZ` — Vertical/Z tolerance or limit. Explicit values override shared FindVertical where documented.
- `Running` — Boolean movement flag. TRUE requests running steps where the client/server allow it.

### Behavior

Pathfinds/moves toward X/Y/Z using separate XY and Z tolerances. AccuracyZ participates in destination acceptance instead of being ignored.

### Notes / limitations

Destination can be accepted within AccuracyXY and AccuracyZ; unreachable targets can fail without moving all the way to the requested coordinates.

### Examples

```basic
VAR result = UO.MoveXYZ(0, 0, 0, 0, 12, TRUE)
```

---

## `UO.Moving`

### Direct runtime overloads

- `UO.Moving() -> Integer`
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
VAR result = UO.Moving()
```

---

## `UO.Msg`

### Direct runtime overloads

- `UO.Msg(arg1:String) -> Unit`
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
UO.Msg(0)
```

---

## `UO.Name`

### Direct runtime overloads

- `UO.Name() -> String`
  - **Return type:** `String`
  - **Return contract:** String player name/title value; empty string is possible when the value is unavailable.

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.Name()
```

---

## `UO.newMoveXY`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Перемещает персонажа к Xdst/Ydst через реальный маршрут ClassicUO Player.Pathfinder.WalkTo. Optimized теперь реально меняет режим эвристики Pathfinder; Accuracy ограничивается 0–20; Running принимает True/1 либо False/0. Необязательный StepCallback может быть 0/nil или именем процедуры/функции Yoko; он вызывается после фактического изменения XYZ, а возврат False останавливает движение. Маршрут использует текущий Z игрока и настройки moveCheckStamina, moveOpenDoor, moveThroughCorner, moveThroughNPC, moveHeuristicMult, moveTurnCost и moveExitOnDisconnect. Возвращает True/1 только при достижении итоговых XY/Z допусков. Отмена — MoverStop.

### Current Yoko signatures / Return

- `UO.newMoveXY(Xdst, Ydst, Optimized, Accuracy, Running, StepCallback)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["newMoveXY"]` → `STATE -> InjectionApiState.MoveCheckStamina` → `STATE -> InjectionApiState.MoveExitOnDisconnect` → `STATE -> InjectionApiState.MoveHeuristicMultiplier` → `STATE -> InjectionApiState.MoveOpenDoor` → `STATE -> InjectionApiState.MoveThroughCorner`
- `UO.newMoveXY(Xdst, Ydst, Optimized, Accuracy, Running, StepCallback)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["newMoveXY"]` → `STATE -> InjectionApiState.MoveCheckStamina` → `STATE -> InjectionApiState.MoveExitOnDisconnect` → `STATE -> InjectionApiState.MoveHeuristicMultiplier` → `STATE -> InjectionApiState.MoveOpenDoor` → `STATE -> InjectionApiState.MoveThroughCorner`

**Pascal compatibility signature:** `function newMoveXY(Xdst: Word; Ydst: Word; Optimized: Boolean; Accuracy: Integer; Running: Boolean; StepCallback: TMoverStepCallBack = nil): Boolean;`

### Parameters

- `Xdst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Ydst` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Optimized` — Boolean path/movement optimization flag; changes the runtime path strategy/heuristic where supported.
- `Accuracy` — Allowed XY destination tolerance in tiles.
- `Running` — Boolean movement flag. TRUE requests running steps where the client/server allow it.
- `StepCallback` — Optional callback invoked after an actual XYZ movement change; returning FALSE stops the movement operation.

### Behavior

Moves toward the requested XY target using the registered optimization/run flags. StepCallback is invoked on actual XYZ changes and may cancel the operation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.newMoveXY(0, 0, TRUE, 0, TRUE, '')
```

---

## `UO.Notoriety`

### Direct runtime overloads

- `UO.Notoriety() -> Integer`
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
VAR result = UO.Notoriety()
```

---

## `UO.NumGumpButton`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Нажимает кнопку на гампе с указанным индексом. GumpIndex — индекс гампа (начиная с 0, как в GetGumpsCount ). Value — ID кнопки для нажатия. Возвращает True , если кнопка успешно нажата, False — если индекс гампа недействителен или персонаж не подключён. В отличие от WaitGump , этот метод обращается к конкретному гампу по индексу, что надёжнее при наличии нескольких открытых гампов.

### Current Yoko signatures / Return

- `UO.NumGumpButton(GumpIndex, Value)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["NumGumpButton"]` → `BRIDGE CONTRACT -> IApiBridge.SelectGump` → `BRIDGE CONTRACT -> IApiBridge.SendGumpSelect`

**Pascal compatibility signature:** `function NumGumpButton(GumpIndex: Word; Value: Integer): Boolean;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Value` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.NumGumpButton(0, 'value')
```

---

## `UO.NumGumpCheckBox`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает значение чекбокса на гампе с указанным индексом. GumpIndex — индекс гампа (начиная с 0). CBID — ID элемента чекбокса. Value — 1 — отметить, 0 — снять отметку. Возвращает True , если чекбокс найден и установлен, False — если индекс гампа недействителен, чекбокс не найден или персонаж не подключён. В отличие от GumpAutoCheckBox , этот метод обращается к конкретному гампу по индексу, что надёжнее при наличии нескольких открытых гампов.

### Current Yoko signatures / Return

- `UO.NumGumpCheckBox(GumpIndex, CBID, Value)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["NumGumpCheckBox"]` → `BRIDGE CONTRACT -> IApiBridge.SelectGump` → `BRIDGE CONTRACT -> IApiBridge.SetGumpValue`

**Pascal compatibility signature:** `function NumGumpCheckBox(GumpIndex: Word; CBID: Integer; Value: Integer): Boolean;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `CBID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Value` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.NumGumpCheckBox(0, self, 'value')
```

---

## `UO.NumGumpRadiobutton`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает значение радиокнопки на гампе с указанным индексом. GumpIndex — индекс гампа (начиная с 0). RadiobuttonID — ID элемента радиокнопки. Value — 1 — выбрать, 0 — снять выбор. Возвращает True , если радиокнопка найдена и установлена, False — если индекс гампа недействителен, радиокнопка не найдена или персонаж не подключён. В отличие от GumpAutoRadiobutton , этот метод обращается к конкретному гампу по индексу.

### Current Yoko signatures / Return

- `UO.NumGumpRadiobutton(GumpIndex, RadiobuttonID, Value)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["NumGumpRadiobutton"]` → `BRIDGE CONTRACT -> IApiBridge.SelectGump` → `BRIDGE CONTRACT -> IApiBridge.SetGumpValue`

**Pascal compatibility signature:** `function NumGumpRadiobutton(GumpIndex: Word; RadiobuttonID: Integer; Value: Integer): Boolean;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `RadiobuttonID` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Value` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.NumGumpRadiobutton(0, self, 'value')
```

---

## `UO.NumGumpTextEntry`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Устанавливает значение текстового поля на гампе с указанным индексом. GumpIndex — индекс гампа (начиная с 0). TextEntryID — ID элемента текстового поля. Value — текстовая строка для заполнения. Возвращает True , если текстовое поле найдено и заполнено, False — если индекс гампа недействителен, текстовое поле не найдено или персонаж не подключён. В отличие от GumpAutoTextEntry , этот метод обращается к конкретному гампу по индексу.

### Current Yoko signatures / Return

- `UO.NumGumpTextEntry(GumpIndex, TextEntryID, Value)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["NumGumpTextEntry"]` → `BRIDGE CONTRACT -> IApiBridge.SelectGump` → `BRIDGE CONTRACT -> IApiBridge.SetGumpValue`

**Pascal compatibility signature:** `function NumGumpTextEntry(GumpIndex: Word; TextEntryID: Integer; Value: String): Boolean;`

### Parameters

- `GumpIndex` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `TextEntryID` — String/text value interpreted according to the command.
- `Value` — String/text value interpreted according to the command.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.NumGumpTextEntry(0, self, 'value')
```

---

## `UO.ObjAtLayer`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) предмета, экипированного в указанном слое собственного персонажа. LayerType — индекс слоя (см. ConstantsAndEnums ). Вспомогательные методы, возвращающие значения слоёв, вынесены на отдельную страницу: Layers . Если 0 , сразу возвращает 0 . Возвращает 0 , если на указанном слое нет экипированного предмета. Это сокращение для ObjAtLayerEx(LayerType, Self) . Для проверки экипировки другого мобайла используйте ObjAtLayerEx .

### Current Yoko signatures / Return

- `UO.ObjAtLayer(LayerType)`
  - **Return type:** `Any`
  - **Return contract:** Any/Variant by design: Integer 0 when the layer is empty; otherwise a hexadecimal serial String such as 0x40000001.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ObjAtLayer"]` → `BRIDGE CONTRACT -> IApiBridge.ObjAtLayer`

**Pascal compatibility signature:** `function ObjAtLayer(LayerType: Byte): Cardinal;`

### Parameters

- `LayerType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.

### Behavior

Looks up the item occupying the requested equipment layer. The direct Yoko compatibility return is deliberately dynamic: 0 when empty, otherwise a hex serial string.

### Notes / limitations

Return type is intentionally Any/Variant for compatibility: test for 0 before converting the non-empty hex serial.

### Examples

```basic
VAR result = UO.ObjAtLayer(0x0190)
```

---

## `UO.ObjAtLayerEx`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает серийный номер (ID) предмета, экипированного в указанном слое заданного мобайла. LayerType — индекс слоя (см. ConstantsAndEnums ). Вспомогательные методы, возвращающие значения слоёв, вынесены на отдельную страницу: Layers . Если 0 , сразу возвращает 0 . PlayerID — ID мобайла для проверки. Возвращает 0 , если на указанном слое нет экипированного предмета, мобайл не существует или персонаж не подключён.

### Current Yoko signatures / Return

- `UO.ObjAtLayerEx(LayerType, PlayerID)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["ObjAtLayerEx"]` → `BRIDGE CONTRACT -> IApiBridge.ObjAtLayerEx`

**Pascal compatibility signature:** `function ObjAtLayerEx(LayerType: Byte; PlayerID: Cardinal): Cardinal;`

### Parameters

- `LayerType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `PlayerID` — Equipment layer name or numeric layer identifier accepted by the runtime overload.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.ObjAtLayerEx(0x0190, self)
```

---

## `UO.Online`

### Direct runtime overloads

- `UO.Online() -> Integer`
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
VAR result = UO.Online()
```

---
