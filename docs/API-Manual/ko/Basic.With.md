# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

With는 저장한 하나의 객체에 대한 작업을 묶습니다. 이름 앞의 점은 그 객체의 멤버를 뜻합니다. With UO와 With moduleName은 이름 공간을 명시적으로 선택하는 Basic 확장 형식입니다.

## 정확한 구문

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## 매개변수

- `objectExpression / UO / moduleName` — 대상은 필수이며 List(), Dictionary() 같은 네이티브 객체, 객체를 가진 변수 또는 객체를 반환하는 함수입니다. 식은 진입할 때 한 번만 평가하며 본문이 비어 있어도 평가합니다. 이 엔진에서 숫자, 문자열, 배열, Unit은 객체 대상이 아닙니다. 같은 이름의 지역 객체 변수가 모듈보다 우선합니다.
- `.Method(arguments) / .field` — 객체 메서드는 괄호와 함께 사용합니다: .Add(value), .Item(index), .Count(). 인수와 결과는 그대로이며 Basic.List/Basic.Dictionary를 참고하세요. 임의 객체 필드나 속성은 여기서 지원하지 않습니다. 모듈에서는 접근 가능한 .field와 .Procedure(arguments)를 쓸 수 있으며 Private 규칙도 적용됩니다. With UO 안의 .Command(...)는 UO.Command(...)입니다. 밖에서는 게임 명령에 계속 UO가 필요합니다.
- `statements / End With` — 본문은 비어 있거나 호출, 대입, 조건 및 올바르게 중첩된 반복문과 블록을 포함할 수 있습니다. End With는 필수입니다. 본문 밖에서는 점으로 시작하는 멤버 이름을 쓸 수 없습니다. 다른 객체는 전체 이름으로 접근할 수 있습니다.

## 반환값

With는 자체 반환값이 없는 제어 블록입니다. ID, Boolean, 성공 여부를 반환하지 않습니다. 호출한 메서드는 각각의 반환 규칙을 유지합니다. 예제의 Return은 Main에서 Integer를 명시적으로 반환하며 127, 28, 72는 예제 계산값입니다.

## 동작

- 준비 단계에서 블록을 검사하고 상대 이름을 연결합니다. 진입할 때 식을 평가하여 현재 호출에 객체 참조를 저장합니다. 원래 변수에 다른 객체를 대입해도 참조는 바뀌지 않습니다. 머리 부분으로 다시 진입하면 재평가하며 재귀 호출은 각자의 참조를 가집니다.
- 안쪽 With의 머리 식은 바깥 문맥에서 평가합니다. 안쪽 본문의 점은 안쪽 객체를 가리키며 End With 뒤에는 바깥 문맥이 복원됩니다. Return, 반복문 이동, 바깥으로 향하는 GoTo는 관련 Finally를 실행한 뒤 벗어난 범위를 제거합니다. With 본문 안으로 바로 이동하는 것은 금지됩니다.
- 잘못된 대상이나 알 수 없는 메서드는 false가 아니라 오류를 발생시킵니다. Catch/On Error로 처리할 수 있습니다. 대상 평가가 실패하면 On Error Resume Next가 블록 전체를 건너뜁니다. With는 자체 반복, 대기, 스레드 생성을 하지 않습니다. 일시 중지와 정지 검사는 유지됩니다. 연결된 이름은 준비된 스크립트와 함께 캐시되며 메서드마다 대상 식을 다시 평가하지 않습니다.

## 예제

### 1. 한 번만 평가

```vb
# Choose는 values를 ByVal, calls를 ByRef로 받아 calls를 1로 늘리고 원래 목록을 반환합니다. 중간에 values에 새 목록을 대입해도 두 .Add는 저장한 목록에 2와 7을 추가합니다. Item은 0과 1 인덱스를 사용합니다. Main은 1*100+2*10+7=127을 반환합니다.
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**매개변수 및 실행 설명:**

Choose는 values를 ByVal, calls를 ByRef로 받아 calls를 1로 늘리고 원래 목록을 반환합니다. 중간에 values에 새 목록을 대입해도 두 .Add는 저장한 목록에 2와 7을 추가합니다. Item은 0과 1 인덱스를 사용합니다. Main은 1*100+2*10+7=127을 반환합니다.

### 2. 중첩 객체와 마무리

```vb
# groups는 문자열 키 "child"에 목록 child를 저장합니다. .Item("child")가 바깥 사전에서 객체를 가져옵니다. 안쪽 .Add(2)와 Finally의 .Add(7)이 목록을 변경합니다. End With 뒤의 .Set("result",8)은 다시 사전에 적용됩니다. Count()는 2, Item("result")는 8을 반환하므로 Main은 28을 반환합니다.
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**매개변수 및 실행 설명:**

groups는 문자열 키 "child"에 목록 child를 저장합니다. .Item("child")가 바깥 사전에서 객체를 가져옵니다. 안쪽 .Add(2)와 Finally의 .Add(7)이 목록을 변경합니다. End With 뒤의 .Set("result",8)은 다시 사전에 적용됩니다. Count()는 2, Item("result")는 8을 반환하므로 Main은 28을 반환합니다.

### 3. 모듈과 UO

```vb
# With Tools는 .total, .AddAmount, .CountItems가 속한 모듈을 지정합니다. total은 4로 시작하고 AddAmount가 amount=3을 ByVal로 받아 7이 됩니다. CountItems는 두 요소 배열을 받아 With UO를 통해 UO.GetArrayLength(values)를 호출하여 2를 얻습니다. Main은 7*10+2=72를 계산합니다. 모듈 접근 규칙은 그대로 적용됩니다.
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**매개변수 및 실행 설명:**

With Tools는 .total, .AddAmount, .CountItems가 속한 모듈을 지정합니다. total은 4로 시작하고 AddAmount가 amount=3을 ByVal로 받아 7이 됩니다. CountItems는 두 요소 배열을 받아 With UO를 통해 UO.GetArrayLength(values)를 호출하여 2를 얻습니다. Main은 7*10+2=72를 계산합니다. 모듈 접근 규칙은 그대로 적용됩니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
