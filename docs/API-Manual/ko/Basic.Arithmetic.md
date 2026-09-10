# +, -, *, /, MOD

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

산술식은 값을 계산합니다. +는 더하기, -는 빼기 또는 부호 반전, *는 곱하기, /는 나누기, MOD는 정수 나머지입니다. 결과를 변수에 대입하거나 RETURN으로 반환하여 사용합니다.

## 정확한 구문

```text
left + right
left - right
-right
left * right
left / right
left MOD right
(expression)
```

## 매개변수

- `left` — 왼쪽 숫자 피연산자: 리터럴, 선언된 변수, 괄호식 또는 함수 결과입니다. 단항 마이너스에는 왼쪽 피연산자가 없습니다.
- `right` — 오른쪽 숫자 피연산자입니다. /에서는 제수입니다. MOD는 Integer로 변환한 뒤에도 0이 아니어야 합니다. 예를 들어 0.5는 0으로 잘려 오류가 발생합니다.
- `operator / precedence` — 우선순위는 단항 마이너스, 같은 우선순위의 * / MOD를 왼쪽부터, 이항 + -를 왼쪽부터 계산하는 순서입니다. 괄호로 순서를 바꿀 수 있습니다. 단항 플러스, 거듭제곱 ^, 역슬래시 정수 나눗셈은 지원하지 않습니다.

## 반환값

정수의 +, -, *, 단항 마이너스는 Integer입니다. 참여하는 숫자 피연산자가 Decimal이면 Decimal을 반환합니다. /는 항상 Decimal이며 5/2=2.5입니다. MOD는 Integer를 반환합니다. 계산된 숫자이며 성공 여부나 아이템 수라는 의미는 스크립트가 부여합니다.

## 동작

- MOD는 두 피연산자를 부호 있는 32비트 정수로 바꾸고 표현 가능한 소수 부분을 0 방향으로 자릅니다. 나머지 부호는 피제수와 같습니다. -17 MOD 5=-2, -2147483648 MOD -1=0입니다. mOd처럼 대소문자를 섞어도 같습니다.
- MOD의 제수가 0이면 TRY/CATCH로 처리할 수 있는 오류가 납니다. /는 부동소수점 나눗셈으로, 0이 아닌 분자를 0으로 나누면 부호 있는 Infinity, 0/0은 NaN입니다. 유한한 값이 필요하면 제수를 미리 확인하세요.
- 정수 +, -, *, 부호 반전은 오버플로 시 하위 32비트를 유지하며 더 큰 정수형으로 자동 확장하지 않습니다. 근삿값을 허용하는 큰 계산은 먼저 피연산자를 Decimal로 바꿀 수 있습니다. 부동소수점에는 이진 반올림 오차가 있습니다.
- 일반 숫자 연산자는 텍스트를 자동으로 해석하지 않습니다. String+String은 문자열을 연결하고 String+Integer는 실패합니다. 숫자 텍스트는 CDbl 등으로 명시적으로 변환하세요. 중위 MOD는 별도 BasicMod 함수보다 정수 텍스트를 엄격하게 해석합니다.
- 평가기에서 식의 순서대로 피연산자를 계산하고 연산자 토큰을 선택하여 InjectionValue를 만듭니다. 괄호 안의 식은 먼저 끝납니다. 피연산자 자체가 해당 API를 호출하지 않는 한 이동, 대기, 네트워크 요청은 발생하지 않습니다.

## 예제

### 1. 우선순위와 괄호

```vb
# plain=2+3*4는 곱셈을 먼저 계산하여 14가 됩니다. grouped=(2+3)*4는 20입니다. Main은 plain*100+grouped=1420을 반환하여 두 계산을 확인합니다.
Option Explicit On
SUB Main()
    VAR plain = 2 + 3 * 4
    VAR grouped = (2 + 3) * 4
    RETURN plain * 100 + grouped
END SUB
```

**매개변수 및 실행 설명:**

plain=2+3*4는 곱셈을 먼저 계산하여 14가 됩니다. grouped=(2+3)*4는 20입니다. Main은 plain*100+grouped=1420을 반환하여 두 계산을 확인합니다.

### 2. 완성된 묶음과 남은 아이템

```vb
# DescribeBatches는 total=27, size=5를 받습니다. size 검사는 0 이하의 묶음 크기를 거부합니다. Fix(total/size)는 5.4를 완성된 5묶음으로 바꾸고, total mOd size는 남은 2개를 구합니다. CStr로 반환 문자열 "5:2"를 만듭니다. 보조 함수 전체가 포함됩니다.
Option Explicit On
FUNCTION DescribeBatches(total, size)
    IF size <= 0 THEN
        RETURN "invalid"
    END IF
    VAR whole = Fix(total / size)
    VAR remaining = total mOd size
    RETURN CStr(whole) + ":" + CStr(remaining)
END FUNCTION
SUB Main()
    RETURN DescribeBatches(27, 5)
END SUB
```

**매개변수 및 실행 설명:**

DescribeBatches는 total=27, size=5를 받습니다. size 검사는 0 이하의 묶음 크기를 거부합니다. Fix(total/size)는 5.4를 완성된 5묶음으로 바꾸고, total mOd size는 남은 2개를 구합니다. CStr로 반환 문자열 "5:2"를 만듭니다. 보조 함수 전체가 포함됩니다.

### 3. 잘못된 제수 처리

```vb
# 10 MOD 0은 unusedResult에 대입하기 전에 오류를 냅니다. CATCH는 problem에 오류를 저장하고 caught=TRUE로 설정합니다. Main의 반환값 1은 이 예제의 오류 처리 표시이며 실패한 MOD의 결과가 아닙니다.
Option Explicit On
SUB Main()
    VAR caught = FALSE
    TRY
        VAR unusedResult = 10 MOD 0
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**매개변수 및 실행 설명:**

10 MOD 0은 unusedResult에 대입하기 전에 오류를 냅니다. CATCH는 problem에 오류를 저장하고 caught=TRUE로 설정합니다. Main의 반환값 1은 이 예제의 오류 처리 표시이며 실패한 MOD의 결과가 아닙니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: signedOperand / additiveOperand / comparativeOperand
Runtime/Interpreter.cs: VisitSignedOperand / VisitAdditiveOperand / VisitComparativeOperand
Runtime/InjectionValue.cs: arithmetic operators
Runtime/NumberConversions.cs: ToInt
-->
