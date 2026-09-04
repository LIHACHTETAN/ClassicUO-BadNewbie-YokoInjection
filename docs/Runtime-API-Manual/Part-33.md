# Runtime API Manual — Part 33

Commands: **WaitJournalLine** through **WarTargetID**. This file is generated from the same canonical Runtime Manual shipped with the project/client.

Canonical source SHA-256: `fcc7bb0bebe94e4b617e1dcb4ab316337d111a1c458a79bda0ae818cb2d4f2bb`

---

## `UO.WaitJournalLine`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ожидает появления указанного текста в журнале, начиная с заданной метки времени. StartTime — метка времени (TDateTime в Pascal, datetime.datetime в Python), начиная с которой сканируется журнал. Проверяются только записи после этого времени. Str — искомый текст. Поддерживает разделитель | для поиска нескольких строк (совпадение, если найдена любая из подстрок). MaxWaitTimeMS — максимальное время ожидания в миллисекундах. 0 — ждать бесконечно. Возвращает True , если текст найден в пределах таймаута, False — в противном случае. Сканирует журнал в цикле до нахождения текста или истечения таймаута. Поиск ведётся в игровом журнале (сообщения от сервера и других игроков). Для поиска в системном журнале (собственные сообщения Stealth) используйте WaitJournalLineSystem .

### Current Yoko signatures / Return

- `UO.WaitJournalLine(StartTime, Str, MaxWaitTimeMS)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitJournalLine"]`

**Pascal compatibility signature:** `function WaitJournalLine(StartTime: TDateTime; Str: String; MaxWaitTimeMS: Integer): Boolean;`

### Parameters

- `StartTime` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Str` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `MaxWaitTimeMS` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WaitJournalLine(0, 0, 1000)
```

---

## `UO.WaitJournalLineSystem`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ожидает появления указанного текста в журнале от отправителя «System», начиная с заданной метки времени. StartTime — метка времени (TDateTime в Pascal, datetime.datetime в Python), начиная с которой сканируется журнал. Str — искомый текст. Поддерживает разделитель | для поиска нескольких строк. MaxWaitTimeMS — максимальное время ожидания в миллисекундах. 0 — ждать бесконечно. Возвращает True , если текст найден, False — в противном случае. Метод идентичен WaitJournalLine , но выбирает только записи журнала, где имя отправителя ( LineName ) равно "System" . Все остальные записи журнала при поиске игнорируются.

### Current Yoko signatures / Return

- `UO.WaitJournalLineSystem(StartTime, Str, MaxWaitTimeMS)`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitJournalLineSystem"]`

**Pascal compatibility signature:** `function WaitJournalLineSystem(StartTime: TDateTime; Str: String; MaxWaitTimeMS: Integer): Boolean;`

### Parameters

- `StartTime` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `Str` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `MaxWaitTimeMS` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads, filters or emits speech/journal data through the registered ClassicUO runtime route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WaitJournalLineSystem(0, 0, 1000)
```

---

## `UO.WaitMenu`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Предустанавливает одноразовый автоматический ответ на меню: при появлении меню с совпадающим заголовком автоматически выбирается указанный пункт, после чего ловушка снимается. MenuCaption — подстрока для поиска в заголовке меню. ElementCaption — подстрока для поиска в нужном пункте меню. Устанавливает одноразовую ловушку через менеджер меню. Когда сервер отправляет меню, заголовок которого содержит MenuCaption и в котором есть пункт, содержащий ElementCaption , этот пункт автоматически выбирается и ловушка удаляется. Можно установить несколько различных ловушек подряд, вызвав WaitMenu несколько раз с разными парами caption/element перед действием, вызывающим меню. Каждая ловушка срабатывает однократно для своего совпадающего меню. Для постоянной (многоразовой) ловушки, срабатывающей каждый раз при появлении подходящего меню, используйте AutoMenu . Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.WaitMenu(MenuCaption, ElementCaption)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitMenu"]` → `BRIDGE CONTRACT -> IApiBridge.WaitMenu`

**Pascal compatibility signature:** `procedure WaitMenu(MenuCaption: String; ElementCaption: String);`

### Additional current runtime overloads

