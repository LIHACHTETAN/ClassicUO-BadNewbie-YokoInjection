# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Try는 본문과 호출한 함수의 실행 오류를 처리합니다. Catch가 오류를 받고 Finally가 마무리를 수행하며 Throw가 오류를 발생시키거나 다시 던집니다. API의 0 또는 false는 일반 반환값이므로 명시적으로 검사해야 합니다. 자동으로 Catch에 들어가지는 않습니다.

## 정확한 구문

```text
Try
    statements
Catch
    handlerStatements
Finally
    cleanupStatements
End Try
Catch name
Catch name As Exception
Catch name As String
Throw stringExpression
Throw
```

## 매개변수

- `Try / statements` — Try에는 하나의 Catch, 하나의 Finally 또는 둘 다와 End Try가 필요합니다. 중첩할 수 있으며 본문이 정상 종료되면 Catch를 건너뜁니다. 이 부분집합은 여러 Catch, When 필터, Exit Try를 구현하지 않습니다.
- `Catch / name / As type` — Catch 변수는 생략할 수 있습니다. name을 지정하면 String 오류 메시지를 받습니다. As String은 이 표현을 나타내며 As Exception은 호환 표기일 뿐 .NET 객체나 형식 필터가 아닙니다. 다른 형식은 거부됩니다. 새 이름은 프로시저 지역 변수가 되어 같은 이름의 전역을 가립니다. 기존 지역 변수에는 형식/Const 규칙을 지켜 대입합니다. Catch가 실행되지 않는 경로에서도 필요하면 Try 앞에서 String을 선언하세요.
- `Finally / End Try` — Catch가 있으면 Finally는 선택 사항이고 본문이 비어 있어도 됩니다. 정상 종료, 오류, Return, Exit Sub/Function, 바깥 방향의 반복문 이동 및 GoTo는 관련 Finally를 실행합니다. End Try는 필수입니다. 스크립트 취소는 의도적으로 Catch와 스크립트 Finally를 건너뛰어 긴급 정지가 지연되지 않도록 합니다.
- `Throw stringExpression` — Throw stringExpression은 메시지를 한 번 평가하여 새 스크립트 오류를 만듭니다. String이 필요하며 다른 값은 CStr로 명시적으로 변환하세요. 이는 Basic 형식이며 VB.NET의 Throw New Exception(...)이 아닙니다. 처리기가 없으면 현재 실행이 실패하고 다른 모든 스크립트가 정지하는 것은 아닙니다.
- `Throw` — 메시지 없는 Throw는 Catch와 그 안의 중첩 블록에서만 쓸 수 있습니다. 원래 메시지, 파일, 줄을 유지하며 활성 오류를 다시 던집니다. Catch에서 호출한 도우미 함수는 이 형식을 쓰려면 자체 Catch가 있어야 합니다.

## 반환값

Try/Catch/Finally와 Throw는 ID, 숫자, Boolean을 반환하지 않습니다. Catch는 name에 메시지를 제공하며 Throw는 값을 반환하지 않고 제어를 옮깁니다. 예제는 Main에서 두 String과 Integer 13을 명시적으로 반환합니다. 내부 API 호출의 반환 규칙은 그대로입니다.

## 동작

- 준비 단계는 블록을 검증하고 GoTo/On Error GoTo로 Try, Catch, Finally 안으로 진입하는 것을 금지합니다. 생성기는 처리기와 마무리 주소를 기록합니다. 각 호출은 자체 활성 처리기를 가지며 오류는 가장 가까운 적절한 Catch로 갑니다. Catch에서 발생한 오류는 자신의 Finally를 거쳐 바깥 처리기로 전달됩니다. 구조적 처리기가 없으면 일반 On Error 규칙이 적용될 수 있습니다.
- Finally 동안 대기 중인 반환, 오류, 바깥 이동을 보관합니다. 중첩 마무리는 안쪽에서 바깥쪽으로 실행됩니다. Finally의 새 오류는 기존 오류를 대체합니다. Basic는 Finally 안의 Return과 바깥 이동도 허용하며 대기 중인 후속 실행을 바꿉니다. 이는 VB.NET과 다릅니다. 다시 던지기는 호출한 도우미를 포함해 최초 실패 위치를 보존합니다.
- 일시 중지/정지 검사는 유지됩니다. Try는 스레드, 재시도, 대기를 만들지 않습니다. 준비된 주소를 재사용하며 일반 조건은 예외 대신 직접 검사해야 합니다. 긴급 정지는 스크립트 마무리를 건너뜁니다. 호스트 소유 자원은 엔진의 별도 수명 관리 규칙을 따릅니다.

## 예제

### 1. 매개변수를 검사하고 메시지 보관

