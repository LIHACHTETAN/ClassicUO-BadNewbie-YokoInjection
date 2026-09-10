# UO.Backpack

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

傳回目前裝備的背包 ID。

## 完整語法

```text
UO.Backpack() -> Integer
```

## 參數

沒有參數。

## 傳回值

Integer — serial/ID，不是 graphic/type、裝備層、物品數量或 Boolean。0 表示沒有目前物件。保留全部 32 位元；請用 <> 0，不要用 = TRUE 或 > 0。儲存的結果不會自動更新。 尋找 Player 的 Backpack 層上尚未銷毀的物品。Player 或背包不存在／已銷毀時為 0。傳回容器 ID，不是內容；不會建立新背包。

## 行為

- 沒有參數。透過 Invoke 在遊戲執行緒讀取本機狀態；取消腳本可中斷對該執行緒的等待。不傳送封包、不開啟容器或 target，也不搬移物品。
- 不加括號的 self/backpack 每次重新讀取，除非被腳本變數遮蔽。引號內的別名由接收命令解析。搬移目的地中的 "self" 表示背包，但 UO.Self() 傳回角色 serial。需要容器 ID 時請明確使用 UO.Backpack()。
- World.Clear 移除 Player，之後讀取為 0。登入或更換背包可能改變 ID。多次讀取並非原子快照。非零 ID 不證明已連線、伺服器允許操作或內容已載入。

### 內部函式：從呼叫到結果

以下為實際讀取用戶端物件的步驟。IsOwnSerial 是範例中完整定義的腳本函式，不是另一個內建 API。

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility 選擇無參數分支，將 bridge 整數包裝成 InjectionValue。沒有 Pascal 輸出參數或額外選用參數。

Integer — serial/ID，不是 graphic/type、裝備層、物品數量或 Boolean。0 表示沒有目前物件。保留全部 32 位元；請用 <> 0，不要用 = TRUE 或 > 0。儲存的結果不會自動更新。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ExecuteStealthCompatibility`.

#### 2. Invoke

尋找 Player 的 Backpack 層上尚未銷毀的物品。Player 或背包不存在／已銷毀時為 0。傳回容器 ID，不是內容；不會建立新背包。 Invoke 在遊戲執行緒讀取；工作執行緒等待管理器處理請求。取消腳本會中斷等待。不增加額外延遲或網路查詢。

Integer — serial/ID，不是 graphic/type、裝備層、物品數量或 Boolean。0 表示沒有目前物件。保留全部 32 位元；請用 <> 0，不要用 = TRUE 或 > 0。儲存的結果不會自動更新。 沒有參數。透過 Invoke 在遊戲執行緒讀取本機狀態；取消腳本可中斷對該執行緒的等待。不傳送封包、不開啟容器或 target，也不搬移物品。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 3. FindItemByLayer

尋找 Player 的 Backpack 層上尚未銷毀的物品。Player 或背包不存在／已銷毀時為 0。傳回容器 ID，不是內容；不會建立新背包。

Integer — serial/ID，不是 graphic/type、裝備層、物品數量或 Boolean。0 表示沒有目前物件。保留全部 32 位元；請用 <> 0，不要用 = TRUE 或 > 0。儲存的結果不會自動更新。

專案原始碼: `src/ClassicUO.Client/Game/GameObjects/Entity.cs`; 函式 `FindItemByLayer`.

#### 4. Clear

World.Clear 移除 Player，之後讀取為 0。登入或更換背包可能改變 ID。多次讀取並非原子快照。非零 ID 不證明已連線、伺服器允許操作或內容已載入。

World.Clear 移除 Player，之後讀取為 0。登入或更換背包可能改變 ID。多次讀取並非原子快照。非零 ID 不證明已連線、伺服器允許操作或內容已載入。

專案原始碼: `src/ClassicUO.Client/Game/World.cs`; 函式 `Clear`.

World.Clear 移除 Player，之後讀取為 0。登入或更換背包可能改變 ID。多次讀取並非原子快照。非零 ID 不證明已連線、伺服器允許操作或內容已載入。


## 範例

### 讀取並顯示 ID

```vb
# 讀取並顯示 ID
#
# 傳回目前裝備的背包 ID。
#
# Integer — serial/ID，不是 graphic/type、裝備層、物品數量或 Boolean。0 表示沒有目前物件。保留全部 32 位元；請用 <> 0，不要用 = TRUE
# 或 > 0。儲存的結果不會自動更新。 尋找 Player 的 Backpack 層上尚未銷毀的物品。Player 或背包不存在／已銷毀時為 0。傳回容器 ID，不是內容；不會建立新背包。

SUB Main()
    # id 儲存一次結果；HEX 將 serial 格式化到日誌。不選擇或使用物件。

    VAR id = UO.Backpack()
    UO.Print('ID: ' + HEX(id))
END SUB
```

**參數與執行說明:**

- id 儲存一次結果；HEX 將 serial 格式化到日誌。不選擇或使用物件。

### 偵測 ID 變化

```vb
# 偵測 ID 變化
#
# 傳回目前裝備的背包 ID。
#
# Integer — serial/ID，不是 graphic/type、裝備層、物品數量或 Boolean。0 表示沒有目前物件。保留全部 32 位元；請用 <> 0，不要用 = TRUE
# 或 > 0。儲存的結果不會自動更新。 尋找 Player 的 Backpack 層上尚未銷毀的物品。Player 或背包不存在／已銷毀時為 0。傳回容器 ID，不是內容；不會建立新背包。

SUB Main()
    # before/after 相隔 250 毫秒讀取。WAIT 僅屬於此範例。兩端 ID 相同仍可能漏掉中途變化。

    VAR before = UO.Backpack()
    WAIT(250)
    VAR after = UO.Backpack()
    IF before <> after THEN
        UO.Print('ID changed: ' + HEX(after))
    END IF
END SUB
```

**參數與執行說明:**

- before/after 相隔 250 毫秒讀取。WAIT 僅屬於此範例。兩端 ID 相同仍可能漏掉中途變化。

### 完整 IsOwnSerial 輔助函式

```vb
# 完整 IsOwnSerial 輔助函式
#
# 傳回目前裝備的背包 ID。
#
# Integer — serial/ID，不是 graphic/type、裝備層、物品數量或 Boolean。0 表示沒有目前物件。保留全部 32 位元；請用 <> 0，不要用 = TRUE
# 或 > 0。儲存的結果不會自動更新。 尋找 Player 的 Backpack 層上尚未銷毀的物品。Player 或背包不存在／已銷毀時為 0。傳回容器 ID，不是內容；不會建立新背包。

SUB Main()
    # candidate 是已儲存的 LastTarget ID。IsOwnSerial(candidate) 接受一個 serial，傳回 Integer Boolean：符合目前非零自身
    # ID 時為 1=TRUE，否則 0=FALSE。定義完整，不改變 target。

    VAR candidate = UO.LastTarget()
    IF IsOwnSerial(candidate) = TRUE THEN
        UO.Print('Own object selected')
    ELSE
        UO.Print('Different object or no own object')
    END IF
END SUB

SUB IsOwnSerial(candidate)
    VAR current = UO.Backpack()
    RETURN current <> 0 AND current = candidate
END SUB
```

**參數與執行說明:**

- candidate 是已儲存的 LastTarget ID。IsOwnSerial(candidate) 接受一個 serial，傳回 Integer Boolean：符合目前非零自身 ID 時為 1=TRUE，否則 0=FALSE。定義完整，不改變 target。
