# UO.GetGold

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

현재 플레이어 status에 보고된 골드 금액을 읽습니다.

## 정확한 구문

```text
UO.GetGold() -> Any
```

## 매개변수

매개변수가 없습니다.

## 반환값

Integer/Decimal: 음수가 아닌 0..4294967295 금액입니다. 2147483647까지 Integer, 그 이상은 모든 UInt32 정수를 정확히 표현하는 Decimal(Double)입니다. 0은 Player 없음/파괴됨 또는 금액 미수신도 뜻합니다. Boolean, ID, 스택 수, 가방/은행 검색 결과가 아닙니다.

## 동작

- 인자가 없습니다. CharacterStatus(0x11)가 보관한 Player.Gold를 읽습니다. 포함되는 골드 범위는 서버가 정합니다. 가방을 순회하거나 은행 잔액을 요청하지 않습니다. Player 없음/파괴됨은 0이며 존재하는 유령은 금액을 유지할 수 있습니다.
- ReadGoldValue는 bridge.Gold를 한 번 읽습니다. C# bridge는 Int32 시그니처를 유지하며 UInt32 비트를 전달합니다. unchecked 변환으로 부호 없는 금액을 복원하고 작은 값은 Integer, 큰 값은 Decimal로 감쌉니다. 최상위 비트가 잔액을 음수로 바꾸지 않습니다. 로컬 변환으로 패킷을 보내지 않습니다.
- 큰 금액은 수치 결과 그대로 비교하세요. CInt/CLng는 32비트 Integer 변환입니다. 큰 BASIC 리터럴은 3000000000.0처럼 소수점을 붙입니다. 구매 전 잔액은 바뀔 수 있습니다. CanAfford는 로컬 확인이며 서버 승인이 아닙니다.
- 호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.

### 내부 함수: 호출부터 결과까지

status 카운터 읽기와 부호 없는 범위 확장의 네이티브 단계입니다. CanAfford는 아래에 완전히 정의된 사용자 BASIC 함수이며 숨겨진 구매 명령이 아닙니다.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases는 누락된 Gold/GetGold 함수와 내장 이름을 추가합니다. UO.Gold 호환 분기와 내장 값도 같은 ReadGoldValue를 사용합니다. 변수가 가리지 않는 내장 이름은 매번 다시 읽습니다.

Integer/Decimal: 음수가 아닌 0..4294967295 금액입니다. 2147483647까지 Integer, 그 이상은 모든 UInt32 정수를 정확히 표현하는 Decimal(Double)입니다. 0은 Player 없음/파괴됨 또는 금액 미수신도 뜻합니다. Boolean, ID, 스택 수, 가방/은행 검색 결과가 아닙니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `RegisterCharacterGetterAliases`.

#### 2. ReadGoldValue

ReadGoldValue는 bridge.Gold를 한 번 읽습니다. C# bridge는 Int32 시그니처를 유지하며 UInt32 비트를 전달합니다. unchecked 변환으로 부호 없는 금액을 복원하고 작은 값은 Integer, 큰 값은 Decimal로 감쌉니다. 최상위 비트가 잔액을 음수로 바꾸지 않습니다. 로컬 변환으로 패킷을 보내지 않습니다.

큰 금액은 수치 결과 그대로 비교하세요. CInt/CLng는 32비트 Integer 변환입니다. 큰 BASIC 리터럴은 3000000000.0처럼 소수점을 붙입니다. 구매 전 잔액은 바뀔 수 있습니다. CanAfford는 로컬 확인이며 서버 승인이 아닙니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ReadGoldValue`.

#### 3. Invoke

인자가 없습니다. CharacterStatus(0x11)가 보관한 Player.Gold를 읽습니다. 포함되는 골드 범위는 서버가 정합니다. 가방을 순회하거나 은행 잔액을 요청하지 않습니다. Player 없음/파괴됨은 0이며 존재하는 유령은 금액을 유지할 수 있습니다.

Invoke는 게임 스레드에서 읽고 대기는 스크립트 취소에 대응합니다. status 요청, 타깃, 패킷 전송, 능력치 변경, 내장 지연이 없습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 4. CharacterStatus

인자가 없습니다. CharacterStatus(0x11)가 보관한 Player.Gold를 읽습니다. 포함되는 골드 범위는 서버가 정합니다. 가방을 순회하거나 은행 잔액을 요청하지 않습니다. Player 없음/파괴됨은 0이며 존재하는 유령은 금액을 유지할 수 있습니다.

호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.

프로젝트 소스: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 함수 `CharacterStatus`.

#### 5. Clear

World.Clear는 Player를 제거합니다. 플레이어와 데이터가 다시 준비될 때까지 0입니다. 재접속 후 저장된 값만으로 조건 충족을 판단하지 마세요.

Integer/Decimal: 음수가 아닌 0..4294967295 금액입니다. 2147483647까지 Integer, 그 이상은 모든 UInt32 정수를 정확히 표현하는 Decimal(Double)입니다. 0은 Player 없음/파괴됨 또는 금액 미수신도 뜻합니다. Boolean, ID, 스택 수, 가방/은행 검색 결과가 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Clear`.

