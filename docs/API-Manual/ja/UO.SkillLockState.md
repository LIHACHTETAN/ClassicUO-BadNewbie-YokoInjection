# UO.SkillLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

スキル成長モードの変更を要求します。

## 正確な構文

```text
UO.SkillLockState(SkillName:Any, skillState:Any) -> Unit
```

## パラメーター

- `SkillName` — 必須のスキル指定："Mining" や "Animal Lore" などクライアントデータの名前、または数値・文字列で指定する十進数インデックス 0..Skills.Length−1。名前は大文字小文字を区別せず、前後空白を除去し、_ を空白に置換します。アイテム ID や 1 始まりの番号ではありません。数値文字列は常にインデックスです。
- `skillState` — 必須のモード：0 — 上昇、1 — 下降、2 — 固定。三つのコードであり Boolean ではなく、true/false では全モードを表せません。

## 戻り値

Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

## 動作

- 有効な要求は GameActions で一つのパケットを送り、直ちにローカルモードを更新します。サーバー規則が適用され、成長は保証されません。不明スキル、不正な番号/モード、キャラクター不在では送信せず無視します。
- 必須のスキル指定："Mining" や "Animal Lore" などクライアントデータの名前、または数値・文字列で指定する十進数インデックス 0..Skills.Length−1。名前は大文字小文字を区別せず、前後空白を除去し、_ を空白に置換します。アイテム ID や 1 始まりの番号ではありません。数値文字列は常にインデックスです。
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

#### 3. FindSkillUnsafe

FindSkillUnsafe は最初に十進数インデックスと範囲を検証し、それ以外は名前を正規化して Skill.Name と大文字小文字を区別せず完全一致で検索します。不明名は null となり、ターゲットを開きません。

不明なスキルまたはキャラクター不在では −1 を返します。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `FindSkillUnsafe`.

#### 4. SetSkillLockState

有効な要求は GameActions で一つのパケットを送り、直ちにローカルモードを更新します。サーバー規則が適用され、成長は保証されません。不明スキル、不正な番号/モード、キャラクター不在では送信せず無視します。

Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `SetSkillLockState`.

#### 5. ChangeSkillLockStatus

有効な要求は GameActions で一つのパケットを送り、直ちにローカルモードを更新します。サーバー規則が適用され、成長は保証されません。不明スキル、不正な番号/モード、キャラクター不在では送信せず無視します。

Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/GameActions.cs`; 関数 `ChangeSkillLockStatus`.

有効な要求は GameActions で一つのパケットを送り、直ちにローカルモードを更新します。サーバー規則が適用され、成長は保証されません。不明スキル、不正な番号/モード、キャラクター不在では送信せず無視します。


## 使用例

### 読み取って表示

```vb
# 読み取って表示
#
# スキル成長モードの変更を要求します。
#
# Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

SUB Main()
    # selector と、書き込みの場合は mode を明示します。最初の行で名前によりスキル、番号により能力値を選択します。Print は表示のみです。

    VAR selector = 'Mining'
    VAR mode = 2
    UO.SkillLockState(selector, mode)
    UO.Print(CStr(UO.GetSkillLockState(selector)))
END SUB
```

**パラメーターと実行の説明:**

- selector と、書き込みの場合は mode を明示します。最初の行で名前によりスキル、番号により能力値を選択します。Print は表示のみです。

### 条件や比較に使用

```vb
# 条件や比較に使用
#
# スキル成長モードの変更を要求します。
#
# Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

SUB Main()
    # しきい値 95.1 とモード 0/1/2 は例の設定です。変更前に −1 を確認します。書き込み後の読み取りはローカルコピーであり、サーバー承認を待ちません。

    VAR selector = 'Mining'
    VAR before = UO.GetSkillLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SkillLockState(selector, 0)
        UO.Print(CStr(UO.GetSkillLockState(selector)))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- しきい値 95.1 とモード 0/1/2 は例の設定です。変更前に −1 を確認します。書き込み後の読み取りはローカルコピーであり、サーバー承認を待ちません。

### 完全な補助関数

```vb
# 完全な補助関数
#
# スキル成長モードの変更を要求します。
#
# Unit — 戻り値はありません。成功/失敗として扱ったり true と比較したりしないでください。後で読めるのはローカルモデルであり、サーバーの承認ではありません。

SUB Main()
    # Main の後に補助関数全体を示します。selector はスキル/能力値、mode は書き込みモードです。ReadValue/ReadMode は元の数値を返し、ApplyMode
    # は引数を検証して処理するだけで戻り値はありません。WAIT(1000) は二つの読み取りを区切ります。

    ApplyMode('Mining', 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetSkillLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SkillLockState(selector, mode)
END SUB
```

**パラメーターと実行の説明:**

- Main の後に補助関数全体を示します。selector はスキル/能力値、mode は書き込みモードです。ReadValue/ReadMode は元の数値を返し、ApplyMode は引数を検証して処理するだけで戻り値はありません。WAIT(1000) は二つの読み取りを区切ります。
