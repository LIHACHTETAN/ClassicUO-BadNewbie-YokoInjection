# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

On Error は現在の手続き・関数で以後に発生する実行時エラーの扱いを選びます。API 呼び出しではなく言語文です。構造化した回復と後処理には Try/Catch/Finally を使います。

## 正確な構文

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## パラメーター

- `label` — 同じ手続き内に存在するラベルを label: と独立行で記述します。On Error より前後どちらでもよく、大文字小文字は区別しません。関数名、文字列、行番号ではありません。不明なラベルは SC009 となりクライアントが実行を止めます。
- `Resume Next / On Error` — On Error Resume Next はラベルに移らず失敗した命令の次へ自動的に進みます。成功した命令は変わりません。現在の手続き呼び出しだけに作用し、全スクリプトには作用しません。
- `0` — On Error GoTo 0 はモードを無効にします。ゼロは制御値であり、ラベルや Boolean の結果ではありません。他の数値ラベルや GoTo -1 は未対応です。
- `Resume / Resume Next` — ハンドラー内の Resume は失敗した命令を再試行し、Resume Next は次へ進みます。記録済みのエラーが必要で、遷移後にそのアドレスを消します。ラベルや時間制限を引数にしません。

## 戻り値

On Error と Resume に戻り値はありません。捕捉したエラーは TRUE/FALSE にならず、代入を自動修復もしません。例は Integer 5、18、10 を明示的に返します。それ以前の副作用は自動的には巻き戻しません。

## 動作

- 準備時に手続き全体を読んでからラベルを解決するため両方向に対応します。実行時はモードを保存し、例外では構造化 Try を先に、On Error を後に検討します。
- エンジンは失敗した命令のアドレスを記録します。ラベルモードはハンドラーへ、自動 Resume Next は命令の次へ進みます。Resume は式や呼び出しを再評価するため、原因を修正し副作用の繰り返しを考慮してください。
- GoTo 0 は保留中の失敗アドレスを消しません。ハンドラーで自身を無効化して修復後に Resume できます。失敗し得るハンドラー処理の前に無効化し、同じ処理への再進入を避けます。
- 構文エラーやキャンセルは回復しません。コマンドが例外を出さず 0、FALSE、失敗状態を返すだけなら On Error は呼ばれません。コマンドの結果を確認します。
- Return または GoTo で通常の流れがハンドラーへ入らないようにします。呼び出し先は独立した状態を持ち、未処理エラーは呼び出し元へ伝わります。その Resume は内部の一行ではなく呼び出し命令全体を再実行します。回数制限や待機は自動ではありません。

## 使用例

### 1. 失敗した代入を一つ飛ばす

```vb
# values[0] は一セルで、インデックス 5 は無効です。result=1。On Error Resume Next は代入前の失敗した読み取りを飛ばすので 1 のままです。GoTo 0 で無効化し result+=4 で 5。Main は 5 を返しますが、読み取り成功という意味ではありません。
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**パラメーターと実行の説明:**

values[0] は一セルで、インデックス 5 は無効です。result=1。On Error Resume Next は代入前の失敗した読み取りを飛ばすので 1 のままです。GoTo 0 で無効化し result+=4 で 5。Main は 5 を返しますが、読み取り成功という意味ではありません。

### 2. 修正して再試行

```vb
# ReadCell はセル 0 に 8 を格納しますが index=2 です。失敗して FixIndex へ進みます。GoTo 0 で無効化、handled=1、index=0。Resume が result=values[index] を繰り返して 8 を格納します。Return で通常のハンドラー到達を防ぎ、Main は 18 を受けます。
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**パラメーターと実行の説明:**

ReadCell はセル 0 に 8 を格納しますが index=2 です。失敗して FixIndex へ進みます。GoTo 0 で無効化、handled=1、index=0。Resume が result=values[index] を繰り返して 8 を格納します。Return で通常のハンドラー到達を防ぎ、Main は 18 を受けます。

### 3. 登録より前にあるハンドラー

```vb
# 通常の入口は GoTo Work で Failed を飛ばします。On Error GoTo Failed が前のラベルを有効化します。インデックス 2 は result を変える前に失敗。ハンドラーは自身を無効化し handled を増やして Resume Next で Return へ進みます。結果 10。ラベルは独立した手続きではありません。
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**パラメーターと実行の説明:**

通常の入口は GoTo Work で Failed を飛ばします。On Error GoTo Failed が前のラベルを有効化します。インデックス 2 は result を変える前に失敗。ハンドラーは自身を無効化し handled を増やして Resume Next で Return へ進みます。結果 10。ラベルは独立した手続きではありません。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
