# UO.GetResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

숫자 또는 이름으로 자신의 플레이어 저항 하나를 선택하여 읽습니다.

## 정확한 구문

```text
UO.GetResist(resistance:Any) -> Integer
```

## 매개변수

- `resistance` — resistance 필수. 숫자: 0=physical, 1=fire, 2=cold, 3=poison, 4=energy. 문자열: physical/phys/armor, fire, cold, poison, energy. 대소문자와 앞뒤 공백은 무시합니다. serial, type, hue, 타깃, 두 번째 인수는 없습니다.

## 반환값

Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된 Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공 표시가 아닙니다.

## 동작

- 값 종류를 먼저 구분합니다. 문자열 "1", "0"은 알 수 없는 이름으로 0을 반환하며 숫자 선택자가 아닙니다. 문자열이 아닌 Decimal은 0 방향으로 소수를 버립니다: 1.9 -> fire, -0.9 -> physical. TRUE=1은 fire, FALSE=0은 physical이며 Array/Unit도 0으로 바뀝니다. 명시적 정수나 허용된 이름을 사용하세요. AddObject 이름은 해석하지 않습니다.
- GetResistance는 bridge getter 하나만 선택합니다. 알 수 없는 숫자/이름은 필드 읽기 없이 Integer 0입니다. 다섯 필드를 원자적으로 읽거나 저항을 변경하지 않습니다.
- PhysicalResistance는 서버의 방어력/상태 필드입니다. 고전 규칙은 방어 수치, 저항 규칙은 물리 저항을 사용할 수 있습니다. API는 규칙을 변환하거나 피해 감소율을 계산하지 않습니다. Armor와 물리 별칭은 같은 필드를 읽습니다.
- 원소 필드는 CharacterStatus(0x11)의 type >= 4에서 수신합니다. 호출 자체는 서버 시대를 검사하지 않습니다. 필드가 없는 간략/구형 상태는 이전 캐시를 유지하며 새 Player는 0으로 시작합니다. 독 저항은 Poisoned 플래그가 아니며 어떤 저항도 Resisting Spells 기술이 아닙니다.
- CharacterStatus는 고정 본문을 검증한 후 상태를 변경하고 저항 word를 부호 있는 Int16으로 변환합니다. 본문이 잘렸으면 이전 데이터를 유지합니다. type 6의 선택적 꼬리는 기존 처리를 유지하며 이 명령들은 그 부분의 최대 저항을 읽지 않습니다.
- Invoke는 게임 스레드에서 읽고 대기는 스크립트 취소에 대응합니다. status 요청, 타깃, 패킷 전송, 능력치 변경, 내장 지연이 없습니다.
- 호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.

### 내부 함수: 호출부터 결과까지

로컬 읽기의 실제 네이티브 단계입니다. 아래 ResistanceAtLeast는 완전히 정의된 사용자 BASIC 함수이며 숨겨진 API나 보호 장비 착용 명령이 아닙니다.

#### 1. RegisterCharacterGetterAliases

GetResist(resistance)와 UO.GetResist(resistance)를 GetResistance에 연결된 단일 인수 함수로 등록합니다. 이 선택자에는 무인수 내장 값이 없습니다.

resistance 필수. 숫자: 0=physical, 1=fire, 2=cold, 3=poison, 4=energy. 문자열: physical/phys/armor, fire, cold, poison, energy. 대소문자와 앞뒤 공백은 무시합니다. serial, type, hue, 타깃, 두 번째 인수는 없습니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `RegisterCharacterGetterAliases`.

#### 2. GetResistance

값 종류를 먼저 구분합니다. 문자열 "1", "0"은 알 수 없는 이름으로 0을 반환하며 숫자 선택자가 아닙니다. 문자열이 아닌 Decimal은 0 방향으로 소수를 버립니다: 1.9 -> fire, -0.9 -> physical. TRUE=1은 fire, FALSE=0은 physical이며 Array/Unit도 0으로 바뀝니다. 명시적 정수나 허용된 이름을 사용하세요. AddObject 이름은 해석하지 않습니다.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`. GetResistance는 bridge getter 하나만 선택합니다. 알 수 없는 숫자/이름은 필드 읽기 없이 Integer 0입니다. 다섯 필드를 원자적으로 읽거나 저항을 변경하지 않습니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `GetResistance`.

#### 3. ToInt

여기서 ToInt는 문자열이 아닌 선택자만 받습니다. Integer 유지, Decimal은 0 방향 절삭, Array/Unit은 0입니다. 결과는 선택 인덱스이며 저항이 아닙니다. 문자열 이름은 GetResistance가 처리합니다.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/NumberConversions.cs`; 함수 `ToInt`.

#### 4. Invoke

Invoke는 위 표에서 선택한 Player 필드를 부호를 유지하여 읽습니다. Player가 없거나 파괴되었으면 0입니다. 상태를 요청하거나 새 데이터를 기다리지 않습니다.

Invoke는 게임 스레드에서 읽고 대기는 스크립트 취소에 대응합니다. status 요청, 타깃, 패킷 전송, 능력치 변경, 내장 지연이 없습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 5. CharacterStatus

