# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

On Error задаёт обработку последующих ошибок выполнения в текущей процедуре или функции. Это конструкция языка, а не вызываемая API-команда. Для структурированной обработки и завершения используйте Try/Catch/Finally.

## Точный синтаксис

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## Параметры

- `label` — Существующая метка внутри той же процедуры, записанная отдельной строкой label:. Может стоять выше или ниже On Error, регистр букв не важен. Это не имя функции, строка в кавычках и не номер строки исходника. Неизвестная метка даёт SC009; клиент блокирует такой скрипт.
- `Resume Next / On Error` — On Error Resume Next включает автоматическое продолжение после ошибочной инструкции без перехода к метке. Успешные инструкции работают обычно. Режим действует в текущем вызове процедуры, а не во всех скриптах.
- `0` — On Error GoTo 0 отключает выбранный режим. Ноль — специальное управляющее значение, не метка и не Boolean-результат. Другие числовые метки и GoTo -1 не поддерживаются.
- `Resume / Resume Next` — В обработчике Resume повторяет ошибочную инструкцию, Resume Next продолжает после неё. Нужна сохранённая ошибка выполнения; после перехода её адрес очищается. Метку либо таймаут эти формы в нашем движке не принимают.

## Возвращает

On Error и Resume ничего не возвращают. Перехваченная ошибка не превращается в TRUE/FALSE и не исправляет присваивание автоматически. Примеры явно возвращают Integer 5,18,10. Ранее выполненные побочные действия автоматически не откатываются.

## Поведение

- Подготовка разрешает метки после чтения всей процедуры, поэтому работают оба направления. Выполнение сохраняет выбранный режим; при исключении сначала рассматривается структурированный Try, затем On Error.
- Движок запоминает адрес ошибочной инструкции. Режим метки переходит в обработчик, автоматический Resume Next — за инструкцию. Resume заново вычисляет её выражения и вызовы: сначала устраните причину, учитывая возможное повторение действий.
- On Error GoTo 0 не стирает сохранённый адрес ошибки: обработчик может отключить себя, исправить данные и выполнить Resume. Отключайте режим перед потенциально ошибочными действиями обработчика, чтобы не войти в него повторно.
- Ошибки синтаксиса и отмена выполнения здесь не перехватываются. Если команда просто возвращает 0, FALSE или иной статус отказа без исключения, On Error не вызывается — проверяйте результат этой команды.
- Обычный поток должен обходить обработчик через Return либо явный GoTo. У вызываемой процедуры свой режим. Её неперехваченная ошибка может дойти до вызывающей; Resume тогда повторит всю инструкцию вызова, а не внутреннюю строку. Автоматического предела попыток и задержки нет.

## Примеры

### 1. Пропустить одно ошибочное присваивание

```vb
# values[0] выделяет одну ячейку; индекс 5 недопустим. result начинается с 1. On Error Resume Next пропускает неудачное чтение до присваивания, поэтому result остаётся 1. GoTo 0 отключает режим; result+=4 даёт 5. Main возвращает 5, но не объявляет чтение успешным.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**Разбор параметров и выполнения:**

values[0] выделяет одну ячейку; индекс 5 недопустим. result начинается с 1. On Error Resume Next пропускает неудачное чтение до присваивания, поэтому result остаётся 1. GoTo 0 отключает режим; result+=4 даёт 5. Main возвращает 5, но не объявляет чтение успешным.

### 2. Исправить и повторить

```vb
# ReadCell хранит 8 в ячейке 0, но начинает с index=2. Ошибка чтения переходит к FixIndex. GoTo 0 отключает дальнейшую обработку; handled становится 1, index — 0. Resume повторяет result=values[index] и теперь записывает 8. Return не даёт обычному потоку попасть в обработчик. Main получает 18.
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**Разбор параметров и выполнения:**

ReadCell хранит 8 в ячейке 0, но начинает с index=2. Ошибка чтения переходит к FixIndex. GoTo 0 отключает дальнейшую обработку; handled становится 1, index — 0. Resume повторяет result=values[index] и теперь записывает 8. Return не даёт обычному потоку попасть в обработчик. Main получает 18.

### 3. Обработчик выше команды

```vb
# Начальный GoTo Work обходит Failed при нормальном входе. On Error GoTo Failed подключает эту ранее объявленную метку. Чтение индекса 2 падает до изменения result. Обработчик отключает себя, увеличивает handled и через Resume Next достигает Return. Результат 1*10+0=10. Метки не являются отдельными процедурами.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**Разбор параметров и выполнения:**

Начальный GoTo Work обходит Failed при нормальном входе. On Error GoTo Failed подключает эту ранее объявленную метку. Чтение индекса 2 падает до изменения result. Обработчик отключает себя, увеличивает handled и через Resume Next достигает Return. Результат 1*10+0=10. Метки не являются отдельными процедурами.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
