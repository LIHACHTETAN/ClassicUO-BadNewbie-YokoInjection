# UO.IsWorldCellPassable

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

檢查前往相鄰世界格的一步，回傳可通行旗標與高度。

## 完整語法

```text
UO.IsWorldCellPassable(CurrX:Any, CurrY:Any, CurrZ:Any, DestX:Any, DestY:Any, DestZ:Any, WorldNum:Any) -> Array
```

## 參數

- `CurrX` — 必要的起點格世界座標 X：已載入地圖範圍內的整數 0..65535，不是 gump 座標。
- `CurrY` — 必要的起點格世界座標 Y：已載入地圖範圍內的整數 0..65535，不是 gump 座標。
- `CurrZ` — 必要的起點高度 −128..127，不是樓層編號。無效高度會被拒絕，不會截斷。
- `DestX` — 必要的目標格世界座標 X：已載入地圖範圍內的整數 0..65535，不是 gump 座標。
- `DestY` — 必要的目標格世界座標 Y：已載入地圖範圍內的整數 0..65535，不是 gump 座標。
- `DestZ` — 必要的備用輸入 Z，通常用 CurrZ。不是 var：不修改變數，也不指定樓層。計算高度在 result[1]。此 bridge 一律提供自己的高度；此引數保留 Pascal 形式。
- `WorldNum` — 必要的地圖編號：UO.WorldNum()。只檢查尺寸已知的目前地圖，不載入其他地圖。

## 傳回值

包含兩個 Integer 的 Array：[0] — 可通行，1 = TRUE、0 = FALSE；[1] — 計算的 Z。只有第一項是邏輯值，不可把陣列本身與 TRUE 比較。零或負高度有效；[0]=0 時，高度不能證明可達。拒絕引數時回傳 [0, CurrZ]。

## 行為

- 不移動、不開門、不選目標，也不傳送網路封包。讀取現有本機幾何，伺服器仍可拒絕稍後的步伐。每次查詢是獨立快照。
- 相鄰格的 X/Y 差都不得超過 1。遠方目標、超出地圖、沒有角色/地圖或 IsDestroyed 都在碰撞計算前拒絕。完整路線請用 GetPathArray 或 NewMoveXY。
- 相同且有效的 X/Y 不需走一步，不經碰撞檢查即回傳 [1, CurrZ]；不代表能離開該格。角色狀態與目前 Pathfinder 規則會影響相鄰步伐；幾何未載入時可能拒絕。

### 內部函式：從呼叫到結果

以下為實際的 C# 內部步驟。IsCellOpen 是範例中完整定義的輔助函式，不是隱藏的內建命令。

#### 1. ExecuteStealthCompatibility

讀取七個 Integer 引數。只有其他 bridge 未提供高度時才用 DestZ。回傳陣列，不修改引數。

包含兩個 Integer 的 Array：[0] — 可通行，1 = TRUE、0 = FALSE；[1] — 計算的 Z。只有第一項是邏輯值，不可把陣列本身與 TRUE 比較。零或負高度有效；[0]=0 時，高度不能證明可達。拒絕引數時回傳 [0, CurrZ]。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ExecuteStealthCompatibility`.

#### 2. CheckWorldStep

Invoke 在座標相減前驗證角色、地圖、尺寸、座標、高度及相鄰關係，再選方向。CanWalkForQuery 後還必須完全符合目標 X/Y。

包含兩個 Integer 的 Array：[0] — 可通行，1 = TRUE、0 = FALSE；[1] — 計算的 Z。只有第一項是邏輯值，不可把陣列本身與 TRUE 比較。零或負高度有效；[0]=0 時，高度不能證明可達。拒絕引數時回傳 [0, CurrZ]。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `CheckWorldStep`.

#### 3. CanWalkForQuery

暫時移除其他路線的禁用格判斷，於 finally 還原。呼叫 CanWalk，不啟動路線。

不移動、不開門、不選目標，也不傳送網路封包。讀取現有本機幾何，伺服器仍可拒絕稍後的步伐。每次查詢是獨立快照。

專案原始碼: `src/ClassicUO.Client/Game/Pathfinder.cs`; 函式 `CanWalkForQuery`.

#### 4. CanWalk

檢查主要步伐與對角側格。回傳 bool，只有接受步伐時才更新 ref 座標。

碰撞函式讀取已載入幾何與角色狀態。對角線改走側格不等於到達要求的目標格。

專案原始碼: `src/ClassicUO.Client/Game/Pathfinder.cs`; 函式 `CanWalk`.

#### 5. CalculateNewZ

接收目標 X/Y、ref 起點 Z 及方向，依角色狀態選擇表面和淨空；bool 表示可通行，z 表示高度。

碰撞函式讀取已載入幾何與角色狀態。對角線改走側格不等於到達要求的目標格。

專案原始碼: `src/ClassicUO.Client/Game/Pathfinder.cs`; 函式 `CalculateNewZ`.

#### 6. CalculateMinMaxZ

接收新格、目前 Z、方向及模式。透過 CreateItemList 取得起點幾何並計算 ref minZ/maxZ。

碰撞函式讀取已載入幾何與角色狀態。對角線改走側格不等於到達要求的目標格。

專案原始碼: `src/ClassicUO.Client/Game/Pathfinder.cs`; 函式 `CalculateMinMaxZ`.

#### 7. CreateItemList

接收清單、X/Y 和模式，收集已載入物件與碰撞規則；bool 表示幾何可用。Map.GetTile 使用 load=false，不讀取新區塊。

碰撞函式讀取已載入幾何與角色狀態。對角線改走側格不等於到達要求的目標格。

專案原始碼: `src/ClassicUO.Client/Game/Pathfinder.cs`; 函式 `CreateItemList`.

不移動、不開門、不選目標，也不傳送網路封包。讀取現有本機幾何，伺服器仍可拒絕稍後的步伐。每次查詢是獨立快照。


## 範例

### 檢查東側格

```vb
# 檢查東側格
#
# 檢查前往相鄰世界格的一步，回傳可通行旗標與高度。
#
# 包含兩個 Integer 的 Array：[0] — 可通行，1 = TRUE、0 = FALSE；[1] — 計算的 Z。只有第一項是邏輯值，不可把陣列本身與 TRUE
# 比較。零或負高度有效；[0]=0 時，高度不能證明可達。拒絕引數時回傳 [0, CurrZ]。

