# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

Str(value) は Basic のスカラー値を文字列に整形します。

## 正確な構文

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## パラメーター

- `value` — 必須の Integer、Decimal、String を一つ渡します。実際の種類でオーバーロードを選択します。Array、Object、Unit に対応する Str はありません。

## 戻り値

String：言語に依存しない数値文字列、または変更されない元の String。正数の前に空白は付きません。桁数の引数はありません。

## 動作

- どちらもゲームを問い合わせずローカルで計算します。引数の省略はエラーです。能力値は UO.Int()/UO.Str() で読み、Int()/Str() では読みません。Int は BasicDouble と Math.Floor、Str は種類に合う InternalSubrutines.Str と固定カルチャの書式を使います。

## 使用例

### Str — 1

```vb
# Str — 1
#
# Str(value) は Basic のスカラー値を文字列に整形します。
#
# String：言語に依存しない数値文字列、または変更されない元の String。正数の前に空白は付きません。桁数の引数はありません。

SUB Main()
    # value=42 は Integer です。Str は先頭空白のない "42" を作り、Main がこの String を返します。

    RETURN Str(42)
END SUB
```

**パラメーターと実行の説明:**

- value=42 は Integer です。Str は先頭空白のない "42" を作り、Main がこの String を返します。

### Str — 2

```vb
# Str — 2
#
# Str(value) は Basic のスカラー値を文字列に整形します。
#
# String：言語に依存しない数値文字列、または変更されない元の String。正数の前に空白は付きません。桁数の引数はありません。

SUB Main()
    # amount=-12.5 は Decimal です。表示言語に関係なく Str はドット付きの "-12.5" を text に保存します。Main は text を返し、amount
    # は数値のままです。

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**パラメーターと実行の説明:**

- amount=-12.5 は Decimal です。表示言語に関係なく Str はドット付きの "-12.5" を text に保存します。Main は text を返し、amount は数値のままです。

### Str — 3

```vb
# Str — 3
#
# Str(value) は Basic のスカラー値を文字列に整形します。
#
# String：言語に依存しない数値文字列、または変更されない元の String。正数の前に空白は付きません。桁数の引数はありません。

SUB Main()
    # ItemLabel は name="ore"、count=3 を受け取ります。Str(name) は名前を保ち、Str(count) は "3" を作ります。関数が " x"
    # で結合し、Main は "ore x3" を返します。

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**パラメーターと実行の説明:**

- ItemLabel は name="ore"、count=3 を受け取ります。Str(name) は名前を保ち、Str(count) は "3" を作ります。関数が " x" で結合し、Main は "ore x3" を返します。
