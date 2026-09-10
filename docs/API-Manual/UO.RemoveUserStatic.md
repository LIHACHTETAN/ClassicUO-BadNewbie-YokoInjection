# UO.RemoveUserStatic

ClassicUO • Runtime API • `UO.RemoveUserStatic.md`

## Точный синтаксис / Registered signatures

```text
UO.RemoveUserStatic(ID:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.RemoveUserStatic`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Удаляет пользовательский статический объект по его идентификатору из локальных данных карты. ID — идентификатор пользовательского статика, возвращённый AddUserStatic (Python: CreateUserStatic ). Возвращает True , если статик найден и удалён, False — в противном случае. Пользовательские статики — это локальные дополнения к данным статических тайлов карты (добавляемые через AddUserStatic ). Они расширяют информацию UOData о статических ячейках и влияют на отрисовку карты и поиск пути локально. Возвращает False , если персонаж не подключён или данные UO не загружены.

### Current Basic signatures / Return

- `UO.RemoveUserStatic(ID:Integer) -> Boolean`
  - **Return type:** `Boolean`
  - **Return contract:** Boolean success/state value: TRUE on success/active state, FALSE otherwise.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["RemoveUserStatic"]` → `STATE -> InjectionApiState.UserStatics` → `BRIDGE CONTRACT -> IApiBridge.RemoveUserStatic`

**Pascal compatibility signature:** `function RemoveUserStatic(ID: Integer): Boolean;`

### Parameters

- `ID` — Object/mobile/item serial. Use 0 only when the command explicitly documents 0 as a sentinel.

### Accepted values / constants

- `ID` — Numeric BASIC value. Exact range/clamping/sentinel values are stated in this card's parameter text and Behavior/Notes.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Uses the registered ClassicUO movement/path route. Movement is applied through the client walker/pathfinder rather than a detached simulation.

### Notes / limitations

Use the exact registered overload and positional argument order. Server/world-dependent effects may complete asynchronously; validate state when the script depends on confirmation.

### Examples

```basic
SUB Main()
    VAR result = UO.RemoveUserStatic(self)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.RemoveUserStatic(self)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = self # ID
    VAR result = UO.RemoveUserStatic(arg1)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = self # ID
    VAR result = UO.RemoveUserStatic(arg1)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
