# UO.BookGetPageText

ClassicUO • Runtime API • `UO.BookGetPageText.md`

## Точный синтаксис / Registered signatures

```text
UO.BookGetPageText(Page:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.BookGetPageText`

### Current Basic signatures / Return

- `UO.BookGetPageText(Page:Integer) -> String`
  - **Return type:** `String`
  - **Return contract:** Text of the requested 1-based page; empty string is valid for an empty/unavailable page.

### Parameters

- `Page` — 1-based page number.

### Accepted values / constants

- `Page` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Reads page text from the currently open `ModernBookGump` first. If no live page text is available, the Basic compatibility buffer is used as a fallback.

### Notes / limitations

The server may not have delivered every book page yet. Opening/navigating the book can cause ClassicUO to request missing page data.

### Examples

```basic
SUB Main()
    VAR page1 = UO.BookGetPageText(1)
    UO.Print(page1)
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.BookGetPageText(1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # Page
    VAR result = UO.BookGetPageText(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Page
    VAR result = UO.BookGetPageText(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
