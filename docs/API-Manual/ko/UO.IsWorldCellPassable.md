# UO.IsWorldCellPassable

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

인접한 월드 칸으로 한 걸음 이동 가능한지 검사하고 통과 여부와 높이를 반환합니다.

## 정확한 구문

```text
UO.IsWorldCellPassable(CurrX:Any, CurrY:Any, CurrZ:Any, DestX:Any, DestY:Any, DestZ:Any, WorldNum:Any) -> Array
```

## 매개변수

- `CurrX` — 필수 시작 칸 월드 좌표 X: 로드된 지도 범위의 정수 0..65535이며 gump 좌표가 아닙니다.
- `CurrY` — 필수 시작 칸 월드 좌표 Y: 로드된 지도 범위의 정수 0..65535이며 gump 좌표가 아닙니다.
- `CurrZ` — 필수 시작 높이 −128..127이며 층 번호가 아닙니다. 잘못된 높이는 제한값으로 자르지 않고 거부합니다.
- `DestX` — 필수 목적지 칸 월드 좌표 X: 로드된 지도 범위의 정수 0..65535이며 gump 좌표가 아닙니다.
- `DestY` — 필수 목적지 칸 월드 좌표 Y: 로드된 지도 범위의 정수 0..65535이며 gump 좌표가 아닙니다.
- `DestZ` — 필수 예비 입력 Z이며 보통 CurrZ입니다. var가 아니므로 변수가 바뀌지 않고 원하는 층도 지정하지 않습니다. 계산된 높이는 result[1]에서 읽습니다. 이 bridge는 항상 자체 높이를 제공하며 인수는 Pascal 형식을 유지합니다.
- `WorldNum` — 필수 지도 번호: UO.WorldNum(). 크기가 알려진 현재 지도만 검사하고 다른 지도를 로드하지 않습니다.

## 반환값

Integer 두 개의 Array: [0] — 통과 여부, 1 = TRUE, 0 = FALSE; [1] — 계산된 Z. 첫 요소만 논리값이며 배열 자체를 TRUE와 비교하면 안 됩니다. 0/음수 높이도 유효하고 [0]=0일 때 높이는 도달 가능성을 증명하지 않습니다. 인수 거부 시 [0, CurrZ]입니다.

## 동작

- 이동, 문 열기, 타깃 지정, 패킷 전송을 하지 않습니다. 기존 로컬 지형을 읽으며 서버는 나중의 걸음을 거부할 수 있습니다. 각 조회는 별개 스냅샷입니다.
- 인접 칸은 X/Y 차이가 각각 1 이하입니다. 먼 목적지, 지도 밖, 캐릭터/지도 부재 또는 IsDestroyed는 충돌 계산 전에 거부합니다. 전체 경로는 GetPathArray나 NewMoveXY를 사용하세요.
- 같고 유효한 X/Y는 걸음이 필요 없어 충돌 검사 없이 [1, CurrZ]를 줍니다. 그 칸에서 나갈 수 있는지 검사하는 것은 아닙니다. 캐릭터 상태와 현재 Pathfinder 규칙이 인접 걸음에 영향을 주며 지형이 로드되지 않았으면 거부할 수 있습니다.

### 내부 함수: 호출부터 결과까지

실제 C# 내부 단계입니다. IsCellOpen는 예제에 완전하게 정의된 보조 함수이며 숨겨진 내장 명령이 아닙니다.

#### 1. ExecuteStealthCompatibility

Integer 인수 일곱 개를 읽습니다. 다른 bridge가 높이를 주지 않을 때만 DestZ를 씁니다. 인수를 바꾸지 않고 배열을 반환합니다.

