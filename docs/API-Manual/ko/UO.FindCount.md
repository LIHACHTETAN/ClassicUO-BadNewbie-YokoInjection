# UO.FindCount

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

검색 객체 수 또는 ID로 지정한 스택의 수량을 읽습니다.

## 정확한 구문

```text
UO.FindCount() -> Integer
UO.FindCount(id:Any) -> Integer
```

## 매개변수

- `id` — FindCount에서만 생략할 수 있습니다. 아이템의 serial: Integer, 10진수/16진수 문자열, lasttarget, lastobject, backpack 또는 AddObject 이름입니다. graphic/type이 아닌 ID를 전달합니다. 알 수 없는 이름은 0입니다. self는 캐릭터이므로 여기서는 0입니다. 생략하면 검색 객체 수를 읽습니다.

## 반환값

Integer — FindCount()는 찾은 객체 수이며 스택 하나를 item 하나로 셉니다. FindCount(id)는 해당 아이템의 현재 Amount입니다. 알 수 없거나 삭제된 ID 및 캐릭터는 0입니다. 겹칠 수 없는 물품은 보통 Amount=1입니다. ID, type 또는 Boolean이 아닙니다.

## 동작

- 일반 FindType(인수 1–5개), FindTypeEx 및 Count/CountEx/CountGround는 이 스크립트의 검색 결과를 교체합니다. 일치 항목이 없으면 결과를 비웁니다. 다음 검색 후에도 쓸 값은 먼저 저장하세요.
- 이 호출은 검색, 컨테이너 열기, 아이템 이동, 패킷 전송을 하지 않고 클라이언트에 로드된 데이터를 읽습니다. FindCount(id)는 이전 검색이 필요 없고 검색 결과를 바꾸지 않습니다.
- FindItem/FindCount()/FindFullQuantity는 검색 시점의 기록입니다. FindQuantity와 FindCount(id)는 현재 수량을 읽으므로 검색 후 아이템의 변경이나 소멸을 반영합니다.

## 예제

### 금화 검색 결과 읽기

```vb
# 금화 검색 결과 읽기
#
# 검색 객체 수 또는 ID로 지정한 스택의 수량을 읽습니다.
#
# Integer — FindCount()는 찾은 객체 수이며 스택 하나를 item 하나로 셉니다. FindCount(id)는 해당 아이템의 현재 Amount입니다. 알 수
# 없거나 삭제된 ID 및 캐릭터는 0입니다. 겹칠 수 없는 물품은 보통 Amount=1입니다. ID, type 또는 Boolean이 아닙니다.

SUB Main()
    # type=0x0EED는 금화, color=-1은 모든 색입니다. 이 FindType 형식에서 backpack은 배낭의 바로 아래 내용물입니다. value에 결과를
    # 저장하고 STR로 표시합니다.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindCount()
    UO.Print(STR(value))
END SUB
```

**매개변수 및 실행 설명:**

- type=0x0EED는 금화, color=-1은 모든 색입니다. 이 FindType 형식에서 backpack은 배낭의 바로 아래 내용물입니다. value에 결과를 저장하고 STR로 표시합니다.

### 객체, 스택, 합계 비교

```vb
# 객체, 스택, 합계 비교
#
# 검색 객체 수 또는 ID로 지정한 스택의 수량을 읽습니다.
#
# Integer — FindCount()는 찾은 객체 수이며 스택 하나를 item 하나로 셉니다. FindCount(id)는 해당 아이템의 현재 Amount입니다. 알 수
# 없거나 삭제된 ID 및 캐릭터는 0입니다. 겹칠 수 없는 물품은 보통 Amount=1입니다. ID, type 또는 Boolean이 아닙니다.

SUB Main()
    # 네 번 모두 같은 검색 뒤에 읽습니다. 50개짜리 두 스택이면 객체 수=2, 첫 스택=50, 합계=100입니다. FindItem은 첫 스택의 고유 ID이며 type이
    # 아닙니다.

    UO.FindType(0x0EED, -1, 'backpack')
    UO.Print(STR(UO.FindCount()))
    UO.Print(STR(UO.FindQuantity()))
    UO.Print(STR(UO.FindFullQuantity()))
    UO.Print('0x' + Hex(UO.FindItem()))
END SUB
```

**매개변수 및 실행 설명:**

- 네 번 모두 같은 검색 뒤에 읽습니다. 50개짜리 두 스택이면 객체 수=2, 첫 스택=50, 합계=100입니다. FindItem은 첫 스택의 고유 ID이며 type이 아닙니다.

### 다른 검색 전에 값 보관

```vb
# 다른 검색 전에 값 보관
#
# 검색 객체 수 또는 ID로 지정한 스택의 수량을 읽습니다.
#
# Integer — FindCount()는 찾은 객체 수이며 스택 하나를 item 하나로 셉니다. FindCount(id)는 해당 아이템의 현재 Amount입니다. 알 수
# 없거나 삭제된 ID 및 캐릭터는 0입니다. 겹칠 수 없는 물품은 보통 Amount=1입니다. ID, type 또는 Boolean이 아닙니다.

SUB Main()
    # 첫 type은 금화이고 0x0F7A는 다른 시약입니다. 두 번째 FindType은 결과를 교체합니다. saved는 이전 값을 유지하고 마지막 호출은 새 결과를 읽습니다.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindCount()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindCount()))
END SUB
```

**매개변수 및 실행 설명:**

- 첫 type은 금화이고 0x0F7A는 다른 시약입니다. 두 번째 FindType은 결과를 교체합니다. saved는 이전 값을 유지하고 마지막 호출은 새 결과를 읽습니다.

### ID로 아이템 직접 읽기

```vb
# ID로 아이템 직접 읽기
#
# 검색 객체 수 또는 ID로 지정한 스택의 수량을 읽습니다.
#
# Integer — FindCount()는 찾은 객체 수이며 스택 하나를 item 하나로 셉니다. FindCount(id)는 해당 아이템의 현재 Amount입니다. 알 수
# 없거나 삭제된 ID 및 캐릭터는 0입니다. 겹칠 수 없는 물품은 보통 Amount=1입니다. ID, type 또는 Boolean이 아닙니다.

SUB Main()
    # lasttarget은 게임에서 이미 선택한 아이템을 가리켜야 합니다. 새 타깃 커서는 나타나지 않습니다. FindCount(id)는 현재 스택을 읽고 아이템이 없으면
    # 0을 반환하며 검색 결과를 유지합니다.

    VAR id = lasttarget
    VAR amount = UO.FindCount(id)
    UO.Print(STR(amount))
END SUB
```

**매개변수 및 실행 설명:**

- lasttarget은 게임에서 이미 선택한 아이템을 가리켜야 합니다. 새 타깃 커서는 나타나지 않습니다. FindCount(id)는 현재 스택을 읽고 아이템이 없으면 0을 반환하며 검색 결과를 유지합니다.
