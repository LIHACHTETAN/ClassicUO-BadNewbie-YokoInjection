# UO.MaxHP

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

로컬 모델에서 최대 체력 값을 읽습니다.

## 정확한 구문

```text
UO.MaxHP() -> Integer
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer — 필드 HitsMax 값이며 백분율이나 Boolean이 아닙니다. 0은 실제 값이거나 데이터 부재일 수 있습니다. 최대값이 0이면 나누지 마세요. 다른 mobile의 값은 알려지지 않았을 수 있습니다. HP/HitsMax는 정확한 점수 대신 서버의 상대적 척도일 수 있습니다. HP=0으로 사망을 증명할 수 없으며 Dead/IsDead를 사용합니다.

## 동작

- status를 열거나 서버에 갱신을 요청하지 않습니다. HP 부재 시 자동 요청하는 Stealth와 달리 이 클라이언트는 기존 데이터만 읽습니다. 능력치 변경이나 패킷 전송은 없습니다.
- 각 결과는 독립적인 읽기입니다. Exists와 다음 호출 사이에 세계가 바뀔 수 있으므로 여러 조회가 원자적 스냅샷을 이루지는 않습니다.
- 객체 조회 시 World.Get은 없거나 IsDestroyed인 항목을 제외하고 0을 반환합니다. HP/HitsMax는 해당 필드가 있는 아이템을 포함한 Entity를 읽고 Mana/Stamina는 Mobile만 읽습니다. 인수를 생략하면 self입니다. 인수 없는 이름에 ID 형식이 반드시 있는 것은 아니므로 시그니처를 확인하세요.
- 인자 없는 조회도 Player가 없거나 파괴되면 0입니다. World.Get 경유뿐 아니라 직접 Mana/Stamina와 그 최댓값도 포함합니다. 존재하는 죽은 캐릭터는 값을 유지할 수 있습니다.

### 내부 함수: 호출부터 결과까지

실제 C# 내부 단계입니다. ReadValue는 예제에 완전하게 정의된 보조 함수이며 숨겨진 내장 명령이 아닙니다.

#### 1. RegisterCharacterGetterAliases

runtime 생성 시 RegisterCharacterGetterAliases가 이름과 호출 형식을 등록합니다. 인수가 없으면 bridge.Self, 있으면 지정한 serial을 사용합니다. 기존 등록은 유지됩니다.

Integer — 필드 HitsMax 값이며 백분율이나 Boolean이 아닙니다. 0은 실제 값이거나 데이터 부재일 수 있습니다. 최대값이 0이면 나누지 마세요. 다른 mobile의 값은 알려지지 않았을 수 있습니다. HP/HitsMax는 정확한 점수 대신 서버의 상대적 척도일 수 있습니다. HP=0으로 사망을 증명할 수 없으며 Dead/IsDead를 사용합니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `RegisterCharacterGetterAliases`.

#### 2. Invoke

Invoke는 게임 스레드에서 읽습니다. 작업 스레드는 관리자의 처리를 기다리며 스크립트 취소가 대기를 중단합니다. 추가 지연이나 네트워크 요청은 없습니다.

각 결과는 독립적인 읽기입니다. Exists와 다음 호출 사이에 세계가 바뀔 수 있으므로 여러 조회가 원자적 스냅샷을 이루지는 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 3. Get

객체 조회 시 World.Get은 없거나 IsDestroyed인 항목을 제외하고 0을 반환합니다. HP/HitsMax는 해당 필드가 있는 아이템을 포함한 Entity를 읽고 Mana/Stamina는 Mobile만 읽습니다. 인수를 생략하면 self입니다. 인수 없는 이름에 ID 형식이 반드시 있는 것은 아니므로 시그니처를 확인하세요.

Integer — 필드 HitsMax 값이며 백분율이나 Boolean이 아닙니다. 0은 실제 값이거나 데이터 부재일 수 있습니다. 최대값이 0이면 나누지 마세요. 다른 mobile의 값은 알려지지 않았을 수 있습니다. HP/HitsMax는 정확한 점수 대신 서버의 상대적 척도일 수 있습니다. HP=0으로 사망을 증명할 수 없으며 Dead/IsDead를 사용합니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Get`.

