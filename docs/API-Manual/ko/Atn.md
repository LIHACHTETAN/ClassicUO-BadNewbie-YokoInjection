# Atn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

아크탄젠트를 계산합니다.

## 정확한 구문

```text
Atn(number:Any) -> Decimal
```

## 매개변수

- `number` — 필수: Integer/Decimal 또는 소수점과 선택적 지수가 있는 십진 텍스트(예: "-1.25e2"). UI 언어와 무관합니다. 잘못된/16진 텍스트, Unit, Array, Object는 0입니다. 숫자 16진 리터럴은 이미 Integer입니다. NaN/Infinity도 가능합니다. 입력은 기울기, 출력은 [-pi/2,pi/2] 라디안입니다. 무한대는 양 끝값, NaN은 유지됩니다. 두 좌표 atan2가 아닙니다.

## 반환값

Decimal — atan(number). 입력은 기울기, 출력은 [-pi/2,pi/2] 라디안입니다. 무한대는 양 끝값, NaN은 유지됩니다. 두 좌표 atan2가 아닙니다. 숫자이며 ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

## 동작

- 스크립트 스레드에서 로컬 계산하며 서버 요청, 이동, 대상, 대기, 전역 변수 변경이 없습니다.
- Decimal은 이진 Double이며 .NET decimal이 아닙니다. 유한 근삿값은 오차 허용치로 비교합니다. NaN/Infinity를 좌표나 수량으로 쓰지 마세요.
- 입력은 기울기, 출력은 [-pi/2,pi/2] 라디안입니다. 무한대는 양 끝값, NaN은 유지됩니다. 두 좌표 atan2가 아닙니다.

### 내부 함수: 호출부터 결과까지

실제 등록/변환 단계입니다. 완전한 보조 함수는 스크립트 수식을 보여 주며 플랫폼 수학 구현을 대체하지 않습니다.

#### 1. Register

Register는 한 인수 BASIC 이름을 네이티브 계산에 연결하고 변환 후 System.Math를 호출합니다. 숨은 스크립트나 서버 프로시저는 실행하지 않습니다.

Decimal — atan(number). 입력은 기울기, 출력은 [-pi/2,pi/2] 라디안입니다. 무한대는 양 끝값, NaN은 유지됩니다. 두 좌표 atan2가 아닙니다. 숫자이며 ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

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
# 아크탄젠트를 계산합니다.
#
# Decimal — atan(number). 입력은 기울기, 출력은 [-pi/2,pi/2] 라디안입니다. 무한대는 양 끝값, NaN은 유지됩니다. 두 좌표 atan2가
# 아닙니다. 숫자이며 ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

SUB Main()
    # number = 0; 예상 결과 0(~는 근사). value가 결과를 저장하며 CStr은 Print용으로 형식화합니다.

    VAR value = Atn(0)
    UO.Print(CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- number = 0; 예상 결과 0(~는 근사). value가 결과를 저장하며 CStr은 Print용으로 형식화합니다.

### 변수로 다른 입력 전달

```vb
# 변수로 다른 입력 전달
#
# 아크탄젠트를 계산합니다.
#
# Decimal — atan(number). 입력은 기울기, 출력은 [-pi/2,pi/2] 라디안입니다. 무한대는 양 끝값, NaN은 유지됩니다. 두 좌표 atan2가
# 아닙니다. 숫자이며 ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

SUB Main()
    # number = 1; 예상 결과 ~0.7853981633974483(~는 근사). value가 결과를 저장하며 CStr은 Print용으로 형식화합니다.

    VAR inputValue = 1
    VAR value = Atn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- number = 1; 예상 결과 ~0.7853981633974483(~는 근사). value가 결과를 저장하며 CStr은 Print용으로 형식화합니다.

### 완전한 재사용 보조 함수

```vb
# 완전한 재사용 보조 함수
#
# 아크탄젠트를 계산합니다.
#
# Decimal — atan(number). 입력은 기울기, 출력은 [-pi/2,pi/2] 라디안입니다. 무한대는 양 끝값, NaN은 유지됩니다. 두 좌표 atan2가
# 아닙니다. 숫자이며 ID나 성공 플래그가 아닙니다. 1/0을 성공/실패로 해석하지 마세요.

# manual-check: scalar-math Atn
SUB Main()
    # rise/run은 기울기입니다. run=0의 대체값 0은 수직 각도가 아닙니다. SlopeDegrees(1,1)≈45; 모든 사분면을 구별하지 않습니다.

    VAR value = SlopeDegrees(1,1)
    UO.Print(CStr(value))
END SUB

SUB SlopeDegrees(rise,run)
    IF run = 0 THEN
        RETURN 0
    END IF
    RETURN Atn(CDbl(rise)/CDbl(run))*180/3.141592653589793
END SUB
```

**매개변수 및 실행 설명:**

- rise/run은 기울기입니다. run=0의 대체값 0은 수직 각도가 아닙니다. SlopeDegrees(1,1)≈45; 모든 사분면을 구별하지 않습니다.
