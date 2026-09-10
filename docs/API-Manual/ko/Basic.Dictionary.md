# Dictionary

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

Dictionary()는 키 → 값 컬렉션을 만듭니다. 반환 객체의 메서드를 사용합니다. 숫자 키와 문자열 키, "ore"와 "Ore"는 서로 다릅니다.

## 정확한 구문

```text
Dictionary() -> Object:Dictionary
Dictionary(source:Dictionary) -> Object:Dictionary
values.Add(key:String/Number, value:Any) -> Unit
values.Item(key:String/Number) -> Any
values[key] = value
values.Set(key:String/Number, value:Any) -> Unit
values.Get(key:String/Number, fallback:Any) -> Any
values.Count() -> Integer
values.ContainsKey(key:String/Number) -> Integer:1/0
values.Remove(key:String/Number) -> Integer:1/0
values.Clear() -> Unit
values.Keys() -> Array
values.Values() -> Array
entry.Key() -> String/Number
entry.Value() -> Any
```

## 매개변수

- `source` — source: 생략하면 빈 컬렉션입니다. List는 배열 또는 List, Dictionary는 Dictionary를 받습니다. 외부 컨테이너만 복사하고 중첩 참조는 공유합니다.
- `index / key` — index / key: List 위치는 0부터 시작하는 정수 숫자이며 Insert는 Count()도 허용합니다. Dictionary 키는 텍스트 또는 유한 숫자입니다. 숫자 1과 1.0은 같은 키이고 텍스트 "1"은 다릅니다.
- `value` — value: 초기화된 Basic 값으로 배열이나 컬렉션도 가능합니다. Unit은 저장할 수 없습니다. 숫자 값, 대소문자를 구분하는 문자열 또는 배열/객체 참조 동일성으로 비교합니다.
- `fallback` — fallback: 키가 없으면 Get이 이 대체값을 반환하고 삽입하지 않습니다. fallback 식을 포함한 모든 인수는 메서드 호출 전에 계산합니다.

## 반환값

생성자는 Object:Dictionary를 반환합니다. Item/인덱스/Get은 값, Count는 키 수를 반환합니다. ContainsKey/Remove는 1=TRUE 또는 0=FALSE, Add/Set/Clear는 Unit, Keys/Values는 새 Array를 반환합니다. For Each는 항목 객체를 내보내며 Key()는 키, Value()는 값을 반환합니다.

## 동작

- Add는 기존 키를 덮어쓰지 않고 거부합니다. Set/인덱스 대입은 생성 또는 교체하며 Item/인덱스 읽기에는 기존 키가 필요합니다. Get은 대체값을 사용합니다. Remove는 키가 없으면 0을 반환하고 Clear는 비웁니다.
- NaN, 무한대, 배열, 객체, Unit은 키가 될 수 없습니다. 키 순서는 보장되지 않습니다. 각 항목은 자신의 키/값 쌍을 유지하며 다음 반복으로 넘어가도 바뀌지 않습니다.
- Keys/Values는 얕은 스냅샷을 만듭니다. 삭제/교체하려면 Keys()를 순회하세요. 사전을 직접 순회하면 항목 객체를 얻습니다.
- 직접 For Each를 실행하는 동안 Set을 포함한 변경을 하면 다음 단계에서 잡을 수 있는 오류가 발생합니다. Try/Finally는 정상적으로 종료합니다. 실패한 수정은 기존 데이터를 유지합니다.
- 별칭과 ByVal 인수는 컬렉션을 공유합니다. 복사와 스냅샷은 외부 컨테이너만 복제합니다. 인덱스 ByRef와 복합 대입은 컨테이너/키를 한 번 계산하며 변수 교체가 저장된 기록 위치를 바꾸지 않습니다.
- 로컬 스크립트 데이터입니다. 메서드는 게임 아이템을 옮기거나 네트워크를 사용하지 않습니다. 하나의 요소로 저장된 아이템 묶음은 한 위치를 차지합니다.

## 예제

### 1. 키 형식과 대체값

```vb
# "ore"는 5에서 8로 바뀝니다. 숫자 키 1은 2, 텍스트 "1"은 3을 저장합니다. Get("wood",7)은 삽입하지 않고 7을 반환합니다. Main은 8*100+2*10+3+7, Integer 830을 반환합니다.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**매개변수 및 실행 설명:**

"ore"는 5에서 8로 바뀝니다. 숫자 키 1은 2, 텍스트 "1"은 3을 저장합니다. Get("wood",7)은 삽입하지 않고 7을 반환합니다. Main은 8*100+2*10+3+7, Integer 830을 반환합니다.

### 2. 항목, 스냅샷, 삭제

```vb
# 두 값의 합은 5입니다. Keys()로 순회 중 삭제할 수 있습니다. copied는 ore=2, snapshot은 두 값을 유지합니다. Clear 후 Count()=0입니다. Main은 5*100+2*10+2+0, Integer 522를 반환합니다.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 2)
    values.Add("wood", 3)
    Var copied = Dictionary(values)
    Var snapshot = values.Values()
    Var total = 0
    For Each entry In values
        If values.ContainsKey(entry.Key()) Then
            total += entry.Value()
        End If
    Next
    For Each key In values.Keys()
        values.Remove(key)
    Next
    values.Clear()
    Return total*100 + copied["ore"]*10 + GetArrayLength(snapshot) + values.Count()
End Sub
```

**매개변수 및 실행 설명:**

두 값의 합은 5입니다. Keys()로 순회 중 삭제할 수 있습니다. copied는 ore=2, snapshot은 두 값을 유지합니다. Clear 후 Count()=0입니다. Main은 5*100+2*10+2+0, Integer 522를 반환합니다.

### 3. 중복 키 처리

```vb
# 첫 Add가 ore=4를 저장합니다. 두 번째 값 7은 오류가 되어 Catch가 caught=1을 설정합니다. ore=4는 보존됩니다. Main은 4*10+1, Integer 41을 반환합니다.
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 4)
    Var caught = 0
    Try
        values.Add("ore", 7)
    Catch problem
        caught = 1
    End Try
    Return values["ore"]*10 + caught
End Sub
```

**매개변수 및 실행 설명:**

첫 Add가 ore=4를 저장합니다. 두 번째 값 7은 오류가 되어 Catch가 caught=1을 설정합니다. ore=4는 보존됩니다. Main은 4*10+1, Integer 41을 반환합니다.

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/DictionaryObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-8.0
-->
