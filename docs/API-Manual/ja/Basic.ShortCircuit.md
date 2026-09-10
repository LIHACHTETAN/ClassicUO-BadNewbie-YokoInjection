# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

AndAlso と OrElse は不要な右オペランドを評価せずに条件を結合します。AndAlso は左が偽なら、OrElse は左が真なら右を省略します。配列アクセスの保護や不要な呼び出しの回避に使えます。

## 正確な構文

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## パラメーター

- `left` — left：最初に一回評価する式。Integer または Decimal のゼロは偽、ゼロ以外の数値は真です。
- `right` — right：必要な場合だけ一回評価する式。省略した配列の読み取り、関数呼び出し、副作用は発生しません。評価する値は数値に限ります。文字列は CBool で明示的に変換してください。

## 戻り値

元のオペランドではなく Integer 1（TRUE）か 0（FALSE）です。result=1 と result=TRUE、result=0 と result=FALSE を同様に使えます。このエンジンの真は 1 で、VB.NET の数値変換の -1 ではありません。普通の件数は件数のままで、この演算が真偽値を生成します。

## 動作

- 比較は各オペランド内で行います。AndAlso は OrElse より優先され、同じ演算子は左結合です。括弧で順序を変更できます。省略した式も解析され、Option Explicit の検査対象です。
- 互換性のため、連続する AND/OR/XOR はオペランド内で従来通り左から両側を評価してから AndAlso/OrElse を処理します。TRUE OR FALSE AndAlso FALSE は FALSE、TRUE OrElse FALSE AND FALSE は TRUE です。混在時は括弧を使ってください。AND、OR、&&、|| は両側を評価します。
- 左値を評価して数値としての真偽を判定し、真偽値を返すか必要な右側を評価します。必要な値のエラーは CATCH に渡り、FINALLY と一時停止・停止の確認も維持されます。呼び出しの省略はその処理自体も省略します。

## 使用例

### 1. 先頭要素を安全に調べる

```vb
# FirstEquals は items と expected を受けます。先に GetArrayLength(items)>0 を調べるため、空配列の items[0] は読みません。Main は [42] と空配列を渡して 1 と 0 を得て、10 を返します。補助関数は全文記載で、配列を変更しません。
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**パラメーターと実行の説明:**

FirstEquals は items と expected を受けます。先に GetArrayLength(items)>0 を調べるため、空配列の items[0] は読みません。Main は [42] と空配列を渡して 1 と 0 を得て、10 を返します。補助関数は全文記載で、配列を変更しません。

### 2. 代替呼び出しを一回だけ実行

```vb
# Probe は ByRef の calls を増やして TRUE を返します。TRUE OrElse Probe(calls) は省略し、FALSE OrElse Probe(calls) は一回呼び出します。両条件は 1 ですが、Main は実際の呼び出し数 1 を返します。
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**パラメーターと実行の説明:**

Probe は ByRef の calls を増やして TRUE を返します。TRUE OrElse Probe(calls) は省略し、FALSE OrElse Probe(calls) は一回呼び出します。両条件は 1 ですが、Main は実際の呼び出し数 1 を返します。

### 3. 除算保護と優先順位

```vb
# AverageExceeds(total, count, limit) は count>0 の場合のみ割り算します。(25,0,10) は 0、(25,2,10) は 12.5>10 なので 1 です。TRUE OrElse FALSE AndAlso FALSE は右側の AndAlso を省略して 1 です。Main は "0:1:1" を返します。
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**パラメーターと実行の説明:**

AverageExceeds(total, count, limit) は count>0 の場合のみ割り算します。(25,0,10) は 0、(25,2,10) は 12.5>10 なので 1 です。TRUE OrElse FALSE AndAlso FALSE は右側の AndAlso を省略して 1 です。Main は "0:1:1" を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
