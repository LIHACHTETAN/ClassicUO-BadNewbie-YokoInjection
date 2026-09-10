# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

DIM은 동적 배열을 만들고 REDIM은 저장 공간을 교체합니다. PRESERVE는 겹치는 인덱스의 값을 복사합니다. 차원에는 개수가 아닌 포함되는 상한을 지정합니다. 읽기 전에 요소를 초기화하세요.

## 정확한 구문

```text
DIM name[upper]
DIM name(upper) AS type
DIM grid[xUpper][yUpper]
DIM grid(xUpper, yUpper)
REDIM name[upper]
REDIM PRESERVE name[upper]
name[index] = value
GetArrayLength(name)
```

## 매개변수

- `name` — name: 배열 변수. DIM은 선언하고 REDIM은 기존 변수의 저장 공간을 바꿉니다. items[i], grid[x][y]로 읽고 씁니다.
- `upper` — upper: Integer로 변환되는 식이며 왼쪽부터 각각 한 번 계산됩니다. DIM items[2]는 0..2의 세 칸을 만듭니다. -1은 빈 차원입니다. 더 작은 상한과 길이 오버플로는 오류이며 실제 크기는 메모리에도 제한됩니다.
- `PRESERVE` — PRESERVE: REDIM의 선택 키워드. 겹치는 인덱스를 재귀적으로 복사합니다. 줄이면 새 범위 밖의 값은 없어집니다. 생략하면 새 칸은 초기화되지 않습니다.
- `AS type` — AS type: DIM 배열 선언에서 허용하는 주석 성격의 표기로, 요소의 형식 지정·초기화·변환을 하지 않습니다. 서로 다른 종류의 값을 함께 저장할 수 있습니다.

## 반환값

DIM과 REDIM은 값을 반환하지 않습니다(Unit). items[i]는 저장 값과 실제 종류 Integer, Decimal, String, Array 또는 Object를 반환합니다. 초기화되지 않은 칸을 읽으면 0이나 FALSE 대신 오류가 발생합니다. GetArrayLength(array)는 바깥 길이를 Integer로 반환하며 배열이 아닌 값에는 0을 반환합니다.

## 동작

- DIM grid(1, 2)는 grid[1][2], 즉 두 행에 각각 세 칸을 뜻합니다. 상한 안의 함수 호출은 유지됩니다. 접근은 grid[1][2]로 하며 식의 소괄호는 함수 호출입니다.
- 대입과 ByVal 전달은 요소가 아닌 참조를 복사합니다. 별칭에서도 공유 칸의 변경이 보입니다. REDIM은 새 배열을 연결하고 기존 별칭은 이전 배열을 유지합니다. PRESERVE는 중첩 배열의 겹치는 좌표를 복사하지만 임의 객체를 완전히 깊은 복사하지는 않습니다.
- 인덱스는 0부터 시작합니다. DIM items[2]=5 같은 DIM/REDIM 초기화 식은 SC014로 거부됩니다. 각 칸을 별도 줄에서 대입하세요. 잘못된 인덱스, 없는 요소 및 초기화되지 않은 읽기는 처리 가능한 오류입니다.
- 이 Basic 방언의 동적 요소 종류와 다차원 PRESERVE는 VB.NET 형식 배열과 다릅니다. 저장된 논리 값은 1/0이지만 일반 숫자나 배열 길이는 성공 플래그가 아닙니다.
- RETURN array는 배열 참조를 반환하며 생성 함수가 끝나도 데이터는 유지됩니다. 다른 변수에 대입해도 요소를 복사하지 않습니다. 공통 함수로 Module 필드용 배열을 만들 수 있습니다. 독립 실행은 DIM을 다시 실행할 때 새 배열을 만듭니다.

## 예제

### 1. 초기화한 요소 합계

```vb
# Abs(-2)는 상한 2를 반환합니다. Main은 세 칸에 2, 4, 6을 넣습니다. Sum은 ByVal로 참조를 받고 0..GetArrayLength(items)-1을 순회하여 12를 반환합니다. 전체 보조 함수가 포함되어 있으며 요소를 바꾸지 않고 빈 배열도 처리합니다.
Option Explicit On
FUNCTION Sum(ByVal items)
    VAR total = 0
    VAR i = 0
    FOR i = 0 TO GetArrayLength(items) - 1
        total += items[i]
    NEXT
    RETURN total
END FUNCTION
SUB Main()
    DIM items(Abs(-2))
    items[0] = 2
    items[1] = 4
    items[2] = 6
    RETURN Sum(items)
END SUB
```

**매개변수 및 실행 설명:**

Abs(-2)는 상한 2를 반환합니다. Main은 세 칸에 2, 4, 6을 넣습니다. Sum은 ByVal로 참조를 받고 0..GetArrayLength(items)-1을 순회하여 12를 반환합니다. 전체 보조 함수가 포함되어 있으며 요소를 바꾸지 않고 빈 배열도 처리합니다.

### 2. 값을 유지하며 확장

```vb
# values에는 7과 8이 있습니다. REDIM PRESERVE values(2)는 세 칸을 만들고 인덱스 0, 1을 복사합니다. 새 칸 2를 9로 초기화합니다. Main은 7*100+8*10+9=789를 반환합니다.
Option Explicit On
SUB Main()
    DIM values[1]
    values[0] = 7
    values[1] = 8
    REDIM PRESERVE values(2)
    values[2] = 9
    RETURN values[0] * 100 + values[1] * 10 + values[2]
END SUB
```

**매개변수 및 실행 설명:**

values에는 7과 8이 있습니다. REDIM PRESERVE values(2)는 세 칸을 만들고 인덱스 0, 1을 복사합니다. 새 칸 2를 9로 초기화합니다. Main은 7*100+8*10+9=789를 반환합니다.

### 3. 별칭과 새 저장 공간

```vb
# grid는 두 행에 각각 두 칸입니다. alias는 같은 배열을 참조하므로 alias[0][1]=9는 grid도 바꿉니다. PRESERVE는 grid를 세 행으로 늘려 9를 보존하고 alias는 두 행을 유지합니다. "9:3:2"는 보존된 값, 새 바깥 길이, 이전 별칭의 길이입니다.
Option Explicit On
SUB Main()
    DIM grid[1][1]
    grid[0][1] = 4
    VAR alias = grid
    alias[0][1] = 9
    REDIM PRESERVE grid[2][1]
    RETURN CStr(grid[0][1]) + ":" + CStr(GetArrayLength(grid)) + ":" + CStr(GetArrayLength(alias))
END SUB
```

**매개변수 및 실행 설명:**

grid는 두 행에 각각 두 칸입니다. alias는 같은 배열을 참조하므로 alias[0][1]=9는 grid도 바꿉니다. PRESERVE는 grid를 세 행으로 늘려 9를 보존하고 alias는 두 행을 유지합니다. "9:3:2"는 보존된 값, 새 바깥 길이, 이전 별칭의 길이입니다.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
