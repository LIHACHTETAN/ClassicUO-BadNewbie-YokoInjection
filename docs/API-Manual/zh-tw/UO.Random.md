# UO.Random

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

選出一個偽隨機整數。Random(min,max) 包含上下限；舊格式 Random(max) 不包含上限。

## 完整語法

```text
UO.Random(max:Integer) -> Integer
UO.Random(min:Integer, max:Integer) -> Integer
```

## 參數

- `min` — 下限，僅用於雙參數格式。32 位元有號整數，範圍 -2147483648 到 2147483647，必須 <= max。
- `max` — 雙參數格式：包含在結果範圍內的上限，可為任意 Integer。單參數格式：不包含的上限，範圍 0..2147483647。Random(0) 傳回 0。

## 傳回值

Integer — 選出的一個數字，不是布林值或 serial。雙參數：min <= 結果 <= max。單一正參數：0 <= 結果 < max。數字可以重複。

## 行為

- 沒有無參數格式。上下限相同時傳回該值。上下限顛倒或單一參數為負數時產生腳本錯誤，不會自動交換上下限。
- 支援完整 32 位元有號範圍，不會因 max+1 溢位。若需要離散小數，可先選整數再除，例如 Random(0,100)/100.0。
- 產生器屬於腳本的 runtime，同時呼叫會同步處理。Random 沒有 seed 參數，與 BASIC Rnd 不同。需要重用同一結果時請先儲存。
- 此呼叫在本機計算，不等待、不移動、不傳送封包。隨機座標仍需檢查地圖及路徑；Random(0)=0 不代表空陣列有有效索引。

## 範例

### 擲骰子

```vb
# 擲骰子
#
# 選出一個偽隨機整數。Random(min,max) 包含上下限；舊格式 Random(max) 不包含上限。
#
# Integer — 選出的一個數字，不是布林值或 serial。雙參數：min <= 結果 <= max。單一正參數：0 <= 結果 < max。數字可以重複。

SUB Main()
    # min=1、max=6 包含全部六個值。roll 儲存一次選擇，STR 將其轉為文字。後續呼叫可能得到相同數字。

    VAR roll = UO.Random(1, 6)
    UO.Print(STR(roll))
END SUB
```

**參數與執行說明:**

- min=1、max=6 包含全部六個值。roll 儲存一次選擇，STR 將其轉為文字。後續呼叫可能得到相同數字。

### 等待隨機時間

```vb
# 等待隨機時間
#
# 選出一個偽隨機整數。Random(min,max) 包含上下限；舊格式 Random(max) 不包含上限。
#
# Integer — 選出的一個數字，不是布林值或 serial。雙參數：min <= 結果 <= max。單一正參數：0 <= 結果 < max。數字可以重複。

SUB Main()
    # min=350、max=700 是包含邊界的毫秒範圍。Random 計算 delay，UO.Wait(delay) 才會等待。請保留伺服器所需的最短延遲。

    VAR delay = UO.Random(350, 700)
    UO.Print(STR(delay))
    UO.Wait(delay)
END SUB
```

**參數與執行說明:**

- min=350、max=700 是包含邊界的毫秒範圍。Random 計算 delay，UO.Wait(delay) 才會等待。請保留伺服器所需的最短延遲。

### 舊式索引與相同邊界

```vb
# 舊式索引與相同邊界
#
# 選出一個偽隨機整數。Random(min,max) 包含上下限；舊格式 Random(max) 不包含上限。
#
# Integer — 選出的一個數字，不是布林值或 serial。雙參數：min <= 結果 <= max。單一正參數：0 <= 結果 < max。數字可以重複。

SUB Main()
    # Random(10) 得到 0..9，不會得到 10。Random(7,7) 一定得到 7。Random(-2,2) 可得到 -2,-1,0,1,2。各運算式分別選出數字。

    VAR index = UO.Random(10)
    VAR fixedValue = UO.Random(7, 7)
    VAR offset = UO.Random(-2, 2)
    UO.Print(STR(index) + ', ' + STR(fixedValue) + ', ' + STR(offset))
END SUB
```

**參數與執行說明:**

- Random(10) 得到 0..9，不會得到 10。Random(7,7) 一定得到 7。Random(-2,2) 可得到 -2,-1,0,1,2。各運算式分別選出數字。
