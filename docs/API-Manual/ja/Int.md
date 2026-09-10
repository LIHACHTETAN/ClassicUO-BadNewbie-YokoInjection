# Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

Int(value) は Basic 数値を負の無限大方向へ切り下げます。

## 正確な構文

```text
Int(value:Any) -> Integer
```

## パラメーター

- `value` — 必須の引数は Integer/Decimal または数値文字列一つです。小数点は表示言語によらずドットです。不正な文字列、Array、Object、Unit は 0 に変換されるため、入力を IsNumeric で確認してください。

## 戻り値

Integer：floor(value)。例は 2.9 -> 2、-2.9 -> -3 です。丸めた値を符号付き Int32 の範囲に収め、非有限値や範囲外を渡さないでください。

## 動作

- どちらもゲームを問い合わせずローカルで計算します。引数の省略はエラーです。能力値は UO.Int()/UO.Str() で読み、Int()/Str() では読みません。Int は BasicDouble と Math.Floor、Str は種類に合う InternalSubrutines.Str と固定カルチャの書式を使います。

## 使用例

### Int — 1

```vb
# Int — 1
#
# Int(value) は Basic 数値を負の無限大方向へ切り下げます。
#
# Integer：floor(value)。例は 2.9 -> 2、-2.9 -> -3 です。丸めた値を符号付き Int32 の範囲に収め、非有限値や範囲外を渡さないでください。

SUB Main()
    # value=2.9。切り下げて Integer 2 となり、Main が返します。

    RETURN Int(2.9)
END SUB
```

**パラメーターと実行の説明:**

- value=2.9。切り下げて Integer 2 となり、Main が返します。

### Int — 2

```vb
# Int — 2
#
# Int(value) は Basic 数値を負の無限大方向へ切り下げます。
#
# Integer：floor(value)。例は 2.9 -> 2、-2.9 -> -3 です。丸めた値を符号付き Int32 の範囲に収め、非有限値や範囲外を渡さないでください。

SUB Main()
    # value=-2.9。切り下げは -3 で、ゼロ方向の切り捨てなら -2 です。Main は Integer -3 を返します。

    VAR value = -2.9
    RETURN Int(value)
END SUB
```

**パラメーターと実行の説明:**

- value=-2.9。切り下げは -3 で、ゼロ方向の切り捨てなら -2 です。Main は Integer -3 を返します。

### Int — 3

```vb
# Int — 3
#
# Int(value) は Basic 数値を負の無限大方向へ切り下げます。
#
# Integer：floor(value)。例は 2.9 -> 2、-2.9 -> -3 です。丸めた値を符号付き Int32 の範囲に収め、非有限値や範囲外を渡さないでください。

SUB Main()
    # WholeUnits は total=27、size=5 を受け取ります。size<=0 なら 0、そうでなければ Int(total/size) が 5.4 を切り下げます。Main
    # は完全な単位数 5 を返します。関数と二つの引数をすべて定義しています。

    RETURN WholeUnits(27,5)
END SUB

SUB WholeUnits(total,size)
    IF size <= 0 THEN
        RETURN 0
    END IF
    RETURN Int(total/size)
END SUB
```

**パラメーターと実行の説明:**

- WholeUnits は total=27、size=5 を受け取ります。size<=0 なら 0、そうでなければ Int(total/size) が 5.4 を切り下げます。Main は完全な単位数 5 を返します。関数と二つの引数をすべて定義しています。
