# +, -, *, /, MOD

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

算術式は値を計算します。+ は加算、- は減算または符号反転、* は乗算、/ は除算、MOD は整数の余りです。結果を変数に代入するか RETURN で返して利用します。

## 正確な構文

```text
left + right
left - right
-right
left * right
left / right
left MOD right
(expression)
```

## パラメーター

- `left` — 左の数値オペランド。リテラル、宣言済み変数、括弧付き式、関数の結果を指定します。単項マイナスには左オペランドがありません。
- `right` — 右の数値オペランド。/ では除数です。MOD では Integer に変換した後も非ゼロである必要があります。例えば 0.5 は 0 に切り捨てられてエラーになります。
- `operator / precedence` — 優先順位は単項マイナス、同順位の * / MOD を左から右、二項 + - を左から右の順です。括弧で変更できます。単項プラス、累乗 ^、バックスラッシュによる整数除算は未対応です。

## 戻り値

整数の +、-、*、単項マイナスは Integer。数値オペランドに Decimal を含む場合は Decimal。/ は常に Decimal で、5/2=2.5。MOD は Integer です。計算された数値であり、成功やアイテム数を表すかどうかはスクリプトが決めます。

## 動作

- MOD は両オペランドを符号付き32ビット整数に変換し、表現可能な小数部分をゼロ方向へ切り捨てます。余りの符号は被除数と同じです。-17 MOD 5=-2、-2147483648 MOD -1=0。mOd のような大文字小文字の混在も使用できます。
- MOD のゼロ除算は TRY/CATCH で処理できるエラーになります。/ は浮動小数点除算で、非ゼロの分子をゼロで割ると符号付き Infinity、0/0 は NaN です。有限の値が必要なら除数を事前に確認してください。
- 整数の +、-、*、符号反転はオーバーフロー時に下位32ビットを保持し、自動で大きな整数型へ変わりません。近似が許される大きな計算では、先にオペランドを Decimal に変換できます。浮動小数点演算には二進数の丸め誤差があります。
- 通常の数値演算子は文字列を自動解析しません。String+String は連結し、String+Integer は失敗します。数値文字列には CDbl などを明示的に使用します。中置 MOD の整数文字列解析は、別の関数 BasicMod より厳密です。
- 評価器は式の順にオペランドを評価し、演算子トークンを選び InjectionValue を生成します。括弧内の式は先に完了します。オペランド自身が関連 API を呼ぶ場合を除き、移動、待機、ネットワーク要求は行いません。

## 使用例

### 1. 優先順位と括弧

```vb
# plain=2+3*4 は先に掛け算を行い 14 になります。grouped=(2+3)*4 は 20 です。Main は plain*100+grouped=1420 を返し、両方の計算を確認できます。
Option Explicit On
SUB Main()
    VAR plain = 2 + 3 * 4
    VAR grouped = (2 + 3) * 4
    RETURN plain * 100 + grouped
END SUB
```

**パラメーターと実行の説明:**

plain=2+3*4 は先に掛け算を行い 14 になります。grouped=(2+3)*4 は 20 です。Main は plain*100+grouped=1420 を返し、両方の計算を確認できます。

### 2. 完全なまとまりと残り

```vb
# DescribeBatches は total=27、size=5 を受け取ります。size がゼロ以下なら拒否します。Fix(total/size) は 5.4 を完全な5組に変換し、total mOd size は残り2個を返します。CStr で文字列 "5:2" を組み立てます。補助関数も全文を掲載しています。
Option Explicit On
FUNCTION DescribeBatches(total, size)
    IF size <= 0 THEN
        RETURN "invalid"
    END IF
    VAR whole = Fix(total / size)
    VAR remaining = total mOd size
    RETURN CStr(whole) + ":" + CStr(remaining)
END FUNCTION
SUB Main()
    RETURN DescribeBatches(27, 5)
END SUB
```

**パラメーターと実行の説明:**

DescribeBatches は total=27、size=5 を受け取ります。size がゼロ以下なら拒否します。Fix(total/size) は 5.4 を完全な5組に変換し、total mOd size は残り2個を返します。CStr で文字列 "5:2" を組み立てます。補助関数も全文を掲載しています。

### 3. 無効な除数の処理

```vb
# 10 MOD 0 は unusedResult への代入前にエラーになります。CATCH が problem に保存し、caught=TRUE を設定します。Main の戻り値1はこの例のエラー処理フラグであり、失敗した MOD の結果ではありません。
Option Explicit On
SUB Main()
    VAR caught = FALSE
    TRY
        VAR unusedResult = 10 MOD 0
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**パラメーターと実行の説明:**

10 MOD 0 は unusedResult への代入前にエラーになります。CATCH が problem に保存し、caught=TRUE を設定します。Main の戻り値1はこの例のエラー処理フラグであり、失敗した MOD の結果ではありません。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: signedOperand / additiveOperand / comparativeOperand
Runtime/Interpreter.cs: VisitSignedOperand / VisitAdditiveOperand / VisitComparativeOperand
Runtime/InjectionValue.cs: arithmetic operators
Runtime/NumberConversions.cs: ToInt
-->
