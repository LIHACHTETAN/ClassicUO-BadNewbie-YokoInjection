# UO.GetResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

以數字或名稱選擇並讀取目前玩家的一項抗性。

## 完整語法

```text
UO.GetResist(resistance:Any) -> Integer
```

## 參數

- `resistance` — resistance 必填。數字：0=physical、1=fire、2=cold、3=poison、4=energy。字串：physical/phys/armor、fire、cold、poison、energy。忽略大小寫與前後空白。不接受 serial、type、hue、目標游標或第二個參數。

## 傳回值

Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

## 行為

- 先判斷值的種類：字串 "1" 與 "0" 是未知名稱，回傳 0，不是數字選擇值。非字串 Decimal 朝零截斷：1.9 -> fire，-0.9 -> physical。TRUE=1 選 fire，FALSE=0 選 physical；Array/Unit 也轉為 0。請使用明確整數或支援的名稱。不解析 AddObject 名稱。
- GetResistance 只選一個 bridge getter；未知數字／名稱直接回傳 Integer 0，不讀取欄位。不會一次原子讀取五項抗性，也不修改抗性。
- PhysicalResistance 是伺服器的護甲／狀態欄位：傳統規則可能採護甲評分，抗性規則則採物理抗性。API 不轉換規則，也不計算傷害減免百分比。Armor 與物理抗性別名讀取相同欄位。
- 元素抗性由 CharacterStatus（0x11）的 type >= 4 封包提供。查詢本身不檢查伺服器年代。精簡／舊式封包缺少這些欄位時保留先前快取；新 Player 初始為 0。毒素抗性不是 Poisoned 標記；這些值也不是 Resisting Spells 技能。
- CharacterStatus 先驗證固定內容，再修改資料並將抗性 word 轉為有號 Int16。固定內容截斷時保留原資料。type 6 的選用尾段保留既有處理方式；這些查詢不讀取尾段的抗性上限。
- Invoke 在遊戲執行緒讀取，等待可隨腳本取消。不會請求 status、開啟 target、傳送封包、修改屬性或加入內建延遲。
- 每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。

### 內部函式：從呼叫到結果

以下是本機讀取的實際原生步驟。ResistanceAtLeast 是下方完整定義的使用者 BASIC 函式，不是隱藏 API，也不是裝備防具的命令。

#### 1. RegisterCharacterGetterAliases

將 GetResist(resistance) 與 UO.GetResist(resistance) 註冊為連到 GetResistance 的單參數函式。此選擇器沒有無參數內建值。

resistance 必填。數字：0=physical、1=fire、2=cold、3=poison、4=energy。字串：physical/phys/armor、fire、cold、poison、energy。忽略大小寫與前後空白。不接受 serial、type、hue、目標游標或第二個參數。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `RegisterCharacterGetterAliases`.

#### 2. GetResistance

先判斷值的種類：字串 "1" 與 "0" 是未知名稱，回傳 0，不是數字選擇值。非字串 Decimal 朝零截斷：1.9 -> fire，-0.9 -> physical。TRUE=1 選 fire，FALSE=0 選 physical；Array/Unit 也轉為 0。請使用明確整數或支援的名稱。不解析 AddObject 名稱。

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`. GetResistance 只選一個 bridge getter；未知數字／名稱直接回傳 Integer 0，不讀取欄位。不會一次原子讀取五項抗性，也不修改抗性。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `GetResistance`.

#### 3. ToInt

此處 ToInt 只接收非字串選擇值：Integer 不變，Decimal 朝零截斷，Array/Unit 變成 0。回傳的是選擇索引，不是抗性。字串名稱由 GetResistance 處理。

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`.

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/NumberConversions.cs`; 函式 `ToInt`.

#### 4. Invoke

Invoke 依上表讀取選定的 Player 欄位並保留正負號。Player 不存在／已銷毀時為 0。不要求狀態封包，也不等待新資料。

Invoke 在遊戲執行緒讀取，等待可隨腳本取消。不會請求 status、開啟 target、傳送封包、修改屬性或加入內建延遲。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 5. CharacterStatus

CharacterStatus 先驗證固定內容，再修改資料並將抗性 word 轉為有號 Int16。固定內容截斷時保留原資料。type 6 的選用尾段保留既有處理方式；這些查詢不讀取尾段的抗性上限。

PhysicalResistance 是伺服器的護甲／狀態欄位：傳統規則可能採護甲評分，抗性規則則採物理抗性。API 不轉換規則，也不計算傷害減免百分比。Armor 與物理抗性別名讀取相同欄位。 元素抗性由 CharacterStatus（0x11）的 type >= 4 封包提供。查詢本身不檢查伺服器年代。精簡／舊式封包缺少這些欄位時保留先前快取；新 Player 初始為 0。毒素抗性不是 Poisoned 標記；這些值也不是 Resisting Spells 技能。

專案原始碼: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 函式 `CharacterStatus`.

#### 6. Clear

World.Clear 移除 Player。玩家及其資料重新可用之前回傳 0。重連後不能用舊值證明符合需求。

Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

專案原始碼: `src/ClassicUO.Client/Game/World.cs`; 函式 `Clear`.

每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。


## 範例

### 以混合大小寫名稱選擇

```vb
# 以混合大小寫名稱選擇
#
# 以數字或名稱選擇並讀取目前玩家的一項抗性。
#
# Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist
# 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

