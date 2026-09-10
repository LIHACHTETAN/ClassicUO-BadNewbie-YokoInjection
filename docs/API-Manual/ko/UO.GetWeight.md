# UO.GetWeight

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

현재 플레이어의 상태 계수를 읽습니다: 현재 무게(stones).

## 정확한 구문

```text
UO.GetWeight() -> Integer
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer — 현재 무게(stones), 모델 범위 0..65535입니다. 0은 실제 값, 미수신 데이터 또는 없거나 파괴된 Player일 수 있습니다. 수량이며 Boolean, ID, type이 아닙니다. 1은 한 단위이고 성공이 아닙니다. 객체를 열거하거나 배열을 반환하지 않습니다.

## 동작

- 인자가 없습니다. 표시된 정확한 시그니처를 사용하세요.
- 게임 스레드에서 Player.Weight를 읽습니다. 현재 Player가 없거나 파괴되었으면 0입니다. 장비 검색, 보너스 계산, 상태 요청, 갱신 대기가 없습니다. 존재하는 유령은 파괴된 Player와 다릅니다.
- Weight는 서버가 보고한 총무게를 stones로 읽습니다. 몸, 장비, 중첩 가방의 어떤 무게를 포함할지는 샤드 규칙에 따릅니다. 컨테이너 순회, 물품 무게 합산, 닫힌 가방 갱신을 하지 않습니다. 개별 물품의 Weight나 items 개수가 아닙니다.
- CharacterStatus는 고정 본문을 검증한 후 갱신합니다. Weight는 자신의 확장 상태, 슬롯은 type 3, Luck는 type 4, 서버 WeightMax는 type 5부터입니다. 선택적 계수가 없는 간략/구형 패킷은 이전 캐시를 유지합니다. 새 Player는 0부터 시작하며 호출이 최신 상태 수신을 증명하지는 않습니다.
- RegisterCharacterGetterAliases는 빠진 무인수 함수와 내장 이름을 등록합니다. 기존 호환 분기도 같은 필드를 읽습니다. 이름의 대소문자는 무관하며 괄호 없는 내장 이름은 변수로 가려지지 않으면 매번 읽습니다.
- 호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.

### 내부 함수: 호출부터 결과까지

상태 캐시 읽기의 네이티브 단계입니다. 예제의 CanCarry, LuckAtLeast, CanAddFollower는 전체 정의가 있는 사용자 BASIC 함수이며 숨겨진 네이티브 동작이 아닙니다. 인벤토리나 추종자를 변경하지 않습니다.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases는 빠진 무인수 함수와 내장 이름을 등록합니다. 기존 호환 분기도 같은 필드를 읽습니다. 이름의 대소문자는 무관하며 괄호 없는 내장 이름은 변수로 가려지지 않으면 매번 읽습니다.

`Weight GetWeight`.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `RegisterCharacterGetterAliases`.

#### 2. Invoke

게임 스레드에서 Player.Weight를 읽습니다. 현재 Player가 없거나 파괴되었으면 0입니다. 장비 검색, 보너스 계산, 상태 요청, 갱신 대기가 없습니다. 존재하는 유령은 파괴된 Player와 다릅니다.

Invoke는 게임 스레드에서 읽고 대기는 스크립트 취소에 대응합니다. status 요청, 타깃, 패킷 전송, 능력치 변경, 내장 지연이 없습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 3. CharacterStatus

CharacterStatus는 고정 본문을 검증한 후 갱신합니다. Weight는 자신의 확장 상태, 슬롯은 type 3, Luck는 type 4, 서버 WeightMax는 type 5부터입니다. 선택적 계수가 없는 간략/구형 패킷은 이전 캐시를 유지합니다. 새 Player는 0부터 시작하며 호출이 최신 상태 수신을 증명하지는 않습니다.

Weight는 서버가 보고한 총무게를 stones로 읽습니다. 몸, 장비, 중첩 가방의 어떤 무게를 포함할지는 샤드 규칙에 따릅니다. 컨테이너 순회, 물품 무게 합산, 닫힌 가방 갱신을 하지 않습니다. 개별 물품의 Weight나 items 개수가 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 함수 `CharacterStatus`.

#### 4. Clear

World.Clear는 Player를 제거합니다. 플레이어와 데이터가 다시 준비될 때까지 0입니다. 재접속 후 저장된 값만으로 조건 충족을 판단하지 마세요.

Integer — 현재 무게(stones), 모델 범위 0..65535입니다. 0은 실제 값, 미수신 데이터 또는 없거나 파괴된 Player일 수 있습니다. 수량이며 Boolean, ID, type이 아닙니다. 1은 한 단위이고 성공이 아닙니다. 객체를 열거하거나 배열을 반환하지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Clear`.

