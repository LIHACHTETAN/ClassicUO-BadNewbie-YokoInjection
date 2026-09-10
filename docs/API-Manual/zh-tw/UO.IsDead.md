# UO.IsDead

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

檢查 mobile 是否死亡。

## 完整語法

```text
UO.IsDead() -> Integer
UO.IsDead(ObjID:Any) -> Any
```

## 參數

- `ObjID` — 所列呼叫形式中的選用物件：數字或十六進位字串 serial、self、lasttarget，或已登錄的 AddObject 名稱。不是 type。省略時讀取 self。某些形式會因未知文字而產生轉換錯誤；請先檢查名稱。

## 傳回值

Integer Boolean：1 = TRUE，0 = FALSE。可與數字或不加引號的邏輯常數比較。 mobile 具有 IsDead 時回傳 1；否則或 mobile 不存在時回傳 0。僅有 HP=0 並不表示死亡。

這是邏輯結果：1 = TRUE，0 = FALSE。以 VAR result = command(...) 儲存後，可用 IF result = TRUE THEN 或 IF result = 1 THEN；否定結果用 IF result = FALSE THEN 或 IF result = 0 THEN。TRUE/FALSE 不加引號。只呼叫一次並儲存結果；重複呼叫可能再次執行動作或讀取已變更的狀態。

## 行為

- 讀取本機模型：不開啟 target、不要求 status、不變更旗標，也不傳送封包。已銷毀的物件即使仍留在字典中，也視為不存在。
- 每個結果都是獨立讀取。Exists 與下一次呼叫之間世界可能改變；多次查詢不是不可分割的快照。

### 內部函式：從呼叫到結果

以下為實際的 C# 內部步驟。ReadState 是範例中完整定義的輔助函式，不是隱藏的內建命令。

#### 1. RegisterCharacterGetterAliases

建立 runtime 時，RegisterCharacterGetterAliases 登錄名稱與呼叫形式。沒有引數時使用 bridge.Self；有引數時使用選定的 serial。既有登錄保持不變。

mobile 具有 IsDead 時回傳 1；否則或 mobile 不存在時回傳 0。僅有 HP=0 並不表示死亡。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject 解析數字、十六進位字串與已儲存名稱。每次呼叫都重新解析 AddObject 名稱；不搜尋 graphic/type，也不開啟互動選取。

所列呼叫形式中的選用物件：數字或十六進位字串 serial、self、lasttarget，或已登錄的 AddObject 名稱。不是 type。省略時讀取 self。某些形式會因未知文字而產生轉換錯誤；請先檢查名稱。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `TryGetObject`.

#### 3. Invoke

Invoke 在遊戲執行緒讀取；工作執行緒等待管理器處理請求。取消腳本會中斷等待。不增加額外延遲或網路查詢。

每個結果都是獨立讀取。Exists 與下一次呼叫之間世界可能改變；多次查詢不是不可分割的快照。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 4. Get

World.Get 依 serial 尋找物件，遇到 IsDestroyed 則回傳 null，再讀取 Mobile 旗標。Alive 檢查 Exists 且沒有 IsDead；物品亦可通過。self 的 Dead 讀取 Player.IsDead。

mobile 具有 IsDead 時回傳 1；否則或 mobile 不存在時回傳 0。僅有 HP=0 並不表示死亡。

專案原始碼: `src/ClassicUO.Client/Game/World.cs`; 函式 `Get`.

讀取本機模型：不開啟 target、不要求 status、不變更旗標，也不傳送封包。已銷毀的物件即使仍留在字典中，也視為不存在。


## 範例

### 檢查自己的狀態

