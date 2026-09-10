# Fix

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

小数部分をゼロ方向に切り捨てます。

## 正確な構文

```text
Fix(value:Any) -> Integer
```

## パラメーター

- `value` — 必須：Integer/Decimal、または小数点と任意の指数を持つ十進文字列（例 "-1.25e2"）。表示言語には依存しません。不正/16進文字列、Unit、Array、Object は0です。数値の16進リテラルは既に Integer です。NaN/Infinity もあり得ます。 有限入力で、切り捨て結果が -2147483648..2147483647 に収まる必要があります。-2.9 は-2で floor の-3とは異なります。範囲外/NaN/Infinity は無効です。

## 戻り値

Integer — truncate(value). 有限入力で、切り捨て結果が -2147483648..2147483647 に収まる必要があります。-2.9 は-2で floor の-3とは異なります。範囲外/NaN/Infinity は無効です。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

## 動作

- スクリプトスレッド内で計算し、サーバー要求、移動、ターゲット、待機、グローバル変数変更は行いません。
- Decimal は二進 Double で、.NET decimal ではありません。有限の近似値は許容誤差付きで比較します。NaN/Infinity を座標や数量に使わないでください。
- 有限入力で、切り捨て結果が -2147483648..2147483647 に収まる必要があります。-2.9 は-2で floor の-3とは異なります。範囲外/NaN/Infinity は無効です。

### 内部関数：呼び出しから結果まで

実際の登録・変換段階です。完全な補助関数はスクリプトの数式を示し、プラットフォームの数学実装を置き換えません。

#### 1. Register

Register は一引数の BASIC 名をネイティブ計算に結び付け、変換後に System.Math を呼びます。隠れたスクリプトやサーバー手続きはありません。

Integer — truncate(value). 有限入力で、切り捨て結果が -2147483648..2147483647 に収まる必要があります。-2.9 は-2で floor の-3とは異なります。範囲外/NaN/Infinity は無効です。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 関数 `Register`.

#### 2. BasicDouble

BasicDouble は Integer/Decimal を保持し、文字列を言語非依存の NumberStyles.Float で読み、他は0にします。Abs は通常の Integer を直接扱ってから Double に切り替えます。

必須：Integer/Decimal、または小数点と任意の指数を持つ十進文字列（例 "-1.25e2"）。表示言語には依存しません。不正/16進文字列、Unit、Array、Object は0です。数値の16進リテラルは既に Integer です。NaN/Infinity もあり得ます。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 関数 `BasicDouble`.

スクリプトスレッド内で計算し、サーバー要求、移動、ターゲット、待機、グローバル変数変更は行いません。


## 使用例

### 直接計算

```vb
# 直接計算
#
# 小数部分をゼロ方向に切り捨てます。
#
# Integer — truncate(value). 有限入力で、切り捨て結果が -2147483648..2147483647 に収まる必要があります。-2.9 は-2で floor
# の-3とは異なります。範囲外/NaN/Infinity は無効です。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

SUB Main()
    # value = 2.9、期待値 2（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

    VAR value = Fix(2.9)
    UO.Print(CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value = 2.9、期待値 2（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

### 変数を使う別の入力

```vb
# 変数を使う別の入力
#
# 小数部分をゼロ方向に切り捨てます。
#
# Integer — truncate(value). 有限入力で、切り捨て結果が -2147483648..2147483647 に収まる必要があります。-2.9 は-2で floor
# の-3とは異なります。範囲外/NaN/Infinity は無効です。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

SUB Main()
    # value = -2.9、期待値 -2（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

    VAR inputValue = -2.9
    VAR value = Fix(inputValue)
    UO.Print(CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value = -2.9、期待値 -2（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

### 完全な再利用可能な補助関数

```vb
# 完全な再利用可能な補助関数
#
# 小数部分をゼロ方向に切り捨てます。
#
# Integer — truncate(value). 有限入力で、切り捨て結果が -2147483648..2147483647 に収まる必要があります。-2.9 は-2で floor
# の-3とは異なります。範囲外/NaN/Infinity は無効です。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

# manual-check: scalar-math Fix
SUB Main()
    # total>=0、size>0 は完全な組数で27/5は5です。無効時の代替0は組数0でもあります。商は Integer 範囲内にします。

    VAR value = WholeBatches(27,5)
    UO.Print(CStr(value))
END SUB

SUB WholeBatches(total,size)
    IF total < 0 OR size <= 0 THEN
        RETURN 0
    END IF
    RETURN Fix(CDbl(total)/CDbl(size))
END SUB
```

**パラメーターと実行の説明:**

- total>=0、size>0 は完全な組数で27/5は5です。無効時の代替0は組数0でもあります。商は Integer 範囲内にします。
