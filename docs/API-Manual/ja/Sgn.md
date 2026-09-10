# Sgn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

数値の符号を返します。

## 正確な構文

```text
Sgn(value:Any) -> Integer
```

## パラメーター

- `value` — 必須：Integer/Decimal、または小数点と任意の指数を持つ十進文字列（例 "-1.25e2"）。表示言語には依存しません。不正/16進文字列、Unit、Array、Object は0です。数値の16進リテラルは既に Integer です。NaN/Infinity もあり得ます。 負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。

## 戻り値

Integer — sign(value). 負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

## 動作

- スクリプトスレッド内で計算し、サーバー要求、移動、ターゲット、待機、グローバル変数変更は行いません。
- Decimal は二進 Double で、.NET decimal ではありません。有限の近似値は許容誤差付きで比較します。NaN/Infinity を座標や数量に使わないでください。
- 負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。

### 内部関数：呼び出しから結果まで

実際の登録・変換段階です。完全な補助関数はスクリプトの数式を示し、プラットフォームの数学実装を置き換えません。

#### 1. Register

Register は一引数の BASIC 名をネイティブ計算に結び付け、変換後に System.Math を呼びます。隠れたスクリプトやサーバー手続きはありません。

Integer — sign(value). 負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 関数 `Register`.

#### 2. BasicDouble

BasicDouble は Integer/Decimal を保持し、文字列を言語非依存の NumberStyles.Float で読み、他は0にします。Abs は通常の Integer を直接扱ってから Double に切り替えます。

必須：Integer/Decimal、または小数点と任意の指数を持つ十進文字列（例 "-1.25e2"）。表示言語には依存しません。不正/16進文字列、Unit、Array、Object は0です。数値の16進リテラルは既に Integer です。NaN/Infinity もあり得ます。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 関数 `BasicDouble`.

#### 3. BasicSgn

負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。

Integer — sign(value). 負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; 関数 `BasicSgn`.

スクリプトスレッド内で計算し、サーバー要求、移動、ターゲット、待機、グローバル変数変更は行いません。


## 使用例

### 直接計算

```vb
# 直接計算
#
# 数値の符号を返します。
#
# Integer — sign(value). 負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。 数値であり ID や成功フラグではありません。1/0
# を成功/失敗と解釈しないでください。

SUB Main()
    # value = -8、期待値 -1（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

    VAR value = Sgn(-8)
    UO.Print(CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value = -8、期待値 -1（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

### 変数を使う別の入力

```vb
# 変数を使う別の入力
#
# 数値の符号を返します。
#
# Integer — sign(value). 負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。 数値であり ID や成功フラグではありません。1/0
# を成功/失敗と解釈しないでください。

SUB Main()
    # value = 10-10、期待値 0（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

    VAR inputValue = 10-10
    VAR value = Sgn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value = 10-10、期待値 0（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

### 完全な再利用可能な補助関数

```vb
# 完全な再利用可能な補助関数
#
# 数値の符号を返します。
#
# Integer — sign(value). 負なら-1、ゼロなら0、正なら+1。NaN は数学エラー、無限大はその符号です。 数値であり ID や成功フラグではありません。1/0
# を成功/失敗と解釈しないでください。

# manual-check: scalar-math Sgn
SUB Main()
    # current/destination は一軸の位置。StepToward は -1/0/1 で、八方向コードや移動ではありません。

    VAR value = StepToward(12,10)
    UO.Print(CStr(value))
END SUB

SUB StepToward(current,destination)
    RETURN Sgn(CDbl(destination)-CDbl(current))
END SUB
```

**パラメーターと実行の説明:**

- current/destination は一軸の位置。StepToward は -1/0/1 で、八方向コードや移動ではありません。
