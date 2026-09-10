# UO.PredictedX

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

プレイヤーが現在キューに入れている移動ステップの後に予測されるX 座標を読みます。

## 正確な構文

```text
UO.PredictedX() -> Integer
```

## パラメーター

引数はありません。

## 戻り値

Integer X。単位はマップのマス。0 は有効な座標、またはプレイヤー不在です。

## 動作

- 構文に示す引数なしの UO 関数のみ。target、serial、type、目的地、距離、timeout は受け取りません。数値であり Boolean、ID、tile レコードではありません。1 は到着を意味しません。
- GetEndPosition はキューの最後の Mobile.Step の X/Y/Z/方向を読みます。キューが空なら現在位置と方向を読みます。O(1) の参照であり、ステップの取り出し、移動、パケット送信、経路計算、到着待ちは行いません。
- X/Y はワールド／マップ座標で、コンテナ gump のピクセル座標ではありません。Z は高さで階数ではありません。単一成分を返し、配列や経路全体の最終目的地は返しません。
- ローカル予測であり、到着の確認ではありません。ステップの追加／完了／拒否、キューのクリア、テレポートで変化します。各成分の個別呼び出しは原子的なスナップショットではなく、X の一致だけでは Y/Z やサーバーの承認を証明できません。
- Invoke はゲームスレッドで読み取ります。ワーカースレッドはマネージャーによる処理を待ち、スクリプトのキャンセルで待機を中断します。追加の遅延や通信要求はありません。
- IPredictedMovementBridge を持たない外部 IApiBridge は現在座標／方向へのフォールバックを維持します。Classic UO はキューを参照するインターフェースを実装しています。

### 内部関数：呼び出しから結果まで

実際のネイティブ読み取り段階です。PredictionEquals は完全に定義したユーザー BASIC 補助関数で、内部コマンドや移動手続きではありません。

#### 1. ExecuteStealthCompatibility

ネイティブ関数が ReadPredictedCoordinate を呼び、対応する IPredictedMovementBridge プロパティを選びます。NewMoveXY や経路探索は開始しません。

構文に示す引数なしの UO 関数のみ。target、serial、type、目的地、距離、timeout は受け取りません。数値であり Boolean、ID、tile レコードではありません。1 は到着を意味しません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ExecuteStealthCompatibility`.

#### 2. ReadPredictedCoordinate

ネイティブ関数が ReadPredictedCoordinate を呼び、対応する IPredictedMovementBridge プロパティを選びます。NewMoveXY や経路探索は開始しません。

IPredictedMovementBridge を持たない外部 IApiBridge は現在座標／方向へのフォールバックを維持します。Classic UO はキューを参照するインターフェースを実装しています。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ReadPredictedCoordinate`.

#### 3. Invoke

Invoke はゲームスレッドで読み取ります。ワーカースレッドはマネージャーによる処理を待ち、スクリプトのキャンセルで待機を中断します。追加の遅延や通信要求はありません。

Integer X。単位はマップのマス。0 は有効な座標、またはプレイヤー不在です。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 4. ReadPredictedPosition

Player が不在または破棄済みなら ReadPredictedPosition は 0 を返します。それ以外は GetEndPosition を呼んで一成分を選択します。

GetEndPosition はキューの最後の Mobile.Step の X/Y/Z/方向を読みます。キューが空なら現在位置と方向を読みます。O(1) の参照であり、ステップの取り出し、移動、パケット送信、経路計算、到着待ちは行いません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `ReadPredictedPosition`.

#### 5. GetEndPosition

GetEndPosition はキューの最後の Mobile.Step の X/Y/Z/方向を読みます。キューが空なら現在位置と方向を読みます。O(1) の参照であり、ステップの取り出し、移動、パケット送信、経路計算、到着待ちは行いません。

X/Y はワールド／マップ座標で、コンテナ gump のピクセル座標ではありません。Z は高さで階数ではありません。単一成分を返し、配列や経路全体の最終目的地は返しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/GameObjects/Mobile.cs`; 関数 `GetEndPosition`.

#### 6. InjectionValue

Integer X。単位はマップのマス。0 は有効な座標、またはプレイヤー不在です。

ローカル予測であり、到着の確認ではありません。ステップの追加／完了／拒否、キューのクリア、テレポートで変化します。各成分の個別呼び出しは原子的なスナップショットではなく、X の一致だけでは Y/Z やサーバーの承認を証明できません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs`; 関数 `InjectionValue`.

PredictionEquals(expected) は数値の座標／高さ／方向を受け取り、プレイヤー不在を拒否し、一つの予測成分を比較します。Integer Boolean の 1=TRUE または 0=FALSE を返し、到着を待機も保証もしません。


## 使用例

### 一つの成分を読む

```vb
# 一つの成分を読む
#
# プレイヤーが現在キューに入れている移動ステップの後に予測されるX 座標を読みます。
#
# Integer X。単位はマップのマス。0 は有効な座標、またはプレイヤー不在です。

SUB Main()
    # predicted は引数なしの呼び出し結果を一度保存します。CStr はログ表示用に数値を整形します。

    VAR predicted = UO.PredictedX()
    UO.Print('Predicted: ' + CStr(predicted))
END SUB
```

**パラメーターと実行の説明:**

- predicted は引数なしの呼び出し結果を一度保存します。CStr はログ表示用に数値を整形します。

### 予測の変化を観察する

```vb
# 予測の変化を観察する
#
# プレイヤーが現在キューに入れている移動ステップの後に予測されるX 座標を読みます。
#
# Integer X。単位はマップのマス。0 は有効な座標、またはプレイヤー不在です。

SUB Main()
    # WAIT(100) は例を 100 ミリ秒停止します。途中で移動しても before/after が一致する場合があります。読み取り自体は移動を開始しません。

    VAR before = UO.PredictedX()
    WAIT(100)
    VAR after = UO.PredictedX()
    IF before <> after THEN
        UO.Print('Prediction changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- WAIT(100) は例を 100 ミリ秒停止します。途中で移動しても before/after が一致する場合があります。読み取り自体は移動を開始しません。

### 完全な比較補助関数

```vb
# 完全な比較補助関数
#
# プレイヤーが現在キューに入れている移動ステップの後に予測されるX 座標を読みます。
#
# Integer X。単位はマップのマス。0 は有効な座標、またはプレイヤー不在です。

SUB Main()
    # expected は例の座標／高さ／方向で、ネイティブコマンドの引数ではありません。PredictionEquals は UO.Self() を確認して一度読み、一致なら
    # 1=TRUE、それ以外は 0=FALSE を返します。Main の下に完全な定義があります。一成分の一致は到着ではありません。

    IF PredictionEquals(1445) = TRUE THEN
        UO.Print('Queued endpoint matches this component')
    ELSE
        UO.Print('Different component or no player')
    END IF
END SUB

SUB PredictionEquals(expected)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR predicted = UO.PredictedX()
    RETURN predicted = expected
END SUB
```

**パラメーターと実行の説明:**

- expected は例の座標／高さ／方向で、ネイティブコマンドの引数ではありません。PredictionEquals は UO.Self() を確認して一度読み、一致なら 1=TRUE、それ以外は 0=FALSE を返します。Main の下に完全な定義があります。一成分の一致は到着ではありません。
