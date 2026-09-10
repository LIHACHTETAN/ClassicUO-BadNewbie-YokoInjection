# UO.UseRec

ClassicUO • Runtime API • `UO.UseRec.md`

## Точный синтаксис / Registered signatures

```text
UO.UseRec() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UseRec`

### Manifest-registered overloads

- `UO.UseRec() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.


### Parameters

- None. The command is strictly zero-argument.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Replays the command and typed arguments stored by the `UO.SetRec()` recorder through the same legacy compatibility dispatcher. Replay does not consume the recording, so the same action can be executed repeatedly. If no valid recording exists, `UO.UseRec()` performs no action and reports the missing recording in a connected client.
### Notes / limitations

- Call `UO.SetRec()`, execute one recordable legacy `UO.*` command, then call `UO.UseRec()`.
- Replay is guarded against recursive re-recording.
- `remain()` returns `1` while a valid recorded action is available and `0` when none is stored.
- The historical Script.dll help did not define playback internals; the behavior above is the explicit ClassicUO/Basic compatibility contract.

### Examples

```basic
SUB Main()
    UO.SetRec()
    UO.SetDefault('healbag', 0x40001234)

    IF remain() = 1 THEN
        UO.UseRec()
    END IF
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.UseRec()
END SUB
```

### Условный вызов из игрового скрипта

```vb
SUB Main()
    IF UO.Connected THEN
        UO.UseRec()
    END IF
END SUB
```

### Повторное использование через процедуру

```vb
SUB RunAction()
    UO.UseRec()
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
