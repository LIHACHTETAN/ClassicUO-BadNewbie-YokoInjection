# VAR / DIM

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

VAR와 스칼라 DIM은 이름 있는 값을 선언합니다. 대입은 표현식을 계산하여 결과를 저장합니다. 프로시저 내부 선언은 해당 호출의 지역 변수이며 외부 선언은 스크립트 전역 변수입니다.

## 정확한 구문

```text
VAR name [AS type] [= expression] [, name ...]
DIM name [AS type] [= expression] [, name ...]
name = expression
LET name = expression
SET name = expression
```

## 매개변수

- `name` — 따옴표 없는 변수 이름. 영문자, 숫자, 밑줄을 사용하고 영문자나 밑줄로 시작하세요. 같은 철자를 유지하고 언어 키워드는 피하세요.
- `type` — 선택적인 AS 형식. Integer/Long/Short/Byte는 엔진의 부호 있는 32비트 정수 변환, Double/Single/Decimal은 배정밀도 숫자, String은 텍스트, Boolean/Bool은 논리값을 사용합니다. Variant/Object는 값의 종류를 유지합니다. VB.NET의 개별 byte/short/long 범위를 적용하는 별칭은 아닙니다.
- `expression` — VAR/DIM의 초기식은 선택 사항이고 대입의 오른쪽 표현식은 필수입니다. 해당 줄이 실행될 때 계산합니다. AS String에 초기식이 없으면 빈 문자열이며 형식 있는 숫자와 Boolean의 기본값은 0입니다. 초기식 없는 무형식 VAR와 VAR AS Variant/Object는 Unit(값 없음)이며 스칼라 DIM은 0을 제공합니다. 형식 없는 변수는 나중에 다른 종류의 값을 저장할 수 있습니다.

## 반환값

값이 없습니다. VAR, DIM, 대입문은 결과를 반환하지 않습니다. 이름을 읽으면 저장된 값을 얻습니다. 예제의 RETURN은 Main에서 값을 반환하며 DIM의 반환값이 아닙니다.

## 동작

- 위 구문의 대괄호는 선택 사항을 나타냅니다. AS나 초기식 주위에 대괄호를 입력하지 마세요. 배열 DIM은 다른 선언 형식을 사용합니다.
- 이 엔진에서 LET와 SET는 일반 대입의 호환 형식입니다. Option Explicit On에서는 이름을 선언하지 않습니다. AS 형식은 나중의 대입에도 적용되며 잘못된 변환이나 지원하지 않는 형식은 실행 오류를 일으킵니다.
- 지역 이름은 프로시저 호출에 속합니다. IF 안에서 선언해도 별도의 블록 범위를 만들지 않습니다. 실행하지 않은 분기는 실행 중 값을 만들지 않습니다. 분기 뒤에서 값이 필요하면 분기 전에 선언하세요.
- Injection 호환 규칙: 호출된 프로시저는 호출자의 현재 전역 스칼라 값과 AS 형식을 상속합니다. 호출된 프로시저에서 스칼라를 다시 대입해도 호출자는 갱신되지 않습니다. 갱신하려면 새 값을 반환하거나 BYREF 인수를 사용하세요. Array/Object 값을 깊게 복제하는 것은 아닙니다. 새 최상위 호출은 전역 변수를 다시 초기화하며 지역 선언은 전역 선언을 바꾸지 않고 자기 프레임의 이름을 가립니다.
- 엔진은 초기식을 계산하고 현재 범위에 저장 공간을 정의한 뒤 형식을 변환합니다. 이후 대입도 오른쪽부터 계산합니다. 예제는 로컬 계산이며 변수를 프로필이나 JSON 파일에 자동 저장하지 않습니다.

## 예제

### 1. 정수 갱신

```vb
# count는 0에서 시작해 5를 받고 LET로 2를 더합니다. Main은 Integer 7을 반환합니다. 첫 DIM은 이름을 선언하고 이후 대입은 값을 갱신합니다.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    LET count = count + 2
    RETURN count
END SUB
```

**매개변수 및 실행 설명:**

count는 0에서 시작해 5를 받고 LET로 2를 더합니다. Main은 Integer 7을 반환합니다. 첫 DIM은 이름을 선언하고 이후 대입은 값을 갱신합니다.

### 2. 텍스트와 논리 플래그

```vb
# label은 빈 String으로 시작합니다. SET가 "ore"를 저장합니다. enabled는 Boolean TRUE이므로 IF 분기는 String "ore"를 반환합니다. 따옴표 없는 TRUE는 논리값 1입니다.
Option Explicit On
SUB Main()
    DIM label AS String
    VAR enabled AS Boolean = TRUE
    SET label = "ore"
    IF enabled = TRUE THEN
        RETURN label
    END IF
    RETURN "disabled"
END SUB
```

**매개변수 및 실행 설명:**

label은 빈 String으로 시작합니다. SET가 "ore"를 저장합니다. enabled는 Boolean TRUE이므로 IF 분기는 String "ore"를 반환합니다. 따옴표 없는 TRUE는 논리값 1입니다.

### 3. 전역 입력과 지역 계산

```vb
# baseAmount는 값이 4인 전역 변수입니다. extra는 Calculate의 지역 변수이며 값은 3입니다. Calculate가 반환한 7을 Main의 자체 지역 result에 저장하고 7을 반환합니다. extra는 Main의 지역 변수가 아닙니다.
Option Explicit On
VAR baseAmount AS Integer = 4
FUNCTION Calculate()
    VAR extra = 3
    RETURN baseAmount + extra
END FUNCTION
SUB Main()
    VAR result = Calculate()
    RETURN result
END SUB
```

**매개변수 및 실행 설명:**

baseAmount는 값이 4인 전역 변수입니다. extra는 Calculate의 지역 변수이며 값은 3입니다. Calculate가 반환한 7을 Main의 자체 지역 result에 저장하고 7을 반환합니다. extra는 Main의 지역 변수가 아닙니다.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim
Runtime/Interpreter.cs: VisitVarDef / VisitAssignment
Runtime/SemanticScope.cs: DefineVar / SetVar / Coerce
-->
