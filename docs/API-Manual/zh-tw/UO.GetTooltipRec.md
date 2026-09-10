# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取物件的結構化屬性，包括每筆資料的 cliloc ID 與替換參數。

## 完整語法

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## 參數

- `ObjID` — 必填的物件 serial，不是 graphic/type，也不是 cliloc ID。接受整數、十進位或十六進位字串、self、backpack、lasttarget、finditem 或 AddObject 名稱。0 表示沒有物件。

## 傳回值

Array<Array>：每列為 [clilocID:Integer, parameters:Array<String>]。rows[i][0] 是訊息 ID；rows[i][1] 是參數陣列。GetArrayLength(rows) 是屬性筆數。尚未收到資料或 ObjID=0 時傳回空陣列。這些 ID 不是物件 serial。

## 行為

- 快取資料立即傳回。沒有 OPL 時會發送請求並等待最多 120 毫秒；取消程序會中止等待。已知的空 OPL 會立即傳回。
- BASIC 陣列對應 TClilocRec：Count 為 GetArrayLength(rows)，Items 為各列。會略過開頭傳輸用的定位字元，保留中間空參數的位置。#數字仍為字串，供後續本地化使用。缺少參數時提供空陣列。修改結果不會更動客戶端快取。
- https://stealth.od.ua/api/GetTooltipRec/

## 範例

### 列出屬性 ID

```vb
# 列出屬性 ID
#
# 讀取物件的結構化屬性，包括每筆資料的 cliloc ID 與替換參數。
#
# Array<Array>：每列為 [clilocID:Integer, parameters:Array<String>]。rows[i][0] 是訊息 ID；rows[i][1]
# 是參數陣列。GetArrayLength(rows) 是屬性筆數。尚未收到資料或 ObjID=0 時傳回空陣列。這些 ID 不是物件 serial。

SUB Main()
    # ObjID=lasttarget 選取物件。i 從 0 開始；row[0] 是 cliloc ID。空陣列不會執行迴圈。

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**參數與執行說明:**

- ObjID=lasttarget 選取物件。i 從 0 開始；row[0] 是 cliloc ID。空陣列不會執行迴圈。

### 翻譯每筆屬性

```vb
# 翻譯每筆屬性
#
# 讀取物件的結構化屬性，包括每筆資料的 cliloc ID 與替換參數。
#
# Array<Array>：每列為 [clilocID:Integer, parameters:Array<String>]。rows[i][0] 是訊息 ID；rows[i][1]
# 是參數陣列。GetArrayLength(rows) 是屬性筆數。尚未收到資料或 ObjID=0 時傳回空陣列。這些 ID 不是物件 serial。

SUB Main()
    # GetClilocByID 接收 ClilocID=row[0] 與 Params=row[1]，並保留參數順序。請勿把整列當作 Params。

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

**參數與執行說明:**

- GetClilocByID 接收 ClilocID=row[0] 與 Params=row[1]，並保留參數順序。請勿把整列當作 Params。

### 讀取數值參數

```vb
# 讀取數值參數
#
# 讀取物件的結構化屬性，包括每筆資料的 cliloc ID 與替換參數。
#
# Array<Array>：每列為 [clilocID:Integer, parameters:Array<String>]。rows[i][0] 是訊息 ID；rows[i][1]
# 是參數陣列。GetArrayLength(rows) 是屬性筆數。尚未收到資料或 ObjID=0 時傳回空陣列。這些 ID 不是物件 serial。

SUB Main()
    # wanted=1060401 是範例屬性 ID，請替換。args[0] 為 String。呼叫 Val 前檢查長度與 IsNumeric；參數可能是文字或 #cliloc。

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

**參數與執行說明:**

- wanted=1060401 是範例屬性 ID，請替換。args[0] 為 String。呼叫 Val 前檢查長度與 IsNumeric；參數可能是文字或 #cliloc。
