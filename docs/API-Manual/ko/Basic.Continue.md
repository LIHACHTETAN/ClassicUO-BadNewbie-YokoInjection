# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Continue는 지정한 종류의 가장 가까운 바깥 반복문에서 남은 본문을 건너뜁니다. Continue For는 숫자 For와 For Each, Continue Do는 Do/Loop와 Repeat/Until, Continue While는 While/Wend에 씁니다.

## 정확한 구문

```text
Continue For
Continue Do
Continue While
```

## 매개변수

- `kind` — kind: Continue 뒤에 For, Do, While 중 하나가 필수이며 괄호는 없습니다. 같은 프로시저에서 해당 반복문이 문장을 감싸야 합니다. 다른 종류의 안쪽 반복문은 이동을 가로채지 않습니다.

## 반환값

Continue는 반환값이 없으며 식에 쓸 수 없습니다. TRUE/FALSE도 아니고 프로시저를 다시 시작하지도 않습니다. 함수는 나중에 RETURN으로 결과를 반환할 수 있으며 예제는 Integer 10, 3, 34를 반환합니다.

## 동작

- For는 NEXT에서 STEP을 적용하고 다음 값을 범위와 비교합니다. For Each는 다음 요소를 가져오며 끝나면 종료합니다. 카운터 초기화나 컬렉션 식 평가는 반복하지 않습니다.
- Do의 시작 조건은 시작에서, Loop의 끝 조건은 끝에서 다시 확인합니다. Repeat/Until은 UNTIL을 사용합니다. 무조건 Do/Loop는 명시적 종료나 중지까지 계속됩니다. While는 WHILE을 재검사하며 Continue Do는 While/Wend를 선택하지 않습니다.
- 준비할 때 가장 가까운 해당 반복문의 주소를 찾습니다. 없으면 Option Explicit 없이도 초기화 전에 SC020을 냅니다. NEXT 이름과 끝도 검사하며 IF 경계를 넘는 기존 FOR/NEXT 호환성은 유지합니다.
- TRY/CATCH를 벗어날 때 거치는 FINALLY를 안에서 밖으로 각각 한 번 실행합니다. 반복문 전체가 TRY 안에 있으면 그 FINALLY는 매회 실행하지 않습니다. FINALLY의 RETURN이나 오류는 보류된 이동을 대체합니다.
- Continue는 기다리지 않습니다. 조회 반복에서는 조건을 갱신하거나 알맞은 대기를 넣어 무한 반복을 피해야 합니다. 일시 정지·중지 확인은 유지됩니다. 벗어난 네이티브 열거자는 해제되며 실행은 서로 독립적입니다. Exit For/Do/While는 다음 반복 대신 종료합니다.

## 예제

### 1. 요소 건너뛰기

```vb
# values는 -2, 4, 0, 6입니다. item<=0이면 -2와 0에서 Continue For를 실행해 total+=item을 건너뜁니다. For Each도 같은 형식입니다. SumPositive와 Main은 4+6인 Integer 10을 반환합니다.
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**매개변수 및 실행 설명:**

values는 -2, 4, 0, 6입니다. item<=0이면 -2와 0에서 Continue For를 실행해 total+=item을 건너뜁니다. For Each도 같은 형식입니다. SumPositive와 Main은 4+6인 Integer 10을 반환합니다.

### 2. 종류로 바깥 반복 선택

```vb
# AdvanceTo는 limit=3을 받으며 count는 0에서 시작합니다. While True 안에서 count를 늘린 뒤 Continue Do로 바깥 Do에 이동합니다. 조건을 재검사하며 count=3에서 끝나 Integer 3을 반환합니다.
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**매개변수 및 실행 설명:**

AdvanceTo는 limit=3을 받으며 count는 0에서 시작합니다. While True 안에서 count를 늘린 뒤 Continue Do로 바깥 Do에 이동합니다. 조건을 재검사하며 count=3에서 끝나 Integer 3을 반환합니다.

### 3. 건너뛴 반복도 정리

```vb
# Process는 limit=3, skip=2를 받습니다. i는 1, 2, 3입니다. 두 번째는 total+=i를 건너뛰지만 Finally는 cleanup을 세 번 늘립니다. total=4, cleanup=3이므로 RETURN cleanup*10+total은 Integer 34입니다.
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**매개변수 및 실행 설명:**

Process는 limit=3, skip=2를 받습니다. i는 1, 2, 3입니다. 두 번째는 total+=i를 건너뛰지만 Finally는 cleanup을 세 번 늘립니다. total=4, cleanup=3이므로 RETURN cleanup*10+total은 Integer 34입니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
