# UO.GetParalisa

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取客戶端目前已知的角色麻痺旗標。

## 完整語法

```text
UO.GetParalisa() -> Integer
UO.GetParalisa(value:Any) -> Integer
```

## 參數

- `value` — 可省略的 mobile serial/ID：整數、十六進位字串、self、lasttarget、其他標準物件別名或 AddObject 名稱。這不是 graphic/type。省略時選擇 self；無法解析的別名變成 0，不會開啟目標游標。

## 傳回值

Integer Boolean：已載入的 mobile 具有 IsParalyzed 時傳回 1 = TRUE；旗標未設定、mobile 未知或已刪除、或物件是道具時傳回 0 = FALSE。這不是剩餘麻痺時間，0 也不保證能夠移動。

## 行為

- 使用 Paralyzed 檢查麻痺旗標。Is/Get 變體、GetParalisa、Frozen 與 GetLocked 都讀取同一旗標。
- 這是本機查詢，不會施加或解除麻痺、不會等待麻痺結束，也不會向伺服器要求更新。
- 對此判斷函式而言，value = TRUE、value = 1 與 IF value 等效。TRUE/FALSE 不加引號。結果是旗標，不是數量或 ID。

## 範例

### 以 TRUE 檢查自己

```vb
# 以 TRUE 檢查自己
#
# 讀取客戶端目前已知的角色麻痺旗標。
#
# Integer Boolean：已載入的 mobile 具有 IsParalyzed 時傳回 1 = TRUE；旗標未設定、mobile 未知或已刪除、或物件是道具時傳回 0 =
# FALSE。這不是剩餘麻痺時間，0 也不保證能夠移動。

SUB Main()
    # 空括號選擇 self。state 儲存一次旗標快照；TRUE 是數值常數 1。
    # FALSE 並不排除牆壁、體力不足或其他無法移動的原因。

    VAR state = UO.GetParalisa()
    IF state = TRUE THEN
        UO.Print('Paralysis flag is set')
    ELSE
        UO.Print('Paralysis flag is absent or unavailable')
    END IF
END SUB
```

**參數與執行說明:**

- 空括號選擇 self。state 儲存一次旗標快照；TRUE 是數值常數 1。
- FALSE 並不排除牆壁、體力不足或其他無法移動的原因。

### 檢查已選取的 mobile

```vb
# 檢查已選取的 mobile
#
# 讀取客戶端目前已知的角色麻痺旗標。
#
# Integer Boolean：已載入的 mobile 具有 IsParalyzed 時傳回 1 = TRUE；旗標未設定、mobile 未知或已刪除、或物件是道具時傳回 0 =
# FALSE。這不是剩餘麻痺時間，0 也不保證能夠移動。

SUB Main()
    # target 以十六進位字串儲存最後目標的 serial。IsNpc 檢查已載入的 mobile，也包括玩家。
    # 引數指定這個已儲存的 target，不會開啟游標或變更 lasttarget。

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR state = UO.GetParalisa(target)
        UO.Print('Selected mobile paralysis 1/0: ' + STR(state))
    ELSE
        UO.Print('No loaded mobile selected')
    END IF
END SUB
```

**參數與執行說明:**

- target 以十六進位字串儲存最後目標的 serial。IsNpc 檢查已載入的 mobile，也包括玩家。
- 引數指定這個已儲存的 target，不會開啟游標或變更 lasttarget。

### 有上限地等待麻痺解除

```vb
# 有上限地等待麻痺解除
#
# 讀取客戶端目前已知的角色麻痺旗標。
#
# Integer Boolean：已載入的 mobile 具有 IsParalyzed 時傳回 1 = TRUE；旗標未設定、mobile 未知或已刪除、或物件是道具時傳回 0 =
# FALSE。這不是剩餘麻痺時間，0 也不保證能夠移動。

SUB Main()
    # 最多等待十次，每次 100 毫秒。每個無引數呼叫都會重新讀取 self。
    # 迴圈結束後另行確認 self 是否仍可用。這只是約一秒加上程式執行時間的觀察，不保證解除麻痺。

    VAR attempts = 0
    WHILE UO.GetParalisa() = TRUE AND attempts < 10
        WAIT(100)
        attempts = attempts + 1
    WEND
    IF UO.IsNpc('self') THEN
        IF UO.GetParalisa() = FALSE THEN
            UO.Print('Paralysis flag is clear')
        ELSE
            UO.Print('Still paralyzed')
        END IF
    ELSE
        UO.Print('Self is unavailable')
    END IF
END SUB
```

**參數與執行說明:**

- 最多等待十次，每次 100 毫秒。每個無引數呼叫都會重新讀取 self。
- 迴圈結束後另行確認 self 是否仍可用。這只是約一秒加上程式執行時間的觀察，不保證解除麻痺。
