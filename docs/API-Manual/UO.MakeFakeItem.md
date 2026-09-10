# UO.MakeFakeItem

ClassicUO • Runtime API • `UO.MakeFakeItem.md`

## Точный синтаксис / Registered signatures

```text
UO.MakeFakeItem(type:Any) -> Unit
UO.MakeFakeItem(type:Any, serial:Any) -> Unit
UO.MakeFakeItem(type:Any, serial:Any, count:Any) -> Unit
UO.MakeFakeItem(type:Any, serial:Any, count:Any, color:Any) -> Unit
UO.MakeFakeItem(type:Any, serial:Any, count:Any, color:Any, x:Any) -> Unit
UO.MakeFakeItem(type:Any, serial:Any, count:Any, color:Any, x:Any, y:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.MakeFakeItem`

### Current Basic signatures / Return

- `UO.MakeFakeItem(type:GraphicId) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteLegacyManualAlias["MakeFakeItem"]`
- `UO.MakeFakeItem(type:GraphicId, serial:ObjectRef) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteLegacyManualAlias["MakeFakeItem"]`
- `UO.MakeFakeItem(type:GraphicId, serial:ObjectRef, count:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteLegacyManualAlias["MakeFakeItem"]`
- `UO.MakeFakeItem(type:GraphicId, serial:ObjectRef, count:Integer, color:Hue) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteLegacyManualAlias["MakeFakeItem"]`
- `UO.MakeFakeItem(type:GraphicId, serial:ObjectRef, count:Integer, color:Hue, x:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteLegacyManualAlias["MakeFakeItem"]`
- `UO.MakeFakeItem(type:GraphicId, serial:ObjectRef, count:Integer, color:Hue, x:Integer, y:Integer) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteLegacyManualAlias["MakeFakeItem"]`

### Parameters

- `type` — item graphic ID. Must be in `1..0xFFFF`.
- `serial` — optional item serial. `0` asks Basic to allocate a collision-free local item serial automatically. A non-zero value must be a valid item serial (`0x40000000..0x7FFFFFFF`).
- `count` — optional stack amount. Values <= 0 are normalized to `1`; values above `65535` are clamped.
- `color` — optional hue. Clamped to the ClassicUO 16-bit hue domain and normalized by the normal client hue rules.
- `x` — optional world X coordinate. If omitted, the player's current X is used.
- `y` — optional world Y coordinate. If omitted, the player's current Y is used.

### Accepted values / constants

- `type` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `serial` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `count` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `color` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.
- `x` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `y` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

Registered arities: 1, 2, 3, 4, 5, 6. Shorter overloads omit only parameters shown absent by those signatures; no additional hidden defaults are assumed.

### Behavior

Creates or updates a **local client-side ground `Item`** through the ClassicUO `World` item collection. The item is made drawable, receives the requested graphic/hue/count and world coordinates, and uses the current player's Z coordinate. When `serial=0`, Basic allocates a free local item serial automatically.

This command does **not** send an item-create request to the Ultima Online server. It is a visual/local runtime object and can disappear when the world is reloaded or the server later sends state that replaces/removes the same serial.

### Notes / limitations

- Requires a loaded player/world.
- This is a client-side visual object; it is not a real server-owned item and cannot be used to create inventory or server resources.
- Supplying a serial already used by an item updates that local item; scripts should normally use `serial=0` unless they intentionally need a stable client-local serial.
- X/Y default to the player's position; Z always uses the player's current Z in this compatibility command.
- The command returns `Unit`; success is observable through world/search APIs rather than a returned serial.

### Examples

```basic
SUB Main()
    # Create 10 gold coins locally at the player position using an automatic serial
    UO.MakeFakeItem(0x0EED, 0, 10, 0, UO.GetX(self), UO.GetY(self))
END SUB
```

```basic
SUB Main()
    # Create a local item one tile east of the player
    UO.MakeFakeItem(0x0F0E, 0, 1, 0, UO.GetX(self) + 1, UO.GetY(self))
END SUB
```

# Character / Stats



## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.MakeFakeItem(0x0EED)
END SUB
```

### Расширенная перегрузка: 6 аргументов

```vb
SUB Main()
    VAR arg1 = 0x0EED # type
    VAR arg2 = self # serial
    VAR arg3 = 3 # count
    VAR arg4 = -1 # color
    VAR arg5 = UO.GetX() # x
    VAR arg6 = UO.GetY() # y
    UO.MakeFakeItem(arg1, arg2, arg3, arg4, arg5, arg6)
END SUB
```

### Перегрузка: 2 аргументов

```vb
SUB Main()
    UO.MakeFakeItem(0x0EED, self)
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    UO.MakeFakeItem(0x0EED, self, 3)
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    UO.MakeFakeItem(0x0EED, self, 3, -1)
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    UO.MakeFakeItem(0x0EED, self, 3, -1, UO.GetX())
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        VAR arg1 = 0x0EED # type
        UO.MakeFakeItem(arg1)
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    VAR arg1 = 0x0EED # type
    UO.MakeFakeItem(arg1)
END SUB

SUB Main()
    # Запуск процедуры выполняет действие:
    RunAction()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass66_0.<RegisterLegacyManualAliases>b__1`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
