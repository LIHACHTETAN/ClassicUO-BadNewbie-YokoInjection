# UO.GetFlying

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

mobile의 비행 상태를 확인합니다.

## 정확한 구문

```text
UO.GetFlying() -> Integer
UO.GetFlying(value:Any) -> Integer
```

## 매개변수

- `value` — 표시된 호출 형식의 선택적 객체입니다. 숫자/16진수 문자열 serial, self, lasttarget 또는 등록된 AddObject 이름을 사용합니다. type이 아닙니다. 생략하면 self를 읽습니다. 일부 형식은 알 수 없는 문자열에서 변환 오류가 발생하므로 이름을 먼저 확인하세요.

## 반환값

Integer Boolean: 1 = TRUE, 0 = FALSE입니다. 숫자 또는 따옴표 없는 논리 상수와 비교할 수 있습니다. mobile에 IsFlying이 있으면 1, 없거나 mobile이 없으면 0입니다. 높이 Z만으로 비행을 판단하지 않습니다.

논리 결과입니다: 1 = TRUE, 0 = FALSE. VAR result = command(...)로 저장한 뒤 IF result = TRUE THEN 또는 IF result = 1 THEN을 사용합니다. 부정 결과는 IF result = FALSE THEN 또는 IF result = 0 THEN입니다. TRUE/FALSE에 따옴표를 쓰지 않습니다. 한 번 호출하고 결과를 저장하세요. 다시 호출하면 동작을 반복하거나 바뀐 상태를 읽을 수 있습니다.

## 동작

- 로컬 모델을 읽습니다. target이나 status 요청, 플래그 변경, 패킷 전송은 없습니다. 파괴된 객체는 사전 항목이 제거되기 전에도 없는 것으로 처리합니다.
- 각 결과는 독립적인 읽기입니다. Exists와 다음 호출 사이에 세계가 바뀔 수 있으므로 여러 조회가 원자적 스냅샷을 이루지는 않습니다.
- Poisoned/Flying은 프로토콜에 따릅니다. 7.0.0.0 전에는 비트 0x04가 중독을 뜻하고, 7.0.0.0부터는 비행을 뜻하며 중독은 별도로 저장됩니다. Z로 비행을 계산하지 않습니다.

### 내부 함수: 호출부터 결과까지

실제 C# 내부 단계입니다. ReadState는 예제에 완전하게 정의된 보조 함수이며 숨겨진 내장 명령이 아닙니다.

#### 1. RegisterCharacterGetterAliases

runtime 생성 시 RegisterCharacterGetterAliases가 이름과 호출 형식을 등록합니다. 인수가 없으면 bridge.Self, 있으면 지정한 serial을 사용합니다. 기존 등록은 유지됩니다.

mobile에 IsFlying이 있으면 1, 없거나 mobile이 없으면 0입니다. 높이 Z만으로 비행을 판단하지 않습니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject가 숫자, 16진수 문자열 및 저장된 이름을 해석합니다. AddObject 이름은 호출할 때마다 다시 해석하며 graphic/type 검색이나 대화형 선택을 수행하지 않습니다.

표시된 호출 형식의 선택적 객체입니다. 숫자/16진수 문자열 serial, self, lasttarget 또는 등록된 AddObject 이름을 사용합니다. type이 아닙니다. 생략하면 self를 읽습니다. 일부 형식은 알 수 없는 문자열에서 변환 오류가 발생하므로 이름을 먼저 확인하세요.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `TryGetObject`.

#### 3. Invoke

Invoke는 게임 스레드에서 읽습니다. 작업 스레드는 관리자의 처리를 기다리며 스크립트 취소가 대기를 중단합니다. 추가 지연이나 네트워크 요청은 없습니다.

각 결과는 독립적인 읽기입니다. Exists와 다음 호출 사이에 세계가 바뀔 수 있으므로 여러 조회가 원자적 스냅샷을 이루지는 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 4. Get

World.Get이 serial을 찾고 IsDestroyed이면 null을 반환한 뒤 Mobile 플래그를 읽습니다. Alive는 Exists와 IsDead의 부재를 확인하며 아이템도 허용합니다. self의 Dead는 Player.IsDead를 읽습니다.

mobile에 IsFlying이 있으면 1, 없거나 mobile이 없으면 0입니다. 높이 Z만으로 비행을 판단하지 않습니다.

프로젝트 소스: `src/ClassicUO.Client/Game/World.cs`; 함수 `Get`.

로컬 모델을 읽습니다. target이나 status 요청, 플래그 변경, 패킷 전송은 없습니다. 파괴된 객체는 사전 항목이 제거되기 전에도 없는 것으로 처리합니다.


## 예제

### 자신의 상태 확인

