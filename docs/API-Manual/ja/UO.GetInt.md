# UO.GetInt

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

現在の知力（Intelligence、INT）を読みます。

## 正確な構文

```text
UO.GetInt() -> Integer
UO.GetInt(ObjID:Any) -> Integer
```

## パラメーター

- `ObjID` — ObjID は表示された一引数形式のみ：キャラクター serial の整数、十進／0x 十六進文字列、"self"、"lasttarget" または AddObject 名。graphic/type ではなく対象を選びます。省略時は現在のプレイヤーです。

## 戻り値

Integer：モデルに保存された現在の能力値、0..65535。百分率、ID、スキル値、ロック設定、Boolean ではありません。0 はプレイヤー不在／破棄済みや対象データなしも表します。= TRUE ではなく数値条件と比較します。上限値や補正前の基本値とは限りません。

## 動作

- () は self、(ObjID) は明示した対象です。それ以外の省略可能な引数はありません。
- Player が存在し未破棄の場合だけ Player.Intelligence を読み、それ以外は 0 です。存在する死亡キャラクターは破棄済みオブジェクトではありません。HP、マナ、スタミナから計算しません。
- GetStr/GetInt/GetDex は ObjID を受け取りますが、能力値は PlayerMobile にしか保存されません。他の serial は読み込み済み mobile でも 0 です。Stealth の一般説明に対する制約で、他者の値を捏造しません。
- Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。
- 呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。
- UO. の有無を問わず同等で、大文字小文字を区別しない名前： `Int Intelligence GetInt GetIntelligence`.
- UO. なしの Int(value) は BASIC 数を切り下げ、Str(value) は文字列に整形します。能力値を読む UO.Int()/UO.Str() とは別の操作です。GetInt(ObjID) は丸め処理ではありません。
- ExecuteStealthCompatibility.Arg は数値変換の前にオブジェクト名を解決します。未知の非数値文字列は変換エラーになり、ターゲットは開きません。Decimal は Integer、Array/Unit は 0 に変換されます。有効な serial を使用してください。

### 内部関数：呼び出しから結果まで

ネイティブ側の読み取り段階です。AttributeAtLeast は下に完全定義されたユーザー BASIC 関数で、隠れた API や能力値変更ではありません。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases は不足する引数なし関数と組み込み名を登録します。既存の互換分岐は対応 getter を選択し、どちらも Integer を返します。組み込み名は変数で隠されない限り再読されます。

UO. の有無を問わず同等で、大文字小文字を区別しない名前： `Int Intelligence GetInt GetIntelligence`.

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `RegisterCharacterGetterAliases`.

#### 2. ExecuteStealthCompatibility

ObjID は表示された一引数形式のみ：キャラクター serial の整数、十進／0x 十六進文字列、"self"、"lasttarget" または AddObject 名。graphic/type ではなく対象を選びます。省略時は現在のプレイヤーです。

ExecuteStealthCompatibility.Arg は数値変換の前にオブジェクト名を解決します。未知の非数値文字列は変換エラーになり、ターゲットは開きません。Decimal は Integer、Array/Unit は 0 に変換されます。有効な serial を使用してください。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ExecuteStealthCompatibility`.

#### 3. GetIntelligence

GetStr/GetInt/GetDex は ObjID を受け取りますが、能力値は PlayerMobile にしか保存されません。他の serial は読み込み済み mobile でも 0 です。Stealth の一般説明に対する制約で、他者の値を捏造しません。

Player が存在し未破棄の場合だけ Player.Intelligence を読み、それ以外は 0 です。存在する死亡キャラクターは破棄済みオブジェクトではありません。HP、マナ、スタミナから計算しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `GetIntelligence`.

#### 4. Invoke

Player が存在し未破棄の場合だけ Player.Intelligence を読み、それ以外は 0 です。存在する死亡キャラクターは破棄済みオブジェクトではありません。HP、マナ、スタミナから計算しません。 Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。

Integer：モデルに保存された現在の能力値、0..65535。百分率、ID、スキル値、ロック設定、Boolean ではありません。0 はプレイヤー不在／破棄済みや対象データなしも表します。= TRUE ではなく数値条件と比較します。上限値や補正前の基本値とは限りません。 呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 5. CharacterStatus

CharacterStatus は該当する自分の status パケットを処理し、受信した STR/DEX/INT を Player.Intelligence に代入します。クエリはこのキャッシュを読み、新しいパケットを待ちません。

Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。

プロジェクトのソース: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 関数 `CharacterStatus`.

#### 6. Clear

World.Clear は Player を除去します。プレイヤーとデータが戻るまでは 0。再接続後の条件達成を保存済みの値だけで判断しません。

Integer：モデルに保存された現在の能力値、0..65535。百分率、ID、スキル値、ロック設定、Boolean ではありません。0 はプレイヤー不在／破棄済みや対象データなしも表します。= TRUE ではなく数値条件と比較します。上限値や補正前の基本値とは限りません。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Clear`.

