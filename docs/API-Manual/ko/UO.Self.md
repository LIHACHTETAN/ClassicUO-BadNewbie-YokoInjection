# UO.Self

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

현재 캐릭터 ID를 반환합니다.

## 정확한 구문

```text
UO.Self() -> Integer
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer — serial/ID이며 graphic/type, 레이어, 수량, Boolean이 아닙니다. 0은 현재 객체 없음입니다. 32비트를 모두 보존하므로 = TRUE 또는 > 0 대신 <> 0으로 검사합니다. 저장한 결과는 자동 갱신되지 않습니다. World.Player.Serial을 읽습니다. Player가 없거나 파괴되었으면 0입니다. 사망과 파괴는 다릅니다. 존재하는 유령도 캐릭터 ID를 유지합니다.

## 동작

- 매개변수가 없습니다. Invoke를 통해 게임 스레드에서 로컬 상태를 읽으며 스크립트 취소로 스레드 대기를 중단할 수 있습니다. 패킷 전송, 컨테이너 열기, target 활성화, 아이템 이동을 하지 않습니다.
- 괄호 없는 self/backpack은 같은 이름의 변수로 가리지 않으면 매번 다시 읽습니다. 따옴표 안의 별칭은 받는 명령이 해석합니다. 이동 목적지의 "self"는 배낭이지만 UO.Self()는 캐릭터 serial입니다. 컨테이너 ID에는 UO.Backpack()을 명시하세요.
- World.Clear는 Player를 제거하며 이후 읽기는 0입니다. 로그인이나 배낭 교체로 ID가 바뀔 수 있습니다. 여러 읽기는 원자적 스냅샷이 아닙니다. 0이 아닌 ID는 연결, 서버 허가, 내용물 로딩을 증명하지 않습니다.

### 내부 함수: 호출부터 결과까지

아래는 실제 클라이언트 객체를 읽는 내부 단계입니다. IsOwnSerial은 예제에 완전히 정의된 도우미이며 별도의 내장 API가 아닙니다.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility가 인수 없는 분기를 선택하고 bridge 정수를 InjectionValue로 감쌉니다. Pascal 출력 매개변수나 추가 선택 인수는 없습니다.

Integer — serial/ID이며 graphic/type, 레이어, 수량, Boolean이 아닙니다. 0은 현재 객체 없음입니다. 32비트를 모두 보존하므로 = TRUE 또는 > 0 대신 <> 0으로 검사합니다. 저장한 결과는 자동 갱신되지 않습니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ExecuteStealthCompatibility`.

#### 2. Invoke

World.Player.Serial을 읽습니다. Player가 없거나 파괴되었으면 0입니다. 사망과 파괴는 다릅니다. 존재하는 유령도 캐릭터 ID를 유지합니다. Invoke는 게임 스레드에서 읽습니다. 작업 스레드는 관리자의 처리를 기다리며 스크립트 취소가 대기를 중단합니다. 추가 지연이나 네트워크 요청은 없습니다.

Integer — serial/ID이며 graphic/type, 레이어, 수량, Boolean이 아닙니다. 0은 현재 객체 없음입니다. 32비트를 모두 보존하므로 = TRUE 또는 > 0 대신 <> 0으로 검사합니다. 저장한 결과는 자동 갱신되지 않습니다. 매개변수가 없습니다. Invoke를 통해 게임 스레드에서 로컬 상태를 읽으며 스크립트 취소로 스레드 대기를 중단할 수 있습니다. 패킷 전송, 컨테이너 열기, target 활성화, 아이템 이동을 하지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 3. Clear

World.Clear는 Player를 제거하며 이후 읽기는 0입니다. 로그인이나 배낭 교체로 ID가 바뀔 수 있습니다. 여러 읽기는 원자적 스냅샷이 아닙니다. 0이 아닌 ID는 연결, 서버 허가, 내용물 로딩을 증명하지 않습니다.

