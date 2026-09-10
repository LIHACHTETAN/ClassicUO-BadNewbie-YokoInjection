# Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

Int(value)는 Basic 숫자를 음의 무한대 방향으로 내림합니다.

## 정확한 구문

```text
Int(value:Any) -> Integer
```

## 매개변수

- `value` — Integer/Decimal 또는 숫자 문자열 하나가 필수입니다. 소수점은 표시 언어와 관계없이 점입니다. 잘못된 문자열, Array, Object, Unit은 0으로 변환되므로 IsNumeric으로 입력을 확인하세요.

## 반환값

Integer: floor(value)입니다. 예: 2.9 -> 2, -2.9 -> -3. 내림한 값은 부호 있는 Int32 범위에 있어야 하며 비유한 값이나 범위 밖 입력을 사용하지 마세요.

## 동작

- 둘 다 게임 조회 없이 로컬에서 계산합니다. 인수를 생략하면 오류입니다. 능력치는 Int()/Str()가 아닌 UO.Int()/UO.Str()로 읽습니다. Int는 BasicDouble과 Math.Floor를 사용하고 Str는 종류에 맞는 InternalSubrutines.Str와 고정 문화권 형식을 사용합니다.

## 예제

### Int — 1

```vb
# Int — 1
#
# Int(value)는 Basic 숫자를 음의 무한대 방향으로 내림합니다.
#
# Integer: floor(value)입니다. 예: 2.9 -> 2, -2.9 -> -3. 내림한 값은 부호 있는 Int32 범위에 있어야 하며 비유한 값이나 범위 밖
# 입력을 사용하지 마세요.

SUB Main()
    # value=2.9입니다. 내림 결과 Integer 2를 Main이 반환합니다.

    RETURN Int(2.9)
END SUB
```

**매개변수 및 실행 설명:**

- value=2.9입니다. 내림 결과 Integer 2를 Main이 반환합니다.

### Int — 2

```vb
# Int — 2
#
# Int(value)는 Basic 숫자를 음의 무한대 방향으로 내림합니다.
#
# Integer: floor(value)입니다. 예: 2.9 -> 2, -2.9 -> -3. 내림한 값은 부호 있는 Int32 범위에 있어야 하며 비유한 값이나 범위 밖
# 입력을 사용하지 마세요.

SUB Main()
    # value=-2.9입니다. 내림은 -3이며 0 방향 버림이라면 -2입니다. Main은 Integer -3을 반환합니다.

    VAR value = -2.9
    RETURN Int(value)
END SUB
```

**매개변수 및 실행 설명:**

- value=-2.9입니다. 내림은 -3이며 0 방향 버림이라면 -2입니다. Main은 Integer -3을 반환합니다.

### Int — 3

```vb
# Int — 3
#
# Int(value)는 Basic 숫자를 음의 무한대 방향으로 내림합니다.
#
# Integer: floor(value)입니다. 예: 2.9 -> 2, -2.9 -> -3. 내림한 값은 부호 있는 Int32 범위에 있어야 하며 비유한 값이나 범위 밖
# 입력을 사용하지 마세요.

SUB Main()
    # WholeUnits는 total=27, size=5를 받습니다. size<=0이면 0, 아니면 Int(total/size)가 5.4를 내립니다. Main은 완전한 단위
    # 수 5를 반환합니다. 함수와 두 매개변수 전체가 정의되어 있습니다.

    RETURN WholeUnits(27,5)
END SUB

SUB WholeUnits(total,size)
    IF size <= 0 THEN
        RETURN 0
    END IF
    RETURN Int(total/size)
END SUB
```

**매개변수 및 실행 설명:**

- WholeUnits는 total=27, size=5를 받습니다. size<=0이면 0, 아니면 Int(total/size)가 5.4를 내립니다. Main은 완전한 단위 수 5를 반환합니다. 함수와 두 매개변수 전체가 정의되어 있습니다.
