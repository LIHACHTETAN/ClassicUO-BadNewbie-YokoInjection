# UO.GetFoundedText

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取此腳本所選日誌記錄的已儲存文字。

## 完整語法

```text
UO.GetFoundedText() -> String
```

## 參數

沒有參數。

## 傳回值

String：所選文字；未選取記錄時為空字串。存在的記錄也可能含有空文字。此值不是 serial、行索引或表示成功的 Boolean。

## 行為

- InJournal、InJournalBetweenTimes、Journal/GetJournal 和 LastJournalMessage 會替換選取記錄。搜尋失敗、Journal 索引無效或由本腳本清除日誌時，選取狀態會重設。此指令不接受參數，也不會執行新搜尋。
- 新訊息不會替換已儲存的文字。記錄遭刪除或從有限緩衝區移除後，文字仍保留，但 GetFoundedTextIndex/LineIndex 變為 -1。其他腳本可清除共用日誌；已儲存的變數不會因此改變。

## 範例

### 讀取搜尋到的訊息

```vb
# 讀取搜尋到的訊息
#
# 讀取此腳本所選日誌記錄的已儲存文字。
#
# String：所選文字；未選取記錄時為空字串。存在的記錄也可能含有空文字。此值不是 serial、行索引或表示成功的 Boolean。

SUB Main()
    # needle 是區分大小寫的子字串。請檢查 InJournal > 0：結果為位置加 1，不是符合條件的記錄數。

    IF UO.InJournal('needle') > 0 THEN
        VAR text = UO.GetFoundedText()
        UO.Print(text)
    END IF
END SUB
```

**參數與執行說明:**

- needle 是區分大小寫的子字串。請檢查 InJournal > 0：結果為位置加 1，不是符合條件的記錄數。

### 讀取已選取的行

```vb
# 讀取已選取的行
#
# 讀取此腳本所選日誌記錄的已儲存文字。
#
# String：所選文字；未選取記錄時為空字串。存在的記錄也可能含有空文字。此值不是 serial、行索引或表示成功的 Boolean。

SUB Main()
    # Journal(0) 選取最新記錄。Print 可能新增訊息，因此先儲存文字和索引。空文字本身不表示記錄不存在。

    VAR latest = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR text = UO.GetFoundedText()
    IF index >= 0 THEN
        UO.Print(text)
    END IF
END SUB
```

**參數與執行說明:**

- Journal(0) 選取最新記錄。Print 可能新增訊息，因此先儲存文字和索引。空文字本身不表示記錄不存在。

### 在另一次搜尋前保留文字

```vb
# 在另一次搜尋前保留文字
#
# 讀取此腳本所選日誌記錄的已儲存文字。
#
# String：所選文字；未選取記錄時為空字串。存在的記錄也可能含有空文字。此值不是 serial、行索引或表示成功的 Boolean。

SUB Main()
    # 第二次搜尋會替換選取狀態；saved 事先複製第一筆搜尋結果。之後的訊息或搜尋不會改變此變數。

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.GetFoundedText()
        VAR another = UO.InJournal('failed')
        UO.Print(saved)
    END IF
END SUB
```

**參數與執行說明:**

- 第二次搜尋會替換選取狀態；saved 事先複製第一筆搜尋結果。之後的訊息或搜尋不會改變此變數。