```vb
# 檢查自己的狀態
#
# 檢查 mobile 是否死亡。
#
# Integer Boolean：1 = TRUE，0 = FALSE。可與數字或不加引號的邏輯常數比較。 mobile 具有 IsDead 時回傳 1；否則或 mobile 不存在時回傳
# 0。僅有 HP=0 並不表示死亡。
#
# 這是邏輯結果：1 = TRUE，0 = FALSE。以 VAR result = command(...) 儲存後，可用 IF result = TRUE THEN 或 IF result
# = 1 THEN；否定結果用 IF result = FALSE THEN 或 IF result = 0 THEN。TRUE/FALSE
# 不加引號。只呼叫一次並儲存結果；重複呼叫可能再次執行動作或讀取已變更的狀態。

SUB Main()
    # 空括號讀取 self。active 儲存一次結果；TRUE 和 FALSE 選擇兩個分支。Print 只顯示範例訊息。

    VAR active = UO.IsDead()
    IF active = TRUE THEN
        UO.Print('State is active')
    ELSE
        UO.Print('State is inactive or unavailable')
    END IF
END SUB
```

**參數與執行說明:**

- 空括號讀取 self。active 儲存一次結果；TRUE 和 FALSE 選擇兩個分支。Print 只顯示範例訊息。

### 選定物件與完整的 ReadState 函式

```vb
# 選定物件與完整的 ReadState 函式
#
# 檢查 mobile 是否死亡。
#
# Integer Boolean：1 = TRUE，0 = FALSE。可與數字或不加引號的邏輯常數比較。 mobile 具有 IsDead 時回傳 1；否則或 mobile 不存在時回傳
# 0。僅有 HP=0 並不表示死亡。
#
# 這是邏輯結果：1 = TRUE，0 = FALSE。以 VAR result = command(...) 儲存後，可用 IF result = TRUE THEN 或 IF result
# = 1 THEN；否定結果用 IF result = FALSE THEN 或 IF result = 0 THEN。TRUE/FALSE
# 不加引號。只呼叫一次並儲存結果；重複呼叫可能再次執行動作或讀取已變更的狀態。

SUB Main()
    # lasttarget 是先前選定的物件。Exists 檢查其是否存在。obj 是 ReadState 唯一的參數；函式原樣回傳命令結果。複製的程式碼包含完整定義。

    IF UO.Exists('lasttarget') THEN
        VAR observed = ReadState('lasttarget')
        UO.Print('State 1/0: ' + CStr(observed))
    END IF
END SUB

SUB ReadState(obj)
    RETURN UO.IsDead(obj)
END SUB
```

**參數與執行說明:**

- lasttarget 是先前選定的物件。Exists 檢查其是否存在。obj 是 ReadState 唯一的參數；函式原樣回傳命令結果。複製的程式碼包含完整定義。

### 偵測半秒內的變化

```vb
# 偵測半秒內的變化
#
# 檢查 mobile 是否死亡。
#
# Integer Boolean：1 = TRUE，0 = FALSE。可與數字或不加引號的邏輯常數比較。 mobile 具有 IsDead 時回傳 1；否則或 mobile 不存在時回傳
# 0。僅有 HP=0 並不表示死亡。
#
# 這是邏輯結果：1 = TRUE，0 = FALSE。以 VAR result = command(...) 儲存後，可用 IF result = TRUE THEN 或 IF result
# = 1 THEN；否定結果用 IF result = FALSE THEN 或 IF result = 0 THEN。TRUE/FALSE
# 不加引號。只呼叫一次並儲存結果；重複呼叫可能再次執行動作或讀取已變更的狀態。

SUB Main()
    # 兩次無引數呼叫均讀取 self；WAIT(500) 表示 500 毫秒。比較兩個快照可能漏掉中途變化，範例不會無限等待。

    VAR before = UO.IsDead()
    WAIT(500)
    VAR after = UO.IsDead()
    IF before <> after THEN
        UO.Print('State changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**參數與執行說明:**

- 兩次無引數呼叫均讀取 self；WAIT(500) 表示 500 毫秒。比較兩個快照可能漏掉中途變化，範例不會無限等待。
