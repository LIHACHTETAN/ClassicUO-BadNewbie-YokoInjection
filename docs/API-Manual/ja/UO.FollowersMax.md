# UO.FollowersMax

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

現在のプレイヤーのステータス値を読み取ります：ペット制御スロット上限。

## 正確な構文

```text
UO.FollowersMax() -> Integer
```

## パラメーター

引数はありません。

## 戻り値

Integer — ペット制御スロット上限、モデルの範囲は 0..255。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり Boolean、ID、type ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

## 動作

- 引数はありません。表示された正確なシグネチャを使用します。
- ゲームスレッドで Player.FollowersMax を読みます。現在の Player が存在しないか破棄済みなら 0。装備の検索、ボーナス計算、ステータス要求、更新待ちは行いません。存在する幽霊と破棄済み Player は別です。
- PetsMax/FollowersMax は status type >= 3 のサーバーが許可した総スロット上限を読みます。空きスロット数ではありません。使用量が上限を超える場合もあります。空き表示は maximum - current を求め、負なら 0 にします。解放、調教、召喚は行いません。
- CharacterStatus は固定部分を検証してから更新します。Weight は自身の拡張ステータス、スロットは type 3、Luck は type 4、サーバー WeightMax は type 5 以降です。省略欄のない簡易／旧式パケットでは以前の値を維持します。新規 Player はゼロから始まり、呼び出しは最新受信の証明になりません。
- RegisterCharacterGetterAliases は不足する引数なし関数と組み込み名を登録します。既存の互換分岐も同じ欄を読みます。名前の大小文字は不問で、括弧なしの組み込み名は変数で隠されなければ毎回読み取ります。
- 呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。

### 内部関数：呼び出しから結果まで

ステータスキャッシュを読むネイティブ処理です。例の CanCarry、LuckAtLeast、CanAddFollower は完全に定義されたユーザー BASIC 関数で、隠れたネイティブ操作ではありません。持ち物やペットを変更しません。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases は不足する引数なし関数と組み込み名を登録します。既存の互換分岐も同じ欄を読みます。名前の大小文字は不問で、括弧なしの組み込み名は変数で隠されなければ毎回読み取ります。

`PetsMax FollowersMax GetPetsMax GetFollowersMax`.

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `RegisterCharacterGetterAliases`.

#### 2. Invoke

ゲームスレッドで Player.FollowersMax を読みます。現在の Player が存在しないか破棄済みなら 0。装備の検索、ボーナス計算、ステータス要求、更新待ちは行いません。存在する幽霊と破棄済み Player は別です。

Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 3. CharacterStatus

CharacterStatus は固定部分を検証してから更新します。Weight は自身の拡張ステータス、スロットは type 3、Luck は type 4、サーバー WeightMax は type 5 以降です。省略欄のない簡易／旧式パケットでは以前の値を維持します。新規 Player はゼロから始まり、呼び出しは最新受信の証明になりません。

PetsMax/FollowersMax は status type >= 3 のサーバーが許可した総スロット上限を読みます。空きスロット数ではありません。使用量が上限を超える場合もあります。空き表示は maximum - current を求め、負なら 0 にします。解放、調教、召喚は行いません。

プロジェクトのソース: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 関数 `CharacterStatus`.

#### 4. Clear

World.Clear は Player を除去します。プレイヤーとデータが戻るまでは 0。再接続後の条件達成を保存済みの値だけで判断しません。

Integer — ペット制御スロット上限、モデルの範囲は 0..255。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり Boolean、ID、type ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Clear`.

呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。


## 使用例

### 保存された値を表示

```vb
# 保存された値を表示
#
# 現在のプレイヤーのステータス値を読み取ります：ペット制御スロット上限。
#
# Integer — ペット制御スロット上限、モデルの範囲は 0..255。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり Boolean、ID、type
# ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

SUB Main()
    # value は引数なしの自分の値を一度保存します。CStr は意味を変えずにジャーナル表示用へ変換します。

    VAR value = UO.FollowersMax()
    UO.Print('FollowersMax: ' + CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value は引数なしの自分の値を一度保存します。CStr は意味を変えずにジャーナル表示用へ変換します。

### 変化を観察

```vb
# 変化を観察
#
# 現在のプレイヤーのステータス値を読み取ります：ペット制御スロット上限。
#
# Integer — ペット制御スロット上限、モデルの範囲は 0..255。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり Boolean、ID、type
# ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

SUB Main()
    # WAIT(500) は before と after を500ミリ秒隔てます。difference
    # は正、ゼロ、負になり、中間更新やキャラクター変更を見落とす場合があります。待機は例の処理です。

    VAR before = UO.FollowersMax()
    WAIT(500)
    VAR after = UO.FollowersMax()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**パラメーターと実行の説明:**

- WAIT(500) は before と after を500ミリ秒隔てます。difference は正、ゼロ、負になり、中間更新やキャラクター変更を見落とす場合があります。待機は例の処理です。

### 完全な判定関数

```vb
# 完全な判定関数
#
# 現在のプレイヤーのステータス値を読み取ります：ペット制御スロット上限。
#
# Integer — ペット制御スロット上限、モデルの範囲は 0..255。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり Boolean、ID、type
# ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

SUB Main()
    # CanAddFollower(extraSlots) は必要制御スロットを受け取ります。2 は2スロット使う1体の例にもなり、必ずしも2体ではありません。負値、Player
    # 不在、maximum <= 0 を拒否し、使用量／上限を読んで extraSlots <= maximum - current に対して Integer Boolean の 1=TRUE
    # または 0=FALSE を返します。加算オーバーフローはなく、上限超過ならゼロでも false。所有者、調教スキル、サーバー許可は確認しません。読み取り間に更新される場合があります。

    IF CanAddFollower(2) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanAddFollower(extraSlots)
    IF extraSlots < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.PetsCurrent()
    VAR maximum = UO.FollowersMax()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extraSlots <= maximum - current
END SUB
```

**パラメーターと実行の説明:**

- CanAddFollower(extraSlots) は必要制御スロットを受け取ります。2 は2スロット使う1体の例にもなり、必ずしも2体ではありません。負値、Player 不在、maximum <= 0 を拒否し、使用量／上限を読んで extraSlots <= maximum - current に対して Integer Boolean の 1=TRUE または 0=FALSE を返します。加算オーバーフローはなく、上限超過ならゼロでも false。所有者、調教スキル、サーバー許可は確認しません。読み取り間に更新される場合があります。
