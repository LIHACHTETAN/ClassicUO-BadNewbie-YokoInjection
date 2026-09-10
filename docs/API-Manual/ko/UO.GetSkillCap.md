# UO.GetSkillCap

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

서버에서 받은 기술 상한 값을 읽습니다.

## 정확한 구문

```text
UO.GetSkillCap(SkillName:Any) -> Decimal
```

## 매개변수

- `SkillName` — 필수 기술 선택자: "Mining", "Animal Lore" 같은 클라이언트 데이터의 이름 또는 숫자/문자열로 지정하는 십진 인덱스 0..Skills.Length−1. 이름은 대소문자를 구분하지 않고 양끝 공백을 제거하며 _를 공백으로 바꿉니다. 아이템 ID나 1부터 시작하는 번호가 아닙니다. 숫자 문자열은 항상 인덱스입니다.

## 반환값

Decimal (Double) — 0.1 단위 기술 점수입니다. 예를 들어 951이 아니라 95.1입니다. CapFixed 필드를 Double로 직접 10으로 나눕니다. 0은 기술 값이 0이거나 캐릭터/기술이 없음을 뜻합니다. Boolean이 아닙니다. 기존 SkillVal/BaseVal은 다른 척도를 사용하므로 혼용하지 마세요.

## 동작

- Invoke는 게임 스레드에서 기존 데이터를 읽으며 네트워크 패킷을 보내지 않습니다. 기술 사용이나 훈련을 하지 않습니다. 두 조회는 별개 스냅샷입니다.
- 필수 기술 선택자: "Mining", "Animal Lore" 같은 클라이언트 데이터의 이름 또는 숫자/문자열로 지정하는 십진 인덱스 0..Skills.Length−1. 이름은 대소문자를 구분하지 않고 양끝 공백을 제거하며 _를 공백으로 바꿉니다. 아이템 ID나 1부터 시작하는 번호가 아닙니다. 숫자 문자열은 항상 인덱스입니다.
- ExecuteStealthCompatibility가 분기를 선택합니다. Text는 기술 선택자, Arg는 숫자 번호와 모드를 읽습니다. 변환할 수 없는 인수는 변환 오류를 낼 수 있습니다.

### 내부 함수: 호출부터 결과까지

실제 C# 내부 단계입니다. ReadValue는 예제에 완전하게 정의된 보조 함수이며 숨겨진 내장 명령이 아닙니다.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility가 분기를 선택합니다. Text는 기술 선택자, Arg는 숫자 번호와 모드를 읽습니다. 변환할 수 없는 인수는 변환 오류를 낼 수 있습니다.

Decimal (Double) — 0.1 단위 기술 점수입니다. 예를 들어 951이 아니라 95.1입니다. CapFixed 필드를 Double로 직접 10으로 나눕니다. 0은 기술 값이 0이거나 캐릭터/기술이 없음을 뜻합니다. Boolean이 아닙니다. 기존 SkillVal/BaseVal은 다른 척도를 사용하므로 혼용하지 마세요.

프로젝트 소스: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 함수 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke는 게임 스레드에서 읽습니다. 작업 스레드는 관리자의 처리를 기다리며 스크립트 취소가 대기를 중단합니다. 추가 지연이나 네트워크 요청은 없습니다.

Invoke는 게임 스레드에서 기존 데이터를 읽으며 네트워크 패킷을 보내지 않습니다. 기술 사용이나 훈련을 하지 않습니다. 두 조회는 별개 스냅샷입니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe는 먼저 십진 인덱스와 범위를 검사합니다. 그렇지 않으면 이름을 정규화하고 Skill.Name과 대소문자 구분 없이 완전히 일치하는 항목을 찾습니다. 모르는 이름은 null이며 타깃을 열지 않습니다.

알 수 없는 기술 또는 캐릭터 부재 시 −1을 반환합니다.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `FindSkillUnsafe`.

#### 4. GetSkillValue

GetSkillValue는 BaseFixed, ValueFixed, CapFixed를 선택하고 정수 십분위 값을 10d로 나눕니다. 중간에 Single로 반올림하지 않습니다.

