# UO.LastTargetY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取最後選擇目標時保存的 Y。

## 完整語法

```text
UO.LastTargetY() -> Integer
```

## 參數

沒有參數。

## 傳回值

Integer — 保存的 Y 座標，不是像素或 Boolean。選擇前、Clear 後或未知物件為 0；實際座標 0 也有效。LastTarget()=0 時仍可取得土地/靜態物件座標。

## 行為

- 沒有參數，不開游標、不選目標、不攻擊或傳送封包。LastTarget 不同於 LastAttack 和 LastStatus。一般選擇 self 不會替換它；ClientMarkChar 可明確更改。
- SetEntity 保存已知 Entity.X/Y，可能是容器內部座標。SetLand/SetStatic 保存世界格。之後移動/移除不改變保存值。GetX/GetY(serial) 取得目前位置。
- Clear 和 World.Clear 即使保留腳本仍會重設。明確設定未知 serial 時 X/Y=0，不繼承舊座標。這不保證目標在伺服器存在。
- 分開讀取不是原子操作。物件目標的 LastTile 保留通訊協定 X/Y=65535；土地/靜態物件的 LastTile(1)/(2) 讀取 X/Y。無括號的 lasttarget 是動態內建值，但可被同名變數遮蔽。
- World.Clear 呼叫 ClearWorldState，清除作用中的游標/callback、已存目標與重複封包。一般 Reset 保留歷史。原生 TargetLast 僅在伺服器游標作用中時傳送已存封包；沒有歷史或為本機 callback 時保留游標且不傳送。 作用中的客戶端 callback 只收到一次 null 取消通知：ClientTargetResponsePresent 變為 1，回應為空。已完成的選取不會再次通知。

### 內部函式：從呼叫到結果

以下為實際的 C# 內部步驟。ReadTargetValue 是範例中完整定義的輔助函式，不是隱藏的內建命令。

#### 1. SetEntity

SetEntity 透過 World.Get 保存 serial 與 X/Y。不存在或銷毀的 Entity 得到 X/Y=0；協定特殊值保持不變。

SetEntity 保存已知 Entity.X/Y，可能是容器內部座標。SetLand/SetStatic 保存世界格。之後移動/移除不改變保存值。GetX/GetY(serial) 取得目前位置。

專案原始碼: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 函式 `SetEntity`.

#### 2. SetLand

SetLand/SetStatic 保存 X/Y/Z 並設 serial 0。SavedX/SavedY 與傳送欄位分開。

Integer — 保存的 Y 座標，不是像素或 Boolean。選擇前、Clear 後或未知物件為 0；實際座標 0 也有效。LastTarget()=0 時仍可取得土地/靜態物件座標。

專案原始碼: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 函式 `SetLand`.

#### 3. SetStatic

SetLand/SetStatic 保存 X/Y/Z 並設 serial 0。SavedX/SavedY 與傳送欄位分開。

Integer — 保存的 Y 座標，不是像素或 Boolean。選擇前、Clear 後或未知物件為 0；實際座標 0 也有效。LastTarget()=0 時仍可取得土地/靜態物件座標。

專案原始碼: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 函式 `SetStatic`.

#### 4. LastTargetY

LastTargetX/LastTargetY 讀取 ITargetSnapshotBridge；舊外部 bridge 保留 GetX/GetY。Invoke 在遊戲執行緒讀取並支援取消。

Integer — 保存的 Y 座標，不是像素或 Boolean。選擇前、Clear 後或未知物件為 0；實際座標 0 也有效。LastTarget()=0 時仍可取得土地/靜態物件座標。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `LastTargetY`.

#### 5. Invoke

LastTargetX/LastTargetY 讀取 ITargetSnapshotBridge；舊外部 bridge 保留 GetX/GetY。Invoke 在遊戲執行緒讀取並支援取消。

沒有參數，不開游標、不選目標、不攻擊或傳送封包。LastTarget 不同於 LastAttack 和 LastStatus。一般選擇 self 不會替換它；ClientMarkChar 可明確更改。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 6. Clear

Clear 清除 serial 及保存座標；World.Clear 在清理時呼叫它。

Clear 和 World.Clear 即使保留腳本仍會重設。明確設定未知 serial 時 X/Y=0，不繼承舊座標。這不保證目標在伺服器存在。

專案原始碼: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 函式 `Clear`.

#### 7. ClearWorldState

World.Clear 呼叫 ClearWorldState，清除作用中的游標/callback、已存目標與重複封包。一般 Reset 保留歷史。原生 TargetLast 僅在伺服器游標作用中時傳送已存封包；沒有歷史或為本機 callback 時保留游標且不傳送。 作用中的客戶端 callback 只收到一次 null 取消通知：ClientTargetResponsePresent 變為 1，回應為空。已完成的選取不會再次通知。

