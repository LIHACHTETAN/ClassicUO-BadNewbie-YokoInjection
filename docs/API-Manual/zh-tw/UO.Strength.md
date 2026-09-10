# UO.Strength

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取目前力量（Strength、STR）。

## 完整語法

```text
UO.Strength() -> Integer
```

## 參數

沒有參數。

## 傳回值

Integer：模型中的目前屬性點數，範圍 0..65535；不是百分比、ID、技能值、鎖定模式或 Boolean。0 也可能表示玩家不存在／已銷毀或對象資料不可用。應比較數值需求，不是 = TRUE。這不是屬性上限，也不保證是未經加成的基礎值。

## 行為

- 本指令無參數。請使用上方精確語法。
- Player 存在且未銷毀時讀取 Player.Strength，否則為 0。仍存在的死亡角色不是已銷毀物件。不會從 HP、法力或耐力推算此屬性。
- GetStr/GetInt/GetDex 接受 ObjID，但此客戶端只在 PlayerMobile 儲存這些屬性：其他 serial 一律回傳 0，即使 mobile 已載入。這是相對於 Stealth 一般說明的限制；不會虛構其他角色的屬性。
- Invoke 在遊戲執行緒讀取，等待可隨腳本取消。不會請求 status、開啟 target、傳送封包、修改屬性或加入內建延遲。
- 每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。
- 以下名稱等價，可有或無 UO.，不區分大小寫： `Str Strength GetStr GetStrength`.
- 不帶 UO. 的 Int(value) 將 BASIC 數字向下取整；Str(value) 將值格式化為文字。它們不同於讀取屬性的 UO.Int()/UO.Str()。GetInt(ObjID) 不會進行數字取整。

### 內部函式：從呼叫到結果

以下為原生讀取階段。AttributeAtLeast 是下方完整定義的使用者 BASIC 輔助函式，不是隱藏 API，也不修改屬性。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases 註冊缺少的無參數函式與內建名稱。既有相容分支選擇自己的 getter；兩條路徑都回傳 Integer。無括號的內建名稱每次重讀，除非被腳本變數遮蔽。

以下名稱等價，可有或無 UO.，不區分大小寫： `Str Strength GetStr GetStrength`.

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `RegisterCharacterGetterAliases`.

#### 2. Invoke

Player 存在且未銷毀時讀取 Player.Strength，否則為 0。仍存在的死亡角色不是已銷毀物件。不會從 HP、法力或耐力推算此屬性。 Invoke 在遊戲執行緒讀取，等待可隨腳本取消。不會請求 status、開啟 target、傳送封包、修改屬性或加入內建延遲。

Integer：模型中的目前屬性點數，範圍 0..65535；不是百分比、ID、技能值、鎖定模式或 Boolean。0 也可能表示玩家不存在／已銷毀或對象資料不可用。應比較數值需求，不是 = TRUE。這不是屬性上限，也不保證是未經加成的基礎值。 每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 3. CharacterStatus

CharacterStatus 處理適用的自身 status 封包時，將收到的 STR/DEX/INT 欄位寫入 Player.Strength。查詢只讀此快取，不等待新封包。

Invoke 在遊戲執行緒讀取，等待可隨腳本取消。不會請求 status、開啟 target、傳送封包、修改屬性或加入內建延遲。

專案原始碼: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 函式 `CharacterStatus`.

#### 4. Clear

World.Clear 移除 Player。玩家及其資料重新可用之前回傳 0。重連後不能用舊值證明符合需求。

Integer：模型中的目前屬性點數，範圍 0..65535；不是百分比、ID、技能值、鎖定模式或 Boolean。0 也可能表示玩家不存在／已銷毀或對象資料不可用。應比較數值需求，不是 = TRUE。這不是屬性上限，也不保證是未經加成的基礎值。

專案原始碼: `src/ClassicUO.Client/Game/World.cs`; 函式 `Clear`.

World.Clear 移除 Player。玩家及其資料重新可用之前回傳 0。重連後不能用舊值證明符合需求。


## 範例

### 讀取並顯示點數

```vb
# 讀取並顯示點數
#
# 讀取目前力量（Strength、STR）。
#
# Integer：模型中的目前屬性點數，範圍 0..65535；不是百分比、ID、技能值、鎖定模式或 Boolean。0 也可能表示玩家不存在／已銷毀或對象資料不可用。應比較數值需求，不是
# = TRUE。這不是屬性上限，也不保證是未經加成的基礎值。

SUB Main()
    # value 保存數值；CStr 僅格式化日誌文字。沒有傳入參數或角色動作。

    VAR value = UO.Strength()
    UO.Print('Strength: ' + CStr(value))
END SUB
```

**參數與執行說明:**

- value 保存數值；CStr 僅格式化日誌文字。沒有傳入參數或角色動作。

### 比較兩次觀測

```vb
# 比較兩次觀測
#
# 讀取目前力量（Strength、STR）。
#
# Integer：模型中的目前屬性點數，範圍 0..65535；不是百分比、ID、技能值、鎖定模式或 Boolean。0 也可能表示玩家不存在／已銷毀或對象資料不可用。應比較數值需求，不是
# = TRUE。這不是屬性上限，也不保證是未經加成的基礎值。

SUB Main()
    # before/after 間隔 1000 毫秒；WAIT 屬於範例。change=after-before 可為正、零或負，無法單獨區分所有中途更新或斷線。

    VAR before = UO.Strength()
    WAIT(1000)
    VAR after = UO.Strength()
    VAR change = after - before
    UO.Print('Change: ' + CStr(change))
END SUB
```

**參數與執行說明:**

- before/after 間隔 1000 毫秒；WAIT 屬於範例。change=after-before 可為正、零或負，無法單獨區分所有中途更新或斷線。

### 完整需求檢查函式

```vb
# 完整需求檢查函式
#
# 讀取目前力量（Strength、STR）。
#
# Integer：模型中的目前屬性點數，範圍 0..65535；不是百分比、ID、技能值、鎖定模式或 Boolean。0 也可能表示玩家不存在／已銷毀或對象資料不可用。應比較數值需求，不是
# = TRUE。這不是屬性上限，也不保證是未經加成的基礎值。

SUB Main()
    # minimum=80 是範例需求，不是客戶端上限。AttributeAtLeast(minimum) 先排除不存在的玩家，再讀一次屬性，以 >= minimum 回傳 Integer
    # Boolean 1=TRUE 或 0=FALSE。邏輯結果來自比較，不是屬性本身。

    IF AttributeAtLeast(80) = TRUE THEN
        UO.Print('Requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB AttributeAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.Strength()
    RETURN value >= minimum
END SUB
```

**參數與執行說明:**

- minimum=80 是範例需求，不是客戶端上限。AttributeAtLeast(minimum) 先排除不存在的玩家，再讀一次屬性，以 >= minimum 回傳 Integer Boolean 1=TRUE 或 0=FALSE。邏輯結果來自比較，不是屬性本身。
