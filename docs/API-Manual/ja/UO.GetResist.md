# UO.GetResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

数値または名前で、自分のプレイヤーの抵抗を一つ選んで読み取ります。

## 正確な構文

```text
UO.GetResist(resistance:Any) -> Integer
```

## パラメーター

- `resistance` — resistance は必須。数値は 0=physical、1=fire、2=cold、3=poison、4=energy。文字列は physical/phys/armor、fire、cold、poison、energy。大文字小文字と前後の空白は無視します。serial、type、hue、ターゲット、第2引数はありません。

## 戻り値

Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1 は1ポイントであり、成功の意味ではありません。

## 動作

- まず値の種類を判定します。文字列 "1" と "0" は未知の名前で 0 を返し、数値選択にはなりません。文字列以外の Decimal はゼロ方向に切り捨てます：1.9 -> fire、-0.9 -> physical。TRUE=1 は fire、FALSE=0 は physical、Array/Unit も 0 に変換されます。明示的な整数か有効な名前を使ってください。AddObject 名は解決しません。
- GetResistance は bridge の getter を一つだけ選びます。未知の数値／名前は読み取りなしで Integer 0。五つの値を原子的に取得する機能でも、抵抗を変更する機能でもありません。
- PhysicalResistance はサーバーの防御／ステータス欄です。従来のルールでは防御値、抵抗のルールでは物理抵抗が使われます。ルール間の変換やダメージ軽減率の計算はしません。Armor と物理抵抗の別名は同じ欄を読みます。
- 属性抵抗は CharacterStatus（0x11）の type >= 4 で届きます。呼び出し自体はサーバーの時代を判定しません。欄のない簡易／旧式ステータスでは以前のキャッシュを維持し、新規 Player は 0 から始まります。毒抵抗は Poisoned フラグではなく、各抵抗は Resisting Spells スキルでもありません。
- CharacterStatus は固定部分を検証してから状態を変更し、抵抗の word を符号付き Int16 に変換します。固定部分の欠落時は以前の状態を維持します。type 6 の省略可能な末尾は従来の処理を維持します。ここではその抵抗上限を読みません。
- Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。
- 呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。

### 内部関数：呼び出しから結果まで

ローカル読み取りの実際のネイティブ処理です。下の ResistanceAtLeast は完全に定義したユーザー BASIC 関数で、隠し API や防具の装備命令ではありません。

#### 1. RegisterCharacterGetterAliases

GetResist(resistance) と UO.GetResist(resistance) を GetResistance に対応する1引数関数として登録します。この選択に引数なしの組み込み値はありません。

resistance は必須。数値は 0=physical、1=fire、2=cold、3=poison、4=energy。文字列は physical/phys/armor、fire、cold、poison、energy。大文字小文字と前後の空白は無視します。serial、type、hue、ターゲット、第2引数はありません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `RegisterCharacterGetterAliases`.

#### 2. GetResistance

まず値の種類を判定します。文字列 "1" と "0" は未知の名前で 0 を返し、数値選択にはなりません。文字列以外の Decimal はゼロ方向に切り捨てます：1.9 -> fire、-0.9 -> physical。TRUE=1 は fire、FALSE=0 は physical、Array/Unit も 0 に変換されます。明示的な整数か有効な名前を使ってください。AddObject 名は解決しません。

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`. GetResistance は bridge の getter を一つだけ選びます。未知の数値／名前は読み取りなしで Integer 0。五つの値を原子的に取得する機能でも、抵抗を変更する機能でもありません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `GetResistance`.

#### 3. ToInt

ここで ToInt が受け取るのは文字列以外の選択値です。Integer はそのまま、Decimal はゼロ方向に切り捨て、Array/Unit は 0。結果は選択番号であり抵抗ではありません。文字列名は GetResistance が処理します。

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`.

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/NumberConversions.cs`; 関数 `ToInt`.

#### 4. Invoke

Invoke は上の対応表で選んだ Player フィールドを符号を保って読みます。Player 不在／破棄時は 0。ステータス要求や新しいデータの待機はしません。

Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 5. CharacterStatus

CharacterStatus は固定部分を検証してから状態を変更し、抵抗の word を符号付き Int16 に変換します。固定部分の欠落時は以前の状態を維持します。type 6 の省略可能な末尾は従来の処理を維持します。ここではその抵抗上限を読みません。

PhysicalResistance はサーバーの防御／ステータス欄です。従来のルールでは防御値、抵抗のルールでは物理抵抗が使われます。ルール間の変換やダメージ軽減率の計算はしません。Armor と物理抵抗の別名は同じ欄を読みます。 属性抵抗は CharacterStatus（0x11）の type >= 4 で届きます。呼び出し自体はサーバーの時代を判定しません。欄のない簡易／旧式ステータスでは以前のキャッシュを維持し、新規 Player は 0 から始まります。毒抵抗は Poisoned フラグではなく、各抵抗は Resisting Spells スキルでもありません。

プロジェクトのソース: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 関数 `CharacterStatus`.

#### 6. Clear

World.Clear は Player を除去します。プレイヤーとデータが戻るまでは 0。再接続後の条件達成を保存済みの値だけで判断しません。

Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1 は1ポイントであり、成功の意味ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Clear`.

呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。


## 使用例

### 大小文字を混ぜた名前で選択

```vb
# 大小文字を混ぜた名前で選択
#
# 数値または名前で、自分のプレイヤーの抵抗を一つ選んで読み取ります。
#
# Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player
# の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1
# は1ポイントであり、成功の意味ではありません。

SUB Main()
    # resistance=" FiRe " は前後の空白と大小文字を無視して炎を選びます。value は符号付き数値のままです。ターゲットは開きません。

    VAR value = UO.GetResist(' FiRe ')
    UO.Print('Fire resistance: ' + CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- resistance=" FiRe " は前後の空白と大小文字を無視して炎を選びます。value は符号付き数値のままです。ターゲットは開きません。

### 数値と文字列の選択を比較

```vb
# 数値と文字列の選択を比較
#
# 数値または名前で、自分のプレイヤーの抵抗を一つ選んで読み取ります。
#
# Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player
# の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1
# は1ポイントであり、成功の意味ではありません。

SUB Main()
    # 2 は冷気、"poison" は毒を選び、serial ではありません。二つのスナップショットの比較は Boolean を返します。毒抵抗は中毒の有無を示しません。

    VAR cold = UO.GetResist(2)
    VAR poison = UO.GetResist('poison')
    IF cold < poison THEN
        UO.Print('Cold resistance is lower')
    ELSE
        UO.Print('Cold resistance is equal or higher')
    END IF
END SUB
```

**パラメーターと実行の説明:**

- 2 は冷気、"poison" は毒を選び、serial ではありません。二つのスナップショットの比較は Boolean を返します。毒抵抗は中毒の有無を示しません。

### 最低抵抗を調べる完全な関数

```vb
# 最低抵抗を調べる完全な関数
#
# 数値または名前で、自分のプレイヤーの抵抗を一つ選んで読み取ります。
#
# Integer — クライアントモデルの符号付きステータス値、-32768..32767。負値を維持します。0 は実際の抵抗、未取得の値、Player
# の不在／破棄を表すことがあります。GetResist は未知の選択値でも 0 を返します。Boolean、ID、スキル、上限ではありません。1
# は1ポイントであり、成功の意味ではありません。

SUB Main()
    # minimum=50 は例の条件で、上限ではありません。ResistanceAtLeast は Player 不在を拒否し、一度読んで value >= minimum に対して
    # Integer Boolean の 1=TRUE または 0=FALSE を返します。抵抗自体は Boolean ではありません。下に完全な定義があります。
    # selector はそのまま GetResist に渡します。この例は "fire" です。Player
    # の存在は検査しますが、任意の選択値やデータの新しさは検証しません。上記の選択値を使ってください。

    IF ResistanceAtLeast('fire', 50) = TRUE THEN
        UO.Print('Local fire resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(selector, minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetResist(selector)
    RETURN value >= minimum
END SUB
```

**パラメーターと実行の説明:**

- minimum=50 は例の条件で、上限ではありません。ResistanceAtLeast は Player 不在を拒否し、一度読んで value >= minimum に対して Integer Boolean の 1=TRUE または 0=FALSE を返します。抵抗自体は Boolean ではありません。下に完全な定義があります。
- selector はそのまま GetResist に渡します。この例は "fire" です。Player の存在は検査しますが、任意の選択値やデータの新しさは検証しません。上記の選択値を使ってください。