호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.


## 예제

### 캐시 계수 표시

```vb
# 캐시 계수 표시
#
# 현재 플레이어의 상태 계수를 읽습니다: 현재 무게(stones).
#
# Integer — 현재 무게(stones), 모델 범위 0..65535입니다. 0은 실제 값, 미수신 데이터 또는 없거나 파괴된 Player일 수 있습니다. 수량이며
# Boolean, ID, type이 아닙니다. 1은 한 단위이고 성공이 아닙니다. 객체를 열거하거나 배열을 반환하지 않습니다.

SUB Main()
    # value는 무인수 자기 플레이어 조회 한 번을 저장합니다. CStr은 뜻을 바꾸지 않고 저널용 문자열로 바꿉니다.

    VAR value = UO.GetWeight()
    UO.Print('Weight: ' + CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- value는 무인수 자기 플레이어 조회 한 번을 저장합니다. CStr은 뜻을 바꾸지 않고 저널용 문자열로 바꿉니다.

### 변화 관찰

```vb
# 변화 관찰
#
# 현재 플레이어의 상태 계수를 읽습니다: 현재 무게(stones).
#
# Integer — 현재 무게(stones), 모델 범위 0..65535입니다. 0은 실제 값, 미수신 데이터 또는 없거나 파괴된 Player일 수 있습니다. 수량이며
# Boolean, ID, type이 아닙니다. 1은 한 단위이고 성공이 아닙니다. 객체를 열거하거나 배열을 반환하지 않습니다.

SUB Main()
    # WAIT(500)은 before와 after 사이 500밀리초입니다. difference는 양수, 0, 음수일 수 있으며 중간 갱신이나 캐릭터 변경을 놓칠 수 있습니다.
    # 대기는 예제에 속합니다.

    VAR before = UO.GetWeight()
    WAIT(500)
    VAR after = UO.GetWeight()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**매개변수 및 실행 설명:**

- WAIT(500)은 before와 after 사이 500밀리초입니다. difference는 양수, 0, 음수일 수 있으며 중간 갱신이나 캐릭터 변경을 놓칠 수 있습니다. 대기는 예제에 속합니다.

### 전체 판단 함수

```vb
# 전체 판단 함수
#
# 현재 플레이어의 상태 계수를 읽습니다: 현재 무게(stones).
#
# Integer — 현재 무게(stones), 모델 범위 0..65535입니다. 0은 실제 값, 미수신 데이터 또는 없거나 파괴된 Player일 수 있습니다. 수량이며
# Boolean, ID, type이 아닙니다. 1은 한 단위이고 성공이 아닙니다. 객체를 열거하거나 배열을 반환하지 않습니다.

SUB Main()
    # CanCarry(extra)는 추가 무게를 stones로 받으며 10은 예시이고 스택 수가 아닙니다. 음수 extra, 없는 Player, maximum <= 0을
    # 거부합니다. 현재/최대값을 읽고 extra <= maximum - current에 대해 Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 뺄셈은
    # current + extra 오버플로를 피합니다. 이미 과적이면 extra=0도 false입니다. 로컬 추정이며 서버 허가가 아닙니다. 읽기는 원자적이지 않고 무게 0은
    # 미수신일 수 있습니다.

    IF CanCarry(10) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanCarry(extra)
    IF extra < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.GetWeight()
    VAR maximum = UO.MaxWeight()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extra <= maximum - current
END SUB
```

**매개변수 및 실행 설명:**

- CanCarry(extra)는 추가 무게를 stones로 받으며 10은 예시이고 스택 수가 아닙니다. 음수 extra, 없는 Player, maximum <= 0을 거부합니다. 현재/최대값을 읽고 extra <= maximum - current에 대해 Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 뺄셈은 current + extra 오버플로를 피합니다. 이미 과적이면 extra=0도 false입니다. 로컬 추정이며 서버 허가가 아닙니다. 읽기는 원자적이지 않고 무게 0은 미수신일 수 있습니다.
