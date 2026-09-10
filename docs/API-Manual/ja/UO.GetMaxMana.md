# UO.GetMaxMana

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

ローカルモデルから最大マナを読みます。

## 正確な構文

```text
UO.GetMaxMana() -> Integer
UO.GetMaxMana(ObjID:Any) -> Any
```

## パラメーター

- `ObjID` — 表示された呼び出し形式で省略できる物体指定です。数値または16進文字列の serial、self、lasttarget、登録済み AddObject 名を指定します。type ではありません。省略時は self。形式によって未知の文字列は変換エラーになるため、先に名前を確認してください。

## 戻り値

Integer — フィールド ManaMax の値であり、百分率や Boolean ではありません。0 は実際の値の場合も、データ不在の場合もあります。最大値 0 で割らないでください。 他の mobile の値は不明な場合があります。HP/HitsMax は正確な点数ではなくサーバーの相対的な尺度の場合があります。HP=0 は死亡の証明ではなく、Dead/IsDead を使用します。

## 動作

- status を開かず、サーバーへ更新も要求しません。HP 不明時に自動要求する Stealth と異なり、このクライアントは既存データを読むだけです。能力値の変更やパケット送信はありません。
- 結果はそれぞれ独立した読み取りです。Exists と次の呼び出しの間に世界が変化するため、複数の照会は不可分なスナップショットではありません。
- 物体を読む場合、World.Get は不在または IsDestroyed の記録を除外して 0 を返します。HP/HitsMax は該当フィールドのあるアイテムを含む Entity を読み、Mana/Stamina は Mobile に限ります。引数なしでは self。引数なしの名前に必ず ID 形式があるとは限らないため、シグネチャを確認してください。
- 引数なしでも Player 不在または破棄済みなら 0 です。World.Get 経由だけでなく、直接の Mana/Stamina と最大値も含みます。存在する死亡キャラクターには値が残る場合があります。

### 内部関数：呼び出しから結果まで

実際の C# 内部処理を示します。ReadValue は例に完全な定義を含む補助関数で、隠れた組み込み命令ではありません。

#### 1. RegisterCharacterGetterAliases

runtime 作成時に RegisterCharacterGetterAliases が名前と形式を登録します。引数なしでは bridge.Self、引数ありでは指定 serial を使います。既存の登録は保持します。

Integer — フィールド ManaMax の値であり、百分率や Boolean ではありません。0 は実際の値の場合も、データ不在の場合もあります。最大値 0 で割らないでください。 他の mobile の値は不明な場合があります。HP/HitsMax は正確な点数ではなくサーバーの相対的な尺度の場合があります。HP=0 は死亡の証明ではなく、Dead/IsDead を使用します。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject は数値、16進文字列、保存名を解決します。AddObject 名は呼び出すたびに解決します。graphic/type の検索や対話的な選択は行いません。

表示された呼び出し形式で省略できる物体指定です。数値または16進文字列の serial、self、lasttarget、登録済み AddObject 名を指定します。type ではありません。省略時は self。形式によって未知の文字列は変換エラーになるため、先に名前を確認してください。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `TryGetObject`.

#### 3. Invoke

Invoke はゲームスレッドで読み取ります。ワーカースレッドはマネージャーによる処理を待ち、スクリプトのキャンセルで待機を中断します。追加の遅延や通信要求はありません。

結果はそれぞれ独立した読み取りです。Exists と次の呼び出しの間に世界が変化するため、複数の照会は不可分なスナップショットではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 4. Get

物体を読む場合、World.Get は不在または IsDestroyed の記録を除外して 0 を返します。HP/HitsMax は該当フィールドのあるアイテムを含む Entity を読み、Mana/Stamina は Mobile に限ります。引数なしでは self。引数なしの名前に必ず ID 形式があるとは限らないため、シグネチャを確認してください。

Integer — フィールド ManaMax の値であり、百分率や Boolean ではありません。0 は実際の値の場合も、データ不在の場合もあります。最大値 0 で割らないでください。 他の mobile の値は不明な場合があります。HP/HitsMax は正確な点数ではなくサーバーの相対的な尺度の場合があります。HP=0 は死亡の証明ではなく、Dead/IsDead を使用します。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Get`.

status を開かず、サーバーへ更新も要求しません。HP 不明時に自動要求する Stealth と異なり、このクライアントは既存データを読むだけです。能力値の変更やパケット送信はありません。


## 使用例

### 自分のキャラクター値を表示する

```vb
# 自分のキャラクター値を表示する
#
# ローカルモデルから最大マナを読みます。
#
# Integer — フィールド ManaMax の値であり、百分率や Boolean ではありません。0 は実際の値の場合も、データ不在の場合もあります。最大値 0 で割らないでください。
# 他の mobile の値は不明な場合があります。HP/HitsMax は正確な点数ではなくサーバーの相対的な尺度の場合があります。HP=0 は死亡の証明ではなく、Dead/IsDead
# を使用します。

SUB Main()
    # 引数なしの呼び出しは self を読みます。value は一つの数を保存し、STR は表示用の文字列に変換するだけです。

    VAR value = UO.GetMaxMana()
    UO.Print('GetMaxMana: ' + STR(value))
END SUB
```

**パラメーターと実行の説明:**

- 引数なしの呼び出しは self を読みます。value は一つの数を保存し、STR は表示用の文字列に変換するだけです。

### 値を条件や計算に使う

```vb
# 値を条件や計算に使う
#
# ローカルモデルから最大マナを読みます。
#
# Integer — フィールド ManaMax の値であり、百分率や Boolean ではありません。0 は実際の値の場合も、データ不在の場合もあります。最大値 0 で割らないでください。
# 他の mobile の値は不明な場合があります。HP/HitsMax は正確な点数ではなくサーバーの相対的な尺度の場合があります。HP=0 は死亡の証明ではなく、Dead/IsDead
# を使用します。

SUB Main()
    # このフィールド用のしきい値や計算を示します。条件の数値は例の設定であり、サーバー制限ではありません。除算前に最大値が正であることを確認します。

    VAR value = UO.GetMaxMana()
    IF value > 0 THEN
        UO.Print('Mana percent: ' + STR(UO.Mana() * 100 / value))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- このフィールド用のしきい値や計算を示します。条件の数値は例の設定であり、サーバー制限ではありません。除算前に最大値が正であることを確認します。

### 完全な ReadValue 補助関数

```vb
# 完全な ReadValue 補助関数
#
# ローカルモデルから最大マナを読みます。
#
# Integer — フィールド ManaMax の値であり、百分率や Boolean ではありません。0 は実際の値の場合も、データ不在の場合もあります。最大値 0 で割らないでください。
# 他の mobile の値は不明な場合があります。HP/HitsMax は正確な点数ではなくサーバーの相対的な尺度の場合があります。HP=0 は死亡の証明ではなく、Dead/IsDead
# を使用します。

SUB Main()
    # lasttarget は以前に選択した物体で、Exists で存在を確認します。obj は ReadValue の唯一の引数です。完全に定義された関数は命令の数値をそのまま返します。

    IF UO.Exists('lasttarget') THEN
        VAR value = ReadValue('lasttarget')
        UO.Print('Selected value: ' + CStr(value))
    END IF
END SUB

SUB ReadValue(obj)
    RETURN UO.GetMaxMana(obj)
END SUB
```

**パラメーターと実行の説明:**

- lasttarget は以前に選択した物体で、Exists で存在を確認します。obj は ReadValue の唯一の引数です。完全に定義された関数は命令の数値をそのまま返します。
