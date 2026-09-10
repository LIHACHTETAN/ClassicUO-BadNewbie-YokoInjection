# Sqr

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

제곱근을 계산합니다.

## 정확한 구문

```text
Sqr(number:Any) -> Decimal
```

## 매개변수

- `number` — 필수: Integer/Decimal 또는 소수점과 선택적 지수가 있는 십진 텍스트(예: "-1.25e2"). UI 언어와 무관합니다. 잘못된/16진 텍스트, Unit, Array, Object는 0입니다. 숫자 16진 리터럴은 이미 Integer입니다. NaN/Infinity도 가능합니다. 입력 >=0이면 음수가 아닌 제곱근입니다. 음수는 NaN, +Infinity는 Infinity, NaN은 유지됩니다.

## 반환값

Decimal — sqrt(number). 입력 >=0이면 음수가 아닌 제곱근입니다. 음수는 NaN, +Infinity는 Infinity, NaN은 유지됩니다. 숫자이며 ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

## 동작

- 스크립트 스레드에서 로컬 계산하며 서버 요청, 이동, 대상, 대기, 전역 변수 변경이 없습니다.
- Decimal은 이진 Double이며 .NET decimal이 아닙니다. 유한 근삿값은 오차 허용치로 비교합니다. NaN/Infinity를 좌표나 수량으로 쓰지 마세요.
- 입력 >=0이면 음수가 아닌 제곱근입니다. 음수는 NaN, +Infinity는 Infinity, NaN은 유지됩니다.

### 내부 함수: 호출부터 결과까지

실제 등록/변환 단계입니다. 완전한 보조 함수는 스크립트 수식을 보여 주며 플랫폼 수학 구현을 대체하지 않습니다.

#### 1. Register

Register는 한 인수 BASIC 이름을 네이티브 계산에 연결하고 변환 후 System.Math를 호출합니다. 숨은 스크립트나 서버 프로시저는 실행하지 않습니다.

Decimal — sqrt(number). 입력 >=0이면 음수가 아닌 제곱근입니다. 음수는 NaN, +Infinity는 Infinity, NaN은 유지됩니다. 숫자이며 ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 함수 `Register`.

#### 2. BasicDouble

BasicDouble은 Integer/Decimal을 유지하고 고정 문화권의 NumberStyles.Float로 텍스트를 읽으며 그 밖의 값은 0입니다. Abs는 일반 Integer를 직접 처리한 뒤 Double로 전환합니다.

필수: Integer/Decimal 또는 소수점과 선택적 지수가 있는 십진 텍스트(예: "-1.25e2"). UI 언어와 무관합니다. 잘못된/16진 텍스트, Unit, Array, Object는 0입니다. 숫자 16진 리터럴은 이미 Integer입니다. NaN/Infinity도 가능합니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 함수 `BasicDouble`.

스크립트 스레드에서 로컬 계산하며 서버 요청, 이동, 대상, 대기, 전역 변수 변경이 없습니다.


## 예제

### 직접 계산

```vb
# 직접 계산
#
# 제곱근을 계산합니다.
#
# Decimal — sqrt(number). 입력 >=0이면 음수가 아닌 제곱근입니다. 음수는 NaN, +Infinity는 Infinity, NaN은 유지됩니다. 숫자이며
# ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

SUB Main()
    # number = 25; 예상 결과 5(~는 근사). value가 결과를 저장하며 CStr은 Print용으로 형식화합니다.

    VAR value = Sqr(25)
    UO.Print(CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- number = 25; 예상 결과 5(~는 근사). value가 결과를 저장하며 CStr은 Print용으로 형식화합니다.

### 변수로 다른 입력 전달

```vb
# 변수로 다른 입력 전달
#
# 제곱근을 계산합니다.
#
# Decimal — sqrt(number). 입력 >=0이면 음수가 아닌 제곱근입니다. 음수는 NaN, +Infinity는 Infinity, NaN은 유지됩니다. 숫자이며
# ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

SUB Main()
    # number = 2; 예상 결과 ~1.4142135623730951(~는 근사). value가 결과를 저장하며 CStr은 Print용으로 형식화합니다.

    VAR inputValue = 2
    VAR value = Sqr(inputValue)
    UO.Print(CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- number = 2; 예상 결과 ~1.4142135623730951(~는 근사). value가 결과를 저장하며 CStr은 Print용으로 형식화합니다.

### 완전한 재사용 보조 함수

```vb
# 완전한 재사용 보조 함수
#
# 제곱근을 계산합니다.
#
# Decimal — sqrt(number). 입력 >=0이면 음수가 아닌 제곱근입니다. 음수는 NaN, +Infinity는 Infinity, NaN은 유지됩니다. 숫자이며
# ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

# manual-check: scalar-math Sqr
SUB Main()
    # dx/dy는 좌표 차이입니다. CDbl은 sqrt(dx²+dy²) 전 정수 오버플로를 막습니다. SegmentLength(3,4)=5; 유클리드 거리이며 경로나 충돌
    # 검사가 아닙니다.

    VAR value = SegmentLength(3,4)
    UO.Print(CStr(value))
END SUB

SUB SegmentLength(dx,dy)
    VAR x = CDbl(dx)
    VAR y = CDbl(dy)
    RETURN Sqr(x*x+y*y)
END SUB
```

**매개변수 및 실행 설명:**

- dx/dy는 좌표 차이입니다. CDbl은 sqrt(dx²+dy²) 전 정수 오버플로를 막습니다. SegmentLength(3,4)=5; 유클리드 거리이며 경로나 충돌 검사가 아닙니다.
