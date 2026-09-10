# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Ігрові команди викликаються через UO.; конструкції Basic, вбудовані та власні функції — за оголошеними іменами.

## Точний синтаксис

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## Параметри

- `UO.command` — UO.command(arguments): обов’язковий префікс ігрового API. UO.GetType(id) читає графіку/тіло, а не тип Basic чи CLR.
- `BasicFunction` — BasicFunction(arguments): наприклад Int(value), Str(value), CInt(value). До функцій Basic не додавайте UO.
- `arguments` — Аргументи об’єктів, фільтрів і шарів self, backpack, ground, Rhand зберігають значення. Ім’я в аргументі не є коротким викликом команди.

## Повертає

Іменування не повертає значення. Результат визначає функція: Int — Integer, Str — String; три Api*Exists повертають Integer 1/0, придатні як TRUE/FALSE.

## Поведінка

- Регістр імен неважливий. InjectionApi реєструє Basic без префікса, InjectionApiUO — ігрові виклики з UO. Для старого короткого виклику аналізатор видає SC005 і підказує зареєстровану заміну UO.; автоматичного виконання старої форми немає. Значення характеристик теж потребують UO. ApiNameExists, ApiSignatureExists, ApiParameterExists прибирають крайові пробіли та перевіряють точне зареєстроване ім’я без додавання префікса. Це метадані, не стан сервера. Оператор рефлексії VB.NET GetType(TypeName) не реалізовано.

## Приклади

### 1. 1

```vb
# graphic читає тіло персонажа або 0 без даних; whole=Int(2.9) дає 2. registered перевіряє UO.GetType з одним аргументом. Main повертає "2:1" незалежно від графіки. Руху чи перенесення немає.
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**Пояснення параметрів і виконання:**

graphic читає тіло персонажа або 0 без даних; whole=Int(2.9) дає 2. registered перевіряє UO.GetType з одним аргументом. Main повертає "2:1" незалежно від графіки. Руху чи перенесення немає.

### 2. 2

```vb
# Повна власна Function GetType отримує value=6 від CInt(6) і повертає 7. UO.GetType читає ігрову графіку. Функція без префікса та ігрова команда з префіксом не перехоплюють виклики одна одної.
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

**Пояснення параметрів і виконання:**

Повна власна Function GetType отримує value=6 від CInt(6) і повертає 7. UO.GetType читає ігрову графіку. Функція без префікса та ігрова команда з префіксом не перехоплюють виклики одна одної.

### 3. 3

```vb
# oldCall=0: нативний GetType відсутній. gameCall=1 і basicCall=1 підтверджують UO.GetType(id) та Int(value). argumentName=1 підтверджує селектор backpack. Main повертає "0:1:1:1". Власні процедури ці перевірки не шукають.
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**Пояснення параметрів і виконання:**

oldCall=0: нативний GetType відсутній. gameCall=1 і basicCall=1 підтверджують UO.GetType(id) та Int(value). argumentName=1 підтверджує селектор backpack. Main повертає "0:1:1:1". Власні процедури ці перевірки не шукають.

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
