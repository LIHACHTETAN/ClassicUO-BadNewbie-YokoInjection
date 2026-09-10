# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Include는 구문 분석과 실행 전에 다른 소스 파일을 읽습니다. 주 스크립트에서 함수와 변수를 사용할 수 있게 하지만 프로시저나 스레드를 자동 실행하지 않습니다.

## 정확한 구문

```text
Include "fileName"
```

## 매개변수

- `fileName` — fileName: 작은따옴표 또는 큰따옴표로 감싼 비어 있지 않은 파일 이름. 상대 및 절대 경로를 지원하며 변수나 식이 아닌 리터럴 경로여야 합니다. 확장자는 자유지만 내용은 엔진이 지원하는 소스 코드여야 합니다.

## 반환값

반환값이 없습니다. 소스 준비 지시문이므로 Include(...)를 대입하거나 ID, TRUE/FALSE, 1/0을 기대하지 마세요. 포함된 함수는 RETURN으로 자신의 값을 반환합니다.

## 동작

- SUB/FUNCTION 밖에서 Include를 한 줄에 따로 씁니다. 포함하는 파일 옆을 먼저 찾고 그 파일의 Include 하위 폴더를 찾습니다. 중첩 경로는 현재 라이브러리가 기준입니다. 상대 경로를 쓰기 전에 주 파일을 저장하세요.
- 전체 경로마다 한 번만 포함합니다. A → B → A 순환은 SC016입니다. 경로·접근·구문 오류는 전역 초기화 전에 실행을 막습니다. 진단과 디버거는 원본 파일과 줄을 유지합니다.
- 문자열 리터럴과 SUB/FUNCTION은 시작한 파일 안에서 닫아야 합니다. 전역 변수나 상수를 중복 선언하면 실행 전에 SC017이 발생합니다.
- 다음 실행은 수정된 라이브러리를 읽습니다. 이미 준비되거나 실행 중인 스크립트는 코드 스냅샷을 유지합니다. 프로필을 복사하거나 다른 스크립트를 실행하지 않습니다.
- 각 파일은 자체 선언 전에 Option Explicit를 지정할 수 있습니다. 생략하면 주 파일 설정을 상속합니다. 선언은 이름 공간을 공유하며 모듈을 자동 생성하지 않습니다.
- UTF-8로 읽고 BOM을 인식합니다. 한 번 준비할 때 주 파일 포함 128개 파일, 중첩 32단계, 소스 문자 16,777,216개가 한도입니다. 주석이나 문자열의 Include는 파일을 읽지 않습니다.
- 각 예제는 별도 폴더입니다. Main.bas와 표시된 모든 파일을 정확한 이름과 하위 폴더에 저장하세요. 완성된 묶음은 API Manual/Examples/Basic.Include/1, /2, /3에 있습니다. 모두 합치지 말고 Main.bas를 실행하세요.

## 예제

### 1. 공통 함수

```vb
# Main.bas가 Common.bas를 포함하고 Add(4, 7)을 호출합니다. left와 right는 값으로 전달됩니다. Add는 합계를, Main은 Integer 11을 반환합니다. Common.bas는 혼자 시작하지 않습니다.
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**매개변수 및 실행 설명:**

Main.bas가 Common.bas를 포함하고 Add(4, 7)을 호출합니다. left와 right는 값으로 전달됩니다. Add는 합계를, Main은 Integer 11을 반환합니다. Common.bas는 혼자 시작하지 않습니다.

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. 중첩 라이브러리

```vb
# Main.bas는 lib/Route.bas를 포함하고 이 파일은 자신의 lib 폴더에서 Math.bas를 포함합니다. Distance(-3, 5)는 dx=-3, dy=5를 Manhattan에 전달합니다. Abs가 부호를 제거해 합계 Integer 8을 반환합니다. 캐릭터를 움직이지 않습니다.
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**매개변수 및 실행 설명:**

Main.bas는 lib/Route.bas를 포함하고 이 파일은 자신의 lib 폴더에서 Math.bas를 포함합니다. Distance(-3, 5)는 dx=-3, dy=5를 Manhattan에 전달합니다. Abs가 부호를 제거해 합계 Integer 8을 반환합니다. 캐릭터를 움직이지 않습니다.

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

### 3. 반복 포함

```vb
# Common.bas와 ./Common.bas는 같은 파일이므로 CONST와 함수가 한 번만 선언됩니다. SharedValue=7이며 GetShared()는 7을 반환합니다. Main은 2를 곱해 Integer 14를 반환합니다. 두 파일 모두 Option Explicit On을 사용합니다.
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**매개변수 및 실행 설명:**

Common.bas와 ./Common.bas는 같은 파일이므로 CONST와 함수가 한 번만 선언됩니다. SharedValue=7이며 GetShared()는 7을 반환합니다. Main은 2를 곱해 Integer 14를 반환합니다. 두 파일 모두 Option Explicit On을 사용합니다.

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
