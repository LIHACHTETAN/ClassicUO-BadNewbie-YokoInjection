# +, -, *, /, MOD

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: zh-tw -->

算術運算式由運算元計算一個值：+ 相加，- 相減或反轉正負號，* 相乘，/ 相除，MOD 取得整數餘數。將結果指定給變數或以 RETURN 傳回，便可繼續使用。

## 完整語法

```text
left + right
left - right
-right
left * right
left / right
left MOD right
(expression)
```

## 參數

- `left` — 左側數值運算元：常值、已宣告變數、括號運算式或函式結果。一元負號沒有左側運算元。
- `right` — 右側數值運算元。對 / 而言是除數；MOD 會先轉成 Integer，轉換後必須非零。例如 0.5 會截斷成 0 並發生錯誤。
- `operator / precedence` — 優先順序為一元負號，接著同級的 * / MOD 由左至右，最後二元 + - 由左至右。括號可改變順序。本語法不支援一元正號、次方 ^ 或反斜線整數除法。

## 傳回值

整數的 +、-、* 與一元負號傳回 Integer；若參與運算的數值運算元是 Decimal，則傳回 Decimal。/ 一律傳回 Decimal：5/2=2.5。MOD 傳回 Integer。這是計算所得的數字，是否代表成功或物品數量由腳本決定。

## 行為

- MOD 將兩個運算元轉為有號 32 位元整數，可表示的小數部分向零截斷。餘數保留被除數的正負號：-17 MOD 5=-2；-2147483648 MOD -1=0。包含 mOd 在內的大小寫組合不影響結果。
- MOD 的除數為零會拋出可由 TRY/CATCH 處理的錯誤。/ 採用浮點除法：非零分子除以零得到帶正負號的 Infinity，0/0 得到 NaN。若需要有限結果，請先檢查除數。
- 整數 +、-、* 與取負號溢位時保留低 32 位元，不會自動擴大整數型別。若允許近似值，大數計算前可先將一個運算元轉成 Decimal；浮點運算仍有二進位捨入誤差。
- 一般數值運算子不會自動解析文字。String+String 串接文字，String+Integer 會失敗。需要解析數字文字時請明確呼叫 CDbl 等轉換。中置 MOD 對整數文字的解析比獨立 BasicMod 函式嚴格。
- 解譯器依運算式順序計算運算元、選取運算子權杖並產生 InjectionValue。括號內的運算式會先完成。除非運算元本身呼叫相關 API，否則不會移動、等待或發出網路要求。

## 範例

### 1. 優先順序與括號

```vb
# plain=2+3*4 先相乘，結果為 14。grouped=(2+3)*4 得到 20。Main 傳回 plain*100+grouped=1420，可驗證兩個計算。
Option Explicit On
SUB Main()
    VAR plain = 2 + 3 * 4
    VAR grouped = (2 + 3) * 4
    RETURN plain * 100 + grouped
END SUB
```

**參數與執行說明:**

plain=2+3*4 先相乘，結果為 14。grouped=(2+3)*4 得到 20。Main 傳回 plain*100+grouped=1420，可驗證兩個計算。

### 2. 完整批次與剩餘物品

```vb
# DescribeBatches 接收 total=27 和 size=5。size 檢查拒絕零或負數批次大小。Fix(total/size) 將 5.4 轉成 5 個完整批次；total mOd size 得到剩下 2 件物品。CStr 將數字轉成傳回文字 "5:2"。輔助函式完整列出。
Option Explicit On
FUNCTION DescribeBatches(total, size)
    IF size <= 0 THEN
        RETURN "invalid"
    END IF
    VAR whole = Fix(total / size)
    VAR remaining = total mOd size
    RETURN CStr(whole) + ":" + CStr(remaining)
END FUNCTION
SUB Main()
    RETURN DescribeBatches(27, 5)
END SUB
```

**參數與執行說明:**

DescribeBatches 接收 total=27 和 size=5。size 檢查拒絕零或負數批次大小。Fix(total/size) 將 5.4 轉成 5 個完整批次；total mOd size 得到剩下 2 件物品。CStr 將數字轉成傳回文字 "5:2"。輔助函式完整列出。

### 3. 處理無效除數

```vb
# 10 MOD 0 在指定 unusedResult 前發生錯誤。CATCH 將錯誤存入 problem，並設定 caught=TRUE。Main 傳回 1，這是範例的錯誤處理旗標，不是失敗 MOD 的結果。
Option Explicit On
SUB Main()
    VAR caught = FALSE
    TRY
        VAR unusedResult = 10 MOD 0
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**參數與執行說明:**

10 MOD 0 在指定 unusedResult 前發生錯誤。CATCH 將錯誤存入 problem，並設定 caught=TRUE。Main 傳回 1，這是範例的錯誤處理旗標，不是失敗 MOD 的結果。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: signedOperand / additiveOperand / comparativeOperand
Runtime/Interpreter.cs: VisitSignedOperand / VisitAdditiveOperand / VisitComparativeOperand
Runtime/InjectionValue.cs: arithmetic operators
Runtime/NumberConversions.cs: ToInt
-->
