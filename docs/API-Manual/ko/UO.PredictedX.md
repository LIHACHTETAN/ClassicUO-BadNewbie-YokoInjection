# UO.PredictedX

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

현재 플레이어의 대기열에 들어 있는 이동 단계 이후 예상되는 X 좌표 값을 읽습니다.

## 정확한 구문

```text
UO.PredictedX() -> Integer
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer X, 지도 칸 단위입니다. 0은 유효한 좌표이거나 플레이어가 없다는 뜻입니다.

## 동작

- 구문에 표시된 인수 없는 UO 함수만 지원합니다. target, serial, type, 목적지, 거리, timeout 인수가 없습니다. 숫자이며 Boolean, ID, tile 레코드가 아닙니다. 1은 도착을 의미하지 않습니다.
- GetEndPosition은 대기열의 마지막 Mobile.Step에서 X/Y/Z/방향을 읽습니다. 대기열이 비면 현재 위치와 방향을 읽습니다. O(1) 읽기이며 단계를 제거하거나 이동, 패킷 전송, 경로 계산, 도착 대기를 하지 않습니다.
- X/Y는 월드/지도 좌표이며 컨테이너 gump의 픽셀이 아닙니다. Z는 높이이며 층수가 아닙니다. 한 성분만 반환하고 배열이나 전체 경로의 최종 목적지는 반환하지 않습니다.
- 로컬 예측이며 도착 확인이 아닙니다. 단계 추가/완료/거절, 대기열 초기화, 순간이동으로 바뀔 수 있습니다. 개별 성분 호출은 원자적 스냅샷이 아닙니다. X만 같다고 Y/Z 일치나 서버 승인이 보장되지 않습니다.
- Invoke는 게임 스레드에서 읽습니다. 작업 스레드는 관리자의 처리를 기다리며 스크립트 취소가 대기를 중단합니다. 추가 지연이나 네트워크 요청은 없습니다.
- IPredictedMovementBridge가 없는 외부 IApiBridge는 현재 좌표/방향으로의 대체 동작을 유지합니다. Classic UO는 대기열을 읽는 인터페이스를 구현합니다.

### 내부 함수: 호출부터 결과까지

실제 네이티브 읽기 단계입니다. PredictionEquals는 전체 정의가 있는 사용자 BASIC 보조 함수이며 내부 명령이나 이동 프로시저가 아닙니다.

#### 1. ExecuteStealthCompatibility

네이티브 함수가 ReadPredictedCoordinate를 호출하여 IPredictedMovementBridge 속성을 선택합니다. NewMoveXY나 경로 탐색을 시작하지 않습니다.

구문에 표시된 인수 없는 UO 함수만 지원합니다. target, serial, type, 목적지, 거리, timeout 인수가 없습니다. 숫자이며 Boolean, ID, tile 레코드가 아닙니다. 1은 도착을 의미하지 않습니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ExecuteStealthCompatibility`.

#### 2. ReadPredictedCoordinate

네이티브 함수가 ReadPredictedCoordinate를 호출하여 IPredictedMovementBridge 속성을 선택합니다. NewMoveXY나 경로 탐색을 시작하지 않습니다.

IPredictedMovementBridge가 없는 외부 IApiBridge는 현재 좌표/방향으로의 대체 동작을 유지합니다. Classic UO는 대기열을 읽는 인터페이스를 구현합니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ReadPredictedCoordinate`.

#### 3. Invoke

Invoke는 게임 스레드에서 읽습니다. 작업 스레드는 관리자의 처리를 기다리며 스크립트 취소가 대기를 중단합니다. 추가 지연이나 네트워크 요청은 없습니다.

Integer X, 지도 칸 단위입니다. 0은 유효한 좌표이거나 플레이어가 없다는 뜻입니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 4. ReadPredictedPosition

Player가 없거나 파괴되었으면 ReadPredictedPosition은 0을 반환합니다. 아니면 GetEndPosition을 호출하고 한 성분을 선택합니다.

GetEndPosition은 대기열의 마지막 Mobile.Step에서 X/Y/Z/방향을 읽습니다. 대기열이 비면 현재 위치와 방향을 읽습니다. O(1) 읽기이며 단계를 제거하거나 이동, 패킷 전송, 경로 계산, 도착 대기를 하지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `ReadPredictedPosition`.

#### 5. GetEndPosition

GetEndPosition은 대기열의 마지막 Mobile.Step에서 X/Y/Z/방향을 읽습니다. 대기열이 비면 현재 위치와 방향을 읽습니다. O(1) 읽기이며 단계를 제거하거나 이동, 패킷 전송, 경로 계산, 도착 대기를 하지 않습니다.

X/Y는 월드/지도 좌표이며 컨테이너 gump의 픽셀이 아닙니다. Z는 높이이며 층수가 아닙니다. 한 성분만 반환하고 배열이나 전체 경로의 최종 목적지는 반환하지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/GameObjects/Mobile.cs`; 함수 `GetEndPosition`.

