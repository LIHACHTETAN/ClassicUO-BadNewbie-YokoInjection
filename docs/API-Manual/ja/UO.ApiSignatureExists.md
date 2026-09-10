# UO.ApiSignatureExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

ネイティブ名と引数の個数を確認します。

## 正確な構文

```text
UO.ApiSignatureExists(name:String, argumentCount:Integer) -> Integer
```

## パラメーター

- `name` — 必須 String：正確な登録名で、呼び出し式ではありません。大小文字と前後の空白を無視し、UO. は追加しません。空・不明は 0。自作プロシージャは対象外です。
- `argumentCount` — 必須 Integer：明示した省略可能引数を含む位置引数の総数。負数や未対応の個数は 0。値の型は確認しません。

## 戻り値

登録済みは Integer 1、それ以外は 0。TRUE/FALSE または 1/0 と比較できます。ゲーム物体、操作成功、サーバー許可を保証しません。

## 動作

- 大文字と小文字は区別しません。InjectionApi は接頭辞なしの Basic、InjectionApiUO は UO. 付きのゲーム呼び出しを登録します。古い短縮呼び出しには SC005 と登録済み UO. 名の候補が表示され、自動実行はされません。属性値にも UO. が必要です。ApiNameExists、ApiSignatureExists、ApiParameterExists は前後の空白を除き、接頭辞を補わず正確な登録名を検査します。サーバー状態ではなくメタデータの検査です。VB.NET のリフレクション演算子 GetType(TypeName) は未実装です。

## 使用例

### UO.ApiSignatureExists — 1

```vb
# UO.ApiSignatureExists — 1
#
# ネイティブ名と引数の個数を確認します。
#
# 登録済みは Integer 1、それ以外は 0。TRUE/FALSE または 1/0 と比較できます。ゲーム物体、操作成功、サーバー許可を保証しません。

SUB Main()
    # 例1は明示的な UO. ゲーム名を検査して 1 を返します。名前と必要な引数数は呼び出しに示されています。

    RETURN UO.ApiSignatureExists('UO.GetType',1)
END SUB
```

**パラメーターと実行の説明:**

- 例1は明示的な UO. ゲーム名を検査して 1 を返します。名前と必要な引数数は呼び出しに示されています。

### UO.ApiSignatureExists — 2

```vb
# UO.ApiSignatureExists — 2
#
# ネイティブ名と引数の個数を確認します。
#
# 登録済みは Integer 1、それ以外は 0。TRUE/FALSE または 1/0 と比較できます。ゲーム物体、操作成功、サーバー許可を保証しません。

SUB Main()
    # 例2は Basic またはセレクターを検査します。Int(value) はあり、Int() はなく、backpack はセレクターです。結果は 1 または "1:0"。

    RETURN CStr(UO.ApiSignatureExists('Int',1)) + ':' + CStr(UO.ApiSignatureExists('Int',0))
END SUB
```

**パラメーターと実行の説明:**

- 例2は Basic またはセレクターを検査します。Int(value) はあり、Int() はなく、backpack はセレクターです。結果は 1 または "1:0"。

### UO.ApiSignatureExists — 3

```vb
# UO.ApiSignatureExists — 3
#
# ネイティブ名と引数の個数を確認します。
#
# 登録済みは Integer 1、それ以外は 0。TRUE/FALSE または 1/0 と比較できます。ゲーム物体、操作成功、サーバー許可を保証しません。

SUB Main()
    # 例3は補助関数の全体を定義し、削除済み短名や未対応の引数数を有効な形と比較します。name、first、second、count は名前／個数をそのまま渡します。呼び出し検査は
    # 0、値検査は "0:1"。

    RETURN CheckForm('UO.GetType',0)
END SUB

FUNCTION CheckForm(name,count)
    RETURN UO.ApiSignatureExists(name,count)
END FUNCTION
```

**パラメーターと実行の説明:**

- 例3は補助関数の全体を定義し、削除済み短名や未対応の引数数を有効な形と比較します。name、first、second、count は名前／個数をそのまま渡します。呼び出し検査は 0、値検査は "0:1"。
