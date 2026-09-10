# UO.SetStatState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

要求變更屬性成長模式。

## 完整語法

```text
UO.SetStatState(statNum:Any, statState:Any) -> Unit
```

## 參數

- `statNum` — 必要的屬性編號：0 — STR、1 — DEX、2 — INT。不是目前屬性值，也不是文字名稱。
- `statState` — 必要的模式：0 — 上升、1 — 下降、2 — 鎖定。這是三個代碼，不是 Boolean；true/false 無法描述所有模式。

## 傳回值

Unit — 無回傳值。不可當成成功/失敗或與 true 比較。後續讀取得到本機模型，不是伺服器確認。

## 行為

- 有效要求透過 GameActions 傳送一個封包，立即修改本機模式。仍受伺服器規則限制，不保證技能或屬性上升。未知技能、無效索引/模式或沒有角色時忽略要求，不傳送封包。
- 必要的屬性編號：0 — STR、1 — DEX、2 — INT。不是目前屬性值，也不是文字名稱。
- ExecuteStealthCompatibility 選擇分支。Text 讀取技能選擇器，Arg 讀取數字編號與模式。無法轉換的引數可能觸發轉換錯誤。

### 內部函式：從呼叫到結果

以下為實際的 C# 內部步驟。ApplyMode 是範例中完整定義的輔助函式，不是隱藏的內建命令。

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility 選擇分支。Text 讀取技能選擇器，Arg 讀取數字編號與模式。無法轉換的引數可能觸發轉換錯誤。

Unit — 無回傳值。不可當成成功/失敗或與 true 比較。後續讀取得到本機模型，不是伺服器確認。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke 在遊戲執行緒讀取；工作執行緒等待管理器處理請求。取消腳本會中斷等待。不增加額外延遲或網路查詢。

有效要求透過 GameActions 傳送一個封包，立即修改本機模式。仍受伺服器規則限制，不保證技能或屬性上升。未知技能、無效索引/模式或沒有角色時忽略要求，不傳送封包。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 3. SetStatLockState

GetStatLockState/SetStatLockState 依 0/1/2 選擇 StrLock、DexLock 或 IntLock。未知編號讀取得到 −1；寫入前驗證兩個範圍。

Unit — 無回傳值。不可當成成功/失敗或與 true 比較。後續讀取得到本機模型，不是伺服器確認。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `SetStatLockState`.

#### 4. ChangeStatLock

有效要求透過 GameActions 傳送一個封包，立即修改本機模式。仍受伺服器規則限制，不保證技能或屬性上升。未知技能、無效索引/模式或沒有角色時忽略要求，不傳送封包。

Unit — 無回傳值。不可當成成功/失敗或與 true 比較。後續讀取得到本機模型，不是伺服器確認。

專案原始碼: `src/ClassicUO.Client/Game/GameActions.cs`; 函式 `ChangeStatLock`.

有效要求透過 GameActions 傳送一個封包，立即修改本機模式。仍受伺服器規則限制，不保證技能或屬性上升。未知技能、無效索引/模式或沒有角色時忽略要求，不傳送封包。


## 範例

### 讀取並顯示

```vb
# 讀取並顯示
#
# 要求變更屬性成長模式。
#
# Unit — 無回傳值。不可當成成功/失敗或與 true 比較。後續讀取得到本機模型，不是伺服器確認。

SUB Main()
    # 範例明確設定 selector，寫入時也設定 mode。第一行以名稱選技能，或以編號選屬性。Print 僅顯示結果。

    VAR selector = 0
    VAR mode = 2
    UO.SetStatState(selector, mode)
    UO.Print(CStr(UO.GetStatLockState(selector)))
END SUB
```

**參數與執行說明:**

- 範例明確設定 selector，寫入時也設定 mode。第一行以名稱選技能，或以編號選屬性。Print 僅顯示結果。

### 用於條件或比較

```vb
# 用於條件或比較
#
# 要求變更屬性成長模式。
#
# Unit — 無回傳值。不可當成成功/失敗或與 true 比較。後續讀取得到本機模型，不是伺服器確認。

SUB Main()
    # 門檻 95.1 與模式 0/1/2 是範例設定。變更模式前檢查 −1。寫入後讀取僅查看本機副本，不等待伺服器確認。

    VAR selector = 0
    VAR before = UO.GetStatLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetStatState(selector, 0)
        UO.Print(CStr(UO.GetStatLockState(selector)))
    END IF
END SUB
```

**參數與執行說明:**

- 門檻 95.1 與模式 0/1/2 是範例設定。變更模式前檢查 −1。寫入後讀取僅查看本機副本，不等待伺服器確認。

### 完整輔助函式

```vb
# 完整輔助函式
#
# 要求變更屬性成長模式。
#
# Unit — 無回傳值。不可當成成功/失敗或與 true 比較。後續讀取得到本機模型，不是伺服器確認。

SUB Main()
    # Main 後列出完整輔助函式。selector 選擇技能/屬性，mode 指定寫入模式。ReadValue/ReadMode 原樣回傳數字；ApplyMode
    # 驗證引數並執行動作，無回傳值。WAIT(1000) 分隔兩次讀取快照。

    ApplyMode(0, 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetStatLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetStatState(selector, mode)
END SUB
```

**參數與執行說明:**

- Main 後列出完整輔助函式。selector 選擇技能/屬性，mode 指定寫入模式。ReadValue/ReadMode 原樣回傳數字；ApplyMode 驗證引數並執行動作，無回傳值。WAIT(1000) 分隔兩次讀取快照。
