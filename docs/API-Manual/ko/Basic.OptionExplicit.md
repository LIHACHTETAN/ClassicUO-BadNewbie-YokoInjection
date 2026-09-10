# Option Explicit

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

스크립트 실행 전에 변수 선언을 요구합니다. 이 엔진 Basic 언어의 파일 지시문이며 UO 명령이나 함수 호출이 아닙니다.

## 정확한 구문

```text
Option Explicit
Option Explicit On
Option Explicit Off
```

## 매개변수

- `On / Off` — On은 엄격한 선언 검사를 켜고 Off는 끕니다. Explicit 뒤에 옵션이 없으면 On입니다. 파일에 지시문 자체가 없으면 기존의 비엄격 모드를 유지합니다. 괄호나 따옴표를 붙이지 마세요.

## 반환값

값이 없습니다. 지시문은 표현식이 아니며 TRUE/FALSE, 숫자, ID를 반환하지 않습니다. 예제의 RETURN은 Main 또는 Enough에 속하며 Option Explicit의 반환이 아닙니다.

## 동작

- 변수, 상수, 프로시저 앞에 한 번만 작성하세요. 앞에는 빈 줄과 주석을 둘 수 있습니다. 중복되거나 뒤늦은 지시문은 SC013 오류이며, 나중에 Off로 전환하는 경우도 같습니다.
- On에서는 선언되지 않은 변수 읽기나 대입에 소스 위치가 포함된 SC006이 발생합니다. 배열 이름, FOR 카운터, 메서드 호출을 받는 객체도 검사합니다. VAR/DIM/CONST, 매개변수, 이름 있는 CATCH 변수로 이름을 선언합니다. FOR VAR는 카운터를 선언합니다.
- 지역 변수는 사용 전에 선언하세요. 한 프로시저의 지역 변수가 다른 프로시저의 이름을 선언하지는 않습니다. 전역 선언은 프로시저에서 사용할 수 있습니다. 이름 검사이며 모든 분기에서 초기화됨을 증명하는 기능은 아닙니다.
- 파서가 파일 전체를 읽고 분석기가 선언을 확인하며 엄격한 검사 오류가 있으면 첫 명령 전에 실행을 거부합니다. 다시 로드하면 이전 스크립트와 독립적으로 새 파일의 옵션을 적용합니다. Off에서도 경고가 나올 수 있고 아직 없는 값을 읽으면 실행 중 실패할 수 있습니다.
- 지시문 자체는 게임 동작이나 패킷 전송을 하지 않습니다. 완전한 VB.NET 호환성이나 게임 대상의 존재를 보장하지 않습니다.

## 예제

### 1. 대입 전에 선언

```vb
# On으로 검사를 켭니다. DIM이 count를 Integer로 선언하므로 5를 대입할 수 있습니다. Main은 5를 반환합니다. count를 선언되지 않은 coutn으로 바꾸면 SC006으로 실행이 차단됩니다.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    RETURN count
END SUB
```

**매개변수 및 실행 설명:**

On으로 검사를 켭니다. DIM이 count를 Integer로 선언하므로 5를 대입할 수 있습니다. Main은 5를 반환합니다. count를 선언되지 않은 coutn으로 바꾸면 SC006으로 실행이 차단됩니다.

### 2. 매개변수와 전역 상수

```vb
# 옵션 생략은 On입니다. minimum은 값이 3인 전역 상수입니다. amount는 Enough의 선언된 매개변수이며 Main의 같은 이름 지역 변수와는 별개입니다. Enough는 5 >= 3을 비교하여 TRUE, 즉 숫자 1을 반환합니다.
Option Explicit
CONST minimum = 3
FUNCTION Enough(amount)
    RETURN amount >= minimum
END FUNCTION
SUB Main()
    VAR amount = 5
    RETURN Enough(amount)
END SUB
```

**매개변수 및 실행 설명:**

옵션 생략은 On입니다. minimum은 값이 3인 전역 상수입니다. amount는 Enough의 선언된 매개변수이며 Main의 같은 이름 지역 변수와는 별개입니다. Enough는 5 >= 3을 비교하여 TRUE, 즉 숫자 1을 반환합니다.

### 3. 이전 스크립트 실행

```vb
# Off에서는 DIM 없이 대입으로 legacyCounter를 만들 수 있습니다. Main은 7을 반환합니다. 이 호환성 예제에는 경고가 남을 수 있습니다. 엄격한 검사를 하려면 변수를 선언하고 On을 사용하세요.
Option Explicit Off
SUB Main()
    legacyCounter = 7
    RETURN legacyCounter
END SUB
```

**매개변수 및 실행 설명:**

Off에서는 DIM 없이 대입으로 legacyCounter를 만들 수 있습니다. Main은 7을 반환합니다. 이 호환성 예제에는 경고가 남을 수 있습니다. 엄격한 검사를 하려면 변수를 선언하고 On을 사용하세요.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: optionExplicit
Analysis/SanityAnalyzer.cs
Analysis/InvalidSymbolVisitor.cs
Runtime/InjectionRuntime.cs
-->
