# UO.LastTargetY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

마지막 대상 선택 때 저장한 Y를 읽습니다.

## 정확한 구문

```text
UO.LastTargetY() -> Integer
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer — 저장된 Y 좌표로 픽셀이나 Boolean이 아닙니다. 선택 전/Clear 후 또는 알 수 없는 객체는 0이며 실제 좌표 0도 유효합니다. LastTarget()=0인 지면/정적 대상도 지원합니다.

## 동작

- 매개변수, 커서 열기, 대상 선택, 공격, 패킷 전송이 없습니다. LastAttack 및 LastStatus와 다릅니다. 일반 self 선택은 대상을 교체하지 않지만 명시적 ClientMarkChar는 바꿀 수 있습니다.
- SetEntity는 알려진 Entity.X/Y를 저장하며 컨테이너 내부 좌표일 수도 있습니다. SetLand/SetStatic는 세계 칸을 저장합니다. 이후 이동/삭제로 바뀌지 않습니다. 현재 위치는 GetX/GetY(serial)로 읽습니다.
- Clear와 World.Clear는 스크립트를 유지해도 초기화합니다. 알 수 없는 serial을 명시하면 이전 좌표를 잇지 않고 X/Y=0이 됩니다. 서버에서의 존재를 보장하지 않습니다.
- 별도 읽기는 원자적이지 않습니다. 객체 대상의 LastTile는 프로토콜 X/Y=65535를 유지합니다. 지면/정적 대상은 LastTile(1)/(2)로 X/Y를 읽습니다. 괄호 없는 lasttarget는 동적 내장 값이지만 변수로 가릴 수 있습니다.
- World.Clear는 ClearWorldState를 호출해 활성 커서/callback, 저장 대상, 반복 패킷을 지웁니다. 일반 Reset은 기록을 유지합니다. 네이티브 TargetLast는 서버 커서가 활성일 때만 저장 패킷을 보냅니다. 기록이 없거나 로컬 callback이면 전송 없이 커서를 유지합니다. 활성 클라이언트 callback은 취소를 뜻하는 null을 한 번 받아 ClientTargetResponsePresent가 1이 되고 응답은 비어 있습니다. 완료된 선택에는 다시 알리지 않습니다.

### 내부 함수: 호출부터 결과까지

실제 C# 내부 단계입니다. ReadTargetValue는 예제에 완전하게 정의된 보조 함수이며 숨겨진 내장 명령이 아닙니다.

#### 1. SetEntity

SetEntity는 World.Get으로 serial과 X/Y를 저장합니다. 없거나 파괴된 Entity는 X/Y=0이며 프로토콜의 특수값은 유지합니다.

SetEntity는 알려진 Entity.X/Y를 저장하며 컨테이너 내부 좌표일 수도 있습니다. SetLand/SetStatic는 세계 칸을 저장합니다. 이후 이동/삭제로 바뀌지 않습니다. 현재 위치는 GetX/GetY(serial)로 읽습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 함수 `SetEntity`.

#### 2. SetLand

SetLand/SetStatic는 serial 0과 X/Y/Z를 저장합니다. SavedX/SavedY는 전송 필드와 분리됩니다.

Integer — 저장된 Y 좌표로 픽셀이나 Boolean이 아닙니다. 선택 전/Clear 후 또는 알 수 없는 객체는 0이며 실제 좌표 0도 유효합니다. LastTarget()=0인 지면/정적 대상도 지원합니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 함수 `SetLand`.

#### 3. SetStatic

SetLand/SetStatic는 serial 0과 X/Y/Z를 저장합니다. SavedX/SavedY는 전송 필드와 분리됩니다.

Integer — 저장된 Y 좌표로 픽셀이나 Boolean이 아닙니다. 선택 전/Clear 후 또는 알 수 없는 객체는 0이며 실제 좌표 0도 유효합니다. LastTarget()=0인 지면/정적 대상도 지원합니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 함수 `SetStatic`.

#### 4. LastTargetY

LastTargetX/LastTargetY는 ITargetSnapshotBridge를 읽으며 구형 외부 bridge는 GetX/GetY를 유지합니다. Invoke는 취소를 지원하며 게임 스레드에서 읽습니다.

Integer — 저장된 Y 좌표로 픽셀이나 Boolean이 아닙니다. 선택 전/Clear 후 또는 알 수 없는 객체는 0이며 실제 좌표 0도 유효합니다. LastTarget()=0인 지면/정적 대상도 지원합니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `LastTargetY`.

#### 5. Invoke

LastTargetX/LastTargetY는 ITargetSnapshotBridge를 읽으며 구형 외부 bridge는 GetX/GetY를 유지합니다. Invoke는 취소를 지원하며 게임 스레드에서 읽습니다.

매개변수, 커서 열기, 대상 선택, 공격, 패킷 전송이 없습니다. LastAttack 및 LastStatus와 다릅니다. 일반 self 선택은 대상을 교체하지 않지만 명시적 ClientMarkChar는 바꿀 수 있습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 6. Clear

Clear는 serial과 저장 좌표를 지우며 World.Clear가 청소 시 호출합니다.

Clear와 World.Clear는 스크립트를 유지해도 초기화합니다. 알 수 없는 serial을 명시하면 이전 좌표를 잇지 않고 X/Y=0이 됩니다. 서버에서의 존재를 보장하지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 함수 `Clear`.

#### 7. ClearWorldState

World.Clear는 ClearWorldState를 호출해 활성 커서/callback, 저장 대상, 반복 패킷을 지웁니다. 일반 Reset은 기록을 유지합니다. 네이티브 TargetLast는 서버 커서가 활성일 때만 저장 패킷을 보냅니다. 기록이 없거나 로컬 callback이면 전송 없이 커서를 유지합니다. 활성 클라이언트 callback은 취소를 뜻하는 null을 한 번 받아 ClientTargetResponsePresent가 1이 되고 응답은 비어 있습니다. 완료된 선택에는 다시 알리지 않습니다.

World.Clear는 ClearWorldState를 호출해 활성 커서/callback, 저장 대상, 반복 패킷을 지웁니다. 일반 Reset은 기록을 유지합니다. 네이티브 TargetLast는 서버 커서가 활성일 때만 저장 패킷을 보냅니다. 기록이 없거나 로컬 callback이면 전송 없이 커서를 유지합니다. 활성 클라이언트 callback은 취소를 뜻하는 null을 한 번 받아 ClientTargetResponsePresent가 1이 되고 응답은 비어 있습니다. 완료된 선택에는 다시 알리지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 함수 `ClearWorldState`.

#### 8. TargetLast

World.Clear는 ClearWorldState를 호출해 활성 커서/callback, 저장 대상, 반복 패킷을 지웁니다. 일반 Reset은 기록을 유지합니다. 네이티브 TargetLast는 서버 커서가 활성일 때만 저장 패킷을 보냅니다. 기록이 없거나 로컬 callback이면 전송 없이 커서를 유지합니다. 활성 클라이언트 callback은 취소를 뜻하는 null을 한 번 받아 ClientTargetResponsePresent가 1이 되고 응답은 비어 있습니다. 완료된 선택에는 다시 알리지 않습니다.

World.Clear는 ClearWorldState를 호출해 활성 커서/callback, 저장 대상, 반복 패킷을 지웁니다. 일반 Reset은 기록을 유지합니다. 네이티브 TargetLast는 서버 커서가 활성일 때만 저장 패킷을 보냅니다. 기록이 없거나 로컬 callback이면 전송 없이 커서를 유지합니다. 활성 클라이언트 callback은 취소를 뜻하는 null을 한 번 받아 ClientTargetResponsePresent가 1이 되고 응답은 비어 있습니다. 완료된 선택에는 다시 알리지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 함수 `TargetLast`.

별도 읽기는 원자적이지 않습니다. 객체 대상의 LastTile는 프로토콜 X/Y=65535를 유지합니다. 지면/정적 대상은 LastTile(1)/(2)로 X/Y를 읽습니다. 괄호 없는 lasttarget는 동적 내장 값이지만 변수로 가릴 수 있습니다.


## 예제

### 저장값 읽기

```vb
# 저장값 읽기
#
# 마지막 대상 선택 때 저장한 Y를 읽습니다.
#
# Integer — 저장된 Y 좌표로 픽셀이나 Boolean이 아닙니다. 선택 전/Clear 후 또는 알 수 없는 객체는 0이며 실제 좌표 0도 유효합니다.
# LastTarget()=0인 지면/정적 대상도 지원합니다.

