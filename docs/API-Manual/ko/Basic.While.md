# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

While는 매 반복 전에 조건을 검사하고 참인 동안 본문을 반복합니다. 이 엔진은 Wend로 닫으며 VB.NET의 End While 표기는 지원하지 않습니다.

## 정확한 구문

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## 매개변수

- `condition` — 첫 검사와 마지막 검사를 포함해 매번 다시 평가하는 식입니다. 비교나 숫자 Boolean을 사용하세요. 0/False는 종료, 1/True 및 다른 0이 아닌 숫자는 계속합니다. 텍스트를 Boolean으로 해석하지 않습니다.
- `statements` — 작업을 수행하고 조건을 진행시키는 본문 명령입니다. 첫 조건이 거짓이면 본문 전체를 건너뜁니다.
- `Wend / exit` — Wend는 조건으로 돌아갑니다. Continue While는 다시 검사하고 Exit While는 다른 종류의 내부 반복문을 넘어 가장 가까운 While를 끝냅니다. Break는 종류와 관계없이 가장 가까운 반복문을 끝냅니다.

## 반환값

While, Wend, Exit While, Break는 반환값이 없습니다. 본문의 RETURN은 프로시저/함수 전체를 종료합니다. 예제는 Integer 6,1,406을 반환합니다. 검색 결과 1은 배열 인덱스이지 성공 Boolean이 아닙니다.

## 동작

- 검사, 본문 실행, 검사로 복귀하는 순서입니다. 숫자 경계를 저장하거나 카운터를 자동 증가시키지 않습니다.
- 진행을 명시적으로 작성하세요. 게임 상태를 반복 조회할 때 적절한 Wait와 기한을 추가하세요. While 자체는 대기하거나 시간 초과되지 않습니다. 일시 중지와 정지는 계속 사용할 수 있습니다.
- Continue나 종료로 떠나는 Try의 Finally는 실행됩니다. 헤더, 명령, Wend는 프로시저나 함수 안에서 각각 별도 줄로 작성합니다.

## 예제

### 1. 자릿수 합계

```vb
# DigitSum은 number=123을 ByVal로 받습니다. MOD 10으로 마지막 자리를 읽고 Fix(number/10)으로 제거합니다: 123→12→1→0. total=3+2+1=6이며 마지막 거짓 조건으로 끝나 Main이 6을 받습니다. 입력 0이면 본문 없이 0을 반환합니다.
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**매개변수 및 실행 설명:**

DigitSum은 number=123을 ByVal로 받습니다. MOD 10으로 마지막 자리를 읽고 Fix(number/10)으로 제거합니다: 123→12→1→0. total=3+2+1=6이며 마지막 거짓 조건으로 끝나 Main이 6을 받습니다. 입력 0이면 본문 없이 0을 반환합니다.

### 2. 첫 일치 찾기

```vb
# FirstAbove는 values=[4,7,9], threshold=6을 받습니다. 길이 검사가 values[index]를 보호합니다. index=1에서 7>6이므로 found=1을 저장하고 Exit While로 끝냅니다. 일치가 없으면 -1이며 Main은 0부터 세는 인덱스 1을 반환합니다.
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**매개변수 및 실행 설명:**

FirstAbove는 values=[4,7,9], threshold=6을 받습니다. 길이 검사가 values[index]를 보호합니다. index=1에서 7>6이므로 found=1을 저장하고 Exit While로 끝냅니다. 일치가 없으면 -1이며 Main은 0부터 세는 인덱스 1을 반환합니다.

### 3. 조건 검사 횟수

```vb
# CanContinue는 checks를 ByRef, index와 limit=3을 ByVal로 받습니다. checks를 늘린 후 index<limit를 1/0으로 반환합니다. index=0,1,2,3에서 검사하므로 세 반복에 네 호출입니다. total=6이며 Main은 406을 반환합니다.
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**매개변수 및 실행 설명:**

CanContinue는 checks를 ByRef, index와 limit=3을 ByVal로 받습니다. checks를 늘린 후 index<limit를 1/0으로 반환합니다. index=0,1,2,3에서 검사하므로 세 반복에 네 호출입니다. total=6이며 Main은 406을 반환합니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
