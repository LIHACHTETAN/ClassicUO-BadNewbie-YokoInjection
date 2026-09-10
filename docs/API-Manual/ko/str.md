# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

Str(value)는 Basic 스칼라 값을 문자열로 만듭니다.

## 정확한 구문

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## 매개변수

- `value` — Integer, Decimal 또는 String 하나가 필수입니다. 실제 종류에 따라 오버로드를 고릅니다. Array, Object, Unit에 맞는 Str 오버로드는 없습니다.

## 반환값

String: 언어에 독립적인 숫자 텍스트 또는 바뀌지 않은 원래 String입니다. 양수 앞에 공백을 붙이지 않습니다. 자릿수 매개변수는 없습니다.

## 동작

- 둘 다 게임 조회 없이 로컬에서 계산합니다. 인수를 생략하면 오류입니다. 능력치는 Int()/Str()가 아닌 UO.Int()/UO.Str()로 읽습니다. Int는 BasicDouble과 Math.Floor를 사용하고 Str는 종류에 맞는 InternalSubrutines.Str와 고정 문화권 형식을 사용합니다.

## 예제

### Str — 1

```vb
# Str — 1
#
# Str(value)는 Basic 스칼라 값을 문자열로 만듭니다.
#
# String: 언어에 독립적인 숫자 텍스트 또는 바뀌지 않은 원래 String입니다. 양수 앞에 공백을 붙이지 않습니다. 자릿수 매개변수는 없습니다.

SUB Main()
    # value=42는 Integer입니다. Str는 앞 공백 없는 "42"를 만들며 Main이 그 String을 반환합니다.

    RETURN Str(42)
END SUB
```

**매개변수 및 실행 설명:**

- value=42는 Integer입니다. Str는 앞 공백 없는 "42"를 만들며 Main이 그 String을 반환합니다.

### Str — 2

```vb
# Str — 2
#
# Str(value)는 Basic 스칼라 값을 문자열로 만듭니다.
#
# String: 언어에 독립적인 숫자 텍스트 또는 바뀌지 않은 원래 String입니다. 양수 앞에 공백을 붙이지 않습니다. 자릿수 매개변수는 없습니다.

SUB Main()
    # amount=-12.5는 Decimal입니다. Str는 표시 언어와 관계없이 점을 포함한 "-12.5"를 text에 저장합니다. Main은 text를 반환하고
    # amount는 숫자로 남습니다.

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**매개변수 및 실행 설명:**

- amount=-12.5는 Decimal입니다. Str는 표시 언어와 관계없이 점을 포함한 "-12.5"를 text에 저장합니다. Main은 text를 반환하고 amount는 숫자로 남습니다.

### Str — 3

```vb
# Str — 3
#
# Str(value)는 Basic 스칼라 값을 문자열로 만듭니다.
#
# String: 언어에 독립적인 숫자 텍스트 또는 바뀌지 않은 원래 String입니다. 양수 앞에 공백을 붙이지 않습니다. 자릿수 매개변수는 없습니다.

SUB Main()
    # ItemLabel은 name="ore", count=3을 받습니다. Str(name)은 이름을 유지하고 Str(count)는 "3"을 만듭니다. 함수가 " x"로
    # 연결하며 Main은 "ore x3"을 반환합니다.

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**매개변수 및 실행 설명:**

- ItemLabel은 name="ore", count=3을 받습니다. Str(name)은 이름을 유지하고 Str(count)는 "3"을 만듭니다. 함수가 " x"로 연결하며 Main은 "ore x3"을 반환합니다.
