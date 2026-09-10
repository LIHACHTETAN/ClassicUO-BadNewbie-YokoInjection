# CONST

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

CONST는 일반적인 재대입을 허용하지 않는 이름 바인딩을 선언합니다. 초기값으로 리터럴이나 표현식 결과를 사용할 수 있으며 선언이 실행될 때 계산합니다.

## 정확한 구문

```text
CONST name [AS type] = expression [, name ...]
```

## 매개변수

- `name` — 따옴표 없는 상수 이름. 범위 내에서 구분되는 이름을 사용하세요. 프로시저 밖의 선언은 전역이며 안의 선언은 해당 호출의 지역 상수입니다.
- `type` — 선택적인 지원 AS 형식으로 VAR와 같은 변환을 사용합니다. 예를 들어 AS Integer는 엔진의 부호 있는 32비트 정수로 변환합니다. 대괄호는 선택 사항을 뜻하므로 AS 주위에 입력하지 마세요.
- `expression` — 필수 초기식. 숫자, 따옴표 문자열, TRUE/FALSE, 산술식, 지원 함수 결과를 사용할 수 있습니다. 이 선언이 실행될 때 한 번 계산하며 파일 전체에서 영구적으로 한 번만 계산하는 것은 아닙니다.

## 반환값

값이 없습니다. CONST는 선언이며 함수나 논리 질의가 아닙니다. 이름을 읽으면 저장된 초기값을 얻습니다. 예제의 RETURN은 Main 또는 ApplyLimit에 속합니다.

## 동작

- 일반 대입, LET, SET는 이 바인딩을 바꾸지 못하며 상수 변경 오류를 발생시킵니다. TRY/CATCH로 해당 실행 오류를 처리할 수 있습니다. Option Explicit는 선언을 요구하지만 모든 잘못된 대입을 실행 전에 검출하지는 않습니다.
- 전역 상수는 새 최상위 실행에서 초기화되고 호출된 프로시저에 상수 표시와 AS 형식을 상속합니다. 지역 상수는 선언 실행 시 초기화됩니다. 따라서 초기식의 함수가 다음 시작 때 다시 작업할 수 있습니다.
- 보호되는 것은 바인딩이며 Array/Object 내부 내용은 동결되지 않습니다. 별도 지역 선언은 전역 이름을 가릴 수 있고 다른 선언은 새 바인딩을 만듭니다. 상수 이름을 재사용하지 마세요.
- 엔진은 초기식을 계산하고 AS를 적용한 뒤 범위에 상수 표시를 기록합니다. 이후 일반 대입은 값을 바꾸기 전에 이 표시를 확인합니다. 스칼라 리터럴 예제는 게임 동작을 실행하지 않습니다.

## 예제

### 1. 고정 지연값으로 계산

```vb
# delay는 값이 350인 지역 Integer 상수입니다. 2를 곱해 별도 변수 doubled=700을 만듭니다. Main은 700을 반환하며 예제 자체는 대기하지 않습니다.
Option Explicit On
SUB Main()
    CONST delay AS Integer = 350
    VAR doubled = delay * 2
    RETURN doubled
END SUB
```

**매개변수 및 실행 설명:**

delay는 값이 350인 지역 Integer 상수입니다. 2를 곱해 별도 변수 doubled=700을 만듭니다. Main은 700을 반환하며 예제 자체는 대기하지 않습니다.

### 2. 전역 한도 전달

```vb
# limit은 값이 50인 전역 Integer 상수입니다. ApplyLimit는 amount=72와 maximum=50을 받아 작은 수량 50을 반환합니다. 보조 함수가 완전히 정의되어 있으며 매개변수를 읽기만 합니다.
Option Explicit On
CONST limit AS Integer = 50
FUNCTION ApplyLimit(amount, maximum)
    IF amount > maximum THEN
        RETURN maximum
    END IF
    RETURN amount
END FUNCTION
SUB Main()
    RETURN ApplyLimit(72, limit)
END SUB
```

**매개변수 및 실행 설명:**

limit은 값이 50인 전역 Integer 상수입니다. ApplyLimit는 amount=72와 maximum=50을 받아 작은 수량 50을 반환합니다. 보조 함수가 완전히 정의되어 있으며 매개변수를 읽기만 합니다.

### 3. 금지된 재대입 처리

```vb
# limit의 초기값은 3입니다. 4를 대입하면 오류가 나고 상수는 바뀌지 않습니다. CATCH는 오류를 problem에 저장하고 caught=TRUE로 설정합니다. Main은 논리값 1을 반환하며 여기서 TRUE와 1은 같습니다.
Option Explicit On
SUB Main()
    CONST limit = 3
    VAR caught = FALSE
    TRY
        limit = 4
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**매개변수 및 실행 설명:**

limit의 초기값은 3입니다. 4를 대입하면 오류가 나고 상수는 바뀌지 않습니다. CATCH는 오류를 problem에 저장하고 caught=TRUE로 설정합니다. Main은 논리값 1을 반환하며 여기서 TRUE와 1은 같습니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: constDeclaration / globalConst
Runtime/DefinitionCollector.cs: VisitGlobalConst
Runtime/Interpreter.cs: VisitConstDef
Runtime/SemanticScope.cs: DefineVar / SetVar
-->
