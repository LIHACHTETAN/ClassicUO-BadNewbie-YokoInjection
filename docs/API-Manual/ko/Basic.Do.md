# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Do는 본문 전이나 후에 조건을 검사합니다. While는 참인 동안, Until은 참이 될 때까지 반복합니다. Repeat … Until은 본문 뒤에 검사하는 지원되는 기존 형식입니다.

## 정확한 구문

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## 매개변수

- `condition / While / Until` — 숫자 Boolean 식 0/False 또는 1/True입니다. While는 참이면 계속하고 Until은 참이면 끝냅니다. 매 검사마다 다시 평가하며 텍스트를 Boolean으로 해석하지 않습니다.
- `position / Repeat` — Do 뒤 조건은 첫 실행을 생략할 수 있습니다. Loop 뒤나 Repeat의 Until은 최소 한 번 실행한 뒤 검사합니다. 조건 위치는 하나만 허용합니다. 무조건 Do … Loop에는 명시적 종료가 필요합니다.
- `statements / exit` — 본문입니다. Continue Do는 다음 조건 검사로 이동하고 Exit Do는 가장 가까운 Do나 Repeat를 끝냅니다. Break는 종류와 무관하게 가장 가까운 반복문을 종료합니다. RETURN은 프로시저/함수 전체를 끝냅니다.

## 반환값

Do, Loop, Repeat, Until, Exit Do에는 반환값이 없습니다. 예제는 Main에서 Integer 1,33,83을 명시적으로 반환하며 이는 결합된 카운터 값이지 명령의 Boolean 결과가 아닙니다.

## 동작

- 준비 단계에서 블록과 이동을 검사합니다. 같은 Do의 처음과 끝 모두에 조건을 지정하면 SC020입니다. 엔진은 선택한 위치에서 평가하고 While/Until 규칙으로 반복합니다.
- 후조건의 Continue Do는 끝 조건을 반드시 검사하며 전조건이면 헤더로 돌아갑니다. Try를 떠나는 이동 전에 Finally가 정확히 한 번 실행됩니다.
- Repeat는 먼저 실행하므로 빈 배열은 진입 전에 처리하세요. 암묵적 시간 제한은 없습니다. 게임 대기에는 Wait와 기한을 사용하며 일시 중지·정지 검사는 유지됩니다.

## 예제

### 1. 전후 검사 차이

```vb
# ready=True는 이미 Until을 만족합니다. Do Until ready는 0번 실행하여 before=0입니다. 두 번째 반복은 증가 후 검사하므로 after=1입니다. Main은 before*10+after=1을 반환합니다.
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**매개변수 및 실행 설명:**

ready=True는 이미 Until을 만족합니다. Do Until ready는 0번 실행하여 before=0입니다. 두 번째 반복은 증가 후 검사하므로 after=1입니다. Main은 before*10+after=1을 반환합니다.

### 2. 제한된 시도와 정리

```vb
# attempts는 0에서 시작해 매번 늘어납니다. 첫 두 Continue Do는 Finally를 실행한 뒤 attempts<4를 검사합니다. 세 번째 Exit Do도 Finally를 실행합니다. attempts=3, cleanup=3이므로 33입니다. 실제 네트워크 재시도가 아닌 로컬 시뮬레이션입니다.
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**매개변수 및 실행 설명:**

attempts는 0에서 시작해 매번 늘어납니다. 첫 두 Continue Do는 Finally를 실행한 뒤 attempts<4를 검사합니다. 세 번째 Exit Do도 Finally를 실행합니다. attempts=3, cleanup=3이므로 33입니다. 실제 네트워크 재시도가 아닌 로컬 시뮬레이션입니다.

### 3. 종료 표식을 읽는 기존 반복문

```vb
# values=[3,5,0]은 비어 있지 않습니다. Repeat는 셀을 읽고 index를 늘려 합산합니다. Until은 0이나 배열 끝에서 멈추며 0을 찾으면 OrElse가 두 번째 검사를 생략합니다. total=8, index=3으로 83을 반환합니다.
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**매개변수 및 실행 설명:**

values=[3,5,0]은 비어 있지 않습니다. Repeat는 셀을 읽고 index를 늘려 합산합니다. Until은 0이나 배열 끝에서 멈추며 0을 찾으면 OrElse가 두 번째 검사를 생략합니다. total=8, index=3으로 83을 반환합니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