status를 열거나 서버에 갱신을 요청하지 않습니다. HP 부재 시 자동 요청하는 Stealth와 달리 이 클라이언트는 기존 데이터만 읽습니다. 능력치 변경이나 패킷 전송은 없습니다.


## 예제

### 자신의 캐릭터 값 표시

```vb
# 자신의 캐릭터 값 표시
#
# 로컬 모델에서 최대 체력 값을 읽습니다.
#
# Integer — 필드 HitsMax 값이며 백분율이나 Boolean이 아닙니다. 0은 실제 값이거나 데이터 부재일 수 있습니다. 최대값이 0이면 나누지 마세요. 다른
# mobile의 값은 알려지지 않았을 수 있습니다. HP/HitsMax는 정확한 점수 대신 서버의 상대적 척도일 수 있습니다. HP=0으로 사망을 증명할 수 없으며
# Dead/IsDead를 사용합니다.

SUB Main()
    # 인수 없는 호출은 self를 읽습니다. value는 숫자 하나를 저장하며 STR은 메시지 표시용으로만 변환합니다.

    VAR value = UO.MaxHP()
    UO.Print('MaxHP: ' + STR(value))
END SUB
```

**매개변수 및 실행 설명:**

- 인수 없는 호출은 self를 읽습니다. value는 숫자 하나를 저장하며 STR은 메시지 표시용으로만 변환합니다.

### 조건 또는 계산에 값 사용

```vb
# 조건 또는 계산에 값 사용
#
# 로컬 모델에서 최대 체력 값을 읽습니다.
#
# Integer — 필드 HitsMax 값이며 백분율이나 Boolean이 아닙니다. 0은 실제 값이거나 데이터 부재일 수 있습니다. 최대값이 0이면 나누지 마세요. 다른
# mobile의 값은 알려지지 않았을 수 있습니다. HP/HitsMax는 정확한 점수 대신 서버의 상대적 척도일 수 있습니다. HP=0으로 사망을 증명할 수 없으며
# Dead/IsDead를 사용합니다.

SUB Main()
    # 이 필드의 임계값 또는 계산 예제입니다. 조건의 숫자는 예제 설정이며 서버 제한이 아닙니다. 나누기 전에 최대값이 양수인지 확인합니다.

    VAR value = UO.MaxHP()
    IF value > 0 THEN
        UO.Print('Known HP percent: ' + STR(UO.GetHP() * 100 / value))
    ELSE
        UO.Print('HP maximum unavailable')
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 이 필드의 임계값 또는 계산 예제입니다. 조건의 숫자는 예제 설정이며 서버 제한이 아닙니다. 나누기 전에 최대값이 양수인지 확인합니다.

### 완전한 ReadValue 보조 함수

```vb
# 완전한 ReadValue 보조 함수
#
# 로컬 모델에서 최대 체력 값을 읽습니다.
#
# Integer — 필드 HitsMax 값이며 백분율이나 Boolean이 아닙니다. 0은 실제 값이거나 데이터 부재일 수 있습니다. 최대값이 0이면 나누지 마세요. 다른
# mobile의 값은 알려지지 않았을 수 있습니다. HP/HitsMax는 정확한 점수 대신 서버의 상대적 척도일 수 있습니다. HP=0으로 사망을 증명할 수 없으며
# Dead/IsDead를 사용합니다.

SUB Main()
    # 이 이름에는 ID 형식이 없습니다. 인수 없는 ReadValue는 self를 읽고 WAIT(1000)으로 두 호출을 구분합니다. 스냅샷 비교는 중간 변화를 놓칠 수
    # 있습니다.

    VAR before = ReadValue()
    WAIT(1000)
    VAR after = ReadValue()
    UO.Print('Before: ' + CStr(before) + '; after: ' + CStr(after))
END SUB

SUB ReadValue()
    RETURN UO.MaxHP()
END SUB
```

**매개변수 및 실행 설명:**

- 이 이름에는 ID 형식이 없습니다. 인수 없는 ReadValue는 self를 읽고 WAIT(1000)으로 두 호출을 구분합니다. 스냅샷 비교는 중간 변화를 놓칠 수 있습니다.
