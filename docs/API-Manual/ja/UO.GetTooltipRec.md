# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

オブジェクトの構造化プロパティを読み取り、各項目の cliloc ID と置換パラメーターを返します。

## 正確な構文

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## パラメーター

- `ObjID` — 必須のオブジェクト serial。graphic/type や cliloc ID ではありません。整数、十進数・十六進数文字列、self、backpack、lasttarget、finditem、AddObject 名を指定できます。0 は対象なしです。

## 戻り値

Array<Array>：各行は [clilocID:Integer, parameters:Array<String>] です。rows[i][0] はメッセージ ID、rows[i][1] はパラメーター配列です。GetArrayLength(rows) はプロパティ数です。未受信または ObjID=0 なら空配列を返します。オブジェクトの serial 一覧ではありません。

## 動作

- キャッシュは即座に返します。OPL がなければ要求を送信し、最大 120 ミリ秒待機します。プロシージャのキャンセルで待機を終了します。既知の空 OPL は即座に返します。
- BASIC 配列で TClilocRec を表します。Count は GetArrayLength(rows)、Items は各行です。先頭の通信用タブは除去し、途中の空パラメーターの位置は保持します。#数値は翻訳用の文字列として残します。パラメーターがなければ空配列です。返されたデータを変更してもキャッシュは変わりません。
- https://stealth.od.ua/api/GetTooltipRec/

## 使用例

### プロパティ ID を列挙する

```vb
# プロパティ ID を列挙する
#
# オブジェクトの構造化プロパティを読み取り、各項目の cliloc ID と置換パラメーターを返します。
#
# Array<Array>：各行は [clilocID:Integer, parameters:Array<String>] です。rows[i][0] はメッセージ
# ID、rows[i][1] はパラメーター配列です。GetArrayLength(rows) はプロパティ数です。未受信または ObjID=0 なら空配列を返します。オブジェクトの
# serial 一覧ではありません。

SUB Main()
    # ObjID=lasttarget は対象を選びます。i は 0 から始まり、row[0] は cliloc ID です。空配列ではループを実行しません。

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**パラメーターと実行の説明:**

- ObjID=lasttarget は対象を選びます。i は 0 から始まり、row[0] は cliloc ID です。空配列ではループを実行しません。

### 各プロパティを翻訳する

```vb
# 各プロパティを翻訳する
#
# オブジェクトの構造化プロパティを読み取り、各項目の cliloc ID と置換パラメーターを返します。
#
# Array<Array>：各行は [clilocID:Integer, parameters:Array<String>] です。rows[i][0] はメッセージ
# ID、rows[i][1] はパラメーター配列です。GetArrayLength(rows) はプロパティ数です。未受信または ObjID=0 なら空配列を返します。オブジェクトの
# serial 一覧ではありません。

SUB Main()
    # GetClilocByID に ClilocID=row[0] と Params=row[1] を順序どおり渡します。行全体を Params に渡さないでください。

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR text = UO.GetClilocByID(row[0], row[1])
        UO.Print(text)
        i = i + 1
    WEND
END SUB
```

**パラメーターと実行の説明:**

- GetClilocByID に ClilocID=row[0] と Params=row[1] を順序どおり渡します。行全体を Params に渡さないでください。

### 数値パラメーターを読む

```vb
# 数値パラメーターを読む
#
# オブジェクトの構造化プロパティを読み取り、各項目の cliloc ID と置換パラメーターを返します。
#
# Array<Array>：各行は [clilocID:Integer, parameters:Array<String>] です。rows[i][0] はメッセージ
# ID、rows[i][1] はパラメーター配列です。GetArrayLength(rows) はプロパティ数です。未受信または ObjID=0 なら空配列を返します。オブジェクトの
# serial 一覧ではありません。

SUB Main()
    # wanted=1060401 は例の ID です。必要な ID に置き換えてください。args[0] は String です。Val の前に長さと IsNumeric
    # を確認します。文字列や #cliloc の場合もあります。

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR wanted = 1060401
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR args = row[1]
        IF row[0] = wanted AND GetArrayLength(args) > 0 THEN
            IF IsNumeric(args[0]) THEN
                UO.Print('Value: ' + STR(Val(args[0])))
            END IF
        END IF
        i = i + 1
    WEND
END SUB
```

**パラメーターと実行の説明:**

- wanted=1060401 は例の ID です。必要な ID に置き換えてください。args[0] は String です。Val の前に長さと IsNumeric を確認します。文字列や #cliloc の場合もあります。
