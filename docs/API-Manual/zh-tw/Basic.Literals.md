# 123 / 0x0EED / "text" / TRUE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

常值直接在原始碼中寫出值。數字與引號文字不需要宣告。TRUE/FALSE 是預先定義的邏輯值。加上引號的數字仍是文字，直到明確或宣告型別轉換改變它。

## 完整語法

```text
123
-2147483648
0x0EED
0xFFFFFFFF
2.5
"text"
'text'
TRUE
FALSE
```

## 參數

- `integer / hexadecimal` — 十進位 Integer，範圍 -2147483648…2147483647，或 0x 後接十六進位 0–9/A–F。請用小寫 x。常值代表 32 位元：0xFFFFFFFF 是 Integer -1，不是正的 64 位元數。
- `floating` — 小數點前後都有數字的浮點數，例如 2.5、-0.25。請寫 0.5 而不是 .5。此原始碼文法不支援逗號、1e3 之類指數表示法及數值常值後綴。
- `text` — 用成對單引號或雙引號包住文字。要在內容加入引號，使用另一種引號或以 Chr(34)/Chr(39) 組合。不會解讀反斜線跳脫或重複引號跳脫。範例字串請放在同一實體行。
- `TRUE / FALSE` — TRUE 是 Integer 1，FALSE 是 Integer 0。不要重新宣告這些名稱。它們是值而非呼叫：寫 TRUE，不寫 TRUE()。

## 傳回值

整數/十六進位常值產生 Integer；有小數點的數值產生 Decimal（二進位浮點）；引號文字產生 String。TRUE/FALSE 產生 Integer 1/0。求值不執行遊戲動作，也不宣告變數。

## 行為

- -5 的負號是一元運算。引擎將 -2147483648 當成最小有號整數，不必先儲存正的絕對值。超出範圍的整數會出錯；確實需要較大近似數時，應使用合適的浮點值。
- 文字保留字元及大小寫。"350" 不是數字 350，"false" 不是 FALSE。# 和 ; 在引號內是文字，外面則開始註解。AS 與轉換函式的規則見 AS 及各函式說明。
- 引擎辨識常值詞彙，使用固定文化設定解析數字，或移除文字外層引號。IDE 語言不會改變原始碼中的小數分隔符號。
- serial、圖像 type 與座標都可能以數字表示。常值本身不賦予此意義；用途由被呼叫 API 的參數契約決定。

## 範例

### 1. 十六進位 type 與整數邊界

```vb
# itemType=0x0EED 等於十進位 3821。lowest=-2147483648 等於有號位元形式 0x80000000。比較成功，Main 回傳 itemType=3821。此處不搜尋物品。
Option Explicit On
SUB Main()
    VAR itemType = 0x0EED
    VAR lowest = -2147483648
    IF lowest = 0x80000000 THEN
        RETURN itemType
    END IF
    RETURN 0
END SUB
```

**參數與執行說明:**

itemType=0x0EED 等於十進位 3821。lowest=-2147483648 等於有號位元形式 0x80000000。比較成功，Main 回傳 itemType=3821。此處不搜尋物品。

### 2. 兩種引號

```vb
# owner="O'Brien" 包含單引號。instruction 用單引號包住含雙引號的文字。連接 owner、" | "、instruction 會回傳 O'Brien | say "go"，腳本不需要反斜線跳脫。
Option Explicit On
SUB Main()
    VAR owner = "O'Brien"
    VAR instruction = 'say "go"'
    RETURN owner + " | " + instruction
END SUB
```

**參數與執行說明:**

owner="O'Brien" 包含單引號。instruction 用單引號包住含雙引號的文字。連接 owner、" | "、instruction 會回傳 O'Brien | say "go"，腳本不需要反斜線跳脫。

### 3. 邏輯值也是數值

```vb
# enabled=TRUE 儲存 1，stopped=FALSE 儲存 0。計算得到 1*10+0=10。Main 回傳計算結果 10，並不是標準的邏輯 TRUE。
Option Explicit On
SUB Main()
    VAR enabled = TRUE
    VAR stopped = FALSE
    RETURN enabled * 10 + stopped
END SUB
```

**參數與執行說明:**

enabled=TRUE 儲存 1，stopped=FALSE 儲存 0。計算得到 1*10+0=10。Main 回傳計算結果 10，並不是標準的邏輯 TRUE。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: number / literal / HEX_NUMBER / DEC_NUMBER
Runtime/Interpreter.cs: VisitNumber / VisitLiteral / VisitSignedOperand
Runtime/InjectionApiUO.cs: TRUE / FALSE intrinsic values
-->