SUB Main()
    # resistance=" FiRe " 忽略前後空白與大小寫後選擇火焰。value 仍是有號數值；不開啟目標游標。

    VAR value = UO.GetResist(' FiRe ')
    UO.Print('Fire resistance: ' + CStr(value))
END SUB
```

**參數與執行說明:**

- resistance=" FiRe " 忽略前後空白與大小寫後選擇火焰。value 仍是有號數值；不開啟目標游標。

### 比較數字與字串選擇值

```vb
# 比較數字與字串選擇值
#
# 以數字或名稱選擇並讀取目前玩家的一項抗性。
#
# Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist
# 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

SUB Main()
    # 2 選寒冷，"poison" 選毒素；它們不是 serial。兩個快照的比較結果為 Boolean；毒素抗性不代表是否中毒。

    VAR cold = UO.GetResist(2)
    VAR poison = UO.GetResist('poison')
    IF cold < poison THEN
        UO.Print('Cold resistance is lower')
    ELSE
        UO.Print('Cold resistance is equal or higher')
    END IF
END SUB
```

**參數與執行說明:**

- 2 選寒冷，"poison" 選毒素；它們不是 serial。兩個快照的比較結果為 Boolean；毒素抗性不代表是否中毒。

### 完整的最低抗性檢查函式

```vb
# 完整的最低抗性檢查函式
#
# 以數字或名稱選擇並讀取目前玩家的一項抗性。
#
# Integer — 用戶端模型中的有號狀態值，範圍 -32768..32767，保留負值。0 可能是真實抗性、尚無資料或 Player 不存在／已銷毀；GetResist
# 的未知選擇值也回傳 0。不是 Boolean、ID、技能或抗性上限。1 表示一點，不代表操作成功。

SUB Main()
    # minimum=50 是範例需求，不是上限。ResistanceAtLeast 先拒絕不存在的 Player，再讀取一次，依 value >= minimum 回傳 Integer
    # Boolean：1=TRUE 或 0=FALSE。抗性值本身不是 Boolean。下方提供完整定義。
    # 函式將 selector 原樣傳入 GetResist；範例使用 "fire"。函式檢查 Player 是否存在，但不驗證任意選擇值，也不保證狀態是最新的。請使用上列選擇值。

    IF ResistanceAtLeast('fire', 50) = TRUE THEN
        UO.Print('Local fire resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(selector, minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetResist(selector)
    RETURN value >= minimum
END SUB
```

**參數與執行說明:**

- minimum=50 是範例需求，不是上限。ResistanceAtLeast 先拒絕不存在的 Player，再讀取一次，依 value >= minimum 回傳 Integer Boolean：1=TRUE 或 0=FALSE。抗性值本身不是 Boolean。下方提供完整定義。
- 函式將 selector 原樣傳入 GetResist；範例使用 "fire"。函式檢查 Player 是否存在，但不驗證任意選擇值，也不保證狀態是最新的。請使用上列選擇值。
