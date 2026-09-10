# UO.GetGold

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

現在のプレイヤーの status に報告された金額を読みます。

## 正確な構文

```text
UO.GetGold() -> Any
```

## パラメーター

引数はありません。

## 戻り値

Integer/Decimal：0..4294967295 の非負金額です。2147483647 までは Integer、それ以上は全 UInt32 整数を正確に表せる Decimal（Double）です。0 は Player 不在／破棄済みや金額未取得も表します。Boolean、ID、スタック数、バッグ／銀行の探索結果ではありません。

## 動作

- 引数なし。CharacterStatus（0x11）が保存した Player.Gold を読みます。含まれる金の範囲はサーバーが決定します。バッグ巡回や銀行残高要求は行いません。Player 不在／破棄済みは 0、存在する幽霊には金額が残る場合があります。
- ReadGoldValue は bridge.Gold を一度読みます。C# bridge は Int32 のまま UInt32 のビットを運びます。unchecked で符号なし金額を復元し、小さい値は Integer、大きい値は Decimal にします。最上位ビットによって残高が負になることはありません。ローカル変換で送信はありません。
- 大きな金額は数値結果のまま比較します。CInt/CLng は 32 ビット Integer への変換です。大きな BASIC リテラルは 3000000000.0 のように小数点付きで書きます。購入前に残高は変化し得ます。CanAfford はローカル確認で、サーバーの承認ではありません。
- 呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。

### 内部関数：呼び出しから結果まで

status カウンターの読み取りと符号なし範囲拡張のネイティブ段階です。CanAfford は下に完全定義されたユーザー BASIC 関数で、隠れた購入命令ではありません。

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases は不足する Gold/GetGold 関数と組み込み名を追加します。UO.Gold 互換分岐と組み込み値も同じ ReadGoldValue を使用します。変数に隠されない組み込み名は毎回再読されます。

Integer/Decimal：0..4294967295 の非負金額です。2147483647 までは Integer、それ以上は全 UInt32 整数を正確に表せる Decimal（Double）です。0 は Player 不在／破棄済みや金額未取得も表します。Boolean、ID、スタック数、バッグ／銀行の探索結果ではありません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `RegisterCharacterGetterAliases`.

#### 2. ReadGoldValue

ReadGoldValue は bridge.Gold を一度読みます。C# bridge は Int32 のまま UInt32 のビットを運びます。unchecked で符号なし金額を復元し、小さい値は Integer、大きい値は Decimal にします。最上位ビットによって残高が負になることはありません。ローカル変換で送信はありません。

大きな金額は数値結果のまま比較します。CInt/CLng は 32 ビット Integer への変換です。大きな BASIC リテラルは 3000000000.0 のように小数点付きで書きます。購入前に残高は変化し得ます。CanAfford はローカル確認で、サーバーの承認ではありません。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ReadGoldValue`.

#### 3. Invoke

引数なし。CharacterStatus（0x11）が保存した Player.Gold を読みます。含まれる金の範囲はサーバーが決定します。バッグ巡回や銀行残高要求は行いません。Player 不在／破棄済みは 0、存在する幽霊には金額が残る場合があります。

Invoke はゲームスレッドで読み、待機はスクリプト中止に対応します。status 要求、ターゲット、パケット送信、値の変更、組み込み待機はありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 4. CharacterStatus

引数なし。CharacterStatus（0x11）が保存した Player.Gold を読みます。含まれる金の範囲はサーバーが決定します。バッグ巡回や銀行残高要求は行いません。Player 不在／破棄済みは 0、存在する幽霊には金額が残る場合があります。

呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。

プロジェクトのソース: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 関数 `CharacterStatus`.

#### 5. Clear

World.Clear は Player を除去します。プレイヤーとデータが戻るまでは 0。再接続後の条件達成を保存済みの値だけで判断しません。

Integer/Decimal：0..4294967295 の非負金額です。2147483647 までは Integer、それ以上は全 UInt32 整数を正確に表せる Decimal（Double）です。0 は Player 不在／破棄済みや金額未取得も表します。Boolean、ID、スタック数、バッグ／銀行の探索結果ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Clear`.

