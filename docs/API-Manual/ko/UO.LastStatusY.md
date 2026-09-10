# UO.LastStatusY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

마지막으로 상태를 수락한 객체의 저장된 Y 좌표를 반환합니다.

## 정확한 구문

```text
UO.LastStatusY() -> Integer
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer — 저장된 Y 좌표로 상태 창의 픽셀이나 Boolean이 아닙니다. 첫 상태 이전과 세계 초기화 후에는 0이지만 실제 좌표 0도 유효합니다. UO.LastStatus()로 기록 존재를 확인하세요.

## 동작

- 매개변수가 없습니다. 읽기는 패킷을 보내거나 창을 열거나 응답을 기다리지 않습니다. UO.GetStatus(id), RequestStats, UpdateObject는 데이터를 요청하며 요청 전송 자체는 LastStatus를 바꾸지 않습니다.
- 수락한 0x11 패킷은 serial과 알려진 X/Y를 모든 스크립트가 공유하는 World에 함께 저장합니다. 알 수 없거나 파괴된 객체, 불완전한 기본 패킷은 기록을 교체하지 않습니다. 이후 다른 객체의 상태가 기록을 교체할 수 있습니다.
- X/Y는 수신 당시 Entity 좌표이며 현재 위치가 아닙니다. mobile은 세계 칸이지만 컨테이너 안의 아이템은 내용물 좌표일 수 있습니다. 상태 패킷 자체에는 X/Y가 없습니다. 나중의 이동/삭제는 저장값을 바꾸지 않으며 World.Clear가 초기화합니다. 존재하는 객체의 현재 위치는 GetX/GetY로 읽습니다.
- 별도 호출은 원자적 스냅샷이 아니며 호출 사이에 갱신될 수 있습니다. serial이 같아도 내 요청에 대한 새 응답임을 증명하지 않습니다. 괄호 없는 laststatus는 동적 내장 값이지만 같은 이름의 변수로 가릴 수 있습니다. UO.LastStatus()는 등록된 함수입니다.

### 내부 함수: 호출부터 결과까지

실제 C# 내부 단계입니다. ReadSavedStatus는 예제에 완전하게 정의된 보조 함수이며 숨겨진 내장 명령이 아닙니다.

#### 1. CharacterStatus

CharacterStatus는 World.Get으로 기본 패킷과 Entity를 검증하고 상태 및 serial/X/Y를 저장합니다. 위치는 상태 패킷이 아닌 Entity에서 읽습니다.

Integer — 저장된 Y 좌표로 상태 창의 픽셀이나 Boolean이 아닙니다. 첫 상태 이전과 세계 초기화 후에는 0이지만 실제 좌표 0도 유효합니다. UO.LastStatus()로 기록 존재를 확인하세요.

프로젝트 소스: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 함수 `CharacterStatus`.

#### 2. LastStatusY

ExecuteStealthCompatibility는 bridge serial을 Integer로 반환합니다. LastStatusX/LastStatusY는 IStatusSnapshotBridge를 사용하며, 이 인터페이스가 없는 구형 외부 bridge는 기존 GetX/GetY 조회를 유지합니다.

Integer — 저장된 Y 좌표로 상태 창의 픽셀이나 Boolean이 아닙니다. 첫 상태 이전과 세계 초기화 후에는 0이지만 실제 좌표 0도 유효합니다. UO.LastStatus()로 기록 존재를 확인하세요.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `LastStatusY`.

#### 3. Invoke

Invoke는 스크립트 취소를 고려하며 게임 스레드에서 World를 읽습니다. 네트워크 응답을 기다리거나 상태를 변경하지 않습니다.

매개변수가 없습니다. 읽기는 패킷을 보내거나 창을 열거나 응답을 기다리지 않습니다. UO.GetStatus(id), RequestStats, UpdateObject는 데이터를 요청하며 요청 전송 자체는 LastStatus를 바꾸지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 4. Clear

Clear는 실행 중인 스크립트를 유지하는 경우에도 serial과 두 좌표를 0으로 초기화합니다.

X/Y는 수신 당시 Entity 좌표이며 현재 위치가 아닙니다. mobile은 세계 칸이지만 컨테이너 안의 아이템은 내용물 좌표일 수 있습니다. 상태 패킷 자체에는 X/Y가 없습니다. 나중의 이동/삭제는 저장값을 바꾸지 않으며 World.Clear가 초기화합니다. 존재하는 객체의 현재 위치는 GetX/GetY로 읽습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Clear`.

