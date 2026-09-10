# UO.BookSetHeader

ClassicUO • Runtime API • `UO.BookSetHeader.md`

## Точный синтаксис / Registered signatures

```text
UO.BookSetHeader(Title:Any, Author:Any) -> Unit
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.BookSetHeader`

### Current Basic signatures / Return

- `UO.BookSetHeader(Title:String, Author:String) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. On a valid editable open book, ClassicUO immediately sends the real book-header update packet.

### Parameters

- `Title` — new book title.
- `Author` — new book author.

### Accepted values / constants

- `Title` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.
- `Author` — Quoted BASIC string. Fixed keywords/enums, when present, are listed in Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Finds the currently open `ModernBookGump`, verifies that it is editable, updates the visible title/author controls and sends `Send_BookHeaderChanged` (or the old-protocol header packet when required by the client version).

### Notes / limitations

- A writable book must already be open.
- Read-only books and missing book windows are rejected with a runtime error message and no packet is sent.
- Server rules remain authoritative and may reject an otherwise valid client request.

### Examples

```basic
SUB Main()
    UO.BookSetHeader('Field Notes', 'LIHACH')
END SUB
```
---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    UO.BookSetHeader(1, 2)
END SUB
```

### Вызов с явно заданными аргументами

```vb
SUB Main()
    VAR arg1 = 1 # Title
    VAR arg2 = 2 # Author
    UO.BookSetHeader(arg1, arg2)
END SUB
```

### Выполнение действия внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # Title
    VAR arg2 = 2 # Author
    UO.BookSetHeader(arg1, arg2)
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`

## Возвращает

Unit — команда не возвращает значение. Вызывайте её отдельной строкой. Не используйте её результат как serial, type или логический признак успеха. Завершение вызова само по себе не подтверждает выполнение действия сервером.
