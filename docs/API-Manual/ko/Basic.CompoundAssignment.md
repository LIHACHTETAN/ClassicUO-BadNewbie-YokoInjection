# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

+=, -=, *=, /=로 기존 변수나 배열 요소를 갱신합니다. 현재 값을 읽고 계산하여 다시 쓰며 대상을 두 번 평가하지 않습니다.

## 정확한 구문

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## 매개변수

- `target` — target: 기존 스칼라 이름 또는 items[index], grid[x][y] 같은 요소입니다. 요소는 초기화되어야 하며 0부터 시작하는 인덱스가 유효해야 합니다. 변수를 선언하지 않습니다.
- `operator` — +=와 &=는 숫자를 더하거나 두 String을 연결하며 -=는 빼기, *=는 곱하기, /=는 나누기입니다. 전처리기가 &=를 +=로 바꾸므로 5 &= 3은 8을 저장합니다. String과 숫자에는 명시적인 CStr이 필요합니다. 연산자를 하나의 토큰으로 쓰세요.
- `value` — value: 대상과 인덱스 뒤에 한 번 계산할 식입니다. 종류가 연산에 맞아야 합니다. 숫자를 String에 추가하기 전에 CStr로 변환하세요.

## 반환값

값 없음(Unit)입니다. 문이며 식이나 성공 플래그가 아닙니다. 다음 줄에서 target을 읽어 저장 결과를 얻으세요. 스칼라 쓰기에는 AS가 적용되어 Integer 5를 /=2 하면 Integer 2, 형식 미지정 숫자 변수는 Decimal 2.5가 됩니다.

## 동작

- 각 배열 참조를 인덱스 계산 전에 보관합니다. 인덱스는 왼쪽부터 한 번씩 실행하고 범위는 오른쪽 피연산자 전에 확인합니다. 인덱스나 오른쪽 ByRef 함수가 배열 변수나 부모 요소를 교체해도 이미 선택한 칸에 씁니다.
- +, -, *, /와 같은 규칙입니다. 정수는 부호 있는 32비트로 오버플로하고 /는 Decimal이며 부동소수점 0 나눗셈은 Infinity/NaN일 수 있습니다. String과 숫자 덧셈은 실패합니다. 배열 요소에는 스칼라 AS 변환이 없습니다.
- 미선언 대상, 미초기화 요소, 잘못된 인덱스, 호환되지 않는 연산, CONST 쓰기, 변환 실패는 잡을 수 있는 오류입니다. 최종 쓰기는 하지 않지만 피연산자 함수가 이미 일으킨 부수 효과는 되돌리지 않습니다. CONST와 AS는 오른쪽이 실행된 후 스칼라를 쓸 때 검사합니다.
- Option Explicit은 실행 전에 이름을 확인합니다. 디버거는 원본 줄 번호를 쓰고 바쁜 루프도 일시 정지와 정지 검사를 유지합니다. 읽기, 계산, 쓰기는 동시 프로시저 사이의 원자적 동기화 연산이 아닙니다.

## 예제

### 1. 네 가지 연산

```vb
# amount는 10에서 시작합니다. +=2는 12, -=3은 9, *=4는 36, /=2는 Decimal 18입니다. Main은 저장값을 반환하며 대입문 자체는 값을 반환하지 않습니다.
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**매개변수 및 실행 설명:**

amount는 10에서 시작합니다. +=2는 12, -=3은 9, *=4는 36, /=2는 Decimal 18입니다. Main은 저장값을 반환하며 대입문 자체는 값을 반환하지 않습니다.

### 2. 인덱스를 한 번 계산

```vb
# NextIndex는 ByRef 매개변수 calls를 증가시키고 0을 반환합니다. items[0]은 5에서 +=2로 7이 됩니다. 호출은 한 번이므로 calls=1입니다. Main은 items[0]*10+calls=71을 반환합니다. 보조 함수 전체가 포함됩니다.
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**매개변수 및 실행 설명:**

NextIndex는 ByRef 매개변수 calls를 증가시키고 0을 반환합니다. items[0]은 5에서 +=2로 7이 됩니다. 호출은 한 번이므로 calls=1입니다. Main은 items[0]*10+calls=71을 반환합니다. 보조 함수 전체가 포함됩니다.

### 3. 상수 보호 처리

```vb
# limit는 CONST 5입니다. limit+=1은 쓸 때 오류가 나고 CATCH는 problem에 저장하며 caught=TRUE로 만듭니다. limit는 5를 유지합니다. Main은 명시적 CStr로 "5:1"을 반환합니다. 플래그는 오류 처리 결과이지 대입 반환값이 아닙니다. 변수에서 문자열을 만듭니다. report=CStr(limit) 다음 report &= ":"와 report &= CStr(caught)를 실행합니다. 각 &=는 report를 갱신하고 Return report는 "5:1"을 반환합니다.
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**매개변수 및 실행 설명:**

limit는 CONST 5입니다. limit+=1은 쓸 때 오류가 나고 CATCH는 problem에 저장하며 caught=TRUE로 만듭니다. limit는 5를 유지합니다. Main은 명시적 CStr로 "5:1"을 반환합니다. 플래그는 오류 처리 결과이지 대입 반환값이 아닙니다. 변수에서 문자열을 만듭니다. report=CStr(limit) 다음 report &= ":"와 report &= CStr(caught)를 실행합니다. 각 &=는 report를 갱신하고 Return report는 "5:1"을 반환합니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