```vb
# 자신의 상태 확인
#
# mobile의 비행 상태를 확인합니다.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE입니다. 숫자 또는 따옴표 없는 논리 상수와 비교할 수 있습니다. mobile에 IsFlying이 있으면
# 1, 없거나 mobile이 없으면 0입니다. 높이 Z만으로 비행을 판단하지 않습니다.
#
# 논리 결과입니다: 1 = TRUE, 0 = FALSE. VAR result = command(...)로 저장한 뒤 IF result = TRUE THEN 또는 IF
# result = 1 THEN을 사용합니다. 부정 결과는 IF result = FALSE THEN 또는 IF result = 0 THEN입니다. TRUE/FALSE에
# 따옴표를 쓰지 않습니다. 한 번 호출하고 결과를 저장하세요. 다시 호출하면 동작을 반복하거나 바뀐 상태를 읽을 수 있습니다.

SUB Main()
    # 빈 괄호는 self를 읽습니다. active에 한 번의 결과를 저장하고 TRUE와 FALSE로 분기합니다. Print는 예시 메시지만 표시합니다.

    VAR active = UO.GetFlying()
    IF active = TRUE THEN
        UO.Print('State is active')
    ELSE
        UO.Print('State is inactive or unavailable')
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 빈 괄호는 self를 읽습니다. active에 한 번의 결과를 저장하고 TRUE와 FALSE로 분기합니다. Print는 예시 메시지만 표시합니다.

### 선택한 객체와 완전한 ReadState 함수

```vb
# 선택한 객체와 완전한 ReadState 함수
#
# mobile의 비행 상태를 확인합니다.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE입니다. 숫자 또는 따옴표 없는 논리 상수와 비교할 수 있습니다. mobile에 IsFlying이 있으면
# 1, 없거나 mobile이 없으면 0입니다. 높이 Z만으로 비행을 판단하지 않습니다.
#
# 논리 결과입니다: 1 = TRUE, 0 = FALSE. VAR result = command(...)로 저장한 뒤 IF result = TRUE THEN 또는 IF
# result = 1 THEN을 사용합니다. 부정 결과는 IF result = FALSE THEN 또는 IF result = 0 THEN입니다. TRUE/FALSE에
# 따옴표를 쓰지 않습니다. 한 번 호출하고 결과를 저장하세요. 다시 호출하면 동작을 반복하거나 바뀐 상태를 읽을 수 있습니다.

SUB Main()
    # lasttarget은 이전에 선택한 객체입니다. Exists로 존재를 확인합니다. obj는 ReadState의 유일한 매개변수이며 함수는 명령 결과를 그대로 반환합니다.
    # 복사한 코드에 전체 정의가 포함됩니다.

    IF UO.Exists('lasttarget') THEN
        VAR observed = ReadState('lasttarget')
        UO.Print('State 1/0: ' + CStr(observed))
    END IF
END SUB

SUB ReadState(obj)
    RETURN UO.GetFlying(obj)
END SUB
```

**매개변수 및 실행 설명:**

- lasttarget은 이전에 선택한 객체입니다. Exists로 존재를 확인합니다. obj는 ReadState의 유일한 매개변수이며 함수는 명령 결과를 그대로 반환합니다. 복사한 코드에 전체 정의가 포함됩니다.

### 0.5초 동안의 변화 감지

```vb
# 0.5초 동안의 변화 감지
#
# mobile의 비행 상태를 확인합니다.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE입니다. 숫자 또는 따옴표 없는 논리 상수와 비교할 수 있습니다. mobile에 IsFlying이 있으면
# 1, 없거나 mobile이 없으면 0입니다. 높이 Z만으로 비행을 판단하지 않습니다.
#
# 논리 결과입니다: 1 = TRUE, 0 = FALSE. VAR result = command(...)로 저장한 뒤 IF result = TRUE THEN 또는 IF
# result = 1 THEN을 사용합니다. 부정 결과는 IF result = FALSE THEN 또는 IF result = 0 THEN입니다. TRUE/FALSE에
# 따옴표를 쓰지 않습니다. 한 번 호출하고 결과를 저장하세요. 다시 호출하면 동작을 반복하거나 바뀐 상태를 읽을 수 있습니다.

SUB Main()
    # 인수 없는 두 호출은 self를 읽고 WAIT(500)은 500밀리초입니다. 두 스냅샷을 비교하므로 중간 변화를 놓칠 수 있습니다. 무한 대기는 없습니다.

    VAR before = UO.GetFlying()
    WAIT(500)
    VAR after = UO.GetFlying()
    IF before <> after THEN
        UO.Print('State changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 인수 없는 두 호출은 self를 읽고 WAIT(500)은 500밀리초입니다. 두 스냅샷을 비교하므로 중간 변화를 놓칠 수 있습니다. 무한 대기는 없습니다.
