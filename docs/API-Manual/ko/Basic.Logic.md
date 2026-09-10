# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

NOT은 조건을 반전합니다. AND는 둘 다, OR는 적어도 하나, XOR는 정확히 하나가 참이어야 합니다. &&는 AND, ||는 OR의 별칭이며 키워드 대소문자를 구분하지 않습니다.

## 정확한 구문

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## 매개변수

- `left` — 이항 연산의 왼쪽 조건입니다. AND/OR는 Integer 또는 Decimal이 필요하며 0은 거짓, 0이 아닌 숫자는 참입니다.
- `right` — 오른쪽 조건이며 AND/OR에서는 숫자여야 합니다. 양쪽을 모두 계산하므로 AND 왼쪽이 거짓이거나 OR 왼쪽이 참이어도 생략하지 않습니다.
- `NOT / grouping` — NOT은 반전할 조건 전체를 괄호로 묶으세요. AND, OR, XOR를 섞을 때도 괄호로 묶음을 명확히 하세요.

## 반환값

Integer 1(TRUE) 또는 Integer 0(FALSE)입니다. 비트 연산이 아닌 논리 연산으로, 2 AND 4는 비트 마스크가 아닌 1입니다. 반환 플래그는 =TRUE 또는 =1, =FALSE 또는 =0으로 검사할 수 있습니다.

## 동작

- 이 엔진에서 AND, OR, XOR는 같은 우선순위로 왼쪽부터 계산합니다. TRUE OR FALSE AND FALSE는 0, TRUE OR (FALSE AND FALSE)는 1입니다. VB 코드를 옮길 때 이 호환 규칙을 고려하세요.
- NOT(condition)은 조건을 계산하고 참과 거짓을 반전합니다. 비교 앞의 NOT 1=2는 NOT(1=2)입니다. 반전한 값 자체가 비교 피연산자라면 (NOT value)로 쓰세요.
- AND/OR는 String, Array, Object, Unit을 거부합니다. 기존 NOT과 XOR는 숫자 0과 같은지 검사하므로 텍스트 "0", 빈 문자열, 배열, 객체, Unit을 0이 아닌 것으로 간주합니다. 이 값에는 명시적인 숫자 조건을 정의하세요. CBool은 별도 변환 규칙을 사용합니다.
- 오른쪽 식은 함수 호출, 대기 및 오류까지 항상 실행됩니다. 괄호는 묶음만 바꾸며 계산을 생략하지 않습니다. 앞 조건이 성공한 경우에만 다음 식을 실행하려면 중첩 IF를 사용하세요.

## 예제

### 1. 이름 붙인 플래그 결합

```vb
# ready=TRUE, blocked=FALSE입니다. NOT(blocked)는 1이므로 canRun은 1입니다. ready XOR blocked는 정확히 하나만 참이므로 참입니다. Main은 canRun*10+exclusive=11을 반환합니다.
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**매개변수 및 실행 설명:**

ready=TRUE, blocked=FALSE입니다. NOT(blocked)는 1이므로 canRun은 1입니다. ready XOR blocked는 정확히 하나만 참이므로 참입니다. Main은 canRun*10+exclusive=11을 반환합니다.

### 2. 두 호출 관찰

```vb
# Mark는 ByRef로 받은 counter를 증가시키고 TRUE를 반환합니다. Main은 counter=0으로 시작합니다. FALSE AND Mark(counter)도 Mark를 호출하고 TRUE OR Mark(counter)도 다시 호출합니다. 조건 결과는 0과 1이지만 Main은 counter=2를 반환합니다. Mark 전체 코드가 포함됩니다.
Option Explicit On
FUNCTION Mark(ByRef counter)
    counter = counter + 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR counter = 0
    VAR first = FALSE AND Mark(counter)
    VAR second = TRUE OR Mark(counter)
    RETURN counter
END SUB
```

**매개변수 및 실행 설명:**

Mark는 ByRef로 받은 counter를 증가시키고 TRUE를 반환합니다. Main은 counter=0으로 시작합니다. FALSE AND Mark(counter)도 Mark를 호출하고 TRUE OR Mark(counter)도 다시 호출합니다. 조건 결과는 0과 1이지만 Main은 counter=2를 반환합니다. Mark 전체 코드가 포함됩니다.

### 3. 명시적인 묶음

```vb
# legacy는 TRUE OR FALSE 다음 AND FALSE를 계산하여 0입니다. grouped는 괄호 안 FALSE AND FALSE 다음 TRUE와 OR를 계산하여 1입니다. Main은 legacy*10+grouped=1을 반환합니다.
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**매개변수 및 실행 설명:**

legacy는 TRUE OR FALSE 다음 AND FALSE를 계산하여 0입니다. grouped는 괄호 안 FALSE AND FALSE 다음 TRUE와 OR를 계산하여 1입니다. Main은 legacy*10+grouped=1을 반환합니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
