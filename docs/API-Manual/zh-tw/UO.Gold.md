# UO.Gold

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

讀取目前玩家 status 回報的金幣金額。

## 完整語法

```text
UO.Gold() -> Any
```

## 參數

沒有參數。

## 傳回值

Integer/Decimal：非負金額 0..4294967295。至 2147483647 為 Integer，更大時為 Decimal（Double），可精確表示每個 UInt32 整數。0 也可能表示 Player 不存在／已銷毀或未取得金額。這不是 Boolean、ID、堆疊數或背包／銀行掃描結果。

## 行為

- 無參數。讀取 CharacterStatus（0x11）快取的 Player.Gold。伺服器決定此計數器包含哪些金幣。指令不遍歷袋子，也不查詢銀行餘額。Player 不存在／已銷毀時為 0；仍存在的幽靈可能保有金額。
- ReadGoldValue 只讀一次 bridge.Gold。C# bridge 保留 Int32 簽章，傳遞 UInt32 位元。unchecked 轉換還原無號金額，小值包裝成 Integer，大值包裝成 Decimal。最高位不再使餘額變負。此轉換在本機完成，不傳封包。
- 比較大金額時保留數值結果。CInt/CLng 會轉為 32 位元 Integer。大型 BASIC 數值常值應帶小數點，例如 3000000000.0。購買前餘額可能已改變；CanAfford 只是本機檢查，不是伺服器批准。
- 每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。

### 內部函式：從呼叫到結果

以下是讀取 status 計數器及擴展無號範圍的原生階段。CanAfford 是下方完整定義的使用者 BASIC 函式，不是隱藏的購買指令。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases 補上缺少的 Gold/GetGold 函式與內建名稱。UO.Gold 相容分支及其內建值都使用 ReadGoldValue。未被變數遮蔽的內建名稱每次都重新讀取。

Integer/Decimal：非負金額 0..4294967295。至 2147483647 為 Integer，更大時為 Decimal（Double），可精確表示每個 UInt32 整數。0 也可能表示 Player 不存在／已銷毀或未取得金額。這不是 Boolean、ID、堆疊數或背包／銀行掃描結果。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `RegisterCharacterGetterAliases`.

#### 2. ReadGoldValue

ReadGoldValue 只讀一次 bridge.Gold。C# bridge 保留 Int32 簽章，傳遞 UInt32 位元。unchecked 轉換還原無號金額，小值包裝成 Integer，大值包裝成 Decimal。最高位不再使餘額變負。此轉換在本機完成，不傳封包。

比較大金額時保留數值結果。CInt/CLng 會轉為 32 位元 Integer。大型 BASIC 數值常值應帶小數點，例如 3000000000.0。購買前餘額可能已改變；CanAfford 只是本機檢查，不是伺服器批准。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `ReadGoldValue`.

#### 3. Invoke

無參數。讀取 CharacterStatus（0x11）快取的 Player.Gold。伺服器決定此計數器包含哪些金幣。指令不遍歷袋子，也不查詢銀行餘額。Player 不存在／已銷毀時為 0；仍存在的幽靈可能保有金額。

Invoke 在遊戲執行緒讀取，等待可隨腳本取消。不會請求 status、開啟 target、傳送封包、修改屬性或加入內建延遲。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 4. CharacterStatus

無參數。讀取 CharacterStatus（0x11）快取的 Player.Gold。伺服器決定此計數器包含哪些金幣。指令不遍歷袋子，也不查詢銀行餘額。Player 不存在／已銷毀時為 0；仍存在的幽靈可能保有金額。

每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。

專案原始碼: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 函式 `CharacterStatus`.

#### 5. Clear

World.Clear 移除 Player。玩家及其資料重新可用之前回傳 0。重連後不能用舊值證明符合需求。

Integer/Decimal：非負金額 0..4294967295。至 2147483647 為 Integer，更大時為 Decimal（Double），可精確表示每個 UInt32 整數。0 也可能表示 Player 不存在／已銷毀或未取得金額。這不是 Boolean、ID、堆疊數或背包／銀行掃描結果。

專案原始碼: `src/ClassicUO.Client/Game/World.cs`; 函式 `Clear`.

每次呼叫重新讀取本機資料。變數保存快照；不同呼叫可能讀到不同更新。非零結果不代表連線正常；零可能是實際數值或資料不存在。


## 範例

### 顯示回報金額

```vb
# 顯示回報金額
#
# 讀取目前玩家 status 回報的金幣金額。
#
# Integer/Decimal：非負金額 0..4294967295。至 2147483647 為 Integer，更大時為 Decimal（Double），可精確表示每個 UInt32
# 整數。0 也可能表示 Player 不存在／已銷毀或未取得金額。這不是 Boolean、ID、堆疊數或背包／銀行掃描結果。

SUB Main()
    # amount 保存一次查詢；CStr 格式化為日誌文字。不搜尋、搬動或花費金幣。

    VAR amount = UO.Gold()
    UO.Print('Status gold: ' + CStr(amount))
END SUB
```

**參數與執行說明:**

- amount 保存一次查詢；CStr 格式化為日誌文字。不搜尋、搬動或花費金幣。

### 包含高價的完整 CanAfford

```vb
# 包含高價的完整 CanAfford
#
# 讀取目前玩家 status 回報的金幣金額。
#
# Integer/Decimal：非負金額 0..4294967295。至 2147483647 為 Integer，更大時為 Decimal（Double），可精確表示每個 UInt32
# 整數。0 也可能表示 Player 不存在／已銷毀或未取得金額。這不是 Boolean、ID、堆疊數或背包／銀行掃描結果。

SUB Main()
    # price=3000000000.0 是範例價格。CanAfford(price) 排除負價格或不存在的 Player，讀一次金額，以 amount >= price 回傳 Integer
    # Boolean 1=TRUE 或 0=FALSE。金額本身不是 Boolean。下方提供完整定義。

    VAR price = 3000000000.0
    IF CanAfford(price) = TRUE THEN
        UO.Print('Local balance is sufficient')
    ELSE
        UO.Print('Local check failed')
    END IF
END SUB

SUB CanAfford(price)
    IF price < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR amount = UO.Gold()
    RETURN amount >= price
END SUB
```

**參數與執行說明:**

- price=3000000000.0 是範例價格。CanAfford(price) 排除負價格或不存在的 Player，讀一次金額，以 amount >= price 回傳 Integer Boolean 1=TRUE 或 0=FALSE。金額本身不是 Boolean。下方提供完整定義。

### 觀察餘額變化

```vb
# 觀察餘額變化
#
# 讀取目前玩家 status 回報的金幣金額。
#
# Integer/Decimal：非負金額 0..4294967295。至 2147483647 為 Integer，更大時為 Decimal（Double），可精確表示每個 UInt32
# 整數。0 也可能表示 Player 不存在／已銷毀或未取得金額。這不是 Boolean、ID、堆疊數或背包／銀行掃描結果。

SUB Main()
    # before/after 間隔 WAIT(500) 毫秒。餘額下降時 difference=after-before 可以是負數，這不同於已修正的無號溢位。可能漏掉中途更新或角色切換。

    VAR before = UO.Gold()
    WAIT(500)
    VAR after = UO.Gold()
    VAR difference = after - before
    UO.Print('Balance change: ' + CStr(difference))
END SUB
```

**參數與執行說明:**

- before/after 間隔 WAIT(500) 毫秒。餘額下降時 difference=after-before 可以是負數，這不同於已修正的無號溢位。可能漏掉中途更新或角色切換。
