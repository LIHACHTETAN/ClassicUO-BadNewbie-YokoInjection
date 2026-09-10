# 123 / 0x0EED / "text" / TRUE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

リテラルは値をコードに直接記述します。数値や引用文字列は宣言不要です。TRUE/FALSE は定義済み論理値です。引用符付きの数値は、明示的変換や宣言型の変換を行うまで文字列です。

## 正確な構文

```text
123
-2147483648
0x0EED
0xFFFFFFFF
2.5
"text"
'text'
TRUE
FALSE
```

## パラメーター

- `integer / hexadecimal` — 10進 Integer の範囲は -2147483648…2147483647。16進数は小文字の 0x と0–9/A–Fで記述します。32ビットを表すため 0xFFFFFFFF は Integer -1であり、正の64ビット数ではありません。
- `floating` — 小数点の両側に数字がある浮動小数点数、例2.5、-0.25。.5ではなく0.5と記述します。この文法ではコンマ、1e3の指数表記、数値リテラルの接尾辞は未対応です。
- `text` — 対応する単一または二重引用符で文字列を囲みます。内部に引用符を入れるには別の引用符か Chr(34)/Chr(39) を使います。逆斜線エスケープや引用符の二重化は解釈されません。例の文字列は1つの物理行に置いてください。
- `TRUE / FALSE` — TRUE は Integer 1、FALSE は Integer 0です。名前を再宣言しないでください。呼び出しではなく値なので TRUE() ではなく TRUE と書きます。

## 戻り値

整数/16進リテラルは Integer、小数点付き数値は Decimal（2進浮動小数点）、引用文字列は String です。TRUE/FALSE は Integer 1/0です。値の評価でゲーム操作や変数宣言は行いません。

## 動作

- -5 の符号は単項演算です。-2147483648 は正の絶対値を先に保存せず、最小の符号付き整数として扱います。範囲外の整数はエラーです。より大きな近似値が必要な計算では適切な浮動小数点を使います。
- 文字列は文字と大小文字を保持します。"350" は数値350ではなく、"false" は FALSE ではありません。# と ; は引用符内では文字、外ではコメントです。変換規則は AS と各関数の説明を参照してください。
- エンジンはトークンを認識し、カルチャに依存せず数値を解析するか文字列の外側の引用符を取り除きます。IDE の言語を変えてもコードの小数点は変わりません。
- serial、画像 type、座標はいずれも数値になり得ます。リテラルだけでは意味は決まらず、呼び出す API の引数仕様が用途を決めます。

## 使用例

### 1. 16進 type と整数境界

```vb
# itemType=0x0EED は10進3821です。lowest=-2147483648 は符号付きビット表現0x80000000と等しく、Main は itemType=3821を返します。アイテム検索は行いません。
Option Explicit On
SUB Main()
    VAR itemType = 0x0EED
    VAR lowest = -2147483648
    IF lowest = 0x80000000 THEN
        RETURN itemType
    END IF
    RETURN 0
END SUB
```

**パラメーターと実行の説明:**

itemType=0x0EED は10進3821です。lowest=-2147483648 は符号付きビット表現0x80000000と等しく、Main は itemType=3821を返します。アイテム検索は行いません。

### 2. 両方の引用符

```vb
# owner="O'Brien" はアポストロフィを含みます。instruction は二重引用符を含む文字列を単一引用符で囲みます。owner、" | "、instruction をつなぐと O'Brien | say "go" を返し、スクリプト内の逆斜線エスケープは不要です。
Option Explicit On
SUB Main()
    VAR owner = "O'Brien"
    VAR instruction = 'say "go"'
    RETURN owner + " | " + instruction
END SUB
```

**パラメーターと実行の説明:**

owner="O'Brien" はアポストロフィを含みます。instruction は二重引用符を含む文字列を単一引用符で囲みます。owner、" | "、instruction をつなぐと O'Brien | say "go" を返し、スクリプト内の逆斜線エスケープは不要です。

### 3. 数値である論理値

```vb
# enabled=TRUE は1、stopped=FALSE は0を保存します。計算は1*10+0=10です。Main は数値の計算結果を返し、標準の論理 TRUE ではありません。
Option Explicit On
SUB Main()
    VAR enabled = TRUE
    VAR stopped = FALSE
    RETURN enabled * 10 + stopped
END SUB
```

**パラメーターと実行の説明:**

enabled=TRUE は1、stopped=FALSE は0を保存します。計算は1*10+0=10です。Main は数値の計算結果を返し、標準の論理 TRUE ではありません。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: number / literal / HEX_NUMBER / DEC_NUMBER
Runtime/Interpreter.cs: VisitNumber / VisitLiteral / VisitSignedOperand
Runtime/InjectionApiUO.cs: TRUE / FALSE intrinsic values
-->
