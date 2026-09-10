# UO.Undress

ClassicUO • Runtime API • `UO.Undress.md`

## Точный синтаксис / Registered signatures

```text
UO.Undress() -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.Undress`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Снимает все экипированные предметы персонажа в рюкзак. Перебирает все слои экипировки (правая рука, левая рука, обувь, штаны, рубашка, шлем, перчатки, кольцо, шея, пояс, торс, браслет, внешний торс, серьги, руки, плащ, мантия, юбка, ноги) и перемещает каждый экипированный предмет в рюкзак с задержкой DressSpeed между операциями. На клиентах версии 7.7.4+ (целочисленная версия ≥ 7007400) используется встроенный пакет UnequipItemsSetMacro вместо ручного перебора слоёв. Возвращает True , если все предметы успешно сняты. Возвращает False , если персонаж не подключён или перенос какого-либо предмета не удался.

### Current Basic signatures / Return

- `UO.Undress() -> Integer`
  - **Return type:** `Integer`
  - **Return contract:** Integer result from the registered runtime implementation; command-specific zero/-1 sentinels are described in Behavior/Notes.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["Undress"]`

**Pascal compatibility signature:** `function Undress: Boolean;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Reads or mutates the current ClassicUO item/equipment state through the registered runtime route and client action queue.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.Undress()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.Undress()
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR result = UO.Undress()
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR result = UO.Undress()
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.Undress`
