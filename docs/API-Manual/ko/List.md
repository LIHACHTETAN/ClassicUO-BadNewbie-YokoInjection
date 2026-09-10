# List

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

List()는 순서가 있고 길이를 바꿀 수 있는 컬렉션을 만듭니다. 반환 객체를 변수에 저장하세요. items.Add는 객체 메서드이며 전역 List.Add 명령은 없습니다.

## 정확한 구문

```text
List() -> Object
List(source:Any) -> Object
```

## 매개변수

- `source` — source: 생략하면 빈 컬렉션입니다. List는 배열 또는 List, Dictionary는 Dictionary를 받습니다. 외부 컨테이너만 복사하고 중첩 참조는 공유합니다.

## 반환값

생성자는 Object:List를 반환합니다. Item/인덱스는 저장값, Count는 요소 수, IndexOf는 0부터 시작하는 위치 또는 -1을 반환합니다. Contains/Remove는 1=TRUE 또는 0=FALSE, Add/Insert/Set/RemoveAt/Clear는 Unit, ToArray는 새 Array를 반환합니다.

## 동작

- index / key: List 위치는 0부터 시작하는 정수 숫자이며 Insert는 Count()도 허용합니다. Dictionary 키는 텍스트 또는 유한 숫자입니다. 숫자 1과 1.0은 같은 키이고 텍스트 "1"은 다릅니다.
- value: 초기화된 Basic 값으로 배열이나 컬렉션도 가능합니다. Unit은 저장할 수 없습니다. 숫자 값, 대소문자를 구분하는 문자열 또는 배열/객체 참조 동일성으로 비교합니다.
- fallback: 키가 없으면 Get이 이 대체값을 반환하고 삽입하지 않습니다. fallback 식을 포함한 모든 인수는 메서드 호출 전에 계산합니다.
- Add는 끝에 추가하고 Insert는 위치 앞에 삽입하며 Set/인덱스 대입은 기존 요소를 교체합니다. Item/인덱스는 읽습니다. Remove는 첫 번째 같은 값, RemoveAt은 지정 위치, Clear는 모든 요소를 삭제합니다.
- Contains는 존재 여부를, IndexOf는 첫 일치 위치를 찾습니다. 음수, 소수, 텍스트 또는 범위 밖 인덱스는 잡을 수 있는 오류를 내고 목록을 변경하지 않습니다.
- For Each는 순서를 유지합니다. ToArray는 얕은 스냅샷입니다. 원본 목록을 수정할 때 이 스냅샷을 순회하세요.
- 직접 For Each를 실행하는 동안 Set을 포함한 변경을 하면 다음 단계에서 잡을 수 있는 오류가 발생합니다. Try/Finally는 정상적으로 종료합니다. 실패한 수정은 기존 데이터를 유지합니다.
- 별칭과 ByVal 인수는 컬렉션을 공유합니다. 복사와 스냅샷은 외부 컨테이너만 복제합니다. 인덱스 ByRef와 복합 대입은 컨테이너/키를 한 번 계산하며 변수 교체가 저장된 기록 위치를 바꾸지 않습니다.
- 로컬 스크립트 데이터입니다. 메서드는 게임 아이템을 옮기거나 네트워크를 사용하지 않습니다. 하나의 요소로 저장된 아이템 묶음은 한 위치를 차지합니다.

## 예제

### 목록 생성과 합계

```vb
# 목록 생성과 합계
#
# List()는 순서가 있고 길이를 바꿀 수 있는 컬렉션을 만듭니다. 반환 객체를 변수에 저장하세요. items.Add는 객체 메서드이며 전역 List.Add 명령은
# 없습니다.
#
# 생성자는 Object:List를 반환합니다. Item/인덱스는 저장값, Count는 요소 수, IndexOf는 0부터 시작하는 위치 또는 -1을 반환합니다.
# Contains/Remove는 1=TRUE 또는 0=FALSE, Add/Insert/Set/RemoveAt/Clear는 Unit, ToArray는 새 Array를
# 반환합니다.

Option Explicit On
Sub Main()
    # Add로 [3,7], Insert(1,5)로 [3,5,7], Set(0,2)로 [2,5,7]이 됩니다. For Each가 세 값을 더합니다. Main은 Integer
    # 14를 반환합니다.

    Var items = List()
    items.Add(3)
    items.Add(7)
    items.Insert(1, 5)
    items.Set(0, 2)
    Var total = 0
    For Each item In items
        total += item
    Next
    Return total
End Sub
```

