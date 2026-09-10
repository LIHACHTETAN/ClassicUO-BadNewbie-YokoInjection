# UO.SetStatState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

능력치 성장 모드 변경을 요청합니다.

## 정확한 구문

```text
UO.SetStatState(statNum:Any, statState:Any) -> Unit
```

## 매개변수

- `statNum` — 필수 능력치 번호: 0 — STR, 1 — DEX, 2 — INT. 현재 값이나 이름 문자열이 아닙니다.
- `statState` — 필수 모드: 0 — 상승, 1 — 하락, 2 — 잠금. 세 가지 코드이며 Boolean이 아닙니다. true/false로 모든 모드를 표현할 수 없습니다.

## 반환값

Unit — 반환값이 없습니다. 성공/실패로 취급하거나 true와 비교하지 마세요. 이후 조회는 로컬 모델이며 서버 확인 응답이 아닙니다.

## 동작

- 유효 요청은 GameActions로 패킷 하나를 보내고 로컬 모드를 즉시 바꿉니다. 서버 규칙은 계속 적용되며 성장하지 않을 수 있습니다. 알 수 없는 기술, 잘못된 인덱스/모드, 캐릭터 부재는 패킷 없이 무시합니다.
- 필수 능력치 번호: 0 — STR, 1 — DEX, 2 — INT. 현재 값이나 이름 문자열이 아닙니다.
- ExecuteStealthCompatibility가 분기를 선택합니다. Text는 기술 선택자, Arg는 숫자 번호와 모드를 읽습니다. 변환할 수 없는 인수는 변환 오류를 낼 수 있습니다.

### 내부 함수: 호출부터 결과까지

실제 C# 내부 단계입니다. ApplyMode는 예제에 완전하게 정의된 보조 함수이며 숨겨진 내장 명령이 아닙니다.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility가 분기를 선택합니다. Text는 기술 선택자, Arg는 숫자 번호와 모드를 읽습니다. 변환할 수 없는 인수는 변환 오류를 낼 수 있습니다.

Unit — 반환값이 없습니다. 성공/실패로 취급하거나 true와 비교하지 마세요. 이후 조회는 로컬 모델이며 서버 확인 응답이 아닙니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke는 게임 스레드에서 읽습니다. 작업 스레드는 관리자의 처리를 기다리며 스크립트 취소가 대기를 중단합니다. 추가 지연이나 네트워크 요청은 없습니다.

유효 요청은 GameActions로 패킷 하나를 보내고 로컬 모드를 즉시 바꿉니다. 서버 규칙은 계속 적용되며 성장하지 않을 수 있습니다. 알 수 없는 기술, 잘못된 인덱스/모드, 캐릭터 부재는 패킷 없이 무시합니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 3. SetStatLockState

GetStatLockState/SetStatLockState는 0/1/2에 따라 StrLock, DexLock, IntLock을 선택합니다. 모르는 번호는 −1이며 쓰기는 전송 전에 두 범위를 검사합니다.

Unit — 반환값이 없습니다. 성공/실패로 취급하거나 true와 비교하지 마세요. 이후 조회는 로컬 모델이며 서버 확인 응답이 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `SetStatLockState`.

#### 4. ChangeStatLock

유효 요청은 GameActions로 패킷 하나를 보내고 로컬 모드를 즉시 바꿉니다. 서버 규칙은 계속 적용되며 성장하지 않을 수 있습니다. 알 수 없는 기술, 잘못된 인덱스/모드, 캐릭터 부재는 패킷 없이 무시합니다.

Unit — 반환값이 없습니다. 성공/실패로 취급하거나 true와 비교하지 마세요. 이후 조회는 로컬 모델이며 서버 확인 응답이 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/GameActions.cs`; 함수 `ChangeStatLock`.

유효 요청은 GameActions로 패킷 하나를 보내고 로컬 모드를 즉시 바꿉니다. 서버 규칙은 계속 적용되며 성장하지 않을 수 있습니다. 알 수 없는 기술, 잘못된 인덱스/모드, 캐릭터 부재는 패킷 없이 무시합니다.


## 예제

### 읽고 표시하기

```vb
# 읽고 표시하기
#
# 능력치 성장 모드 변경을 요청합니다.
#
# Unit — 반환값이 없습니다. 성공/실패로 취급하거나 true와 비교하지 마세요. 이후 조회는 로컬 모델이며 서버 확인 응답이 아닙니다.

SUB Main()
    # 예제는 selector와 쓰기용 mode를 명시합니다. 첫 줄은 이름으로 기술을, 번호로 능력치를 선택합니다. Print는 표시만 합니다.

    VAR selector = 0
    VAR mode = 2
    UO.SetStatState(selector, mode)
    UO.Print(CStr(UO.GetStatLockState(selector)))
END SUB
```

**매개변수 및 실행 설명:**

- 예제는 selector와 쓰기용 mode를 명시합니다. 첫 줄은 이름으로 기술을, 번호로 능력치를 선택합니다. Print는 표시만 합니다.

### 조건 또는 비교에 사용

```vb
# 조건 또는 비교에 사용
#
# 능력치 성장 모드 변경을 요청합니다.
#
# Unit — 반환값이 없습니다. 성공/실패로 취급하거나 true와 비교하지 마세요. 이후 조회는 로컬 모델이며 서버 확인 응답이 아닙니다.

SUB Main()
    # 임계값 95.1과 모드 0/1/2는 예제 설정입니다. 변경 전에 −1을 확인합니다. 쓰기 후 읽기는 서버 응답을 기다리지 않고 로컬 복사본을 보여 줍니다.

    VAR selector = 0
    VAR before = UO.GetStatLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetStatState(selector, 0)
        UO.Print(CStr(UO.GetStatLockState(selector)))
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 임계값 95.1과 모드 0/1/2는 예제 설정입니다. 변경 전에 −1을 확인합니다. 쓰기 후 읽기는 서버 응답을 기다리지 않고 로컬 복사본을 보여 줍니다.

### 완전한 보조 함수

```vb
# 완전한 보조 함수
#
# 능력치 성장 모드 변경을 요청합니다.
#
# Unit — 반환값이 없습니다. 성공/실패로 취급하거나 true와 비교하지 마세요. 이후 조회는 로컬 모델이며 서버 확인 응답이 아닙니다.

SUB Main()
    # Main 뒤에 보조 함수 전체가 나옵니다. selector는 기술/능력치, mode는 쓰기 모드입니다. ReadValue/ReadMode는 원래 숫자를 반환합니다.
    # ApplyMode는 인수를 검사하고 동작하며 반환값이 없습니다. WAIT(1000)은 두 조회 스냅샷을 구분합니다.

    ApplyMode(0, 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetStatLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetStatState(selector, mode)
END SUB
```

**매개변수 및 실행 설명:**

- Main 뒤에 보조 함수 전체가 나옵니다. selector는 기술/능력치, mode는 쓰기 모드입니다. ReadValue/ReadMode는 원래 숫자를 반환합니다. ApplyMode는 인수를 검사하고 동작하며 반환값이 없습니다. WAIT(1000)은 두 조회 스냅샷을 구분합니다.
