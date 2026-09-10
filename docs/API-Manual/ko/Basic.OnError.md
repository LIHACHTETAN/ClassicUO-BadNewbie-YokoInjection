# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

On Error는 현재 프로시저나 함수에서 이후 실행 오류를 처리할 방식을 선택합니다. API 호출이 아닌 언어 문장입니다. 구조화된 복구와 정리는 Try/Catch/Finally를 사용하세요.

## 정확한 구문

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## 매개변수

- `label` — 같은 프로시저에 있는 레이블을 label:로 별도 줄에 씁니다. On Error 전후 모두 가능하며 대소문자를 구분하지 않습니다. 함수명, 문자열, 소스 줄 번호가 아닙니다. 없는 레이블은 SC009를 발생시키며 클라이언트가 실행을 막습니다.
- `Resume Next / On Error` — On Error Resume Next는 레이블로 이동하지 않고 실패한 명령 다음으로 자동 진행합니다. 성공한 명령에는 영향이 없습니다. 현재 프로시저 호출에만 적용하며 모든 스크립트에 적용하지 않습니다.
- `0` — On Error GoTo 0은 모드를 끕니다. 0은 특별한 제어값이지 레이블이나 Boolean 결과가 아닙니다. 다른 숫자 레이블과 GoTo -1은 지원하지 않습니다.
- `Resume / Resume Next` — 처리기 안의 Resume는 실패한 명령을 재시도하고 Resume Next는 그 다음으로 갑니다. 기록된 실행 오류가 필요하며 이동 후 그 주소를 지웁니다. 레이블이나 시간 제한 인수를 받지 않습니다.

## 반환값

On Error와 Resume에는 반환값이 없습니다. 잡은 오류가 TRUE/FALSE로 바뀌거나 대입이 자동 복구되지 않습니다. 예제는 Integer 5,18,10을 명시적으로 반환합니다. 앞서 발생한 부수 효과는 자동으로 되돌리지 않습니다.

## 동작

- 준비 단계에서 프로시저 전체를 읽은 뒤 레이블을 해결하므로 양방향 모두 됩니다. 실행 중 모드를 저장하며 예외가 생기면 구조화된 Try를 먼저, On Error를 나중에 고려합니다.
- 엔진은 실패한 명령 주소를 기록합니다. 레이블 모드는 처리기로, 자동 Resume Next는 명령 다음으로 갑니다. Resume는 식과 호출을 다시 평가하므로 원인을 먼저 고치고 반복되는 부수 효과를 고려하세요.
- GoTo 0은 보류된 실패 주소를 지우지 않습니다. 처리기는 자신을 끄고 복구한 뒤 Resume할 수 있습니다. 오류 가능한 처리기 작업 전에 모드를 꺼 같은 처리기로 재진입하지 않게 하세요.
- 문법 오류와 실행 취소는 복구하지 않습니다. 명령이 예외 없이 0, FALSE, 실패 상태만 반환하면 On Error는 호출되지 않습니다. 해당 명령의 결과를 검사하세요.
- Return이나 GoTo로 정상 흐름이 처리기에 들어가지 않게 하세요. 호출된 프로시저는 고유 상태를 가지며 미처리 오류가 호출자로 전달될 수 있습니다. 그곳의 Resume는 내부 한 줄이 아닌 전체 호출 명령을 반복합니다. 자동 재시도 제한이나 대기는 없습니다.

## 예제

### 1. 실패한 대입 하나 건너뛰기

```vb
# values[0]은 한 셀이며 인덱스 5는 잘못되었습니다. result=1입니다. On Error Resume Next가 대입 전 실패한 읽기를 건너뛰어 1을 유지합니다. GoTo 0으로 끄고 result+=4를 하면 5입니다. Main은 5를 반환하지만 읽기 성공을 뜻하지 않습니다.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**매개변수 및 실행 설명:**

values[0]은 한 셀이며 인덱스 5는 잘못되었습니다. result=1입니다. On Error Resume Next가 대입 전 실패한 읽기를 건너뛰어 1을 유지합니다. GoTo 0으로 끄고 result+=4를 하면 5입니다. Main은 5를 반환하지만 읽기 성공을 뜻하지 않습니다.

### 2. 수정 후 재시도

```vb
# ReadCell은 셀 0에 8을 저장하지만 index=2입니다. 오류로 FixIndex에 갑니다. GoTo 0으로 끄고 handled=1, index=0으로 바꿉니다. Resume가 result=values[index]를 반복해 8을 저장합니다. Return은 정상 흐름의 처리기 진입을 막으며 Main은 18을 받습니다.
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**매개변수 및 실행 설명:**

ReadCell은 셀 0에 8을 저장하지만 index=2입니다. 오류로 FixIndex에 갑니다. GoTo 0으로 끄고 handled=1, index=0으로 바꿉니다. Resume가 result=values[index]를 반복해 8을 저장합니다. Return은 정상 흐름의 처리기 진입을 막으며 Main은 18을 받습니다.

### 3. 등록보다 앞선 처리기

```vb
# 처음 GoTo Work로 Failed를 건너뜁니다. On Error GoTo Failed가 앞선 레이블을 등록합니다. 인덱스 2는 result를 바꾸기 전에 실패합니다. 처리기는 자신을 끄고 handled를 늘린 뒤 Resume Next로 Return에 갑니다. 결과는 10이며 레이블은 별도 프로시저가 아닙니다.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**매개변수 및 실행 설명:**

처음 GoTo Work로 Failed를 건너뜁니다. On Error GoTo Failed가 앞선 레이블을 등록합니다. 인덱스 2는 result를 바꾸기 전에 실패합니다. 처리기는 자신을 끄고 handled를 늘린 뒤 Resume Next로 Return에 갑니다. 결과는 10이며 레이블은 별도 프로시저가 아닙니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
