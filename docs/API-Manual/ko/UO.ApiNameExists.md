# UO.ApiNameExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

호출 가능한 네이티브 이름 등록을 검사합니다.

## 정확한 구문

```text
UO.ApiNameExists(name:String) -> Integer
```

## 매개변수

- `name` — 필수 String: 호출 표현식이 아닌 정확한 등록 이름입니다. 대소문자와 양끝 공백은 무시하며 UO.를 추가하지 않습니다. 빈 이름/미등록 이름은 0, 사용자 프로시저는 제외합니다.

## 반환값

등록되어 있으면 Integer 1, 아니면 0입니다. TRUE/FALSE 또는 1/0과 비교할 수 있습니다. 게임 객체, 작업 성공, 서버 권한을 보장하지 않습니다.

## 동작

- 대소문자를 구분하지 않습니다. InjectionApi는 접두사 없는 Basic을, InjectionApiUO는 UO.가 있는 게임 호출을 등록합니다. 이전 짧은 호출에는 SC005와 등록된 UO. 대안이 표시되며 자동 실행하지 않습니다. 캐릭터 속성 값도 UO.가 필요합니다. ApiNameExists, ApiSignatureExists, ApiParameterExists는 양끝 공백을 제거하고 접두사를 추가하지 않은 정확한 등록 이름을 검사합니다. 서버 상태가 아닌 메타데이터 검사입니다. VB.NET 리플렉션 연산자 GetType(TypeName)은 구현되지 않았습니다.

## 예제

### UO.ApiNameExists — 1

```vb
# UO.ApiNameExists — 1
#
# 호출 가능한 네이티브 이름 등록을 검사합니다.
#
# 등록되어 있으면 Integer 1, 아니면 0입니다. TRUE/FALSE 또는 1/0과 비교할 수 있습니다. 게임 객체, 작업 성공, 서버 권한을 보장하지 않습니다.

SUB Main()
    # 예제 1은 명시적 UO. 게임 이름을 검사하여 1을 반환합니다. 정확한 이름과 필요한 인수 개수가 호출에 표시됩니다.

    RETURN UO.ApiNameExists('UO.GetType')
END SUB
```

**매개변수 및 실행 설명:**

- 예제 1은 명시적 UO. 게임 이름을 검사하여 1을 반환합니다. 정확한 이름과 필요한 인수 개수가 호출에 표시됩니다.

### UO.ApiNameExists — 2

```vb
# UO.ApiNameExists — 2
#
# 호출 가능한 네이티브 이름 등록을 검사합니다.
#
# 등록되어 있으면 Integer 1, 아니면 0입니다. TRUE/FALSE 또는 1/0과 비교할 수 있습니다. 게임 객체, 작업 성공, 서버 권한을 보장하지 않습니다.

SUB Main()
    # 예제 2는 Basic 또는 선택기를 검사합니다. Int(value)는 있고 Int()는 없으며 backpack은 선택기입니다. 호출에 따라 1 또는 "1:0"입니다.

    VAR name = 'CInt'
    RETURN UO.ApiNameExists(name)
END SUB
```

**매개변수 및 실행 설명:**

- 예제 2는 Basic 또는 선택기를 검사합니다. Int(value)는 있고 Int()는 없으며 backpack은 선택기입니다. 호출에 따라 1 또는 "1:0"입니다.

### UO.ApiNameExists — 3

```vb
# UO.ApiNameExists — 3
#
# 호출 가능한 네이티브 이름 등록을 검사합니다.
#
# 등록되어 있으면 Integer 1, 아니면 0입니다. TRUE/FALSE 또는 1/0과 비교할 수 있습니다. 게임 객체, 작업 성공, 서버 권한을 보장하지 않습니다.

SUB Main()
    # 예제 3은 도우미 전체를 정의하여 삭제된 짧은 이름이나 미지원 인수 개수를 유효한 형태와 비교합니다. name, first, second, count는 이름/개수를
    # 그대로 전달합니다. 호출 검사는 0, 값 검사는 "0:1"을 반환합니다.

    RETURN HasBoth('GetType','UO.GetType')
END SUB

FUNCTION HasBoth(first,second)
    RETURN UO.ApiNameExists(first) AndAlso UO.ApiNameExists(second)
END FUNCTION
```

**매개변수 및 실행 설명:**

- 예제 3은 도우미 전체를 정의하여 삭제된 짧은 이름이나 미지원 인수 개수를 유효한 형태와 비교합니다. name, first, second, count는 이름/개수를 그대로 전달합니다. 호출 검사는 0, 값 검사는 "0:1"을 반환합니다.
