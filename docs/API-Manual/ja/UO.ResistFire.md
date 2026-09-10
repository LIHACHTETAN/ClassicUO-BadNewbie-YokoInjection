# UO.ResistFire

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

現在のプレイヤーの抵抗フィールドを読み取ります：炎。

## 正確な構文

```text
UO.ResistFire() -> Integer
```

## パラメーター

引数はありません。

## 戻り値

Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1 は1ポイントであり、成功の意味ではありません。

## 動作

- 引数はありません。表示された正確なシグネチャを使用します。
- ゲームスレッドで Player.FireResistance を読みます。現在の Player が存在しないか破棄済みなら 0。装備の検索、ボーナス計算、ステータス要求、更新待ちは行いません。存在する幽霊と破棄済み Player は別です。
- 属性抵抗は CharacterStatus（0x11）の type >= 4 で届きます。呼び出し自体はサーバーの時代を判定しません。欄のない簡易／旧式ステータスでは以前のキャッシュを維持し、新規 Player は 0 から始まります。毒抵抗は Poisoned フラグではなく、各抵抗は Resisting Spells スキルでもありません。
- CharacterStatus は固定部分を検証してから状態を変更し、抵抗の word を符号付き Int16 に変換します。固定部分の欠落時は以前の状態を維持します。type 6 の省略可能な末尾は従来の処理を維持します。ここではその抵抗上限を読みません。
- 呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。
- RegisterCharacterGetterAliases は不足する引数なし関数と組み込み名を登録します。既存の互換分岐も同じ欄を読みます。名前の大小文字は不問で、括弧なしの組み込み名は変数で隠されなければ毎回読み取ります。

### 内部関数：呼び出しから結果まで

ローカル読み取りの実際のネイティブ処理です。下の ResistanceAtLeast は完全に定義したユーザー BASIC 関数で、隠し API や防具の装備命令ではありません。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases は不足する引数なし関数と組み込み名を登録します。既存の互換分岐も同じ欄を読みます。名前の大小文字は不問で、括弧なしの組み込み名は変数で隠されなければ毎回読み取ります。

`FireResist ResistFire GetFireResist GetResistFire`.

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `RegisterCharacterGetterAliases`.

#### 2. Invoke

ゲームスレッドで Player.FireResistance を読みます。現在の Player が存在しないか破棄済みなら 0。装備の検索、ボーナス計算、ステータス要求、更新待ちは行いません。存在する幽霊と破棄済み Player は別です。

Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 3. CharacterStatus

CharacterStatus は固定部分を検証してから状態を変更し、抵抗の word を符号付き Int16 に変換します。固定部分の欠落時は以前の状態を維持します。type 6 の省略可能な末尾は従来の処理を維持します。ここではその抵抗上限を読みません。

属性抵抗は CharacterStatus（0x11）の type >= 4 で届きます。呼び出し自体はサーバーの時代を判定しません。欄のない簡易／旧式ステータスでは以前のキャッシュを維持し、新規 Player は 0 から始まります。毒抵抗は Poisoned フラグではなく、各抵抗は Resisting Spells スキルでもありません。

プロジェクトのソース: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 関数 `CharacterStatus`.

#### 4. Clear

World.Clear は Player を除去します。プレイヤーとデータが戻るまでは 0。再接続後の条件達成を保存済みの値だけで判断しません。

Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1 は1ポイントであり、成功の意味ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Clear`.

呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。


## 使用例

### キャッシュ値を表示

```vb
# キャッシュ値を表示
#
# 現在のプレイヤーの抵抗フィールドを読み取ります：炎。
#
# Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player
# の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1
# は1ポイントであり、成功の意味ではありません。

SUB Main()
    # value は引数なしのプレイヤー読み取りを一度保存します。CStr はジャーナル用に文字列化します。

    VAR value = UO.ResistFire()
    UO.Print('FireResistance: ' + CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value は引数なしのプレイヤー読み取りを一度保存します。CStr はジャーナル用に文字列化します。

### 二つの観察結果を比較

```vb
# 二つの観察結果を比較
#
# 現在のプレイヤーの抵抗フィールドを読み取ります：炎。
#
# Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player
# の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1
# は1ポイントであり、成功の意味ではありません。

SUB Main()
    # before と after の間に WAIT(500)、500ミリ秒の待機があります。difference は負にもなり、中間更新を見落とすことがあります。この待機はサンプルの処理です。

    VAR before = UO.ResistFire()
    WAIT(500)
    VAR after = UO.ResistFire()
    VAR difference = after - before
    UO.Print('Resistance change: ' + CStr(difference))
END SUB
```

**パラメーターと実行の説明:**

- before と after の間に WAIT(500)、500ミリ秒の待機があります。difference は負にもなり、中間更新を見落とすことがあります。この待機はサンプルの処理です。

### 最低抵抗を調べる完全な関数

```vb
# 最低抵抗を調べる完全な関数
#
# 現在のプレイヤーの抵抗フィールドを読み取ります：炎。
#
# Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player
# の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1
# は1ポイントであり、成功の意味ではありません。

SUB Main()
    # minimum=50 は例の条件で、上限ではありません。ResistanceAtLeast は Player 不在を拒否し、一度読んで value >= minimum に対して
    # Integer Boolean の 1=TRUE または 0=FALSE を返します。抵抗自体は Boolean ではありません。下に完全な定義があります。

    IF ResistanceAtLeast(50) = TRUE THEN
        UO.Print('Local resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.ResistFire()
    RETURN value >= minimum
END SUB
```

**パラメーターと実行の説明:**

- minimum=50 は例の条件で、上限ではありません。ResistanceAtLeast は Player 不在を拒否し、一度読んで value >= minimum に対して Integer Boolean の 1=TRUE または 0=FALSE を返します。抵抗自体は Boolean ではありません。下に完全な定義があります。
