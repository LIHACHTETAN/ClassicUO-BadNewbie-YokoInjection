# UO.GetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取屬性的本機成長模式。

## 完整語法

```text
UO.GetStatLockState(statNum:Any) -> Integer
```

## 參數

- `statNum` — 必要的屬性編號：0 — STR、1 — DEX、2 — INT。不是目前屬性值，也不是文字名稱。

## 傳回值

Integer：0 — 上升、1 — 下降、2 — 鎖定。模式代碼，不是 true/false。 編號超出 0..2 時回傳 −1。沒有角色時，有效編號預設回傳 0；不代表伺服器確認的狀態。

## 行為

- Invoke 在遊戲執行緒讀取已有資料，不傳送網路封包。不使用或訓練技能。兩次查詢是獨立快照。
- 必要的屬性編號：0 — STR、1 — DEX、2 — INT。不是目前屬性值，也不是文字名稱。
- ExecuteStealthCompatibility 選擇分支。Text 讀取技能選擇器，Arg 讀取數字編號與模式。無法轉換的引數可能觸發轉換錯誤。

### 內部函式：從呼叫到結果

以下為實際的 C# 內部步驟。ReadMode 是範例中完整定義的輔助函式，不是隱藏的內建命令。

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility 選擇分支。Text 讀取技能選擇器，Arg 讀取數字編號與模式。無法轉換的引數可能觸發轉換錯誤。

Integer：0 — 上升、1 — 下降、2 — 鎖定。模式代碼，不是 true/false。 編號超出 0..2 時回傳 −1。沒有角色時，有效編號預設回傳 0；不代表伺服器確認的狀態。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke 在遊戲執行緒讀取；工作執行緒等待管理器處理請求。取消腳本會中斷等待。不增加額外延遲或網路查詢。

Invoke 在遊戲執行緒讀取已有資料，不傳送網路封包。不使用或訓練技能。兩次查詢是獨立快照。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 3. GetStatLockState

GetStatLockState/SetStatLockState 依 0/1/2 選擇 StrLock、DexLock 或 IntLock。未知編號讀取得到 −1；寫入前驗證兩個範圍。

Integer：0 — 上升、1 — 下降、2 — 鎖定。模式代碼，不是 true/false。 編號超出 0..2 時回傳 −1。沒有角色時，有效編號預設回傳 0；不代表伺服器確認的狀態。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `GetStatLockState`.

Invoke 在遊戲執行緒讀取已有資料，不傳送網路封包。不使用或訓練技能。兩次查詢是獨立快照。


## 範例

### 讀取並顯示

```vb
# 讀取並顯示
#
# 讀取屬性的本機成長模式。
#
# Integer：0 — 上升、1 — 下降、2 — 鎖定。模式代碼，不是 true/false。 編號超出 0..2 時回傳 −1。沒有角色時，有效編號預設回傳
# 0；不代表伺服器確認的狀態。

SUB Main()
    # 範例明確設定 selector，寫入時也設定 mode。第一行以名稱選技能，或以編號選屬性。Print 僅顯示結果。

    VAR selector = 0
    VAR mode = UO.GetStatLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**參數與執行說明:**

- 範例明確設定 selector，寫入時也設定 mode。第一行以名稱選技能，或以編號選屬性。Print 僅顯示結果。

### 用於條件或比較

```vb
# 用於條件或比較
#
# 讀取屬性的本機成長模式。
#
# Integer：0 — 上升、1 — 下降、2 — 鎖定。模式代碼，不是 true/false。 編號超出 0..2 時回傳 −1。沒有角色時，有效編號預設回傳
# 0；不代表伺服器確認的狀態。

SUB Main()
    # 門檻 95.1 與模式 0/1/2 是範例設定。變更模式前檢查 −1。寫入後讀取僅查看本機副本，不等待伺服器確認。

    VAR mode = UO.GetStatLockState(0)
    IF mode = 2 THEN
        UO.Print("Locked")
    ELSE
        IF mode = -1 THEN
            UO.Print("Unknown selector")
        ELSE
            UO.Print("Mode: " + CStr(mode))
        END IF
    END IF
END SUB
```

**參數與執行說明:**

- 門檻 95.1 與模式 0/1/2 是範例設定。變更模式前檢查 −1。寫入後讀取僅查看本機副本，不等待伺服器確認。

### 完整輔助函式

```vb
# 完整輔助函式
#
# 讀取屬性的本機成長模式。
#
# Integer：0 — 上升、1 — 下降、2 — 鎖定。模式代碼，不是 true/false。 編號超出 0..2 時回傳 −1。沒有角色時，有效編號預設回傳
# 0；不代表伺服器確認的狀態。

SUB Main()
    # Main 後列出完整輔助函式。selector 選擇技能/屬性，mode 指定寫入模式。ReadValue/ReadMode 原樣回傳數字；ApplyMode
    # 驗證引數並執行動作，無回傳值。WAIT(1000) 分隔兩次讀取快照。

    VAR before = ReadMode(0)
    WAIT(1000)
    VAR after = ReadMode(0)
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetStatLockState(selector)
END SUB
```

**參數與執行說明:**

- Main 後列出完整輔助函式。selector 選擇技能/屬性，mode 指定寫入模式。ReadValue/ReadMode 原樣回傳數字；ApplyMode 驗證引數並執行動作，無回傳值。WAIT(1000) 分隔兩次讀取快照。
