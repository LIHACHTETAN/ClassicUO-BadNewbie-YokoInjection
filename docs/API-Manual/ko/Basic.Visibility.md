# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Public은 모듈 멤버를 외부 코드에 공개합니다. Private는 같은 모듈의 함수, 프로시저, 초기화 식에서만 접근할 수 있습니다. 한정자는 호출이 아닌 선언 앞에 씁니다.

## 정확한 구문

```text
Public declaration
Private declaration
```

## 매개변수

- `visibility` — visibility: Public 또는 Private입니다. 생략하면 모듈 SUB/FUNCTION은 공개, VAR/DIM/CONST는 비공개입니다.
- `declaration` — declaration: SUB/FUNCTION, 스칼라 VAR/DIM 또는 CONST입니다. Public은 Module과 파일 수준 선언에도 쓸 수 있습니다. 파일 수준이나 프로시저 본문의 Private는 금지됩니다. 멤버 선언 이름에는 점을 넣지 않습니다.

## 반환값

Public과 Private는 값을 반환하지 않고 필드 형식이나 함수 결과도 바꾸지 않습니다. Normalize(12)는 RETURN으로 Integer 10을 반환합니다. NextCount()는 새 개수를 반환하며 TRUE/FALSE가 아닙니다.

## 동작

- Module 안에서는 자신의 짧은 이름과 전체 이름을 쓸 수 있습니다. 외부에서는 ModuleName.Member로 Public만 접근합니다. Public이 짧은 전역 이름을 만드는 것은 아닙니다.
- Option Explicit Off에서도 실행 전에 접근을 검사합니다. 다른 모듈의 Private 접근은 SC019, 잘못된 모듈/한정자 선언은 SC018 또는 구문 오류입니다. 이런 오류가 있으면 초기화 식도 실행하지 않습니다.
- 공개 함수는 비공개 도우미를 호출할 수 있으며 호출 함수가 선언된 모듈을 기준으로 판단합니다. 비공개 도우미는 IDE, 단축키, 외부 프로시저 API에서 따로 시작할 수 없습니다.
- Public Const는 여전히 변경 불가이고 Public Var는 변경 가능합니다. 명시적인 지역 변수는 자신의 프로시저 안에서만 동명 필드를 가립니다. Private는 소스를 암호화하거나 소유자에게 코드를 숨기지 않습니다.
- 디버거의 짧은 이름과 Private 접근은 선택한 프레임에 따릅니다. 모듈 안에서는 필드를 읽을 수 있지만 외부 호출자로 전환하면 ModuleName.privateField 식은 거부됩니다.

## 예제

### 1. 공개 입구와 비공개 도우미

```vb
# value=12가 Limits.Normalize와 Clamp로 전달됩니다. maximum=10으로 제한해 두 함수는 Integer 10을 반환합니다. Main은 Normalize만 호출하며 외부 Limits.Clamp(12) 호출은 금지됩니다.
Option Explicit On
Module Limits
    Private Const maximum = 10
    Private Function Clamp(ByVal value)
        If value > maximum Then
            Return maximum
        End If
        Return value
    End Function
    Public Function Normalize(ByVal value)
        Return Clamp(value)
    End Function
End Module
Sub Main()
    Return Limits.Normalize(12)
End Sub
```

**매개변수 및 실행 설명:**

value=12가 Limits.Normalize와 Clamp로 전달됩니다. maximum=10으로 제한해 두 함수는 Integer 10을 반환합니다. Main은 Normalize만 호출하며 외부 Limits.Clamp(12) 호출은 금지됩니다.

### 2. 비공개 필드와 지역 변수

```vb
# 한정자 없는 VAR value=7은 Store 내부의 비공개 필드입니다. Read는 필드 7을 반환하고 LocalValue는 자신의 value=9를 선언해 필드를 바꾸지 않습니다. Main은 7*10+9, Integer 79를 반환합니다.
Option Explicit On
Module Store
    Var value = 7
    Public Function Read()
        Return value
    End Function
    Public Function LocalValue()
        Var value = 9
        Return value
    End Function
End Module
Sub Main()
    Return Store.Read() * 10 + Store.LocalValue()
End Sub
```

**매개변수 및 실행 설명:**

한정자 없는 VAR value=7은 Store 내부의 비공개 필드입니다. Read는 필드 7을 반환하고 LocalValue는 자신의 value=9를 선언해 필드를 바꾸지 않습니다. Main은 7*10+9, Integer 79를 반환합니다.

### 3. 공개 상수와 내부 카운터

```vb
# Public Const increment=2는 Counter.increment로 읽습니다. Private count는 1로 시작합니다. NextCount는 increment를 더해 3을 저장하고 반환합니다. Main은 3*10+2, Integer 32를 반환합니다. 외부 Counter.count 접근과 increment 변경은 금지됩니다.
Option Explicit On
Module Counter
    Public Const increment = 2
    Private Var count = 1
    Public Function NextCount()
        count += increment
        Return count
    End Function
End Module
Sub Main()
    Var result = Counter.NextCount()
    Return result * 10 + Counter.increment
End Sub
```

**매개변수 및 실행 설명:**

Public Const increment=2는 Counter.increment로 읽습니다. Private count는 1로 시작합니다. NextCount는 increment를 더해 3을 저장하고 반환합니다. Main은 3*10+2, Integer 32를 반환합니다. 외부 Counter.count 접근과 increment 변경은 금지됩니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
