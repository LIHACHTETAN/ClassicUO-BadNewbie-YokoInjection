# UO.GetGumpInfo

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

サーバーガンプとそのコントロールの整合したスナップショットを読み取ります。

## 正確な構文

```text
UO.GetGumpInfo(GumpIndex:Any) -> Array
```

## パラメーター

- `GumpIndex` — 必須の Integer。0 から GetGumpsCount()-1 までのインデックスであり、serial や GumpID ではありません。負数や範囲外は無効です。ウィンドウの開閉や並べ替えでインデックスは変化します。

## 戻り値

Array — 5 要素の Array：[0] Integer の serial、[1] Integer の GumpID、[2] 空白だけではないテキストの Array<String>、[3] 通常ボタンの説明の Array<String>、[4] 入れ子を含む有効な全コントロールの説明の Array<String>。無効、終了済み、無視対象のガンプは [] を返します。最上位ビットがある ID は負の Integer になります。Hex でビット表現を表示できます。

## 動作

- 全データをゲームスレッドへの 1 回の要求でコピーします。その後の変更や終了は保存した配列を変えません。有効なサーバーガンプのみが対象で、ローカルのバックパック、マップ、設定ウィンドウは含みません。
- これは BASIC の配列であり、Pascal の TGumpInfo レコードや元のレイアウトパケットではありません。説明には種類、page、ID、X/Y、寸法があり、ボタンには ButtonID、action、toPage、画像、切り替え要素には checked と inactive/active が追加されます。テキストには空白や = が含まれる場合があります。ラジオボタンは [4] に含まれ、[3] には含まれません。
- AddGumpIgnoreByID/BySerial は現在のスクリプトでこの読み取り結果を非表示にし、ClearGumpsIgnore はフィルターを解除します。GetGumpsCount は変わりません。存在するガンプでもテキスト配列が空の場合があります。配列の長さには Len ではなく GetArrayLength を使います。

## 使用例

### 両方の ID を読む

```vb
# 両方の ID を読む
#
# サーバーガンプとそのコントロールの整合したスナップショットを読み取ります。
#
# Array — 5 要素の Array：[0] Integer の serial、[1] Integer の GumpID、[2] 空白だけではないテキストの
# Array<String>、[3] 通常ボタンの説明の Array<String>、[4] 入れ子を含む有効な全コントロールの説明の
# Array<String>。無効、終了済み、無視対象のガンプは [] を返します。最上位ビットがある ID は負の Integer になります。Hex でビット表現を表示できます。

SUB Main()
    # 0 は最初のサーバーガンプです。要素を読む前に GetArrayLength(info)=5 を確認します。info[0] は serial、info[1] は同じスナップショットの
    # GumpID です。

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        UO.Print('Serial=' + Hex(info[0]))
        UO.Print('GumpID=' + Hex(info[1]))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- 0 は最初のサーバーガンプです。要素を読む前に GetArrayLength(info)=5 を確認します。info[0] は serial、info[1] は同じスナップショットの GumpID です。

### 実際の ButtonID を列挙する

```vb
# 実際の ButtonID を列挙する
#
# サーバーガンプとそのコントロールの整合したスナップショットを読み取ります。
#
# Array — 5 要素の Array：[0] Integer の serial、[1] Integer の GumpID、[2] 空白だけではないテキストの
# Array<String>、[3] 通常ボタンの説明の Array<String>、[4] 入れ子を含む有効な全コントロールの説明の
# Array<String>。無効、終了済み、無視対象のガンプは [] を返します。最上位ビットがある ID は負の Integer になります。Hex でビット表現を表示できます。

SUB Main()
    # info[3] はボタンの説明です。i は行インデックスであり、応答に使う ID は説明内の ButtonID です。ラジオボタンは全コントロール一覧に含まれます。

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR buttons = info[3]
        VAR i = 0
        WHILE i < GetArrayLength(buttons)
            UO.Print(buttons[i])
            i = i + 1
        WEND
    END IF
END SUB
```

**パラメーターと実行の説明:**

- info[3] はボタンの説明です。i は行インデックスであり、応答に使う ID は説明内の ButtonID です。ラジオボタンは全コントロール一覧に含まれます。

### 終了前にテキストを保存する

```vb
# 終了前にテキストを保存する
#
# サーバーガンプとそのコントロールの整合したスナップショットを読み取ります。
#
# Array — 5 要素の Array：[0] Integer の serial、[1] Integer の GumpID、[2] 空白だけではないテキストの
# Array<String>、[3] 通常ボタンの説明の Array<String>、[4] 入れ子を含む有効な全コントロールの説明の
# Array<String>。無効、終了済み、無視対象のガンプは [] を返します。最上位ビットがある ID は負の Integer になります。Hex でビット表現を表示できます。

SUB Main()
    # info[2] はテキストのコピーです。CloseSimpleGump(0) は NoClose がない場合だけローカルで閉じ、値を返しません。保存したテキストは残ります。texts[0]
    # の前に配列の長さを確認します。

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR texts = info[2]
        UO.CloseSimpleGump(0)
        IF GetArrayLength(texts) > 0 THEN
            UO.Print(texts[0])
        END IF
    END IF
END SUB
```

**パラメーターと実行の説明:**

- info[2] はテキストのコピーです。CloseSimpleGump(0) は NoClose がない場合だけローカルで閉じ、値を返しません。保存したテキストは残ります。texts[0] の前に配列の長さを確認します。
