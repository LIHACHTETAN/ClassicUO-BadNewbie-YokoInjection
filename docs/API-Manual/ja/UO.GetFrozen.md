# UO.GetFrozen

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

クライアントが現在把握している mobile の麻痺フラグを読み取ります。

## 正確な構文

```text
UO.GetFrozen() -> Integer
UO.GetFrozen(value:Any) -> Integer
```

## パラメーター

- `value` — 省略可能な mobile の serial/ID。整数、16進文字列、self、lasttarget、ほかの標準オブジェクト別名、または AddObject の名前を指定します。graphic/type ではありません。省略時は self。解決できない別名は 0 になり、ターゲットカーソルは開きません。

## 戻り値

Integer Boolean：読み込み済みの mobile に IsParalyzed がある場合は 1 = TRUE。フラグがない、mobile が不明または削除済み、あるいはアイテムの場合は 0 = FALSE。残り時間ではなく、0 でも移動できるとは限りません。

## 動作

- Paralyzed は麻痺フラグを確認します。Is/Get の各別名、GetParalisa、Frozen、GetLocked も同じフラグを読み取ります。
- ローカルデータの照会です。麻痺を与えたり治したりせず、終了を待つことも、サーバーに更新を要求することもありません。
- この判定では value = TRUE、value = 1、IF value は同じ意味です。TRUE/FALSE に引用符は付けません。戻り値はフラグであり、個数や ID ではありません。

## 使用例

### TRUE で自分を確認する

```vb
# TRUE で自分を確認する
#
# クライアントが現在把握している mobile の麻痺フラグを読み取ります。
#
# Integer Boolean：読み込み済みの mobile に IsParalyzed がある場合は 1 = TRUE。フラグがない、mobile
# が不明または削除済み、あるいはアイテムの場合は 0 = FALSE。残り時間ではなく、0 でも移動できるとは限りません。

SUB Main()
    # 空の括弧は self を選びます。state は一回分のフラグを保存し、TRUE は数値定数 1 です。
    # FALSE でも、壁、スタミナ不足など別の移動阻害要因はあり得ます。

    VAR state = UO.GetFrozen()
    IF state = TRUE THEN
        UO.Print('Paralysis flag is set')
    ELSE
        UO.Print('Paralysis flag is absent or unavailable')
    END IF
END SUB
```

**パラメーターと実行の説明:**

- 空の括弧は self を選びます。state は一回分のフラグを保存し、TRUE は数値定数 1 です。
- FALSE でも、壁、スタミナ不足など別の移動阻害要因はあり得ます。

### 選択した mobile を確認する

```vb
# 選択した mobile を確認する
#
# クライアントが現在把握している mobile の麻痺フラグを読み取ります。
#
# Integer Boolean：読み込み済みの mobile に IsParalyzed がある場合は 1 = TRUE。フラグがない、mobile
# が不明または削除済み、あるいはアイテムの場合は 0 = FALSE。残り時間ではなく、0 でも移動できるとは限りません。

SUB Main()
    # target は最後のターゲットの serial を16進文字列で保存します。IsNpc はプレイヤーを含む読み込み済みの mobile を確認します。
    # 引数は保存済みの target を指定します。カーソルを開かず、lasttarget も変更しません。

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR state = UO.GetFrozen(target)
        UO.Print('Selected mobile paralysis 1/0: ' + STR(state))
    ELSE
        UO.Print('No loaded mobile selected')
    END IF
END SUB
```

**パラメーターと実行の説明:**

- target は最後のターゲットの serial を16進文字列で保存します。IsNpc はプレイヤーを含む読み込み済みの mobile を確認します。
- 引数は保存済みの target を指定します。カーソルを開かず、lasttarget も変更しません。

### 上限を設けて麻痺解除を待つ

```vb
# 上限を設けて麻痺解除を待つ
#
# クライアントが現在把握している mobile の麻痺フラグを読み取ります。
#
# Integer Boolean：読み込み済みの mobile に IsParalyzed がある場合は 1 = TRUE。フラグがない、mobile
# が不明または削除済み、あるいはアイテムの場合は 0 = FALSE。残り時間ではなく、0 でも移動できるとは限りません。

SUB Main()
    # 100 ミリ秒の待機を最大10回行います。引数なしの呼び出しごとに self を読み直します。
    # ループ後には self の存在を別に確認します。約1秒と実行時間の観察であり、回復を保証するものではありません。

    VAR attempts = 0
    WHILE UO.GetFrozen() = TRUE AND attempts < 10
        WAIT(100)
        attempts = attempts + 1
    WEND
    IF UO.IsNpc('self') THEN
        IF UO.GetFrozen() = FALSE THEN
            UO.Print('Paralysis flag is clear')
        ELSE
            UO.Print('Still paralyzed')
        END IF
    ELSE
        UO.Print('Self is unavailable')
    END IF
END SUB
```

**パラメーターと実行の説明:**

- 100 ミリ秒の待機を最大10回行います。引数なしの呼び出しごとに self を読み直します。
- ループ後には self の存在を別に確認します。約1秒と実行時間の観察であり、回復を保証するものではありません。
