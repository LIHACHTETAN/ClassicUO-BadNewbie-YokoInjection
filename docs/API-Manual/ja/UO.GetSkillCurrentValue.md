# UO.GetSkillCurrentValue

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

修正値を含むスキルの有効値を読みます。

## 正確な構文

```text
UO.GetSkillCurrentValue(SkillName:Any) -> Decimal
```

## パラメーター

- `SkillName` — 必須のスキル指定："Mining" や "Animal Lore" などクライアントデータの名前、または数値・文字列で指定する十進数インデックス 0..Skills.Length−1。名前は大文字小文字を区別せず、前後空白を除去し、_ を空白に置換します。アイテム ID や 1 始まりの番号ではありません。数値文字列は常にインデックスです。

## 戻り値

Decimal (Double) — 0.1 刻みのスキル点数。例は 951 ではなく 95.1。フィールド ValueFixed を直接 Double として 10 で割ります。0 はスキル値ゼロ、またはキャラクター/スキル不在です。Boolean ではありません。旧 SkillVal/BaseVal は別の尺度なので混用しないでください。

## 動作

- Invoke はゲームスレッドで既存データを読み、ネットワークパケットを送りません。スキルを使用・訓練しません。二回の照会は独立したスナップショットです。
- 必須のスキル指定："Mining" や "Animal Lore" などクライアントデータの名前、または数値・文字列で指定する十進数インデックス 0..Skills.Length−1。名前は大文字小文字を区別せず、前後空白を除去し、_ を空白に置換します。アイテム ID や 1 始まりの番号ではありません。数値文字列は常にインデックスです。
- ExecuteStealthCompatibility が分岐を選びます。Text はスキル指定、Arg は数値番号とモードを読みます。変換不能な引数は変換エラーになる場合があります。

### 内部関数：呼び出しから結果まで

実際の C# 内部処理を示します。ReadValue は例に完全な定義を含む補助関数で、隠れた組み込み命令ではありません。

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility が分岐を選びます。Text はスキル指定、Arg は数値番号とモードを読みます。変換不能な引数は変換エラーになる場合があります。

Decimal (Double) — 0.1 刻みのスキル点数。例は 951 ではなく 95.1。フィールド ValueFixed を直接 Double として 10 で割ります。0 はスキル値ゼロ、またはキャラクター/スキル不在です。Boolean ではありません。旧 SkillVal/BaseVal は別の尺度なので混用しないでください。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke はゲームスレッドで読み取ります。ワーカースレッドはマネージャーによる処理を待ち、スクリプトのキャンセルで待機を中断します。追加の遅延や通信要求はありません。

Invoke はゲームスレッドで既存データを読み、ネットワークパケットを送りません。スキルを使用・訓練しません。二回の照会は独立したスナップショットです。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe は最初に十進数インデックスと範囲を検証し、それ以外は名前を正規化して Skill.Name と大文字小文字を区別せず完全一致で検索します。不明名は null となり、ターゲットを開きません。

不明なスキルまたはキャラクター不在では −1 を返します。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `FindSkillUnsafe`.

#### 4. GetSkillValue

GetSkillValue は BaseFixed、ValueFixed、CapFixed を選び、整数の十分位値を 10d で割ります。途中で Single に丸めません。

Decimal (Double) — 0.1 刻みのスキル点数。例は 951 ではなく 95.1。フィールド ValueFixed を直接 Double として 10 で割ります。0 はスキル値ゼロ、またはキャラクター/スキル不在です。Boolean ではありません。旧 SkillVal/BaseVal は別の尺度なので混用しないでください。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `GetSkillValue`.

Invoke はゲームスレッドで既存データを読み、ネットワークパケットを送りません。スキルを使用・訓練しません。二回の照会は独立したスナップショットです。


## 使用例

### 読み取って表示

```vb
# 読み取って表示
#
# 修正値を含むスキルの有効値を読みます。
#
# Decimal (Double) — 0.1 刻みのスキル点数。例は 951 ではなく 95.1。フィールド ValueFixed を直接 Double として 10 で割ります。0
# はスキル値ゼロ、またはキャラクター/スキル不在です。Boolean ではありません。旧 SkillVal/BaseVal は別の尺度なので混用しないでください。

SUB Main()
    # selector と、書き込みの場合は mode を明示します。最初の行で名前によりスキル、番号により能力値を選択します。Print は表示のみです。

    VAR selector = 'Mining'
    VAR value = UO.GetSkillCurrentValue(selector)
    UO.Print(CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- selector と、書き込みの場合は mode を明示します。最初の行で名前によりスキル、番号により能力値を選択します。Print は表示のみです。

### 条件や比較に使用

```vb
# 条件や比較に使用
#
# 修正値を含むスキルの有効値を読みます。
#
# Decimal (Double) — 0.1 刻みのスキル点数。例は 951 ではなく 95.1。フィールド ValueFixed を直接 Double として 10 で割ります。0
# はスキル値ゼロ、またはキャラクター/スキル不在です。Boolean ではありません。旧 SkillVal/BaseVal は別の尺度なので混用しないでください。

SUB Main()
    # しきい値 95.1 とモード 0/1/2 は例の設定です。変更前に −1 を確認します。書き込み後の読み取りはローカルコピーであり、サーバー承認を待ちません。

    IF UO.GetSkillLockState('Mining') >= 0 THEN
        VAR value = UO.GetSkillCurrentValue('Mining')
        IF value >= 95.1 THEN
            UO.Print('Value >= 95.1: ' + CStr(value))
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
# 修正値を含むスキルの有効値を読みます。
#
# Decimal (Double) — 0.1 刻みのスキル点数。例は 951 ではなく 95.1。フィールド ValueFixed を直接 Double として 10 で割ります。0
# はスキル値ゼロ、またはキャラクター/スキル不在です。Boolean ではありません。旧 SkillVal/BaseVal は別の尺度なので混用しないでください。

SUB Main()
    # Main の後に補助関数全体を示します。selector はスキル/能力値、mode は書き込みモードです。ReadValue/ReadMode は元の数値を返し、ApplyMode
    # は引数を検証して処理するだけで戻り値はありません。WAIT(1000) は二つの読み取りを区切ります。

    VAR before = ReadValue('Animal_Lore')
    WAIT(1000)
    VAR after = ReadValue('Animal Lore')
    UO.Print(CStr(after - before))
END SUB

SUB ReadValue(selector)
    RETURN UO.GetSkillCurrentValue(selector)
END SUB
```

**パラメーターと実行の説明:**

- Main の後に補助関数全体を示します。selector はスキル/能力値、mode は書き込みモードです。ReadValue/ReadMode は元の数値を返し、ApplyMode は引数を検証して処理するだけで戻り値はありません。WAIT(1000) は二つの読み取りを区切ります。
