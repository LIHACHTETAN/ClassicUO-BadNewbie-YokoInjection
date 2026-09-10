# UO.GetFoundedText

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

このスクリプトが選択したジャーナル項目の保存済みテキストを読み取ります。

## 正確な構文

```text
UO.GetFoundedText() -> String
```

## パラメーター

引数はありません。

## 戻り値

String：選択したテキスト。未選択の場合は空文字列です。存在する項目のテキストが空の場合もあります。serial、行インデックス、成功を示す Boolean ではありません。

## 動作

- InJournal、InJournalBetweenTimes、Journal/GetJournal、LastJournalMessage は選択を置き換えます。検索失敗、無効な Journal インデックス、このスクリプトによる消去で選択をリセットします。引数はなく、新しい検索も行いません。
- 新しいメッセージは保存済みテキストを置き換えません。項目が削除されたりバッファから追い出されたりしてもテキストは残り、GetFoundedTextIndex/LineIndex は -1 になります。他のスクリプトが共有ジャーナルを消去しても、保存済み変数は変わりません。

## 使用例

### 見つかったメッセージを読む

```vb
# 見つかったメッセージを読む
#
# このスクリプトが選択したジャーナル項目の保存済みテキストを読み取ります。
#
# String：選択したテキスト。未選択の場合は空文字列です。存在する項目のテキストが空の場合もあります。serial、行インデックス、成功を示す Boolean ではありません。

SUB Main()
    # needle は大文字と小文字を区別する部分文字列です。InJournal > 0 を確認してください。結果は位置に 1 を加えた値で、一致数ではありません。

    IF UO.InJournal('needle') > 0 THEN
        VAR text = UO.GetFoundedText()
        UO.Print(text)
    END IF
END SUB
```

**パラメーターと実行の説明:**

- needle は大文字と小文字を区別する部分文字列です。InJournal > 0 を確認してください。結果は位置に 1 を加えた値で、一致数ではありません。

### 選択した行を読む

```vb
# 選択した行を読む
#
# このスクリプトが選択したジャーナル項目の保存済みテキストを読み取ります。
#
# String：選択したテキスト。未選択の場合は空文字列です。存在する項目のテキストが空の場合もあります。serial、行インデックス、成功を示す Boolean ではありません。

SUB Main()
    # Journal(0) は最新項目を選択します。Print はメッセージを追加する場合があるため、その前にテキストとインデックスを保存します。空文字列だけでは項目がないとは判断できません。

    VAR latest = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR text = UO.GetFoundedText()
    IF index >= 0 THEN
        UO.Print(text)
    END IF
END SUB
```

**パラメーターと実行の説明:**

- Journal(0) は最新項目を選択します。Print はメッセージを追加する場合があるため、その前にテキストとインデックスを保存します。空文字列だけでは項目がないとは判断できません。

### 次の検索前にテキストを保存する

```vb
# 次の検索前にテキストを保存する
#
# このスクリプトが選択したジャーナル項目の保存済みテキストを読み取ります。
#
# String：選択したテキスト。未選択の場合は空文字列です。存在する項目のテキストが空の場合もあります。serial、行インデックス、成功を示す Boolean ではありません。

SUB Main()
    # saved は、次の検索が選択を置き換える前に最初の結果をコピーします。その後のメッセージや検索でこの変数は変化しません。

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.GetFoundedText()
        VAR another = UO.InJournal('failed')
        UO.Print(saved)
    END IF
END SUB
```

**パラメーターと実行の説明:**

- saved は、次の検索が選択を置き換える前に最初の結果をコピーします。その後のメッセージや検索でこの変数は変化しません。