#### 6. InjectionValue

Integer X, 지도 칸 단위입니다. 0은 유효한 좌표이거나 플레이어가 없다는 뜻입니다.

로컬 예측이며 도착 확인이 아닙니다. 단계 추가/완료/거절, 대기열 초기화, 순간이동으로 바뀔 수 있습니다. 개별 성분 호출은 원자적 스냅샷이 아닙니다. X만 같다고 Y/Z 일치나 서버 승인이 보장되지 않습니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs`; 함수 `InjectionValue`.

PredictionEquals(expected)는 숫자 좌표/높이/방향을 받아 플레이어가 없으면 거절하고 한 예측 성분을 비교합니다. Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 도착을 기다리거나 보장하지 않습니다.


## 예제

### 한 성분 읽기

```vb
# 한 성분 읽기
#
# 현재 플레이어의 대기열에 들어 있는 이동 단계 이후 예상되는 X 좌표 값을 읽습니다.
#
# Integer X, 지도 칸 단위입니다. 0은 유효한 좌표이거나 플레이어가 없다는 뜻입니다.

SUB Main()
    # predicted는 인수 없는 호출 한 번을 저장합니다. CStr는 저널 표시용 숫자 형식을 만듭니다.

    VAR predicted = UO.PredictedX()
    UO.Print('Predicted: ' + CStr(predicted))
END SUB
```

**매개변수 및 실행 설명:**

- predicted는 인수 없는 호출 한 번을 저장합니다. CStr는 저널 표시용 숫자 형식을 만듭니다.

### 예측 변화 관찰

```vb
# 예측 변화 관찰
#
# 현재 플레이어의 대기열에 들어 있는 이동 단계 이후 예상되는 X 좌표 값을 읽습니다.
#
# Integer X, 지도 칸 단위입니다. 0은 유효한 좌표이거나 플레이어가 없다는 뜻입니다.

SUB Main()
    # WAIT(100)은 이 예제를 100밀리초 멈춥니다. 중간에 이동했어도 before/after가 같을 수 있습니다. 읽기 자체는 이동을 시작하지 않습니다.

    VAR before = UO.PredictedX()
    WAIT(100)
    VAR after = UO.PredictedX()
    IF before <> after THEN
        UO.Print('Prediction changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- WAIT(100)은 이 예제를 100밀리초 멈춥니다. 중간에 이동했어도 before/after가 같을 수 있습니다. 읽기 자체는 이동을 시작하지 않습니다.

### 완전한 비교 보조 함수

```vb
# 완전한 비교 보조 함수
#
# 현재 플레이어의 대기열에 들어 있는 이동 단계 이후 예상되는 X 좌표 값을 읽습니다.
#
# Integer X, 지도 칸 단위입니다. 0은 유효한 좌표이거나 플레이어가 없다는 뜻입니다.

SUB Main()
    # expected는 예제의 좌표/높이/방향이며 네이티브 명령의 인수가 아닙니다. PredictionEquals는 UO.Self()를 확인하고 한 번 읽어 같으면
    # 1=TRUE, 아니면 0=FALSE를 반환합니다. Main 아래에 전체 정의가 있습니다. 한 성분의 일치는 도착이 아닙니다.

    IF PredictionEquals(1445) = TRUE THEN
        UO.Print('Queued endpoint matches this component')
    ELSE
        UO.Print('Different component or no player')
    END IF
END SUB

SUB PredictionEquals(expected)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR predicted = UO.PredictedX()
    RETURN predicted = expected
END SUB
```

**매개변수 및 실행 설명:**

- expected는 예제의 좌표/높이/방향이며 네이티브 명령의 인수가 아닙니다. PredictionEquals는 UO.Self()를 확인하고 한 번 읽어 같으면 1=TRUE, 아니면 0=FALSE를 반환합니다. Main 아래에 전체 정의가 있습니다. 한 성분의 일치는 도착이 아닙니다.
