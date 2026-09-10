# UO.Random

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

擬似乱数の整数を一つ選びます。Random(min,max) は両端を含み、従来の Random(max) は上限を含みません。

## 正確な構文

```text
UO.Random(max:Integer) -> Integer
UO.Random(min:Integer, max:Integer) -> Integer
```

## パラメーター

- `min` — 下限。引数が二つの場合だけ使います。-2147483648 から 2147483647 までの符号付き 32 ビット整数で、max 以下にします。
- `max` — 引数が二つ：結果に含まれる上限。任意の Integer を指定できます。引数が一つ：含まれない上限で、0..2147483647。Random(0) は 0 を返します。

## 戻り値

Integer — 選ばれた数値一つです。真偽値や serial ではありません。二引数：min <= 結果 <= max。一つの正の引数：0 <= 結果 < max。同じ値が続く場合もあります。

## 動作

- 引数なしの形式はありません。両端が等しければその値を返します。上下限の逆転や単一の負の引数はスクリプトエラーです。自動的に入れ替えません。
- max+1 のオーバーフローを起こさず、符号付き 32 ビットの全範囲に対応します。離散的な小数には整数を選んで割ります。例：Random(0,100)/100.0。
- 生成器はスクリプトの runtime に属し、同時呼び出しは同期されます。seed 引数はなく、BASIC Rnd とは別の関数です。同じ結果を再使用する場合は変数に保存します。
- ローカルで計算するだけで、待機、移動、パケット送信はしません。ランダムな座標の通行可否は別途確認します。Random(0)=0 でも空の配列に有効な添字はありません。

## 使用例

### サイコロを振る

```vb
# サイコロを振る
#
# 擬似乱数の整数を一つ選びます。Random(min,max) は両端を含み、従来の Random(max) は上限を含みません。
#
# Integer — 選ばれた数値一つです。真偽値や serial ではありません。二引数：min <= 結果 <= max。一つの正の引数：0 <= 結果 <
# max。同じ値が続く場合もあります。

SUB Main()
    # min=1、max=6 では六つの値をすべて含みます。roll は一回の結果を保存し、STR は文字列に変換します。次の呼び出しで同じ値が出る場合もあります。

    VAR roll = UO.Random(1, 6)
    UO.Print(STR(roll))
END SUB
```

**パラメーターと実行の説明:**

- min=1、max=6 では六つの値をすべて含みます。roll は一回の結果を保存し、STR は文字列に変換します。次の呼び出しで同じ値が出る場合もあります。

### ランダムな時間待つ

```vb
# ランダムな時間待つ
#
# 擬似乱数の整数を一つ選びます。Random(min,max) は両端を含み、従来の Random(max) は上限を含みません。
#
# Integer — 選ばれた数値一つです。真偽値や serial ではありません。二引数：min <= 結果 <= max。一つの正の引数：0 <= 結果 <
# max。同じ値が続く場合もあります。

SUB Main()
    # min=350、max=700 は両端を含むミリ秒です。Random が delay を計算し、UO.Wait(delay) が待機します。サーバーに必要な最短待機時間は確保してください。

    VAR delay = UO.Random(350, 700)
    UO.Print(STR(delay))
    UO.Wait(delay)
END SUB
```

**パラメーターと実行の説明:**

- min=350、max=700 は両端を含むミリ秒です。Random が delay を計算し、UO.Wait(delay) が待機します。サーバーに必要な最短待機時間は確保してください。

### 従来の添字と等しい上下限

```vb
# 従来の添字と等しい上下限
#
# 擬似乱数の整数を一つ選びます。Random(min,max) は両端を含み、従来の Random(max) は上限を含みません。
#
# Integer — 選ばれた数値一つです。真偽値や serial ではありません。二引数：min <= 結果 <= max。一つの正の引数：0 <= 結果 <
# max。同じ値が続く場合もあります。

SUB Main()
    # Random(10) は 0..9 で、10 は出ません。Random(7,7) は必ず 7。Random(-2,2) は -2,-1,0,1,2 のいずれかです。各式は独立した選択です。

    VAR index = UO.Random(10)
    VAR fixedValue = UO.Random(7, 7)
    VAR offset = UO.Random(-2, 2)
    UO.Print(STR(index) + ', ' + STR(fixedValue) + ', ' + STR(offset))
END SUB
```

**パラメーターと実行の説明:**

- Random(10) は 0..9 で、10 は出ません。Random(7,7) は必ず 7。Random(-2,2) は -2,-1,0,1,2 のいずれかです。各式は独立した選択です。
