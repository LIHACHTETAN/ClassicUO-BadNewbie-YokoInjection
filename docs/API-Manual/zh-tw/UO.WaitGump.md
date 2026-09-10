# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

依序登記一次性的按鈕回應。腳本立即繼續，缺少視窗不會使腳本停住 30 秒。

## 完整語法

```text
UO.WaitGump(Value:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any, trigger16:Any) -> Unit
UO.WaitGump(triggerId:Integer) -> Unit
UO.WaitGump(triggerId:String) -> Unit
```

## 參數

- `triggerId` — Integer ButtonID 或數字 String。單一字串可用 | 或逗號分隔順序。2..16 個參數的形式也接受陣列及巢狀序列。登記前會解析所有 ID。空序列、用戶端等待按鈕超過 256 個，或巢狀深度超過 32 層，都會報錯且不會部分登記。
- `Value` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger1` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger2` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger3` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger4` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger5` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger6` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger7` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger8` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger9` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger10` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger11` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger12` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger13` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger14` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger15` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。
- `trigger16` — 序列元素：Integer ButtonID、數字 String、以 |/逗號分隔的字串，或上述元素的 Array。由左至右依 triggerId 的限制與規則處理。Value 是單一 Any 參數名稱，也接受陣列。

## 傳回值

Unit — 不傳回值：不是成功狀態、新值或伺服器確認。

## 行為

- 必須有符合 ButtonID 的實際 Activate 按鈕；會略過換頁按鈕及不符的視窗。後面的 ID 不會越過第一個等待 ID。每次收到版面時，每個視窗最多回應一次。重建版面可以沿用同一視窗物件。
- 同一腳本再次呼叫 WaitGump 會延長其等待序列。搜尋不以 GumpID 篩選；精確選取請用 NumGumpButton 或 SendGumpSelect。ButtonID=0 也需要實際 ID 0 的 Activate 按鈕，不是通用關閉指令。
- 程序正常結束後仍保留待執行操作。取消擁有者或以名稱呼叫 Terminate 會移除其操作；TerminateAll 會全部移除，包括已結束程序留下的操作。切換世界也會清空佇列。不會儲存在設定檔。

## 範例

### 單次回應

```vb
# 單次回應
#
# 依序登記一次性的按鈕回應。腳本立即繼續，缺少視窗不會使腳本停住 30 秒。
#
# Unit — 不傳回值：不是成功狀態、新值或伺服器確認。

SUB Main()
    # 100 是回應的 ButtonID。WaitGump 在 UseObject 前登記；腳本繼續不表示伺服器已確認回應。

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**參數與執行說明:**

- 100 是回應的 ButtonID。WaitGump 在 UseObject 前登記；腳本繼續不表示伺服器已確認回應。

### 多個步驟

```vb
# 多個步驟
#
# 依序登記一次性的按鈕回應。腳本立即繼續，缺少視窗不會使腳本停住 30 秒。
#
# Unit — 不傳回值：不是成功狀態、新值或伺服器確認。

SUB Main()
    # 7、22、1 是連續表單的 ButtonID，依此順序檢查。參數數量不是延遲時間；呼叫會登記整段序列。

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**參數與執行說明:**

- 7、22、1 是連續表單的 ButtonID，依此順序檢查。參數數量不是延遲時間；呼叫會登記整段序列。

### 取消等待

```vb
# 取消等待
#
# 依序登記一次性的按鈕回應。腳本立即繼續，缺少視窗不會使腳本停住 30 秒。
#
# Unit — 不傳回值：不是成功狀態、新值或伺服器確認。

SUB Main()
    # 7|22|1 字串指定相同序列。之後的 TerminateAll 會清除所有待執行 Gump 操作並停止所有程序；作用範圍是全域。

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**參數與執行說明:**

- 7|22|1 字串指定相同序列。之後的 TerminateAll 會清除所有待執行 Gump 操作並停止所有程序；作用範圍是全域。