```vb
# CheckedAmount는 Integer amount=-2를 ByVal로 받습니다. 음수여서 Throw "amount must be non-negative"가 발생합니다. Catch는 String을 problem으로 받아 message에 복사하며 As Exception은 객체를 만들지 않습니다. Finally는 finished=1로 설정합니다. Main은 "amount must be non-negative:1"을 반환합니다. 음수가 아니면 정상 반환하고 Catch를 건너뜁니다.
Option Explicit On
Function CheckedAmount(ByVal amount As Integer) As Integer
    If amount < 0 Then
        Throw "amount must be non-negative"
    End If
    Return amount
End Function

Sub Main()
    Dim message=""
    Dim finished=0
    Try
        CheckedAmount(-2)
    Catch problem As Exception
        message=problem
    Finally
        finished=1
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**매개변수 및 실행 설명:**

CheckedAmount는 Integer amount=-2를 ByVal로 받습니다. 음수여서 Throw "amount must be non-negative"가 발생합니다. Catch는 String을 problem으로 받아 message에 복사하며 As Exception은 객체를 만들지 않습니다. Finally는 finished=1로 설정합니다. Main은 "amount must be non-negative:1"을 반환합니다. 음수가 아니면 정상 반환하고 Catch를 건너뜁니다.

### 2. 바깥 처리기로 다시 던지기

```vb
# 안쪽 Throw가 "missing item"을 만듭니다. 안쪽 Catch가 trace=1로 설정하고 메시지 없는 Throw가 같은 오류를 유지합니다. 안쪽 Finally가 2를 붙이고 바깥 Catch가 outerProblem을 message에 복사하며 3을 붙인 뒤 바깥 Finally가 4를 붙입니다. Main은 "1234:missing item"을 반환합니다. trace는 실행 순서이며 오류 코드가 아닙니다.
Option Explicit On
Sub Main()
    Dim trace=0
    Dim message=""
    Try
        Try
            Throw "missing item"
        Catch problem
            trace=1
            Throw
        Finally
            trace=trace*10+2
        End Try
    Catch outerProblem
        message=outerProblem
        trace=trace*10+3
    Finally
        trace=trace*10+4
    End Try
    Return CStr(trace) & ":" & message
End Sub
```

**매개변수 및 실행 설명:**

안쪽 Throw가 "missing item"을 만듭니다. 안쪽 Catch가 trace=1로 설정하고 메시지 없는 Throw가 같은 오류를 유지합니다. 안쪽 Finally가 2를 붙이고 바깥 Catch가 outerProblem을 message에 복사하며 3을 붙인 뒤 바깥 Finally가 4를 붙입니다. Main은 "1234:missing item"을 반환합니다. trace는 실행 순서이며 오류 코드가 아닙니다.

### 3. 시작한 반복마다 마무리하기

```vb
# number는 1, 2, 3이 됩니다. total에는 1만 더합니다. Continue For가 2를 건너뛰고 Exit For가 3에서 끝내기 때문입니다. 시작한 세 Try 모두 Finally를 실행하여 finished=3이 됩니다. Main은 1*10+3=13을 반환합니다. Finally에 오류가 필수인 것은 아니며 반복문 이동은 해당 반복의 마무리를 기다립니다.
Option Explicit On
Sub Main()
    Dim total=0
    Dim finished=0
    For Var number=1 To 3
        Try
            If number=2 Then
                Continue For
            End If
            If number=3 Then
                Exit For
            End If
            total+=number
        Finally
            finished+=1
        End Try
    Next
    Return total*10+finished
End Sub
```

**매개변수 및 실행 설명:**

number는 1, 2, 3이 됩니다. total에는 1만 더합니다. Continue For가 2를 건너뛰고 Exit For가 3에서 끝내기 때문입니다. 시작한 세 Try 모두 Finally를 실행하여 finished=3이 됩니다. Main은 1*10+3=13을 반환합니다. Finally에 오류가 필수인 것은 아니며 반복문 이동은 해당 반복의 마무리를 기다립니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: tryStatement / catchClause / finallyClause / throwStatement
Analysis/TryStructureValidator.cs: VisitTryStatement / VisitSubrutine / VisitCatchClause / VisitThrowStatement
Runtime/Instructions/Generator.cs: Generate(TryStatementContext)
Runtime/Instructions/TryInstruction.cs: TryInstruction / CatchInstruction / FinallyInstruction / EndTryInstruction
Runtime/Interpreter.cs: CallSubrutine / TryHandleStructuredError / Transfer / DeferReturn / Failure
Runtime/SemanticScope.cs: IsLocal / DefineVar / SetVar
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/try-catch-finally-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/throw-statement
-->
