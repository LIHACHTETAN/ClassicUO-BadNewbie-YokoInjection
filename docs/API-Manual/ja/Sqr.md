# Sqr

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

平方根を計算します。

## 正確な構文

```text
Sqr(number:Any) -> Decimal
```

## パラメーター

- `number` — 必須：Integer/Decimal、または小数点と任意の指数を持つ十進文字列（例 "-1.25e2"）。表示言語には依存しません。不正/16進文字列、Unit、Array、Object は0です。数値の16進リテラルは既に Integer です。NaN/Infinity もあり得ます。 入力 >=0 は非負の平方根。負は NaN、+Infinity は Infinity、NaN はそのままです。

## 戻り値

Decimal — sqrt(number). 入力 >=0 は非負の平方根。負は NaN、+Infinity は Infinity、NaN はそのままです。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

## 動作

- スクリプトスレッド内で計算し、サーバー要求、移動、ターゲット、待機、グローバル変数変更は行いません。
- Decimal は二進 Double で、.NET decimal ではありません。有限の近似値は許容誤差付きで比較します。NaN/Infinity を座標や数量に使わないでください。
- 入力 >=0 は非負の平方根。負は NaN、+Infinity は Infinity、NaN はそのままです。

### 内部関数：呼び出しから結果まで

実際の登録・変換段階です。完全な補助関数はスクリプトの数式を示し、プラットフォームの数学実装を置き換えません。

#### 1. Register

Register は一引数の BASIC 名をネイティブ計算に結び付け、変換後に System.Math を呼びます。隠れたスクリプトやサーバー手続きはありません。

Decimal — sqrt(number). 入力 >=0 は非負の平方根。負は NaN、+Infinity は Infinity、NaN はそのままです。 数値であり ID や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

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
# 平方根を計算します。
#
# Decimal — sqrt(number). 入力 >=0 は非負の平方根。負は NaN、+Infinity は Infinity、NaN はそのままです。 数値であり ID
# や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

SUB Main()
    # number = 25、期待値 5（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

    VAR value = Sqr(25)
    UO.Print(CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- number = 25、期待値 5（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

### 変数を使う別の入力

```vb
# 変数を使う別の入力
#
# 平方根を計算します。
#
# Decimal — sqrt(number). 入力 >=0 は非負の平方根。負は NaN、+Infinity は Infinity、NaN はそのままです。 数値であり ID
# や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

SUB Main()
    # number = 2、期待値 ~1.4142135623730951（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

    VAR inputValue = 2
    VAR value = Sqr(inputValue)
    UO.Print(CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- number = 2、期待値 ~1.4142135623730951（~ は近似）。value が結果を保存し、CStr は Print 用の表示に変換します。

### 完全な再利用可能な補助関数

```vb
# 完全な再利用可能な補助関数
#
# 平方根を計算します。
#
# Decimal — sqrt(number). 入力 >=0 は非負の平方根。負は NaN、+Infinity は Infinity、NaN はそのままです。 数値であり ID
# や成功フラグではありません。1/0 を成功/失敗と解釈しないでください。

# manual-check: scalar-math Sqr
SUB Main()
    # dx/dy は座標差。CDbl で sqrt(dx²+dy²)
    # 前の整数オーバーフローを防ぎます。SegmentLength(3,4)=5。ユークリッド距離で、経路や衝突判定ではありません。

    VAR value = SegmentLength(3,4)
    UO.Print(CStr(value))
END SUB

SUB SegmentLength(dx,dy)
    VAR x = CDbl(dx)
    VAR y = CDbl(dy)
    RETURN Sqr(x*x+y*y)
END SUB
```

**パラメーターと実行の説明:**

- dx/dy は座標差。CDbl で sqrt(dx²+dy²) 前の整数オーバーフローを防ぎます。SegmentLength(3,4)=5。ユークリッド距離で、経路や衝突判定ではありません。
