# String + / &

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

+ または Basic 互換の & で文字列を結合します。数量や座標などの数値は CStr で明示的に変換してからメッセージに追加します。

## 正確な構文

```text
leftText + rightText
leftText & rightText
"label" & CStr(number)
```

## パラメーター

- `leftText` — 左の文字列。リテラル、String 変数、文字列に変換した関数の結果です。
- `rightText` — 右の文字列。CStr(number) は数値を変換し、CStr(Unit) は空文字列です。空白やコロンなどの区切りは自分で指定します。

## 戻り値

両オペランドが String なら String です。成功フラグは返しません。このエンジンでは & を + に正規化して同じ規則を使います。数値同士なら加算され、2 & 3 は Integer 5 です。String と数値の混在はエラーで、VB の暗黙変換とは異なります。

## 動作

- 両側を順に評価して結合し、連鎖は左から処理します。数値計算は括弧で囲み、その結果を変換してから結合します。
- 区切り、空白、引用符、改行は自動追加されません。文字列リテラル内の & はそのままです。論理トークン && は AND のままで、文字列結合ではありません。
- CStr の数値書式はクライアント言語によらず、小数点はピリオドです。変換と結合は表示や送信をしません。必要なら結果の String を次の API 呼び出しに渡します。
- 文字列は不変で、結合は元の変数を変更せず新しい値を作ります。大きな文字列を何度も増やすと内容がコピーされるため、毎回レポート全体を作り直さず必要な出力だけ作ります。

## 使用例

### 1. 数量にラベルを付ける

```vb
# amount=50 は Integer。CStr(amount) は "50" です。"Items: " にコロンと末尾の空白を含みます。Main は "Items: 50" を返し、自動表示はしません。
Option Explicit On
SUB Main()
    VAR amount = 50
    RETURN "Items: " & CStr(amount)
END SUB
```

**パラメーターと実行の説明:**

amount=50 は Integer。CStr(amount) は "50" です。"Items: " にコロンと末尾の空白を含みます。Main は "Items: 50" を返し、自動表示はしません。

### 2. 再利用できる完全な関数

```vb
# Label は name="ore"、amount=3 を受け取り、名前、指定したコロン、CStr(amount) を結合します。全文掲載の関数は "ore:3" を Main に返し、他の名前や数量にも使えます。
Option Explicit On
FUNCTION Label(name, amount)
    RETURN name + ":" + CStr(amount)
END FUNCTION
SUB Main()
    RETURN Label("ore", 3)
END SUB
```

**パラメーターと実行の説明:**

Label は name="ore"、amount=3 を受け取り、名前、指定したコロン、CStr(amount) を結合します。全文掲載の関数は "ore:3" を Main に返し、他の名前や数量にも使えます。

### 3. 計算してから結合

```vb
# CStr(2+3) は先に5を計算して "5" に変換します。後のリテラルではセミコロン、空白、A&B を維持します。Main は "Total: 5; literal: A&B" を返します。
Option Explicit On
SUB Main()
    RETURN "Total: " & CStr(2 + 3) & "; literal: A&B"
END SUB
```

**パラメーターと実行の説明:**

CStr(2+3) は先に5を計算して "5" に変換します。後のリテラルではセミコロン、空白、A&B を維持します。Main は "Total: 5; literal: A&B" を返します。

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: ProtectLiteralText / ReplaceConcatenationOutsideLiterals
Runtime/InjectionValue.cs: operator + / explicit operator string
Runtime/InjectionApi.cs: CStr
-->
