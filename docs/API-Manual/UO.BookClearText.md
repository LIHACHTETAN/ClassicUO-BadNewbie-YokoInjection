# UO.BookClearText

ClassicUO • Runtime API • `UO.BookClearText.md`

## Точный синтаксис / Registered signatures

```text
UO.BookClearText() -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.BookClearText`

### Current Basic signatures / Return

- `UO.BookClearText() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Clears the Basic book buffer and, when an editable book is open, sends empty content for its pages.

### Parameters

- None.

### Accepted values / constants

- None; this command's registered overload takes no positional arguments.

### Defaults / omitted arguments

No parameters; no argument defaults apply.

### Behavior

Clears all pages of the currently open editable ClassicUO book through the same real page-update packet path used by `BookSetPageText`.

### Notes / limitations

A writable book must be open for a server-side book change. With no open book, only the compatibility buffer can be cleared and an error is reported for the missing live target.

### Examples

```basic
SUB Main()
    UO.BookClearText()
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.BookClearText()
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    UO.BookClearText()
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    UO.BookClearText()
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