World.Clear 呼叫 ClearWorldState，清除作用中的游標/callback、已存目標與重複封包。一般 Reset 保留歷史。原生 TargetLast 僅在伺服器游標作用中時傳送已存封包；沒有歷史或為本機 callback 時保留游標且不傳送。 作用中的客戶端 callback 只收到一次 null 取消通知：ClientTargetResponsePresent 變為 1，回應為空。已完成的選取不會再次通知。

專案原始碼: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 函式 `ClearWorldState`.

#### 8. TargetLast

World.Clear 呼叫 ClearWorldState，清除作用中的游標/callback、已存目標與重複封包。一般 Reset 保留歷史。原生 TargetLast 僅在伺服器游標作用中時傳送已存封包；沒有歷史或為本機 callback 時保留游標且不傳送。 作用中的客戶端 callback 只收到一次 null 取消通知：ClientTargetResponsePresent 變為 1，回應為空。已完成的選取不會再次通知。

World.Clear 呼叫 ClearWorldState，清除作用中的游標/callback、已存目標與重複封包。一般 Reset 保留歷史。原生 TargetLast 僅在伺服器游標作用中時傳送已存封包；沒有歷史或為本機 callback 時保留游標且不傳送。 作用中的客戶端 callback 只收到一次 null 取消通知：ClientTargetResponsePresent 變為 1，回應為空。已完成的選取不會再次通知。

專案原始碼: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 函式 `TargetLast`.

分開讀取不是原子操作。物件目標的 LastTile 保留通訊協定 X/Y=65535；土地/靜態物件的 LastTile(1)/(2) 讀取 X/Y。無括號的 lasttarget 是動態內建值，但可被同名變數遮蔽。


## 範例

### 讀取保存值

```vb
# 讀取保存值
#
# 讀取最後選擇目標時保存的 Y。
#
# Integer — 保存的 Y 座標，不是像素或 Boolean。選擇前、Clear 後或未知物件為 0；實際座標 0 也有效。LastTarget()=0 時仍可取得土地/靜態物件座標。

SUB Main()
    # value 為結果；HEX 顯示 ID，CStr 顯示座標。不進行選擇。

    VAR value = UO.LastTargetY()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**參數與執行說明:**

- value 為結果；HEX 顯示 ID，CStr 顯示座標。不進行選擇。

### 比較保存位置與目前位置

```vb
# 比較保存位置與目前位置
#
# 讀取最後選擇目標時保存的 Y。
#
# Integer — 保存的 Y 座標，不是像素或 Boolean。選擇前、Clear 後或未知物件為 0；實際座標 0 也有效。LastTarget()=0 時仍可取得土地/靜態物件座標。

SUB Main()
    # id 是保存的 serial。GetX/GetY 前先用 Exists；兩組位置可能不同。ID=0 不能證明已選過某個點。

    VAR id = UO.LastTarget()
    VAR x = UO.LastTargetX()
    VAR y = UO.LastTargetY()
    UO.Print('Saved XY: ' + CStr(x) + ',' + CStr(y))
    IF id <> 0 AND UO.Exists(id) THEN
        UO.Print('Live XY: ' + CStr(UO.GetX(id)) + ',' + CStr(UO.GetY(id)))
    END IF
END SUB
```

**參數與執行說明:**

- id 是保存的 serial。GetX/GetY 前先用 Exists；兩組位置可能不同。ID=0 不能證明已選過某個點。

### 完整的 ReadTargetValue 輔助函式

```vb
# 完整的 ReadTargetValue 輔助函式
#
# 讀取最後選擇目標時保存的 Y。
#
# Integer — 保存的 Y 座標，不是像素或 Boolean。選擇前、Clear 後或未知物件為 0；實際座標 0 也有效。LastTarget()=0 時仍可取得土地/靜態物件座標。

SUB Main()
    # minimum/maximum 設定輔助函式的篩選範圍，不是 API 參數。-1 是其自訂越界訊號。ID 版本保留任何非零 serial 及最高位元。

    VAR value = ReadTargetValue(0,65535)
    UO.Print('Checked value: ' + CStr(value))
END SUB

SUB ReadTargetValue(minimum,maximum)
    VAR value = UO.LastTargetY()
    IF value < minimum OR value > maximum THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**參數與執行說明:**

- minimum/maximum 設定輔助函式的篩選範圍，不是 API 參數。-1 是其自訂越界訊號。ID 版本保留任何非零 serial 及最高位元。
