# UO.UseSelfPaperdollScroll

ClassicUO • Runtime API • `UO.UseSelfPaperdollScroll.md`

## Точный синтаксис / Registered signatures

```text
UO.UseSelfPaperdollScroll() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.UseSelfPaperdollScroll`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Открывает скролл статуса персонажа (Character Status, из окна папердолла) для текущего персонажа. Несмотря на название, этот метод не открывает сам paperdoll — он отправляет пакет «paperdoll scroll». Результат зависит от реализации сервера: может открыться текстовое окно со статусом, многостраничный гамп или другой UI, специфичный для шарда. Для открытия скролла другого мобайла используйте UseOtherPaperdollScroll .

### Current Basic signatures / Return

- `UO.UseSelfPaperdollScroll() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. The command performs its registered action; verify server-dependent effects through a getter/state check when required.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["UseSelfPaperdollScroll"]` → `BRIDGE CONTRACT -> IApiBridge.Self` → `BRIDGE CONTRACT -> IApiBridge.UseObject`

**Pascal compatibility signature:** `procedure UseSelfPaperdollScroll;`

### Parameters

- None. This command has a zero-argument overload or exposes no positional arguments in the current runtime registration.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Executes the registered Basic runtime implementation shown in the Runtime route. The behavior is source-backed by the current registration rather than the historical Stealth text alone.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    UO.UseSelfPaperdollScroll()
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.UseSelfPaperdollScroll()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.UseSelfPaperdollScroll()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.UseSelfPaperdollScroll()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
