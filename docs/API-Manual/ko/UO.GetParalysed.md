# UO.GetParalysed

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

클라이언트가 현재 알고 있는 mobile의 마비 플래그를 읽습니다.

## 정확한 구문

```text
UO.GetParalysed() -> Integer
UO.GetParalysed(value:Any) -> Integer
```

## 매개변수

- `value` — 선택적 mobile serial/ID: 정수, 16진수 문자열, self, lasttarget, 다른 표준 객체 별칭 또는 AddObject 이름입니다. graphic/type이 아닙니다. 생략하면 self를 선택합니다. 해석할 수 없는 별칭은 0이 되며 타깃 커서를 열지 않습니다.

## 반환값

Integer Boolean: 로드된 mobile에 IsParalyzed가 있으면 1 = TRUE입니다. 플래그가 없거나, mobile이 알려지지 않았거나 삭제되었거나, 객체가 아이템이면 0 = FALSE입니다. 남은 마비 시간이 아니며 0이어도 이동이 가능하다는 보장은 없습니다.

## 동작

- Paralyzed로 마비 플래그를 확인합니다. Is/Get 변형, GetParalisa, Frozen, GetLocked도 같은 플래그를 읽습니다.
- 로컬 데이터 조회입니다. 마비를 걸거나 해제하지 않고, 끝날 때까지 기다리지 않으며, 서버에 갱신을 요청하지 않습니다.
- 이 판정에서는 value = TRUE, value = 1, IF value가 같습니다. TRUE/FALSE에는 따옴표를 쓰지 않습니다. 반환값은 플래그이며 수량이나 ID가 아닙니다.

## 예제

### TRUE로 자신을 확인하기

```vb
# TRUE로 자신을 확인하기
#
# 클라이언트가 현재 알고 있는 mobile의 마비 플래그를 읽습니다.
#
# Integer Boolean: 로드된 mobile에 IsParalyzed가 있으면 1 = TRUE입니다. 플래그가 없거나, mobile이 알려지지 않았거나 삭제되었거나,
# 객체가 아이템이면 0 = FALSE입니다. 남은 마비 시간이 아니며 0이어도 이동이 가능하다는 보장은 없습니다.

SUB Main()
    # 빈 괄호는 self를 선택합니다. state는 플래그의 한 시점 값을 저장하고 TRUE는 숫자 상수 1입니다.
    # FALSE라도 벽, 스태미나 부족 또는 다른 이동 방해 원인이 있을 수 있습니다.

    VAR state = UO.GetParalysed()
    IF state = TRUE THEN
        UO.Print('Paralysis flag is set')
    ELSE
        UO.Print('Paralysis flag is absent or unavailable')
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 빈 괄호는 self를 선택합니다. state는 플래그의 한 시점 값을 저장하고 TRUE는 숫자 상수 1입니다.
- FALSE라도 벽, 스태미나 부족 또는 다른 이동 방해 원인이 있을 수 있습니다.

### 선택한 mobile 확인하기

```vb
# 선택한 mobile 확인하기
#
# 클라이언트가 현재 알고 있는 mobile의 마비 플래그를 읽습니다.
#
# Integer Boolean: 로드된 mobile에 IsParalyzed가 있으면 1 = TRUE입니다. 플래그가 없거나, mobile이 알려지지 않았거나 삭제되었거나,
# 객체가 아이템이면 0 = FALSE입니다. 남은 마비 시간이 아니며 0이어도 이동이 가능하다는 보장은 없습니다.

SUB Main()
    # target은 마지막 타깃의 serial을 16진수 문자열로 저장합니다. IsNpc는 플레이어를 포함하여 로드된 mobile인지 확인합니다.
    # 인수는 저장된 target을 선택합니다. 커서를 열거나 lasttarget을 변경하지 않습니다.

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR state = UO.GetParalysed(target)
        UO.Print('Selected mobile paralysis 1/0: ' + STR(state))
    ELSE
        UO.Print('No loaded mobile selected')
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- target은 마지막 타깃의 serial을 16진수 문자열로 저장합니다. IsNpc는 플레이어를 포함하여 로드된 mobile인지 확인합니다.
- 인수는 저장된 target을 선택합니다. 커서를 열거나 lasttarget을 변경하지 않습니다.

### 제한을 두고 마비 해제 기다리기

```vb
# 제한을 두고 마비 해제 기다리기
#
# 클라이언트가 현재 알고 있는 mobile의 마비 플래그를 읽습니다.
#
# Integer Boolean: 로드된 mobile에 IsParalyzed가 있으면 1 = TRUE입니다. 플래그가 없거나, mobile이 알려지지 않았거나 삭제되었거나,
# 객체가 아이템이면 0 = FALSE입니다. 남은 마비 시간이 아니며 0이어도 이동이 가능하다는 보장은 없습니다.

SUB Main()
    # 100밀리초 대기를 최대 10회 수행합니다. 인수 없는 호출마다 self를 다시 읽습니다.
    # 반복문 뒤에는 self가 여전히 존재하는지 따로 확인합니다. 약 1초에 실행 시간을 더한 관찰일 뿐이며 회복을 보장하지 않습니다.

    VAR attempts = 0
    WHILE UO.GetParalysed() = TRUE AND attempts < 10
        WAIT(100)
        attempts = attempts + 1
    WEND
    IF UO.IsNpc('self') THEN
        IF UO.GetParalysed() = FALSE THEN
            UO.Print('Paralysis flag is clear')
        ELSE
            UO.Print('Still paralyzed')
        END IF
    ELSE
        UO.Print('Self is unavailable')
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- 100밀리초 대기를 최대 10회 수행합니다. 인수 없는 호출마다 self를 다시 읽습니다.
- 반복문 뒤에는 self가 여전히 존재하는지 따로 확인합니다. 약 1초에 실행 시간을 더한 관찰일 뿐이며 회복을 보장하지 않습니다.
