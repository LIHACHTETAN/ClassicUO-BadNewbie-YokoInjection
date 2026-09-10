# UO.MaxWeight

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

現在のプレイヤーのステータス値を読み取ります：最大重量（stones）。

## 正確な構文

```text
UO.MaxWeight() -> Integer
```

## パラメーター

引数はありません。

## 戻り値

Integer — 最大重量（stones）、モデルの範囲は 0..65535。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり Boolean、ID、type ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

## 動作

- 引数はありません。表示された正確なシグネチャを使用します。
- ゲームスレッドで Player.WeightMax を読みます。現在の Player が存在しないか破棄済みなら 0。装備の検索、ボーナス計算、ステータス要求、更新待ちは行いません。存在する幽霊と破棄済み Player は別です。
- MaxWeight はキャッシュ WeightMax を読みます。自身の status type >= 5 はサーバーの UInt16 上限を使い、0 もそのままです。古い拡張ステータスでは受信時に一度計算します。UO プロトコル >= 5.0.0a は 7 * floor(STR / 2) + 40、それより前は STR * 4 + 25。UInt16 保存のため極端な値は 65536 を法として折り返します。STR=101 はそれぞれ 390、429。STR の別更新時に getter は再計算しません。
- CharacterStatus は固定部分を検証してから更新します。Weight は自身の拡張ステータス、スロットは type 3、Luck は type 4、サーバー WeightMax は type 5 以降です。省略欄のない簡易／旧式パケットでは以前の値を維持します。新規 Player はゼロから始まり、呼び出しは最新受信の証明になりません。
- RegisterCharacterGetterAliases は不足する引数なし関数と組み込み名を登録します。既存の互換分岐も同じ欄を読みます。名前の大小文字は不問で、括弧なしの組み込み名は変数で隠されなければ毎回読み取ります。
- 呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。

### 内部関数：呼び出しから結果まで

ステータスキャッシュを読むネイティブ処理です。例の CanCarry、LuckAtLeast、CanAddFollower は完全に定義されたユーザー BASIC 関数で、隠れたネイティブ操作ではありません。持ち物やペットを変更しません。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases は不足する引数なし関数と組み込み名を登録します。既存の互換分岐も同じ欄を読みます。名前の大小文字は不問で、括弧なしの組み込み名は変数で隠されなければ毎回読み取ります。

`MaxWeight GetMaxWeight`.

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `RegisterCharacterGetterAliases`.

#### 2. Invoke

ゲームスレッドで Player.WeightMax を読みます。現在の Player が存在しないか破棄済みなら 0。装備の検索、ボーナス計算、ステータス要求、更新待ちは行いません。存在する幽霊と破棄済み Player は別です。

Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 3. CharacterStatus

CharacterStatus は固定部分を検証してから更新します。Weight は自身の拡張ステータス、スロットは type 3、Luck は type 4、サーバー WeightMax は type 5 以降です。省略欄のない簡易／旧式パケットでは以前の値を維持します。新規 Player はゼロから始まり、呼び出しは最新受信の証明になりません。

MaxWeight はキャッシュ WeightMax を読みます。自身の status type >= 5 はサーバーの UInt16 上限を使い、0 もそのままです。古い拡張ステータスでは受信時に一度計算します。UO プロトコル >= 5.0.0a は 7 * floor(STR / 2) + 40、それより前は STR * 4 + 25。UInt16 保存のため極端な値は 65536 を法として折り返します。STR=101 はそれぞれ 390、429。STR の別更新時に getter は再計算しません。

プロジェクトのソース: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 関数 `CharacterStatus`.

#### 4. Clear

World.Clear は Player を除去します。プレイヤーとデータが戻るまでは 0。再接続後の条件達成を保存済みの値だけで判断しません。

Integer — 最大重量（stones）、モデルの範囲は 0..65535。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり Boolean、ID、type ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Clear`.

呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。


## 使用例

### 保存された値を表示

```vb
# 保存された値を表示
#
# 現在のプレイヤーのステータス値を読み取ります：最大重量（stones）。
#
# Integer — 最大重量（stones）、モデルの範囲は 0..65535。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり
# Boolean、ID、type ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

SUB Main()
    # value は引数なしの自分の値を一度保存します。CStr は意味を変えずにジャーナル表示用へ変換します。

    VAR value = UO.MaxWeight()
    UO.Print('WeightMax: ' + CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value は引数なしの自分の値を一度保存します。CStr は意味を変えずにジャーナル表示用へ変換します。

### 変化を観察

```vb
# 変化を観察
#
# 現在のプレイヤーのステータス値を読み取ります：最大重量（stones）。
#
# Integer — 最大重量（stones）、モデルの範囲は 0..65535。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり
# Boolean、ID、type ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

SUB Main()
    # WAIT(500) は before と after を500ミリ秒隔てます。difference
    # は正、ゼロ、負になり、中間更新やキャラクター変更を見落とす場合があります。待機は例の処理です。

    VAR before = UO.MaxWeight()
    WAIT(500)
    VAR after = UO.MaxWeight()
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
# 現在のプレイヤーのステータス値を読み取ります：最大重量（stones）。
#
# Integer — 最大重量（stones）、モデルの範囲は 0..65535。0 は実値、未取得データ、Player 不在／破棄の可能性があります。数量であり
# Boolean、ID、type ではありません。1 は1単位で、成功の意味ではありません。物体を列挙せず、配列も返しません。

SUB Main()
    # CanCarry(extra) は追加重量を stones で受け取ります。10 は例で、スタック数ではありません。負の extra、Player 不在、maximum <= 0
    # を拒否し、現在値と最大値を読んで extra <= maximum - current に対し Integer Boolean の 1=TRUE または 0=FALSE を返します。減算は
    # current + extra のオーバーフローを避けます。過積載では extra=0 も
    # false。ローカル見積りでサーバーの許可ではありません。読み取りは原子的でなく、重量ゼロは未取得の場合もあります。

    IF CanCarry(10) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanCarry(extra)
    IF extra < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.Weight()
    VAR maximum = UO.MaxWeight()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extra <= maximum - current
END SUB
```

**パラメーターと実行の説明:**

- CanCarry(extra) は追加重量を stones で受け取ります。10 は例で、スタック数ではありません。負の extra、Player 不在、maximum <= 0 を拒否し、現在値と最大値を読んで extra <= maximum - current に対し Integer Boolean の 1=TRUE または 0=FALSE を返します。減算は current + extra のオーバーフローを避けます。過積載では extra=0 も false。ローカル見積りでサーバーの許可ではありません。読み取りは原子的でなく、重量ゼロは未取得の場合もあります。
