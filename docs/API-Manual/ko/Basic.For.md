# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

For는 도달 가능한 끝값을 포함하는 숫자 범위에서 블록을 반복합니다. 배열 인덱스나 정해진 횟수의 작업에 적합하며 For Each는 요소 값을 순회합니다.

## 정확한 구문

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## 매개변수

- `counter / VAR` — 쓰기 가능한 스칼라 카운터입니다. VAR는 프로시저 안에 선언하며 생략하면 기존 변수를 사용합니다. Option Explicit On에서는 미리 선언하거나 For Var를 사용하세요. 형식은 DIM counter AS Integer로 먼저 선언합니다. 숫자 For 헤더 안의 AS는 지원하지 않습니다.
- `start` — 시작 숫자 식입니다. 한 번 평가하고 대입한 다음 limit와 increment를 평가합니다.
- `limit` — 범위에 포함되는 끝값으로 진입 시 한 번 평가합니다. 양수 단계는 counter <= limit, 음수 단계는 counter >= limit를 확인합니다.
- `increment` — 선택적 숫자 단계로 기본값은 1입니다. 음수나 소수도 가능하지만 0은 잡을 수 있는 오류입니다. 카운터 형식과 단계가 실제로 진행할 수 있어야 합니다.
- `statements / Next / exit` — 본문과 Next는 별도 줄입니다. Next 뒤 이름은 생략 가능하지만 쓰면 카운터와 같아야 합니다. Continue For는 다음 단계로, Exit For는 가장 가까운 For/For Each 밖으로 이동합니다. Break는 종류와 관계없이 가장 가까운 반복문을 끝냅니다.

## 반환값

For, Next, Exit For는 값을 반환하지 않습니다. 카운터는 숫자이며 자동 아이템 ID가 아닙니다. 이 엔진은 정상 종료 후 범위 밖 값 대신 마지막으로 실행한 값을 유지합니다. 본문을 건너뛰면 start, 조기 종료하면 현재 값을 유지합니다. 예제는 Main에서 Integer 12, 28, 395를 반환합니다.

## 동작

- 진입 순서: start 대입, 끝값과 단계 저장, 0 거부, 첫 값 검사입니다. 방향이 맞지 않으면 본문을 건너뛰며 start=limit이면 한 번 실행합니다.
- Next는 counter+step을 검사하고 다음 반복이 범위 안일 때만 대입합니다. 1 To 5 Step 3은 1과 4를 방문합니다. 끝값·단계의 원래 변수를 바꿔도 저장된 값은 바뀌지 않지만 카운터 자체를 바꾸면 다음 단계에 영향을 줍니다.
- 실행 전 구조와 Next 이름을 검사하며 구조 오류는 SC020입니다. 중첩 반복문에는 서로 다른 카운터를 사용하세요. Try를 떠나면 Finally를 실행합니다. 일시 중지와 정지는 유지되지만 자동 지연이나 시간 제한은 없습니다.

## 예제

### 1. 배열 셀 합계

```vb
# values[2]는 인덱스 0,1,2에 2,4,6을 담습니다. Sum은 배열을 ByVal로 받고 index=0에서 시작해 length-1=2를 저장합니다. 기본 단계 1로 세 셀을 방문하고 total=12를 Main에 반환합니다.
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**매개변수 및 실행 설명:**

values[2]는 인덱스 0,1,2에 2,4,6을 담습니다. Sum은 배열을 ByVal로 받고 index=0에서 시작해 length-1=2를 저장합니다. 기본 단계 1로 세 셀을 방문하고 total=12를 Main에 반환합니다.

### 2. 끝에서부터 삭제

```vb
# items에는 -1,3,-2,5가 있습니다. 시작 Count()-1=3, 끝 0, 단계 -1입니다. 음수 요소를 삭제하면 이미 방문한 인덱스만 이동하므로 남은 요소를 놓치지 않습니다. 3과 5가 남아 Count()*10+3+5는 28을 반환합니다.
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**매개변수 및 실행 설명:**

items에는 -1,3,-2,5가 있습니다. 시작 Count()-1=3, 끝 0, 단계 -1입니다. 음수 요소를 삭제하면 이미 방문한 인덱스만 이동하므로 남은 요소를 놓치지 않습니다. 3과 5가 남아 Count()*10+3+5는 28을 반환합니다.

### 3. 저장된 경계와 최종 카운터

```vb
# ReadLimit는 ByRef calls를 증가시키고 value를 반환합니다. 시작 1, 끝 5, 단계 2를 각각 한 번 평가해 calls=3입니다. 본문의 upper=99, stride=1은 이 반복을 바꾸지 않습니다. 1,3,5를 방문하여 total=9, index는 5로 남습니다. Main은 395를 반환합니다.
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**매개변수 및 실행 설명:**

ReadLimit는 ByRef calls를 증가시키고 value를 반환합니다. 시작 1, 끝 5, 단계 2를 각각 한 번 평가해 calls=3입니다. 본문의 upper=99, stride=1은 이 반복을 바꾸지 않습니다. 1,3,5를 방문하여 total=9, index는 5로 남습니다. Main은 395를 반환합니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
