# UO.PredictedDirection

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取角色目前已排入佇列的步驟結束後，預測的方向。

## 完整語法

```text
UO.PredictedDirection() -> Integer
```

## 參數

沒有參數。

## 傳回值

Integer 方向 0..7，已移除跑步位元。0 代表北方，也可能表示角色不存在。

## 行為

- 僅支援語法列出的無引數 UO 函式。沒有 target、serial、type、目的地、距離或 timeout 引數。結果是數值，不是 Boolean、ID 或 tile 記錄；1 不代表抵達。
- GetEndPosition 讀取已排入佇列的最後一個 Mobile.Step 的 X/Y/Z/方向；佇列為空時讀取角色目前的位置與方向。O(1) 讀取不會取走步驟、移動、傳送封包、計算路徑或等待抵達。
- 世界方向：0 北、1 東北、2 東、3 東南、4 南、5 西南、6 西、7 西北。畫面使用等角投影。Direction.Mask 移除跑步旗標；不回傳速度。
- 這是本機預測，不是已確認抵達。新增／完成／遭拒的步驟、清空佇列或傳送都可能改變結果。各分量的獨立讀取不構成原子快照；X 相同不能證明 Y/Z 相同或伺服器接受移動。
- Invoke 在遊戲執行緒讀取；工作執行緒等待管理器處理請求。取消腳本會中斷等待。不增加額外延遲或網路查詢。
- 未實作 IPredictedMovementBridge 的外部 IApiBridge 保留讀取目前位置／方向的後備行為。Classic UO 已實作可讀取佇列的介面。

### 內部函式：從呼叫到結果

以下是真正的原生讀取階段。PredictionEquals 是完整定義的使用者 BASIC 輔助函式，不是內建命令或移動程序。

#### 1. ExecuteStealthCompatibility

原生函式呼叫 ReadPredictedCoordinate，選取對應的 IPredictedMovementBridge 屬性。不會呼叫 NewMoveXY 或啟動尋路。

僅支援語法列出的無引數 UO 函式。沒有 target、serial、type、目的地、距離或 timeout 引數。結果是數值，不是 Boolean、ID 或 tile 記錄；1 不代表抵達。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ExecuteStealthCompatibility`.

#### 2. ReadPredictedCoordinate

原生函式呼叫 ReadPredictedCoordinate，選取對應的 IPredictedMovementBridge 屬性。不會呼叫 NewMoveXY 或啟動尋路。

未實作 IPredictedMovementBridge 的外部 IApiBridge 保留讀取目前位置／方向的後備行為。Classic UO 已實作可讀取佇列的介面。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ReadPredictedCoordinate`.

#### 3. Invoke

Invoke 在遊戲執行緒讀取；工作執行緒等待管理器處理請求。取消腳本會中斷等待。不增加額外延遲或網路查詢。

Integer 方向 0..7，已移除跑步位元。0 代表北方，也可能表示角色不存在。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 4. ReadPredictedPosition

Player 不存在或已銷毀時，ReadPredictedPosition 回傳 0；否則呼叫 GetEndPosition 並取出一個分量。

GetEndPosition 讀取已排入佇列的最後一個 Mobile.Step 的 X/Y/Z/方向；佇列為空時讀取角色目前的位置與方向。O(1) 讀取不會取走步驟、移動、傳送封包、計算路徑或等待抵達。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `ReadPredictedPosition`.

#### 5. GetEndPosition

GetEndPosition 讀取已排入佇列的最後一個 Mobile.Step 的 X/Y/Z/方向；佇列為空時讀取角色目前的位置與方向。O(1) 讀取不會取走步驟、移動、傳送封包、計算路徑或等待抵達。

世界方向：0 北、1 東北、2 東、3 東南、4 南、5 西南、6 西、7 西北。畫面使用等角投影。Direction.Mask 移除跑步旗標；不回傳速度。

專案原始碼: `src/ClassicUO.Client/Game/GameObjects/Mobile.cs`; 函式 `GetEndPosition`.

#### 6. InjectionValue

Integer 方向 0..7，已移除跑步位元。0 代表北方，也可能表示角色不存在。

這是本機預測，不是已確認抵達。新增／完成／遭拒的步驟、清空佇列或傳送都可能改變結果。各分量的獨立讀取不構成原子快照；X 相同不能證明 Y/Z 相同或伺服器接受移動。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs`; 函式 `InjectionValue`.

PredictionEquals(expected) 接收一個數值座標／高度／方向，拒絕不存在的角色，並比較一個預測分量。回傳 Integer Boolean：1=TRUE 或 0=FALSE；不會等待或保證抵達。


## 範例

### 讀取一個分量

```vb
# 讀取一個分量
#
# 讀取角色目前已排入佇列的步驟結束後，預測的方向。
#
# Integer 方向 0..7，已移除跑步位元。0 代表北方，也可能表示角色不存在。

SUB Main()
    # predicted 儲存一次無引數呼叫；CStr 將數字格式化以輸出到日誌。

    VAR predicted = UO.PredictedDirection()
    UO.Print('Predicted: ' + CStr(predicted))
END SUB
```

**參數與執行說明:**

- predicted 儲存一次無引數呼叫；CStr 將數字格式化以輸出到日誌。

### 觀察預測變化

```vb
# 觀察預測變化
#
# 讀取角色目前已排入佇列的步驟結束後，預測的方向。
#
# Integer 方向 0..7，已移除跑步位元。0 代表北方，也可能表示角色不存在。

SUB Main()
    # WAIT(100) 讓本範例暫停 100 毫秒。即使中間曾移動，before/after 也可能相等；這些讀取不會啟動移動。

    VAR before = UO.PredictedDirection()
    WAIT(100)
    VAR after = UO.PredictedDirection()
    IF before <> after THEN
        UO.Print('Prediction changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**參數與執行說明:**

- WAIT(100) 讓本範例暫停 100 毫秒。即使中間曾移動，before/after 也可能相等；這些讀取不會啟動移動。

### 完整比較輔助函式

```vb
# 完整比較輔助函式
#
# 讀取角色目前已排入佇列的步驟結束後，預測的方向。
#
# Integer 方向 0..7，已移除跑步位元。0 代表北方，也可能表示角色不存在。

SUB Main()
    # expected 是範例的座標／高度／方向，不是原生命令的引數。PredictionEquals 先檢查 UO.Self()，讀取一次，相等回傳 1=TRUE，否則
    # 0=FALSE。Main 下方有完整定義。單一分量相等不代表抵達。

    IF PredictionEquals(4) = TRUE THEN
        UO.Print('Queued endpoint matches this component')
    ELSE
        UO.Print('Different component or no player')
    END IF
END SUB

SUB PredictionEquals(expected)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR predicted = UO.PredictedDirection()
    RETURN predicted = expected
END SUB
```

**參數與執行說明:**

- expected 是範例的座標／高度／方向，不是原生命令的引數。PredictionEquals 先檢查 UO.Self()，讀取一次，相等回傳 1=TRUE，否則 0=FALSE。Main 下方有完整定義。單一分量相等不代表抵達。