Integer 두 개의 Array: [0] — 통과 여부, 1 = TRUE, 0 = FALSE; [1] — 계산된 Z. 첫 요소만 논리값이며 배열 자체를 TRUE와 비교하면 안 됩니다. 0/음수 높이도 유효하고 [0]=0일 때 높이는 도달 가능성을 증명하지 않습니다. 인수 거부 시 [0, CurrZ]입니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ExecuteStealthCompatibility`.

#### 2. CheckWorldStep

Invoke는 좌표 뺄셈 전에 캐릭터, 지도, 크기, 좌표, 높이, 인접 여부를 검사하고 방향을 고릅니다. CanWalkForQuery 후 목적지 X/Y와 정확히 일치해야 합니다.

Integer 두 개의 Array: [0] — 통과 여부, 1 = TRUE, 0 = FALSE; [1] — 계산된 Z. 첫 요소만 논리값이며 배열 자체를 TRUE와 비교하면 안 됩니다. 0/음수 높이도 유효하고 [0]=0일 때 높이는 도달 가능성을 증명하지 않습니다. 인수 거부 시 [0, CurrZ]입니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `CheckWorldStep`.

#### 3. CanWalkForQuery

다른 경로의 금지 칸 판정을 잠시 제거했다가 finally에서 복원합니다. 경로를 시작하지 않고 CanWalk를 호출합니다.

이동, 문 열기, 타깃 지정, 패킷 전송을 하지 않습니다. 기존 로컬 지형을 읽으며 서버는 나중의 걸음을 거부할 수 있습니다. 각 조회는 별개 스냅샷입니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Pathfinder.cs`; 함수 `CanWalkForQuery`.

#### 4. CanWalk

주 걸음과 대각선 옆 칸을 검사합니다. bool을 반환하며 승인된 걸음만 ref 좌표를 갱신합니다.

충돌 함수는 로드된 지형과 캐릭터 상태를 읽습니다. 대각선 대신 옆 칸으로 가는 것은 요청한 칸에 도달한 것이 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Pathfinder.cs`; 함수 `CanWalk`.

#### 5. CalculateNewZ

목적지 X/Y, ref 시작 Z, 방향을 받아 캐릭터 상태에 따라 표면과 여유 공간을 고릅니다. bool은 통과 여부, z는 높이입니다.

충돌 함수는 로드된 지형과 캐릭터 상태를 읽습니다. 대각선 대신 옆 칸으로 가는 것은 요청한 칸에 도달한 것이 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Pathfinder.cs`; 함수 `CalculateNewZ`.

#### 6. CalculateMinMaxZ

새 칸, 현재 Z, 방향, 모드를 받습니다. CreateItemList의 시작 지형으로 ref minZ/maxZ를 계산합니다.

충돌 함수는 로드된 지형과 캐릭터 상태를 읽습니다. 대각선 대신 옆 칸으로 가는 것은 요청한 칸에 도달한 것이 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Pathfinder.cs`; 함수 `CalculateMinMaxZ`.

#### 7. CreateItemList

목록, X/Y, 모드를 받아 로드된 객체와 충돌 규칙을 모읍니다. bool은 지형 유무입니다. Map.GetTile은 load=false로 새 블록을 읽지 않습니다.

충돌 함수는 로드된 지형과 캐릭터 상태를 읽습니다. 대각선 대신 옆 칸으로 가는 것은 요청한 칸에 도달한 것이 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Pathfinder.cs`; 함수 `CreateItemList`.

이동, 문 열기, 타깃 지정, 패킷 전송을 하지 않습니다. 기존 로컬 지형을 읽으며 서버는 나중의 걸음을 거부할 수 있습니다. 각 조회는 별개 스냅샷입니다.


## 예제

### 동쪽 칸 검사

