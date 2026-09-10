# UO.GetDead

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

mobile が死亡しているか調べます。

## 正確な構文

```text
UO.GetDead() -> Integer
UO.GetDead(value:Any) -> Integer
```

## パラメーター

- `value` — 表示された呼び出し形式で省略できる物体指定です。数値または16進文字列の serial、self、lasttarget、登録済み AddObject 名を指定します。type ではありません。省略時は self。形式によって未知の文字列は変換エラーになるため、先に名前を確認してください。

## 戻り値

Integer Boolean：1 = TRUE、0 = FALSE。数値または引用符のない論理定数と比較できます。 mobile が IsDead なら 1、それ以外または存在しなければ 0。HP=0 だけで死亡とは判断しません。

論理的な結果です。1 = TRUE、0 = FALSE。VAR result = command(...) で保存した後は IF result = TRUE THEN または IF result = 1 THEN、否定時は IF result = FALSE THEN または IF result = 0 THEN と書けます。TRUE/FALSE に引用符は付けません。一度呼び出して保存してください。再呼び出しは動作を繰り返したり、変更後の状態を読んだりする場合があります。

## 動作

- ローカルモデルを読みます。target、status 要求、フラグ変更、パケット送信は行いません。破棄済みの物体は辞書から削除される前でも不在として扱います。
- 結果はそれぞれ独立した読み取りです。Exists と次の呼び出しの間に世界が変化するため、複数の照会は不可分なスナップショットではありません。

### 内部関数：呼び出しから結果まで

実際の C# 内部処理を示します。ReadState は例に完全な定義を含む補助関数で、隠れた組み込み命令ではありません。

#### 1. RegisterCharacterGetterAliases

runtime 作成時に RegisterCharacterGetterAliases が名前と形式を登録します。引数なしでは bridge.Self、引数ありでは指定 serial を使います。既存の登録は保持します。

mobile が IsDead なら 1、それ以外または存在しなければ 0。HP=0 だけで死亡とは判断しません。

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

World.Get は serial を検索し、IsDestroyed なら null を返してから Mobile フラグを読みます。Alive は Exists と IsDead の不在を確認し、アイテムも認めます。self の Dead は Player.IsDead を読みます。

mobile が IsDead なら 1、それ以外または存在しなければ 0。HP=0 だけで死亡とは判断しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Get`.

ローカルモデルを読みます。target、status 要求、フラグ変更、パケット送信は行いません。破棄済みの物体は辞書から削除される前でも不在として扱います。


## 使用例

### 自分の状態を確認する

```vb
# 自分の状態を確認する
#
# mobile が死亡しているか調べます。
#
# Integer Boolean：1 = TRUE、0 = FALSE。数値または引用符のない論理定数と比較できます。 mobile が IsDead なら 1、それ以外または存在しなければ
# 0。HP=0 だけで死亡とは判断しません。
#
# 論理的な結果です。1 = TRUE、0 = FALSE。VAR result = command(...) で保存した後は IF result = TRUE THEN または IF
# result = 1 THEN、否定時は IF result = FALSE THEN または IF result = 0 THEN と書けます。TRUE/FALSE
# に引用符は付けません。一度呼び出して保存してください。再呼び出しは動作を繰り返したり、変更後の状態を読んだりする場合があります。

SUB Main()
    # 空の括弧は self を読みます。active に一度の結果を保存し、TRUE と FALSE で分岐します。Print はメッセージ例を表示するだけです。

    VAR active = UO.GetDead()
    IF active = TRUE THEN
        UO.Print('State is active')
    ELSE
        UO.Print('State is inactive or unavailable')
    END IF
END SUB
```

**パラメーターと実行の説明:**

- 空の括弧は self を読みます。active に一度の結果を保存し、TRUE と FALSE で分岐します。Print はメッセージ例を表示するだけです。

### 選択した物体と完全な ReadState 関数

```vb
# 選択した物体と完全な ReadState 関数
#
# mobile が死亡しているか調べます。
#
# Integer Boolean：1 = TRUE、0 = FALSE。数値または引用符のない論理定数と比較できます。 mobile が IsDead なら 1、それ以外または存在しなければ
# 0。HP=0 だけで死亡とは判断しません。
#
# 論理的な結果です。1 = TRUE、0 = FALSE。VAR result = command(...) で保存した後は IF result = TRUE THEN または IF
# result = 1 THEN、否定時は IF result = FALSE THEN または IF result = 0 THEN と書けます。TRUE/FALSE
# に引用符は付けません。一度呼び出して保存してください。再呼び出しは動作を繰り返したり、変更後の状態を読んだりする場合があります。

SUB Main()
    # lasttarget は以前に選択した物体です。Exists で存在を確認します。obj は ReadState
    # の唯一の引数で、関数は命令の結果をそのまま返します。コピーするコードに定義全体を含みます。

    IF UO.Exists('lasttarget') THEN
        VAR observed = ReadState('lasttarget')
        UO.Print('State 1/0: ' + CStr(observed))
    END IF
END SUB

SUB ReadState(obj)
    RETURN UO.GetDead(obj)
END SUB
```

**パラメーターと実行の説明:**

- lasttarget は以前に選択した物体です。Exists で存在を確認します。obj は ReadState の唯一の引数で、関数は命令の結果をそのまま返します。コピーするコードに定義全体を含みます。

### 半秒間の変化を検出する

```vb
# 半秒間の変化を検出する
#
# mobile が死亡しているか調べます。
#
# Integer Boolean：1 = TRUE、0 = FALSE。数値または引用符のない論理定数と比較できます。 mobile が IsDead なら 1、それ以外または存在しなければ
# 0。HP=0 だけで死亡とは判断しません。
#
# 論理的な結果です。1 = TRUE、0 = FALSE。VAR result = command(...) で保存した後は IF result = TRUE THEN または IF
# result = 1 THEN、否定時は IF result = FALSE THEN または IF result = 0 THEN と書けます。TRUE/FALSE
# に引用符は付けません。一度呼び出して保存してください。再呼び出しは動作を繰り返したり、変更後の状態を読んだりする場合があります。

SUB Main()
    # 引数なしの両呼び出しは self を読み、WAIT(500) は 500 ミリ秒です。二つのスナップショットの比較なので途中の変化を見逃す場合があります。無限待機はありません。

    VAR before = UO.GetDead()
    WAIT(500)
    VAR after = UO.GetDead()
    IF before <> after THEN
        UO.Print('State changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- 引数なしの両呼び出しは self を読み、WAIT(500) は 500 ミリ秒です。二つのスナップショットの比較なので途中の変化を見逃す場合があります。無限待機はありません。
