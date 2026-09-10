# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

GoTo는 현재 프로시저 또는 함수의 이름 있는 레이블로 실행을 옮깁니다. 레이블은 코드 위치이며 호출 가능한 프로시저가 아닙니다. 일반 제어에는 If, 반복문, Return을 사용하세요.

## 정확한 구문

```text
GoTo label
label:
```

## 매개변수

- `label` — 같은 프로시저 안에서 label:을 별도 줄에 선언한 식별자입니다. 이동은 따옴표, 괄호, 대상 뒤 콜론 없이 GoTo label로 씁니다. 앞뒤 이동을 지원하며 대소문자를 구분하지 않습니다. 다른 프로시저에서는 이름을 재사용할 수 있습니다. 이름에 점을 쓸 수 있지만 모듈 멤버라는 뜻은 아닙니다. 숫자, 계산식, 다른 프로시저의 레이블은 지원되는 대상이 아닙니다.

## 반환값

GoTo와 label:은 값을 반환하지 않으며 1/0 또는 TRUE/FALSE로 성공을 나타내지 않습니다. 예제의 Main은 직접 계산한 Integer -1, 6, 123을 명시적으로 Return합니다.

## 동작

- 준비 단계에서 레이블 주소를 기록하고 프로시저 전체를 읽은 뒤 이동 대상을 연결합니다. 실행은 확정된 주소를 사용하므로 소스를 다시 검색하지 않습니다. 변수 값은 유지되고 이전 동작은 취소되지 않습니다.
- 알 수 없는 대상은 SC009이며 클라이언트가 실행을 막습니다. 같은 프로시저의 중복 이름은 대소문자가 달라도 초기화 전에 SC021을 냅니다. Include 진단은 원본 파일과 줄을 유지합니다. 불필요한 문자는 경고를 일으킬 수 있으므로 정확한 구문을 쓰세요.
- 활성 Try 밖으로 이동하면 안쪽에서 바깥쪽 순서로 Finally를 실행한 뒤 대상에 도착합니다. 같은 활성 Try 안의 이동은 그 상태를 유지합니다. Finally 오류로 대상에 도착하지 못할 수도 있습니다.
- 반복문과 Try/Catch/Finally는 정상 시작문으로 들어가세요. 중간으로 이동해도 건너뛴 초기화나 실행 상태를 복원하지 않으므로 재개 방법으로 지원되지 않습니다. 일반 반복 제어에는 Continue 또는 Exit를 사용하세요.
- 뒤로 이동할 때 자동 시도 횟수 제한, 시간 제한, 대기가 없습니다. 종료 조건을 명시적으로 바꾸세요. 일반 흐름도 레이블을 지나가므로 불필요한 구간은 이동이나 Return으로 건너뜁니다. 오류 처리기는 On Error로 설정합니다.

## 예제

### 1. 앞으로 분기

```vb
# amount=0은 NoItems를 선택해 result=-1로 만든 후 Finished에서 -1을 반환합니다. amount=4이면 정상 경로가 40을 대입하고 GoTo Finished가 NoItems를 건너뜁니다. 두 레이블은 Main에 속하며 함수 호출이 아닙니다.
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

**매개변수 및 실행 설명:**

amount=0은 NoItems를 선택해 result=-1로 만든 후 Finished에서 -1을 반환합니다. amount=4이면 정상 경로가 40을 대입하고 GoTo Finished가 NoItems를 건너뜁니다. 두 레이블은 Main에 속하며 함수 호출이 아닙니다.

### 2. 횟수가 제한된 반복

```vb
# attempt는 0에서 시작하여 검사 전에 증가합니다. Again과 again은 같은 레이블입니다. 세 번에 걸쳐 1, 2, 3을 더한 뒤 attempt<3이 거짓이 되어 6을 반환합니다. total은 레이블 앞에서 초기화하므로 이동할 때 0으로 되돌아가지 않습니다.
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

**매개변수 및 실행 설명:**

attempt는 0에서 시작하여 검사 전에 증가합니다. Again과 again은 같은 레이블입니다. 세 번에 걸쳐 1, 2, 3을 더한 뒤 attempt<3이 거짓이 되어 6을 반환합니다. total은 레이블 앞에서 초기화하므로 이동할 때 0으로 되돌아가지 않습니다.

### 3. 중첩 Try 벗어나기

```vb
# trace가 1이 된 뒤 GoTo Finished가 trace=99를 건너뜁니다. 안쪽 Finally는 숫자 2, 바깥쪽은 3을 붙입니다. 그 뒤 Finished에 도착하여 123을 반환합니다. 이 이동에서 각 Finally는 한 번씩 실행됩니다.
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

**매개변수 및 실행 설명:**

trace가 1이 된 뒤 GoTo Finished가 trace=99를 건너뜁니다. 안쪽 Finally는 숫자 2, 바깥쪽은 3을 붙입니다. 그 뒤 Finished에 도착하여 123을 반환합니다. 이 이동에서 각 Finally는 한 번씩 실행됩니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
