# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ru -->

Include подключает исходный код из другого файла до разбора и запуска скрипта. Общие функции и переменные становятся доступны основному скрипту; отдельный поток или процедура автоматически не запускаются.

## Точный синтаксис

```text
Include "fileName"
```

## Параметры

- `fileName` — fileName: непустое имя файла в одинарных или двойных кавычках. Допускаются относительный и абсолютный пути. Это буквальный путь, а не выражение или переменная. Расширение не ограничено; содержимое должно быть текстом поддерживаемого языка.

## Возвращает

Возвращаемого значения нет: Include — директива подготовки исходников. Нельзя писать value = Include(...), ждать от неё ID, TRUE/FALSE или 1/0. Подключённые функции возвращают свои значения обычным RETURN.

## Поведение

- Пишите Include отдельной строкой вне SUB/FUNCTION. Сначала ищется файл рядом с подключающим файлом, затем в его подпапке Include. Вложенный путь считается от текущей библиотеки, а не от основного скрипта. Для относительного пути основной скрипт нужно сохранить.
- Один и тот же полный путь подключается один раз за подготовку. Цикл A → B → A считается ошибкой SC016. Ошибки пути, доступа и синтаксиса останавливают запуск до инициализации глобальных переменных. В диагностике и отладчике сохраняются файл и строка исходника.
- Строковые литералы и SUB/FUNCTION нужно закрывать в том же файле. Повторное объявление глобальной переменной или константы даёт SC017 до запуска.
- После изменения библиотеки следующий запуск читает новое содержимое. Уже подготовленный или работающий скрипт сохраняет свой снимок кода. Общий код не копирует настройки профиля и не запускает другие скрипты.
- Каждый файл может указать собственный Option Explicit до своих объявлений. Если директивы нет, действует режим основного файла. Объявления делят пространство имён; одинаковые имена функций не образуют модуль автоматически.
- Файлы читаются как UTF-8 с распознаванием BOM. Пределы одной подготовки: 128 файлов вместе с основным, 32 уровня вложения, 16 777 216 символов исходников. Комментарии и текстовые строки с Include не подключают файлы.
- Каждый пример ниже — отдельная папка. Сохраните Main.bas и все показанные файлы с точными именами и подпапками. Готовые наборы находятся в API Manual/Examples/Basic.Include/1, /2 и /3. Запускайте Main.bas, а не объединённый текст всех файлов.

## Примеры

### 1. Общая функция

```vb
# Main.bas подключает Common.bas и вызывает Add(4, 7). left и right передаются по значению; Add возвращает их сумму, Main возвращает Integer 11. Common.bas сам не запускается.
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**Разбор параметров и выполнения:**

Main.bas подключает Common.bas и вызывает Add(4, 7). left и right передаются по значению; Add возвращает их сумму, Main возвращает Integer 11. Common.bas сам не запускается.

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. Вложенная библиотека

```vb
# Main.bas подключает lib/Route.bas. Та подключает Math.bas из своей папки lib. Distance(-3, 5) передаёт dx=-3 и dy=5 функции Manhattan; Abs убирает знак, сумма равна Integer 8. Это арифметический пример, он не перемещает персонажа.
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**Разбор параметров и выполнения:**

Main.bas подключает lib/Route.bas. Та подключает Math.bas из своей папки lib. Distance(-3, 5) передаёт dx=-3 и dy=5 функции Manhattan; Abs убирает знак, сумма равна Integer 8. Это арифметический пример, он не перемещает персонажа.

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

### 3. Повторное подключение

```vb
# Common.bas и ./Common.bas обозначают один файл: CONST и функция объявляются один раз. SharedValue=7; GetShared() возвращает 7, Main умножает его на 2 и возвращает Integer 14. Оба файла используют Option Explicit On.
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**Разбор параметров и выполнения:**

Common.bas и ./Common.bas обозначают один файл: CONST и функция объявляются один раз. SharedValue=7; GetShared() возвращает 7, Main умножает его на 2 и возвращает Integer 14. Оба файла используют Option Explicit On.

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