호출마다 로컬 값을 다시 읽습니다. 변수는 스냅샷이며 별도 호출은 서로 다른 업데이트를 볼 수 있습니다. 0이 아닌 값은 접속 확인이 아니며 0은 실제 값과 데이터 없음을 모두 나타냅니다.


## 예제

### 보고된 금액 출력

```vb
# 보고된 금액 출력
#
# 현재 플레이어 status에 보고된 골드 금액을 읽습니다.
#
# Integer/Decimal: 음수가 아닌 0..4294967295 금액입니다. 2147483647까지 Integer, 그 이상은 모든 UInt32 정수를 정확히
# 표현하는 Decimal(Double)입니다. 0은 Player 없음/파괴됨 또는 금액 미수신도 뜻합니다. Boolean, ID, 스택 수, 가방/은행 검색 결과가
# 아닙니다.

SUB Main()
    # amount는 조회 한 번의 결과이며 CStr는 일지용 서식만 지정합니다. 골드를 검색, 이동, 소비하지 않습니다.

    VAR amount = UO.GetGold()
    UO.Print('Status gold: ' + CStr(amount))
END SUB
```

**매개변수 및 실행 설명:**

- amount는 조회 한 번의 결과이며 CStr는 일지용 서식만 지정합니다. 골드를 검색, 이동, 소비하지 않습니다.

### 큰 가격을 사용하는 완전한 CanAfford

```vb
# 큰 가격을 사용하는 완전한 CanAfford
#
# 현재 플레이어 status에 보고된 골드 금액을 읽습니다.
#
# Integer/Decimal: 음수가 아닌 0..4294967295 금액입니다. 2147483647까지 Integer, 그 이상은 모든 UInt32 정수를 정확히
# 표현하는 Decimal(Double)입니다. 0은 Player 없음/파괴됨 또는 금액 미수신도 뜻합니다. Boolean, ID, 스택 수, 가방/은행 검색 결과가
# 아닙니다.

SUB Main()
    # price=3000000000.0은 예제 가격입니다. CanAfford(price)는 음수 가격이나 Player 없음을 거부하고 한 번 읽어 amount >= price
    # 비교로 Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 금액 자체는 Boolean이 아닙니다. 전체 정의가 아래에 있습니다.

    VAR price = 3000000000.0
    IF CanAfford(price) = TRUE THEN
        UO.Print('Local balance is sufficient')
    ELSE
        UO.Print('Local check failed')
    END IF
END SUB

SUB CanAfford(price)
    IF price < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR amount = UO.GetGold()
    RETURN amount >= price
END SUB
```

**매개변수 및 실행 설명:**

- price=3000000000.0은 예제 가격입니다. CanAfford(price)는 음수 가격이나 Player 없음을 거부하고 한 번 읽어 amount >= price 비교로 Integer Boolean 1=TRUE 또는 0=FALSE를 반환합니다. 금액 자체는 Boolean이 아닙니다. 전체 정의가 아래에 있습니다.

### 잔액 변화 관측

```vb
# 잔액 변화 관측
#
# 현재 플레이어 status에 보고된 골드 금액을 읽습니다.
#
# Integer/Decimal: 음수가 아닌 0..4294967295 금액입니다. 2147483647까지 Integer, 그 이상은 모든 UInt32 정수를 정확히
# 표현하는 Decimal(Double)입니다. 0은 Player 없음/파괴됨 또는 금액 미수신도 뜻합니다. Boolean, ID, 스택 수, 가방/은행 검색 결과가
# 아닙니다.

SUB Main()
    # before/after 간격은 WAIT(500)밀리초입니다. 잔액이 줄면 difference=after-before는 음수일 수 있으며 수정한 부호 없는 오버플로와
    # 다릅니다. 중간 업데이트나 캐릭터 변경을 놓칠 수 있습니다.

    VAR before = UO.GetGold()
    WAIT(500)
    VAR after = UO.GetGold()
    VAR difference = after - before
    UO.Print('Balance change: ' + CStr(difference))
END SUB
```

**매개변수 및 실행 설명:**

- before/after 간격은 WAIT(500)밀리초입니다. 잔액이 줄면 difference=after-before는 음수일 수 있으며 수정한 부호 없는 오버플로와 다릅니다. 중간 업데이트나 캐릭터 변경을 놓칠 수 있습니다.
