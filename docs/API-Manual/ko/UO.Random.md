# UO.Random

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

의사 난수 정수 하나를 선택합니다. Random(min,max)는 양쪽 경계를 포함하고, 기존 Random(max)는 상한을 포함하지 않습니다.

## 정확한 구문

```text
UO.Random(max:Integer) -> Integer
UO.Random(min:Integer, max:Integer) -> Integer
```

## 매개변수

- `min` — 하한이며 인수가 두 개일 때만 사용합니다. -2147483648부터 2147483647까지의 부호 있는 32비트 정수로, max 이하여야 합니다.
- `max` — 인수가 두 개: 포함되는 상한이며 모든 Integer 값이 가능합니다. 인수가 하나: 제외되는 상한이며 0..2147483647입니다. Random(0)은 0을 반환합니다.

## 반환값

Integer — 선택한 숫자 하나입니다. 논리값이나 serial이 아닙니다. 두 인수: min <= 결과 <= max. 양수 인수 하나: 0 <= 결과 < max. 같은 값이 반복될 수 있습니다.

## 동작

- 인수가 없는 형식은 없습니다. 경계가 같으면 그 값을 반환합니다. 경계를 거꾸로 지정하거나 단일 인수를 음수로 지정하면 스크립트 오류가 발생하며, 경계를 자동으로 바꾸지 않습니다.
- max+1 오버플로 없이 부호 있는 32비트 전체 범위를 지원합니다. 일정 간격의 소수가 필요하면 정수를 선택한 뒤 나눕니다. 예: Random(0,100)/100.0.
- 생성기는 스크립트 runtime에 속하고 동시 호출은 동기화됩니다. seed 매개변수는 없으며 BASIC Rnd와 다른 함수입니다. 같은 결과를 다시 쓰려면 변수에 저장합니다.
- 로컬 계산만 하며 대기, 이동, 패킷 전송을 하지 않습니다. 무작위 좌표는 지도와 경로를 따로 확인해야 합니다. Random(0)=0이어도 빈 배열에는 유효한 인덱스가 없습니다.

## 예제

### 주사위 굴리기

```vb
# 주사위 굴리기
#
# 의사 난수 정수 하나를 선택합니다. Random(min,max)는 양쪽 경계를 포함하고, 기존 Random(max)는 상한을 포함하지 않습니다.
#
# Integer — 선택한 숫자 하나입니다. 논리값이나 serial이 아닙니다. 두 인수: min <= 결과 <= max. 양수 인수 하나: 0 <= 결과 < max.
# 같은 값이 반복될 수 있습니다.

SUB Main()
    # min=1, max=6은 여섯 값을 모두 포함합니다. roll에 한 번의 결과를 저장하고 STR로 문자열로 바꿉니다. 다음 호출에서 같은 값이 나올 수도 있습니다.

    VAR roll = UO.Random(1, 6)
    UO.Print(STR(roll))
END SUB
```

**매개변수 및 실행 설명:**

- min=1, max=6은 여섯 값을 모두 포함합니다. roll에 한 번의 결과를 저장하고 STR로 문자열로 바꿉니다. 다음 호출에서 같은 값이 나올 수도 있습니다.

### 무작위 시간 동안 대기

```vb
# 무작위 시간 동안 대기
#
# 의사 난수 정수 하나를 선택합니다. Random(min,max)는 양쪽 경계를 포함하고, 기존 Random(max)는 상한을 포함하지 않습니다.
#
# Integer — 선택한 숫자 하나입니다. 논리값이나 serial이 아닙니다. 두 인수: min <= 결과 <= max. 양수 인수 하나: 0 <= 결과 < max.
# 같은 값이 반복될 수 있습니다.

SUB Main()
    # min=350, max=700은 경계를 포함한 밀리초 범위입니다. Random은 delay를 계산하고 UO.Wait(delay)가 실제로 기다립니다. 서버에 필요한 최소
    # 지연을 유지하세요.

    VAR delay = UO.Random(350, 700)
    UO.Print(STR(delay))
    UO.Wait(delay)
END SUB
```

**매개변수 및 실행 설명:**

- min=350, max=700은 경계를 포함한 밀리초 범위입니다. Random은 delay를 계산하고 UO.Wait(delay)가 실제로 기다립니다. 서버에 필요한 최소 지연을 유지하세요.

### 기존 인덱스 형식과 같은 경계

```vb
# 기존 인덱스 형식과 같은 경계
#
# 의사 난수 정수 하나를 선택합니다. Random(min,max)는 양쪽 경계를 포함하고, 기존 Random(max)는 상한을 포함하지 않습니다.
#
# Integer — 선택한 숫자 하나입니다. 논리값이나 serial이 아닙니다. 두 인수: min <= 결과 <= max. 양수 인수 하나: 0 <= 결과 < max.
# 같은 값이 반복될 수 있습니다.

SUB Main()
    # Random(10)은 0..9이며 10은 나오지 않습니다. Random(7,7)은 항상 7입니다. Random(-2,2)는 -2,-1,0,1,2 중 하나입니다. 각 식은
    # 별도로 값을 선택합니다.

    VAR index = UO.Random(10)
    VAR fixedValue = UO.Random(7, 7)
    VAR offset = UO.Random(-2, 2)
    UO.Print(STR(index) + ', ' + STR(fixedValue) + ', ' + STR(offset))
END SUB
```

**매개변수 및 실행 설명:**

- Random(10)은 0..9이며 10은 나오지 않습니다. Random(7,7)은 항상 7입니다. Random(-2,2)는 -2,-1,0,1,2 중 하나입니다. 각 식은 별도로 값을 선택합니다.