World.Clear는 Player를 제거하며 이후 읽기는 0입니다. 로그인이나 배낭 교체로 ID가 바뀔 수 있습니다. 여러 읽기는 원자적 스냅샷이 아닙니다. 0이 아닌 ID는 연결, 서버 허가, 내용물 로딩을 증명하지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Clear`.

World.Clear는 Player를 제거하며 이후 읽기는 0입니다. 로그인이나 배낭 교체로 ID가 바뀔 수 있습니다. 여러 읽기는 원자적 스냅샷이 아닙니다. 0이 아닌 ID는 연결, 서버 허가, 내용물 로딩을 증명하지 않습니다.


## 예제

### ID 읽기 및 출력

```vb
# ID 읽기 및 출력
#
# 현재 캐릭터 ID를 반환합니다.
#
# Integer — serial/ID이며 graphic/type, 레이어, 수량, Boolean이 아닙니다. 0은 현재 객체 없음입니다. 32비트를 모두 보존하므로 =
# TRUE 또는 > 0 대신 <> 0으로 검사합니다. 저장한 결과는 자동 갱신되지 않습니다. World.Player.Serial을 읽습니다. Player가 없거나
# 파괴되었으면 0입니다. 사망과 파괴는 다릅니다. 존재하는 유령도 캐릭터 ID를 유지합니다.

SUB Main()
    # id는 호출 결과 하나를 저장하고 HEX는 일지용 serial 형식을 만듭니다. 객체를 선택하거나 사용하지 않습니다.

    VAR id = UO.Self()
    UO.Print('ID: ' + HEX(id))
END SUB
```

**매개변수 및 실행 설명:**

- id는 호출 결과 하나를 저장하고 HEX는 일지용 serial 형식을 만듭니다. 객체를 선택하거나 사용하지 않습니다.

### ID 변경 감지

```vb
# ID 변경 감지
#
# 현재 캐릭터 ID를 반환합니다.
#
# Integer — serial/ID이며 graphic/type, 레이어, 수량, Boolean이 아닙니다. 0은 현재 객체 없음입니다. 32비트를 모두 보존하므로 =
# TRUE 또는 > 0 대신 <> 0으로 검사합니다. 저장한 결과는 자동 갱신되지 않습니다. World.Player.Serial을 읽습니다. Player가 없거나
# 파괴되었으면 0입니다. 사망과 파괴는 다릅니다. 존재하는 유령도 캐릭터 ID를 유지합니다.

SUB Main()
    # before/after는 250밀리초 간격입니다. WAIT는 예제에만 있습니다. 끝점 ID가 같아도 중간 변경은 놓칠 수 있습니다.

    VAR before = UO.Self()
    WAIT(250)
    VAR after = UO.Self()
    IF before <> after THEN
        UO.Print('ID changed: ' + HEX(after))
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- before/after는 250밀리초 간격입니다. WAIT는 예제에만 있습니다. 끝점 ID가 같아도 중간 변경은 놓칠 수 있습니다.

### 완전한 IsOwnSerial 도우미

```vb
# 완전한 IsOwnSerial 도우미
#
# 현재 캐릭터 ID를 반환합니다.
#
# Integer — serial/ID이며 graphic/type, 레이어, 수량, Boolean이 아닙니다. 0은 현재 객체 없음입니다. 32비트를 모두 보존하므로 =
# TRUE 또는 > 0 대신 <> 0으로 검사합니다. 저장한 결과는 자동 갱신되지 않습니다. World.Player.Serial을 읽습니다. Player가 없거나
# 파괴되었으면 0입니다. 사망과 파괴는 다릅니다. 존재하는 유령도 캐릭터 ID를 유지합니다.

SUB Main()
    # candidate는 저장된 LastTarget ID입니다. IsOwnSerial(candidate)는 serial 하나를 받아 현재의 0이 아닌 자신의 ID면
    # Integer Boolean 1=TRUE, 아니면 0=FALSE를 반환합니다. 함수 정의가 모두 포함되며 target을 바꾸지 않습니다.

    VAR candidate = UO.LastTarget()
    IF IsOwnSerial(candidate) = TRUE THEN
        UO.Print('Own object selected')
    ELSE
        UO.Print('Different object or no own object')
    END IF
END SUB

SUB IsOwnSerial(candidate)
    VAR current = UO.Self()
    RETURN current <> 0 AND current = candidate
END SUB
```

**매개변수 및 실행 설명:**

- candidate는 저장된 LastTarget ID입니다. IsOwnSerial(candidate)는 serial 하나를 받아 현재의 0이 아닌 자신의 ID면 Integer Boolean 1=TRUE, 아니면 0=FALSE를 반환합니다. 함수 정의가 모두 포함되며 target을 바꾸지 않습니다.