Decimal (Double) — 0.1 단위 기술 점수입니다. 예를 들어 951이 아니라 95.1입니다. CapFixed 필드를 Double로 직접 10으로 나눕니다. 0은 기술 값이 0이거나 캐릭터/기술이 없음을 뜻합니다. Boolean이 아닙니다. 기존 SkillVal/BaseVal은 다른 척도를 사용하므로 혼용하지 마세요.

프로젝트 소스: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 함수 `GetSkillValue`.

Invoke는 게임 스레드에서 기존 데이터를 읽으며 네트워크 패킷을 보내지 않습니다. 기술 사용이나 훈련을 하지 않습니다. 두 조회는 별개 스냅샷입니다.


## 예제

### 읽고 표시하기

```vb
# 읽고 표시하기
#
# 서버에서 받은 기술 상한 값을 읽습니다.
#
# Decimal (Double) — 0.1 단위 기술 점수입니다. 예를 들어 951이 아니라 95.1입니다. CapFixed 필드를 Double로 직접 10으로 나눕니다.
# 0은 기술 값이 0이거나 캐릭터/기술이 없음을 뜻합니다. Boolean이 아닙니다. 기존 SkillVal/BaseVal은 다른 척도를 사용하므로 혼용하지 마세요.

SUB Main()
    # 예제는 selector와 쓰기용 mode를 명시합니다. 첫 줄은 이름으로 기술을, 번호로 능력치를 선택합니다. Print는 표시만 합니다.

    VAR selector = 'Mining'
    VAR value = UO.GetSkillCap(selector)
    UO.Print(CStr(value))
END SUB
```

**매개변수 및 실행 설명:**

- 예제는 selector와 쓰기용 mode를 명시합니다. 첫 줄은 이름으로 기술을, 번호로 능력치를 선택합니다. Print는 표시만 합니다.

### 조건 또는 비교에 사용

```vb
# 조건 또는 비교에 사용
#
# 서버에서 받은 기술 상한 값을 읽습니다.
#
# Decimal (Double) — 0.1 단위 기술 점수입니다. 예를 들어 951이 아니라 95.1입니다. CapFixed 필드를 Double로 직접 10으로 나눕니다.
# 0은 기술 값이 0이거나 캐릭터/기술이 없음을 뜻합니다. Boolean이 아닙니다. 기존 SkillVal/BaseVal은 다른 척도를 사용하므로 혼용하지 마세요.

SUB Main()
    # 임계값 95.1과 모드 0/1/2는 예제 설정입니다. 변경 전에 −1을 확인합니다. 쓰기 후 읽기는 서버 응답을 기다리지 않고 로컬 복사본을 보여 줍니다.

    IF UO.GetSkillLockState('Mining') >= 0 THEN
        VAR value = UO.GetSkillCap('Mining')
        IF value >= 95.1 THEN
            UO.Print('Value >= 95.1: ' + CStr(value))
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
# 서버에서 받은 기술 상한 값을 읽습니다.
#
# Decimal (Double) — 0.1 단위 기술 점수입니다. 예를 들어 951이 아니라 95.1입니다. CapFixed 필드를 Double로 직접 10으로 나눕니다.
# 0은 기술 값이 0이거나 캐릭터/기술이 없음을 뜻합니다. Boolean이 아닙니다. 기존 SkillVal/BaseVal은 다른 척도를 사용하므로 혼용하지 마세요.

SUB Main()
    # Main 뒤에 보조 함수 전체가 나옵니다. selector는 기술/능력치, mode는 쓰기 모드입니다. ReadValue/ReadMode는 원래 숫자를 반환합니다.
    # ApplyMode는 인수를 검사하고 동작하며 반환값이 없습니다. WAIT(1000)은 두 조회 스냅샷을 구분합니다.

    VAR before = ReadValue('Animal_Lore')
    WAIT(1000)
    VAR after = ReadValue('Animal Lore')
    UO.Print(CStr(after - before))
END SUB

SUB ReadValue(selector)
    RETURN UO.GetSkillCap(selector)
END SUB
```

**매개변수 및 실행 설명:**

- Main 뒤에 보조 함수 전체가 나옵니다. selector는 기술/능력치, mode는 쓰기 모드입니다. ReadValue/ReadMode는 원래 숫자를 반환합니다. ApplyMode는 인수를 검사하고 동작하며 반환값이 없습니다. WAIT(1000)은 두 조회 스냅샷을 구분합니다.