**매개변수 및 실행 설명:**

- Add로 [3,7], Insert(1,5)로 [3,5,7], Set(0,2)로 [2,5,7]이 됩니다. For Each가 세 값을 더합니다. Main은 Integer 14를 반환합니다.

### 독립 복사와 스냅샷

```vb
# 독립 복사와 스냅샷
#
# List()는 순서가 있고 길이를 바꿀 수 있는 컬렉션을 만듭니다. 반환 객체를 변수에 저장하세요. items.Add는 객체 메서드이며 전역 List.Add 명령은
# 없습니다.
#
# 생성자는 Object:List를 반환합니다. Item/인덱스는 저장값, Count는 요소 수, IndexOf는 0부터 시작하는 위치 또는 -1을 반환합니다.
# Contains/Remove는 1=TRUE 또는 0=FALSE, Add/Insert/Set/RemoveAt/Clear는 Unit, ToArray는 새 Array를
# 반환합니다.

Option Explicit On
Sub Main()
    # seed=[4,6]입니다. copied와 snapshot은 값을 유지합니다. 원본은 [9,6]이 되고 Remove(6)는 TRUE=1을 반환합니다.
    # RemoveAt(0)으로 비워지고 Clear 후에도 비어 있습니다. Main은 4*100+6*10+1+0, Integer 461을 반환합니다.

    Dim seed[1]
    seed[0] = 4
    seed[1] = 6
    Var items = List(seed)
    Var copied = List(items)
    Var snapshot = items.ToArray()
    items[0] = 9
    Var removed = items.Remove(6)
    items.RemoveAt(0)
    items.Clear()
    Return snapshot[0]*100 + copied[1]*10 + removed + items.Count()
End Sub
```

**매개변수 및 실행 설명:**

- seed=[4,6]입니다. copied와 snapshot은 값을 유지합니다. 원본은 [9,6]이 되고 Remove(6)는 TRUE=1을 반환합니다. RemoveAt(0)으로 비워지고 Clear 후에도 비어 있습니다. Main은 4*100+6*10+1+0, Integer 461을 반환합니다.

### 검색과 ByRef 수정

```vb
# 검색과 ByRef 수정
#
# List()는 순서가 있고 길이를 바꿀 수 있는 컬렉션을 만듭니다. 반환 객체를 변수에 저장하세요. items.Add는 객체 메서드이며 전역 List.Add 명령은
# 없습니다.
#
# 생성자는 Object:List를 반환합니다. Item/인덱스는 저장값, Count는 요소 수, IndexOf는 0부터 시작하는 위치 또는 -1을 반환합니다.
# Contains/Remove는 1=TRUE 또는 0=FALSE, Add/Insert/Set/RemoveAt/Clear는 Unit, ToArray는 새 Array를
# 반환합니다.

Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    # NextIndex는 한 번 실행되어 calls=1, 인덱스 0입니다. Bump가 5를 6으로 바꿉니다. Contains(6)=TRUE, IndexOf(6)=0,
    # Item(0)은 6입니다. Main은 Integer 601을 반환합니다.

    Var items = List()
    items.Add(5)
    Var calls = 0
    Bump(items[NextIndex(calls)])
    If items.Contains(6) AndAlso items.IndexOf(6) = 0 Then
        Return items.Item(0)*100 + calls
    End If
    Return -1
End Sub
```

**매개변수 및 실행 설명:**

- NextIndex는 한 번 실행되어 calls=1, 인덱스 0입니다. Bump가 5를 6으로 바꿉니다. Contains(6)=TRUE, IndexOf(6)=0, Item(0)은 6입니다. Main은 Integer 601을 반환합니다.
