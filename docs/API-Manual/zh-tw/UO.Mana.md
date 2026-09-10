# UO.Mana

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

從本機模型讀取目前魔力。

## 完整語法

```text
UO.Mana() -> Any
```

## 參數

沒有參數。

## 傳回值

Integer — 欄位 Mana 的值，不是百分比或 Boolean。0 可能是真實數值，也可能表示缺少資料。不能以 0 的最大值作為除數。 其他 mobile 的數值可能未知。HP/HitsMax 可能是伺服器的相對刻度，而非精確點數。HP=0 不能證明死亡；請用 Dead/IsDead。

## 行為

- 不開啟 status，也不要求伺服器更新。與 Stealth 自動要求缺失 HP 的行為不同，此客戶端僅讀取既有資料。不改變屬性，也不傳送封包。
- 每個結果都是獨立讀取。Exists 與下一次呼叫之間世界可能改變；多次查詢不是不可分割的快照。
- 讀取物件時，World.Get 排除不存在或 IsDestroyed 的記錄並得到 0。HP/HitsMax 讀取 Entity，包括具有這些欄位的物品；Mana/Stamina 必須是 Mobile。省略引數時讀取 self。無引數名稱不一定有 ID 形式，請查看簽章。
- 無參數讀取也會在 Player 不存在或已銷毀時回傳 0。這包含直接的 Mana/Stamina 及其最大值，不限於經由 World.Get 的形式。仍存在的死亡角色可能保留數值。

### 內部函式：從呼叫到結果

以下為實際的 C# 內部步驟。ReadValue 是範例中完整定義的輔助函式，不是隱藏的內建命令。

#### 1. RegisterCharacterGetterAliases

建立 runtime 時，RegisterCharacterGetterAliases 登錄名稱與呼叫形式。沒有引數時使用 bridge.Self；有引數時使用選定的 serial。既有登錄保持不變。

Integer — 欄位 Mana 的值，不是百分比或 Boolean。0 可能是真實數值，也可能表示缺少資料。不能以 0 的最大值作為除數。 其他 mobile 的數值可能未知。HP/HitsMax 可能是伺服器的相對刻度，而非精確點數。HP=0 不能證明死亡；請用 Dead/IsDead。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `RegisterCharacterGetterAliases`.

#### 2. Invoke

Invoke 在遊戲執行緒讀取；工作執行緒等待管理器處理請求。取消腳本會中斷等待。不增加額外延遲或網路查詢。

每個結果都是獨立讀取。Exists 與下一次呼叫之間世界可能改變；多次查詢不是不可分割的快照。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

不開啟 status，也不要求伺服器更新。與 Stealth 自動要求缺失 HP 的行為不同，此客戶端僅讀取既有資料。不改變屬性，也不傳送封包。


## 範例

### 顯示自己的角色數值

```vb
# 顯示自己的角色數值
#
# 從本機模型讀取目前魔力。
#
# Integer — 欄位 Mana 的值，不是百分比或 Boolean。0 可能是真實數值，也可能表示缺少資料。不能以 0 的最大值作為除數。 其他 mobile
# 的數值可能未知。HP/HitsMax 可能是伺服器的相對刻度，而非精確點數。HP=0 不能證明死亡；請用 Dead/IsDead。

SUB Main()
    # 無引數呼叫讀取 self。value 儲存一個數字，STR 只將它轉成訊息文字。

    VAR value = UO.Mana()
    UO.Print('Mana: ' + STR(value))
END SUB
```

**參數與執行說明:**

- 無引數呼叫讀取 self。value 儲存一個數字，STR 只將它轉成訊息文字。

### 將數值用於條件或計算

```vb
# 將數值用於條件或計算
#
# 從本機模型讀取目前魔力。
#
# Integer — 欄位 Mana 的值，不是百分比或 Boolean。0 可能是真實數值，也可能表示缺少資料。不能以 0 的最大值作為除數。 其他 mobile
# 的數值可能未知。HP/HitsMax 可能是伺服器的相對刻度，而非精確點數。HP=0 不能證明死亡；請用 Dead/IsDead。

SUB Main()
    # 範例對此欄位套用門檻或計算。條件中的數字是範例設定，不是伺服器限制。除法前會檢查最大值是否大於 0。

    VAR value = UO.Mana()
    IF value >= 10 THEN
        UO.Print('At least ten mana points are known')
    END IF
END SUB
```

**參數與執行說明:**

- 範例對此欄位套用門檻或計算。條件中的數字是範例設定，不是伺服器限制。除法前會檢查最大值是否大於 0。

### 完整的 ReadValue 輔助函式

```vb
# 完整的 ReadValue 輔助函式
#
# 從本機模型讀取目前魔力。
#
# Integer — 欄位 Mana 的值，不是百分比或 Boolean。0 可能是真實數值，也可能表示缺少資料。不能以 0 的最大值作為除數。 其他 mobile
# 的數值可能未知。HP/HitsMax 可能是伺服器的相對刻度，而非精確點數。HP=0 不能證明死亡；請用 Dead/IsDead。

SUB Main()
    # 此名稱沒有 ID 形式。無參數 ReadValue 讀取 self，兩次呼叫之間使用 WAIT(1000)。比較兩個快照可能漏掉中途變化。

    VAR before = ReadValue()
    WAIT(1000)
    VAR after = ReadValue()
    UO.Print('Before: ' + CStr(before) + '; after: ' + CStr(after))
END SUB

SUB ReadValue()
    RETURN UO.Mana()
END SUB
```

**參數與執行說明:**

- 此名稱沒有 ID 形式。無參數 ReadValue 讀取 self，兩次呼叫之間使用 WAIT(1000)。比較兩個快照可能漏掉中途變化。
