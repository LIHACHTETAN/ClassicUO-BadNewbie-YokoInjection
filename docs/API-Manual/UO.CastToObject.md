# UO.CastToObject

ClassicUO • Runtime API • `UO.CastToObject.md`

## Точный синтаксис / Registered signatures

```text
UO.CastToObject(SpellName:Any, ObjID:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.CastToObject`

### Current Basic signatures / Return

- `UO.CastToObject(SpellName:String|Spell, ObjID:ObjectRef) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CastToObject"]`
- `UO.CastToObject(SpellIndex:Integer|Spell, ObjID:ObjectRef) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["CastToObject"]`

### Parameters

- `SpellName` — registered spell name understood by the active Basic/ClassicUO cast route.
- `SpellIndex` — numeric spell identifier accepted by the bridge.
- `ObjID` — target object/mobile serial.

### Accepted values / constants

- `SpellName` — Registered spell name or numeric spell ID, matching the overload form.
- `ObjID` — self/backpack/lasttarget/saved object name or valid decimal/0x serial, according to the overload. 0 only where documented as no-object/clear.
- `SpellIndex` — Registered spell name or numeric spell ID, matching the overload form.

### Defaults / omitted arguments

No parameters are optional; choose the spell-name or numeric-spell overload and provide a target object.

### Behavior

Queues/sets the object target and submits the spell through the ClassicUO cast bridge. The target wait is cancelled when the cast request itself is rejected so a failed `CastToObject` does not leave a stale target trap behind.

### Notes / limitations

Invalid/rejected spell requests return `False`. A `True` result means the client accepted/sent the cast request; it does not guarantee that the server completed the spell. Mana, reagents, skill checks, range, line-of-sight, server rules, interruption and target validity can still make the spell fail afterward. Confirm server completion through journal/state when the script depends on it.
### Examples

```basic
SUB Main()
    IF UO.CastToObject('Greater Heal', self) THEN
        UO.Print('Cast request accepted')
    ELSE
        UO.Print('Cast request rejected')
    END IF
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.CastToObject('Heal', 2)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 'Heal' # SpellName
    VAR arg2 = 2 # ObjID
    VAR result = UO.CastToObject(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'Heal' # SpellName
    VAR arg2 = 2 # ObjID
    VAR result = UO.CastToObject(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
