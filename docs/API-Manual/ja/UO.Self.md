# UO.Self

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

現在のキャラクターの ID を返します。

## 正確な構文

```text
UO.Self() -> Integer
```

## パラメーター

引数はありません。

## 戻り値

Integer — serial/ID です。graphic/type、レイヤー、個数、Boolean ではありません。0 は現在のオブジェクトなし。32 ビットを保持するため、= TRUE や > 0 ではなく <> 0 で確認します。保存した値は自動更新されません。 World.Player.Serial を読みます。Player が存在しないか破棄済みなら 0。死亡と破棄は別です。存在する幽霊にもキャラクター ID があります。

## 動作

- 引数なし。Invoke を通してゲームスレッドでローカル状態を読みます。スクリプトの取消でその待機を中断できます。パケット送信、コンテナ表示、target 開始、アイテム移動は行いません。
- 括弧なしの self/backpack は変数で隠されない限り毎回読み直します。引用符付きの別名は受け取るコマンドが解決します。移動先の "self" はバックパックですが、UO.Self() はキャラクター serial です。コンテナ ID には UO.Backpack() を指定します。
- World.Clear で Player が除去され、以降は 0 です。ログインやバッグ交換で ID が変わる場合があります。複数回の読み取りは不可分なスナップショットではありません。非ゼロ ID は接続、サーバー許可、中身の読込完了を保証しません。

### 内部関数：呼び出しから結果まで

以下は実際のクライアントオブジェクトを読む内部手順です。IsOwnSerial は例に完全定義された補助関数であり、別の組み込み API ではありません。

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility が引数なしの分岐を選び、bridge の整数を InjectionValue に包みます。Pascal の出力引数や追加の省略可能引数はありません。

Integer — serial/ID です。graphic/type、レイヤー、個数、Boolean ではありません。0 は現在のオブジェクトなし。32 ビットを保持するため、= TRUE や > 0 ではなく <> 0 で確認します。保存した値は自動更新されません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ExecuteStealthCompatibility`.

#### 2. Invoke

World.Player.Serial を読みます。Player が存在しないか破棄済みなら 0。死亡と破棄は別です。存在する幽霊にもキャラクター ID があります。 Invoke はゲームスレッドで読み取ります。ワーカースレッドはマネージャーによる処理を待ち、スクリプトのキャンセルで待機を中断します。追加の遅延や通信要求はありません。

Integer — serial/ID です。graphic/type、レイヤー、個数、Boolean ではありません。0 は現在のオブジェクトなし。32 ビットを保持するため、= TRUE や > 0 ではなく <> 0 で確認します。保存した値は自動更新されません。 引数なし。Invoke を通してゲームスレッドでローカル状態を読みます。スクリプトの取消でその待機を中断できます。パケット送信、コンテナ表示、target 開始、アイテム移動は行いません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 3. Clear

World.Clear で Player が除去され、以降は 0 です。ログインやバッグ交換で ID が変わる場合があります。複数回の読み取りは不可分なスナップショットではありません。非ゼロ ID は接続、サーバー許可、中身の読込完了を保証しません。

World.Clear で Player が除去され、以降は 0 です。ログインやバッグ交換で ID が変わる場合があります。複数回の読み取りは不可分なスナップショットではありません。非ゼロ ID は接続、サーバー許可、中身の読込完了を保証しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Clear`.

World.Clear で Player が除去され、以降は 0 です。ログインやバッグ交換で ID が変わる場合があります。複数回の読み取りは不可分なスナップショットではありません。非ゼロ ID は接続、サーバー許可、中身の読込完了を保証しません。


## 使用例

### ID を取得して表示

```vb
# ID を取得して表示
#
# 現在のキャラクターの ID を返します。
#
# Integer — serial/ID です。graphic/type、レイヤー、個数、Boolean ではありません。0 は現在のオブジェクトなし。32 ビットを保持するため、=
# TRUE や > 0 ではなく <> 0 で確認します。保存した値は自動更新されません。 World.Player.Serial を読みます。Player が存在しないか破棄済みなら
# 0。死亡と破棄は別です。存在する幽霊にもキャラクター ID があります。

SUB Main()
    # id に一度の結果を保存し、HEX で日誌向けに書式化します。オブジェクトの選択や使用はしません。

    VAR id = UO.Self()
    UO.Print('ID: ' + HEX(id))
END SUB
```

**パラメーターと実行の説明:**

- id に一度の結果を保存し、HEX で日誌向けに書式化します。オブジェクトの選択や使用はしません。

### ID の変更を検出

```vb
# ID の変更を検出
#
# 現在のキャラクターの ID を返します。
#
# Integer — serial/ID です。graphic/type、レイヤー、個数、Boolean ではありません。0 は現在のオブジェクトなし。32 ビットを保持するため、=
# TRUE や > 0 ではなく <> 0 で確認します。保存した値は自動更新されません。 World.Player.Serial を読みます。Player が存在しないか破棄済みなら
# 0。死亡と破棄は別です。存在する幽霊にもキャラクター ID があります。

SUB Main()
    # before/after は 250 ミリ秒間隔です。WAIT は例にのみ含まれます。両端が同じでも途中の変化は見落とす場合があります。

    VAR before = UO.Self()
    WAIT(250)
    VAR after = UO.Self()
    IF before <> after THEN
        UO.Print('ID changed: ' + HEX(after))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- before/after は 250 ミリ秒間隔です。WAIT は例にのみ含まれます。両端が同じでも途中の変化は見落とす場合があります。

### 完全な IsOwnSerial 関数

```vb
# 完全な IsOwnSerial 関数
#
# 現在のキャラクターの ID を返します。
#
# Integer — serial/ID です。graphic/type、レイヤー、個数、Boolean ではありません。0 は現在のオブジェクトなし。32 ビットを保持するため、=
# TRUE や > 0 ではなく <> 0 で確認します。保存した値は自動更新されません。 World.Player.Serial を読みます。Player が存在しないか破棄済みなら
# 0。死亡と破棄は別です。存在する幽霊にもキャラクター ID があります。

SUB Main()
    # candidate は保存済み LastTarget ID。IsOwnSerial(candidate) は serial を一つ受け取り、現在の非ゼロの自身 ID なら Integer
    # Boolean の 1=TRUE、それ以外は 0=FALSE を返します。定義は完全で target を変更しません。

    VAR candidate = UO.LastTarget()
    IF IsOwnSerial(candidate) = TRUE THEN
        UO.Print('Own object selected')
    ELSE
        UO.Print('Different object or no own object')
    END IF
END SUB

SUB IsOwnSerial(candidate)
    VAR current = UO.Self()
    RETURN current <> 0 AND current = candidate
END SUB
```

**パラメーターと実行の説明:**

- candidate は保存済み LastTarget ID。IsOwnSerial(candidate) は serial を一つ受け取り、現在の非ゼロの自身 ID なら Integer Boolean の 1=TRUE、それ以外は 0=FALSE を返します。定義は完全で target を変更しません。
