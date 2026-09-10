# UO.GetGumpInfo

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取伺服器 Gump 與其控制項的一致快照。

## 完整語法

```text
UO.GetGumpInfo(GumpIndex:Any) -> Array
```

## 參數

- `GumpIndex` — 必要的 Integer：索引範圍為 0 到 GetGumpsCount()-1，不是 serial 或 GumpID。負數或超出範圍的索引無效。開啟、關閉或重新排列視窗可能改變索引。

## 傳回值

Array — 包含五個欄位的 Array：[0] Integer serial；[1] Integer GumpID；[2] 非空白文字的 Array<String>；[3] 一般按鈕描述的 Array<String>；[4] 包含巢狀項目的所有有效控制項描述 Array<String>。無效、已關閉或被忽略的 Gump 回傳 []。最高位元為 1 的 ID 會以負 Integer 表示；可用 Hex 顯示其位元。

## 行為

- 整份快照在一次遊戲執行緒請求中複製。之後的編輯或關閉不會改變已儲存的陣列。只包含有效的伺服器 Gump，不包含本機背包、地圖及設定視窗。
- 這是 BASIC 陣列，不是 Pascal TGumpInfo 記錄，也不是原始版面封包。描述包含類型、page、ID、X/Y 及尺寸；按鈕另有 ButtonID、action、toPage 和圖像；切換項目另有 checked 與 inactive/active。文字可能含空格及 =。單選按鈕位於 [4]，不在 [3]。
- AddGumpIgnoreByID/BySerial 會在目前腳本中隱藏此讀取結果；ClearGumpsIgnore 會清除篩選。GetGumpsCount 不變。存在的 Gump 也可能有空文字陣列。陣列長度應使用 GetArrayLength，而非 Len。

## 範例

### 讀取兩個 ID

```vb
# 讀取兩個 ID
#
# 讀取伺服器 Gump 與其控制項的一致快照。
#
# Array — 包含五個欄位的 Array：[0] Integer serial；[1] Integer GumpID；[2] 非空白文字的 Array<String>；[3]
# 一般按鈕描述的 Array<String>；[4] 包含巢狀項目的所有有效控制項描述 Array<String>。無效、已關閉或被忽略的 Gump 回傳 []。最高位元為 1 的 ID
# 會以負 Integer 表示；可用 Hex 顯示其位元。

SUB Main()
    # 0 選擇第一個伺服器 Gump。存取欄位前檢查 GetArrayLength(info)=5。info[0] 是 serial，info[1] 是同一份快照的 GumpID。

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        UO.Print('Serial=' + Hex(info[0]))
        UO.Print('GumpID=' + Hex(info[1]))
    END IF
END SUB
```

**參數與執行說明:**

- 0 選擇第一個伺服器 Gump。存取欄位前檢查 GetArrayLength(info)=5。info[0] 是 serial，info[1] 是同一份快照的 GumpID。

### 列出實際 ButtonID

```vb
# 列出實際 ButtonID
#
# 讀取伺服器 Gump 與其控制項的一致快照。
#
# Array — 包含五個欄位的 Array：[0] Integer serial；[1] Integer GumpID；[2] 非空白文字的 Array<String>；[3]
# 一般按鈕描述的 Array<String>；[4] 包含巢狀項目的所有有效控制項描述 Array<String>。無效、已關閉或被忽略的 Gump 回傳 []。最高位元為 1 的 ID
# 會以負 Integer 表示；可用 Hex 顯示其位元。

SUB Main()
    # info[3] 包含按鈕描述。i 是列索引；回應要使用的是描述中的 ButtonID。單選按鈕屬於完整控制項清單。

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR buttons = info[3]
        VAR i = 0
        WHILE i < GetArrayLength(buttons)
            UO.Print(buttons[i])
            i = i + 1
        WEND
    END IF
END SUB
```

**參數與執行說明:**

- info[3] 包含按鈕描述。i 是列索引；回應要使用的是描述中的 ButtonID。單選按鈕屬於完整控制項清單。

### 關閉前保留文字

```vb
# 關閉前保留文字
#
# 讀取伺服器 Gump 與其控制項的一致快照。
#
# Array — 包含五個欄位的 Array：[0] Integer serial；[1] Integer GumpID；[2] 非空白文字的 Array<String>；[3]
# 一般按鈕描述的 Array<String>；[4] 包含巢狀項目的所有有效控制項描述 Array<String>。無效、已關閉或被忽略的 Gump 回傳 []。最高位元為 1 的 ID
# 會以負 Integer 表示；可用 Hex 顯示其位元。

SUB Main()
    # info[2] 是文字副本。CloseSimpleGump(0) 只在沒有 NoClose 時於本機關閉，且不回傳值。儲存的文字仍保留；讀取 texts[0] 前應檢查陣列長度。

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR texts = info[2]
        UO.CloseSimpleGump(0)
        IF GetArrayLength(texts) > 0 THEN
            UO.Print(texts[0])
        END IF
    END IF
END SUB
```

**參數與執行說明:**

- info[2] 是文字副本。CloseSimpleGump(0) 只在沒有 NoClose 時於本機關閉，且不回傳值。儲存的文字仍保留；讀取 texts[0] 前應檢查陣列長度。
