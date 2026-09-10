# UO.Dex

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

현재 민첩(Dexterity, DEX)을 읽습니다.

## 정확한 구문

```text
UO.Dex() -> Integer
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer: 모델에 저장된 현재 능력치 0..65535입니다. 백분율, ID, 기술 값, 잠금 모드, Boolean이 아닙니다. 0은 플레이어 없음/파괴됨 또는 대상 데이터 없음도 뜻합니다. = TRUE 대신 수치 조건과 비교하세요. 상한이나 보정 전 기본값을 보장하지 않습니다.

## 동작

- 인자가 없습니다. 표시된 정확한 시그니처를 사용하세요.
- Player가 존재하고 파괴되지 않았을 때 Player.Dexterity를 읽으며, 아니면 0입니다. 존재하는 죽은 캐릭터는 파괴된 객체가 아닙니다. HP, 마나, 스태미나에서 계산하지 않습니다.
- GetStr/GetInt/GetDex는 ObjID를 받지만 이 능력치는 PlayerMobile에만 저장됩니다. 다른 serial은 로드된 mobile이라도 0을 반환합니다. 일반 Stealth 설명과 다른 제한이며 다른 캐릭터의 값을 만들어 내지 않습니다.
- Invoke는 게임 스레드에서 읽고 대기는 스크립트 취소에 대응합니다. status 요청, 타깃, 패킷 전송, 능력치 변경, 내장 지연이 없습니다.
- 호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.
- UO. 유무와 대소문자에 관계없이 같은 능력치를 읽는 이름: `Dex Dexterity GetDex GetDexterity`.
- UO. 없는 Int(value)는 BASIC 숫자를 내림하고 Str(value)는 텍스트로 서식화합니다. 능력치를 읽는 UO.Int()/UO.Str()와 다른 연산입니다. GetInt(ObjID)는 숫자 반올림이 아닙니다.

### 내부 함수: 호출부터 결과까지

네이티브 읽기 단계입니다. AttributeAtLeast는 아래에 완전히 정의된 사용자 BASIC 함수이며 숨겨진 API나 능력치 변경 기능이 아닙니다.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases는 누락된 인자 없는 함수와 내장 이름을 등록합니다. 기존 호환 분기는 해당 getter를 선택하고 두 경로 모두 Integer를 반환합니다. 내장 이름은 변수가 가리지 않으면 다시 읽습니다.

UO. 유무와 대소문자에 관계없이 같은 능력치를 읽는 이름: `Dex Dexterity GetDex GetDexterity`.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `RegisterCharacterGetterAliases`.

#### 2. Invoke

Player가 존재하고 파괴되지 않았을 때 Player.Dexterity를 읽으며, 아니면 0입니다. 존재하는 죽은 캐릭터는 파괴된 객체가 아닙니다. HP, 마나, 스태미나에서 계산하지 않습니다. Invoke는 게임 스레드에서 읽고 대기는 스크립트 취소에 대응합니다. status 요청, 타깃, 패킷 전송, 능력치 변경, 내장 지연이 없습니다.

Integer: 모델에 저장된 현재 능력치 0..65535입니다. 백분율, ID, 기술 값, 잠금 모드, Boolean이 아닙니다. 0은 플레이어 없음/파괴됨 또는 대상 데이터 없음도 뜻합니다. = TRUE 대신 수치 조건과 비교하세요. 상한이나 보정 전 기본값을 보장하지 않습니다. 호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 3. CharacterStatus

CharacterStatus는 해당하는 자신 status 패킷의 STR/DEX/INT 필드를 Player.Dexterity에 대입합니다. 조회는 이 캐시를 읽고 새 패킷을 기다리지 않습니다.

Invoke는 게임 스레드에서 읽고 대기는 스크립트 취소에 대응합니다. status 요청, 타깃, 패킷 전송, 능력치 변경, 내장 지연이 없습니다.

프로젝트 소스: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 함수 `CharacterStatus`.

#### 4. Clear

World.Clear는 Player를 제거합니다. 플레이어와 데이터가 다시 준비될 때까지 0입니다. 재접속 후 저장된 값만으로 조건 충족을 판단하지 마세요.

Integer: 모델에 저장된 현재 능력치 0..65535입니다. 백분율, ID, 기술 값, 잠금 모드, Boolean이 아닙니다. 0은 플레이어 없음/파괴됨 또는 대상 데이터 없음도 뜻합니다. = TRUE 대신 수치 조건과 비교하세요. 상한이나 보정 전 기본값을 보장하지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Clear`.

