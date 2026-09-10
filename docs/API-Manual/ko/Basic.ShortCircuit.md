# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

AndAlso와 OrElse는 불필요한 오른쪽 피연산자를 건너뛰며 조건을 결합합니다. AndAlso는 왼쪽이 거짓이면, OrElse는 왼쪽이 참이면 오른쪽을 생략합니다. 배열 접근을 보호하거나 불필요한 호출을 피할 때 사용하세요.

## 정확한 구문

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## 매개변수

- `left` — left: 먼저 한 번 계산하는 식. Integer 또는 Decimal의 0은 거짓이며 0이 아닌 수는 참입니다.
- `right` — right: 필요한 경우에만 한 번 계산하는 식. 생략한 배열 읽기, 함수 호출과 부작용은 발생하지 않습니다. 계산하는 피연산자는 숫자여야 하며 문자열은 CBool로 명시적으로 변환하세요.

## 반환값

원래 피연산자가 아닌 Integer 1(TRUE) 또는 0(FALSE)을 반환합니다. result=1과 result=TRUE, result=0과 result=FALSE를 동일하게 쓸 수 있습니다. 이 엔진의 참은 1이며 VB.NET 숫자 변환의 -1이 아닙니다. 일반 개수는 여전히 개수이며 이 연산이 논리 값을 만듭니다.

## 동작

- 비교는 피연산자 안에서 계산됩니다. AndAlso가 OrElse보다 우선하며 같은 연산자는 왼쪽부터 결합합니다. 괄호로 순서를 바꿀 수 있습니다. 생략한 식도 구문 분석과 Option Explicit 검사를 받습니다.
- 호환성을 위해 연속된 AND/OR/XOR는 피연산자 안에서 기존처럼 왼쪽부터 양쪽을 계산한 뒤 AndAlso/OrElse를 처리합니다. TRUE OR FALSE AndAlso FALSE는 FALSE, TRUE OrElse FALSE AND FALSE는 TRUE입니다. 혼합할 때는 괄호를 사용하세요. AND, OR, &&, ||는 양쪽을 계산합니다.
- 엔진은 왼쪽 값을 계산하고 숫자의 참/거짓을 확인한 뒤 논리 값을 반환하거나 필요한 오른쪽을 계산합니다. 필요한 피연산자의 오류는 CATCH로 전달되며 FINALLY와 일시 정지/정지 검사는 유지됩니다. 호출을 생략하면 해당 호출의 모든 동작도 생략됩니다.

## 예제

### 1. 첫 요소를 안전하게 확인

```vb
# FirstEquals는 items와 expected를 받습니다. GetArrayLength(items)>0을 먼저 확인하므로 빈 배열의 items[0]은 읽지 않습니다. Main은 [42]와 빈 배열을 전달해 1과 0을 얻고 10을 반환합니다. 전체 보조 함수가 제공되며 배열은 바꾸지 않습니다.
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**매개변수 및 실행 설명:**

FirstEquals는 items와 expected를 받습니다. GetArrayLength(items)>0을 먼저 확인하므로 빈 배열의 items[0]은 읽지 않습니다. Main은 [42]와 빈 배열을 전달해 1과 0을 얻고 10을 반환합니다. 전체 보조 함수가 제공되며 배열은 바꾸지 않습니다.

### 2. 대체 호출을 한 번 실행

```vb
# Probe는 ByRef로 calls를 증가시키고 TRUE를 반환합니다. TRUE OrElse Probe(calls)는 호출을 생략하고 FALSE OrElse Probe(calls)는 한 번 호출합니다. 두 조건 모두 1이며 Main은 실제 호출 횟수 1을 반환합니다.
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**매개변수 및 실행 설명:**

Probe는 ByRef로 calls를 증가시키고 TRUE를 반환합니다. TRUE OrElse Probe(calls)는 호출을 생략하고 FALSE OrElse Probe(calls)는 한 번 호출합니다. 두 조건 모두 1이며 Main은 실제 호출 횟수 1을 반환합니다.

### 3. 나눗셈 보호와 우선순위

```vb
# AverageExceeds(total, count, limit)는 count>0일 때만 나눕니다. (25,0,10)은 0, (25,2,10)은 12.5>10이므로 1입니다. TRUE OrElse FALSE AndAlso FALSE는 오른쪽 AndAlso를 생략하고 1입니다. Main은 "0:1:1"을 반환합니다.
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**매개변수 및 실행 설명:**

AverageExceeds(total, count, limit)는 count>0일 때만 나눕니다. (25,0,10)은 0, (25,2,10)은 12.5>10이므로 1입니다. TRUE OrElse FALSE AndAlso FALSE는 오른쪽 AndAlso를 생략하고 1입니다. Main은 "0:1:1"을 반환합니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
