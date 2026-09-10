# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: uk -->

Include підключає інший файл вихідного коду до розбору й запуску. Спільні функції та змінні стають доступними головному скрипту; процедура чи потік автоматично не запускаються.

## Точний синтаксис

```text
Include "fileName"
```

## Параметри

- `fileName` — fileName: непорожнє ім’я файлу в одинарних або подвійних лапках. Можна вказати відносний чи абсолютний шлях. Це буквальний шлях, а не вираз або змінна. Розширення довільне; вміст має бути кодом підтримуваної мови.

## Повертає

Значення не повертається: Include — директива підготовки коду. Не присвоюйте Include(...) змінній і не очікуйте ID, TRUE/FALSE чи 1/0. Підключені функції повертають власні значення через RETURN.

## Поведінка

- Пишіть Include окремим рядком поза SUB/FUNCTION. Пошук: поруч із файлом, що підключає, потім у його підпапці Include. Вкладені шляхи рахуються від поточної бібліотеки. Для відносних шляхів спочатку збережіть головний файл.
- Кожен повний шлях підключається один раз за підготовку. Цикл A → B → A дає SC016. Помилки шляху, доступу й синтаксису зупиняють запуск до ініціалізації глобальних змінних. Діагностика й відлагоджувач зберігають файл і рядок джерела.
- Закривайте рядкові літерали та SUB/FUNCTION у тому самому файлі. Повторне оголошення глобальної змінної або константи дає SC017 до запуску.
- Наступний запуск читає зміни бібліотеки; уже підготовлений чи запущений скрипт зберігає свій знімок коду. Налаштування профілів не копіюються, інші скрипти не запускаються.
- Кожен файл може задати Option Explicit перед власними оголошеннями; інакше успадковує режим головного файлу. Оголошення мають спільний простір імен, модуль автоматично не створюється.
- Читання UTF-8 з розпізнаванням BOM. Межі: 128 файлів разом із головним, 32 рівні вкладення, 16 777 216 символів коду. Include у коментарях або рядках тексту не підключає файли.
- Кожен приклад має окрему папку. Збережіть Main.bas та всі показані файли з точними назвами й підпапками. Готові набори: API Manual/Examples/Basic.Include/1, /2, /3. Запускайте Main.bas, не об’єднуйте весь код в один файл.

## Приклади

### 1. Спільна функція

```vb
# Main.bas підключає Common.bas і викликає Add(4, 7). left і right передаються за значенням; Add повертає суму, Main — Integer 11. Common.bas сам не запускається.
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**Пояснення параметрів і виконання:**

Main.bas підключає Common.bas і викликає Add(4, 7). left і right передаються за значенням; Add повертає суму, Main — Integer 11. Common.bas сам не запускається.

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. Вкладена бібліотека

```vb
# Main.bas підключає lib/Route.bas, а вона — Math.bas зі своєї папки lib. Distance(-3, 5) передає dx=-3, dy=5 до Manhattan; Abs прибирає знак, сума — Integer 8. Це арифметика, персонаж не рухається.
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**Пояснення параметрів і виконання:**

Main.bas підключає lib/Route.bas, а вона — Math.bas зі своєї папки lib. Distance(-3, 5) передає dx=-3, dy=5 до Manhattan; Abs прибирає знак, сума — Integer 8. Це арифметика, персонаж не рухається.

**lib/Route.bas**

```vbnet
Option Explicit On
Include "Math.bas"
FUNCTION Distance(ByVal dx, ByVal dy)
    RETURN Manhattan(dx, dy)
END FUNCTION
```

**lib/Math.bas**

```vbnet
Option Explicit On
FUNCTION Manhattan(ByVal dx, ByVal dy)
    RETURN Abs(dx) + Abs(dy)
END FUNCTION
```

### 3. Повторне підключення

```vb
# Common.bas і ./Common.bas — один файл, його CONST і функція оголошуються один раз. SharedValue=7; GetShared() повертає 7, Main множить на 2 та повертає Integer 14. Обидва файли мають Option Explicit On.
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**Пояснення параметрів і виконання:**

Common.bas і ./Common.bas — один файл, його CONST і функція оголошуються один раз. SharedValue=7; GetShared() повертає 7, Main множить на 2 та повертає Integer 14. Обидва файли мають Option Explicit On.

**Common.bas**

```vbnet
Option Explicit On
CONST SharedValue = 7
FUNCTION GetShared()
    RETURN SharedValue
END FUNCTION
```

<!-- implementation references (not callable script procedures):
Parsing/ScriptSourceGraph.cs: Load / Builder.AddInclude / ResolveLine
Runtime/InjectionRuntime.cs: Prepare / Load
Runtime/Interpreter.cs: Location / EvaluateInitializer / CallObserved
Analysis/SanityAnalyzer.cs: Analyze
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: PrepareScriptForExecution
InjectionScript.Lsp/Workspace.cs: UpdateDiagnostic
-->