World.Clear は Player を除去します。プレイヤーとデータが戻るまでは 0。再接続後の条件達成を保存済みの値だけで判断しません。


## 使用例

### ポイントを表示する

```vb
# ポイントを表示する
#
# 現在の知力（Intelligence、INT）を読みます。
#
# Integer：モデルに保存された現在の能力値、0..65535。百分率、ID、スキル値、ロック設定、Boolean ではありません。0
# はプレイヤー不在／破棄済みや対象データなしも表します。= TRUE ではなく数値条件と比較します。上限値や補正前の基本値とは限りません。

SUB Main()
    # value が数値を保存し、CStr は日誌用に整形するだけです。引数やキャラクター動作はありません。

    VAR value = UO.GetInt()
    UO.Print('Intelligence: ' + CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value が数値を保存し、CStr は日誌用に整形するだけです。引数やキャラクター動作はありません。

### 二つの観測を比較する

```vb
# 二つの観測を比較する
#
# 現在の知力（Intelligence、INT）を読みます。
#
# Integer：モデルに保存された現在の能力値、0..65535。百分率、ID、スキル値、ロック設定、Boolean ではありません。0
# はプレイヤー不在／破棄済みや対象データなしも表します。= TRUE ではなく数値条件と比較します。上限値や補正前の基本値とは限りません。

SUB Main()
    # before/after の間は 1000 ミリ秒で、WAIT は例の一部です。change=after-before は正、零、負になり、中間更新や切断を単独では区別できません。

    VAR before = UO.GetInt()
    WAIT(1000)
    VAR after = UO.GetInt()
    VAR change = after - before
    UO.Print('Change: ' + CStr(change))
END SUB
```

**パラメーターと実行の説明:**

- before/after の間は 1000 ミリ秒で、WAIT は例の一部です。change=after-before は正、零、負になり、中間更新や切断を単独では区別できません。

### 条件確認関数の完全例

```vb
# 条件確認関数の完全例
#
# 現在の知力（Intelligence、INT）を読みます。
#
# Integer：モデルに保存された現在の能力値、0..65535。百分率、ID、スキル値、ロック設定、Boolean ではありません。0
# はプレイヤー不在／破棄済みや対象データなしも表します。= TRUE ではなく数値条件と比較します。上限値や補正前の基本値とは限りません。

SUB Main()
    # minimum=80 は条件例で上限ではありません。AttributeAtLeast(minimum) はプレイヤー不在を除外し、一度読み、>= minimum によって Integer
    # Boolean 1=TRUE または 0=FALSE を返します。論理値になるのは比較で、能力値自体ではありません。

    IF AttributeAtLeast(80) = TRUE THEN
        UO.Print('Requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB AttributeAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetInt()
    RETURN value >= minimum
END SUB
```

**パラメーターと実行の説明:**

- minimum=80 は条件例で上限ではありません。AttributeAtLeast(minimum) はプレイヤー不在を除外し、一度読み、>= minimum によって Integer Boolean 1=TRUE または 0=FALSE を返します。論理値になるのは比較で、能力値自体ではありません。

### serial と名前でプレイヤーを選ぶ

```vb
# serial と名前でプレイヤーを選ぶ
#
# 現在の知力（Intelligence、INT）を読みます。
#
# Integer：モデルに保存された現在の能力値、0..65535。百分率、ID、スキル値、ロック設定、Boolean ではありません。0
# はプレイヤー不在／破棄済みや対象データなしも表します。= TRUE ではなく数値条件と比較します。上限値や補正前の基本値とは限りません。

SUB Main()
    # id は UO.Self() の serial で type ではありません。AddObject は第二引数があるためターゲットなしで statSubject
    # に保存します。両呼び出しは同じ対象を選びますが、読み取りはアトミックではありません。

    VAR id = UO.Self()
    IF id <> 0 THEN
        UO.AddObject('statSubject', id)
        VAR direct = UO.GetInt(id)
        VAR byName = UO.GetInt('statSubject')
        UO.Print('Direct: ' + CStr(direct) + '; alias: ' + CStr(byName))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- id は UO.Self() の serial で type ではありません。AddObject は第二引数があるためターゲットなしで statSubject に保存します。両呼び出しは同じ対象を選びますが、読み取りはアトミックではありません。
