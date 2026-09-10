# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

각 항목의 cliloc ID와 치환 매개변수를 포함한 객체의 구조화된 속성을 읽습니다.

## 정확한 구문

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## 매개변수

- `ObjID` — 필수 객체 serial이며 graphic/type 또는 cliloc ID가 아닙니다. 정수, 10진수·16진수 문자열, self, backpack, lasttarget, finditem, AddObject 이름을 받습니다. 0은 객체 없음을 뜻합니다.

## 반환값

Array<Array>: 각 행은 [clilocID:Integer, parameters:Array<String>]입니다. rows[i][0]은 메시지 ID, rows[i][1]은 매개변수 배열입니다. GetArrayLength(rows)는 속성 개수입니다. 수신된 기록이 없거나 ObjID=0이면 빈 배열을 반환합니다. 객체 serial 목록이 아닙니다.

## 동작

- 캐시 데이터는 즉시 반환합니다. OPL이 없으면 요청 후 최대 120밀리초 기다립니다. 프로시저 취소는 대기를 중단합니다. 이미 알려진 빈 OPL은 즉시 반환합니다.
- BASIC 배열로 TClilocRec를 표현합니다. Count는 GetArrayLength(rows), Items는 각 행입니다. 앞쪽 전송용 탭은 건너뛰고 중간의 빈 매개변수 위치는 유지합니다. #숫자는 현지화용 문자열로 남습니다. 매개변수가 없으면 빈 배열입니다. 반환값을 수정해도 클라이언트 캐시는 바뀌지 않습니다.
- https://stealth.od.ua/api/GetTooltipRec/

## 예제

### 속성 ID 나열

```vb
# 속성 ID 나열
#
# 각 항목의 cliloc ID와 치환 매개변수를 포함한 객체의 구조화된 속성을 읽습니다.
#
# Array<Array>: 각 행은 [clilocID:Integer, parameters:Array<String>]입니다. rows[i][0]은 메시지 ID,
# rows[i][1]은 매개변수 배열입니다. GetArrayLength(rows)는 속성 개수입니다. 수신된 기록이 없거나 ObjID=0이면 빈 배열을 반환합니다. 객체
# serial 목록이 아닙니다.

SUB Main()
    # ObjID=lasttarget으로 객체를 선택합니다. i는 0부터 시작하며 row[0]은 cliloc ID입니다. 빈 배열에서는 반복문을 실행하지 않습니다.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**매개변수 및 실행 설명:**

- ObjID=lasttarget으로 객체를 선택합니다. i는 0부터 시작하며 row[0]은 cliloc ID입니다. 빈 배열에서는 반복문을 실행하지 않습니다.

### 각 속성 번역

```vb
# 각 속성 번역
#
# 각 항목의 cliloc ID와 치환 매개변수를 포함한 객체의 구조화된 속성을 읽습니다.
#
# Array<Array>: 각 행은 [clilocID:Integer, parameters:Array<String>]입니다. rows[i][0]은 메시지 ID,
# rows[i][1]은 매개변수 배열입니다. GetArrayLength(rows)는 속성 개수입니다. 수신된 기록이 없거나 ObjID=0이면 빈 배열을 반환합니다. 객체
# serial 목록이 아닙니다.

SUB Main()
    # GetClilocByID에 ClilocID=row[0], Params=row[1]을 순서대로 전달합니다. 전체 행을 Params로 전달하지 마세요.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR text = UO.GetClilocByID(row[0], row[1])
        UO.Print(text)
        i = i + 1
    WEND
END SUB
```

**매개변수 및 실행 설명:**

- GetClilocByID에 ClilocID=row[0], Params=row[1]을 순서대로 전달합니다. 전체 행을 Params로 전달하지 마세요.

### 숫자 매개변수 읽기

```vb
# 숫자 매개변수 읽기
#
# 각 항목의 cliloc ID와 치환 매개변수를 포함한 객체의 구조화된 속성을 읽습니다.
#
# Array<Array>: 각 행은 [clilocID:Integer, parameters:Array<String>]입니다. rows[i][0]은 메시지 ID,
# rows[i][1]은 매개변수 배열입니다. GetArrayLength(rows)는 속성 개수입니다. 수신된 기록이 없거나 ObjID=0이면 빈 배열을 반환합니다. 객체
# serial 목록이 아닙니다.

SUB Main()
    # wanted=1060401은 예시 속성 ID이므로 바꾸세요. args[0]은 String입니다. Val 전에 길이와 IsNumeric을 확인하세요. 매개변수가 텍스트나
    # #cliloc일 수도 있습니다.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR wanted = 1060401
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR args = row[1]
        IF row[0] = wanted AND GetArrayLength(args) > 0 THEN
            IF IsNumeric(args[0]) THEN
                UO.Print('Value: ' + STR(Val(args[0])))
            END IF
        END IF
        i = i + 1
    WEND
END SUB
```

**매개변수 및 실행 설명:**

- wanted=1060401은 예시 속성 ID이므로 바꾸세요. args[0]은 String입니다. Val 전에 길이와 IsNumeric을 확인하세요. 매개변수가 텍스트나 #cliloc일 수도 있습니다.
