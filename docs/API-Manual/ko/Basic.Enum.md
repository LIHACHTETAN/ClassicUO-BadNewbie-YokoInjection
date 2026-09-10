# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Enum은 스크립트 상태와 모드를 나타내는 이름 있는 Integer 상수를 묶습니다. 파일이나 Module 수준에 선언하며 Sub/Function 내부에는 선언할 수 없습니다. VB.NET 열거형의 일부를 지원하며 .NET Enum 객체를 만들지 않습니다.

## 정확한 구문

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## 매개변수

- `Public / Private` — 기본은 Public이며 Module 내부도 같습니다. Private은 Module 내부에서만 허용되고 다른 모듈과 파일 범위에서 형식 및 멤버를 숨깁니다.
- `name` — Mode처럼 점 없는 단순 이름을 사용하며 대소문자를 구분하지 않습니다. UO와 내장 형식 이름은 예약되어 있습니다. 전체 이름은 Enum, Module, 전역 변수와 중복될 수 없습니다.
- `As Integer` — 선택 사항입니다. 기반 형식은 부호 있는 32비트 Integer, -2147483648..2147483647만 지원합니다. 다른 형식은 거부됩니다. 변수, 매개변수, Function 반환형의 As Mode는 일반 Integer 저장 및 변환을 사용하며 나열된 멤버 값으로 제한하지 않습니다. 초기화하지 않으면 0입니다.
- `member` — 한 줄에 단순 멤버 이름 하나, 최소 한 멤버가 필요합니다. 중복 이름, True, False는 금지됩니다. 식이 없으면 첫 값은 0, 이후 값은 이전 값에 1을 더합니다. 서로 다른 이름이 같은 값을 가져도 됩니다.
- `constantExpression` — 선택적 상수 식: 10진/0x 정수, 괄호, 단항 음수, + - * / Mod, 이전 멤버와 이미 선언된 숫자 Const. 최종 값은 범위 내 정수여야 하며 중간 나눗셈에는 소수가 허용됩니다. 참조 Const도 Integer 결과여야 하며 형식 없음 또는 As Integer/Long/Short/Byte만 허용됩니다. 함수 호출, 변수, 문자열, 비교, 배열 읽기는 금지됩니다. 이후 멤버 참조, 순환 의존성, 128단계 초과 의존성은 거부됩니다.
- `name.member` — Mode.Ready로 읽고 모듈 외부에서는 Tools.Mode.Ready를 사용합니다. Tools 안에서는 Mode.Ready, With Mode 안에서는 .Ready를 사용합니다. 대입, +=, ByRef 되쓰기로 상수를 변경할 수 없습니다. Enum 형식은 함수처럼 호출하지 않습니다.

## 반환값

선언 자체는 반환값과 호출 괄호가 없습니다. 멤버를 읽으면 Integer, 예를 들어 Mode.Working = 3을 반환합니다. 상태값이지 자동 성공 표시는 아닙니다. state = Mode.Finished라는 Boolean 비교는 1/True 또는 0/False를 반환하며 두 표기 모두 사용할 수 있습니다. 상태 0은 실패가 아니라 Idle일 수 있습니다.

## 동작

- 준비 단계에서 EnumCatalog가 스크립트/API를 실행하지 않고 이전 숫자 상수와 자동 번호를 계산하며 이름, 접근, 범위를 검사합니다. SC026은 Option Explicit이 없어도 시작을 차단합니다. 구문 오류도 실행을 차단하고 편집 중 미완성 선언은 진단을 표시합니다.
- DefinitionCollector는 전역 초기화 및 Optional 기본값보다 먼저 불변 멤버를 등록하므로 해당 위치는 파일 뒤쪽의 Enum도 참조할 수 있습니다. Enum 내부 식은 여전히 이전 상수만 사용합니다. 준비된 스크립트가 고정 목록을 보관하고 다른 스크립트를 로드하면 교체됩니다.
- ScriptBindings는 모듈 상대 이름과 Private을 한 번 해석합니다. 실행은 일반 상수를 읽으며 반복문에서 재계산하거나 리플렉션을 사용하지 않습니다. As Mode는 Integer로 정규화되어 디버거에 Integer로 표시될 수 있습니다. Include에서 선언을 가져올 수 있습니다. Flags 특성, System.Enum 메서드, 암시적 멤버 가져오기, 자동 멤버 목록은 없습니다.

## 예제

### 1. 상태에 이름 지정

```vb
# Idle=0과 Queued=1은 자동입니다. Working=10으로 순서가 바뀌므로 Finished=11입니다. state As TaskState는 10을 받습니다. Main은 CStr로 숫자를 변환하여 String "0:1:10:11"을 반환합니다. 이름은 자신의 상태로 바꿀 수 있고 선언 자체는 절차를 시작하지 않습니다.
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**매개변수 및 실행 설명:**

Idle=0과 Queued=1은 자동입니다. Working=10으로 순서가 바뀌므로 Finished=11입니다. state As TaskState는 10을 받습니다. Main은 CStr로 숫자를 변환하여 String "0:1:10:11"을 반환합니다. 이름은 자신의 상태로 바꿀 수 있고 선언 자체는 절차를 시작하지 않습니다.

### 2. 모듈 상태 숨기기

```vb
# Controller.Mode는 Controller 내부 전용입니다. NextMode는 distance ByVal As Integer를 받아 호출자 인수를 변경하지 않습니다. distance<=1이면 Arrived=5, 아니면 Walking=4이며 state는 0부터 시작합니다. Main은 3과 1을 전달해 4와 5를 받고 Integer 45를 반환합니다. 캐릭터 이동은 없고 distance는 예제 입력입니다. 외부에서는 Controller.NextMode만 호출할 수 있으며 Controller.Mode.Arrived는 읽을 수 없습니다.
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**매개변수 및 실행 설명:**

Controller.Mode는 Controller 내부 전용입니다. NextMode는 distance ByVal As Integer를 받아 호출자 인수를 변경하지 않습니다. distance<=1이면 Arrived=5, 아니면 Walking=4이며 state는 0부터 시작합니다. Main은 3과 1을 전달해 4와 5를 받고 Integer 45를 반환합니다. 캐릭터 이동은 없고 distance는 예제 입력입니다. 외부에서는 Controller.NextMode만 호출할 수 있으며 Controller.Mode.Arrived는 읽을 수 없습니다.

### 3. 상태 변경 후 Boolean 반환

```vb
# 이전 Integer Const인 FirstState=2로 Idle=2, Working=3, Finished=4가 됩니다. Advance는 state를 ByRef로 받아 Main의 변수를 바꿉니다. With Mode는 이름을 줄이고 Select Case는 전환을 선택합니다. 두 번 호출하면 2→3→4입니다. IsFinal은 ByVal 복사본을 Finished와 비교하므로 Main은 1/True를 반환합니다. 한 번 전환했다면 0/False입니다. Advance를 다시 호출하면 "No next state" 오류가 발생하며 Mode 상수는 바뀌지 않습니다.
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**매개변수 및 실행 설명:**

이전 Integer Const인 FirstState=2로 Idle=2, Working=3, Finished=4가 됩니다. Advance는 state를 ByRef로 받아 Main의 변수를 바꿉니다. With Mode는 이름을 줄이고 Select Case는 전환을 선택합니다. 두 번 호출하면 2→3→4입니다. IsFinal은 ByVal 복사본을 Finished와 비교하므로 Main은 1/True를 반환합니다. 한 번 전환했다면 0/False입니다. Advance를 다시 호출하면 "No next state" 오류가 발생하며 Mode 상수는 바뀌지 않습니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