- `UO.WaitMenu(arg1:String, arg2:String, arg3:String, arg4:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitMenu(arg1:String, arg2:String, arg3:String, arg4:String, arg5:String, arg6:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `MenuCaption` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `ElementCaption` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg4` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg5` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg6` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Reads or updates the current client UI/Gump state through the registered Yoko/ClassicUO UI route.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitMenu(0, 0)
```

```basic
UO.WaitMenu(0, 0, 0, 0)
```

```basic
UO.WaitMenu(0, 0, 0, 0, 0, 0)
```

---

## `UO.WaitTargetGround`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Предустанавливает ловушку таргета, которая автоматически нацелится на первый объект указанного типа, найденный на земле. ObjType — graphic (тип) искомого объекта на земле. Метод выполняет поиск FindType на земле (контейнер Ground ). Если объект найден, устанавливается ловушка таргета на его ID. Если курсор цели уже активен в момент вызова, ловушка срабатывает немедленно. Иначе ловушка ожидает следующий входящий курсор цели и автоматически отвечает на него. Если подходящий объект на земле не найден, логируется ошибка и ловушка не устанавливается.

### Current Yoko signatures / Return

- `UO.WaitTargetGround(ObjType)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.WaitTargetGround"]`

**Pascal compatibility signature:** `procedure WaitTargetGround(ObjType: Word);`

### Additional current runtime overloads

- `UO.WaitTargetGround(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitTargetGround(0x0190)
```

```basic
UO.WaitTargetGround(0, 0)
```

---

## `UO.WaitTargetLast`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Предустанавливает ловушку таргета, которая автоматически нацелится на последний объект, на который выполнялось нацеливание. Если курсор цели уже активен в момент вызова, ловушка срабатывает немедленно. Иначе ловушка ожидает следующий входящий курсор цели и автоматически нацеливается на объект, бывший целью в последний раз. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.WaitTargetLast()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.WaitTargetLast"]`

**Pascal compatibility signature:** `procedure WaitTargetLast;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitTargetLast()
```

---

## `UO.WaitTargetObject`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Предустанавливает ловушку таргета, которая автоматически нацелится на указанный объект. ObjID — serial (ID) объекта-цели. Если курсор цели уже активен в момент вызова, ловушка срабатывает немедленно. Иначе ловушка ожидает следующий входящий курсор цели (от заклинания, навыка или другого действия) и автоматически нацеливается на объект. Ловушка срабатывает один раз. Рекомендуемый подход к нацеливанию: установить ловушку до действия, вызывающего курсор, а не ожидать появления курсора и затем отвечать. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.WaitTargetObject(ObjID)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitTargetObject"]` → `BRIDGE CONTRACT -> IApiBridge.WaitTargetObject`

**Pascal compatibility signature:** `procedure WaitTargetObject(ObjID: Cardinal);`

### Additional current runtime overloads

