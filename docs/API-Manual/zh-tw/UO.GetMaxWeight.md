# UO.GetMaxWeight

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取目前玩家的狀態計數值：最大重量（stones）。

## 完整語法

```text
UO.GetMaxWeight() -> Integer
```

## 參數

沒有參數。

## 傳回值

Integer — 最大重量（stones），模型範圍 0..65535。0 可能是真實值、未知資料或 Player 不存在／已銷毀。這是數量，不是 Boolean、ID 或 type：1 表示一單位，不代表成功。不列舉物件，也不回傳陣列。

## 行為

- 本指令無參數。請使用上方精確語法。
- 在遊戲執行緒讀取 Player.WeightMax；目前 Player 不存在或已銷毀時回傳 0。不搜尋裝備、不重算加成、不要求狀態封包，也不等待更新。仍存在的鬼魂不等於已銷毀的 Player。
- MaxWeight 讀取 WeightMax 快取。自身狀態 type >= 5 使用伺服器提供的 UInt16 上限，包括 0。較舊的擴充狀態在收到時計算一次：UO 通訊協定 >= 5.0.0a 使用 7 * floor(STR / 2) + 40；更舊的使用 STR * 4 + 25。結果以 UInt16 儲存，極端值會依模數 65536 回繞。STR=101 分別得到 390 或 429。STR 單獨變更時，getter 不重新計算。
- CharacterStatus 先驗證固定內容再更新。Weight 來自自身擴充狀態，控制欄位從 type 3、Luck 從 type 4、伺服器 WeightMax 從 type 5 開始提供。精簡／舊式封包沒有選用計數值時保留舊快取。新 Player 從零開始；呼叫不代表已取得最新狀態。
- RegisterCharacterGetterAliases 補上缺少的無參數函式與內建名稱；既有相容分支讀取同一欄位。名稱不區分大小寫；不帶括號的內建名稱在未被變數遮蔽時會重新讀取。
- 每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。

### 內部函式：從呼叫到結果

以下是讀取狀態快取的原生步驟。範例完整定義的 CanCarry、LuckAtLeast 或 CanAddFollower 是使用者 BASIC 函式，不是隱藏的原生操作，不會修改背包或寵物。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases 補上缺少的無參數函式與內建名稱；既有相容分支讀取同一欄位。名稱不區分大小寫；不帶括號的內建名稱在未被變數遮蔽時會重新讀取。

`MaxWeight GetMaxWeight`.

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `RegisterCharacterGetterAliases`.

#### 2. Invoke

在遊戲執行緒讀取 Player.WeightMax；目前 Player 不存在或已銷毀時回傳 0。不搜尋裝備、不重算加成、不要求狀態封包，也不等待更新。仍存在的鬼魂不等於已銷毀的 Player。

Invoke 在遊戲執行緒讀取，等待可隨腳本取消。不會請求 status、開啟 target、傳送封包、修改屬性或加入內建延遲。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 3. CharacterStatus

CharacterStatus 先驗證固定內容再更新。Weight 來自自身擴充狀態，控制欄位從 type 3、Luck 從 type 4、伺服器 WeightMax 從 type 5 開始提供。精簡／舊式封包沒有選用計數值時保留舊快取。新 Player 從零開始；呼叫不代表已取得最新狀態。

MaxWeight 讀取 WeightMax 快取。自身狀態 type >= 5 使用伺服器提供的 UInt16 上限，包括 0。較舊的擴充狀態在收到時計算一次：UO 通訊協定 >= 5.0.0a 使用 7 * floor(STR / 2) + 40；更舊的使用 STR * 4 + 25。結果以 UInt16 儲存，極端值會依模數 65536 回繞。STR=101 分別得到 390 或 429。STR 單獨變更時，getter 不重新計算。

專案原始碼: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 函式 `CharacterStatus`.

#### 4. Clear

World.Clear 移除 Player。玩家及其資料重新可用之前回傳 0。重連後不能用舊值證明符合需求。

Integer — 最大重量（stones），模型範圍 0..65535。0 可能是真實值、未知資料或 Player 不存在／已銷毀。這是數量，不是 Boolean、ID 或 type：1 表示一單位，不代表成功。不列舉物件，也不回傳陣列。

專案原始碼: `src/ClassicUO.Client/Game/World.cs`; 函式 `Clear`.

每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。


## 範例

### 顯示快取計數值

```vb
# 顯示快取計數值
#
# 讀取目前玩家的狀態計數值：最大重量（stones）。
#
# Integer — 最大重量（stones），模型範圍 0..65535。0 可能是真實值、未知資料或 Player 不存在／已銷毀。這是數量，不是 Boolean、ID 或 type：1
# 表示一單位，不代表成功。不列舉物件，也不回傳陣列。

SUB Main()
    # value 儲存一次無參數的自身查詢；CStr 僅格式化為日誌文字，不改變數值意義。

    VAR value = UO.GetMaxWeight()
    UO.Print('WeightMax: ' + CStr(value))
END SUB
```

**參數與執行說明:**

- value 儲存一次無參數的自身查詢；CStr 僅格式化為日誌文字，不改變數值意義。

### 觀察變化

```vb
# 觀察變化
#
# 讀取目前玩家的狀態計數值：最大重量（stones）。
#
# Integer — 最大重量（stones），模型範圍 0..65535。0 可能是真實值、未知資料或 Player 不存在／已銷毀。這是數量，不是 Boolean、ID 或 type：1
# 表示一單位，不代表成功。不列舉物件，也不回傳陣列。

SUB Main()
    # WAIT(500) 使 before 與 after 相隔 500 毫秒。difference 可為正、零或負；可能漏掉中途更新與角色切換。等待屬於此範例。

    VAR before = UO.GetMaxWeight()
    WAIT(500)
    VAR after = UO.GetMaxWeight()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**參數與執行說明:**

- WAIT(500) 使 before 與 after 相隔 500 毫秒。difference 可為正、零或負；可能漏掉中途更新與角色切換。等待屬於此範例。

### 完整判斷函式

```vb
# 完整判斷函式
#
# 讀取目前玩家的狀態計數值：最大重量（stones）。
#
# Integer — 最大重量（stones），模型範圍 0..65535。0 可能是真實值、未知資料或 Player 不存在／已銷毀。這是數量，不是 Boolean、ID 或 type：1
# 表示一單位，不代表成功。不列舉物件，也不回傳陣列。

SUB Main()
    # CanCarry(extra) 接受額外 stones 重量；10 是範例，不是堆疊數量。拒絕負的 extra、沒有 Player 或 maximum <= 0；讀取目前值與上限，再依
    # extra <= maximum - current 回傳 Integer Boolean：1=TRUE 或 0=FALSE。減法避免 current + extra 溢位。已超重時即使
    # extra=0 也為 false。這是本機估計，不是伺服器許可；讀取不具原子性，零重量也可能未知。

    IF CanCarry(10) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanCarry(extra)
    IF extra < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.Weight()
    VAR maximum = UO.GetMaxWeight()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extra <= maximum - current
END SUB
```

**參數與執行說明:**

- CanCarry(extra) 接受額外 stones 重量；10 是範例，不是堆疊數量。拒絕負的 extra、沒有 Player 或 maximum <= 0；讀取目前值與上限，再依 extra <= maximum - current 回傳 Integer Boolean：1=TRUE 或 0=FALSE。減法避免 current + extra 溢位。已超重時即使 extra=0 也為 false。這是本機估計，不是伺服器許可；讀取不具原子性，零重量也可能未知。
