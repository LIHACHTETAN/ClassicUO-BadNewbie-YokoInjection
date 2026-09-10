# 123 / 0x0EED / "text" / TRUE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

리터럴은 코드에 값을 직접 적습니다. 숫자와 따옴표 문자열은 선언이 필요 없습니다. TRUE/FALSE는 미리 정의된 논리 값입니다. 따옴표 안의 숫자는 명시적 변환이나 선언 형식 변환 전까지 문자열입니다.

## 정확한 구문

```text
123
-2147483648
0x0EED
0xFFFFFFFF
2.5
"text"
'text'
TRUE
FALSE
```

## 매개변수

- `integer / hexadecimal` — 십진 Integer 범위는 -2147483648…2147483647이며 16진수는 소문자 0x와 0–9/A–F로 씁니다. 32비트를 나타내므로 0xFFFFFFFF는 Integer -1이지 양의 64비트 숫자가 아닙니다.
- `floating` — 소수점 앞뒤에 숫자가 있는 부동소수점 값으로 2.5, -0.25 등이 있습니다. .5 대신 0.5로 씁니다. 이 문법은 쉼표, 1e3 지수 표기, 숫자 리터럴 접미사를 지원하지 않습니다.
- `text` — 서로 맞는 작은따옴표 또는 큰따옴표로 문자열을 감쌉니다. 내용에 따옴표를 넣으려면 다른 종류나 Chr(34)/Chr(39)를 사용합니다. 역슬래시 이스케이프와 따옴표 두 번 쓰기는 해석하지 않습니다. 예제 문자열을 한 물리적 줄에 두세요.
- `TRUE / FALSE` — TRUE는 Integer 1, FALSE는 Integer 0입니다. 이 이름을 다시 선언하지 마세요. 호출이 아닌 값이므로 TRUE() 대신 TRUE로 씁니다.

## 반환값

정수/16진 리터럴은 Integer, 소수점 숫자는 Decimal(이진 부동소수점), 따옴표 문자열은 String입니다. TRUE/FALSE는 Integer 1/0입니다. 값 계산은 게임 동작이나 변수 선언을 수행하지 않습니다.

## 동작

- -5의 부호는 단항 연산입니다. -2147483648은 양의 절댓값을 먼저 저장하지 않고 최소 부호 있는 정수로 처리합니다. 범위 밖 정수는 오류입니다. 더 큰 근삿값이 필요한 계산에는 적절한 부동소수점을 쓰세요.
- 문자열은 문자와 대소문자를 유지합니다. "350"은 숫자 350이 아니고 "false"는 FALSE가 아닙니다. #과 ;는 따옴표 안에서 문자, 밖에서 주석입니다. 변환 규칙은 AS 및 각 함수 설명을 참조하세요.
- 엔진은 토큰을 인식하고 문화권에 의존하지 않고 숫자를 해석하거나 문자열의 바깥 따옴표를 제거합니다. IDE 언어를 바꿔도 코드의 소수 구분자는 바뀌지 않습니다.
- serial, 그래픽 type, 좌표는 모두 숫자로 표현될 수 있습니다. 리터럴 자체가 의미를 정하지 않으며 호출한 API의 매개변수 계약이 용도를 결정합니다.

## 예제

### 1. 16진 type과 정수 경계

```vb
# itemType=0x0EED는 십진 3821입니다. lowest=-2147483648은 부호 있는 비트 형태 0x80000000과 같으므로 Main은 itemType=3821을 반환합니다. 아이템을 검색하지는 않습니다.
Option Explicit On
SUB Main()
    VAR itemType = 0x0EED
    VAR lowest = -2147483648
    IF lowest = 0x80000000 THEN
        RETURN itemType
    END IF
    RETURN 0
END SUB
```

**매개변수 및 실행 설명:**

itemType=0x0EED는 십진 3821입니다. lowest=-2147483648은 부호 있는 비트 형태 0x80000000과 같으므로 Main은 itemType=3821을 반환합니다. 아이템을 검색하지는 않습니다.

### 2. 두 가지 따옴표

```vb
# owner="O'Brien"에는 작은따옴표가 있습니다. instruction은 큰따옴표가 포함된 문자열을 작은따옴표로 감쌉니다. owner, " | ", instruction을 연결하면 O'Brien | say "go"를 반환하며 스크립트에 역슬래시 이스케이프가 필요 없습니다.
Option Explicit On
SUB Main()
    VAR owner = "O'Brien"
    VAR instruction = 'say "go"'
    RETURN owner + " | " + instruction
END SUB
```

**매개변수 및 실행 설명:**

owner="O'Brien"에는 작은따옴표가 있습니다. instruction은 큰따옴표가 포함된 문자열을 작은따옴표로 감쌉니다. owner, " | ", instruction을 연결하면 O'Brien | say "go"를 반환하며 스크립트에 역슬래시 이스케이프가 필요 없습니다.

### 3. 논리 값도 숫자

```vb
# enabled=TRUE는 1, stopped=FALSE는 0을 저장합니다. 계산은 1*10+0=10입니다. Main은 계산된 숫자 결과를 반환하며 표준 논리 TRUE가 아닙니다.
Option Explicit On
SUB Main()
    VAR enabled = TRUE
    VAR stopped = FALSE
    RETURN enabled * 10 + stopped
END SUB
```

**매개변수 및 실행 설명:**

enabled=TRUE는 1, stopped=FALSE는 0을 저장합니다. 계산은 1*10+0=10입니다. Main은 계산된 숫자 결과를 반환하며 표준 논리 TRUE가 아닙니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: number / literal / HEX_NUMBER / DEC_NUMBER
Runtime/Interpreter.cs: VisitNumber / VisitLiteral / VisitSignedOperand
Runtime/InjectionApiUO.cs: TRUE / FALSE intrinsic values
-->