- `UO.WaitTargetObject(arg1:String, arg2:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `ObjID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitTargetObject(self)
```

```basic
UO.WaitTargetObject(0, 0)
```

---

## `UO.WaitTargetObjectType`

### Direct runtime overloads

- `UO.WaitTargetObjectType(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WaitTargetObjectType(arg1:Any, arg2:Any, arg3:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg3` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitTargetObjectType(0, 0)
```

```basic
UO.WaitTargetObjectType(0, 0, 0)
```

---

## `UO.WaitTargetSelf`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Предустанавливает ловушку таргета, которая автоматически нацелится на текущего персонажа (себя). Эквивалентно WaitTargetObject(Self) , но проверяет, что ID игрока не равен нулю. Если ID равен 0 , логируется ошибка и ловушка не устанавливается. Если курсор цели уже активен в момент вызова, ловушка срабатывает немедленно. Иначе ловушка ожидает следующий входящий курсор цели. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.WaitTargetSelf()`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.WaitTargetSelf"]`

**Pascal compatibility signature:** `procedure WaitTargetSelf;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitTargetSelf()
```

---

## `UO.WaitTargetTile`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Предустанавливает ловушку таргета, которая автоматически нацелится на указанный тайл по заданным координатам. Tile — graphic ID тайла-цели. X , Y — горизонтальная и вертикальная координаты карты. Z — высота цели. Если курсор цели уже активен в момент вызова, ловушка срабатывает немедленно. Иначе ловушка ожидает следующий входящий курсор цели и автоматически нацеливается. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.WaitTargetTile(Tile, X, Y, Z)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.WaitTargetTile"]`

**Pascal compatibility signature:** `procedure WaitTargetTile(Tile: Word; X: Word; Y: Word; Z: ShortInt);`

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
UO.WaitTargetTile(0, UO.GetX(self), UO.GetY(self), UO.GetZ(self))
```

---

## `UO.WaitTargetType`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Предустанавливает ловушку таргета, которая автоматически нацелится на первый объект указанного типа, найденный в рюкзаке. ObjType — graphic (тип) искомого объекта в рюкзаке. Метод выполняет поиск FindType в рюкзаке. Если объект найден, устанавливается ловушка таргета на его ID. Если курсор цели уже активен в момент вызова, ловушка срабатывает немедленно. Иначе ловушка ожидает следующий входящий курсор цели и автоматически нацеливается. Если подходящий объект в рюкзаке не найден, логируется ошибка и ловушка не устанавливается. Для поиска на земле вместо рюкзака используйте WaitTargetGround .

### Current Yoko signatures / Return

- `UO.WaitTargetType(ObjType)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DIRECT NATIVE REGISTRATION -> InjectionApiUO.Register["UO.WaitTargetType"]`

**Pascal compatibility signature:** `procedure WaitTargetType(ObjType: Word);`

### Additional current runtime overloads

- `UO.WaitTargetType(arg1:Any, arg2:Any) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `arg1` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.
- `arg2` — Positional runtime argument. Use the exact type/value domain shown by the in-client Inspector and the command description.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitTargetType(0x0190)
```

```basic
UO.WaitTargetType(0, 0)
```

---

## `UO.WaitTargetXYZ`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Предустанавливает ловушку таргета, которая автоматически нацелится на указанные координаты карты без graphic тайла. X , Y — горизонтальная и вертикальная координаты карты. Z — высота цели. Если курсор цели уже активен в момент вызова, ловушка срабатывает немедленно. Иначе ловушка ожидает следующий входящий курсор цели и автоматически нацеливается (graphic тайла = 0). Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.WaitTargetXYZ(X, Y, Z)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitTargetXYZ"]`

**Pascal compatibility signature:** `procedure WaitTargetXYZ(X: Word; Y: Word; Z: ShortInt);`

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
UO.WaitTargetXYZ(UO.GetX(self), UO.GetY(self), UO.GetZ(self))
```

---

## `UO.WaitTextEntry`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Ищет текущий ожидающий диалог ввода текста и отвечает на него; если такого нет, устанавливает ловушку на следующий входящий. Value — текст для автоматического ввода. Метод сначала проверяет, есть ли уже ожидающий диалог ввода текста. Если да — текст отправляется немедленно. Если нет — устанавливается ловушка: при получении от сервера диалога ввода текста указанный текст будет отправлен автоматически. Устарел. Этот метод неточен, поскольку отвечает на любой диалог ввода текста без разбора. Для более точного контроля рекомендуется использовать обработчики событий. Не выполняет действий, если персонаж не подключён.

### Current Yoko signatures / Return

- `UO.WaitTextEntry(Value)`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WaitTextEntry"]` → `BRIDGE CONTRACT -> IApiBridge.SetGumpValue`

**Pascal compatibility signature:** `procedure WaitTextEntry(Value: String);`

### Parameters

- `Value` — String/text value interpreted according to the command.

### Behavior

Executes the registered Yoko runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
UO.WaitTextEntry('value')
```

---

## `UO.WarMode`

### Direct runtime overloads

- `UO.WarMode(arg1:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
- `UO.WarMode() -> Integer`
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
UO.WarMode(0)
```

```basic
VAR result = UO.WarMode()
```

---

## `UO.WarTargetID`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Yoko signatures and return contracts below are authoritative when behavior differs.

Возвращает serial (ID) текущей боевой цели (мобайла, который сейчас атакуется). Возвращает 0 , если боевая цель не установлена.

### Current Yoko signatures / Return

- `UO.WarTargetID()`
  - **Return type:** `Integer`
  - **Return contract:** Integer runtime value. Zero may be a valid value or a command-specific no-result/failure sentinel.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["WarTargetID"]` → `BRIDGE CONTRACT -> IApiBridge.LastAttack`

**Pascal compatibility signature:** `function WarTargetID: Cardinal;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Behavior

Uses the registered targeting/combat route against current ClassicUO world state; server-dependent effects are asynchronous and should be verified through state/journal getters when needed.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
VAR result = UO.WarTargetID()
```

---
