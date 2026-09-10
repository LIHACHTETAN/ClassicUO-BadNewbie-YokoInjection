# UO.ApiSignatureExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

檢查原生名稱是否接受指定參數數量。

## 完整語法

```text
UO.ApiSignatureExists(name:String, argumentCount:Integer) -> Integer
```

## 參數

- `name` — 必要 String：確切註冊名稱，不是呼叫運算式。忽略大小寫和前後空白，不補 UO.。空白或未知名稱回傳 0，不含自訂程序。
- `argumentCount` — 必要 Integer：位置參數總數，包含明確傳入的選填參數。負數或不支援的數量回傳 0，不檢查值的型別。

## 傳回值

已註冊回傳 Integer 1，否則 0，可與 TRUE/FALSE 或 1/0 比較。不保證遊戲物件、操作成功或伺服器權限。

## 行為

- 名稱不分大小寫。InjectionApi 註冊不帶前綴的 Basic；InjectionApiUO 註冊帶 UO. 的遊戲呼叫。舊短名呼叫會產生 SC005 並建議已註冊的 UO. 名稱，不會自動執行替代呼叫。角色屬性值也需要 UO.。ApiNameExists、ApiSignatureExists、ApiParameterExists 去除前後空白後檢查確切的註冊名稱，不會補上前綴；它們檢查中繼資料而非伺服器狀態。未實作 VB.NET 反射運算子 GetType(TypeName)。

## 範例

### UO.ApiSignatureExists — 1

```vb
# UO.ApiSignatureExists — 1
#
# 檢查原生名稱是否接受指定參數數量。
#
# 已註冊回傳 Integer 1，否則 0，可與 TRUE/FALSE 或 1/0 比較。不保證遊戲物件、操作成功或伺服器權限。

SUB Main()
    # 第一例檢查明確的 UO. 遊戲名稱，回傳 1。確切名稱與必要的參數數量均列於呼叫中。

    RETURN UO.ApiSignatureExists('UO.GetType',1)
END SUB
```

**參數與執行說明:**

- 第一例檢查明確的 UO. 遊戲名稱，回傳 1。確切名稱與必要的參數數量均列於呼叫中。

### UO.ApiSignatureExists — 2

```vb
# UO.ApiSignatureExists — 2
#
# 檢查原生名稱是否接受指定參數數量。
#
# 已註冊回傳 Integer 1，否則 0，可與 TRUE/FALSE 或 1/0 比較。不保證遊戲物件、操作成功或伺服器權限。

SUB Main()
    # 第二例檢查 Basic 或選擇器：Int(value) 存在，Int() 不存在；backpack 是選擇器。依呼叫回傳 1 或 "1:0"。

    RETURN CStr(UO.ApiSignatureExists('Int',1)) + ':' + CStr(UO.ApiSignatureExists('Int',0))
END SUB
```

**參數與執行說明:**

- 第二例檢查 Basic 或選擇器：Int(value) 存在，Int() 不存在；backpack 是選擇器。依呼叫回傳 1 或 "1:0"。

### UO.ApiSignatureExists — 3

```vb
# UO.ApiSignatureExists — 3
#
# 檢查原生名稱是否接受指定參數數量。
#
# 已註冊回傳 Integer 1，否則 0，可與 TRUE/FALSE 或 1/0 比較。不保證遊戲物件、操作成功或伺服器權限。

SUB Main()
    # 第三例完整定義輔助函式，比較已刪除的短名或不支援的參數數量與有效形式。name、first、second、count 原樣傳遞名稱／數量。呼叫檢查回傳 0，值檢查回傳 "0:1"。

    RETURN CheckForm('UO.GetType',0)
END SUB

FUNCTION CheckForm(name,count)
    RETURN UO.ApiSignatureExists(name,count)
END FUNCTION
```

**參數與執行說明:**

- 第三例完整定義輔助函式，比較已刪除的短名或不支援的參數數量與有效形式。name、first、second、count 原樣傳遞名稱／數量。呼叫檢查回傳 0，值檢查回傳 "0:1"。
