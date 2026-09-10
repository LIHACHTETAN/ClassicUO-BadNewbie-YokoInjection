# UO.GetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

능력치의 로컬 성장 모드를 읽습니다.

## 정확한 구문

```text
UO.GetStatLockState(statNum:Any) -> Integer
```

## 매개변수

- `statNum` — 필수 능력치 번호: 0 — STR, 1 — DEX, 2 — INT. 현재 값이나 이름 문자열이 아닙니다.

## 반환값

Integer: 0 — 상승, 1 — 하락, 2 — 잠금. 모드 코드이며 true/false가 아닙니다. 0..2 밖의 번호는 −1을 반환합니다. 캐릭터가 없으면 유효 번호는 기본값 0을 반환하며 서버 상태를 확인한 것은 아닙니다.

## 동작

- Invoke는 게임 스레드에서 기존 데이터를 읽으며 네트워크 패킷을 보내지 않습니다. 기술 사용이나 훈련을 하지 않습니다. 두 조회는 별개 스냅샷입니다.
- 필수 능력치 번호: 0 — STR, 1 — DEX, 2 — INT. 현재 값이나 이름 문자열이 아닙니다.
- ExecuteStealthCompatibility가 분기를 선택합니다. Text는 기술 선택자, Arg는 숫자 번호와 모드를 읽습니다. 변환할 수 없는 인수는 변환 오류를 낼 수 있습니다.

### 내부 함수: 호출부터 결과까지

실제 C# 내부 단계입니다. ReadMode는 예제에 완전하게 정의된 보조 함수이며 숨겨진 내장 명령이 아닙니다.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility가 분기를 선택합니다. Text는 기술 선택자, Arg는 숫자 번호와 모드를 읽습니다. 변환할 수 없는 인수는 변환 오류를 낼 수 있습니다.

Integer: 0 — 상승, 1 — 하락, 2 — 잠금. 모드 코드이며 true/false가 아닙니다. 0..2 밖의 번호는 −1을 반환합니다. 캐릭터가 없으면 유효 번호는 기본값 0을 반환하며 서버 상태를 확인한 것은 아닙니다.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke는 게임 스레드에서 읽습니다. 작업 스레드는 관리자의 처리를 기다리며 스크립트 취소가 대기를 중단합니다. 추가 지연이나 네트워크 요청은 없습니다.

Invoke는 게임 스레드에서 기존 데이터를 읽으며 네트워크 패킷을 보내지 않습니다. 기술 사용이나 훈련을 하지 않습니다. 두 조회는 별개 스냅샷입니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 3. GetStatLockState

GetStatLockState/SetStatLockState는 0/1/2에 따라 StrLock, DexLock, IntLock을 선택합니다. 모르는 번호는 −1이며 쓰기는 전송 전에 두 범위를 검사합니다.

Integer: 0 — 상승, 1 — 하락, 2 — 잠금. 모드 코드이며 true/false가 아닙니다. 0..2 밖의 번호는 −1을 반환합니다. 캐릭터가 없으면 유효 번호는 기본값 0을 반환하며 서버 상태를 확인한 것은 아닙니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `GetStatLockState`.

Invoke는 게임 스레드에서 기존 데이터를 읽으며 네트워크 패킷을 보내지 않습니다. 기술 사용이나 훈련을 하지 않습니다. 두 조회는 별개 스냅샷입니다.


## 예제

### 읽고 표시하기

```vb
# 읽고 표시하기
#
# 능력치의 로컬 성장 모드를 읽습니다.
#
# Integer: 0 — 상승, 1 — 하락, 2 — 잠금. 모드 코드이며 true/false가 아닙니다. 0..2 밖의 번호는 −1을 반환합니다. 캐릭터가 없으면 유효
# 번호는 기본값 0을 반환하며 서버 상태를 확인한 것은 아닙니다.

SUB Main()
    # 예제는 selector와 쓰기용 mode를 명시합니다. 첫 줄은 이름으로 기술을, 번호로 능력치를 선택합니다. Print는 표시만 합니다.

    VAR selector = 0
    VAR mode = UO.GetStatLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**매개변수 및 실행 설명:**

- 예제는 selector와 쓰기용 mode를 명시합니다. 첫 줄은 이름으로 기술을, 번호로 능력치를 선택합니다. Print는 표시만 합니다.

### 조건 또는 비교에 사용

```vb
# 조건 또는 비교에 사용
#
# 능력치의 로컬 성장 모드를 읽습니다.
#
# Integer: 0 — 상승, 1 — 하락, 2 — 잠금. 모드 코드이며 true/false가 아닙니다. 0..2 밖의 번호는 −1을 반환합니다. 캐릭터가 없으면 유효
# 번호는 기본값 0을 반환하며 서버 상태를 확인한 것은 아닙니다.

SUB Main()
    # 임계값 95.1과 모드 0/1/2는 예제 설정입니다. 변경 전에 −1을 확인합니다. 쓰기 후 읽기는 서버 응답을 기다리지 않고 로컬 복사본을 보여 줍니다.

    VAR mode = UO.GetStatLockState(0)
    IF mode = 2 THEN
        UO.Print("Locked")
    ELSE
        IF mode = -1 THEN
            UO.Print("Unknown selector")
        ELSE
            UO.Print("Mode: " + CStr(mode))
        END IF
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 임계값 95.1과 모드 0/1/2는 예제 설정입니다. 변경 전에 −1을 확인합니다. 쓰기 후 읽기는 서버 응답을 기다리지 않고 로컬 복사본을 보여 줍니다.

### 완전한 보조 함수

```vb
# 완전한 보조 함수
#
# 능력치의 로컬 성장 모드를 읽습니다.
#
# Integer: 0 — 상승, 1 — 하락, 2 — 잠금. 모드 코드이며 true/false가 아닙니다. 0..2 밖의 번호는 −1을 반환합니다. 캐릭터가 없으면 유효
# 번호는 기본값 0을 반환하며 서버 상태를 확인한 것은 아닙니다.

SUB Main()
    # Main 뒤에 보조 함수 전체가 나옵니다. selector는 기술/능력치, mode는 쓰기 모드입니다. ReadValue/ReadMode는 원래 숫자를 반환합니다.
    # ApplyMode는 인수를 검사하고 동작하며 반환값이 없습니다. WAIT(1000)은 두 조회 스냅샷을 구분합니다.

    VAR before = ReadMode(0)
    WAIT(1000)
    VAR after = ReadMode(0)
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetStatLockState(selector)
END SUB
```

**매개변수 및 실행 설명:**

- Main 뒤에 보조 함수 전체가 나옵니다. selector는 기술/능력치, mode는 쓰기 모드입니다. ReadValue/ReadMode는 원래 숫자를 반환합니다. ApplyMode는 인수를 검사하고 동작하며 반환값이 없습니다. WAIT(1000)은 두 조회 스냅샷을 구분합니다.
