# UO.SetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

能力値成長モードの変更を要求します。

## 正確な構文

```text
UO.SetStatLockState(statNum:Any, statState:Any) -> Unit
```

## パラメーター

- `statNum` — 必須の能力値番号：0 — STR、1 — DEX、2 — INT。現在値や文字列の名前ではありません。
- `statState` — 必須のモード：0 — 上昇、1 — 下降、2 — 固定。三つのコードであり Boolean ではなく、true/false では全モードを表せません。

## 戻り値

Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

## 動作

- 有効な要求は GameActions で一つのパケットを送り、直ちにローカルモードを更新します。サーバー規則が適用され、成長は保証されません。不明スキル、不正な番号/モード、キャラクター不在では送信せず無視します。
- 必須の能力値番号：0 — STR、1 — DEX、2 — INT。現在値や文字列の名前ではありません。
- ExecuteStealthCompatibility が分岐を選びます。Text はスキル指定、Arg は数値番号とモードを読みます。変換不能な引数は変換エラーになる場合があります。

### 内部関数：呼び出しから結果まで

実際の C# 内部処理を示します。ApplyMode は例に完全な定義を含む補助関数で、隠れた組み込み命令ではありません。

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility が分岐を選びます。Text はスキル指定、Arg は数値番号とモードを読みます。変換不能な引数は変換エラーになる場合があります。

Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke はゲームスレッドで読み取ります。ワーカースレッドはマネージャーによる処理を待ち、スクリプトのキャンセルで待機を中断します。追加の遅延や通信要求はありません。

有効な要求は GameActions で一つのパケットを送り、直ちにローカルモードを更新します。サーバー規則が適用され、成長は保証されません。不明スキル、不正な番号/モード、キャラクター不在では送信せず無視します。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 3. SetStatLockState

GetStatLockState/SetStatLockState は 0/1/2 で StrLock、DexLock、IntLock を選びます。不明番号は −1 を読み、書き込みでは送信前に両方の範囲を検証します。

Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `SetStatLockState`.

#### 4. ChangeStatLock

有効な要求は GameActions で一つのパケットを送り、直ちにローカルモードを更新します。サーバー規則が適用され、成長は保証されません。不明スキル、不正な番号/モード、キャラクター不在では送信せず無視します。

Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/GameActions.cs`; 関数 `ChangeStatLock`.

有効な要求は GameActions で一つのパケットを送り、直ちにローカルモードを更新します。サーバー規則が適用され、成長は保証されません。不明スキル、不正な番号/モード、キャラクター不在では送信せず無視します。


## 使用例

### 読み取って表示

```vb
# 読み取って表示
#
# 能力値成長モードの変更を要求します。
#
# Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

SUB Main()
    # selector と、書き込みの場合は mode を明示します。最初の行で名前によりスキル、番号により能力値を選択します。Print は表示のみです。

    VAR selector = 0
    VAR mode = 2
    UO.SetStatLockState(selector, mode)
    UO.Print(CStr(UO.GetStatLockState(selector)))
END SUB
```

**パラメーターと実行の説明:**

- selector と、書き込みの場合は mode を明示します。最初の行で名前によりスキル、番号により能力値を選択します。Print は表示のみです。

### 条件や比較に使用

```vb
# 条件や比較に使用
#
# 能力値成長モードの変更を要求します。
#
# Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

SUB Main()
    # しきい値 95.1 とモード 0/1/2 は例の設定です。変更前に −1 を確認します。書き込み後の読み取りはローカルコピーであり、サーバー承認を待ちません。

    VAR selector = 0
    VAR before = UO.GetStatLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetStatLockState(selector, 0)
        UO.Print(CStr(UO.GetStatLockState(selector)))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- しきい値 95.1 とモード 0/1/2 は例の設定です。変更前に −1 を確認します。書き込み後の読み取りはローカルコピーであり、サーバー承認を待ちません。

### 完全な補助関数

```vb
# 完全な補助関数
#
# 能力値成長モードの変更を要求します。
#
# Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

SUB Main()
    # Main の後に補助関数全体を示します。selector はスキル/能力値、mode は書き込みモードです。ReadValue/ReadMode は元の数値を返し、ApplyMode
    # は引数を検証して処理するだけで戻り値はありません。WAIT(1000) は二つの読み取りを区切ります。

    ApplyMode(0, 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetStatLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetStatLockState(selector, mode)
END SUB
```

**パラメーターと実行の説明:**

- Main の後に補助関数全体を示します。selector はスキル/能力値、mode は書き込みモードです。ReadValue/ReadMode は元の数値を返し、ApplyMode は引数を検証して処理するだけで戻り値はありません。WAIT(1000) は二つの読み取りを区切ります。
