# UO.SetRec

ClassicUO • Runtime API • `UO.SetRec.md`

## Точный синтаксис / Registered signatures

```text
UO.SetRec() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.SetRec`

### Manifest-registered overloads

- `UO.SetRec() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- None. The command is strictly zero-argument.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

`UO.SetRec()` is the one-shot recorder. It clears the previous recording, arms capture, then lets the next compatible legacy `UO.*` command execute normally while storing the command name together with its typed arguments. The recorder disarms immediately after that one capture; `UO.UseRec()` replays the saved action.
### Notes / limitations

- Recording is one-shot: after one compatible command is captured, the recorder automatically disarms.
- `UO.SetRec()` and `UO.UseRec()` themselves are never captured.
- The stored command is kept in Basic runtime state and survives the normal runtime-state snapshot/restore path.
- `remain()` returns `0` immediately after `UO.SetRec()` and `1` after a command has been captured.
- This behavior is a documented ClassicUO/Basic compatibility definition because no authoritative public Script.dll implementation of the historical semantics is available.

### Examples

```basic
SUB Main()
    UO.SetRec()
    UO.SetDefault('healbag', 0x40001234)  # executes and is recorded
    IF remain() = 1 THEN
        UO.UseRec()                       # repeats SetDefault with the same arguments
    END IF
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.SetRec()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.SetRec()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.SetRec()
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
