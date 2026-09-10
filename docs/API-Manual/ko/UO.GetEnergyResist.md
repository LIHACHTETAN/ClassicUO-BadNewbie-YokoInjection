# UO.GetEnergyResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

현재 플레이어의 저항 필드를 읽습니다: 에너지.

## 정확한 구문

```text
UO.GetEnergyResist() -> Integer
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된 Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공 표시가 아닙니다.

## 동작

- 인자가 없습니다. 표시된 정확한 시그니처를 사용하세요.
- 게임 스레드에서 Player.EnergyResistance를 읽습니다. 현재 Player가 없거나 파괴되었으면 0입니다. 장비 검색, 보너스 계산, 상태 요청, 갱신 대기가 없습니다. 존재하는 유령은 파괴된 Player와 다릅니다.
- 원소 필드는 CharacterStatus(0x11)의 type >= 4에서 수신합니다. 호출 자체는 서버 시대를 검사하지 않습니다. 필드가 없는 간략/구형 상태는 이전 캐시를 유지하며 새 Player는 0으로 시작합니다. 독 저항은 Poisoned 플래그가 아니며 어떤 저항도 Resisting Spells 기술이 아닙니다.
- CharacterStatus는 고정 본문을 검증한 후 상태를 변경하고 저항 word를 부호 있는 Int16으로 변환합니다. 본문이 잘렸으면 이전 데이터를 유지합니다. type 6의 선택적 꼬리는 기존 처리를 유지하며 이 명령들은 그 부분의 최대 저항을 읽지 않습니다.
- 호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.
- RegisterCharacterGetterAliases는 빠진 무인수 함수와 내장 이름을 등록합니다. 기존 호환 분기도 같은 필드를 읽습니다. 이름의 대소문자는 무관하며 괄호 없는 내장 이름은 변수로 가려지지 않으면 매번 읽습니다.

### 내부 함수: 호출부터 결과까지

로컬 읽기의 실제 네이티브 단계입니다. 아래 ResistanceAtLeast는 완전히 정의된 사용자 BASIC 함수이며 숨겨진 API나 보호 장비 착용 명령이 아닙니다.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases는 빠진 무인수 함수와 내장 이름을 등록합니다. 기존 호환 분기도 같은 필드를 읽습니다. 이름의 대소문자는 무관하며 괄호 없는 내장 이름은 변수로 가려지지 않으면 매번 읽습니다.

`EnergyResist ResistEnergy GetEnergyResist GetResistEnergy`.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `RegisterCharacterGetterAliases`.

#### 2. Invoke

게임 스레드에서 Player.EnergyResistance를 읽습니다. 현재 Player가 없거나 파괴되었으면 0입니다. 장비 검색, 보너스 계산, 상태 요청, 갱신 대기가 없습니다. 존재하는 유령은 파괴된 Player와 다릅니다.

Invoke는 게임 스레드에서 읽고 대기는 스크립트 취소에 대응합니다. status 요청, 타깃, 패킷 전송, 능력치 변경, 내장 지연이 없습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 3. CharacterStatus

CharacterStatus는 고정 본문을 검증한 후 상태를 변경하고 저항 word를 부호 있는 Int16으로 변환합니다. 본문이 잘렸으면 이전 데이터를 유지합니다. type 6의 선택적 꼬리는 기존 처리를 유지하며 이 명령들은 그 부분의 최대 저항을 읽지 않습니다.

원소 필드는 CharacterStatus(0x11)의 type >= 4에서 수신합니다. 호출 자체는 서버 시대를 검사하지 않습니다. 필드가 없는 간략/구형 상태는 이전 캐시를 유지하며 새 Player는 0으로 시작합니다. 독 저항은 Poisoned 플래그가 아니며 어떤 저항도 Resisting Spells 기술이 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 함수 `CharacterStatus`.

#### 4. Clear

World.Clear는 Player를 제거합니다. 플레이어와 데이터가 다시 준비될 때까지 0입니다. 재접속 후 저장된 값만으로 조건 충족을 판단하지 마세요.

Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된 Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공 표시가 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Clear`.

호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.


## 예제

### 캐시 값 출력

```vb
# 캐시 값 출력
#
# 현재 플레이어의 저항 필드를 읽습니다: 에너지.
#
# Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된
# Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공
# 표시가 아닙니다.

SUB Main()
    # value는 무인수 플레이어 조회 한 번을 저장합니다. CStr은 저널 출력용 문자열로 만듭니다.

    VAR value = UO.GetEnergyResist()
    UO.Print('EnergyResistance: ' + CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- value는 무인수 플레이어 조회 한 번을 저장합니다. CStr은 저널 출력용 문자열로 만듭니다.

### 두 관측 비교

```vb
# 두 관측 비교
#
# 현재 플레이어의 저항 필드를 읽습니다: 에너지.
#
# Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된
# Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공
# 표시가 아닙니다.

SUB Main()
    # before와 after 사이 WAIT(500)은 500밀리초입니다. difference는 음수일 수 있고 중간 갱신을 놓칠 수 있습니다. 대기는 예제에 속합니다.

    VAR before = UO.GetEnergyResist()
    WAIT(500)
    VAR after = UO.GetEnergyResist()
    VAR difference = after - before
    UO.Print('Resistance change: ' + CStr(difference))
END SUB
```

**매개변수 및 실행 설명:**

- before와 after 사이 WAIT(500)은 500밀리초입니다. difference는 음수일 수 있고 중간 갱신을 놓칠 수 있습니다. 대기는 예제에 속합니다.

### 최소 저항 확인 전체 함수

```vb
# 최소 저항 확인 전체 함수
#
# 현재 플레이어의 저항 필드를 읽습니다: 에너지.
#
# Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된
# Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공
# 표시가 아닙니다.

SUB Main()
    # minimum=50은 예시 조건이며 상한이 아닙니다. ResistanceAtLeast는 없는 Player를 거부하고 한 번 읽어 value >= minimum에 대해
    # Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 저항 자체는 Boolean이 아닙니다. 아래에 전체 정의가 있습니다.

    IF ResistanceAtLeast(50) = TRUE THEN
        UO.Print('Local resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetEnergyResist()
    RETURN value >= minimum
END SUB
```

**매개변수 및 실행 설명:**

- minimum=50은 예시 조건이며 상한이 아닙니다. ResistanceAtLeast는 없는 Player를 거부하고 한 번 읽어 value >= minimum에 대해 Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 저항 자체는 Boolean이 아닙니다. 아래에 전체 정의가 있습니다.
