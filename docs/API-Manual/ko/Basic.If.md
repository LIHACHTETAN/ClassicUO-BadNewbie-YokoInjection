# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

IF는 최대 하나의 분기를 선택합니다. IF와 이어지는 ELSEIF를 순서대로 확인해 처음 참인 조건을 선택합니다. 모두 거짓이면 선택적인 ELSE를 실행하고 보통 END IF 다음으로 진행합니다.

## 정확한 구문

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## 매개변수

- `condition` — condition: 진입 시 한 번 확인하는 식. 숫자 0은 거짓, 0이 아닌 수는 참입니다. 명시적인 비교나 API 논리 결과를 권장합니다.
- `elseifCondition` — elseifCondition: 앞선 조건이 모두 거짓일 때만 확인하는 추가 조건. ELSEIF는 한 단어로 씁니다.
- `statements / ELSE` — statements / ELSE: 다음 줄들의 명령. ELSE는 선택 사항이며 조건 없이 마지막에 한 번만 올 수 있습니다. THEN과 END IF는 필수이며 여러 줄 블록을 사용합니다.

## 반환값

값을 반환하지 않습니다(Unit). IF는 제어문이며 함수가 아닙니다. 조건이나 선택된 RETURN은 값을 만들 수 있습니다. 논리 값 1/0은 TRUE/FALSE와 비교할 수 있습니다. IF count는 0이 아닌 모든 개수를 받아들이지만 IF count=TRUE는 1만 일치합니다.

## 동작

- 컴파일러는 조건 및 종료 점프를 만듭니다. 거짓이면 다음 조건이나 ELSE로 이동하고 선택한 분기는 나머지를 건너뜁니다. 중첩 IF에는 자체 ELSE가 있습니다. RETURN은 바깥 FINALLY를 수행하며 프로시저를 종료합니다.
- 기존 호환성을 위해 IF는 모든 종류를 CBool로 변환하지 않고 숫자 0과 비교합니다. 문자열 "0", 빈 문자열, 배열, 객체, Unit은 참 분기를 선택합니다. 문자열을 명시적으로 변환하거나 원하는 속성을 비교하세요. AndAlso/OrElse는 숫자를 요구합니다.
- 건너뛴 분기의 선언은 실행 중 변수를 만들지 않습니다. 공유할 결과는 IF 전에 선언하고 초기화하세요. Option Explicit는 이름을 검사하며 모든 경로의 대입을 보장하지 않습니다. 여러 ELSE는 Option Explicit 없이도 실행 전 SC015로 거부됩니다.

## 예제

### 1. 네 가지 분류

```vb
# Classify(value)는 <0, =0, <10, 마지막 ELSE를 확인합니다. -2, 0, 7, 20은 negative, zero, small, large를 반환합니다. Main은 "negative:zero:small:large"를 반환하고 각 호출은 RETURN 하나만 실행합니다.
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**매개변수 및 실행 설명:**

Classify(value)는 <0, =0, <10, 마지막 ELSE를 확인합니다. -2, 0, 7, 20은 negative, zero, small, large를 반환합니다. Main은 "negative:zero:small:large"를 반환하고 각 호출은 RETURN 하나만 실행합니다.

### 2. 중첩된 판단

```vb
# Action(enabled, amount)는 enabled를 확인한 뒤 amount>0에 따라 work 또는 idle을 선택합니다. 바깥 ELSE는 disabled입니다. (TRUE,5), (TRUE,0), (FALSE,5)는 "work:idle:disabled"를 만듭니다. END IF마다 해당 블록을 닫습니다.
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**매개변수 및 실행 설명:**

Action(enabled, amount)는 enabled를 확인한 뒤 amount>0에 따라 work 또는 idle을 선택합니다. 바깥 ELSE는 disabled입니다. (TRUE,5), (TRUE,0), (FALSE,5)는 "work:idle:disabled"를 만듭니다. END IF마다 해당 블록을 닫습니다.

### 3. 조건 확인 순서

```vb
# Check(calls,value)는 ByRef의 calls를 증가시키고 value를 반환합니다. 첫 조건은 거짓, 둘째는 참이므로 셋째와 ELSE는 생략합니다. result=7, calls=2이며 Main은 calls*10+result=27을 반환합니다. 모든 보조 함수가 포함됩니다.
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**매개변수 및 실행 설명:**

Check(calls,value)는 ByRef의 calls를 증가시키고 value를 반환합니다. 첫 조건은 거짓, 둘째는 참이므로 셋째와 ELSE는 생략합니다. result=7, calls=2이며 Main은 calls*10+result=27을 반환합니다. 모든 보조 함수가 포함됩니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
