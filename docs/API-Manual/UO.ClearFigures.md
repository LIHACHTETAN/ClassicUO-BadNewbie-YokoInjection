# UO.ClearFigures

ClassicUO • Runtime API • `UO.ClearFigures.md`

## Точный синтаксис / Registered signatures

```text
UO.ClearFigures() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.ClearFigures`

### Current Basic signatures / Return

- `UO.ClearFigures() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. All Basic-created World Map figures are removed from both visual map state and runtime figure state.
  - **Runtime route:** `InjectionApiUO` -> `IApiBridge.ClearMapFigures` -> `WorldMapGump`.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Clears every client-side map figure created through the Basic `AddFigure` API. Normal World Map marker files/user markers are not affected.

### Notes / limitations

This operates only on Basic figure overlays; it does not delete persisted `userMarkers` map files.

### Examples

```basic
SUB Main()
    UO.ClearFigures()
END SUB
```

# Search / World



## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.ClearFigures()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.ClearFigures()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.ClearFigures()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
