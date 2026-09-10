# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Select Case는 저장한 값을 후보와 순서대로 비교하여 한 분기를 선택합니다. 아이템 분류, 스크립트 모드, 숫자 범위에 적합합니다. UO. 없이 쓰는 Basic 구문이며 식 안의 게임 API 호출에는 UO.가 필요합니다.

## 정확한 구문

```text
Select Case expression
    Case value1, value2
        statements
        Exit Select
    Case from To to
        statements
    Case Is >= value
        statements
    Case Else
        statements
End Select
```

## 매개변수

- `expression` — 필수 식으로 변수, 리터럴 또는 함수 호출을 씁니다. 빈 블록이나 Case Else만 있는 블록도 진입할 때마다 정확히 한 번 평가합니다.
- `value / from / to` — Case에는 값 하나 또는 쉼표로 구분한 후보 식을 씁니다. from To to는 양 끝을 포함하며 뒤집힌 범위는 일치하지 않습니다. 하한 비교가 성공해야 상한을 평가합니다. 함수 인수 안의 쉼표는 후보를 나누지 않습니다.
- `Is comparison value` — =, <>, <, <=, >, >=로 비교합니다. Is는 생략 가능하여 Case Is >= 5와 Case >= 5가 같습니다. 엔진의 값 비교이며 객체 형식 검사가 아닙니다.
- `Case Else` — 앞선 Case가 모두 실패할 때 쓰는 선택적 기본 분기입니다. 하나만 마지막에 둘 수 있습니다. 생략하면 불일치 시 End Select 다음으로 진행합니다.
- `Exit Select` — 가장 가까운 바깥 Select Case에서 나와 해당 End Select 다음으로 갑니다. 바깥 반복문이나 프로시저를 종료하지 않습니다. Select Case 밖에서 사용하면 로드 오류입니다.

## 반환값

Select Case, Case, End Select, Exit Select는 값을 반환하지 않으며 TRUE나 1과 비교할 수 없습니다. 예제 함수는 Return으로 String 또는 Integer를 명시적으로 반환합니다. TRUE는 숫자 1, FALSE는 0이므로 Case True는 1과 일치하며 모든 0이 아닌 수와 일치하지 않습니다.

## 동작

- 준비 단계에서 SelectInstruction, 순서가 있는 CaseInstruction 검사와 확정된 점프를 만듭니다. 선택 값은 현재 함수 호출에만 저장되어 가짜 지역 변수로 표시되지 않습니다. 재귀와 중첩 블록은 독립적인 값을 가지며 재진입 때 이전 값을 바꿉니다.
- CaseMatches는 왼쪽에서 오른쪽으로 검사하여 첫 일치에서 멈춥니다. 선택한 본문을 한 번 실행한 후 나머지 분기를 건너뜁니다. Case 안에서 변수를 바꾸어도 선택 값을 다시 읽지 않습니다. 이미 발생한 부수 효과는 되돌리지 않습니다.
- 숫자와 문자열은 일반 엔진 비교 규칙을 따르며 문자열은 대소문자를 구분합니다. Option Compare Text 및 VB.NET 자동 형 변환은 구현되지 않았습니다. 숫자와 텍스트를 비교할 때 명시적으로 변환하세요.
- End Select가 필수입니다. 첫 Case 앞에 실행 코드를 두거나 서로 다른 분기에 For/Next를 나누면 안 됩니다. 잘못된 구조는 로드를 막습니다. GoTo로 중간에 들어가지 말고 Select Case로 진입하세요.
- 오류는 현재 처리기로 전달됩니다. 선택 식이 실패하면 On Error Resume Next는 전체 블록을 건너뛰고, Case가 실패하면 다음 Case로 이동합니다. Resume는 실패한 명령을 재시도합니다. Exit Select는 떠나는 활성 Finally를 실행합니다. 명령 사이의 일시 정지와 중지 검사를 유지하며 대기나 시간 제한을 추가하지 않습니다.

## 예제

