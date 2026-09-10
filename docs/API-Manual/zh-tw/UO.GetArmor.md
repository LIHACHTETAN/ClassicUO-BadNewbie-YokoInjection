# UO.GetArmor

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取目前玩家的抗性欄位：物理護甲／抗性。

## 完整語法

```text
UO.GetArmor() -> Integer
```

## 參數

沒有參數。

## 傳回值

Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

## 行為

- 本指令無參數。請使用上方精確語法。
- 在遊戲執行緒讀取 Player.PhysicalResistance；目前 Player 不存在或已銷毀時回傳 0。不搜尋裝備、不重算加成、不要求狀態封包，也不等待更新。仍存在的鬼魂不等於已銷毀的 Player。
- PhysicalResistance 是伺服器的護甲／狀態欄位：傳統規則可能採護甲評分，抗性規則則採物理抗性。API 不轉換規則，也不計算傷害減免百分比。Armor 與物理抗性別名讀取相同欄位。
- CharacterStatus 先驗證固定內容，再修改資料並將抗性 word 轉為有號 Int16。固定內容截斷時保留原資料。type 6 的選用尾段保留既有處理方式；這些查詢不讀取尾段的抗性上限。
- 每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。
- RegisterCharacterGetterAliases 補上缺少的無參數函式與內建名稱；既有相容分支讀取同一欄位。名稱不區分大小寫；不帶括號的內建名稱在未被變數遮蔽時會重新讀取。

### 內部函式：從呼叫到結果

以下是本機讀取的實際原生步驟。ResistanceAtLeast 是下方完整定義的使用者 BASIC 函式，不是隱藏 API，也不是裝備防具的命令。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases 補上缺少的無參數函式與內建名稱；既有相容分支讀取同一欄位。名稱不區分大小寫；不帶括號的內建名稱在未被變數遮蔽時會重新讀取。

`Armor PhysicalResist ResistPhysical GetArmor GetPhysicalResist GetResistPhysical`.

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `RegisterCharacterGetterAliases`.

#### 2. Invoke

在遊戲執行緒讀取 Player.PhysicalResistance；目前 Player 不存在或已銷毀時回傳 0。不搜尋裝備、不重算加成、不要求狀態封包，也不等待更新。仍存在的鬼魂不等於已銷毀的 Player。

Invoke 在遊戲執行緒讀取，等待可隨腳本取消。不會請求 status、開啟 target、傳送封包、修改屬性或加入內建延遲。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 3. CharacterStatus

CharacterStatus 先驗證固定內容，再修改資料並將抗性 word 轉為有號 Int16。固定內容截斷時保留原資料。type 6 的選用尾段保留既有處理方式；這些查詢不讀取尾段的抗性上限。

PhysicalResistance 是伺服器的護甲／狀態欄位：傳統規則可能採護甲評分，抗性規則則採物理抗性。API 不轉換規則，也不計算傷害減免百分比。Armor 與物理抗性別名讀取相同欄位。

專案原始碼: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 函式 `CharacterStatus`.

#### 4. Clear

World.Clear 移除 Player。玩家及其資料重新可用之前回傳 0。重連後不能用舊值證明符合需求。

Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

專案原始碼: `src/ClassicUO.Client/Game/World.cs`; 函式 `Clear`.

每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。


## 範例

### 顯示快取值

```vb
# 顯示快取值
#
# 讀取目前玩家的抗性欄位：物理護甲／抗性。
#
# Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist
# 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

SUB Main()
    # value 儲存一次無參數的玩家查詢；CStr 將結果格式化為日誌文字。

    VAR value = UO.GetArmor()
    UO.Print('PhysicalResistance: ' + CStr(value))
END SUB
```

**參數與執行說明:**

- value 儲存一次無參數的玩家查詢；CStr 將結果格式化為日誌文字。

### 比較兩次觀察

```vb
# 比較兩次觀察
#
# 讀取目前玩家的抗性欄位：物理護甲／抗性。
#
# Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist
# 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

SUB Main()
    # WAIT(500) 使 before 與 after 相隔 500 毫秒；difference 可為負值，可能漏掉中途更新。等待屬於範例，不是 API 延遲。

    VAR before = UO.GetArmor()
    WAIT(500)
    VAR after = UO.GetArmor()
    VAR difference = after - before
    UO.Print('Resistance change: ' + CStr(difference))
END SUB
```

**參數與執行說明:**

- WAIT(500) 使 before 與 after 相隔 500 毫秒；difference 可為負值，可能漏掉中途更新。等待屬於範例，不是 API 延遲。

### 完整的最低抗性檢查函式

```vb
# 完整的最低抗性檢查函式
#
# 讀取目前玩家的抗性欄位：物理護甲／抗性。
#
# Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist
# 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

SUB Main()
    # minimum=50 是範例需求，不是上限。ResistanceAtLeast 先拒絕不存在的 Player，再讀取一次，依 value >= minimum 回傳 Integer
    # Boolean：1=TRUE 或 0=FALSE。抗性值本身不是 Boolean。下方提供完整定義。

    IF ResistanceAtLeast(50) = TRUE THEN
        UO.Print('Local resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetArmor()
    RETURN value >= minimum
END SUB
```

**參數與執行說明:**

- minimum=50 是範例需求，不是上限。ResistanceAtLeast 先拒絕不存在的 Player，再讀取一次，依 value >= minimum 回傳 Integer Boolean：1=TRUE 或 0=FALSE。抗性值本身不是 Boolean。下方提供完整定義。