SUB Main()
    # value가 반환값입니다. HEX는 ID를, CStr은 좌표를 표시합니다. 선택하지 않습니다.

    VAR value = UO.LastTargetY()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- value가 반환값입니다. HEX는 ID를, CStr은 좌표를 표시합니다. 선택하지 않습니다.

### 저장 위치와 현재 위치 비교

```vb
# 저장 위치와 현재 위치 비교
#
# 마지막 대상 선택 때 저장한 Y를 읽습니다.
#
# Integer — 저장된 Y 좌표로 픽셀이나 Boolean이 아닙니다. 선택 전/Clear 후 또는 알 수 없는 객체는 0이며 실제 좌표 0도 유효합니다.
# LastTarget()=0인 지면/정적 대상도 지원합니다.

SUB Main()
    # id는 저장된 serial입니다. GetX/GetY 전에 Exists로 확인합니다. 위치는 다를 수 있으며 ID=0은 점을 선택했다는 증거가 아닙니다.

    VAR id = UO.LastTarget()
    VAR x = UO.LastTargetX()
    VAR y = UO.LastTargetY()
    UO.Print('Saved XY: ' + CStr(x) + ',' + CStr(y))
    IF id <> 0 AND UO.Exists(id) THEN
        UO.Print('Live XY: ' + CStr(UO.GetX(id)) + ',' + CStr(UO.GetY(id)))
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- id는 저장된 serial입니다. GetX/GetY 전에 Exists로 확인합니다. 위치는 다를 수 있으며 ID=0은 점을 선택했다는 증거가 아닙니다.

### 완전한 ReadTargetValue 보조 함수

```vb
# 완전한 ReadTargetValue 보조 함수
#
# 마지막 대상 선택 때 저장한 Y를 읽습니다.
#
# Integer — 저장된 Y 좌표로 픽셀이나 Boolean이 아닙니다. 선택 전/Clear 후 또는 알 수 없는 객체는 0이며 실제 좌표 0도 유효합니다.
# LastTarget()=0인 지면/정적 대상도 지원합니다.

SUB Main()
    # minimum/maximum은 보조 함수의 범위 설정이며 API 매개변수가 아닙니다. -1은 보조 함수 자체의 범위 초과 신호입니다. ID 버전은 최상위 비트를 포함한
    # 0이 아닌 serial을 보존합니다.

    VAR value = ReadTargetValue(0,65535)
    UO.Print('Checked value: ' + CStr(value))
END SUB

SUB ReadTargetValue(minimum,maximum)
    VAR value = UO.LastTargetY()
    IF value < minimum OR value > maximum THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**매개변수 및 실행 설명:**

- minimum/maximum은 보조 함수의 범위 설정이며 API 매개변수가 아닙니다. -1은 보조 함수 자체의 범위 초과 신호입니다. ID 버전은 최상위 비트를 포함한 0이 아닌 serial을 보존합니다.