World.Clear는 Player를 제거합니다. 플레이어와 데이터가 다시 준비될 때까지 0입니다. 재접속 후 저장된 값만으로 조건 충족을 판단하지 마세요.


## 예제

### 능력치 출력

```vb
# 능력치 출력
#
# 현재 민첩(Dexterity, DEX)을 읽습니다.
#
# Integer: 모델에 저장된 현재 능력치 0..65535입니다. 백분율, ID, 기술 값, 잠금 모드, Boolean이 아닙니다. 0은 플레이어 없음/파괴됨 또는 대상
# 데이터 없음도 뜻합니다. = TRUE 대신 수치 조건과 비교하세요. 상한이나 보정 전 기본값을 보장하지 않습니다.

SUB Main()
    # value는 수치를 보관하며 CStr는 일지용 텍스트로만 바꿉니다. 인자나 캐릭터 동작이 없습니다.

    VAR value = UO.Dex()
    UO.Print('Dexterity: ' + CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- value는 수치를 보관하며 CStr는 일지용 텍스트로만 바꿉니다. 인자나 캐릭터 동작이 없습니다.

### 두 관측 비교

```vb
# 두 관측 비교
#
# 현재 민첩(Dexterity, DEX)을 읽습니다.
#
# Integer: 모델에 저장된 현재 능력치 0..65535입니다. 백분율, ID, 기술 값, 잠금 모드, Boolean이 아닙니다. 0은 플레이어 없음/파괴됨 또는 대상
# 데이터 없음도 뜻합니다. = TRUE 대신 수치 조건과 비교하세요. 상한이나 보정 전 기본값을 보장하지 않습니다.

SUB Main()
    # before/after 간격은 1000밀리초이며 WAIT는 예제에 포함됩니다. change=after-before는 양수, 0, 음수일 수 있고 중간 업데이트나 접속
    # 종료를 단독으로 구별하지 못합니다.

    VAR before = UO.Dex()
    WAIT(1000)
    VAR after = UO.Dex()
    VAR change = after - before
    UO.Print('Change: ' + CStr(change))
END SUB
```

**매개변수 및 실행 설명:**

- before/after 간격은 1000밀리초이며 WAIT는 예제에 포함됩니다. change=after-before는 양수, 0, 음수일 수 있고 중간 업데이트나 접속 종료를 단독으로 구별하지 못합니다.

### 완전한 조건 검사 함수

```vb
# 완전한 조건 검사 함수
#
# 현재 민첩(Dexterity, DEX)을 읽습니다.
#
# Integer: 모델에 저장된 현재 능력치 0..65535입니다. 백분율, ID, 기술 값, 잠금 모드, Boolean이 아닙니다. 0은 플레이어 없음/파괴됨 또는 대상
# 데이터 없음도 뜻합니다. = TRUE 대신 수치 조건과 비교하세요. 상한이나 보정 전 기본값을 보장하지 않습니다.

SUB Main()
    # minimum=80은 예제 조건이지 상한이 아닙니다. AttributeAtLeast(minimum)는 플레이어 없음을 거부하고 한 번 읽어 >= minimum 비교로
    # Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 능력치 자체가 아닌 비교가 논리값입니다.

    IF AttributeAtLeast(80) = TRUE THEN
        UO.Print('Requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB AttributeAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.Dex()
    RETURN value >= minimum
END SUB
```

**매개변수 및 실행 설명:**

- minimum=80은 예제 조건이지 상한이 아닙니다. AttributeAtLeast(minimum)는 플레이어 없음을 거부하고 한 번 읽어 >= minimum 비교로 Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 능력치 자체가 아닌 비교가 논리값입니다.
