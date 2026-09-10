# UO.BookSetText

ClassicUO • Runtime API • `UO.BookSetText.md`

## Точный синтаксис / Registered signatures

```text
UO.BookSetText(Text:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.BookSetText`

### Current Basic signatures / Return

- `UO.BookSetText(Text:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Accepted text is divided into pages and each page is sent through the real ClassicUO book-page packet path.

### Parameters

- `Text` — full book text. Newlines form lines; form-feed (`Chr(12)`) may be used as an explicit page separator.

### Accepted values / constants

- `Text` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Updates the currently open editable book rather than only storing a Basic-side string. Without explicit form-feed separators, lines are divided automatically into groups of up to ten lines per page. Each affected page is updated locally and sent to the server.

### Notes / limitations

- The text must fit the open book's page count and current per-page/per-line limits.
- A read-only or missing book is not modified.
- Server validation remains authoritative.

### Examples

```basic
SUB Main()
    UO.BookSetText('First page line 1' + Chr(10) + 'First page line 2')
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.BookSetText('example')
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 'example' # Text
    UO.BookSetText(arg1)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 'example' # Text
    UO.BookSetText(arg1)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
