# UO.GetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

能力値のローカル成長モードを読みます。

## 正確な構文

```text
UO.GetStatLockState(statNum:Any) -> Integer
```

## パラメーター

- `statNum` — 必須の能力値番号：0 — STR、1 — DEX、2 — INT。現在値や文字列の名前ではありません。

## 戻り値

Integer：0 — 上昇、1 — 下降、2 — 固定。モードコードであり true/false ではありません。 0..2 以外の番号では −1。キャラクター不在時の有効番号は既定値 0 となり、サーバー状態の確認にはなりません。

## 動作

- Invoke はゲームスレッドで既存データを読み、ネットワークパケットを送りません。スキルを使用・訓練しません。二回の照会は独立したスナップショットです。
- 必須の能力値番号：0 — STR、1 — DEX、2 — INT。現在値や文字列の名前ではありません。
- ExecuteStealthCompatibility が分岐を選びます。Text はスキル指定、Arg は数値番号とモードを読みます。変換不能な引数は変換エラーになる場合があります。

### 内部関数：呼び出しから結果まで

実際の C# 内部処理を示します。ReadMode は例に完全な定義を含む補助関数で、隠れた組み込み命令ではありません。

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility が分岐を選びます。Text はスキル指定、Arg は数値番号とモードを読みます。変換不能な引数は変換エラーになる場合があります。

Integer：0 — 上昇、1 — 下降、2 — 固定。モードコードであり true/false ではありません。 0..2 以外の番号では −1。キャラクター不在時の有効番号は既定値 0 となり、サーバー状態の確認にはなりません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke はゲームスレッドで読み取ります。ワーカースレッドはマネージャーによる処理を待ち、スクリプトのキャンセルで待機を中断します。追加の遅延や通信要求はありません。

Invoke はゲームスレッドで既存データを読み、ネットワークパケットを送りません。スキルを使用・訓練しません。二回の照会は独立したスナップショットです。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 3. GetStatLockState

GetStatLockState/SetStatLockState は 0/1/2 で StrLock、DexLock、IntLock を選びます。不明番号は −1 を読み、書き込みでは送信前に両方の範囲を検証します。

Integer：0 — 上昇、1 — 下降、2 — 固定。モードコードであり true/false ではありません。 0..2 以外の番号では −1。キャラクター不在時の有効番号は既定値 0 となり、サーバー状態の確認にはなりません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `GetStatLockState`.

Invoke はゲームスレッドで既存データを読み、ネットワークパケットを送りません。スキルを使用・訓練しません。二回の照会は独立したスナップショットです。


## 使用例

### 読み取って表示

```vb
# 読み取って表示
#
# 能力値のローカル成長モードを読みます。
#
# Integer：0 — 上昇、1 — 下降、2 — 固定。モードコードであり true/false ではありません。 0..2 以外の番号では −1。キャラクター不在時の有効番号は既定値
# 0 となり、サーバー状態の確認にはなりません。

SUB Main()
    # selector と、書き込みの場合は mode を明示します。最初の行で名前によりスキル、番号により能力値を選択します。Print は表示のみです。

    VAR selector = 0
    VAR mode = UO.GetStatLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**パラメーターと実行の説明:**

- selector と、書き込みの場合は mode を明示します。最初の行で名前によりスキル、番号により能力値を選択します。Print は表示のみです。

### 条件や比較に使用

```vb
# 条件や比較に使用
#
# 能力値のローカル成長モードを読みます。
#
# Integer：0 — 上昇、1 — 下降、2 — 固定。モードコードであり true/false ではありません。 0..2 以外の番号では −1。キャラクター不在時の有効番号は既定値
# 0 となり、サーバー状態の確認にはなりません。

SUB Main()
    # しきい値 95.1 とモード 0/1/2 は例の設定です。変更前に −1 を確認します。書き込み後の読み取りはローカルコピーであり、サーバー承認を待ちません。

    VAR mode = UO.GetStatLockState(0)
    IF mode = 2 THEN
        UO.Print("Locked")
    ELSE
        IF mode = -1 THEN
            UO.Print("Unknown selector")
        ELSE
            UO.Print("Mode: " + CStr(mode))
        END IF
    END IF
END SUB
```

**パラメーターと実行の説明:**

- しきい値 95.1 とモード 0/1/2 は例の設定です。変更前に −1 を確認します。書き込み後の読み取りはローカルコピーであり、サーバー承認を待ちません。

### 完全な補助関数

```vb
# 完全な補助関数
#
# 能力値のローカル成長モードを読みます。
#
# Integer：0 — 上昇、1 — 下降、2 — 固定。モードコードであり true/false ではありません。 0..2 以外の番号では −1。キャラクター不在時の有効番号は既定値
# 0 となり、サーバー状態の確認にはなりません。

SUB Main()
    # Main の後に補助関数全体を示します。selector はスキル/能力値、mode は書き込みモードです。ReadValue/ReadMode は元の数値を返し、ApplyMode
    # は引数を検証して処理するだけで戻り値はありません。WAIT(1000) は二つの読み取りを区切ります。

    VAR before = ReadMode(0)
    WAIT(1000)
    VAR after = ReadMode(0)
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetStatLockState(selector)
END SUB
```

**パラメーターと実行の説明:**

- Main の後に補助関数全体を示します。selector はスキル/能力値、mode は書き込みモードです。ReadValue/ReadMode は元の数値を返し、ApplyMode は引数を検証して処理するだけで戻り値はありません。WAIT(1000) は二つの読み取りを区切ります。
