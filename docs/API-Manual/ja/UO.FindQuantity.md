# UO.FindQuantity

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

最初の検索結果の現在の数量を読みます。

## 正確な構文

```text
UO.FindQuantity() -> Any
```

## パラメーター

引数はありません。

## 戻り値

Integer — FindItem() で識別されるアイテムの現在の Amount。存在するキャラクターでは 1、存在しない／削除済みオブジェクトでは 0。他のスタックは加算せず、呼び出し時に読み取ります。

## 動作

- 通常の FindType（引数 1–5 個）、FindTypeEx、Count/CountEx/CountGround はこのスクリプトの検索結果を置き換えます。一致なしなら結果を空にします。再検索後も必要な値は先に保存します。
- これらの呼び出しは検索、容器の開閉、移動、パケット送信を行わず、クライアントが読み込んだデータを使います。FindCount(id) は事前の検索を必要とせず、その結果も変更しません。
- FindItem/FindCount()/FindFullQuantity は検索時の記録です。FindQuantity と FindCount(id) は現在の数量を読むため、検索後の変更や消失が反映されます。

## 使用例

### 金貨の検索を読む

```vb
# 金貨の検索を読む
#
# 最初の検索結果の現在の数量を読みます。
#
# Integer — FindItem() で識別されるアイテムの現在の Amount。存在するキャラクターでは 1、存在しない／削除済みオブジェクトでは
# 0。他のスタックは加算せず、呼び出し時に読み取ります。

SUB Main()
    # type=0x0EED は金貨、color=-1 は任意の色です。この形式の FindType の backpack はバックパック直下を選択します。value に結果を保存し、STR
    # で文字列表示します。

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindQuantity()
    UO.Print(STR(value))
END SUB
```

**パラメーターと実行の説明:**

- type=0x0EED は金貨、color=-1 は任意の色です。この形式の FindType の backpack はバックパック直下を選択します。value に結果を保存し、STR で文字列表示します。

### オブジェクト数、スタック、合計を比較

```vb
# オブジェクト数、スタック、合計を比較
#
# 最初の検索結果の現在の数量を読みます。
#
# Integer — FindItem() で識別されるアイテムの現在の Amount。存在するキャラクターでは 1、存在しない／削除済みオブジェクトでは
# 0。他のスタックは加算せず、呼び出し時に読み取ります。

SUB Main()
    # 四つとも同じ検索の後に読みます。50 個のスタックが二つなら、個数=2、最初のスタック=50、合計=100。FindItem は最初のスタック固有の ID で、type ではありません。

    UO.FindType(0x0EED, -1, 'backpack')
    UO.Print(STR(UO.FindCount()))
    UO.Print(STR(UO.FindQuantity()))
    UO.Print(STR(UO.FindFullQuantity()))
    UO.Print('0x' + Hex(UO.FindItem()))
END SUB
```

**パラメーターと実行の説明:**

- 四つとも同じ検索の後に読みます。50 個のスタックが二つなら、個数=2、最初のスタック=50、合計=100。FindItem は最初のスタック固有の ID で、type ではありません。

### 別の検索の前に値を保存

```vb
# 別の検索の前に値を保存
#
# 最初の検索結果の現在の数量を読みます。
#
# Integer — FindItem() で識別されるアイテムの現在の Amount。存在するキャラクターでは 1、存在しない／削除済みオブジェクトでは
# 0。他のスタックは加算せず、呼び出し時に読み取ります。

SUB Main()
    # 最初の type は金貨、0x0F7A は別の試薬です。二度目の FindType が検索結果を置き換えます。saved は古い値を保ち、最後の読み取りは新しい結果を使います。

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindQuantity()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindQuantity()))
END SUB
```

**パラメーターと実行の説明:**

- 最初の type は金貨、0x0F7A は別の試薬です。二度目の FindType が検索結果を置き換えます。saved は古い値を保ち、最後の読み取りは新しい結果を使います。