SUB Main()
    # x/y/z 是起點，x+1/y 是鄰格；第六個引數是備用 Z，最後是目前地圖。先檢查 result[0] 再使用 result[1]。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR result = UO.IsWorldCellPassable(x,y,z,x+1,y,z,UO.WorldNum())
    IF result[0] = TRUE THEN
        UO.Print('Passable, Z=' + CStr(result[1]))
    ELSE
        UO.Print('Blocked')
    END IF
END SUB
```

**參數與執行說明:**

- x/y/z 是起點，x+1/y 是鄰格；第六個引數是備用 Z，最後是目前地圖。先檢查 result[0] 再使用 result[1]。

### 讀取 Z 而不修改引數

```vb
# 讀取 Z 而不修改引數
#
# 檢查前往相鄰世界格的一步，回傳可通行旗標與高度。
#
# 包含兩個 Integer 的 Array：[0] — 可通行，1 = TRUE、0 = FALSE；[1] — 計算的 Z。只有第一項是邏輯值，不可把陣列本身與 TRUE
# 比較。零或負高度有效；[0]=0 時，高度不能證明可達。拒絕引數時回傳 [0, CurrZ]。

SUB Main()
    # proposedZ 仍為 0。targetZ 來自 result[1]，不是輸入引數。拒絕時不推測高度。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR proposedZ = 0
    VAR result = UO.IsWorldCellPassable(x,y,z,x,y+1,proposedZ,UO.WorldNum())
    IF result[0] = 1 THEN
        VAR targetZ = result[1]
        UO.Print('Input=' + CStr(proposedZ) + '; result=' + CStr(targetZ))
    END IF
END SUB
```

**參數與執行說明:**

- proposedZ 仍為 0。targetZ 來自 result[1]，不是輸入引數。拒絕時不推測高度。

### 完整的 IsCellOpen 函式

```vb
# 完整的 IsCellOpen 函式
#
# 檢查前往相鄰世界格的一步，回傳可通行旗標與高度。
#
# 包含兩個 Integer 的 Array：[0] — 可通行，1 = TRUE、0 = FALSE；[1] — 計算的 Z。只有第一項是邏輯值，不可把陣列本身與 TRUE
# 比較。零或負高度有效；[0]=0 時，高度不能證明可達。拒絕引數時回傳 [0, CurrZ]。

SUB Main()
    # Main 後提供完整函式，接收起點 X/Y/Z、目標 X/Y 和地圖，補上第六個引數，只回傳 Integer 1/0，並非陣列。因此 IsCellOpen 可與 TRUE
    # 比較。程式不移動角色。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR openCell = IsCellOpen(x,y,UO.GetZ(),x+1,y+1,UO.WorldNum())
    IF openCell = TRUE THEN
        UO.Print('Diagonal cell is locally passable')
    END IF
END SUB

SUB IsCellOpen(x,y,z,toX,toY,map)
    VAR cellResult = UO.IsWorldCellPassable(x,y,z,toX,toY,z,map)
    IF GetArrayLength(cellResult) <> 2 THEN
        RETURN 0
    END IF
    RETURN cellResult[0]
END SUB
```

**參數與執行說明:**

- Main 後提供完整函式，接收起點 X/Y/Z、目標 X/Y 和地圖，補上第六個引數，只回傳 Integer 1/0，並非陣列。因此 IsCellOpen 可與 TRUE 比較。程式不移動角色。
