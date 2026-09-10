# UO.GetSkillCap

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取從伺服器收到的技能上限。

## 完整語法

```text
UO.GetSkillCap(SkillName:Any) -> Decimal
```

## 參數

- `SkillName` — 必要的技能選擇器：客戶端資料中的名稱，例如 "Mining" 或 "Animal Lore"，或 0..Skills.Length−1 的十進位索引，可用數字或字串。名稱忽略大小寫、移除前後空白，並將 _ 換成空格。這不是物品 ID，也不是從 1 開始的索引。數字字串一律表示索引。

## 傳回值

Decimal (Double) — 技能點數，步進為 0.1，例如 95.1 而非 951。欄位 CapFixed 直接以 Double 除以 10。0 表示技能值為零，或角色/技能不存在。不是 Boolean。舊式 SkillVal/BaseVal 使用不同尺度，請勿混用。

## 行為

- Invoke 在遊戲執行緒讀取已有資料，不傳送網路封包。不使用或訓練技能。兩次查詢是獨立快照。
- 必要的技能選擇器：客戶端資料中的名稱，例如 "Mining" 或 "Animal Lore"，或 0..Skills.Length−1 的十進位索引，可用數字或字串。名稱忽略大小寫、移除前後空白，並將 _ 換成空格。這不是物品 ID，也不是從 1 開始的索引。數字字串一律表示索引。
- ExecuteStealthCompatibility 選擇分支。Text 讀取技能選擇器，Arg 讀取數字編號與模式。無法轉換的引數可能觸發轉換錯誤。

### 內部函式：從呼叫到結果

以下為實際的 C# 內部步驟。ReadValue 是範例中完整定義的輔助函式，不是隱藏的內建命令。

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility 選擇分支。Text 讀取技能選擇器，Arg 讀取數字編號與模式。無法轉換的引數可能觸發轉換錯誤。

Decimal (Double) — 技能點數，步進為 0.1，例如 95.1 而非 951。欄位 CapFixed 直接以 Double 除以 10。0 表示技能值為零，或角色/技能不存在。不是 Boolean。舊式 SkillVal/BaseVal 使用不同尺度，請勿混用。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke 在遊戲執行緒讀取；工作執行緒等待管理器處理請求。取消腳本會中斷等待。不增加額外延遲或網路查詢。

Invoke 在遊戲執行緒讀取已有資料，不傳送網路封包。不使用或訓練技能。兩次查詢是獨立快照。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe 先驗證十進位索引與範圍；否則正規化名稱，以忽略大小寫的完整匹配查找 Skill.Name。未知名稱得到 null，不開啟目標游標。

未知技能或沒有角色時回傳 −1。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `FindSkillUnsafe`.

#### 4. GetSkillValue

GetSkillValue 選擇 BaseFixed、ValueFixed 或 CapFixed，將整數十分位值除以 10d，不經過 Single 的中間捨入。

Decimal (Double) — 技能點數，步進為 0.1，例如 95.1 而非 951。欄位 CapFixed 直接以 Double 除以 10。0 表示技能值為零，或角色/技能不存在。不是 Boolean。舊式 SkillVal/BaseVal 使用不同尺度，請勿混用。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `GetSkillValue`.

Invoke 在遊戲執行緒讀取已有資料，不傳送網路封包。不使用或訓練技能。兩次查詢是獨立快照。


## 範例

### 讀取並顯示

```vb
# 讀取並顯示
#
# 讀取從伺服器收到的技能上限。
#
# Decimal (Double) — 技能點數，步進為 0.1，例如 95.1 而非 951。欄位 CapFixed 直接以 Double 除以 10。0
# 表示技能值為零，或角色/技能不存在。不是 Boolean。舊式 SkillVal/BaseVal 使用不同尺度，請勿混用。

SUB Main()
    # 範例明確設定 selector，寫入時也設定 mode。第一行以名稱選技能，或以編號選屬性。Print 僅顯示結果。

    VAR selector = 'Mining'
    VAR value = UO.GetSkillCap(selector)
    UO.Print(CStr(value))
END SUB
```

**參數與執行說明:**

- 範例明確設定 selector，寫入時也設定 mode。第一行以名稱選技能，或以編號選屬性。Print 僅顯示結果。

### 用於條件或比較

```vb
# 用於條件或比較
#
# 讀取從伺服器收到的技能上限。
#
# Decimal (Double) — 技能點數，步進為 0.1，例如 95.1 而非 951。欄位 CapFixed 直接以 Double 除以 10。0
# 表示技能值為零，或角色/技能不存在。不是 Boolean。舊式 SkillVal/BaseVal 使用不同尺度，請勿混用。

SUB Main()
    # 門檻 95.1 與模式 0/1/2 是範例設定。變更模式前檢查 −1。寫入後讀取僅查看本機副本，不等待伺服器確認。

    IF UO.GetSkillLockState('Mining') >= 0 THEN
        VAR value = UO.GetSkillCap('Mining')
        IF value >= 95.1 THEN
            UO.Print('Value >= 95.1: ' + CStr(value))
        END IF
    END IF
END SUB
```

**參數與執行說明:**

- 門檻 95.1 與模式 0/1/2 是範例設定。變更模式前檢查 −1。寫入後讀取僅查看本機副本，不等待伺服器確認。

### 完整輔助函式

```vb
# 完整輔助函式
#
# 讀取從伺服器收到的技能上限。
#
# Decimal (Double) — 技能點數，步進為 0.1，例如 95.1 而非 951。欄位 CapFixed 直接以 Double 除以 10。0
# 表示技能值為零，或角色/技能不存在。不是 Boolean。舊式 SkillVal/BaseVal 使用不同尺度，請勿混用。

SUB Main()
    # Main 後列出完整輔助函式。selector 選擇技能/屬性，mode 指定寫入模式。ReadValue/ReadMode 原樣回傳數字；ApplyMode
    # 驗證引數並執行動作，無回傳值。WAIT(1000) 分隔兩次讀取快照。

    VAR before = ReadValue('Animal_Lore')
    WAIT(1000)
    VAR after = ReadValue('Animal Lore')
    UO.Print(CStr(after - before))
END SUB

SUB ReadValue(selector)
    RETURN UO.GetSkillCap(selector)
END SUB
```

**參數與執行說明:**

- Main 後列出完整輔助函式。selector 選擇技能/屬性，mode 指定寫入模式。ReadValue/ReadMode 原樣回傳數字；ApplyMode 驗證引數並執行動作，無回傳值。WAIT(1000) 分隔兩次讀取快照。
