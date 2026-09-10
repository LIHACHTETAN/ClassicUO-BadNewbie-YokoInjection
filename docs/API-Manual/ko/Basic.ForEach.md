# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

For Each는 숫자 인덱스 없이 배열이나 열거 가능한 네이티브 컬렉션의 요소를 순서대로 읽습니다. 프로시저나 함수 안의 반복문이며 API 함수 호출이 아닙니다.

## 정확한 구문

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## 매개변수

- `item` — item: 반복 변수입니다. 기존 지역 변수, 매개변수 또는 접근 가능한 필드를 재사용하며 없으면 Option Explicit On에서도 지역 변수를 만듭니다. 상수에는 쓸 수 없습니다.
- `type` — type: 선택적인 AS type으로 Integer 등이 가능합니다. 지역 반복 변수를 선언하고 요소마다 변환합니다. AS가 없으면 기존 변수의 형식을 유지합니다.
- `collection` — collection: 진입할 때 한 번 평가하는 식입니다. 배열 또는 열거 가능한 네이티브 객체를 받으며 스칼라는 오류입니다. 중첩 배열은 먼저 행을 반환하므로 셀에는 안쪽 반복문을 씁니다.
- `statements / NEXT item` — statements / NEXT item: 본문과 끝입니다. NEXT 뒤 이름은 생략할 수 있지만 쓰면 반복 변수와 같아야 합니다. NEXT는 별도 줄에 씁니다.

## 반환값

For Each와 Next는 값을 반환하지 않습니다. item은 요소 값을 받으며 자동으로 인덱스, ID, 묶음 수량을 받는 것이 아닙니다. 본문의 RETURN은 함수 전체를 끝냅니다. 예제는 Integer 12, 105, 10을 반환합니다.

## 동작

- 준비 단계에서 초기화 전에 FOR EACH와 NEXT를 연결하며 잘못된 연결은 SC020입니다. collection을 한 번 평가한 뒤 참조와 별도 커서를 저장합니다. item을 변경해도 커서는 움직이지 않습니다.
- 배열은 인덱스 오름차순으로 읽습니다. 빈 배열은 본문을 건너뛰고 AS 없는 기존 변수 값을 유지합니다. 초기화되지 않은 요소나 AS 변환 실패는 잡을 수 있는 오류입니다.
- item 대입은 배열 요소를 교체하지 않습니다. 중첩 배열과 객체는 참조이므로 row 셀 수정은 해당 행을 바꿉니다. collection 재대입은 현재 열거 대상을 바꾸지 않으며 같은 배열의 다음 요소 수정은 읽을 때 반영됩니다.
- Continue For는 가장 가까운 For 또는 For Each의 다음 반복으로, Exit For는 그 밖으로 이동합니다. 오류, RETURN, 취소는 네이티브 열거자를 해제합니다. 컬렉션이 열거 중 수정을 금지할 수 있으며 자동 복사본은 없습니다.
- 반복 변수는 종료 후에도 프로시저 안에서 마지막 값을 유지합니다. 각 실행은 독립된 커서를 가집니다. IDE 이름 완성, 반복문 템플릿, 선언 이동과 일시 정지·중지가 지원됩니다.

## 예제

### 1. 인덱스 없는 합계

```vb
# values[2]에는 2, 4, 6 세 요소가 있습니다. SumItems는 배열을 받고 item은 각 숫자를 받습니다. total은 0에서 12가 되며 RETURN은 Integer 12를 Main에 전달합니다. NEXT item은 해당 반복을 닫습니다.
Option Explicit On
Function SumItems(values)
    Var total = 0
    For Each item In values
        total += item
    Next item
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return SumItems(values)
End Sub
```

**매개변수 및 실행 설명:**

values[2]에는 2, 4, 6 세 요소가 있습니다. SumItems는 배열을 받고 item은 각 숫자를 받습니다. total은 0에서 12가 되며 RETURN은 Integer 12를 Main에 전달합니다. NEXT item은 해당 반복을 닫습니다.

### 2. 한 번 평가하고 변환

```vb
# SelectItems는 calls를 ByRef로 받아 1로 늘리고 ["2", "3"]을 반환합니다. AS Integer가 2, 3으로 변환하여 total=5입니다. item=100은 원본이나 순서를 바꾸지 않습니다. Main은 calls*100+total인 Integer 105를 반환합니다.
Option Explicit On
Function SelectItems(ByRef calls)
    calls += 1
    Dim values[1]
    values[0] = "2"
    values[1] = "3"
    Return values
End Function
Sub Main()
    Var calls = 0
    Var total = 0
    For Each item As Integer In SelectItems(calls)
        total += item
        item = 100
    Next
    Return calls * 100 + total
End Sub
```

**매개변수 및 실행 설명:**

SelectItems는 calls를 ByRef로 받아 1로 늘리고 ["2", "3"]을 반환합니다. AS Integer가 2, 3으로 변환하여 total=5입니다. item=100은 원본이나 순서를 바꾸지 않습니다. Main은 calls*100+total인 Integer 105를 반환합니다.

### 3. 중첩 배열

```vb
# rows[1][1]은 두 행에 각각 두 셀이 있습니다. row는 행 참조, cell은 1, 2, 3, 4를 받습니다. 각 NEXT가 자기 반복문을 닫습니다. SumGrid와 Main은 Integer 10을 반환하며 ID나 수량을 자동 추론하지 않습니다.
Option Explicit On
Function SumGrid(rows)
    Var total = 0
    For Each row In rows
        For Each cell In row
            total += cell
        Next cell
    Next row
    Return total
End Function
Sub Main()
    Dim rows[1][1]
    rows[0][0] = 1
    rows[0][1] = 2
    rows[1][0] = 3
    rows[1][1] = 4
    Return SumGrid(rows)
End Sub
```

**매개변수 및 실행 설명:**

rows[1][1]은 두 행에 각각 두 셀이 있습니다. row는 행 참조, cell은 1, 2, 3, 4를 받습니다. 각 NEXT가 자기 반복문을 닫습니다. SumGrid와 Main은 Integer 10을 반환하며 ID나 수량을 자동 추론하지 않습니다.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
