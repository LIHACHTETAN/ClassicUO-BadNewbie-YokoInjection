# UO.LastStatusY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

傳回最後接受狀態物件所保存的 Y 座標。

## 完整語法

```text
UO.LastStatusY() -> Integer
```

## 參數

沒有參數。

## 傳回值

Integer — 保存的 Y 座標，不是狀態視窗像素或 Boolean。首次狀態前及清除世界後為 0；但實際座標也可以是 0。以 UO.LastStatus() 判斷是否有記錄。

## 行為

- 不接受參數。讀取不傳送封包、不開視窗，也不等待回覆。UO.GetStatus(id)、RequestStats 和 UpdateObject 只請求資料；送出請求不會改變 LastStatus。
- 接受 0x11 封包時，將 serial 及本機已知 X/Y 一起存入所有腳本共用的 World。未知或已銷毀物件、不完整的基本封包不會取代記錄。之後其他物件的狀態可取代它。
- X/Y 是接收時的 Entity 座標，不是即時位置。對 mobile 為世界格；容器內物品可能是容器內容座標。狀態封包本身不含 X/Y。之後移動或移除物件不改變快照；World.Clear 會重設。現存物件的即時座標請用 GetX/GetY。
- 分開呼叫不是原子快照；中間可能收到更新。相同 serial 不能證明是自己請求的新回覆。沒有括號的 laststatus 是即時內建值，但可能被同名腳本變數遮蔽；UO.LastStatus() 是已註冊函式。

### 內部函式：從呼叫到結果

以下為實際的 C# 內部步驟。ReadSavedStatus 是範例中完整定義的輔助函式，不是隱藏的內建命令。

#### 1. CharacterStatus

CharacterStatus 透過 World.Get 驗證基本封包和 Entity，更新狀態並保存 serial/X/Y。位置來自 Entity，不是狀態封包。

Integer — 保存的 Y 座標，不是狀態視窗像素或 Boolean。首次狀態前及清除世界後為 0；但實際座標也可以是 0。以 UO.LastStatus() 判斷是否有記錄。

專案原始碼: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 函式 `CharacterStatus`.

#### 2. LastStatusY

ExecuteStealthCompatibility 將 bridge serial 傳回為 Integer。LastStatusX/LastStatusY 使用 IStatusSnapshotBridge；未實作此介面的舊外部 bridge 保留 GetX/GetY 查詢。

Integer — 保存的 Y 座標，不是狀態視窗像素或 Boolean。首次狀態前及清除世界後為 0；但實際座標也可以是 0。以 UO.LastStatus() 判斷是否有記錄。

專案原始碼: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 函式 `LastStatusY`.

#### 3. Invoke

Invoke 在遊戲執行緒讀取 World，並支援腳本取消。不等待網路回覆，也不改變狀態。

不接受參數。讀取不傳送封包、不開視窗，也不等待回覆。UO.GetStatus(id)、RequestStats 和 UpdateObject 只請求資料；送出請求不會改變 LastStatus。

專案原始碼: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 函式 `Invoke`.

#### 4. Clear

Clear 將 serial 和兩個座標歸零，即使保留執行中的腳本亦然。

X/Y 是接收時的 Entity 座標，不是即時位置。對 mobile 為世界格；容器內物品可能是容器內容座標。狀態封包本身不含 X/Y。之後移動或移除物件不改變快照；World.Clear 會重設。現存物件的即時座標請用 GetX/GetY。

專案原始碼: `src/ClassicUO.Client/Game/World.cs`; 函式 `Clear`.

分開呼叫不是原子快照；中間可能收到更新。相同 serial 不能證明是自己請求的新回覆。沒有括號的 laststatus 是即時內建值，但可能被同名腳本變數遮蔽；UO.LastStatus() 是已註冊函式。


## 範例

### 讀取最後的值

```vb
# 讀取最後的值
#
# 傳回最後接受狀態物件所保存的 Y 座標。
#
# Integer — 保存的 Y 座標，不是狀態視窗像素或 Boolean。首次狀態前及清除世界後為 0；但實際座標也可以是 0。以 UO.LastStatus() 判斷是否有記錄。

SUB Main()
    # 只讀取一次。HEX 以十六進位顯示 serial；CStr 顯示數字座標。不會選擇物件。

    VAR value = UO.LastStatusY()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**參數與執行說明:**

- 只讀取一次。HEX 以十六進位顯示 serial；CStr 顯示數字座標。不會選擇物件。

### 請求狀態並讀取已知資料

```vb
# 請求狀態並讀取已知資料
#
# 傳回最後接受狀態物件所保存的 Y 座標。
#
# Integer — 保存的 Y 座標，不是狀態視窗像素或 Boolean。首次狀態前及清除世界後為 0；但實際座標也可以是 0。以 UO.LastStatus() 判斷是否有記錄。

SUB Main()
    # subject 是 self 的 serial。500 是範例的毫秒等待時間，不保證收到回覆。顯示的記錄可能是舊資料或其他物件。

    VAR subject = UO.Self()
    IF subject <> 0 THEN
        UO.GetStatus(subject)
        WAIT(500)
        VAR value = UO.LastStatusY()
        UO.Print('Known value: ' + CStr(value))
    END IF
END SUB
```

**參數與執行說明:**

- subject 是 self 的 serial。500 是範例的毫秒等待時間，不保證收到回覆。顯示的記錄可能是舊資料或其他物件。

### 完整的 ReadSavedStatus 輔助函式

```vb
# 完整的 ReadSavedStatus 輔助函式
#
# 傳回最後接受狀態物件所保存的 Y 座標。
#
# Integer — 保存的 Y 座標，不是狀態視窗像素或 Boolean。首次狀態前及清除世界後為 0；但實際座標也可以是 0。以 UO.LastStatus() 判斷是否有記錄。

SUB Main()
    # expectedId 是 Main 保存的 serial。下方完整定義輔助函式；-1 表示所選記錄已改變，並非命令本身的回傳碼。前後檢查可減少混用物件，但不能保證相同 serial
    # 更新時的原子性。

    VAR expectedId = UO.LastStatus()
    IF expectedId <> 0 THEN
        VAR value = ReadSavedStatus(expectedId)
        UO.Print('Checked value: ' + CStr(value))
    END IF
END SUB

SUB ReadSavedStatus(expectedId)
    IF expectedId = 0 OR UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    VAR value = UO.LastStatusY()
    IF UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**參數與執行說明:**

- expectedId 是 Main 保存的 serial。下方完整定義輔助函式；-1 表示所選記錄已改變，並非命令本身的回傳碼。前後檢查可減少混用物件，但不能保證相同 serial 更新時的原子性。
