# UO.GetStaticTilesArrayEx

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

직사각형 안의 Static/Multi/Item 레코드를 graphic/type으로 검색합니다.

## 정확한 구문

```text
UO.GetStaticTilesArrayEx(Xmin:Any, Ymin:Any, Xmax:Any, Ymax:Any, WorldNum:Any, TileTypes:Any) -> Any
```

## 매개변수

- `Xmin` — 두 모서리의 월드 좌표이며 경계를 포함합니다. 범위 0..65535, 모서리 순서는 자동으로 정리됩니다. 최대 1,000,000칸이며 잘못된 경계는 지도 읽기 전에 스크립트 오류를 냅니다.
- `Ymin` — 두 모서리의 월드 좌표이며 경계를 포함합니다. 범위 0..65535, 모서리 순서는 자동으로 정리됩니다. 최대 1,000,000칸이며 잘못된 경계는 지도 읽기 전에 스크립트 오류를 냅니다.
- `Xmax` — 두 모서리의 월드 좌표이며 경계를 포함합니다. 범위 0..65535, 모서리 순서는 자동으로 정리됩니다. 최대 1,000,000칸이며 잘못된 경계는 지도 읽기 전에 스크립트 오류를 냅니다.
- `Ymax` — 두 모서리의 월드 좌표이며 경계를 포함합니다. 범위 0..65535, 모서리 순서는 자동으로 정리됩니다. 최대 1,000,000칸이며 잘못된 경계는 지도 읽기 전에 스크립트 오류를 냅니다.
- `WorldNum` — 지도/패싯 번호 0..255. UO.WorldNum()을 사용합니다. 다른 지도이면 빈 Array를 반환하며 처리 구간 사이에 지도가 바뀌면 부분 결과를 버립니다.
- `TileTypes` — 숫자 graphic/type의 Array입니다. 타입을 반복해도 레코드는 중복 추가되지 않습니다. 숫자 하나도 단일 타입으로 허용합니다. 빈 Array는 모든 타입, 0 하나만 담은 배열은 타입 0만 찾습니다.

## 반환값

각 레코드가 [graphic, X, Y, Z, hue]인 Array이며 모든 필드는 Integer입니다. Z는 바닥 높이, hue는 색상입니다. 같은 칸의 여러 레코드는 따로 유지됩니다. 일치 항목이 없으면 빈 Array입니다. 개수는 GetArrayLength(result)로 읽습니다. 인덱스는 0부터 시작합니다. Boolean, serial, Pascal record가 아니며 일곱 번째 출력 인수도 없습니다.

## 동작

- 로컬 자료만 읽으며 FindItem/FindCount를 바꾸거나 이동, target, 서버 명령 전송을 하지 않습니다.
- X 오름차순, 각 X 안에서 Y 오름차순입니다. 같은 칸의 레코드는 bridge 순서를 유지하며 거리나 높이로 정렬하지 않습니다.
- 한 구간에서 최대 32칸을 처리하며 약 1ms의 유연한 시간 예산을 사용합니다. 구간 사이에 취소를 확인합니다. 복잡한 칸이나 처음 읽는 자료는 더 오래 걸릴 수 있습니다. 큰 영역은 나누세요. 읽는 동안 월드가 바뀔 수 있습니다.
- 현재 static 분기는 Static, Multi, Item과 로드된 지상 아이템을 포함하지만 Land와 Mobile은 제외합니다. 파일의 정적 타일만 읽는 것보다 범위가 넓습니다.

### 내부 함수: 호출부터 결과까지

실제 C# 처리 단계이며 추가 UO 명령이 아닙니다. 예제에 보조 프로시저 전체가 포함되어 있습니다.

#### 1. ExecuteStealthCompatibility

인수 여섯 개를 받습니다. 일반 형식은 타입 하나를 전달하고 Ex는 Array 또는 숫자를 타입 목록으로 바꿉니다.

land/static 모드로 FindPortableTiles를 호출하고 레코드 Array를 직접 반환합니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ExecuteStealthCompatibility`.

#### 2. FindPortableTiles

64비트 연산으로 좌표, 지도, 면적을 검증하고 모서리를 정리한 뒤 타입 HashSet을 만듭니다.

X/Y 커서를 보관하고 ExecutePathQuerySlice로 ScanSlice를 실행합니다. 구간 사이의 Wait(0)이 취소를 확인하며 지도 변경 시 빈 Array를 반환합니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `FindPortableTiles`.

#### 3. ScanSlice

게임 스레드에서 최대 32칸을 처리하며 각 칸 뒤에 커서를 저장합니다.

GetLandscapeTile은 graphic/Z/flags, GetStaticTiles는 graphic/Z/hue 세 값 묶음을 제공합니다. 일치 레코드를 추가하고 구간 사이에 제어를 돌려줍니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ScanSlice`.

#### 4. GetChunk2

블록 좌표와 로드 옵션을 받고 선형 인덱스를 만들기 전에 두 축을 검증합니다.

