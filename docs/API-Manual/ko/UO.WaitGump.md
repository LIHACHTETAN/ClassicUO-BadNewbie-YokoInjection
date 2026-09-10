# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

일회성 버튼 응답을 순서대로 등록합니다. 스크립트는 즉시 계속되며 창이 없어도 30초 동안 멈추지 않습니다.

## 정확한 구문

```text
UO.WaitGump(Value:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any, trigger16:Any) -> Unit
UO.WaitGump(triggerId:Integer) -> Unit
UO.WaitGump(triggerId:String) -> Unit
```

## 매개변수

- `triggerId` — Integer ButtonID 또는 숫자 String입니다. 한 문자열에 | 또는 쉼표로 순서를 지정할 수 있습니다. 2..16개 인수 형식에서는 배열과 중첩 순서도 허용됩니다. 등록 전에 모든 ID를 해석합니다. 빈 순서, 클라이언트 전체에서 대기 버튼 256개 초과, 중첩 32단계 초과는 부분 등록 없이 오류를 냅니다.
- `Value` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger1` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger2` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger3` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger4` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger5` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger6` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger7` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger8` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger9` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger10` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger11` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger12` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger13` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger14` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger15` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.
- `trigger16` — 순서 요소: Integer ButtonID, 숫자 String, |/쉼표로 구분한 문자열 또는 해당 요소의 Array입니다. 왼쪽부터 triggerId의 제한과 규칙을 적용합니다. Value는 단일 Any 매개변수 이름이며 배열도 받습니다.

## 반환값

Unit — 반환값이 없습니다. 성공 여부, 새 값, 서버 확인 중 어느 것도 반환하지 않습니다.

## 동작

- 해당 ButtonID를 가진 실제 Activate 버튼이 필요합니다. 페이지 전환과 일치하지 않는 창은 건너뜁니다. 뒤의 ID가 첫 대기 ID보다 먼저 실행되지 않습니다. 레이아웃 수신마다 창당 최대 한 번 응답합니다. 재구성 시 같은 창 오브젝트를 사용할 수 있습니다.
- 같은 스크립트의 다음 WaitGump는 기존 대기 순서에 추가됩니다. GumpID로 제한하지 않으므로 정확한 선택에는 NumGumpButton 또는 SendGumpSelect를 사용하세요. ButtonID=0도 실제 ID 0의 Activate 버튼이 필요하며 모든 창을 닫는 지정이 아닙니다.
- 프로시저가 정상 종료되어도 대기 작업은 남습니다. 소유자 취소 또는 이름을 지정한 Terminate는 해당 작업을 지웁니다. TerminateAll은 종료된 프로시저가 남긴 작업도 모두 지웁니다. 월드 변경 시에도 큐를 비웁니다. 프로필에는 저장하지 않습니다.

## 예제

### 한 번 응답

```vb
# 한 번 응답
#
# 일회성 버튼 응답을 순서대로 등록합니다. 스크립트는 즉시 계속되며 창이 없어도 30초 동안 멈추지 않습니다.
#
# Unit — 반환값이 없습니다. 성공 여부, 새 값, 서버 확인 중 어느 것도 반환하지 않습니다.

SUB Main()
    # 100은 응답 ButtonID입니다. WaitGump는 UseObject 전에 등록합니다. 스크립트가 계속된다고 서버가 응답을 확인했다는 뜻은 아닙니다.

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**매개변수 및 실행 설명:**

- 100은 응답 ButtonID입니다. WaitGump는 UseObject 전에 등록합니다. 스크립트가 계속된다고 서버가 응답을 확인했다는 뜻은 아닙니다.

### 여러 단계

```vb
# 여러 단계
#
# 일회성 버튼 응답을 순서대로 등록합니다. 스크립트는 즉시 계속되며 창이 없어도 30초 동안 멈추지 않습니다.
#
# Unit — 반환값이 없습니다. 성공 여부, 새 값, 서버 확인 중 어느 것도 반환하지 않습니다.

SUB Main()
    # 7, 22, 1은 연속된 양식의 ButtonID이며 이 순서로 확인합니다. 인수 개수는 지연 시간이 아니며 호출이 전체 순서를 등록합니다.

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**매개변수 및 실행 설명:**

- 7, 22, 1은 연속된 양식의 ButtonID이며 이 순서로 확인합니다. 인수 개수는 지연 시간이 아니며 호출이 전체 순서를 등록합니다.

### 대기 취소

```vb
# 대기 취소
#
# 일회성 버튼 응답을 순서대로 등록합니다. 스크립트는 즉시 계속되며 창이 없어도 30초 동안 멈추지 않습니다.
#
# Unit — 반환값이 없습니다. 성공 여부, 새 값, 서버 확인 중 어느 것도 반환하지 않습니다.

SUB Main()
    # 7|22|1 문자열은 같은 순서를 지정합니다. 이후 TerminateAll은 모든 검프 대기 작업을 지우고 모든 프로시저를 중지합니다. 전체에 적용됩니다.

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**매개변수 및 실행 설명:**

- 7|22|1 문자열은 같은 순서를 지정합니다. 이후 TerminateAll은 모든 검프 대기 작업을 지우고 모든 프로시저를 중지합니다. 전체에 적용됩니다.
