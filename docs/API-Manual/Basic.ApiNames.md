# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Игровые команды вызываются через UO.; конструкции Basic, встроенные и собственные функции — по их объявленным именам.

## Точный синтаксис

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## Параметры

- `UO.command` — UO.command(arguments): обязательный префикс игрового API. UO.GetType(id) читает графику/тело, а не тип Basic или CLR.
- `BasicFunction` — BasicFunction(arguments): например Int(value), Str(value), CInt(value). Добавлять UO. к функции Basic не нужно.
- `arguments` — Аргументы объектов, фильтров и слоёв self, backpack, ground, Rhand сохраняют смысл. Имя в аргументе не является коротким вызовом игровой команды.

## Возвращает

Правило именования ничего не возвращает. Результат определяет вызванная функция: Int — Integer, Str — String; три проверки Api*Exists возвращают Integer 1/0, которые можно использовать как TRUE/FALSE.

## Поведение

- Регистр имён не важен. InjectionApi регистрирует библиотеку Basic без префикса, InjectionApiUO — игровые вызовы с UO. При старом коротком вызове анализатор выдаёт SC005 и подсказывает зарегистрированную замену UO.; скрытого выполнения старого вызова нет. Значения характеристик персонажа тоже требуют UO. ApiNameExists, ApiSignatureExists и ApiParameterExists убирают пробелы по краям и проверяют точное зарегистрированное имя, не дописывая префикс. Это проверка метаданных, не состояния сервера. Оператор рефлексии VB.NET GetType(TypeName) в движке не реализован.

## Примеры

### 1. 1

```vb
# graphic читает тело текущего персонажа, либо 0 при отсутствии данных; whole=Int(2.9) даёт 2. registered проверяет регистрацию UO.GetType с одним аргументом. Main возвращает "2:1" независимо от графики персонажа. Движение и перенос предметов не выполняются.
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**Разбор параметров и выполнения:**

graphic читает тело текущего персонажа, либо 0 при отсутствии данных; whole=Int(2.9) даёт 2. registered проверяет регистрацию UO.GetType с одним аргументом. Main возвращает "2:1" независимо от графики персонажа. Движение и перенос предметов не выполняются.

### 2. 2

```vb
# Полностью показанная пользовательская Function GetType получает value=6 из CInt(6) и возвращает 7. UO.GetType по-прежнему читает игровую графику. Своя функция без префикса и игровая команда с префиксом не перехватывают вызовы друг друга.
Option Explicit On
Function GetType(value)
    Return value + 1
End Function
Sub Main()
    Var localResult = GetType(CInt(6))
    Var graphic = UO.GetType('self')
    Return localResult
End Sub
```

**Разбор параметров и выполнения:**

Полностью показанная пользовательская Function GetType получает value=6 из CInt(6) и возвращает 7. UO.GetType по-прежнему читает игровую графику. Своя функция без префикса и игровая команда с префиксом не перехватывают вызовы друг друга.

### 3. 3

```vb
# oldCall=0: GetType не зарегистрирован как нативный вызов. gameCall=1 и basicCall=1 подтверждают UO.GetType(id) и Int(value). argumentName=1 показывает, что backpack остаётся селектором аргумента. Main возвращает "0:1:1:1". Эти проверки не ищут пользовательские процедуры.
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**Разбор параметров и выполнения:**

oldCall=0: GetType не зарегистрирован как нативный вызов. gameCall=1 и basicCall=1 подтверждают UO.GetType(id) и Int(value). argumentName=1 показывает, что backpack остаётся селектором аргумента. Main возвращает "0:1:1:1". Эти проверки не ищут пользовательские процедуры.

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
