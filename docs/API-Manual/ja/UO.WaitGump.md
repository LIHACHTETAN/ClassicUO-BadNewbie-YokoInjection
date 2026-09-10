# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

一度限りのボタン応答を順番に登録します。スクリプトは直ちに続行し、ウィンドウがなくても 30 秒間停止しません。

## 正確な構文

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

## パラメーター

- `triggerId` — Integer の ButtonID または数値 String。単一文字列では | やコンマで順序を区切れます。2..16 引数の形式では配列や入れ子の列も指定できます。登録前にすべての ID を解析します。空の列、クライアント全体で 256 件を超える待機ボタン、32 段を超える入れ子は、部分登録せずエラーにします。
- `Value` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger1` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger2` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger3` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger4` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger5` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger6` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger7` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger8` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger9` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger10` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger11` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger12` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger13` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger14` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger15` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。
- `trigger16` — 順序の要素：Integer ButtonID、数値 String、|/コンマで区切る文字列、またはそれらの Array。左から右へ triggerId の制限と規則で処理します。Value は単独の Any 引数名で、配列も指定できます。

## 戻り値

Unit — 戻り値はありません。成功、新しい値、サーバーの確認のいずれも返しません。

## 動作

- 指定 ButtonID の実際の Activate ボタンが必要です。ページ切替や不一致のウィンドウは無視します。後の ID は先頭の待機 ID を追い越しません。レイアウト受信 1 回につき各ウィンドウへ最大 1 回応答します。再構築時は同じウィンドウオブジェクトを再利用できます。
- 同じスクリプトの次の WaitGump は待機列に追加します。GumpID で絞り込まないため、正確な指定には NumGumpButton または SendGumpSelect を使います。ButtonID=0 も ID 0 の実際の Activate ボタンが必要で、すべてのウィンドウを閉じる指定ではありません。
- プロシージャの正常終了後も待機操作は残ります。所有者の中止または名前付き Terminate はその操作を削除します。TerminateAll は終了済みプロシージャの分も含め全件削除します。ワールド変更でもキューを消去します。プロファイルには保存しません。

## 使用例

### 単一応答

```vb
# 単一応答
#
# 一度限りのボタン応答を順番に登録します。スクリプトは直ちに続行し、ウィンドウがなくても 30 秒間停止しません。
#
# Unit — 戻り値はありません。成功、新しい値、サーバーの確認のいずれも返しません。

SUB Main()
    # 100 は応答の ButtonID です。WaitGump は UseObject より先に登録します。スクリプトの続行はサーバーの確認を意味しません。

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**パラメーターと実行の説明:**

- 100 は応答の ButtonID です。WaitGump は UseObject より先に登録します。スクリプトの続行はサーバーの確認を意味しません。

### 複数の段階

```vb
# 複数の段階
#
# 一度限りのボタン応答を順番に登録します。スクリプトは直ちに続行し、ウィンドウがなくても 30 秒間停止しません。
#
# Unit — 戻り値はありません。成功、新しい値、サーバーの確認のいずれも返しません。

SUB Main()
    # 7、22、1 は連続するフォームの ButtonID で、この順に調べます。引数の個数は待ち時間ではなく、呼び出しで列全体を登録します。

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**パラメーターと実行の説明:**

- 7、22、1 は連続するフォームの ButtonID で、この順に調べます。引数の個数は待ち時間ではなく、呼び出しで列全体を登録します。

### 待機操作を中止

```vb
# 待機操作を中止
#
# 一度限りのボタン応答を順番に登録します。スクリプトは直ちに続行し、ウィンドウがなくても 30 秒間停止しません。
#
# Unit — 戻り値はありません。成功、新しい値、サーバーの確認のいずれも返しません。

SUB Main()
    # 7|22|1 は同じ順序を指定します。その後の TerminateAll は全 Gump 待機操作を削除し、全プロシージャを停止します。全体に作用します。

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**パラメーターと実行の説明:**

- 7|22|1 は同じ順序を指定します。その後の TerminateAll は全 Gump 待機操作を削除し、全プロシージャを停止します。全体に作用します。
