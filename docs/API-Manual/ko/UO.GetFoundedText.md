# UO.GetFoundedText

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ko -->

이 스크립트가 선택한 저널 항목의 저장된 텍스트를 읽습니다.

## 정확한 구문

```text
UO.GetFoundedText() -> String
```

## 매개변수

매개변수가 없습니다.

## 반환값

String — 선택한 텍스트이며, 선택한 항목이 없으면 빈 문자열입니다. 실제 항목도 빈 텍스트를 가질 수 있습니다. serial, 줄 인덱스 또는 성공을 나타내는 Boolean이 아닙니다.

## 동작

- InJournal, InJournalBetweenTimes, Journal/GetJournal, LastJournalMessage는 선택을 바꿉니다. 검색 실패, 잘못된 Journal 인덱스 또는 이 스크립트의 저널 지우기는 선택을 초기화합니다. 인수가 없으며 새 검색을 하지 않습니다.
- 새 메시지는 저장된 텍스트를 바꾸지 않습니다. 항목이 삭제되거나 버퍼에서 밀려나도 텍스트는 유지되지만 GetFoundedTextIndex/LineIndex는 -1이 됩니다. 다른 스크립트가 공유 저널을 지워도 저장된 변수는 바뀌지 않습니다.

## 예제

### 찾은 메시지 읽기

```vb
# 찾은 메시지 읽기
#
# 이 스크립트가 선택한 저널 항목의 저장된 텍스트를 읽습니다.
#
# String — 선택한 텍스트이며, 선택한 항목이 없으면 빈 문자열입니다. 실제 항목도 빈 텍스트를 가질 수 있습니다. serial, 줄 인덱스 또는 성공을 나타내는
# Boolean이 아닙니다.

SUB Main()
    # needle은 대소문자를 구분하는 부분 문자열입니다. InJournal > 0을 확인하세요. 결과는 위치에 1을 더한 값이며 일치 개수가 아닙니다.

    IF UO.InJournal('needle') > 0 THEN
        VAR text = UO.GetFoundedText()
        UO.Print(text)
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- needle은 대소문자를 구분하는 부분 문자열입니다. InJournal > 0을 확인하세요. 결과는 위치에 1을 더한 값이며 일치 개수가 아닙니다.

### 선택한 줄 읽기

```vb
# 선택한 줄 읽기
#
# 이 스크립트가 선택한 저널 항목의 저장된 텍스트를 읽습니다.
#
# String — 선택한 텍스트이며, 선택한 항목이 없으면 빈 문자열입니다. 실제 항목도 빈 텍스트를 가질 수 있습니다. serial, 줄 인덱스 또는 성공을 나타내는
# Boolean이 아닙니다.

SUB Main()
    # Journal(0)은 최신 항목을 선택합니다. Print가 메시지를 추가할 수 있으므로 먼저 텍스트와 인덱스를 저장합니다. 빈 텍스트만으로 항목이 없다고 판단할 수
    # 없습니다.

    VAR latest = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR text = UO.GetFoundedText()
    IF index >= 0 THEN
        UO.Print(text)
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- Journal(0)은 최신 항목을 선택합니다. Print가 메시지를 추가할 수 있으므로 먼저 텍스트와 인덱스를 저장합니다. 빈 텍스트만으로 항목이 없다고 판단할 수 없습니다.

### 다음 검색 전에 텍스트 보관하기

```vb
# 다음 검색 전에 텍스트 보관하기
#
# 이 스크립트가 선택한 저널 항목의 저장된 텍스트를 읽습니다.
#
# String — 선택한 텍스트이며, 선택한 항목이 없으면 빈 문자열입니다. 실제 항목도 빈 텍스트를 가질 수 있습니다. serial, 줄 인덱스 또는 성공을 나타내는
# Boolean이 아닙니다.

SUB Main()
    # saved는 두 번째 검색이 선택을 바꾸기 전에 첫 결과를 복사합니다. 이후 메시지나 검색은 이 변수를 바꾸지 않습니다.

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.GetFoundedText()
        VAR another = UO.InJournal('failed')
        UO.Print(saved)
    END IF
END SUB
```

**매개변수 및 실행 설명:**

- saved는 두 번째 검색이 선택을 바꾸기 전에 첫 결과를 복사합니다. 이후 메시지나 검색은 이 변수를 바꾸지 않습니다.