呼び出しごとにローカル値を再読します。変数はスナップショットで、別々の呼び出しには異なる更新が見える場合があります。非ゼロは接続確認ではなく、0 は実値とデータなしの両方を表します。


## 使用例

### 報告された金額を表示

```vb
# 報告された金額を表示
#
# 現在のプレイヤーの status に報告された金額を読みます。
#
# Integer/Decimal：0..4294967295 の非負金額です。2147483647 までは Integer、それ以上は全 UInt32 整数を正確に表せる
# Decimal（Double）です。0 は Player 不在／破棄済みや金額未取得も表します。Boolean、ID、スタック数、バッグ／銀行の探索結果ではありません。

SUB Main()
    # amount は一回の結果を保存し、CStr は日誌用に整形します。金の探索、移動、消費はしません。

    VAR amount = UO.GetGold()
    UO.Print('Status gold: ' + CStr(amount))
END SUB
```

**パラメーターと実行の説明:**

- amount は一回の結果を保存し、CStr は日誌用に整形します。金の探索、移動、消費はしません。

### 高額価格を使う完全な CanAfford

```vb
# 高額価格を使う完全な CanAfford
#
# 現在のプレイヤーの status に報告された金額を読みます。
#
# Integer/Decimal：0..4294967295 の非負金額です。2147483647 までは Integer、それ以上は全 UInt32 整数を正確に表せる
# Decimal（Double）です。0 は Player 不在／破棄済みや金額未取得も表します。Boolean、ID、スタック数、バッグ／銀行の探索結果ではありません。

SUB Main()
    # price=3000000000.0 は価格例です。CanAfford(price) は負の価格や Player 不在を除外し、一度読んで amount >= price により
    # Integer Boolean 1=TRUE または 0=FALSE を返します。金額自体は Boolean ではありません。下に完全定義を示します。

    VAR price = 3000000000.0
    IF CanAfford(price) = TRUE THEN
        UO.Print('Local balance is sufficient')
    ELSE
        UO.Print('Local check failed')
    END IF
END SUB

SUB CanAfford(price)
    IF price < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR amount = UO.GetGold()
    RETURN amount >= price
END SUB
```

**パラメーターと実行の説明:**

- price=3000000000.0 は価格例です。CanAfford(price) は負の価格や Player 不在を除外し、一度読んで amount >= price により Integer Boolean 1=TRUE または 0=FALSE を返します。金額自体は Boolean ではありません。下に完全定義を示します。

### 残高の変化を観測

```vb
# 残高の変化を観測
#
# 現在のプレイヤーの status に報告された金額を読みます。
#
# Integer/Decimal：0..4294967295 の非負金額です。2147483647 までは Integer、それ以上は全 UInt32 整数を正確に表せる
# Decimal（Double）です。0 は Player 不在／破棄済みや金額未取得も表します。Boolean、ID、スタック数、バッグ／銀行の探索結果ではありません。

SUB Main()
    # before/after の間に WAIT(500) ミリ秒を置きます。残高が減れば difference=after-before
    # は負になり、修正済みの符号なしオーバーフローとは異なります。途中の更新やキャラクター変更は見逃す場合があります。

    VAR before = UO.GetGold()
    WAIT(500)
    VAR after = UO.GetGold()
    VAR difference = after - before
    UO.Print('Balance change: ' + CStr(difference))
END SUB
```

**パラメーターと実行の説明:**

- before/after の間に WAIT(500) ミリ秒を置きます。残高が減れば difference=after-before は負になり、修正済みの符号なしオーバーフローとは異なります。途中の更新やキャラクター変更は見逃す場合があります。