### 1. 수량 분류

```vb
# DescribeAmount는 amount를 ByVal로 받습니다. Case 0은 empty, 양 끝을 포함하는 1 To 4는 small, Is >= 5는 large를 반환합니다. 음수는 Case Else로 갑니다. Main은 -1, 0, 4, 5로 호출하여 negative:empty:small:large를 만듭니다. 문자열은 스크립트가 정한 결과입니다.
Option Explicit On
Function DescribeAmount(ByVal amount)
    Select Case amount
        Case 0
            Return "empty"
        Case 1 To 4
            Return "small"
        Case Is >= 5
            Return "large"
        Case Else
            Return "negative"
    End Select
End Function

Sub Main()
    Return DescribeAmount(-1) & ":" & DescribeAmount(0) & ":" & DescribeAmount(4) & ":" & DescribeAmount(5)
End Sub
```

**매개변수 및 실행 설명:**

DescribeAmount는 amount를 ByVal로 받습니다. Case 0은 empty, 양 끝을 포함하는 1 To 4는 small, Is >= 5는 large를 반환합니다. 음수는 Case Else로 갑니다. Main은 -1, 0, 4, 5로 호출하여 negative:empty:small:large를 만듭니다. 문자열은 스크립트가 정한 결과입니다.

### 2. 호출 관찰

```vb
# ReadMode는 ByRef로 reads를 늘리고 한 번만 2를 반환합니다. Candidate는 checks를 늘리고 value를 반환합니다. 후보 1은 실패하고 2는 일치하므로 3은 건너뜁니다. selected는 7이고 Main은 게임 접근 없이 1*100+2*10+7=127을 반환합니다.
Option Explicit On
Function ReadMode(ByRef reads)
    reads += 1
    Return 2
End Function

Function Candidate(ByRef checks, ByVal value)
    checks += 1
    Return value
End Function

Sub Main()
    Dim reads = 0
    Dim checks = 0
    Dim selected = 0
    Select Case ReadMode(reads)
        Case Candidate(checks, 1)
            selected = -1
        Case Candidate(checks, 2), Candidate(checks, 3)
            selected = 7
        Case Else
            selected = -9
    End Select
    Return reads * 100 + checks * 10 + selected
End Sub
```

**매개변수 및 실행 설명:**

ReadMode는 ByRef로 reads를 늘리고 한 번만 2를 반환합니다. Candidate는 checks를 늘리고 value를 반환합니다. 후보 1은 실패하고 2는 일치하므로 3은 건너뜁니다. selected는 7이고 Main은 게임 접근 없이 1*100+2*10+7=127을 반환합니다.

### 3. 중첩 선택 탈출

```vb
# route가 harvest이므로 첫 후보와 일치하여 trace=1이 됩니다. 내부 Case 2에서 Exit Select를 실행하고 trace=99는 건너뛰지만 Finally는 숫자 2를 붙입니다. 바깥 분기에서 3을 붙여 123을 반환합니다. 바깥 Case Else는 건너뜁니다. route를 다른 문자열로 바꾸면 -1을 반환합니다.
Option Explicit On
Sub Main()
    Dim route = "harvest"
    Dim trace = 0
    Select Case route
        Case "harvest", "loot"
            trace = 1
            Select Case 2
                Case 2
                    Try
                        Exit Select
                        trace = 99
                    Finally
                        trace = trace * 10 + 2
                    End Try
            End Select
            trace = trace * 10 + 3
        Case Else
            trace = -1
    End Select
    Return trace
End Sub
```

**매개변수 및 실행 설명:**

route가 harvest이므로 첫 후보와 일치하여 trace=1이 됩니다. 내부 Case 2에서 Exit Select를 실행하고 trace=99는 건너뛰지만 Finally는 숫자 2를 붙입니다. 바깥 분기에서 3을 붙여 123을 반환합니다. 바깥 Case Else는 건너뜁니다. route를 다른 문자열로 바꾸면 -1을 반환합니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