CharacterStatus는 고정 본문을 검증한 후 상태를 변경하고 저항 word를 부호 있는 Int16으로 변환합니다. 본문이 잘렸으면 이전 데이터를 유지합니다. type 6의 선택적 꼬리는 기존 처리를 유지하며 이 명령들은 그 부분의 최대 저항을 읽지 않습니다.

PhysicalResistance는 서버의 방어력/상태 필드입니다. 고전 규칙은 방어 수치, 저항 규칙은 물리 저항을 사용할 수 있습니다. API는 규칙을 변환하거나 피해 감소율을 계산하지 않습니다. Armor와 물리 별칭은 같은 필드를 읽습니다. 원소 필드는 CharacterStatus(0x11)의 type >= 4에서 수신합니다. 호출 자체는 서버 시대를 검사하지 않습니다. 필드가 없는 간략/구형 상태는 이전 캐시를 유지하며 새 Player는 0으로 시작합니다. 독 저항은 Poisoned 플래그가 아니며 어떤 저항도 Resisting Spells 기술이 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 함수 `CharacterStatus`.

#### 6. Clear

World.Clear는 Player를 제거합니다. 플레이어와 데이터가 다시 준비될 때까지 0입니다. 재접속 후 저장된 값만으로 조건 충족을 판단하지 마세요.

Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된 Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공 표시가 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Clear`.

호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.


## 예제

### 대소문자가 섞인 이름 선택

```vb
# 대소문자가 섞인 이름 선택
#
# 숫자 또는 이름으로 자신의 플레이어 저항 하나를 선택하여 읽습니다.
#
# Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된
# Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공
# 표시가 아닙니다.

SUB Main()
    # resistance=" FiRe "는 앞뒤 공백과 대소문자를 무시하여 화염을 선택합니다. value는 부호 있는 숫자이며 타깃 커서를 열지 않습니다.

    VAR value = UO.GetResist(' FiRe ')
    UO.Print('Fire resistance: ' + CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- resistance=" FiRe "는 앞뒤 공백과 대소문자를 무시하여 화염을 선택합니다. value는 부호 있는 숫자이며 타깃 커서를 열지 않습니다.

### 숫자 및 문자열 선택자 비교

```vb
# 숫자 및 문자열 선택자 비교
#
# 숫자 또는 이름으로 자신의 플레이어 저항 하나를 선택하여 읽습니다.
#
# Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된
# Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공
# 표시가 아닙니다.

SUB Main()
    # 2는 냉기, "poison"은 독을 선택하며 serial이 아닙니다. 두 스냅샷 비교는 Boolean이고 독 저항은 중독 여부를 뜻하지 않습니다.

    VAR cold = UO.GetResist(2)
    VAR poison = UO.GetResist('poison')
    IF cold < poison THEN
        UO.Print('Cold resistance is lower')
    ELSE
        UO.Print('Cold resistance is equal or higher')
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 2는 냉기, "poison"은 독을 선택하며 serial이 아닙니다. 두 스냅샷 비교는 Boolean이고 독 저항은 중독 여부를 뜻하지 않습니다.

### 최소 저항 확인 전체 함수

```vb
# 최소 저항 확인 전체 함수
#
# 숫자 또는 이름으로 자신의 플레이어 저항 하나를 선택하여 읽습니다.
#
# Integer — 클라이언트 모델의 부호 있는 상태 값, -32768..32767입니다. 음수를 유지합니다. 0은 실제 저항, 미수신 값 또는 없거나 파괴된
# Player를 뜻할 수 있으며 GetResist는 알 수 없는 선택자에도 0을 반환합니다. Boolean, ID, 기술, 저항 상한이 아닙니다. 1은 1포인트이며 성공
# 표시가 아닙니다.

SUB Main()
    # minimum=50은 예시 조건이며 상한이 아닙니다. ResistanceAtLeast는 없는 Player를 거부하고 한 번 읽어 value >= minimum에 대해
    # Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 저항 자체는 Boolean이 아닙니다. 아래에 전체 정의가 있습니다.
    # selector를 그대로 GetResist에 전달합니다. 예제는 "fire"를 씁니다. 함수는 Player 존재를 검사하지만 임의 선택자나 최신 상태 여부는 검증하지
    # 않습니다. 위 목록의 선택자를 사용하세요.

    IF ResistanceAtLeast('fire', 50) = TRUE THEN
        UO.Print('Local fire resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(selector, minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetResist(selector)
    RETURN value >= minimum
END SUB
```

**매개변수 및 실행 설명:**

- minimum=50은 예시 조건이며 상한이 아닙니다. ResistanceAtLeast는 없는 Player를 거부하고 한 번 읽어 value >= minimum에 대해 Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 저항 자체는 Boolean이 아닙니다. 아래에 전체 정의가 있습니다.
- selector를 그대로 GetResist에 전달합니다. 예제는 "fire"를 씁니다. 함수는 Player 존재를 검사하지만 임의 선택자나 최신 상태 여부는 검증하지 않습니다. 위 목록의 선택자를 사용하세요.
