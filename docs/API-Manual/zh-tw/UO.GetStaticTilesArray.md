# UO.GetStaticTilesArray

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

在矩形範圍內依 graphic/type 搜尋 Static/Multi/Item 記錄。

## 完整語法

```text
UO.GetStaticTilesArray(Xmin:Any, Ymin:Any, Xmax:Any, Ymax:Any, WorldNum:Any, TileType:Any) -> Any
```

## 參數

- `Xmin` — 兩個角的世界座標，包含邊界，範圍 0..65535。顛倒的角會自動調整。最多 1,000,000 格；不合法的邊界會在讀取地圖前產生腳本錯誤。
- `Ymin` — 兩個角的世界座標，包含邊界，範圍 0..65535。顛倒的角會自動調整。最多 1,000,000 格；不合法的邊界會在讀取地圖前產生腳本錯誤。
- `Xmax` — 兩個角的世界座標，包含邊界，範圍 0..65535。顛倒的角會自動調整。最多 1,000,000 格；不合法的邊界會在讀取地圖前產生腳本錯誤。
- `Ymax` — 兩個角的世界座標，包含邊界，範圍 0..65535。顛倒的角會自動調整。最多 1,000,000 格；不合法的邊界會在讀取地圖前產生腳本錯誤。
- `WorldNum` — 地圖／facet 編號 0..255；使用 UO.WorldNum()。不同地圖傳回空 Array。分批處理期間若切換地圖，會捨棄部分結果。
- `TileType` — 一個方塊的 graphic/type，通常為 0..65535，不是 serial。0 只比對 graphic 0；-1 不是萬用值。沒有相符類型時結果為空。

## 傳回值

記錄 Array，每筆為 [graphic, X, Y, Z, hue]，所有欄位都是 Integer。Z 是底部高度，hue 是顏色。同一格的多筆記錄保持獨立。沒有符合項目時傳回空 Array。 使用 GetArrayLength(result) 取得記錄數。索引從 0 開始。結果不是 Boolean、serial 或 Pascal record；沒有第七個輸出參數。

## 行為

- 只讀取本機資料，不改變 FindItem/FindCount，不移動、不啟動 target，也不傳送伺服器指令。
- X 由小到大，每個 X 內的 Y 也由小到大。同一格的記錄保留 bridge 順序，不依距離或高度排序。
- 每批最多 32 格，時間軟性預算約 1 毫秒。批次之間檢查取消。複雜格子或首次讀取可能超時。請分割大型區域；搜尋期間世界資料可能改變。
- 目前 static 分支包含 Static、Multi 與 Item，包括已載入的地面物品，但不包含 Land 與 Mobile。範圍比僅讀取檔案中的靜態物件更廣。

### 內部函式：從呼叫到結果

以下是真正的 C# 處理步驟，不是額外的 UO 指令。範例包含完整的輔助程序。

#### 1. ExecuteStealthCompatibility

接收六個參數；一般形式傳入一個類型，Ex 將 Array 或單一數值轉成類型清單。

以 land/static 模式呼叫 FindPortableTiles，直接傳回記錄 Array。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ExecuteStealthCompatibility`.

#### 2. FindPortableTiles

以 64 位元算術檢查座標、地圖及面積，調整角的順序並建立類型 HashSet。

保留 X/Y 游標，透過 ExecutePathQuerySlice 排程 ScanSlice。批次之間的 Wait(0) 檢查取消；地圖切換時傳回空 Array。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `FindPortableTiles`.

#### 3. ScanSlice

在遊戲執行緒每次處理最多 32 格，每格之後保存游標。

GetLandscapeTile 提供 graphic/Z/flags；GetStaticTiles 提供 graphic/Z/hue 三元組。加入符合記錄，並在批次之間交回控制。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ScanSlice`.

#### 4. GetChunk2

接收區塊座標及載入旗標，在計算線性索引前檢查兩個軸。

傳回 Chunk 或 null；超出地圖的 Y 不會改讀相鄰欄。重用已載入區塊，必要時讀取新區塊。

專案原始碼: `src/ClassicUO.Client/Game/Map/Map.cs`; 函式 `GetChunk2`.