별도 호출은 원자적 스냅샷이 아니며 호출 사이에 갱신될 수 있습니다. serial이 같아도 내 요청에 대한 새 응답임을 증명하지 않습니다. 괄호 없는 laststatus는 동적 내장 값이지만 같은 이름의 변수로 가릴 수 있습니다. UO.LastStatus()는 등록된 함수입니다.


## 예제

### 마지막 값 읽기

```vb
# 마지막 값 읽기
#
# 마지막으로 상태를 수락한 객체의 저장된 Y 좌표를 반환합니다.
#
# Integer — 저장된 Y 좌표로 상태 창의 픽셀이나 Boolean이 아닙니다. 첫 상태 이전과 세계 초기화 후에는 0이지만 실제 좌표 0도 유효합니다.
# UO.LastStatus()로 기록 존재를 확인하세요.

SUB Main()
    # 한 번만 읽습니다. HEX는 serial을 16진수로, CStr은 좌표를 숫자로 표시합니다. 객체를 선택하지 않습니다.

    VAR value = UO.LastStatusY()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- 한 번만 읽습니다. HEX는 serial을 16진수로, CStr은 좌표를 숫자로 표시합니다. 객체를 선택하지 않습니다.

### 상태 요청 후 알려진 데이터 읽기

```vb
# 상태 요청 후 알려진 데이터 읽기
#
# 마지막으로 상태를 수락한 객체의 저장된 Y 좌표를 반환합니다.
#
# Integer — 저장된 Y 좌표로 상태 창의 픽셀이나 Boolean이 아닙니다. 첫 상태 이전과 세계 초기화 후에는 0이지만 실제 좌표 0도 유효합니다.
# UO.LastStatus()로 기록 존재를 확인하세요.

SUB Main()
    # subject는 self의 serial입니다. 500은 예시 대기 밀리초이며 응답 보장이 아닙니다. 표시된 기록은 오래되었거나 다른 객체의 것일 수 있습니다.

    VAR subject = UO.Self()
    IF subject <> 0 THEN
        UO.GetStatus(subject)
        WAIT(500)
        VAR value = UO.LastStatusY()
        UO.Print('Known value: ' + CStr(value))
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- subject는 self의 serial입니다. 500은 예시 대기 밀리초이며 응답 보장이 아닙니다. 표시된 기록은 오래되었거나 다른 객체의 것일 수 있습니다.

### 완전한 ReadSavedStatus 보조 함수

```vb
# 완전한 ReadSavedStatus 보조 함수
#
# 마지막으로 상태를 수락한 객체의 저장된 Y 좌표를 반환합니다.
#
# Integer — 저장된 Y 좌표로 상태 창의 픽셀이나 Boolean이 아닙니다. 첫 상태 이전과 세계 초기화 후에는 0이지만 실제 좌표 0도 유효합니다.
# UO.LastStatus()로 기록 존재를 확인하세요.

SUB Main()
    # expectedId는 Main에 저장한 serial입니다. 보조 함수를 아래에 완전히 정의했습니다. -1은 선택된 기록이 바뀌었다는 뜻으로 API 자체의 반환 코드가
    # 아닙니다. 전후 확인은 객체 혼합을 줄이지만 같은 serial 갱신 시 원자성을 보장하지 못합니다.

    VAR expectedId = UO.LastStatus()
    IF expectedId <> 0 THEN
        VAR value = ReadSavedStatus(expectedId)
        UO.Print('Checked value: ' + CStr(value))
    END IF
END SUB

SUB ReadSavedStatus(expectedId)
    IF expectedId = 0 OR UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    VAR value = UO.LastStatusY()
    IF UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**매개변수 및 실행 설명:**

- expectedId는 Main에 저장한 serial입니다. 보조 함수를 아래에 완전히 정의했습니다. -1은 선택된 기록이 바뀌었다는 뜻으로 API 자체의 반환 코드가 아닙니다. 전후 확인은 객체 혼합을 줄이지만 같은 serial 갱신 시 원자성을 보장하지 못합니다.
