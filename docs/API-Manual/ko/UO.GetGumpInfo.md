# UO.GetGumpInfo

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

서버 검프와 해당 컨트롤의 일관된 스냅샷을 읽습니다.

## 정확한 구문

```text
UO.GetGumpInfo(GumpIndex:Any) -> Array
```

## 매개변수

- `GumpIndex` — 필수 Integer: 0부터 GetGumpsCount()-1까지의 인덱스입니다. serial이나 GumpID가 아닙니다. 음수와 범위 밖 인덱스는 유효하지 않습니다. 창을 열거나 닫거나 순서를 바꾸면 인덱스가 달라집니다.

## 반환값

Array — 5개 필드의 Array: [0] Integer serial, [1] Integer GumpID, [2] 공백만 있는 문자열을 제외한 텍스트 Array<String>, [3] 일반 버튼 설명 Array<String>, [4] 중첩된 항목을 포함한 모든 유효 컨트롤 설명 Array<String>. 잘못되거나 닫혔거나 무시된 검프는 []를 반환합니다. 최상위 비트가 설정된 ID는 음수 Integer입니다. Hex로 비트 표현을 표시합니다.

## 동작

- 게임 스레드에 한 번 요청하여 전체 스냅샷을 복사합니다. 이후 변경하거나 창을 닫아도 저장된 배열은 변하지 않습니다. 활성 서버 검프만 포함하며 로컬 배낭, 지도, 설정 창은 제외합니다.
- 이 BASIC 배열은 Pascal TGumpInfo 레코드나 원본 레이아웃 패킷이 아닙니다. 설명에는 종류, page, ID, X/Y, 크기가 포함됩니다. 버튼에는 ButtonID, action, toPage와 이미지가, 선택 요소에는 checked와 inactive/active가 추가됩니다. 텍스트에는 공백과 =가 포함될 수 있습니다. 라디오 버튼은 [4]에 속하며 [3]에는 없습니다.
- AddGumpIgnoreByID/BySerial은 현재 스크립트에서 이 읽기 결과를 숨기고 ClearGumpsIgnore는 필터를 해제합니다. GetGumpsCount는 변하지 않습니다. 검프가 존재해도 텍스트 배열은 비어 있을 수 있습니다. 배열 길이는 Len이 아닌 GetArrayLength로 읽습니다.

## 예제

### 두 ID 읽기

```vb
# 두 ID 읽기
#
# 서버 검프와 해당 컨트롤의 일관된 스냅샷을 읽습니다.
#
# Array — 5개 필드의 Array: [0] Integer serial, [1] Integer GumpID, [2] 공백만 있는 문자열을 제외한 텍스트
# Array<String>, [3] 일반 버튼 설명 Array<String>, [4] 중첩된 항목을 포함한 모든 유효 컨트롤 설명 Array<String>. 잘못되거나
# 닫혔거나 무시된 검프는 []를 반환합니다. 최상위 비트가 설정된 ID는 음수 Integer입니다. Hex로 비트 표현을 표시합니다.

SUB Main()
    # 0은 첫 번째 서버 검프입니다. 필드에 접근하기 전에 GetArrayLength(info)=5인지 확인합니다. info[0]은 serial이고 info[1]은 같은
    # 스냅샷의 GumpID입니다.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        UO.Print('Serial=' + Hex(info[0]))
        UO.Print('GumpID=' + Hex(info[1]))
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 0은 첫 번째 서버 검프입니다. 필드에 접근하기 전에 GetArrayLength(info)=5인지 확인합니다. info[0]은 serial이고 info[1]은 같은 스냅샷의 GumpID입니다.

### 실제 ButtonID 나열하기

```vb
# 실제 ButtonID 나열하기
#
# 서버 검프와 해당 컨트롤의 일관된 스냅샷을 읽습니다.
#
# Array — 5개 필드의 Array: [0] Integer serial, [1] Integer GumpID, [2] 공백만 있는 문자열을 제외한 텍스트
# Array<String>, [3] 일반 버튼 설명 Array<String>, [4] 중첩된 항목을 포함한 모든 유효 컨트롤 설명 Array<String>. 잘못되거나
# 닫혔거나 무시된 검프는 []를 반환합니다. 최상위 비트가 설정된 ID는 음수 Integer입니다. Hex로 비트 표현을 표시합니다.

SUB Main()
    # info[3]은 버튼 설명을 담습니다. i는 줄 인덱스이며 응답에 사용할 ID는 설명의 ButtonID 필드에 있습니다. 라디오 버튼은 전체 컨트롤 목록에 포함됩니다.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR buttons = info[3]
        VAR i = 0
        WHILE i < GetArrayLength(buttons)
            UO.Print(buttons[i])
            i = i + 1
        WEND
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- info[3]은 버튼 설명을 담습니다. i는 줄 인덱스이며 응답에 사용할 ID는 설명의 ButtonID 필드에 있습니다. 라디오 버튼은 전체 컨트롤 목록에 포함됩니다.

### 닫기 전에 텍스트 보관하기

```vb
# 닫기 전에 텍스트 보관하기
#
# 서버 검프와 해당 컨트롤의 일관된 스냅샷을 읽습니다.
#
# Array — 5개 필드의 Array: [0] Integer serial, [1] Integer GumpID, [2] 공백만 있는 문자열을 제외한 텍스트
# Array<String>, [3] 일반 버튼 설명 Array<String>, [4] 중첩된 항목을 포함한 모든 유효 컨트롤 설명 Array<String>. 잘못되거나
# 닫혔거나 무시된 검프는 []를 반환합니다. 최상위 비트가 설정된 ID는 음수 Integer입니다. Hex로 비트 표현을 표시합니다.

SUB Main()
    # info[2]는 텍스트 복사본입니다. CloseSimpleGump(0)은 NoClose가 없을 때만 로컬에서 닫으며 값을 반환하지 않습니다. 저장된 텍스트는 유지됩니다.
    # texts[0]을 읽기 전에 배열 길이를 확인합니다.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR texts = info[2]
        UO.CloseSimpleGump(0)
        IF GetArrayLength(texts) > 0 THEN
            UO.Print(texts[0])
        END IF
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- info[2]는 텍스트 복사본입니다. CloseSimpleGump(0)은 NoClose가 없을 때만 로컬에서 닫으며 값을 반환하지 않습니다. 저장된 텍스트는 유지됩니다. texts[0]을 읽기 전에 배열 길이를 확인합니다.