```vb
# 동쪽 칸 검사
#
# 인접한 월드 칸으로 한 걸음 이동 가능한지 검사하고 통과 여부와 높이를 반환합니다.
#
# Integer 두 개의 Array: [0] — 통과 여부, 1 = TRUE, 0 = FALSE; [1] — 계산된 Z. 첫 요소만 논리값이며 배열 자체를 TRUE와
# 비교하면 안 됩니다. 0/음수 높이도 유효하고 [0]=0일 때 높이는 도달 가능성을 증명하지 않습니다. 인수 거부 시 [0, CurrZ]입니다.

SUB Main()
    # x/y/z는 시작, x+1/y는 이웃, 여섯 번째 인수는 예비 Z, 마지막은 현재 지도입니다. result[1]을 쓰기 전에 result[0]을 검사합니다.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR result = UO.IsWorldCellPassable(x,y,z,x+1,y,z,UO.WorldNum())
    IF result[0] = TRUE THEN
        UO.Print('Passable, Z=' + CStr(result[1]))
    ELSE
        UO.Print('Blocked')
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- x/y/z는 시작, x+1/y는 이웃, 여섯 번째 인수는 예비 Z, 마지막은 현재 지도입니다. result[1]을 쓰기 전에 result[0]을 검사합니다.

### 인수를 바꾸지 않고 Z 읽기

```vb
# 인수를 바꾸지 않고 Z 읽기
#
# 인접한 월드 칸으로 한 걸음 이동 가능한지 검사하고 통과 여부와 높이를 반환합니다.
#
# Integer 두 개의 Array: [0] — 통과 여부, 1 = TRUE, 0 = FALSE; [1] — 계산된 Z. 첫 요소만 논리값이며 배열 자체를 TRUE와
# 비교하면 안 됩니다. 0/음수 높이도 유효하고 [0]=0일 때 높이는 도달 가능성을 증명하지 않습니다. 인수 거부 시 [0, CurrZ]입니다.

SUB Main()
    # proposedZ는 0으로 유지됩니다. targetZ는 인수가 아닌 result[1]에서 읽습니다. 거부 시 높이를 추정하지 않습니다.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR proposedZ = 0
    VAR result = UO.IsWorldCellPassable(x,y,z,x,y+1,proposedZ,UO.WorldNum())
    IF result[0] = 1 THEN
        VAR targetZ = result[1]
        UO.Print('Input=' + CStr(proposedZ) + '; result=' + CStr(targetZ))
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- proposedZ는 0으로 유지됩니다. targetZ는 인수가 아닌 result[1]에서 읽습니다. 거부 시 높이를 추정하지 않습니다.

### 완전한 IsCellOpen 함수

```vb
# 완전한 IsCellOpen 함수
#
# 인접한 월드 칸으로 한 걸음 이동 가능한지 검사하고 통과 여부와 높이를 반환합니다.
#
# Integer 두 개의 Array: [0] — 통과 여부, 1 = TRUE, 0 = FALSE; [1] — 계산된 Z. 첫 요소만 논리값이며 배열 자체를 TRUE와
# 비교하면 안 됩니다. 0/음수 높이도 유효하고 [0]=0일 때 높이는 도달 가능성을 증명하지 않습니다. 인수 거부 시 [0, CurrZ]입니다.

SUB Main()
    # Main 다음의 전체 함수는 시작 X/Y/Z, 목적지 X/Y, 지도를 받고 여섯 번째 인수를 보충합니다. 배열이 아닌 Integer 1/0만 반환하므로
    # IsCellOpen은 TRUE와 비교할 수 있습니다. 캐릭터를 움직이지 않습니다.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR openCell = IsCellOpen(x,y,UO.GetZ(),x+1,y+1,UO.WorldNum())
    IF openCell = TRUE THEN
        UO.Print('Diagonal cell is locally passable')
    END IF
END SUB

SUB IsCellOpen(x,y,z,toX,toY,map)
    VAR cellResult = UO.IsWorldCellPassable(x,y,z,toX,toY,z,map)
    IF GetArrayLength(cellResult) <> 2 THEN
        RETURN 0
    END IF
    RETURN cellResult[0]
END SUB
```

**매개변수 및 실행 설명:**

- Main 다음의 전체 함수는 시작 X/Y/Z, 목적지 X/Y, 지도를 받고 여섯 번째 인수를 보충합니다. 배열이 아닌 Integer 1/0만 반환하므로 IsCellOpen은 TRUE와 비교할 수 있습니다. 캐릭터를 움직이지 않습니다.
