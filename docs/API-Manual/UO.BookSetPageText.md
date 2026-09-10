# UO.BookSetPageText

ClassicUO • Runtime API • `UO.BookSetPageText.md`

## Точный синтаксис / Registered signatures

```text
UO.BookSetPageText(Page:Any, Text:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.BookSetPageText`

### Current Basic signatures / Return

- `UO.BookSetPageText(Page:Integer, Text:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. A valid editable page is updated locally and sent to the server with a real book-page packet.

### Parameters

- `Page` — 1-based page number.
- `Text` — page text. Newlines split the text into book lines.

### Accepted values / constants

- `Page` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.
- `Text` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Writes a page into the currently open editable `ModernBookGump`, updates the page buffer/UI and sends `Send_BookPageData` for that page.

### Notes / limitations

- `Page` must be in `1..BookPageCount`.
- A page is limited to ClassicUO's current book-line capacity (`10` lines, with the current book control's per-line character limit).
- Invalid page, too many/too-long lines, read-only book or no open book results in an error and no page update.

### Examples

```basic
SUB Main()
    UO.BookSetPageText(1, 'Line one' + Chr(10) + 'Line two')
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.BookSetPageText(1, 'example')
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Page
    VAR arg2 = 'example' # Text
    UO.BookSetPageText(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Page
    VAR arg2 = 'example' # Text
    UO.BookSetPageText(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
