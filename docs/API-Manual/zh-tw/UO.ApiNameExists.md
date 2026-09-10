# UO.ApiNameExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: zh-tw -->

檢查是否註冊可呼叫的原生名稱。

## 完整語法

```text
UO.ApiNameExists(name:String) -> Integer
```

## 參數

- `name` — 必要 String：確切註冊名稱，不是呼叫運算式。忽略大小寫和前後空白，不補 UO.。空白或未知名稱回傳 0，不含自訂程序。

## 傳回值

已註冊回傳 Integer 1，否則 0，可與 TRUE/FALSE 或 1/0 比較。不保證遊戲物件、操作成功或伺服器權限。

## 行為

- 名稱不分大小寫。InjectionApi 註冊不帶前綴的 Basic；InjectionApiUO 註冊帶 UO. 的遊戲呼叫。舊短名呼叫會產生 SC005 並建議已註冊的 UO. 名稱，不會自動執行替代呼叫。角色屬性值也需要 UO.。ApiNameExists、ApiSignatureExists、ApiParameterExists 去除前後空白後檢查確切的註冊名稱，不會補上前綴；它們檢查中繼資料而非伺服器狀態。未實作 VB.NET 反射運算子 GetType(TypeName)。

## 範例

### UO.ApiNameExists — 1

```vb
# UO.ApiNameExists — 1
#
# 檢查是否註冊可呼叫的原生名稱。
#
# 已註冊回傳 Integer 1，否則 0，可與 TRUE/FALSE 或 1/0 比較。不保證遊戲物件、操作成功或伺服器權限。

SUB Main()
    # 第一例檢查明確的 UO. 遊戲名稱，回傳 1。確切名稱與必要的參數數量均列於呼叫中。

    RETURN UO.ApiNameExists('UO.GetType')
END SUB
```

**參數與執行說明:**

- 第一例檢查明確的 UO. 遊戲名稱，回傳 1。確切名稱與必要的參數數量均列於呼叫中。

### UO.ApiNameExists — 2

```vb
# UO.ApiNameExists — 2
#
# 檢查是否註冊可呼叫的原生名稱。
#
# 已註冊回傳 Integer 1，否則 0，可與 TRUE/FALSE 或 1/0 比較。不保證遊戲物件、操作成功或伺服器權限。

SUB Main()
    # 第二例檢查 Basic 或選擇器：Int(value) 存在，Int() 不存在；backpack 是選擇器。依呼叫回傳 1 或 "1:0"。

    VAR name = 'CInt'
    RETURN UO.ApiNameExists(name)
END SUB
```

**參數與執行說明:**

- 第二例檢查 Basic 或選擇器：Int(value) 存在，Int() 不存在；backpack 是選擇器。依呼叫回傳 1 或 "1:0"。

### UO.ApiNameExists — 3

```vb
# UO.ApiNameExists — 3
#
# 檢查是否註冊可呼叫的原生名稱。
#
# 已註冊回傳 Integer 1，否則 0，可與 TRUE/FALSE 或 1/0 比較。不保證遊戲物件、操作成功或伺服器權限。

SUB Main()
    # 第三例完整定義輔助函式，比較已刪除的短名或不支援的參數數量與有效形式。name、first、second、count 原樣傳遞名稱／數量。呼叫檢查回傳 0，值檢查回傳 "0:1"。

    RETURN HasBoth('GetType','UO.GetType')
END SUB

FUNCTION HasBoth(first,second)
    RETURN UO.ApiNameExists(first) AndAlso UO.ApiNameExists(second)
END FUNCTION
```

**參數與執行說明:**

- 第三例完整定義輔助函式，比較已刪除的短名或不支援的參數數量與有效形式。name、first、second、count 原樣傳遞名稱／數量。呼叫檢查回傳 0，值檢查回傳 "0:1"。
