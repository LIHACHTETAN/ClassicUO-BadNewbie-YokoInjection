# SUB Main()

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Basic 파일에는 프로시저/함수 정의와 선택적 전역 선언을 넣습니다. 실행할 작업은 프로시저 안에 둡니다. 다음 예제는 Main()을 진입점으로 하는 완전한 파일이며 프로시저 밖에 붙일 코드 조각이 아닙니다.

## 정확한 구문

```text
Option Explicit On
SUB Main()
    statement
END SUB
# comment
; comment
REM comment
// comment
' comment
```

## 매개변수

- `Main / entry` — 실행 대상으로 선택한 프로시저입니다. Main은 관용적인 이름이며 자동 실행 명령이 아닙니다. SUB Main()은 인수 없는 프로시저를 선언합니다. 보조 함수는 호출될 때만 동작합니다.
- `statement` — SUB…END SUB 또는 FUNCTION…END FUNCTION 안에서 실행문을 한 줄에 하나씩 씁니다. 전역 VAR/CONST와 Option Explicit는 밖에 두며 Option Explicit는 선언보다 앞에 둡니다.
- `comment` — #과 ;는 문자열 따옴표 밖에서 주석을 시작하며 코드 뒤에도 쓸 수 있습니다. REM, //, 작은따옴표는 선택적 들여쓰기 뒤에서 전체 줄 주석을 시작합니다. 문자열 안에서는 이 문자를 그대로 유지할 수 있습니다.

## 반환값

파일을 읽거나 SUB를 선언하는 것 자체는 값을 반환하지 않습니다. RETURN expression은 값을 반환하고 현재 호출을 즉시 끝냅니다. 본문 끝에 도달하거나 식 없이 RETURN을 쓰면 Unit(값 없음)이 됩니다.

## 동작

- 현지화된 주석과 문자열을 보존하려면 UTF-8로 저장하세요. CRLF와 LF 줄바꿈을 모두 받습니다. 들여쓰기와 빈 줄은 읽기 쉽게 하지만 END SUB나 END FUNCTION을 대신하지 않습니다.
- 키워드, 프로시저 이름, 변수 이름은 대소문자를 구분하지 않습니다. itemCount, ITEMCOUNT, ItemCount는 같은 바인딩입니다. 문자열 표기는 보존되며 UO.SetGlobal("Key", …)의 문자열 키는 식별자가 아니라 데이터입니다.
- 단순 이름은 ASCII 영문자 또는 밑줄로 시작하고 뒤에 영문자, 숫자, 밑줄을 씁니다. 직접 선언할 때 예약어와 API 이름을 피하세요. UO.Print는 한정된 호출 이름입니다. 이름 뒤 콜론은 레이블을 정의하며 여러 문장의 일반 구분자가 아닙니다.
- 엔진은 지원하는 Basic 구문을 정규화하고 전체 파일을 분석하여 선언을 수집하고 이름을 검사합니다. 따라서 보조 함수를 Main 아래에 둘 수 있습니다. 파일을 읽을 때 모든 정의가 실행되는 것은 아니며, 선택한 프로시저를 시작할 때 실행을 초기화하고 그 호출을 따릅니다.
- 예제는 값만 계산합니다. 템플릿을 확인한 후 필요한 UO 호출을 본문에 넣습니다. 이는 이 엔진의 규칙이며 다른 Basic의 모든 기능을 지원한다는 뜻은 아닙니다.

## 예제

### 1. 주석과 문자열 내용

```vb
# Main은 note에 "ore #1; keep"을 선언합니다. 문자열의 #과 ;는 그대로 남습니다. 다른 #, REM, //, 작은따옴표 주석은 작업을 하지 않습니다. RETURN은 원래 문자열을 반환합니다.
Option Explicit On
# Complete file
SUB Main()
    REM Full-line comment
    VAR note = "ore #1; keep" # Trailing comment
    // Another full-line comment
    ' Another full-line comment
    RETURN note
END SUB
```

**매개변수 및 실행 설명:**

Main은 note에 "ore #1; keep"을 선언합니다. 문자열의 #과 ;는 그대로 남습니다. 다른 #, REM, //, 작은따옴표 주석은 작업을 하지 않습니다. RETURN은 원래 문자열을 반환합니다.

### 2. 완전히 정의된 보조 함수

```vb
# Main은 amount=7로 DoubleCount를 호출합니다. Main 아래에 정의된 함수는 Integer 매개변수에 2를 곱하여 14를 반환하고 Main이 결과를 전달합니다. 빠진 Include 파일이나 선언되지 않은 함수가 필요하지 않습니다.
Option Explicit On
SUB Main()
    RETURN DoubleCount(7)
END SUB
FUNCTION DoubleCount(ByVal amount AS Integer)
    VAR result = amount * 2
    RETURN result
END FUNCTION
```

**매개변수 및 실행 설명:**

Main은 amount=7로 DoubleCount를 호출합니다. Main 아래에 정의된 함수는 Integer 매개변수에 2를 곱하여 14를 반환하고 Main이 결과를 전달합니다. 빠진 Include 파일이나 선언되지 않은 함수가 필요하지 않습니다.

### 3. 식별자 대소문자

```vb
# itemCount=3을 선언한 뒤 ITEMCOUNT와 itemcount로 같은 변수에 2를 더합니다. 대소문자가 섞인 키워드도 허용됩니다. Main은 5를 반환하며 표기 차이로 변수가 추가 생성되지 않습니다.
Option Explicit On
sUb Main()
    Var itemCount = 3
    ITEMCOUNT = itemcount + 2
    ReTuRn ItemCount
EnD sUb
```

**매개변수 및 실행 설명:**

itemCount=3을 선언한 뒤 ITEMCOUNT와 itemcount로 같은 변수에 2를 더합니다. 대소문자가 섞인 키워드도 허용됩니다. Main은 5를 반환하며 표기 차이로 변수가 추가 생성되지 않습니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: file / subrutine / LineComment / SYMBOL
Runtime/BasicSyntaxPreprocessor.cs: Process
Runtime/InjectionRuntime.cs: Prepare / Load / CallSubrutineValues
Runtime/SemanticScope.cs: Scope
https://learn.microsoft.com/en-us/dotnet/visual-basic/reference/language-specification/introduction (comparison of identifier casing only)
-->
