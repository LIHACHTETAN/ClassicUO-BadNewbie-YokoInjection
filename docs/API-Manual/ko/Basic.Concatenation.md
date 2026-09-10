# String + / &

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

+ 또는 Basic 호환 표기 &로 텍스트를 연결합니다. 수량이나 좌표 같은 숫자는 CStr로 명시적으로 변환한 뒤 메시지에 추가하세요.

## 정확한 구문

```text
leftText + rightText
leftText & rightText
"label" & CStr(number)
```

## 매개변수

- `leftText` — 왼쪽 텍스트: 리터럴, String 변수 또는 텍스트로 바꾼 함수 결과입니다.
- `rightText` — 오른쪽 텍스트입니다. CStr(number)는 숫자를 바꾸고 CStr(Unit)은 빈 문자열입니다. 공백이나 콜론 등 구분자는 직접 넣으세요.

## 반환값

양쪽이 String이면 String이며 성공 플래그가 아닙니다. 이 엔진은 &를 +로 바꾸어 같은 규칙을 사용합니다. 숫자끼리는 더하므로 2 & 3은 Integer 5입니다. String과 숫자를 섞으면 오류이며 VB의 암시적 텍스트 변환과 다릅니다.

## 동작

- 양쪽을 순서대로 계산하여 연결하고 연속 연결은 왼쪽부터 처리합니다. 숫자 계산은 괄호로 묶고 결과를 변환한 뒤 연결하세요.
- 구분자, 공백, 따옴표, 줄바꿈은 자동 추가하지 않습니다. 문자열 리터럴 안의 &는 그대로이며 논리 토큰 &&는 AND로 유지됩니다.
- CStr은 클라이언트 언어와 무관한 숫자 형식을 쓰고 소수점은 마침표입니다. 변환과 연결 자체는 출력하거나 전송하지 않습니다. 필요하면 결과 String을 다음 API에 넘기세요.
- 문자열은 불변이므로 연결은 원본 변수를 바꾸지 않고 새 값을 만듭니다. 큰 문자열을 계속 늘리면 내용이 복사되므로 루프마다 보고서 전체를 다시 만들기보다 필요한 출력만 만드세요.

## 예제

### 1. 수량에 레이블 추가

```vb
# amount=50은 Integer이고 CStr(amount)는 "50"입니다. "Items: "에는 콜론과 끝 공백이 있습니다. Main은 "Items: 50"을 반환하며 자동 출력하지 않습니다.
Option Explicit On
SUB Main()
    VAR amount = 50
    RETURN "Items: " & CStr(amount)
END SUB
```

**매개변수 및 실행 설명:**

amount=50은 Integer이고 CStr(amount)는 "50"입니다. "Items: "에는 콜론과 끝 공백이 있습니다. Main은 "Items: 50"을 반환하며 자동 출력하지 않습니다.

### 2. 재사용할 완전한 함수

```vb
# Label은 name="ore", amount=3을 받아 이름, 직접 넣은 콜론, CStr(amount)를 연결합니다. 전체 함수가 "ore:3"을 Main에 반환하며 다른 이름과 수량에도 사용할 수 있습니다.
Option Explicit On
FUNCTION Label(name, amount)
    RETURN name + ":" + CStr(amount)
END FUNCTION
SUB Main()
    RETURN Label("ore", 3)
END SUB
```

**매개변수 및 실행 설명:**

Label은 name="ore", amount=3을 받아 이름, 직접 넣은 콜론, CStr(amount)를 연결합니다. 전체 함수가 "ore:3"을 Main에 반환하며 다른 이름과 수량에도 사용할 수 있습니다.

### 3. 계산 후 연결

```vb
# CStr(2+3)은 5를 먼저 계산하고 "5"로 바꿉니다. 두 번째 리터럴의 세미콜론, 공백, A&B는 유지됩니다. Main은 "Total: 5; literal: A&B"를 반환합니다.
Option Explicit On
SUB Main()
    RETURN "Total: " & CStr(2 + 3) & "; literal: A&B"
END SUB
```

**매개변수 및 실행 설명:**

CStr(2+3)은 5를 먼저 계산하고 "5"로 바꿉니다. 두 번째 리터럴의 세미콜론, 공백, A&B는 유지됩니다. Main은 "Total: 5; literal: A&B"를 반환합니다.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: ProtectLiteralText / ReplaceConcatenationOutsideLiterals
Runtime/InjectionValue.cs: operator + / explicit operator string
Runtime/InjectionApi.cs: CStr
-->
