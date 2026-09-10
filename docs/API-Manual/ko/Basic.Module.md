# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Module은 함수, 프로시저, VAR/DIM, CONST를 하나의 이름으로 묶습니다. 외부에서는 Tools.Sum 또는 Counter.count를 쓰며, 현재 모듈 안에서는 짧은 멤버 이름을 사용할 수 있습니다.

## 정확한 구문

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## 매개변수

- `moduleName` — moduleName: Tools와 같은 단순 식별자이며 대소문자를 구분하지 않습니다. UO는 예약되어 있습니다. 중복 이름과 중첩 Module은 허용하지 않습니다.
- `members` — members: SUB/FUNCTION, 스칼라 VAR/DIM, CONST, Include와 유효한 Option Explicit입니다. 필드에 배열이나 객체 값을 저장할 수 있습니다. 모듈 바로 아래의 DIM[...]은 지원하지 않으므로 함수로 배열을 만들어 VAR에 저장하세요.
- `member / arguments` — member / arguments: 멤버 이름과 함수 인수입니다. Tools.Sum(2, 3)은 left=2, right=3을 전달합니다. Counter.count 필드에는 괄호가 필요 없습니다.

## 반환값

Module 자체에는 반환값이 없으며 Module(...)처럼 호출하지 않습니다. Tools.Sum(...)은 함수의 RETURN 값을, 필드는 저장된 값을 반환합니다. 비교 결과는 Integer 1/0으로 조건과 비교에서 TRUE/FALSE에 대응합니다. 임의의 숫자, ID, 개수가 모두 불리언 결과인 것은 아닙니다.

## 동작

- 파일 수준에서 Module을 선언하고 End Module로 닫습니다. Include로 모듈 전체나 멤버를 불러올 수 있으며 오류에는 원본 파일과 줄이 유지됩니다. Option Explicit는 실제 파일 단위로 적용됩니다.
- 준비 단계에서 전체 이름을 수집하고 짧은 참조를 현재 모듈에 연결하며 실행 전에 접근을 검사합니다. 명시적인 지역 매개변수, VAR, CONST, DIM은 같은 이름의 필드를 가립니다. 그 외에는 모듈 필드, 기존 전역 변수 순서로 찾습니다.
- 독립 실행을 시작할 때 선언 순서대로 필드를 초기화합니다. 같은 실행의 중첩 호출은 필드 변경을 공유합니다. 새 실행은 다시 초기화하며 동시에 실행하는 스크립트끼리는 상태를 공유하지 않습니다. 디스크 저장 기능이 아닙니다.
- 함수/프로시저의 기본 접근은 Public이고 필드/상수는 Private입니다. Private는 Module 안에서만 허용됩니다. Public / Private를 참고하세요.
- IDE는 전체 프로시저 이름을 표시합니다. 필수 인수가 없는 공개 프로시저는 목록에서 실행할 수 있고 비공개 도우미는 내부용으로 남습니다. 완성, 정의 이동, 변수 조회는 현재 모듈 범위를 따릅니다.

## 예제

### 1. 다른 모듈의 같은 이름

```vb
# Tools.Sum은 left=2와 right=3을 더해 5를, Other.Sum은 곱해 6을 반환합니다. 전체 이름으로 구별하며 Main은 Integer 11을 반환합니다.
Option Explicit On
Module Tools
    Public Function Sum(ByVal left, ByVal right)
        Return left + right
    End Function
End Module
Module Other
    Public Function Sum(ByVal left, ByVal right)
        Return left * right
    End Function
End Module
Sub Main()
    Return Tools.Sum(2, 3) + Other.Sum(2, 3)
End Sub
```

**매개변수 및 실행 설명:**

Tools.Sum은 left=2와 right=3을 더해 5를, Other.Sum은 곱해 6을 반환합니다. 전체 이름으로 구별하며 Main은 Integer 11을 반환합니다.

### 2. 한 실행의 공유 필드

```vb
# count는 0으로 시작합니다. Increment마다 같은 필드에 1을 더하므로 두 번 호출하면 before=2입니다. Counter.count=5 변경은 Read에도 보입니다. Main은 2*10+5, Integer 25를 반환합니다. 새 실행은 다시 0으로 시작합니다.
Option Explicit On
Module Counter
    Public Var count As Integer = 0
    Public Sub Increment()
        count += 1
    End Sub
    Public Function Read()
        Return count
    End Function
End Module
Sub Main()
    Counter.Increment()
    Counter.Increment()
    Var before = Counter.Read()
    Counter.count = 5
    Return before * 10 + Counter.Read()
End Sub
```

**매개변수 및 실행 설명:**

count는 0으로 시작합니다. Increment마다 같은 필드에 1을 더하므로 두 번 호출하면 before=2입니다. Counter.count=5 변경은 Read에도 보입니다. Main은 2*10+5, Integer 25를 반환합니다. 새 실행은 다시 0으로 시작합니다.

### 3. 불리언 함수 결과

```vb
# maximum=4는 Limits 내부에서 접근합니다. Allowed(3)은 Integer 1, Allowed(7)은 Integer 0입니다. accepted=TRUE와 rejected=FALSE로 확인하며 성공하면 Main은 Integer 10을 반환합니다.
Option Explicit On
Module Limits
    Private Const maximum = 4
    Public Function Allowed(ByVal amount)
        Return amount <= maximum
    End Function
End Module
Sub Main()
    Var accepted = Limits.Allowed(3)
    Var rejected = Limits.Allowed(7)
    If accepted = TRUE AndAlso rejected = FALSE Then
        Return 10
    End If
    Return 0
End Sub
```

**매개변수 및 실행 설명:**

maximum=4는 Limits 내부에서 접근합니다. Allowed(3)은 Integer 1, Allowed(7)은 Integer 0입니다. accepted=TRUE와 rejected=FALSE로 확인하며 성공하면 Main은 Integer 10을 반환합니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