Chunk 또는 null을 반환합니다. 지도 밖 Y를 이웃 열로 바꾸지 않습니다. 로드된 블록을 재사용하고 필요할 때 새 블록을 읽습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Map/Map.cs`; 함수 `GetChunk2`.

로컬 자료만 읽으며 FindItem/FindCount를 바꾸거나 이동, target, 서버 명령 전송을 하지 않습니다.


## 예제

### 캐릭터 주변 검색

```vb
# 캐릭터 주변 검색
#
# 직사각형 안의 Static/Multi/Item 레코드를 graphic/type으로 검색합니다.
#
# 각 레코드가 [graphic, X, Y, Z, hue]인 Array이며 모든 필드는 Integer입니다. Z는 바닥 높이, hue는 색상입니다. 같은 칸의 여러 레코드는
# 따로 유지됩니다. 일치 항목이 없으면 빈 Array입니다. 개수는 GetArrayLength(result)로 읽습니다. 인덱스는 0부터 시작합니다. Boolean,
# serial, Pascal record가 아니며 일곱 번째 출력 인수도 없습니다.

SUB Main()
    # x/y는 self 좌표, map은 현재 지도입니다. 3×3 영역은 경계를 포함합니다. Ex는 예시 타입 두 개, 일반 형식은 하나를 씁니다. graphic을 자신의
    # 리소스에 맞게 바꾸고 물체 ID와 혼동하지 마세요.

    DIM types[1]
    types[0] = 0x0CCA
    types[1] = 0x0CCB
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetStaticTilesArrayEx(x, y, x + 2, y + 2, map, types)
    UO.Print("Records: " + CStr(GetArrayLength(rows)))
END SUB
```

**매개변수 및 실행 설명:**

- x/y는 self 좌표, map은 현재 지도입니다. 3×3 영역은 경계를 포함합니다. Ex는 예시 타입 두 개, 일반 형식은 하나를 씁니다. graphic을 자신의 리소스에 맞게 바꾸고 물체 ID와 혼동하지 마세요.

### 뒤집힌 모서리와 모든 필드

```vb
# 뒤집힌 모서리와 모든 필드
#
# 직사각형 안의 Static/Multi/Item 레코드를 graphic/type으로 검색합니다.
#
# 각 레코드가 [graphic, X, Y, Z, hue]인 Array이며 모든 필드는 Integer입니다. Z는 바닥 높이, hue는 색상입니다. 같은 칸의 여러 레코드는
# 따로 유지됩니다. 일치 항목이 없으면 빈 Array입니다. 개수는 GetArrayLength(result)로 읽습니다. 인덱스는 0부터 시작합니다. Boolean,
# serial, Pascal record가 아니며 일곱 번째 출력 인수도 없습니다.

SUB Main()
    # 2×2 영역은 큰 모서리에서 작은 모서리 순서로 지정하지만 자동 정리됩니다. row는 레코드 하나입니다. PrintTile은 전체가 정의되어 있으며 숫자만 출력합니다.
    # 지형 예제의 hue=0은 보조 인수의 자리 표시자이며 지형 레코드에는 hue가 없습니다.

    DIM types[1]
    types[0] = 0x0CCA
    types[1] = 0x0CCB
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetStaticTilesArrayEx(x + 1, y + 1, x, y, map, types)
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        PrintTile(row[0], row[1], row[2], row[3], row[4])
        i = i + 1
    WEND
END SUB

SUB PrintTile(graphic, x, y, z, hue)
    UO.Print("Type=" + CStr(graphic) + " X=" + CStr(x) + " Y=" + CStr(y))
    UO.Print("Z=" + CStr(z) + " hue=" + CStr(hue))
END SUB
```

**매개변수 및 실행 설명:**

- 2×2 영역은 큰 모서리에서 작은 모서리 순서로 지정하지만 자동 정리됩니다. row는 레코드 하나입니다. PrintTile은 전체가 정의되어 있으며 숫자만 출력합니다. 지형 예제의 hue=0은 보조 인수의 자리 표시자이며 지형 레코드에는 hue가 없습니다.

### 횟수를 제한한 반복 검색

```vb
# 횟수를 제한한 반복 검색
#
# 직사각형 안의 Static/Multi/Item 레코드를 graphic/type으로 검색합니다.
#
# 각 레코드가 [graphic, X, Y, Z, hue]인 Array이며 모든 필드는 Integer입니다. Z는 바닥 높이, hue는 색상입니다. 같은 칸의 여러 레코드는
# 따로 유지됩니다. 일치 항목이 없으면 빈 Array입니다. 개수는 GetArrayLength(result)로 읽습니다. 인덱스는 0부터 시작합니다. Boolean,
# serial, Pascal record가 아니며 일곱 번째 출력 인수도 없습니다.

SUB Main()
    # 한 칸을 최대 세 번 검색하며 사이에 WAIT(250)을 둡니다. 매 호출은 새 결과를 만듭니다. 길이 0은 현재 일치 항목이 없다는 뜻이지 서버에 영원히 없다는 뜻은
    # 아닙니다.

    DIM types[1]
    types[0] = 0x0CCA
    types[1] = 0x0CCB
    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR attempt = 0
    WHILE attempt < 3
        VAR rows = UO.GetStaticTilesArrayEx(x, y, x, y, map, types)
        UO.Print("Records: " + CStr(GetArrayLength(rows)))
        attempt = attempt + 1
        WAIT(250)
    WEND
END SUB
```

**매개변수 및 실행 설명:**

- 한 칸을 최대 세 번 검색하며 사이에 WAIT(250)을 둡니다. 매 호출은 새 결과를 만듭니다. 길이 0은 현재 일치 항목이 없다는 뜻이지 서버에 영원히 없다는 뜻은 아닙니다.
