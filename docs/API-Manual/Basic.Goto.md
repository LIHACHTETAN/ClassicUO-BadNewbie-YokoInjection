# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

GoTo переводит выполнение к именованной метке в текущей процедуре или функции. Метка обозначает место в коде, а не отдельную вызываемую процедуру. Для обычных ветвлений и циклов удобнее If, циклы и Return.

## Точный синтаксис

```text
GoTo label
label:
```

## Параметры

- `label` — Имя, объявленное отдельной строкой label: внутри той же процедуры. Пишите GoTo label без кавычек, скобок и двоеточия после цели. Метка может быть выше или ниже; регистр букв не важен. В другой процедуре имя можно повторить. В имени допустимы точки, но они не превращают метку в член модуля. Числа, вычисляемые выражения и метки чужой процедуры не являются поддерживаемыми целями.

## Возвращает

GoTo и label: ничего не возвращают. Они не сообщают об успехе через 1/0 или TRUE/FALSE. Примеры явно возвращают из Main Integer -1, 6 и 123 — результаты собственных вычислений скрипта.

## Поведение

- При подготовке движок записывает адреса меток и разрешает переходы после чтения всей процедуры. При выполнении используется готовый адрес без повторного поиска по исходнику. Значения переменных сохраняются, предыдущие действия не откатываются.
- Неизвестная цель даёт SC009; клиент блокирует запуск. Повтор имени в одной процедуре, в том числе с другим регистром, даёт SC021 до инициализации. Для Include ошибка указывает исходный файл и строку. Лишние символы после цели могут дать предупреждение — используйте точный синтаксис.
- Выход из активных блоков Try выполняет их Finally изнутри наружу, затем достигает метки. Переход внутри того же активного Try сохраняет этот блок. Ошибка в Finally может помешать достижению цели.
- Входите в циклы и Try/Catch/Finally через обычные начальные конструкции. Переход в середину не восстанавливает пропущенную инициализацию и состояние блоков; так возобновлять их нельзя. Для обычного управления циклом используйте Continue или Exit.
- Переход назад не имеет автоматического лимита попыток, таймаута или задержки. Меняйте условие выхода явно. Обычный поток также проходит через метку: обходите ненужный участок переходом или Return. GoTo не устанавливает обработчик ошибок; для этого есть On Error.

## Примеры

### 1. Выбрать переход вперёд

```vb
# amount=0 выбирает NoItems, где result становится -1. Затем поток проходит через Finished и Main возвращает -1. При amount=4 обычная ветка присваивает 40, а GoTo Finished обходит NoItems. Обе метки принадлежат Main, это не вызовы функций.
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**Разбор параметров и выполнения:**

amount=0 выбирает NoItems, где result становится -1. Затем поток проходит через Finished и Main возвращает -1. При amount=4 обычная ветка присваивает 40, а GoTo Finished обходит NoItems. Обе метки принадлежат Main, это не вызовы функций.

### 2. Ограничить повторение

```vb
# attempt начинается с 0 и увеличивается перед условием. Again и again — одна метка. Три прохода прибавляют 1, 2 и 3; затем attempt<3 ложно и Return даёт 6. total инициализирован до метки, поэтому повторный переход его не обнуляет.
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**Разбор параметров и выполнения:**

attempt начинается с 0 и увеличивается перед условием. Again и again — одна метка. Три прохода прибавляют 1, 2 и 3; затем attempt<3 ложно и Return даёт 6. total инициализирован до метки, поэтому повторный переход его не обнуляет.

### 3. Выйти из вложенных Try

```vb
# trace получает 1; GoTo Finished пропускает trace=99. Внутренний Finally дописывает цифру 2, внешний — 3. Только после этого выполнение достигает Finished и возвращает 123. При этом переходе каждый блок завершения выполняется один раз.
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**Разбор параметров и выполнения:**

trace получает 1; GoTo Finished пропускает trace=99. Внутренний Finally дописывает цифру 2, внешний — 3. Только после этого выполнение достигает Finished и возвращает 123. При этом переходе каждый блок завершения выполняется один раз.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
