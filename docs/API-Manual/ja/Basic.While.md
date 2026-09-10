# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

While は各反復の前に条件を検査し、真の間繰り返します。このエンジンでは Wend で閉じます。VB.NET の End While は対応していません。

## 正確な構文

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## パラメーター

- `condition` — 最初と最後を含む各検査で再評価する式。比較または数値 Boolean を使います。0/False で終了、1/True や他の非ゼロ数値で継続します。文字列は Boolean として解析しません。
- `statements` — 処理を行い、条件を変化させる本体の文。最初の検査が偽なら本体は一度も実行しません。
- `Wend / exit` — Wend は条件に戻ります。Continue While は再検査、Exit While は他種の内部ループを越えても最も近い While を終了します。Break は種類を問わず最も近いループを終了します。

## 戻り値

While、Wend、Exit While、Break に戻り値はありません。本体内の RETURN は手続き・関数全体を終了します。例は Integer 6、1、406 を返します。検索結果の 1 は配列インデックスで、成功の Boolean ではありません。

## 動作

- 検査、本体、検査への復帰の順です。数値境界の保存やカウンターの自動更新はしません。
- 進行は明示的に記述します。ゲーム状態を繰り返し確認する場合は適切な Wait と期限を設けます。While 自体は待機も時間切れも行いません。一時停止・停止は利用可能です。
- Continue や終了で離れる Try の Finally は実行されます。ヘッダー、各文、Wend は手続きまたは関数内の別々の行に記述します。

## 使用例

### 1. 各桁の合計

```vb
# DigitSum は number=123 を ByVal で受けます。MOD 10 で末尾の桁を読み、Fix(number/10) で除きます：123→12→1→0。total=3+2+1=6。最後の偽条件で終了して Main は 6 を受けます。入力 0 なら本体を飛ばして 0 を返します。
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**パラメーターと実行の説明:**

DigitSum は number=123 を ByVal で受けます。MOD 10 で末尾の桁を読み、Fix(number/10) で除きます：123→12→1→0。total=3+2+1=6。最後の偽条件で終了して Main は 6 を受けます。入力 0 なら本体を飛ばして 0 を返します。

### 2. 最初の一致を検索

```vb
# FirstAbove は values=[4,7,9] と threshold=6 を受けます。長さの検査が values[index] を保護します。index=1 で 7>6 となり found=1 を保存し Exit While で終了。一致しなければ -1 のままです。Main はゼロ始まりのインデックス 1 を返します。
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**パラメーターと実行の説明:**

FirstAbove は values=[4,7,9] と threshold=6 を受けます。長さの検査が values[index] を保護します。index=1 で 7>6 となり found=1 を保存し Exit While で終了。一致しなければ -1 のままです。Main はゼロ始まりのインデックス 1 を返します。

### 3. 条件の評価回数

```vb
# CanContinue は checks を ByRef、index と limit=3 を ByVal で受けます。checks を増やし index<limit を 1/0 で返します。index=0、1、2、3 で検査するので三反復に四呼び出しです。total=6、Main は 406 を返します。
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**パラメーターと実行の説明:**

CanContinue は checks を ByRef、index と limit=3 を ByVal で受けます。checks を増やし index<limit を 1/0 で返します。index=0、1、2、3 で検査するので三反復に四呼び出しです。total=6、Main は 406 を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