只讀取本機資料，不改變 FindItem/FindCount，不移動、不啟動 target，也不傳送伺服器指令。


## 範例

### 搜尋角色附近

```vb
# 搜尋角色附近
#
# 在矩形範圍內依 graphic/type 搜尋 Static/Multi/Item 記錄。
#
# 記錄 Array，每筆為 [graphic, X, Y, Z, hue]，所有欄位都是 Integer。Z 是底部高度，hue 是顏色。同一格的多筆記錄保持獨立。沒有符合項目時傳回空
# Array。 使用 GetArrayLength(result) 取得記錄數。索引從 0 開始。結果不是 Boolean、serial 或 Pascal record；沒有第七個輸出參數。

SUB Main()
    # x/y 是 self 的座標，map 是目前地圖。3×3 區域包含邊界。Ex 使用兩個範例類型，一般形式使用一個。請依資源更換 graphic，不要傳入物件 ID。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetStaticTilesArray(x, y, x + 2, y + 2, map, 0x0CCA)
    UO.Print("Records: " + CStr(GetArrayLength(rows)))
END SUB
```

**參數與執行說明:**

- x/y 是 self 的座標，map 是目前地圖。3×3 區域包含邊界。Ex 使用兩個範例類型，一般形式使用一個。請依資源更換 graphic，不要傳入物件 ID。

### 顛倒的角與所有結果欄位

```vb
# 顛倒的角與所有結果欄位
#
# 在矩形範圍內依 graphic/type 搜尋 Static/Multi/Item 記錄。
#
# 記錄 Array，每筆為 [graphic, X, Y, Z, hue]，所有欄位都是 Integer。Z 是底部高度，hue 是顏色。同一格的多筆記錄保持獨立。沒有符合項目時傳回空
# Array。 使用 GetArrayLength(result) 取得記錄數。索引從 0 開始。結果不是 Boolean、serial 或 Pascal record；沒有第七個輸出參數。

SUB Main()
    # 2×2 區域使用由大到小的角座標，程式會調整順序。row 是一筆記錄。PrintTile 已完整定義，只輸出數字。地表範例中的 hue=0 是程序佔位參數；地表記錄沒有 hue 欄位。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetStaticTilesArray(x + 1, y + 1, x, y, map, 0x0CCA)
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        PrintTile(row[0], row[1], row[2], row[3], row[4])
        i = i + 1
    WEND
END SUB

SUB PrintTile(graphic, x, y, z, hue)
    UO.Print("Type=" + CStr(graphic) + " X=" + CStr(x) + " Y=" + CStr(y))
    UO.Print("Z=" + CStr(z) + " hue=" + CStr(hue))
END SUB
```

**參數與執行說明:**

- 2×2 區域使用由大到小的角座標，程式會調整順序。row 是一筆記錄。PrintTile 已完整定義，只輸出數字。地表範例中的 hue=0 是程序佔位參數；地表記錄沒有 hue 欄位。

### 限制重試次數的輪詢

```vb
# 限制重試次數的輪詢
#
# 在矩形範圍內依 graphic/type 搜尋 Static/Multi/Item 記錄。
#
# 記錄 Array，每筆為 [graphic, X, Y, Z, hue]，所有欄位都是 Integer。Z 是底部高度，hue 是顏色。同一格的多筆記錄保持獨立。沒有符合項目時傳回空
# Array。 使用 GetArrayLength(result) 取得記錄數。索引從 0 開始。結果不是 Boolean、serial 或 Pascal record；沒有第七個輸出參數。

SUB Main()
    # 最多搜尋同一格三次，兩次之間 WAIT(250)。每次呼叫產生新結果。長度為零只表示目前沒有符合項目，不代表伺服器上永久不存在。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR attempt = 0
    WHILE attempt < 3
        VAR rows = UO.GetStaticTilesArray(x, y, x, y, map, 0x0CCA)
        UO.Print("Records: " + CStr(GetArrayLength(rows)))
        attempt = attempt + 1
        WAIT(250)
    WEND
END SUB
```

**參數與執行說明:**

- 最多搜尋同一格三次，兩次之間 WAIT(250)。每次呼叫產生新結果。長度為零只表示目前沒有符合項目，不代表伺服器上永久不存在。
