# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Wait Until은 조건이 참이 되거나 제한 시간이 끝날 때까지 반복 확인합니다. VB.NET 문이 아닌 Basic 확장입니다. 현재 스크립트에서 실행하며 새 스레드나 다른 프로시저를 시작하지 않습니다.

## 정확한 구문

```text
Wait Until condition Timeout milliseconds
```

## 매개변수

- `condition` — condition은 즉시 평가하고 이후 짧은 대기 사이에 다시 평가합니다. Boolean 또는 비교식을 사용하세요. 숫자 0은 false이며 나머지는 If 규칙을 따릅니다. 문자열 "false"는 Boolean false가 아닙니다. UO나 사용자 함수를 호출할 수 있지만 오류는 전파되고 부수 효과는 매 검사마다 반복됩니다.
- `Timeout milliseconds` — Timeout은 필수입니다. milliseconds는 첫 검사 전에 한 번 평가하며 Integer 0..2147483647이어야 합니다. 음수, 소수, String은 조건 실행 전에 오류를 냅니다. 0은 즉시 검사만 허용합니다. 다른 위치에서는 timeout을 일반 변수 이름으로 사용할 수 있습니다.

## 반환값

문 자체는 값을 반환하지 않습니다. 성공하면 다음 줄로 진행하고 시간 초과는 파일과 줄이 포함된 실행 오류를 발생시킵니다. Try/Catch 또는 On Error로 처리할 수 있으며 없으면 현재 실행이 실패합니다. 자동으로 false를 반환하지 않습니다. 예제 2에서 True/1 또는 False/0을 반환하는 함수를 직접 만듭니다.

## 동작

- 엔진은 시간을 저장하고 단조 증가 Stopwatch를 시작합니다. 첫 즉시 검사는 제한이 0이어도 성공할 수 있습니다. false이면 루프에서 취소와 일시 정지를 확인하고 남은 시간을 계산한 뒤 최대 10밀리초 기다렸다가 검사합니다. 지속적인 바쁜 루프를 피하며 운영체제 스케줄링으로 간격이 길어질 수 있습니다.
- 일시 정지는 검사를 멈추지만 실제 경과 시간은 제한에 포함됩니다. 재개할 때 기한이 지났으면 다음 검사 전에 시간 초과가 발생합니다. 중지는 대기를 중단하고 다른 긴급 취소처럼 스크립트 Catch/Finally를 건너뜁니다. condition 안에서 막힌 호출을 강제로 중단할 수 없으므로 조건 함수는 짧게 유지하세요. 시작된 검사는 끝난 뒤 결과 또는 오류가 처리됩니다.
- 조건 오류를 시간 초과로 바꾸지 않습니다. 일반 오류와 시간 초과는 해당 Finally를 실행합니다. 변수는 현재 호출에 속하며 다시 진입하면 새 제한 시간을 시작합니다. End Wait나 추가 검사 간격 인수는 없습니다. Wait(milliseconds)는 별도의 지연 함수로 유지됩니다.

## 예제

### 1. 시간 제한 안에서 함수 확인하기

```vb
# checks는 0으로 시작합니다. Ready가 ByRef로 받아 매 검사마다 증가시키며 required=3은 ByVal입니다. budget=5000은 최대 5초입니다. 첫 두 검사는 false, 세 번째는 true여서 Main은 Integer 3을 반환합니다. 서버 연결 모의 구현이 아닌 결정적인 폴링 예제이며 실제 필요한 상태 조건으로 바꿀 수 있습니다.
Option Explicit On
Function Ready(ByRef checks As Integer, ByVal required As Integer) As Boolean
    checks += 1
    Return checks >= required
End Function

Sub Main()
    Dim checks As Integer = 0
    Const budget = 5000
    Wait Until Ready(checks, 3) Timeout budget
    Return checks
End Sub
```

**매개변수 및 실행 설명:**

checks는 0으로 시작합니다. Ready가 ByRef로 받아 매 검사마다 증가시키며 required=3은 ByVal입니다. budget=5000은 최대 5초입니다. 첫 두 검사는 false, 세 번째는 true여서 Main은 Integer 3을 반환합니다. 서버 연결 모의 구현이 아닌 결정적인 폴링 예제이며 실제 필요한 상태 조건으로 바꿀 수 있습니다.

### 2. Boolean을 반환하는 함수 만들기

```vb
# TryWait는 ready=False와 budget=0을 받습니다. 즉시 검사가 실패하면 시간 초과가 나고 Catch problem이 Return False를 실행합니다. Main은 False와 비교 가능한 0을 반환합니다. ready=True라면 1/True입니다. 모든 실행 오류를 잡으므로 구분하려면 problem을 확인하세요. ready는 Boolean 값이며 콜백 함수가 아닙니다.
Option Explicit On
Function TryWait(ByVal ready As Boolean, ByVal budget As Integer) As Boolean
    Try
        Wait Until ready Timeout budget
        Return True
    Catch problem
        Return False
    End Try
End Function

Sub Main()
    Dim success = TryWait(False, 0)
    Return success
End Sub
```

**매개변수 및 실행 설명:**

TryWait는 ready=False와 budget=0을 받습니다. 즉시 검사가 실패하면 시간 초과가 나고 Catch problem이 Return False를 실행합니다. Main은 False와 비교 가능한 0을 반환합니다. ready=True라면 1/True입니다. 모든 실행 오류를 잡으므로 구분하려면 problem을 확인하세요. ready는 Boolean 값이며 콜백 함수가 아닙니다.

### 3. 조건 오류를 보존하고 마무리하기

```vb
# CheckStatus가 state=-1을 받으면 즉시 "disconnected"를 발생시킵니다. 3000밀리초 제한은 오류를 바꾸지 않습니다. Catch는 problem을 message로 복사하고 Finally는 finished=True/1로 설정합니다. Main은 "disconnected:1"을 반환합니다. state=1은 즉시 성공하고 state=0은 시간 초과까지 false입니다. 게임 연결 없이 실행됩니다.
Option Explicit On
Function CheckStatus(ByVal state As Integer) As Boolean
    If state < 0 Then
        Throw "disconnected"
    End If
    Return state = 1
End Function

Sub Main()
    Dim message = ""
    Dim finished = False
    Try
        Wait Until CheckStatus(-1) Timeout 3000
    Catch problem
        message = problem
    Finally
        finished = True
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**매개변수 및 실행 설명:**

CheckStatus가 state=-1을 받으면 즉시 "disconnected"를 발생시킵니다. 3000밀리초 제한은 오류를 바꾸지 않습니다. Catch는 problem을 message로 복사하고 Finally는 finished=True/1로 설정합니다. Main은 "disconnected:1"을 반환합니다. state=1은 즉시 성공하고 state=0은 시간 초과까지 false입니다. 게임 연결 없이 실행됩니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
