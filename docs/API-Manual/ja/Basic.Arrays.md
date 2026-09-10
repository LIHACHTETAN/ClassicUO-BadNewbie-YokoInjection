# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

DIM は動的配列を作り、REDIM はその格納領域を置き換えます。PRESERVE は重なる添字の値をコピーします。各次元は要素数ではなく、含まれる上限を指定します。読む前に要素を初期化してください。

## 正確な構文

```text
DIM name[upper]
DIM name(upper) AS type
DIM grid[xUpper][yUpper]
DIM grid(xUpper, yUpper)
REDIM name[upper]
REDIM PRESERVE name[upper]
name[index] = value
GetArrayLength(name)
```

## パラメーター

- `name` — name：配列変数。DIM は宣言し、REDIM は既存変数の格納先を置き換えます。要素の読み書きには items[i]、grid[x][y] を使います。
- `upper` — upper：Integer に変換する式。左から右へ各一回評価します。DIM items[2] は 0..2 の三要素を作ります。-1 は空の次元です。それ未満や長さのオーバーフローはエラーです。実用上の大きさはメモリにも制限されます。
- `PRESERVE` — PRESERVE：REDIM の省略可能な指定。重なる添字を再帰的にコピーし、縮小時には新しい範囲外の値を失います。省略すると要素は未初期化です。
- `AS type` — AS type：DIM 配列宣言で受け付ける注記ですが、要素の型指定・初期化・変換は行いません。異なる種類の値を格納できます。

## 戻り値

DIM と REDIM は値を返しません（Unit）。items[i] は格納値を実際の種類 Integer、Decimal、String、Array、Object で返します。未初期化要素の読み取りはエラーになり、0 や FALSE にはなりません。GetArrayLength(array) は外側の長さを Integer で返し、配列以外なら 0 です。

## 動作

- DIM grid(1, 2) は grid[1][2]、つまり二行・各三要素です。境界内の関数呼び出しは維持されます。アクセスは grid[1][2] のままです。式内の丸括弧は関数呼び出しを意味します。
- 代入と ByVal 渡しは要素ではなく参照をコピーします。別名から共通要素の変更が見えます。REDIM は新配列に結び直し、別名は古い配列を保持します。PRESERVE は入れ子の配列の重なる座標をコピーし、任意のオブジェクトを完全に複製するものではありません。
- 添字はゼロ始まりのみです。DIM items[2]=5 などの DIM/REDIM 初期化式は SC014 で拒否されるため、各要素を別の行で設定します。不正な添字、存在しない要素、未初期化の読み取りは捕捉可能なエラーです。
- この Basic 方言の動的な要素種類と多次元 PRESERVE は VB.NET の型付き配列とは異なります。格納した真偽値は 1/0 ですが、一般の数値や配列長は成功フラグではありません。
- RETURN array は配列の参照を返し、作成した関数の終了後もデータは有効です。別の変数への代入は要素をコピーしません。共通関数で Module フィールド用の配列を作れます。独立した実行では DIM を実行するたびに新しい配列を作ります。

## 使用例

### 1. 初期化した要素の合計

```vb
# Abs(-2) は上限 2 を返し、Main は三要素に 2、4、6 を設定します。Sum は参照を ByVal で受け、0..GetArrayLength(items)-1 を巡回して 12 を返します。補助関数は全文記載で、要素を変更せず空配列にも対応します。
Option Explicit On
FUNCTION Sum(ByVal items)
    VAR total = 0
    VAR i = 0
    FOR i = 0 TO GetArrayLength(items) - 1
        total += items[i]
    NEXT
    RETURN total
END FUNCTION
SUB Main()
    DIM items(Abs(-2))
    items[0] = 2
    items[1] = 4
    items[2] = 6
    RETURN Sum(items)
END SUB
```

**パラメーターと実行の説明:**

Abs(-2) は上限 2 を返し、Main は三要素に 2、4、6 を設定します。Sum は参照を ByVal で受け、0..GetArrayLength(items)-1 を巡回して 12 を返します。補助関数は全文記載で、要素を変更せず空配列にも対応します。

### 2. 値を保って拡張

```vb
# values は 7 と 8 を保持します。REDIM PRESERVE values(2) は三要素を作り、添字 0、1 をコピーします。新要素 2 は 9 に初期化します。Main は 7*100+8*10+9=789 を返します。
Option Explicit On
SUB Main()
    DIM values[1]
    values[0] = 7
    values[1] = 8
    REDIM PRESERVE values(2)
    values[2] = 9
    RETURN values[0] * 100 + values[1] * 10 + values[2]
END SUB
```

**パラメーターと実行の説明:**

values は 7 と 8 を保持します。REDIM PRESERVE values(2) は三要素を作り、添字 0、1 をコピーします。新要素 2 は 9 に初期化します。Main は 7*100+8*10+9=789 を返します。

### 3. 別名と新領域を確認

```vb
# grid は二行・各二要素です。alias は同じ配列なので alias[0][1]=9 は grid も変更します。PRESERVE は grid を三行に拡張し 9 を保持しますが、alias は二行のままです。"9:3:2" は保持値、新しい外側の長さ、古い別名の長さです。
Option Explicit On
SUB Main()
    DIM grid[1][1]
    grid[0][1] = 4
    VAR alias = grid
    alias[0][1] = 9
    REDIM PRESERVE grid[2][1]
    RETURN CStr(grid[0][1]) + ":" + CStr(GetArrayLength(grid)) + ":" + CStr(GetArrayLength(alias))
END SUB
```

**パラメーターと実行の説明:**

grid は二行・各二要素です。alias は同じ配列なので alias[0][1]=9 は grid も変更します。PRESERVE は grid を三行に拡張し 9 を保持しますが、alias は二行のままです。"9:3:2" は保持値、新しい外側の長さ、古い別名の長さです。

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
